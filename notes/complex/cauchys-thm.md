---
layout: page
title: Cauchy's Theorem
---

/\*TODO: green's theorem (first do Stoke's theorem and follow that proof philosophically)\*/

## Cauchy's Theorem

/\*motivation?\*/

An alternative way to think of a complex function \\(f: \mathbb{C} \to \mathbb{C}\\) is as a vector field: we assign the vector \\(f(z) \in \mathbb{C}\\) to each point \\(z \in \mathbb{C}\\). When functions are thought of from this perspective, 

**Thm (Cauchy's Theorem).** Let \\(\Omega \subset \mathbb{C}\\) be an open connected region and let \\(f(z)\\) be a holomorphic function over \\(\Omega\\). Then, 
\\[
    \int_{\partial \Omega} f(z) dz = 0.
\\]

*Proof.* /\*just use Green's theorem:\*/ /\*todo: explain steps below\*/

\\[
    \begin{align}
        \int_{\partial \Omega} f(z)
        &= \int_{\partial \Omega} (u(x+iy) + iv(x+iy))(dx+idy)\\\\\
        &= \int_{\partial \Omega} (udx - vdy) + i\int_{\partial \Omega}(vdx + udy)\\\\\
        &= -\int_{\partial \Omega} \frac{\partial v}{\partial x} + \frac{\partial u}{\partial y}dxdy
           + \int_{\partial \Omega} \frac{\partial u}{\partial x} - \frac{\partial v}{\partial y}dxdy
        = 0
    \end{align}
\\]

/\*intuition in terms of Polya vector field\*/

#### Consequences

/\*talk about path invariance for integrals\*/

/\*talk about integrals for annulus.\*/