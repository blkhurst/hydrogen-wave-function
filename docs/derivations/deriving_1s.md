# Deriving the closed-form for the 1s orbital

### Closed Form

```math
\begin{aligned}
\psi_{100}(r,\theta,\varphi)
&= R_{10}(r) \cdot Y_0^0(\theta,\varphi) \\
&= \left( \frac{2}{a_0^{3/2}} \cdot e^{-\frac{r}{a_0}} \right) \cdot \left( \frac{1}{2\sqrt{\pi}} \right) \\
&= \frac{2}{2 \sqrt{\pi} \cdot a_0^{3/2}} \cdot e^{-\frac{r}{a_0}} \\
&= \boxed{\frac{1}{\sqrt{\pi a_0^3}} \cdot e^{-\frac{r}{a_0}}}
\end{aligned}
```

> **Note:** $Z=1$, $0!=1$, $x^0=1$, and $\frac{d^0}{dx^0}f(x)=f(x)$.

## Derivation

### Radial wave function

```math
\begin{aligned}
R_{nl}(r)
&= N_{nl} \cdot e^{-\rho/2} \cdot \rho^{l} \cdot L^{2l+1}_{n-l-1}(\rho) \\
R_{10}(r)
&= N_{10} \cdot e^{-\rho/2} \cdot \rho^{0} \cdot L^{2 \cdot 0+1}_{1-0-1}(\rho) \\
&= \frac{2}{a_0^{3/2}} \cdot e^{-\frac{r}{a_0}}
\end{aligned}
```

#### Normalisation constant

```math
\begin{aligned}
N_{nl}
&= \sqrt{ \left(\frac{2Z}{na_0}\right)^3  \frac{(n - l - 1)!}{2n[(n + l)!]} } \\
N_{10}
&= \sqrt{ \left(\frac{2 \cdot 1}{1 \cdot a_0}\right)^3  \frac{(1 - 0 - 1)!}{2 \cdot 1[(1 + 0)!]} } \\
&= \sqrt{ \left(\frac{2}{a_0}\right)^3  \frac{1}{2} }
= \sqrt{ \left(\frac{2^3}{a_0^3}\right)  \frac{1}{2} }
= \sqrt{ \frac{8}{2a_0^3} }
= \sqrt{ \frac{4}{a_0^3} }
= \frac{\sqrt{4}}{\sqrt{a_0^3}}
= \frac{2}{a_0^{3/2}}
\end{aligned}
```

#### Simplify terms using $\rho$

```math
\rho
= \frac{2Zr}{na_0}
= \frac{2 \cdot 1 \cdot r}{1 \cdot a_0}
= \frac{2r}{a_0}
```

```math
\rho^l
= \left(\frac{2r}{a_0}\right)^0
= 1
```

```math
\large
e^{-\rho/2}
= e^{-\frac{1}{2} \rho}
= e^{-\frac{1}{2} \left(\frac{2r}{a_0}\right)}
= e^{-\frac{2r}{2a_0}}
= e^{-\frac{r}{a_0}}
```

#### Associated Laguerre Polynomial

```math
\begin{aligned}
L_n^{(\alpha)}(\rho)
&= \frac{\rho^{-\alpha} e^\rho}{n!} \frac{d^n}{d\rho^n} (e^{-\rho} \rho^{n+\alpha}) \\
L_{n-l-1}^{(2l+1)}(\rho)
= L_0^{(1)}(\rho)
&= \frac{\rho^{-1} e^\rho}{0!} \frac{d^0}{d\rho^0} (e^{-\rho} \rho^{0+1}) \\
&= \rho^{-1} e^\rho (e^{-\rho} \rho) \\
&= 1
\end{aligned}
```

### Spherical Harmonic

```math
\begin{aligned}
Y_l^m(\theta, \varphi)
&= N_l^m \cdot P_l^m(\cos\theta) \cdot e^{im\varphi} \\
Y_0^0(\theta, \varphi)
&= N_0^0 \cdot P_0^0(\cos\theta) \cdot e^{i0\varphi} \\
&= \frac{1}{2\sqrt{\pi}}
\end{aligned}
```

#### Normalisation constant

```math
\begin{aligned}
N_l^m
&= \sqrt{\frac{2l + 1}{4\pi} \frac{(l - m)!}{(l + m)!}} \\
N_0^0
&= \sqrt{\frac{2 \cdot 0 + 1}{4\pi} \frac{(0 - 0)!}{(0 + 0)!}} \\
&= \sqrt{\frac{1}{4\pi}}
= \frac{\sqrt{1}}{\sqrt{4\pi}}
= \frac{\sqrt{1}}{\sqrt{4}\sqrt{\pi}}
= \frac{1}{2\sqrt{\pi}}
\end{aligned}
```

#### Associated Legendre Polynomial

```math
\begin{aligned}
P_l^m(x)
&= \frac{(-1)^m}{2^l l!} (1 - x^2)^{m/2} \frac{d^{l+m}}{dx^{l+m}} (x^2 - 1)^l \\
P_0^0(x)
&= \frac{(-1)^0}{2^0 0!} (1 - x^2)^{0/2} \frac{d^{0+0}}{dx^{0+0}} (x^2 - 1)^0 \\
&= \frac{1}{1 \cdot 1} \cdot 1 \cdot 1
= 1
\end{aligned}
```
