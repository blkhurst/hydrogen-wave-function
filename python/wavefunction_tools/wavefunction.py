import numpy as np
import numpy.typing as npt

from .radial_wave_function import radial_distribution, radial_wave_function
from .spherical_harmonic import spherical_harmonic
from .utilities import cartesian_to_spherical


def wavefunction(
    n: int, l: int, m: int, r: npt.ArrayLike, theta: npt.ArrayLike, phi: npt.ArrayLike
) -> tuple[np.ndarray, np.ndarray]:
    """Hydrogen wave function psi_{nlm}(r,theta,phi)."""
    r = np.asarray(r, dtype=float)
    theta = np.asarray(theta, dtype=float)
    phi = np.asarray(phi, dtype=float)

    R = radial_wave_function(n, l, r)
    Y_re, Y_im = spherical_harmonic(l, m, theta, phi)

    real = R * Y_re
    imag = R * Y_im

    return real, imag


def wavefunction_cartesian(
    n: int, l: int, m: int, x: npt.ArrayLike, y: npt.ArrayLike, z: npt.ArrayLike
) -> tuple[np.ndarray, np.ndarray]:
    """Hydrogen wave function psi_{nlm}(x,y,z)."""
    r, theta, phi = cartesian_to_spherical(x, y, z)
    return wavefunction(n, l, m, r, theta, phi)


def wavefunction_slice_cartesian(
    n: int,
    l: int,
    m: int,
    plane: str,
    u: npt.ArrayLike,
    v: npt.ArrayLike,
) -> tuple[np.ndarray, np.ndarray]:
    """Hydrogen wave function psi_{nlm}(x,y,z) on a 2D plane."""

    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)

    offset = 0.0
    if plane == "xy":
        x, y = u, v
        z = np.full_like(x, offset, dtype=float)
    elif plane == "xz":
        x, z = u, v
        y = np.full_like(x, offset, dtype=float)
    elif plane == "yz":
        y, z = u, v
        x = np.full_like(y, offset, dtype=float)
    else:
        raise ValueError("plane must be one of: 'xy', 'xz', 'yz'")

    r, theta, phi = cartesian_to_spherical(x, y, z)
    return wavefunction(n, l, m, r, theta, phi)


def radial_axis(n: int, l: int, tail: float = 1e-3) -> float:
    """Approximate radius containing (1 - tail) probability."""
    r = np.linspace(0.0, 100.0 * n * n, 20000)  # ? Arbitrary conservative max radius
    P = radial_distribution(n, l, r)
    dr = r[1] - r[0]
    cdf = np.cumsum(P) * dr
    cdf /= cdf[-1]
    return float(r[np.searchsorted(cdf, 1.0 - tail)])


def probability_density(re: npt.ArrayLike, im: npt.ArrayLike) -> np.ndarray:
    """Return |psi|^2 from real/imag parts."""
    re = np.asarray(re, dtype=float)
    im = np.asarray(im, dtype=float)
    return re * re + im * im
