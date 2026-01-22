# Binomial Coefficient

> "Generalized Binomial Coefficient" usually refers to extending $\binom{x}{y}$ beyond integers (often via the Gamma function).
> The multiplicative product form extends the _upper_ argument $n$ to non-integers, but still requires integer $k \ge 0$.

### Factorial Formula

$$
\begin{aligned}
\binom{n}{k} &= \frac{n!}{k! (n - k)!}
& (0 \le k \le n)
\end{aligned}
$$

Defined for non-negative integer $n$ and $k$. $(n,k\in\mathbb{Z}_{\ge 0})$.

### Multiplicative Formula

$$
\binom{n}{k} = \prod_{i=1}^{k} \frac{n + 1 - i}{i}
$$

Generalizes the **upper** argument $n \in \mathbb{R}$ while keeping $k \in \mathbb{Z}_{\ge 0}$.\
This is a good balance for numerical implementations (e.g. compute shaders): it avoids large intermediate factorials and doesn’t require implementing Gamma functions.

### Gamma Formula (Generalized Binomial Coefficient)

When $x$ and $y$ are not necessarily integers, the binomial coefficient can be extended to real or complex arguments using the Gamma function:

$$
\binom{x}{y} = \frac{\Gamma(x + 1)}{\Gamma(y + 1) \Gamma(x - y + 1)}
$$

## Resources

[Binomial coefficient - Wikipedia](https://en.wikipedia.org/wiki/Binomial_coefficient#Multiplicative_formula)
