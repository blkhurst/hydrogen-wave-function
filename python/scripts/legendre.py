import numpy as np
import matplotlib.pyplot as plt

from wavefunction_tools import associated_legendre_polynomial


def main() -> None:
    x = np.linspace(-1, 1.0, 400)

    # (l, m, color, linestyle)
    curves = [
        (1, 1, "b", "-"),
        (2, 1, "m", "-"),
        (3, 1, "y", "-"),
        (4, 1, "g", "-"),
        (5, 1, "c", "-"),
    ]

    # dark_background, bmh, fivethirtyeight, ggplot, Solarize_Light2
    plt.style.use("bmh")
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot
    for l, m, colour, ls in curves:
        y = associated_legendre_polynomial(l, m, x)
        ax.plot(
            x,
            y,
            color=colour,
            linestyle=ls,
            linewidth=2,
            label="$P_%s^{%s}$" % (l, m),
        )

    ax.set_title("Associated Legendre Polynomial")
    ax.set_ylabel(r"$P_l^m(x)$")
    ax.legend(loc="upper center", ncol=3)
    fig.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
