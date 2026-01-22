import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

from wavefunction_tools.utilities import a0
from wavefunction_tools import radial_distribution, radial_wave_function


def r_axis_label() -> str:
    if np.isclose(a0, 1.0, rtol=0.0, atol=1e-12):
        return r"$r\ (a_0),\ a_0=1\ \mathrm{Bohr\ radii}$"
    if np.isclose(a0, 0.52917721067, rtol=0.0, atol=1e-6):
        return rf"$r\ (\AA),\ a_0={a0:.6f}\ \AA$"
    return rf"$r\ (a_0),\ a_0={a0:g}$"


def main():
    numerically_normalise = False
    r = np.linspace(0.0, 25.0, 2000)

    # (n, l, color, linestyle)
    curves = [
        (1, 0, "r", "-"),
        (2, 0, "y", "-"),
        (2, 1, "y", "--"),
        (3, 0, "g", "-"),
        (3, 1, "g", "--"),
        (3, 2, "r", "--"),
    ]

    plt.style.use("bmh")
    fig, (axL, axR) = plt.subplots(figsize=(14, 7), ncols=2)

    # Radial Wave Function (L)
    for n, l, color, ls in curves:
        y = radial_wave_function(n, l, r)
        axL.plot(
            r,
            y,
            color=color,
            linestyle=ls,
            linewidth=2,
            label=rf"$R_{{{n}{l}}}(r)$",
        )
    axL.set_title("Radial Wave Function")
    axL.set_xlabel(r_axis_label())
    axL.set_ylabel("$R(r)$")
    axL.set_xlim(0, r.max())
    axL.set_ylim(-0.1, 0.65)
    axL.legend(ncol=1, frameon=False)

    # Radial Distribution (R)
    for n, l, color, ls in curves:
        y = radial_distribution(n, l, r)
        # Numerical integration normalisation not required if radial_distribution is correct
        if numerically_normalise == True:
            integral = simpson(y=y, x=r)
            y = y / integral
        axR.plot(
            r,
            y,
            color=color,
            linestyle=ls,
            linewidth=2,
            label=rf"$P_{{{n}{l}}}(r)$",
        )
    axR.set_title("Radial Distribution")
    axR.set_xlabel(r_axis_label())
    axR.set_ylabel("$P_{nl}(r)$")
    axR.set_xlim(0, r.max())
    axR.set_ylim(0, 0.65)
    axR.legend(ncol=1, frameon=False)

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
