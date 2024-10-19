---
layout: page
title: Green's Theorem
---

## Green's Theorem.

/\*motivation and visuals\*/

\\[
    \operatorname{curl}(P \partial_x + Q \partial_y) = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}.
\\]

**Theorem.** Consider a vector field \\(V = P(x,y) \partial_x + Q(x,y)\partial_y\\) defined on some open set \\(U \subset \mathbb{R}^2\\) where \\(P,Q\\) are continuously differentiable. Then for any region \\(\Omega \subset U\\) with smooth boundary \\(\partial \Omega\\)
\\[
    \int_{\partial \Omega} V \cdot \nu ds = \int_{\Omega} \operatorname{curl}(V)dA,
\\]
where \\(\nu\\) is the outward pointing unit normal, and the line integral about \\(\partial \Omega\\) is taken counterclockwise.

/\*alternate phrasing:\*/

\\[
    \int_{\partial \Omega} Pdx + Qdy = \int_{\Omega} \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} dxdy
\\]

*Proof.* /\*TODO\*/

#### Derivation from Stoke's Theorem

Consider the \\(1\\)-form \\(Pdx + Qdy\\). Then by Stoke's theorem, /\*todo: explain below more\*/

\\[
    \begin{align}
    \int_{\partial \Omega} Pdx + Qdy
    &= \int_{\Omega} d(Pdx + Qdy) \\\\\
    &= \int_{\Omega} dP \wedge dx + dQ \wedge dx \\\\\
    &= \int_{\Omega} \left(\frac{\partial P}{\partial x}dx + \frac{\partial P}{\partial y}dy \right) \wedge dx 
                   + \left(\frac{\partial Q}{\partial x}dx + \frac{\partial Q}{\partial y}dy\right) \wedge dy\\\\\
    &= \int_{\Omega} \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} dx \wedge dy
    \end{align}
\\]