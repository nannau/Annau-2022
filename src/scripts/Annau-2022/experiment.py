from generator import Generator
from critic import Critic

from dataclasses import dataclass
from typing import Tuple

import mlflow
import torch

@dataclass
class SRModelRun:
    """Class for defining attributes of GAN model runs saved in MLFlow"""
    region: str
    sr_config: str
    exp_id: str
    parent_path: str
    generator_param_dim: Tuple[int, int, int, int] = (16, 128, 7, 2)
    critic_param_dim: Tuple[int, int, int] = (16, 128, 2)


    def _check_cuda_available(self):
        if not torch.cuda.is_available():
            raise AssertionError("CUDA not available")

    def load_generator(self):
        self._check_cuda_available()
        G = Generator(*self.generator_param_dim).cuda()
        return self._load_state_dict("Generator", G)

    def load_critic(self):
        self._check_cuda_available()
        C = Critic(*self.critic_param_dim).cuda()
        return self._load_state_dict("Critic", C)

    def _load_state_dict(self, model_name, model_class):
        state_dict = mlflow.pytorch.load_state_dict(
            self.parent_path + self.exp_id + "/" + model_name
        )
        model_class.load_state_dict(state_dict)
        return model_class
