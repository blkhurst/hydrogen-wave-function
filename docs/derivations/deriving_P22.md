# Derivation of $P_2^2$

### Expand-first method

```math
\begin{aligned}
P_l^m(x)
&= \frac{(-1)^m}{2^l \, l!} \, (1-x^2)^{m/2} \, \frac{d^{l+m}}{dx^{l+m}} \Big[ (x^2-1)^l \Big] \\
P_2^2(x)
&= \frac{(-1)^2}{2^2 \, 2!} \, (1-x^2)^{2/2} \, \frac{d^{4}}{dx^{4}} \Big[ (x^2-1)^2 \Big]
&& \small\text{(substitute)} \\
&= \frac{1}{8} \, (1-x^2) \, \frac{d^{4}}{dx^{4}} \Big[ (x^2-1)^2 \Big]
&& \small\text{(simplify constants)} \\
\\
\text{Let } f(x) &= (x^2-1)^2 = x^4-2x^2+1
&& \small\text{(expand)} \\
\frac{d}{dx}\Big[f(x)\Big] &= 4x^3-4x && \small\text{(power rule; sum/difference rule)} \\
\frac{d^2}{dx^2}\Big[f(x)\Big] &= 12x^2-4 && \small\text{(power rule)} \\
\frac{d^3}{dx^3}\Big[f(x)\Big] &= 24x && \small\text{(power rule)} \\
\frac{d^4}{dx^4}\Big[f(x)\Big] &= 24 && \small\text{(power rule)} \\
\\
P_2^2(x)
&= \frac{1}{8} \, (1-x^2) \cdot 24
&& \small\text{(substitute)} \\
&= 3(1-x^2)
&& \small\text{(simplify)}
\end{aligned}
```

### Chain-rule method

```math
\begin{aligned}
P_l^m(x)
&= \frac{(-1)^m}{2^l \, l!} \, (1-x^2)^{m/2} \, \frac{d^{l+m}}{dx^{l+m}} \Big[ (x^2-1)^l \Big] \\
P_2^2(x)
&= \frac{(-1)^2}{2^2 \, 2!} \, (1-x^2)^{2/2} \, \frac{d^{4}}{dx^{4}} \Big[ (x^2-1)^2 \Big]
&& \small\text{(substitute)} \\
&= \frac{1}{8} \, (1-x^2) \, \frac{d^{4}}{dx^{4}} \Big[ (x^2-1)^2 \Big]
&& \small\text{(simplify constants)} \\
\\
\text{Let } g(x) &= (x^2-1)^2 \\
\frac{d}{dx}\Big[g(x)\Big]
&= 2(x^2-1)\cdot \frac{d}{dx}\Big[(x^2-1)\Big]
&& \small\text{(chain rule)} \\
&= 2(x^2-1)\cdot \Big(\frac{d}{dx}\Big[x^2\Big]-\frac{d}{dx}\Big[1\Big]\Big)
&& \small\text{(sum / difference rule)} \\
&= 2(x^2-1)\cdot (2x-0)
&& \small\text{(power rule; constant rule)} \\
&= 4x(x^2-1)
&& \small\text{(simplify)} \\
&= 4x^3-4x
&& \small\text{(expand)} \\
\\
\frac{d^{2}}{dx^{2}}\Big[g(x)\Big]
&= \frac{d}{dx}\Big[4x^3-4x\Big]
&& \small\text{(rewrite derivatives)} \\
&= 12x^2-4
&& \small\text{(power rule)} \\
\\
\frac{d^{3}}{dx^{3}}\Big[g(x)\Big]
&= \frac{d}{dx}\Big[12x^2-4\Big]
&& \small\text{(rewrite derivatives)} \\
&= 24x
&& \small\text{(power rule; constant rule)} \\
\\
\frac{d^{4}}{dx^{4}}\Big[g(x)\Big]
&= \frac{d}{dx}\Big[24x\Big]
&& \small\text{(rewrite derivatives)} \\
&= 24
&& \small\text{(power rule)} \\
\\
P_2^2(x)
&= \frac{1}{8} \, (1-x^2)\cdot 24
&& \small\text{(substitute)} \\
&= 3(1-x^2)
&& \small\text{(simplify)}
\end{aligned}
```
