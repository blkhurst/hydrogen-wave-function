import numpy as np
import matplotlib.pyplot as plt

from wavefunction_tools import associated_laguerre_polynomial


def main() -> None:
    x = np.arange(-2.0, 10.00, 0.02)

    # (n, k, color, linestyle)
    curves = [
        (0, 0, "orange", "-"),
        (1, 0, "blue", "-"),
        (1, 1, "blue", "--"),
        (2, 0, "red", "-"),
        (2, 1, "red", "--"),
        (2, 2, "red", ":"),
        (3, 0, "green", "-"),
        (3, 1, "green", "--"),
        (3, 2, "green", ":"),
        (3, 3, "green", "-."),
    ]

    plt.style.use("bmh")
    fig, ax = plt.subplots(figsize=(10, 6))

    for n, k, color, ls in curves:
        y = associated_laguerre_polynomial(n, k, x)
        ax.plot(
            x,
            y,
            color=color,
            linestyle=ls,
            linewidth=2,
            label=rf"$L_{{{n}}}^{{({k})}}(x)$",
        )

    ax.set_title("Associated (Generalized) Laguerre Polynomials")
    ax.set_ylabel(r"$L_n^k(x)$")
    ax.set_xlim(-2, 10)
    ax.set_ylim(-5, 10)
    ax.grid(True, alpha=0.3)
    ax.legend(ncol=2, frameon=False)
    fig.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
