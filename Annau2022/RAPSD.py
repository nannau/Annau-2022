from typing import Generator

import numpy as np
import scipy.stats as stats


"""This module contains functions that calculate the
radially averaged power spectral density (RASPD)
"""


def calculate_2dft(image: np.ndarray) -> np.ndarray:
    """Computes the fourier transform and returns the amplitudes"""
    fourier_image = np.fft.fftn(image)
    # fourier_image = torch.fft.fftn(image)
    fourier_amplitudes = np.abs(fourier_image)**2
    # fourier_amplitudes = torch.abs(fourier_image)**2

    return fourier_amplitudes.flatten()


def define_wavenumers(hr_dim: int) -> np.ndarray:
    """Defines the wavenumbers for the RASPD"""
    kfreq = np.fft.fftfreq(hr_dim)*hr_dim
    kfreq2D = np.meshgrid(kfreq, kfreq)
    knrm = np.sqrt(kfreq2D[0]**2 + kfreq2D[1]**2)
    return knrm.flatten()


def compute_rapsd(hr_field: Generator, var_ref: dict = None) -> np.ndarray:
    """Computes the RASPD for a given super-resolution model"""

    if var_ref is None:
        var_ref = {"u10": 0, "v10": 1}

    var_rapsd = {}
    [var_rapsd.setdefault(x, []) for x in var_ref]

    for x in hr_field:
        for var_name, var_idx in var_ref.items():

            knrm = define_wavenumers(x.shape[-1])
            # Bins to average the spectra over
            kbins = np.arange(0.5, x.shape[-1]//2+1, 1.)
            # "Interpolate" at the bin centers
            kvals = 0.5 * (kbins[1:] + kbins[:-1])
            wind_2d = calculate_2dft(x[var_idx, ...].cpu().detach().numpy())

            # This ends up compute the radial average
            average_bins, _, _ = stats.binned_statistic(
                knrm, wind_2d, statistic="mean", bins=kbins
                )

            # Weight by the surface area in radial average bin
            average_bins *= np.pi * (kbins[1:]**2 - kbins[:-1]**2)
            # Add to a list -- each element is a RASPD
            var_rapsd[var_name].append(average_bins)

    var_rapsd_avg = {"k": kvals}
    for var_name in var_ref:
        var_rapsd_avg[var_name] = np.mean(
            np.array(var_rapsd[var_name]),
            axis=0
        )

    return var_rapsd_avg
