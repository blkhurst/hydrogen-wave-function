# Superposition

### Hydrogen Orbital Superposition

Since the Schrodinger equation is **linear**, any linear combination of solutions is also a solution.

```math
\ket{\psi} = \alpha \ket{n l m} + \beta \ket{n' l' m'}
```

- $\ket{nlm}$ and $\ket{n'l'm'}$ are orbital eigenstates.
- $\alpha$ and $\beta$ are complex coefficients (probability amplitudes).
- They must satisfy $|\alpha|^2 + |\beta|^2 = 1$ (normalisation).

You can view a specific superposition, for instance $\alpha=\beta=\tfrac{1}{\sqrt2}$. In the application, in order to easily evolve over time, I chose to use sine and cosine, since $\cos(s)^2 + \sin(s)^2 = 1$, where $s \in [0, \frac{\pi}{2}]$ to ensure $\alpha$ and $\beta$ reach exactly 0 or 1 at their endpoints.

### Time-dependence

In order to view superposition interference patterns over time, the phase must differ between eigenstates (which occurs when the states have different energies).

```math
\Psi(\mathbf r,t)=\alpha\,\psi_a(\mathbf r)e^{-iE_a t/\hbar} + \beta\,\psi_b(\mathbf r)e^{-iE_b t/\hbar}
```

> **Note:** The application linearly interpolates the superposition coefficients $\alpha$ and $\beta$ between two time-dependent eigenstates. The resulting superpositions are all valid states, but the interpolation path is an animation choice.

## Resources

- [Quantum superposition - Wikipedia](https://en.wikipedia.org/wiki/Quantum_superposition)
- [Transitions in hydrogen wavefunctions - YouTube](https://www.youtube.com/watch?v=o3vFLcg10N0)
- [Is there any time-dependent hydrogen atom Schrodinger equation, solvable analytically? - Physics Stack Exchange](https://physics.stackexchange.com/questions/95085/is-there-any-time-dependent-hydrogen-atom-schr%C3%B6dinger-equation-solvable-analyti)
- [Hydrogen wavefunctions transitioning between different states ](https://community.wolfram.com/groups/-/m/t/2483815)
