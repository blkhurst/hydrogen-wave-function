from .utilities import factorial_ratio, a0, Z
from .laguerre import associated_laguerre_polynomial

import numpy as np
import numpy.typing as npt


def radial_wave_function(n: int, l: int, r: npt.ArrayLike) -> np.ndarray:
    """Radial wave function R_{nl}(r)"""
    r = np.asarray(r, dtype=float)

    if n <= 0:
        raise ValueError("n must be a non-negative integer.")
    if l < 0 or l >= n:
        raise ValueError("Require 0 <= l <= n-1.")

    root_term1 = ((2 * Z) / (n * a0)) ** 3
    root_term2 = factorial_ratio(n - l - 1, n + l) / (2 * n)
    # rootTerm2 = factorial(n - l - 1) / (2 * n * factorial(n + l))
    normalisation = np.sqrt(root_term1 * root_term2)

    rho = (2 * Z * r) / (n * a0)
    exponential = np.exp(-rho / 2.0)
    laguerre = associated_laguerre_polynomial(n - l - 1, 2 * l + 1, rho)

    return normalisation * exponential * rho**l * laguerre


def radial_distribution(n: int, l: int, r: npt.ArrayLike) -> np.ndarray:
    """Radial probability density P_{nl}(r) assuming ∫|Y_l^m|^2 dΩ = 1"""
    r = np.asarray(r, dtype=float)
    R = radial_wave_function(n, l, r)
    return (r**2) * (R**2)

    # If spherical harmonics are normalised so ∫|Y_l^m|^2 dΩ = 4π
    # return 4 * np.pi * (r**2) * (R**2)
