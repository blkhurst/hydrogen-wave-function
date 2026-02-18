# Documentation

Notes and derivations supporting the hydrogen wavefunction implementation and visualisations.

## Contents

- Equations
  - [Associated Laguerre Polynomial](./Associated%20Laguerre%20Polynomial.md)
  - [Associated Legendre Polynomial](./Associated%20Legendre%20Polynomial.md)
  - [Binomial Coefficient](./Binomial%20Coefficient.md)
  - [Complex Number](./Complex%20Number.md)
  - [Hydrogen Wave Function](./Hydrogen%20Wave%20Function.md)
  - [Quantum Superposition](./Quantum%20Superposition.md)
  - [Radial Wave Function](./Radial%20Wave%20Function.md)
  - [Spherical Coordinates](./Spherical%20Coordinates.md)
  - [Spherical Harmonics](./Spherical%20Harmonics.md)
- Implementation
  - [Sampling](./Sampling.md)
- Derivations
  - [Deriving the 1s orbital](./derivations/deriving_1s.md)

## Conventions

- **Units**: default to $a_0 = 1$ (distances measured in **Bohr radii**). Useful conversions:
  - $a_0 \approx 0.52917721067\,\AA$
  - $a_0 \approx 5.2917721067 \times 10^{-11} \text{m}$
- **Spherical coordinates**: physics convention (ISO 80000-2:2019).
- **Spherical harmonic normalisation**: $\int_{\Omega} |Y_l^m|^2 d\Omega = 1$ (not $4\pi$).
- **Condon–Shortley phase**: implemented in the **associated Legendre** definitions $P_l^m$, not in $Y_l^m$.
- **Numerical stability**: closed forms often involve factorials / binomials which can overflow or lose precision. Prefer stable techniques, recurrence relations, and factorial ratios where possible.
  - **Binomial**: use multiplicative/product form for $\binom{n}{k}$ (integer $k$, possibly non-integer $n$).
  - **Laguerre**: use the three-term recurrence for $L_n^{(\alpha)}(x)$.
  - **Legendre**: use recurrence relations for $P_l^m(x)$.
  - **Factorial ratios**: avoid large factorials; prefer product identities like
    ```math
    \frac{A!}{B!}=\prod_{t=A+1}^{B}\frac{1}{t}\quad (0\le A\le B)
    ```
