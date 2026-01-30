# Spherical Coordinates

### Convention

We use the common **physics convention** (ISO 80000-2:2019):

```math
\begin{array}{ll}
\small\text{Radial distance} & r \in [0, \infty) \\
\small\text{Polar / Colatitude / Elevation angle} & \theta \in [0, \pi] \\
\small\text{Azimuthal angle} & \phi \in [0, 2\pi) \\
\end{array}
```

- North pole: $\theta = 0$
- South pole: $\theta = \pi$

### Conversion

```math
\begin{aligned}
r &= \sqrt{x^2 + y^2 + z^2} \\
\theta &= \arccos\left( \frac{z}{r} \right) \\
\phi &= \text{arctan2}(y, x)
\end{aligned}
```

```math
\begin{aligned}
x &= r \sin(\theta) \cos(\phi) \\
y &= r \sin(\theta) \sin(\phi) \\
z &= r \cos(\theta) \\
\end{aligned}
```

### Jacobian (volume element)

The Jacobian determinant tells you how much physical space one grid cell in your chosen coordinates represents, and therefore provides the correct volume measure for integrating (or summing) a density to obtain a probability.

```math
P(A) = \int_A p(x) \; dV
```

```math
\begin{aligned}
dV_{\text{cartesian}} &= dx\,dy\,dz \\
dV_{\text{spherical}} &= r^2\sin\theta\,dr\,d\theta\,d\phi
\end{aligned}
```

On a **Cartesian grid**, each voxel has a constant volume and therefore the Jacobian is 1.\
On a **spherical grid**, the Jacobian $r^2\sin\theta$ accounts for the spherical shell area growing with radius $r$, and for the azimuthal ring shrinking near the poles.

The **solid angle** element can sometimes be written as $d\Omega = \sin\theta\text{ }d\theta\text{ }d\phi$.

- $d\Omega$ describes direction on a unit sphere.
- $dV$ describes 3D volume.

## Resources

- [Spherical coordinate system - Conversions - Wikipedia](https://en.wikipedia.org/wiki/Spherical_coordinate_system#Coordinate_system_conversions)
