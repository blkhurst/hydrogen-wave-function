import numpy as np
import numpy.typing as npt


def time_dependent_factor(n: float, time: float, hbar: float = 1.0) -> complex:
    """Calculate the time-dependent factor for a given principal quantum number n and time."""
    energy = -(13.6 / (n**2))
    exponent = -energy * time / hbar
    e_real = np.cos(exponent)
    e_imag = np.sin(exponent)
    return e_real + 1j * e_imag


def superpose_wavefunctions(
    psi1: tuple[npt.ArrayLike, npt.ArrayLike],
    psi2: tuple[npt.ArrayLike, npt.ArrayLike],
    factor: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Superpose two wavefunctions using factor [0,1]."""
    theta = 0.5 * np.pi * factor  # Map factor [0,1] to angle [0, pi/2]
    alpha = np.cos(theta)
    beta = np.sin(theta)

    re1, im1 = psi1
    re2, im2 = psi2

    re = alpha * np.asarray(re1, dtype=float) + beta * np.asarray(re2, dtype=float)
    im = alpha * np.asarray(im1, dtype=float) + beta * np.asarray(im2, dtype=float)
    return re, im


# psi_1 = wavefunction(1, 0, 0, 0, 0, 0) * time_dependent_factor(1, time)
# psi_2 = wavefunction(2, 1, 0, 0, 0, 0) * time_dependent_factor(2, time)
# psi_superposition = superpose_wavefunctions(psi_1, psi_2, factor)
