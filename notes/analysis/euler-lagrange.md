---
layout: page
title: Euler Lagrange Equations
---

<!-- FOCUS ON 1D CASE HERE -->

## Euler-Lagrange Equations

#### Formal Statement
Consider the function
\\[
    S(q) = \int_a^b \mathcal{L}(t, q(t), q'(t))dt
\\]
where \\(q: [a,b] \to \mathbb{R}\\) is some path and \\(\mathcal{L}: \mathbb{R} \times \mathbb{R} \times \mathbb{R} \to \mathbb{R}\\) is a function. Then \\(q\\) is a stationary point of \\(S\\) if and only if it satisfies the following *Euler-Lagrange Equation*
\\[
    \frac{d L}{d q}(t, q(t), q'(t)) - \frac{d }{d t}\frac{d L}{d q'}(t, q(t), q'(t)) = 0.
\\]

**Example.**
We can use the Euler-Lagrange equations to study the length of lines between points in the plane. Indeed, the graph of a function \\(q: [a,b] \to \mathbb{R}\\) with \\(q(a) = A\\) and \\(q(b) = B\\) models a path between \\((a, A)\\) and \\((b, B)\\). The length of this graph is given by
\\[
    \operatorname{Length}(q) = \int_a^b \sqrt{1+y'(t)^2}dt.
\\]
That is, the Lagrangian $\mathcal{L}$ is given by
\\[
    \mathcal{L}(t, y, y') = \sqrt{1+y'(t)^2}.
\\]
Thus according to the Euler-Lagrange equation, the critical points of this length function occur precisely when
\\[
\begin{align}
    0 &= \frac{d L}{d q} - \frac{d }{d t}\frac{d L}{d q'}\\\\\
    &= -\frac{d }{d t}\left(\frac{y'(t)}{\sqrt{1+y'(t)^2}}\right)\\\\\
    &= -\frac{y^{\prime \prime}(t)}{(1+y'(t)^2))^{3/2}}
\end{align}
\\]
Thus we conclude \\(y^{\prime \prime}(t) = 0\\) and so \\(y(t)\\) is linear as expected.

**Proof.** We study the behavior of \\(S\\) under a small pertubation of \\(q\\). Define this pertubation by \\(q_{\varepsilon}(t) = q(t) + \varepsilon f(t)\\) for small \\(\varepsilon\\) where \\(f(a) = f(b) = 0\\).

This small pertubation slightly changes the value of \\(S\\), so write
\\[
    S_{\varepsilon} = \int_a^b \mathcal{L}(t, q_{\varepsilon}, q_{\varepsilon}'(t))dt.
\\]

The question is: if \\(S\\) achieves a critical point at \\(q\\), what can \\(q\\) be? Formally, this is equivalent to mandating
\\[
    \left.\frac{d S_{\varepsilon}}{d \varepsilon}\right\|\_{\varepsilon = 0} = 0.
\\]
Observe
\\[
\begin{align}
    \frac{d S_{\varepsilon}}{d \varepsilon}
    &= \int\_a^b \frac{d \mathcal{L}_{\varepsilon}}{d \varepsilon} dt\\\\\
    &= \int\_a^b \frac{\partial \mathcal{L}\_{\varepsilon}}{\partial t} \frac{d t}{d \varepsilon}
    + \frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g\_{\varepsilon}}\frac{d g\_{\varepsilon}}{d \varepsilon}
    + \frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g'\_{\varepsilon}}\frac{d g'\_{\varepsilon}}{d \varepsilon}dt\\\\\
    &= \int\_a^b \frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g\_{\varepsilon}}f(t)dt
    + \int\_a^b\frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g'\_{\varepsilon}}f'(t)dt\\\\\
    &= \int\_a^b \frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g\_{\varepsilon}}f(t)dt
    - \int\_a^b\frac{d }{d t}\frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g'\_{\varepsilon}}f(t)dt
    + \left. \frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g'\_{\varepsilon}}f(t)\right\|\_a^b\\\\\
    &= \int\_a^b \left(\frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g\_{\varepsilon}} - \frac{d }{d t}\frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g'\_{\varepsilon}} \right)f(t)dt
\end{align}
\\]

Thus we could equivalently say \\(S\\) achieves a critical point at \\(q\\) if
\\[
    0 = \int\_a^b \left(\frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g\_{\varepsilon}} - \frac{d }{d t}\frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g'\_{\varepsilon}} \right)f(t)dt
\\]
for all \\(f: [a,b] \to \mathbb{R}\\) such that \\(f(a) = f(b) = 0\\). However, this occurs if and only if
\\[
    \frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g\_{\varepsilon}} - \frac{d }{d t}\frac{\partial \mathcal{L}\_{\varepsilon}}{\partial g'\_{\varepsilon}} = 0
\\]∎