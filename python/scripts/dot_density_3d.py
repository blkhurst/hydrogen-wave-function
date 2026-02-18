"""
Dot Density Plot (3D)
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
    sample_orbital,
    spherical_to_cartesian,
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
    n, l, m = 3, 1, 0
    num_samples = 10_000
    point_size = 5
    num_r = 4096
    num_theta = 256
    num_phi = 512
    r_max = radial_axis(n, l)
    use_phase_colouring = False

    # Sample points (spherical)
    r, theta, phi, (psi_re, psi_im) = sample_orbital(
        n=n,
        l=l,
        m=m,
        num_samples=num_samples,
        r_max=r_max,
        resolution_r=num_r,
        resolution_theta=num_theta,
        resolution_phi=num_phi,
        add_jitter=False,
        basis="complex",
    )

    # Convert to Cartesian
    x, y, z = spherical_to_cartesian(r, theta, phi)

    # Color
    if use_phase_colouring:
        color, alpha = phase_colouring(psi_re + 1j * psi_im, gamma=0.15)
    else:
        color, alpha = sign_colouring(psi_re + 1j * psi_im, gamma=0.15)

    # Plot
    plt.style.use("dark_background")  # bmh
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    sc = ax.scatter(
        x,
        y,
        z,
        c=color,
        alpha=alpha if use_phase_colouring else None,  # Alpha in RGBA
        cmap="twilight",
        s=point_size,
        linewidths=0,
    )

    ax.set_title(rf"Dot Density: $(n,l,m)=({n},{l},{m})$ (3D)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim(-r_max, r_max)
    ax.set_ylim(-r_max, r_max)
    ax.set_zlim(-r_max, r_max)
    ax.grid(False)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.set_box_aspect((1, 1, 1))

    if use_phase_colouring:
        cbar = fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.04)
        cbar.set_label(r"Phase $\arg(\psi)$ (radians)")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
