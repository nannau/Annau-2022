import torch
import numpy as np
import pytorch_msssim


def compute_mae(x, y):
    return torch.mean(torch.abs(x - y))


def mean_stats(x, y, f):
    sx = torch.hypot(x[:, 0, ...], x[:, 1, ...])
    sy = torch.hypot(y[:, 0, ...], y[:, 1, ...])

    sx = f(sx)
    sy = f(sy)

    return torch.mean(sx - sy)


def median_symmetric_accuracy(x, y):
    return 100*(np.exp(np.median(np.abs(np.log(y/x))))-1)


def _standardize_zero_one(x):
    return (x - torch.min(x)) / (torch.max(x) - torch.min(x))


def compute_ms_ssim(x, y):
    for i in range(x.shape[1]):
        x[:, i, ...] = _standardize_zero_one(x[:, i, ...])
        y[:, i, ...] = _standardize_zero_one(y[:, i, ...])

    return pytorch_msssim.msssim(x, y, window_size=7)
