import numpy as np


Z = 1
a0 = 1


def alternating_sign(exponent: int) -> int:
    """Return (-1)^m for integer m."""
    # return pow((-1), exponent)
    return 1 if (exponent % 2 == 0) else -1


def condon_shortley_phase_factor(m: int) -> int:
    """Condon-Shortley phase factor: (-1)^m."""
    return alternating_sign(m)


def factorial_ratio(a: int, b: int) -> float:
    """Return a!/b! for integers 0<=a<=b using a product (avoids factorials)."""
    if a < 0 or b < 0 or a > b:
        raise ValueError("Require 0 <= a <= b")
    prod = 1.0
    for k in range(a + 1, b + 1):
        prod /= k
    return prod


def binomial(n: float, k: int) -> float:
    """
    Generalized Binomial Coefficient - Multiplicative Formula
    C(n, k) for real n and integer k >= 0
    """
    product = 1
    for i in range(1, k + 1):
        product *= (n + 1 - i) / i
    return product


def spherical_to_cartesian(
    r: np.ndarray, theta: np.ndarray, phi: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Convert spherical (r,theta,phi) to Cartesian (x,y,z)."""
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z


def cartesian_to_spherical(
    x: np.ndarray, y: np.ndarray, z: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Convert Cartesian (x,y,z) to Spherical (r,theta,phi)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    z = np.asarray(z, dtype=float)

    r = np.sqrt(x * x + y * y + z * z)
    safe_r = np.where(r == 0.0, 1.0, r)

    theta = np.arccos(np.clip(z / safe_r, -1.0, 1.0))  # [0, pi]
    phi = np.arctan2(y, x)  # (-pi, pi]
    phi = np.where(phi < 0.0, phi + 2.0 * np.pi, phi)  # [0, 2pi)

    return r, theta, phi


def complex_phase(re: npt.ArrayLike, im: npt.ArrayLike, deg=False) -> np.ndarray:
    """Return the phase (angle) of a complex number in radians."""
    # return np.angle(re + 1j * im)
    re = np.asarray(re, dtype=float)
    im = np.asarray(im, dtype=float)
    angle = np.arctan2(im, re)
    if deg:
        angle *= 180.0 / np.pi
    return angle


def complex_magnitude(re: npt.ArrayLike, im: npt.ArrayLike) -> np.ndarray:
    """Return the magnitude of a complex number."""
    re = np.asarray(re, dtype=float)
    im = np.asarray(im, dtype=float)
    return np.sqrt(re**2 + im**2)


def complex_magnitude_squared(re: npt.ArrayLike, im: npt.ArrayLike) -> np.ndarray:
    """Return |psi|^2 from real/imag parts."""
    re = np.asarray(re, dtype=float)
    im = np.asarray(im, dtype=float)
    return re * re + im * im
