# Derivation of $L_2^{(2)}(x)$

### Operator identity

```math
e^{x}\,\frac{d^{n}}{dx^{n}}\!\left(e^{-x} f(x)\right)=\left(\frac{d}{dx}-1\right)^{n} f(x)
```

Here $(\frac{d}{dx}-1)$ means "differentiate, then subtract the unchanged function" (a linear operator), applied $n$ times. The operator form and exponential Rodrigues form are equivalent.

### Differential operator method

```math
\begin{aligned}
L_n^{(\alpha)}(x)
&= \frac{x^{-\alpha}}{n!}\left(\frac{d}{dx}-1\right)^n x^{n+\alpha} \\
L_2^{(2)}(x)
&= \frac{x^{-2}}{2!}\left(\frac{d}{dx}-1\right)^2 x^{2+2}
&& \small\text{(substitute)} \\
&= \frac{x^{-2}}{2}\left(\frac{d}{dx}-1\right)^2 x^{4}
&& \small\text{(simplify constants)}
\end{aligned}
```

Apply the operator:

```math
\begin{aligned}
\text{Let } h_0(x) &= x^4 \\
h_1(x)
&= \left(\frac{d}{dx}-1\right)h_0(x)
&& \small\text{(apply operator)} \\
&= \frac{d}{dx}\Big[x^4\Big] - x^4
&& \small\text{(definition)} \\
&= 4x^3 - x^4
&& \small\text{(power rule)} \\
\\
h_2(x)
&= \left(\frac{d}{dx}-1\right)h_1(x)
&& \small\text{(apply operator)} \\
&= \frac{d}{dx}\Big[4x^3-x^4\Big] - \Big(4x^3-x^4\Big)
&& \small\text{(definition)} \\
&= \Big(\frac{d}{dx}\Big[4x^3\Big]-\frac{d}{dx}\Big[x^4\Big]\Big) - 4x^3 + x^4
&& \small\text{(sum / difference rule)} \\
&= \Big(12x^2-4x^3\Big) - 4x^3 + x^4
&& \small\text{(power rule)} \\
&= x^4 - 8x^3 + 12x^2
&& \small\text{(simplify)}
\end{aligned}
```

Multiply the prefactor:

```math
\begin{aligned}
L_2^{(2)}(x)
&= \frac{x^{-2}}{2}\,h_2(x) \\
&= \frac{x^{-2}}{2}\Big(x^4 - 8x^3 + 12x^2\Big)
&& \small\text{(substitute)} \\
&= \frac{1}{2}\Big(x^2 - 8x + 12\Big)
&& \small\text{(simplify)} \\
&= \frac{1}{2} x^2 - 4x + 6
&& \small\text{(distribute)}
\end{aligned}
```

```math
\boxed{L_2^{(2)}(x)=\frac{1}{2} x^2 - 4x + 6}
```

---

### Exponential Rodrigues method

```math
\begin{aligned}
L_n^{(\alpha)}(x)
&= \frac{x^{-\alpha} e^x}{n!}\,\frac{d^n}{dx^n}\Big[e^{-x}x^{n+\alpha}\Big] \\
L_2^{(2)}(x)
&= \frac{x^{-2} e^x}{2!}\,\frac{d^2}{dx^2}\Big[e^{-x}x^{2+2}\Big]
&& \small\text{(substitute)} \\
&= \frac{x^{-2} e^x}{2}\,\frac{d^2}{dx^2}\Big[e^{-x}x^{4}\Big]
&& \small\text{(simplify constants)}
\end{aligned}
```

Compute derivatives:

```math
\begin{aligned}
\text{Let } f(x) &= e^{-x}x^4 \\
\frac{d}{dx}\Big[f(x)\Big]
&= \frac{d}{dx}\Big[e^{-x}x^4\Big]
&& \small\text{(rewrite)} \\
&= e^{-x}\frac{d}{dx}\Big[x^4\Big] + x^4\frac{d}{dx}\Big[e^{-x}\Big]
&& \small\text{(product rule)} \\
&= e^{-x}(4x^3) + x^4(-e^{-x})
&& \small\text{(power rule)} \\
&= e^{-x}\Big(4x^3-x^4\Big)
&& \small\text{(factor)} \\
\\
\frac{d^2}{dx^2}\Big[f(x)\Big]
&= \frac{d}{dx}\Big[e^{-x}(4x^3-x^4)\Big]
&& \small\text{(rewrite derivatives)} \\
&= e^{-x}\frac{d}{dx}\Big[4x^3-x^4\Big] + (4x^3-x^4)\frac{d}{dx}\Big[e^{-x}\Big]
&& \small\text{(product rule)} \\
&= e^{-x}\Big(12x^2-4x^3\Big) + (4x^3-x^4)(-e^{-x})
&& \small\text{(power rule)} \\
&= e^{-x}\Big(12x^2-4x^3-4x^3+x^4\Big)
&& \small\text{(simplify)} \\
&= e^{-x}\Big(x^4-8x^3+12x^2\Big)
&& \small\text{(simplify)}
\end{aligned}
```

Substitute back:

```math
\begin{aligned}
L_2^{(2)}(x)
&= \frac{x^{-2} e^x}{2}\,\Big[e^{-x}\big(x^4-8x^3+12x^2\big)\Big]
&& \small\text{(substitute)} \\
&= \frac{x^{-2}}{2}\,\Big(x^4-8x^3+12x^2\Big)
&& \small\text{(since }e^x e^{-x}=1\small\text{)} \\
&= \frac{1}{2}\,\frac{1}{x^2}\,\Big(x^4-8x^3+12x^2\Big)
&& \small\text{(rewrite as factor; }x^{-2}=\frac{1}{x^2}\small\text{)} \\
&= \frac{1}{2}\,\Big(\frac{x^4}{x^2}-\frac{8x^3}{x^2}+\frac{12x^2}{x^2}\Big)
&& \small\text{(distribute } \frac{1}{x^2}\small\text{)} \\
&= \frac{1}{2}\,\Big(x^2-8x+12\Big)
&& \small\text{(simplify)} \\
&= \frac{1}{2} x^2 - 4x + 6
&& \small\text{(distribute)}
\end{aligned}
```

```math
\boxed{L_2^{(2)}(x)=\frac{1}{2} x^2 - 4x + 6}
```
