import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from wavefunction_tools.wavefunction import Axis
from wavefunction_tools import (
    radial_axis,
    time_dependent_factor,
    wavefunction_line_cartesian,
    superpose_wavefunctions,
    complex_magnitude_squared,
    complex_multiply,
)


def ramp01(t: float, travel: float, pause: float) -> tuple[int, float]:
    seg_len = pause + travel
    seg_idx = int(t // seg_len)
    local = t - seg_idx * seg_len
    if local < pause:
        f = 0.0
    else:
        f = (local - pause) / travel
        f = float(np.clip(f, 0.0, 1.0))
    return seg_idx, f


def main():
    axis: Axis = "z"  # Important to use "z" for m=0 states
    time_dependent = True
    mix_factor = 0.5  # [0,1] Only used if time_dependent is False
    auto_scale_y = False  # Autoscaling can appear to "freeze" plots due to y-limits constantly changing
    auto_scale_x = False

    travel = 2.0
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

    #
    r_max = max(radial_axis(n, l) for (n, l, _m) in states)
    u = np.linspace(-r_max, r_max, 3000)

    # Precompute orbitals #? Note that all orbitals are computed on same size grid, not ideal for auto-scaling
    orbitals: list[tuple[np.ndarray, np.ndarray]] = []
    for n, l, m in states:
        re, im = wavefunction_line_cartesian(n, l, m, axis=axis, u=u)
        orbitals.append((re, im))

    # Precompute r_max
    state_rmax = [radial_axis(n, l) for (n, l, _m) in states]

    # Setup graph
    plt.style.use("bmh")
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(14, 6))

    ax0.set_title("Superposition")
    ax0.set_xlabel(axis)
    ax0.set_ylabel(r"$\Psi(%s,t)$" % axis)
    ax0.grid(False)

    ax1.set_title(r"Probability Density $|\Psi(%s,t)|^2$" % axis)
    ax1.set_xlabel(axis)
    ax1.set_ylabel(r"$|\Psi|^2$")
    ax1.grid(False)

    (line_re,) = ax0.plot(u, np.zeros_like(u), linewidth=1.5, label="Re")
    (line_im,) = ax0.plot(u, np.zeros_like(u), linewidth=1.5, label="Im")
    (line_p,) = ax1.plot(u, np.zeros_like(u), linewidth=2, label=r"$|\Psi|^2$")

    ax0.legend()
    ax1.legend()
    fig.tight_layout()

    start = time.time()

    def animate(_i: int):
        t = time.time() - start

        # Compute superposition coefficients
        seg, s = ramp01(t, travel=travel, pause=pause)
        k = seg % (len(states) - 1)

        # Time-dependence
        n1 = states[k][0]
        n2 = states[k + 1][0]
        l1 = states[k][1]
        l2 = states[k + 1][1]
        m1 = states[k][2]
        m2 = states[k + 1][2]
        factor = t if time_dependent else mix_factor
        td1 = time_dependent_factor(n1, factor)
        td2 = time_dependent_factor(n2, factor)
        psi1 = complex_multiply(orbitals[k], td1)
        psi2 = complex_multiply(orbitals[k + 1], td2)

        # Superpose
        re, im = superpose_wavefunctions(psi1, psi2, s)
        magnitude_squared = complex_magnitude_squared(re, im)

        # Update graphs
        line_re.set_ydata(re)
        line_im.set_ydata(im)
        line_p.set_ydata(magnitude_squared)

        ax0.set_title(
            rf"Superposition | $(n,l,m)=({n1},{l1},{m1}) \to ({n2},{l2},{m2})$"
        )

        # Auto-scale y-axis
        reim_max = max(re.max(), im.max(), -re.min(), -im.min())
        magnitude_squared_max = float(magnitude_squared.max())
        if auto_scale_y:
            ax0.set_ylim(-1.05 * reim_max, 1.05 * reim_max)
        ax1.set_ylim(-0.05 * magnitude_squared_max, 1.05 * magnitude_squared_max)

        # Auto-scale x-axis
        if auto_scale_x:
            r1 = state_rmax[k]
            r2 = state_rmax[k + 1]
            s_ease = s * s * (3 - 2 * s)
            r = (1.0 - s_ease) * r1 + s_ease * r2
            # r = (1.0 - s) * r1 + s * r2  # linear
            ax0.set_xlim(-r, r)
            ax1.set_xlim(-r, r)

    ani = animation.FuncAnimation(
        fig,
        animate,
        interval=1000 / 60,
        cache_frame_data=False,
    )
    plt.show()


if __name__ == "__main__":
    main()
