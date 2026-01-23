import numpy as np
import matplotlib.pyplot as plt

from wavefunction_tools import spherical_harmonic


def normalise(values: np.ndarray) -> np.ndarray:
    vmin = np.nanmin(values)
    vmax = np.nanmax(values)
    if np.isclose(vmin, vmax):
        return np.ones_like(values, dtype=float)
    return (values - vmin) / (vmax - vmin)


def main() -> None:
    l, m = 3, 2
    resolution = 100

    # Spherical coordinates:
    # theta in [0, pi] (polar / colatitude), phi in [0, 2pi] (azimuth)
    theta = np.linspace(0.0, np.pi, resolution)
    phi = np.linspace(0.0, 2.0 * np.pi, resolution)
    theta, phi = np.meshgrid(theta, phi)

    # Unit sphere
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    # Compute Y_l^m
    re, im = spherical_harmonic(l, m, theta, phi)

    # Map to colours
    re_col = plt.cm.seismic(normalise(re))
    im_col = plt.cm.seismic(normalise(im))

    plt.style.use("bmh")
    fig = plt.figure(figsize=(14, 7), constrained_layout=True)

    # Real part
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    ax1.set_title(rf"Real $Y_{{{l}}}^{{{m}}}(\theta,\phi)$")
    ax1.plot_surface(x, y, z, facecolors=re_col)

    # Imag part
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    ax2.set_title(rf"Imag $Y_{{{l}}}^{{{m}}}(\theta,\phi)$")
    ax2.plot_surface(x, y, z, facecolors=im_col)

    for ax in (ax1, ax2):
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-1, 1)
        ax.set_box_aspect((1, 1, 1))

    plt.show()


if __name__ == "__main__":
    main()
