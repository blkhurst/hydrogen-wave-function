from .utilities import alternating_sign, binomial

import numpy as np
import numpy.typing as npt
from math import factorial


def _associated_laguerre_sum_binomial(
    n: int, alpha: float, x: npt.ArrayLike
) -> np.ndarray:
    """
    Generalized Laguerre L_n^alpha(x) using Generalized Binomial Coefficient C(alpha, k) (alpha may be non-integer).
    Good as a reference for small n; prefer the recurrence for larger n to avoid numerical issues.
    """
    x = np.asarray(x, dtype=float)
    summation = np.zeros_like(x)
    for i in range(0, n + 1):
        cspf = alternating_sign(i)
        binomial1 = binomial(n + alpha, n - i)
        term1 = x**i / factorial(i)
        summation += cspf * binomial1 * term1
    return summation


def _associated_laguerre_sum_factorial(n: int, k: int, x: npt.ArrayLike) -> np.ndarray:
    """Associated Laguerre L_n^k(x) using factorial form (k must be non-negative integer)."""
    x = np.asarray(x, dtype=float)
    summation = np.zeros_like(x)
    for m in range(0, n + 1):
        cspf = alternating_sign(m)
        binomial1 = factorial(n + k) / (
            factorial(n - m) * factorial(k + m) * factorial(m)
        )
        term1 = x**m
        summation += cspf * binomial1 * term1
    return summation


def associated_laguerre_polynomial(n: int, k: int, x: npt.ArrayLike) -> np.ndarray:
    """Associated Laguerre L_n^k(x) using recurrence relation."""
    x = np.asarray(x, dtype=float)

    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return 1 + k - x

    L_n_minus_2 = np.ones_like(x)
    L_n_minus_1 = 1 + k - x

    L_n = np.zeros_like(x)
    for current_n in range(2, n + 1):
        L_n = (
            (2 * current_n - 1 + k - x) * L_n_minus_1
            - (current_n + k - 1) * L_n_minus_2
        ) / (current_n)
        L_n_minus_2 = L_n_minus_1
        L_n_minus_1 = L_n
    return L_n


def laguerre_derivative(n: int, k: int, x: npt.ArrayLike) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    return -associated_laguerre_polynomial(n - 1, k + 1, x)
