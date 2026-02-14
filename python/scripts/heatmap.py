import numpy as np
import matplotlib.pyplot as plt

from wavefunction_tools import (
    radial_axis,
    wavefunction_slice_cartesian,
    complex_phase,
    complex_magnitude,
    complex_magnitude_squared,
)


def main() -> None:
    n, l, m = 3, 1, -1
    plane = "yz"  # "xy", "xz", "yz"
    resolution = 1000  # per axis
    magnitude_squared = False  # if True, display |psi|^2 instead of |psi|

    axis_limit = radial_axis(n, l)
    u = np.linspace(-axis_limit, axis_limit, resolution)
    v = np.linspace(-axis_limit, axis_limit, resolution)
    u_grid, v_grid = np.meshgrid(u, v, indexing="xy")

    re, im = wavefunction_slice_cartesian(n, l, m, plane, u_grid, v_grid)
    magnitude = (
        complex_magnitude_squared(re, im)
        if magnitude_squared
        else complex_magnitude(re, im)
    )
    phase = complex_phase(re, im)

    plt.style.use("bmh")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    im1 = ax1.imshow(
        magnitude,  # ? Should display normalise by dividing by psi_max
        extent=(-axis_limit, axis_limit, -axis_limit, axis_limit),
        cmap="twilight",
    )
    ax1.set_aspect("equal", adjustable="box")
    ax1.set_title(
        r"$|\psi_{%s,%s,%s}|%s$ on %s-plane"
        % (n, l, m, "^2" if magnitude_squared else "", plane)
    )
    ax1.set_xlabel(f"{plane[0]}")
    ax1.set_ylabel(f"{plane[1]}")
    cbar1 = fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)
    cbar1.set_label(r"$|\psi|^2$" if magnitude_squared else r"$|\psi|$")

    im2 = ax2.imshow(
        phase,
        extent=(-axis_limit, axis_limit, -axis_limit, axis_limit),
        cmap="twilight_shifted",
        vmin=-np.pi,
        vmax=np.pi,
    )
    ax2.set_title(r"$\arg(\psi)$ (phase) on %s-plane" % (plane))
    ax2.set_aspect("equal", adjustable="box")
    ax2.set_xlabel(f"{plane[0]}")
    ax2.set_ylabel(f"{plane[1]}")
    cbar2 = fig.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)
    cbar2.set_label("phase (rad)")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
