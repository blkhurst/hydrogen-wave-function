# Associated Laguerre Polynomial

> Also called "Generalized Laguerre Polynomial"

### Rodrigues’ Formula

$$
\begin{aligned}
L_n^{(\alpha)}(x)
&= \frac{x^{-\alpha} e^x}{n!} \frac{d^n}{dx^n} (e^{-x} x^{n+\alpha}) \\
&= \frac{x^{-\alpha}}{n!} \left(\left( \frac{d}{dx} -1 \right)^n x^{n+\alpha}\right)
\end{aligned}
$$

Where $\left( \frac{d}{dx} -1 \right)^n$ means "apply the operator to the result $n$ times".

### Closed Forms

Explicit sum for $L_n^{(\alpha)}$ with degree ($n \in 0,1,2,\dots$) and parameter $\alpha$, derived by applying Leibniz's theorem for differentiation of a product to Rodrigues' formula. When ($\alpha = k$) is a non-negative integer, the generalized binomial coefficient can be written using factorials.

$$
L_n^{(\alpha)}(x)
= \sum_{i=0}^{n} (-1)^i \binom{n + \alpha}{n - i} \frac{x^i}{i!}
$$

$$
\begin{aligned}
L_n^k(x)
&= \sum_{m=0}^{n} (-1)^m \frac{(n + k)!}{(n - m)! (k + m)! m!} x^m
& (k \in \mathbb{Z}_{\ge 0})
\end{aligned}
$$

### Recurrence Relations

For numerical computation, using recurrence properties is usually more stable than closed-form sums since it avoids huge intermediate factorial terms that could overflow and lose precision.

Two base cases used to seed the three-term recurrence:

$$
\begin{aligned}
L_0^{(\alpha)}(x) &= 1 \\
L_1^{(\alpha)}(x) &= 1 + \alpha - x \\
L_{k+1}^{(\alpha)}(x) &= \frac{(2k + 1 + \alpha - x) L_k^{(\alpha)}(x) - (k + \alpha) L_{k-1}^{(\alpha)}(x)}{k + 1}
& (k \ge 1)
\end{aligned}
$$

Written in terms of $L_k^{(\alpha)}$

$$
\begin{aligned}
L_{k}^{(\alpha)}(x)
&= \frac{(2k - 1 + \alpha - x) L_{k-1}^{(\alpha)}(x) - (k + \alpha - 1) L_{k-2}^{(\alpha)}(x)}{k}
& (k \ge 2)
\end{aligned}
$$

Recurrence relations are often written in the form $(k+1) L_{k+1}^{(\alpha)}(x)=\dots$; to isolate $L_{k+1}^{(\alpha)}(x)$, divide both sides by $(k+1)$.

## References

- [Laguerre polynomials - Generalized Laguerre polynomials - Wikipedia](https://en.wikipedia.org/wiki/Laguerre_polynomials#Generalized_Laguerre_polynomials)
- [Associated Laguerre Polynomial - Factorial Formula - Wolfram](https://mathworld.wolfram.com/AssociatedLaguerrePolynomial.html)
