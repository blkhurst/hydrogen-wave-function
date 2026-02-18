"""
Superposition Heatmap (2D)
- Note that for performance in Python, we precompute all orbitals using the same axis_limits.
  This is required since superposing two wavefunctions must be done on the same coordinate grid.
- In C++, to support fixed-resolution auto-scaling, we keep the texture size constant, but evaluate
  both orbitals per-frame with an updated shared axis_limits (normalised texture coords -> axis_limits).
"""

import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from wavefunction_tools.utilities import complex_multiply
from wavefunction_tools import (
    radial_axis,
    wavefunction_slice_cartesian,
    time_dependent_factor,
    superpose_wavefunctions,
    complex_phase,
    complex_magnitude,
    complex_magnitude_squared,
)


def ramp01(t: float, travel: float, pause: float) -> tuple[int, float]:
    seg_len = pause + travel
    seg_idx = int(t // seg_len)
    local = t - seg_idx * seg_len
    if local < pause:
        return seg_idx, 0.0
    f = (local - pause) / travel
    return seg_idx, float(np.clip(f, 0.0, 1.0))


def display_normalise(x: np.ndarray, gamma: float = 1.0) -> np.ndarray:
    x = x / (x.max() + 1e-30)
    return np.clip(x, 0.0, 1.0) ** gamma


def main():
    plane = "yz"  # "xy", "xz", "yz"
    resolution = 700
    magnitude_squared = False  # if True, display |psi|^2 instead of |psi|
    gamma = 1.0  # Display normalisation gamma

    time_dependent = True
    time_scale = 0.5
    mix_factor = 0.5  # [0,1] Only used if time_dependent is False

    travel = 1.2
    pause = 0.8

    states = [
        (1, 0, 0),
        (2, 1, 0),
        (3, 2, 0),
        (4, 3, 0),
        (3, 2, 0),
        (2, 1, 0),
        (1, 0, 0),
    ]

    # Create grid
    axis_limit = max(radial_axis(n, l) for (n, l, _m) in states)
    u = np.linspace(-axis_limit, axis_limit, resolution)
    v = np.linspace(-axis_limit, axis_limit, resolution)
    u_grid, v_grid = np.meshgrid(u, v, indexing="xy")

    # Precompute orbitals
    orbitals: list[tuple[np.ndarray, np.ndarray]] = []
    for n, l, m in states:
        re, im = wavefunction_slice_cartesian(
            n, l, m, plane, u_grid, v_grid, basis="complex"
        )
        orbitals.append((re, im))

    # Initial frame
    re0, im0 = orbitals[0]
    magnitude0 = (
        complex_magnitude_squared(re0, im0)
        if magnitude_squared
        else complex_magnitude(re0, im0)
    )
    magnitude0 = display_normalise(magnitude0, gamma=gamma)
    phase0 = complex_phase(re0, im0)

    # Setup graph
    plt.style.use("bmh")
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(16, 7))
    extent = (-axis_limit, axis_limit, -axis_limit, axis_limit)

    im_magnitude = ax0.imshow(magnitude0, extent=extent, origin="lower", cmap="magma")
    ax0.set_title(r"$|\Psi|^2$" if magnitude_squared else r"$|\Psi|$")
    ax0.set_xlabel(plane[0])
    ax0.set_ylabel(plane[1])
    ax0.set_aspect("equal", adjustable="box")
    ax0.grid(False)
    cbar0 = fig.colorbar(im_magnitude, ax=ax0, fraction=0.046, pad=0.04)
    cbar0.set_label(ax0.get_title())

    im_phase = ax1.imshow(
        phase0,
        extent=extent,
        origin="lower",
        cmap="twilight",
        vmin=-np.pi,
        vmax=np.pi,
    )
    ax1.set_title(r"phase $\arg(\Psi)$")
    ax1.set_xlabel(plane[0])
    ax1.set_ylabel(plane[1])
    ax1.set_aspect("equal", adjustable="box")
    ax1.grid(False)
    cbar1 = fig.colorbar(im_phase, ax=ax1, fraction=0.046, pad=0.04)
    cbar1.set_label("radians")

    title = fig.suptitle("", fontsize=14)
    fig.tight_layout()

    start = time.time()

    def animate(_i: int):
        t = (time.time() - start) * time_scale

        # Compute superposition coefficients
        seg, s = ramp01(t, travel=travel, pause=pause)
        k = seg % (len(states) - 1)

        # Time-dependence
        (n1, l1, m1) = states[k]
        (n2, l2, m2) = states[k + 1]
        factor = t if time_dependent else mix_factor
        td1 = time_dependent_factor(n1, factor)
        td2 = time_dependent_factor(n2, factor)
        psi1 = complex_multiply(orbitals[k], td1)
        psi2 = complex_multiply(orbitals[k + 1], td2)

        # Superpose
        re, im = superpose_wavefunctions(psi1, psi2, s)
        magnitude = (
            complex_magnitude_squared(re, im)
            if magnitude_squared
            else complex_magnitude(re, im)
        )
        magnitude = display_normalise(magnitude, gamma=gamma)
        phase = complex_phase(re, im)

        # Update graphs
        im_magnitude.set_data(magnitude)
        im_phase.set_data(phase)

        title.set_text(
            rf"{plane}-plane: $(n,l,m)=({n1},{l1},{m1}) \to ({n2},{l2},{m2})$   "
            rf"$s={s:.2f}$"
        )

    _ani = animation.FuncAnimation(
        fig,
        animate,
        interval=1000 / 60,
        cache_frame_data=False,
    )
    plt.show()


if __name__ == "__main__":
    main()
