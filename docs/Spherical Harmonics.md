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

## Resources

- [Spherical harmonics - Wikipedia](https://en.wikipedia.org/wiki/Spherical_harmonics#Conventions)
  - > "where $P_{\ell }^{m}$ are associated Legendre polynomials without the Condon–Shortley phase (to avoid counting the phase twice)."
- [Spherical and Spheroidal Harmonics - Symmetry - dlmf.nist.gov](https://dlmf.nist.gov/14.30#E6)
