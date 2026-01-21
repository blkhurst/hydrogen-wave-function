from .utilities import condon_shortley_phase_factor as cspf, factorial_ratio
from .utilities import binomial

import numpy as np
import numpy.typing as npt
from math import factorial


def double_factorial(n: int) -> int:
    """Compute n!! for integer n."""
    if n <= 0:
        return 1
    product = 1
    for k in range(n, 0, -2):
        product *= k
    return product


def associated_legendre_polynomial(l: int, m: int, x: npt.ArrayLike) -> np.ndarray:
    """
    Associated Legendre polynomial P_l^m(x) of degree l and order m, using recurrence relation.
    Includes the Condon-Shortley phase factor.
    """
    x = np.asarray(x, dtype=float)
    if l < 0:
        raise ValueError("Degree l must be non-negative integer.")
    if abs(m) > l:
        return np.zeros_like(x, dtype=float)

    if m < 0:
        mp = -m
        sign = cspf(mp)
        factor = factorial_ratio(l - mp, l + mp)
        # factor = factorial(l - mp) / factorial(l + mp)
        return sign * factor * associated_legendre_polynomial(l, mp, x)

    P_mm = cspf(m) * double_factorial(2 * m - 1) * (1 - x**2) ** (m / 2)
    if l == m:
        return P_mm

    P_m_plus_1_m = x * (2 * m + 1) * P_mm
    if l == m + 1:
        return P_m_plus_1_m

    P_lm_minus_2 = P_mm
    P_lm_minus_1 = P_m_plus_1_m
    P_lm = np.zeros_like(x, dtype=float)
    for current_l in range(m + 2, l + 1):
        P_lm = (
            x * (2 * current_l - 1) * P_lm_minus_1 - (current_l + m - 1) * P_lm_minus_2
        ) / (current_l - m)
        P_lm_minus_2 = P_lm_minus_1
        P_lm_minus_1 = P_lm

    return P_lm


def _associated_legendre_sum(l: int, m: int, x: npt.ArrayLike) -> np.ndarray:
    """Associated Legendre polynomial P_l^m(x) using explicit summation formula (for reference)."""
    x = np.asarray(x, dtype=float)

    if abs(m) > l:
        return np.zeros_like(x, dtype=float)

    if m < 0:
        mp = -m
        factor = factorial_ratio(l - mp, l + mp)
        # factor = factorial(l - mp) / factorial(l + mp)
        return cspf(mp) * factor * _associated_legendre_sum(l, mp, x)

    summation = np.zeros_like(x, dtype=float)
    for k in range(m, l + 1):
        term1 = factorial(k) / factorial(k - m)
        term2 = x ** (k - m)
        binomial1 = binomial(l, k)
        binomial2 = binomial((l + k - 1) / 2.0, l)  # Requires Generalized Binomial Form
        summation += term1 * term2 * binomial1 * binomial2

    return cspf(m) * 2**l * (1 - x**2) ** (m / 2) * summation
