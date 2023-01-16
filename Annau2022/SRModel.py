from Annau2022.models.generator import Generator
from typing import Tuple, Optional

import pydantic
import mlflow
import torch
import json


class SRModelData(pydantic.BaseModel):
    """Class for defining attributes of GAN model runs saved in MLFlow"""
    region: str
    sr_model_name: str
    exp_id: str
    parent_path: str = "/workspace/Annau2022/models/store/"
    data_path: str = "/workspace/Annau2022/data/"
    generator_param_dim: Tuple[int, int, int, int] = (16, 128, 7, 2)
    device: str = "cuda" if torch.cuda.is_available() else "cpu"

    @pydantic.validator("generator_param_dim")
    @classmethod
    def check_generator_param_dim(cls, v):
        if len(v) != 4:
            raise ValueError("Generator param dim must be a tuple of length 4")
        return v

    def load_test(self) -> Tuple[torch.Tensor, torch.Tensor]:
        return self._read_pt('lr_test_'), self._read_pt('hr_test_')

    def load_train(self) -> Tuple[torch.Tensor, torch.Tensor]:
        return self._read_pt('lr_train_'), self._read_pt('hr_train_')

    def _read_pt(self, prefix) -> Tuple[torch.Tensor, torch.Tensor]:
        """Loads train and test tensors from disk. The compatible
        dimensions are
        lr: (batch_size, 7, 16, 16)
        hr: (batch_size, 2, 128, 128)
        """
        return torch.load(f"{self.data_path}{prefix}{self.region}.pt").to(
            self.device
        )

    def load_generator(self) -> Generator:
        G = Generator(*self.generator_param_dim).to(self.device)
        return self._load_state_dict("Generator", G)

    def _load_state_dict(self, model_name, model_class) -> torch.nn.Module:
        state_dict = mlflow.pytorch.load_state_dict(
            f"{self.parent_path}{self.exp_id}/{model_name}/{model_name}_999"
        )
        model_class.load_state_dict(state_dict)
        return model_class


class GeneratorInputMismatchError(Exception):
    """Custom error for when the input tensor to the generator is the wrong shape"""
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(self.message)


class SuperResolver(pydantic.BaseModel):
    """Class for super resolving data once a model has been trained"""
    region: str
    lr: torch.Tensor
    hr: torch.Tensor
    model: torch.nn.Module
    batch_size: int = 1
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    stats_path = "/workspace/Annau2022/data/stats.json"


    @pydantic.root_validator(pre=True)
    @classmethod
    def check_lr_shape(cls, values):
        coarse_dim = values["model"].coarse_dim
        nc = values["model"].nc

        if len(values["lr"].shape) != 4:
            raise ValueError("Input tensor must have shape batch_size, nc, coarse_dim_x, coarse_dim_y")

        batch_size, nc_tensor, coarse_dim_x, coarse_dim_y = values["lr"].shape

        if (nc_tensor, coarse_dim_x, coarse_dim_y) != (nc, coarse_dim, coarse_dim):
            raise GeneratorInputMismatchError(
                value=values["lr"],
                message=f"Input tensor contains dimensions need to match Generator of {nc, coarse_dim, coarse_dim} but received {nc_tensor, coarse_dim_x, coarse_dim_y} must have shape batch_size, nc, coarse_dim_x, coarse_dim_y"
            )

        return values

    def load_stats_json(self) -> torch.Tensor:
        """Loads the mean and std from the stats.json file and normalises the input tensor"""
        with open(self.stats_path, 'r') as f:
            stats = json.load(f)
        return stats

    def denormalise(self, x: torch.Tensor, stats: dict) -> torch.Tensor:
        """Denormalizes input tensor to reverse mean 0, std 1
        """
        x[:, 0, ...] = x[:, 0, ...]*stats[self.region]["std"]["u10"] + stats[self.region]["mean"]["u10"]
        x[:, 1, ...] = x[:, 1, ...]*stats[self.region]["std"]["v10"] + stats[self.region]["mean"]["v10"]

        return x

    def super_resolve(self) -> torch.Tensor:
        """Super resolves the input tensor using the model and denormalizes it"""
        stats = self.load_stats_json()

        dataset = torch.utils.data.TensorDataset(self.lr)
        loader = torch.utils.data.DataLoader(dataset, self.batch_size, shuffle=False)

        for batch_idx, lr_batch in enumerate(loader):
            yield self.denormalise(self.model(lr_batch[0]), stats)

    def ground_truth(self) -> torch.Tensor:
        """Super resolves the input tensor using the model and denormalizes it"""
        stats = self.load_stats_json()

        dataset = torch.utils.data.TensorDataset(self.hr)
        loader = torch.utils.data.DataLoader(dataset, self.batch_size, shuffle=False)

        for batch_idx, hr_batch in enumerate(loader):
            yield self.denormalise(hr_batch[0], stats)

    class Config:
        arbitrary_types_allowed = True
