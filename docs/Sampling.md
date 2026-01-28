# Sampling

Monte Carlo methods use randomness to approximate results that are hard to compute analytically. In our case, we want to **select random points in 3D space** such that the density of points match the hydrogen electron probability, i.e. points appear more often where the electron is more likely to be found.

We start with **uniform random numbers** which are easy to generate, then **transform** them into samples from the target distribution. I started by implementing a simple, but wasteful approach called **rejection sampling**, where we propose points uniformly in a region and keep points under the graph of its density function, but yielded too many rejections to be efficient.

Instead, I switched to **inverse transform sampling**, which uses an inverse **CDF** (cumulative distribution function) derived from the **PDF** (probability density function) which instantly maps a uniform sample $u \sim U[0, 1]$ to a drawn value from the target distribution.

### Why arrays are needed (numerical CDF)

Since our probability density function involves exponentials, polynomials, and special functions, we generally **cannot write a closed-form inverse CDF** $F^{-1}(u)$. Instead, we compute and sample the cumulative distribution numerically:

1. Build a **discrete PDF** $P$ of a given resolution.
2. **Normalise** so that $\sum_i P_i = 1$
3. Compute a **discrete CDF** using $F[i] = \sum_{j=0}^i P_j$
4. Generate $u \sim U[0, 1]$, and find the index where $F[i] \ge u$. (Using **binary search**).

> Normalising is still required since we are sampling a **finite** resolution and $r_{max}$.

## Array-Based Inverse Transform Sampling

### Cartesian 3D Grid

A straightforward approach (as well as my original implementation) is to precompute a **three-dimensional grid** over $(x,y,z)$, build the **PDF array** from $|\psi(x,y,z)|^2$, compute the **CDF**, then sample indices via inverse-transform sampling.

The primary bottleneck is memory usage. With resolution $n$ per axis, storage scales as $O(n^3)$. Storing a single array at resolution $n = 1024$ would yield $1024^3 \approx 1.07 \times 10^9$ entries. Assuming single float32 precision, that is $\approx 4\text{ GB}$ per array, so storing both PDF and CDF would be impractical at the desired resolution.

### Spherical (Separable Radial + Angular)

We can drastically reduce computation and memory usage by realising that the hydrogen wavefunction separates in spherical coordinates:

```math
|\psi|^2 r^2\sin\theta
= \underbrace{r^2|R(r)|^2}_{\text{radial PDF}} \cdot \underbrace{|Y(\theta,\phi)|^2\sin\theta}_{\text{angular PDF in }\theta,\phi}
```

Instead of storing a single three-dimensional CDF $(x,y,z)$, we can store a **one-dimensional radial CDF** over $r$, and a **two-dimensional angular CDF** over $(\theta, \varphi)$.

By comparison, this stores $O(n)$ radial data and $O(n^2)$ angular data. That's $(1024 + 1024^2) \approx 1.05 \times 10^6$ (approximately $4\text{ MB}$), orders of magnitude smaller than the three dimensional approach.

#### How to generate and sample

1. Choose radial resolution $n_r$ and range $r \in [0,r_{max}]$.
2. Choose angular resolution $(n_{\theta},n_{\varphi})$ in range $\theta \in [0,\pi]$ and $\varphi \in [0,2\pi]$.
3. Build the **radial PDF** $P_r(r)$, normalise, then cumulative-sum to build the **radial CDF**.
4. Build the **angular PDF** $P_{\Omega}(\theta,\varphi)$, flatten to 1D, normalise, then cumulative-sum to build the **angular CDF**.
5. Generate $u_r, u_{\Omega} \sim U[0, 1]$ and inverse-transform sample $r$ from the radial CDF, and $(\theta,\varphi)$ from the angular CDF (unflatten the angular index back to $(\theta,\varphi)$).
6. Convert $(r,\theta,\varphi)$ to Cartesian points $(x,y,z)$ for plotting.

#### Cartesian vs Spherical (Jacobian)

When building a **discrete PDF/CDF for sampling**, we discretise $|\psi|^2 dV$, so the cell **volume element** $dV$ depends on the coordinate system:

```math
\begin{aligned}
dV_{\text{cartesian}} &= dx\,dy\,dz \\
dV_{\text{spherical}} &= r^2\sin\theta\,dr\,d\theta\,d\varphi
\end{aligned}
```

On a **uniform Cartesian grid**, each voxel has a constant volume.\
On a **uniform spherical grid**, the volume element grows with radius $r$ and depends on $\theta$.

The factor $r^2\sin\theta$ is the **Jacobian** of the coordinate transform. For example, sampling uniforms in $r$ forgetting the $r^2$ growth would produce too many points near the center.

> The **Jacobian** is only present when converting a density into **probability** (i.e. integrating/summing) in spherical coordinates. On a uniform Cartesian grid, or when evaluating density at a point, we use $|\psi|^2$ without $dV$.
