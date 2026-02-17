"""
Dot Density Plot
- Density of samples represents probability density $|psi|^2$
- Color represents either phase $arg(psi)$ or sign of real part (positive/negative)
- Alpha also represents probability density, with gamma scaling to enhance visibility of low-density regions
"""

import numpy as np
import matplotlib.pyplot as plt

from wavefunction_tools import (
    complex_phase,
    complex_magnitude_squared,
    radial_axis,
    sample_orbital_plane,
)


def phase_colouring(psi: complex, gamma: float = 0.1) -> np.ndarray:
    phase = complex_phase(psi.real, psi.imag)  # [-pi, pi]
    magnitude_squared = complex_magnitude_squared(psi.real, psi.imag)
    magnitude_squared /= magnitude_squared.max() + 1e-30  # Display Normalise
    alpha = magnitude_squared**gamma
    alpha = np.clip(alpha, 0.0, 1.0)
    return phase, alpha


def sign_colouring(psi: complex, gamma: float = 0.1) -> np.ndarray:
    magnitude_squared = complex_magnitude_squared(psi.real, psi.imag)
    magnitude_squared /= magnitude_squared.max() + 1e-30  # Display Normalise
    alpha = np.abs(magnitude_squared) ** gamma
    alpha = np.clip(alpha, 0.0, 1.0)

    sign = np.sign(psi.real)
    col_pos = np.array([1.0, 0.8, 0.2, 1.0])
    col_neg = np.array([0.8, 0.8, 0.8, 1.0])
    rgba = np.repeat(col_neg[None, :], psi.size, axis=0)
    rgba[sign >= 0] = col_pos
    rgba[:, 3] = alpha

    return rgba, alpha


def main():
    n, l, m = 3, 1, -1
    plane = "yz"  # "xy", "xz", "yz"
    num_samples = 50_000
    point_size = 1  # 0.2
    axis_resolution = 4000  # PDA/CDA resolution per axis
    axis_limit = radial_axis(n, l)
    use_phase_colouring = False

    # Sample points
    u, v, (psi_re, psi_im) = sample_orbital_plane(
        n=n,
        l=l,
        m=m,
        num_samples=num_samples,
        plane=plane,
        axis_limit=axis_limit,
        axis_resolution=axis_resolution,
        add_jitter=False,
    )

    # Color
    if use_phase_colouring:
        color, alpha = phase_colouring(psi_re + 1j * psi_im, gamma=0.1)
    else:
        color, alpha = sign_colouring(psi_re + 1j * psi_im, gamma=0.1)

    # Plot
    plt.style.use("dark_background")  # bmh
    fig, ax = plt.subplots(figsize=(8, 8))

    sc = ax.scatter(
        u,
        v,
        c=color,
        cmap="twilight",
        s=point_size,
        alpha=alpha,
        linewidths=0,
    )

    axis_labels = {"xy": ("x", "y"), "xz": ("x", "z"), "yz": ("y", "z")}
    a, b = axis_labels.get(plane, ("u", "v"))

    ax.set_title(rf"Dot Density: $(n,l,m)=({n},{l},{m})$ on {plane}-plane")
    ax.set_xlabel(a)
    ax.set_ylabel(b)
    ax.set_aspect("equal", adjustable="box")

    if use_phase_colouring:
        cbar = fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.04)
        cbar.set_label(r"Phase $\arg(\psi)$ (radians)")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
