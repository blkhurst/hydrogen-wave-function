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
    u_grid, v_grid, pda, cda = build_plane_pda_cda(
        n, l, m, plane, axis_limit, axis_resolution, basis
    )

    # Sample Plane
    uv_indices = sample_cdf(cda, num_samples)

    u_indices = uv_indices // axis_resolution
    v_indices = uv_indices % axis_resolution

    u_samples = u_grid[u_indices]
    v_samples = v_grid[v_indices]

    # Add Jitter using half cell size
    if add_jitter:
        rng = np.random.default_rng()
        du = u_grid[1] - u_grid[0]
        dv = v_grid[1] - v_grid[0]
        u_samples += (rng.random(num_samples) - 0.5) * du
        v_samples += (rng.random(num_samples) - 0.5) * dv
        # Clamp?

    # Re-evaluate psi at sampled points
    psi = wavefunction_slice_cartesian(
        n, l, m, plane, u_samples, v_samples, basis=basis
    )

    return u_samples, v_samples, psi


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
    u_grid = np.linspace(-axis_limit, axis_limit, axis_resolution)
    v_grid = np.linspace(-axis_limit, axis_limit, axis_resolution)
    u_mesh, v_mesh = np.meshgrid(u_grid, v_grid, indexing="ij")

    # Compute PDA (no Jacobian required since plane is Cartesian) #? Should I discrete re-normalise?
    re, im = wavefunction_slice_cartesian(n, l, m, plane, u_mesh, v_mesh, basis=basis)
    pda = re**2 + im**2

    # TODO: Revisit
    # Guard against near-zero density (e.g. nodal planes)
    du = float(u_grid[1] - u_grid[0])
    dv = float(v_grid[1] - v_grid[0])
    mass = float(pda.sum()) * du * dv  # approx $\int\int |psi|^2 dudv$ on this plane
    if mass < 1e-12:
        raise ValueError("Near-zero probability density (e.g. nodal plane).")

    flat = pda.ravel()
    cda = np.cumsum(flat)
    cda /= cda[-1]

    return u_grid, v_grid, pda, cda


def sample_cdf(cdf: npt.ArrayLike, num_samples: int) -> np.ndarray:
    """Sample from a CDF using inverse transform sampling."""
    rng = np.random.default_rng()
    u = rng.uniform(0.0, 1.0, size=num_samples)
    index = np.searchsorted(cdf, u, side="left")
    return np.minimum(index, len(cdf) - 1)  # Clamp
