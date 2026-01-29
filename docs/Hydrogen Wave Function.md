# Hydrogen Wave Function

### Definition

```math
\psi_{nlm}(r, \theta, \varphi) = R_{nl}(r) \ Y_l^{m_l}(\theta, \varphi)
```

```math
\begin{array}{cll}
\small\text{Wave Functions} & \psi & \small\text{Wave function ("Psi")} \\
& R_{nl} & \small\text{Radial wave function} \\
& Y_l^{m_l} & \small\text{Angular wave function / Spherical harmonic} \\
\small\text{Quantum Numbers} & n & \small\text{Principal quantum number} \\
& l & \small\text{Azimuthal quantum number} \\
& m_l & \small\text{Magnetic quantum number} \\
& m_s & \small\text{Spin quantum number} \\
\small\text{Spherical Coordinates} & r & \small\text{Radial distance} \\
& \theta & \small\text{Polar angle} \\
& \varphi & \small\text{Azimuthal angle} \\
\end{array}
```

### Probability Density

```math
\rho(r, \theta, \varphi) = |\psi_{nlm}(r,\theta,\varphi)|^2
```

This computes the **probability density**. By itself it does **not** give the probability of a point. To get an actual probability, we must integrate the density over a **region of space** using the appropriate volume element $dV$.

In **Cartesian coordinates**, the volume element is $dV = dx \text{ } dy \text{ } dz$.\
In **spherical coordinates**, the volume element is $dV = r^2 \text{ } \sin\theta \text{ } dr \text{ } d\theta \text{ } d\varphi$.

```math
\int_{\mathbb{R}^3} |\psi|^2 \; dV = 1
```

```math
\int_0^{\infty} \int_0^{\pi} \int_0^{2\pi} |\psi(r,\theta,\varphi)|^2 \; r^2 \, \sin\theta \, dr \, d\theta \, d\varphi = 1
```

> This assumes the spherical harmonics are normalised so that $\int |Y_l^m|^2 \text{ } d\Omega = 1$.

For example, when building a **discrete PDF/CDF array**, we wish to integrate/sum the region in order to normalise. Therefore we compute the probability using the respective volume element $dV$. If we only want to **evaluate the density at a single point**, we just use $|\psi|^2$ (no $dV$).

### Time Dependence

```math
\Psi_{nlm}(r,\theta,\varphi,t) = \psi_{nlm}(r,\theta,\varphi) \; e^{-iE_n t/\hbar}
```

```math
E_n = -\dfrac {m_e e^4}{8\epsilon_0^2 h^2 n^2} = -\dfrac{13.6 \; eV}{n^2}
```

```math
\begin{array}{ll}
E_n & \small\text{Energy of the electron} \\
m_e & \small\text{Mass of the electron} \\
e & \small\text{Elementary charge} \\
\epsilon_0 & \small\text{Permittivity of free space} \\
h & \small\text{Planck's constant} \\
\hbar & \small\text{Reduced Planck constant} \\
n & \small\text{Principal quantum number}
\end{array}
```

Since $|e^{-iE_n t/\hbar}|^2 = 1$, the **probability density is time-independent** for a single eigenstate. Time dependence becomes visible in **superpositions** of different energies, producing interference patterns.

```math
\Psi(\mathbf r,t)=\alpha\,\psi_a(\mathbf r)e^{-iE_a t/\hbar} + \beta\,\psi_b(\mathbf r)e^{-iE_b t/\hbar}
```

## Resources

- [Wave function - Wikipedia](https://en.wikipedia.org/wiki/Wave_function#Hydrogen_atom)
- [Atomic orbital - Real orbitals - Wikipedia](https://en.wikipedia.org/wiki/Atomic_orbital#Real_orbitals)
- [The Hydrogen Atom, Part 1 of 3: Intro to Quantum Physics - Youtube](https://www.youtube.com/watch?v=-Y0XL-K0jy0)
- [How To Solve The Schrodinger Equation For The Hydrogen Atom - Youtube](https://www.youtube.com/watch?v=MaXFT-c8u1E&t=529s)
- [Is there any time-dependent hydrogen atom Schrodinger equation, solvable analytically? - Physics Stack Exchange](https://physics.stackexchange.com/questions/95085/is-there-any-time-dependent-hydrogen-atom-schr%C3%B6dinger-equation-solvable-analyti)
