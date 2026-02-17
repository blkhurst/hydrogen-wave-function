# Spherical Harmonics

> Also called the "Angular Wave Function"

### Definition

```math
Y_l^m(\theta, \varphi) =\sqrt{\frac{2l + 1}{4\pi} \frac{(l - m)!}{(l + m)!}} P_l^m(\text{cos }\theta) e^{im\varphi}
```

```math
Y_l^{-m}(\theta, \varphi) = (-1)^m \; \overline{Y_l^m(\theta, \varphi)}
```

```math
\begin{array}{ll}
\sqrt{\;\;\;\;} & \small\text{Normalisation constant} \\
P_l^m(\text{cos }\theta) & \small\text{Associated Legendre Polynomial} \\
i & \small\text{Imaginary number} \; \sqrt{-1} \\
e^{im\varphi} & \small\text{Complex exponential} \\
\overline{Y_l^m(\theta, \varphi)} & \small\text{Complex conjugate}
\end{array}
```

The **Condon-Shortley phase factor** is $(-1)^m$; include it **either** in $P_l^{\pm m}$ **or** $Y_l^m$, but not both. This implementation includes it in the associated Legendre functions.

### Negative $m$ identity derivation

```math
\begin{aligned}
Y_\ell^{-m}(\theta,\varphi)
&=\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-(-m))!}{(\ell+(-m))!}}\;P_\ell^{-m}(\cos\theta)\,e^{-im\varphi} \\
&=\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell+m)!}{(\ell-m)!}}
\left[(-1)^m\frac{(\ell-m)!}{(\ell+m)!}P_\ell^{m}(\cos\theta)\right]e^{-im\varphi} \\
&=(-1)^m\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-m)!}{(\ell+m)!}}\;P_\ell^{m}(\cos\theta)\,e^{-im\varphi} \\
&=(-1)^m\left(\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-m)!}{(\ell+m)!}}\;P_\ell^{m}(\cos\theta)\,e^{im\varphi}\right)^*
= (-1)^m\;\overline{Y_\ell^{m}(\theta,\varphi)}
\end{aligned}
```

> Notice that if the **Condon-Shortley phase factor** were included in $Y_l^m$ instead of the associated Legendre functions $P_l^{\pm m}$, the identity $Y_l^{-m}=(-1)^m\;\overline{Y_\ell^{m}(\theta,\varphi)}$ remains unchanged.

### Normalisation conventions

The definition above uses the common **orthonormal** convention:

```math
\int_0^{2\pi} \int_0^{\pi} |Y_l^m(\theta,\varphi)|^2 \sin\theta \, d\theta \, d\varphi = 1
```

Some authors (often in chemistry) instead use a convention where the spherical harmonics are scaled so the integral equals $4\pi$. This can make factors of $4\pi$ appear, for instance in the radial probability density.

```math
\int_\Omega |Y_l^m|^2 \; d\Omega = 4\pi,
\qquad
d\Omega = \sin\theta \, d\theta \, d\varphi
```

### Real form

```math
\begin{aligned}
Y_{lm}^{\text{real}} &=
\begin{cases}
Y_l^0 & \text{ if } m=0 \\
\sqrt{2} \, (-1)^m \, \Im \{Y_l^{|m|}\} & \text{ if } m<0 \\
\sqrt{2} \, (-1)^m \, \Re \{Y_l^m\} & \text{ if } m>0
\end{cases}
\end{aligned}
```

These are often used in chemistry because they align with Cartesian-oriented "real orbitals" (e.g. $p_x,p_y$). This definition assumes the Condon-Shortley phase convention is used, regardless of whether it's implemented within $Y_l^m$ or $P_l^m$.

## Resources

- [Spherical harmonics - Wikipedia](https://en.wikipedia.org/wiki/Spherical_harmonics#Conventions)
  - > "where $P_{\ell }^{m}$ are associated Legendre polynomials without the Condon–Shortley phase (to avoid counting the phase twice)."
- [Spherical and Spheroidal Harmonics - Symmetry - dlmf.nist.gov](https://dlmf.nist.gov/14.30#E6)
