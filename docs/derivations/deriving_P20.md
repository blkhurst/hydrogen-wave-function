# Derivation of $P_2^0$

### Expand-first method

```math
\begin{aligned}
P_l^m(x)
&= \frac{(-1)^m}{2^l \, l!} \, (1-x^2)^{m/2} \, \frac{d^{l+m}}{dx^{l+m}} \Big[ (x^2-1)^l \Big] \\
P_2^0(x)
&= \frac{(-1)^0}{2^2 \, 2!} \, (1-x^2)^{0/2} \, \frac{d^{2}}{dx^{2}} \Big[ (x^2-1)^2 \Big]
&& \small\text{(substitute)} \\
&= \frac{1}{8} \, \frac{d^2}{dx^2} \Big[ (x^2-1)^2 \Big]
&& \small\text{(simplify constants)} \\
&= \frac{1}{8} \, \frac{d^2}{dx^2} \Big[ x^4 - 2x^2 + 1 \Big]
&& \small\text{(expand)} \\
&= \frac{1}{8} \, \frac{d}{dx}\Big[\frac{d}{dx} \Big[ x^4 - 2x^2 + 1 \Big] \Big]
&& \small\text{(rewrite derivatives)} \\
&= \frac{1}{8} \, \frac{d}{dx}\Big[\frac{d}{dx}[x^4] - 2\frac{d}{dx}[x^2] + \frac{d}{dx}[1]\Big]
&& \small\text{(sum/difference/constant multiple rule)} \\
&= \frac{1}{8} \, \frac{d}{dx}\Big[4x^3 - 4x + 0\Big]
&& \small\text{(power rule; constant rule)} \\
&= \frac{1}{8} \left(\frac{d}{dx} \Big[ 4x^3 \Big] - \frac{d}{dx} \Big[ 4x \Big] \right)
&& \small\text{(sum / difference rule)} \\
&= \frac{1}{8} \Big(12x^2 - 4 \Big)
&& \small\text{(power rule)} \\
&= \frac{1}{8} \, 4 \Big(3x^2 - 1 \Big)
&& \small\text{(common factor)} \\
&= \frac{1}{2} (3x^2 - 1)
&& \small\text{(simplify) }
\end{aligned}
```

### Chain-rule method

```math
\begin{aligned}
P_l^m(x)
&= \frac{(-1)^m}{2^l \, l!} \, (1-x^2)^{m/2} \, \frac{d^{l+m}}{dx^{l+m}} \Big[ (x^2-1)^l \Big] \\
P_2^0(x)
&= \frac{(-1)^0}{2^2 \, 2!} \, (1-x^2)^{0/2} \, \frac{d^{2}}{dx^{2}} \Big[ (x^2-1)^2 \Big]
&& \small\text{(substitute)} \\
&= \frac{1}{8} \, \frac{d^2}{dx^2} \Big[ (x^2-1)^2 \Big]
&& \small\text{(simplify constants)} \\
&= \frac{1}{8} \, \frac{d}{dx}\Big[\frac{d}{dx} \Big[ (x^2-1)^2 \Big]\Big]
&& \small\text{(rewrite derivatives)} \\
&= \frac{1}{8} \, \frac{d}{dx} \Big[ 2(x^2 - 1) \cdot \frac{d}{dx} \Big[ (x^2 - 1) \Big] \Big]
&& \small\text{(chain rule)} \\
&= \frac{1}{8} \, \frac{d}{dx} \Big[ 2(x^2 - 1) \cdot (2x) \Big]
&& \small\text{(power rule; constant rule)} \\
&= \frac{1}{8} \, \frac{d}{dx} \Big[ 4x^3 - 4x \Big]
&& \small\text{(simplify)} \\
&= \frac{1}{8} \, \Big(12x^2 - 4 \Big)
&& \small\text{(power rule)} \\
&= \frac{1}{8} \, 4 \Big(3x^2 - 1 \Big)
&& \small\text{(common factor)} \\
&= \frac{1}{2} (3x^2 - 1)
&& \small\text{(simplify)}
\end{aligned}
```
