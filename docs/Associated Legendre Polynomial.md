# Associated Legendre Polynomial

### Rodrigues’ Formula

$$
P_l^m(x) = \frac{(-1)^m}{2^l l!} (1 - x^2)^{m/2} \frac{d^{l+m}}{dx^{l+m}} (x^2 - 1)^l
$$

#### Negative $m$ Extension

$$
P_l^{-m}(x) = (-1)^m \frac{(l - m)!}{(l + m)!} P_l^m(x)
$$

$$
\text{If}\quad |m| \gt \ell\quad \text{then}\quad P_\ell^{m} = 0
$$

The **Condon-Shortley Phase Factor** $(-1)^m$ is optional, but in the spherical harmonic context, should be included **once**, either within the associated Legendre polynomials $P_l^{\pm m}$, **or** within the spherical harmonics $Y_l^m$, but not both.

### Closed Forms

```math
P_l^m(x)
= (-1)^m \cdot 2^l \cdot (1 - x^2)^{m/2} \cdot \sum_{k=m}^l \frac{k!}{(k - m)!} \cdot x^{k-m} \cdot \binom{l}{k} \binom{\frac{l + k - 1}{2}}{l}
```

This summation contains a binomial coefficient with a non-integer upper value, and therefore must be used with the **Generalized Binomial Coefficient**. Use the negative $m$ extension for $m \lt 0$.

### Recurrence Relations

For numerical computation, using recurrence properties is usually more stable than closed-form sums since it avoids huge intermediate factorial terms that could overflow and lose precision. This three-term recurrence consists of two base identities $P_l^l$ and $P_{l+1}^l$ that can be used to compute any $P_l^m$.

```math
\begin{aligned}
P_l^l(x) &= (-1)^l (2l - 1)!! (1 - x^2)^{l/2} \\
P_{l+1}^l(x) &= x(2l + 1) P_l^l(x) \\
\end{aligned}
```

```math
\begin{aligned}
(l - m + 1) P_{l+1}^m(x) &= (2l + 1) x P_l^m(x) - (l + m) P_{l-1}^m(x)
& (l \ge 1)
\end{aligned}
```

Written in terms of $P_l^m$:

$$
\begin{aligned}
P_l^m(x) &= \frac{x(2l - 1) P_{l-1}^m(x) - (l + m - 1) P_{l-2}^m(x)}{l - m}
& (l \ge 2)
\end{aligned}
$$

Note that the **double factorial** $(2l - 1)!!$ is **not** the same as applying the factorial function twice $(n!)!$. It means the product of every other integer, odd or even depending on the starting value.

In addition, to avoid overflow when computing a **factorial ratio**, use a product form. For integers $0 \le A \le B$:

$$
\frac{A!}{B!} = \prod_{t=A+1}^{B} \frac{1}{t}
$$

## References

- [Associated Legendre polynomials - Wikipedia](https://en.wikipedia.org/wiki/Associated_Legendre_polynomials)
- [Associated Legendre Polynomial - Wolfram](https://mathworld.wolfram.com/AssociatedLegendrePolynomial.html)
- [Double Factorial - Wikipedia](https://en.wikipedia.org/wiki/Double_factorial)
- For spherical harmonics, $x = cos\theta \in [-1, 1]$.
