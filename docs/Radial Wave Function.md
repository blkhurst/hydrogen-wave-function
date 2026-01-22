# Radial

### Radial Wave Function

```math
R_{nl}(r)
= \sqrt{ \left(\frac{2Z}{na_0}\right)^3  \frac{(n - l - 1)!}{2n[(n + l)!]} } \; e^{-\rho/2} \rho^{l} \; L^{2l+1}_{n-l-1}(\rho)
```

```math
\begin{array}{cll}
\sqrt{\;\;\;\;} & & \small\text{Normalisation constant} \\
Z & 1 & \small\text{Atomic number (Hydrogen)} \\
a_0 & \frac{4\pi \epsilon_0 \hbar^2}{m_e e^2} & \small\text{Bohr radius (constant)} \\
\rho & \frac{2Zr}{na_0} & \small\text{Scaled radial distance} \\
e & \small\approx 2.71828 & \small\text{Euler's number} \\
L_{n-l-1}^{2l+1}(\rho) & & \small\text{Associated Laguerre Polynomial}
\end{array}
```

Using $a_0 = 1$ means $r$ is measured in **Bohr radii** (atomic units), while $a_0 = 0.52917721067 \text{\AA}$ means $r$ is measured in Angstroms.

### Radial Distribution

$$
P_{nl}(r) = r^2|R_{nl}(r)|^2
$$

This is the **radial probability density**, meaning $P_{nl}(r)dr$ is the probability of finding an electron in the shell $[r, r+dr]$, where $d\Omega = sin\theta d\theta d\varphi$. This assumes our spherical harmonic implementation satisfies $\int |Y_l^m|^2 d\Omega = 1$. Some authors normalise so that $\int |Y_l^m|^2 d\Omega = 4\pi$, in which case:

$$
P_{nl}(r) = 4\pi r^2|R_{nl}(r)|^2
$$

## Resources

- [Wave function - Hydrogen atom - Wikipedia](https://en.wikipedia.org/wiki/Wave_function#Hydrogen_atom)
- [Hydrogen atom - Wikipedia](https://en.wikipedia.org/wiki/Hydrogen_atom)
- [2.2.2: Quantum Numbers and Atomic Wave Functions - Chemistry LibreTexts](<https://chem.libretexts.org/Bookshelves/Inorganic_Chemistry/Inorganic_Chemistry_(LibreTexts)/02%3A_Atomic_Structure/2.02%3A_The_Schrodinger_equation_particle_in_a_box_and_atomic_wavefunctions/2.2.02%3A_Quantum_Numbers_and_Atomic_Wave_Functions>)
- [Hydrogen Radial Probabilities (gsu.edu)](http://hyperphysics.phy-astr.gsu.edu/hbase/hydwf.html#c1)
