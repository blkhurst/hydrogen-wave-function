import numpy as np
import numpy.typing as npt

from .wavefunction import Basis, wavefunction_slice_cartesian, radial_axis


def sample_orbital_plane(
    n: int,
    l: int,
    m: int,
    num_samples: int = 10000,
    plane: str = "xy",  # xy, xz, yz
    axis_limit: float | None = None,
    axis_resolution: int = 1024,
    add_jitter: bool = True,
    basis: Basis = "complex",
) -> tuple[np.ndarray, np.ndarray, tuple[np.ndarray, np.ndarray]]:
    """Inverse-transform sample - XY, XZ, or YZ plane."""

    if axis_limit is None:
        axis_limit = radial_axis(n, l)

    # Plane PDA & CDA
    x_grid, y_grid, pda, cda = build_plane_pda_cda(
        n, l, m, plane, axis_limit, axis_resolution, basis
    )

    # Sample Radial
    xy_indices = sample_cdf(cda, num_samples)

    x_indices = xy_indices // axis_resolution
    y_indices = xy_indices % axis_resolution

    x_samples = x_grid[x_indices]
    y_samples = y_grid[y_indices]

    # Add Jitter using half cell size
    if add_jitter == True:
        rng = np.random.default_rng()
        dx = x_grid[1] - x_grid[0]
        dy = y_grid[1] - y_grid[0]
        x_samples += (rng.random(num_samples) - 0.5) * dx
        y_samples += (rng.random(num_samples) - 0.5) * dy
        # Clamp?

    # Re-evaluate psi at sampled points
    psi = wavefunction_slice_cartesian(
        n, l, m, plane, x_samples, y_samples, basis=basis
    )

    return x_samples, y_samples, psi


def build_plane_pda_cda(
    n: int,
    l: int,
    m: int,
    plane: str,
    axis_limit: float,
    axis_resolution: int,
    basis: Basis,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Build plane probability density array and cumulative distribution array."""

    if plane not in ("xy", "xz", "yz"):
        raise ValueError("plane must be one of: 'xy', 'xz', 'yz'")

    # Build grid
    x_grid = np.linspace(-axis_limit, axis_limit, axis_resolution)
    y_grid = np.linspace(-axis_limit, axis_limit, axis_resolution)
    x_mesh, y_mesh = np.meshgrid(x_grid, y_grid, indexing="ij")

    # Compute PDA (no Jacobian required since plane is Cartesian) #? Should I discrete re-normalise?
    re, im = wavefunction_slice_cartesian(n, l, m, plane, x_mesh, y_mesh, basis=basis)
    pda = re**2 + im**2

    # Compute CDA
    flattened_pda = pda.ravel()
    cda = np.cumsum(flattened_pda)
    if cda[-1] == 0.0:
        raise ValueError("All-zero density on this plane/range.")
    cda /= cda[-1]

    return x_grid, y_grid, pda, cda


def sample_cdf(cdf: npt.ArrayLike, num_samples: int) -> np.ndarray:
    """Sample from a CDF using inverse transform sampling."""
    rng = np.random.default_rng()
    u = rng.uniform(0.0, 1.0, size=num_samples)
    index = np.searchsorted(cdf, u, side="left")
    return np.minimum(index, len(cdf) - 1)  # Clamp
