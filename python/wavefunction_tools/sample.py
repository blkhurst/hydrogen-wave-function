"""Built to accept scalar or array inputs"""

import numpy as np
import numpy.typing as npt

from .radial_wave_function import radial_distribution
from .spherical_harmonic import spherical_harmonic
from .wavefunction import wavefunction, radial_axis


def sample_orbital(
    n: int,
    l: int,
    m: int,
    num_samples: int = 10000,
    r_max: float | None = None,
    resolution_r: int = 4096,
    resolution_theta: int = 256,
    resolution_phi: int = 512,
    add_jitter: bool = False,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, tuple[np.ndarray, np.ndarray]]:
    """Inverse-transform sample - Separate radial and angular parts."""

    if r_max is None:
        r_max = radial_axis(n, l)

    # Radial PDA & CDA
    r_grid, pda_r, cda_r = build_radial_pda_cda(n, l, r_max, resolution_r)

    # Angular PDA & CDA
    theta_grid, phi_grid, pda_omega, cda_omega = build_angular_pda_cda(
        l, m, resolution_theta, resolution_phi
    )

    # Sample Radial
    r_indices = sample_cdf(cda_r, num_samples)
    r_samples = r_grid[r_indices]

    # Sample Angular (Unflattening index assumes row-major order)
    omega_indices = sample_cdf(cda_omega, num_samples)

    theta_indices = omega_indices // resolution_phi
    phi_indices = omega_indices % resolution_phi

    theta_samples = theta_grid[theta_indices]
    phi_samples = phi_grid[phi_indices]

    # Add Jitter using half cell size
    if add_jitter:
        rng = np.random.default_rng()

        dr = float(r_grid[1] - r_grid[0])
        dtheta = float(theta_grid[1] - theta_grid[0])
        dphi = float(phi_grid[1] - phi_grid[0])

        r_samples += (rng.random(num_samples) - 0.5) * dr
        theta_samples += (rng.random(num_samples) - 0.5) * dtheta
        phi_samples += (rng.random(num_samples) - 0.5) * dphi

        # Clamp to valid range
        r_samples = np.clip(r_samples, 0.0, r_max)
        theta_samples = np.clip(theta_samples, 0.0, np.pi)
        phi_samples = np.mod(phi_samples, 2.0 * np.pi)

    # Re-evaluate psi at sampled points
    psi = wavefunction(n, l, m, r_samples, theta_samples, phi_samples)

    return r_samples, theta_samples, phi_samples, psi


def build_radial_pda_cda(
    n: int, l: int, r_max: float, r_resolution: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Build radial probability density array and cumulative distribution array."""

    # Build grid
    r_grid = np.linspace(0.0, r_max, r_resolution)

    # Compute PDA (includes r^2 factor) #? Should I discrete re-normalise?
    pda = radial_distribution(n, l, r_grid)

    # Compute CDA
    cda = np.cumsum(pda)
    cda /= cda[-1]

    return r_grid, pda, cda


def build_angular_pda_cda(
    l: int, m: int, theta_resolution: int, phi_resolution: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Build angular probability density array and cumulative distribution array."""

    # Build grids
    theta_grid = np.linspace(0.0, np.pi, theta_resolution)  # [0, pi]
    phi_grid = np.linspace(0.0, 2.0 * np.pi, phi_resolution, endpoint=False)  # [0, 2pi)
    theta_mesh, phi_mesh = np.meshgrid(theta_grid, phi_grid, indexing="ij")

    # Compute PDA
    Y_re, Y_im = spherical_harmonic(l, m, theta_mesh, phi_mesh)
    pda = Y_re**2 + Y_im**2
    pda *= np.sin(theta_mesh)  # Jacobian factor

    # Compute CDA (flattened using row-major order)
    cda = np.cumsum(pda.flatten())
    cda /= cda[-1]

    return theta_grid, phi_grid, pda, cda


def sample_cdf(cdf: npt.ArrayLike, num_samples: int) -> np.ndarray:
    """Sample from a CDF using inverse transform sampling."""
    rng = np.random.default_rng()
    u = rng.uniform(0.0, 1.0, size=num_samples)
    index = np.searchsorted(cdf, u, side="left")
    return np.minimum(index, len(cdf) - 1)  # Clamp
