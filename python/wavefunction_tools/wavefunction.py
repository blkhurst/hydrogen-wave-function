import numpy as np
import numpy.typing as npt
from typing import Literal

from .radial_wave_function import radial_distribution, radial_wave_function
from .spherical_harmonic import spherical_harmonic, spherical_harmonic_real
from .utilities import cartesian_to_spherical


Axis = Literal["x", "y", "z"]
Plane = Literal["xy", "xz", "yz"]
Basis = Literal["complex", "real"]


def wavefunction(
    n: int,
    l: int,
    m: int,
    r: npt.ArrayLike,
    theta: npt.ArrayLike,
    phi: npt.ArrayLike,
    basis: Basis = "complex",
) -> tuple[np.ndarray, np.ndarray]:
    """Hydrogen wave function psi_{nlm}(r,theta,phi)."""
    r = np.asarray(r, dtype=float)
    theta = np.asarray(theta, dtype=float)
    phi = np.asarray(phi, dtype=float)

    R = radial_wave_function(n, l, r)

    if basis == "real":
        Y_re = spherical_harmonic_real(l, m, theta, phi)
        real = R * Y_re
        imag = np.zeros_like(real)
        return real, imag

    Y_re, Y_im = spherical_harmonic(l, m, theta, phi)
    real = R * Y_re
    imag = R * Y_im

    return real, imag


def wavefunction_cartesian(
    n: int,
    l: int,
    m: int,
    x: npt.ArrayLike,
    y: npt.ArrayLike,
    z: npt.ArrayLike,
    basis: Basis = "complex",
) -> tuple[np.ndarray, np.ndarray]:
    """Hydrogen wave function psi_{nlm}(x,y,z)."""
    r, theta, phi = cartesian_to_spherical(x, y, z)
    return wavefunction(n, l, m, r, theta, phi, basis=basis)


def wavefunction_slice_cartesian(
    n: int,
    l: int,
    m: int,
    plane: Plane,
    u: npt.ArrayLike,
    v: npt.ArrayLike,
    basis: Basis = "complex",
) -> tuple[np.ndarray, np.ndarray]:
    """Hydrogen wave function psi_{nlm}(x,y,z) on a 2D plane."""
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)

    x, y, z = _plane_to_xyz(plane, u, v)
    return wavefunction_cartesian(n, l, m, x, y, z, basis=basis)


def wavefunction_line_cartesian(
    n: int,
    l: int,
    m: int,
    axis: Axis,
    u: npt.ArrayLike,
    basis: Basis = "complex",
) -> tuple[np.ndarray, np.ndarray]:
    """Hydrogen wave function psi_{nlm}(x,y,z) on a 1D line."""
    u = np.asarray(u, dtype=float)
    x, y, z = _axis_to_xyz(axis, u)
    return wavefunction_cartesian(n, l, m, x, y, z, basis=basis)


def radial_axis(n: int, l: int, tail: float = 1e-3) -> float:
    """Approximate radius containing (1 - tail) probability."""
    r = np.linspace(0.0, 100.0 * n * n, 20000)  # ? Arbitrary conservative max radius
    P = radial_distribution(n, l, r)
    dr = r[1] - r[0]
    cdf = np.cumsum(P) * dr
    cdf /= cdf[-1]
    return float(r[np.searchsorted(cdf, 1.0 - tail)])


def _plane_to_xyz(
    plane: Plane, u: npt.ArrayLike, v: npt.ArrayLike, offset: float = 0.0
):
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
    return x, y, z


def _axis_to_xyz(axis: Axis, u: npt.ArrayLike, offset: float = 0.0):
    if axis == "x":
        x = u
        y = np.full_like(x, offset, dtype=float)
        z = np.full_like(x, offset, dtype=float)
    elif axis == "y":
        y = u
        x = np.full_like(y, offset, dtype=float)
        z = np.full_like(y, offset, dtype=float)
    elif axis == "z":
        z = u
        x = np.full_like(z, offset, dtype=float)
        y = np.full_like(z, offset, dtype=float)
    else:
        raise ValueError("axis must be one of: 'x', 'y', 'z'")
    return x, y, z
