from .utilities import condon_shortley_phase_factor as cspf, factorial_ratio
from .legendre import associated_legendre_polynomial

import numpy as np
import numpy.typing as npt


def spherical_harmonic(
    l: int, m: int, theta: npt.ArrayLike, phi: npt.ArrayLike
) -> tuple[np.ndarray, np.ndarray]:
    """Spherical Harmonic Y_l^m(\\theta, \\phi) using Condon-Shortley convention in P_l^m."""
    theta = np.asarray(theta, dtype=float)
    phi = np.asarray(phi, dtype=float)

    if m < 0:
        mp = -m
        re, im = spherical_harmonic(l, mp, theta, phi)
        sign = cspf(mp)
        return sign * re, -sign * im  # conjugate

    root_term1 = (2 * l + 1) / (4 * np.pi)
    root_term2 = factorial_ratio(l - m, l + m)
    # rootTerm2 = factorial(l - m) / factorial(l + m)
    normalisation = np.sqrt(root_term1 * root_term2)

    legendre = associated_legendre_polynomial(l, m, np.cos(theta))

    complex_exponent = m * phi
    complex_exponential_real = np.cos(complex_exponent)
    complex_exponential_imag = np.sin(complex_exponent)

    re = normalisation * legendre * complex_exponential_real
    im = normalisation * legendre * complex_exponential_imag
    return re, im


def spherical_harmonic_real(
    l: int, m: int, theta: npt.ArrayLike, phi: npt.ArrayLike
) -> np.ndarray:
    """Real-form spherical harmonic Y_{lm}^real, as a real linear combination of +-m"""
    theta = np.asarray(theta, dtype=float)
    phi = np.asarray(phi, dtype=float)

    mp = abs(m)
    phase = cspf(mp)
    re, im = spherical_harmonic(l, mp, theta, phi)

    if m == 0:
        return re
    if m < 0:
        return np.sqrt(2.0) * phase * im
    return np.sqrt(2.0) * phase * re
