---
layout: page
title: Riemannian Metric
---

#### Define Riemannian Metric

#### Using Riemmannian Metric (Maybe next page?)

/\*need to define tangent vectors somewhere\*/

/\*give formal and informal decscriptions?\*/

/\*length\*/

The length of a curve $\gamma: [a,b] \to M$ is defined by
\\[
    \operatorname{length}(\gamma) = \int_a^b \|\gamma'(t)\|_g dt
    = \int_a^b \sqrt{g(\gamma'(t), \gamma'(t))} dt.
\\]

However, to compute the length in practice, we will have an expression for \\(\gamma(t)\\) in coordinates $(x^i)$, which we can write as
\\[
    \gamma(t) = (x^1(t), \cdots, x^n(t))
\\]
Then we have /\*justify... will require using however I define tangent vectors\*/
\\[
    \gamma'(t) = \frac{\partial x^i}{\partial t}\partial_{x^i}
\\]

<p>
With this, a more practical formula for the length of the curve $\gamma$ is given by
\[
     \operatorname{length}(\gamma)
    = \int_a^b \sqrt{g(\gamma'(t), \gamma'(t))} dt
    = \int_a^b \sqrt{g \left(\frac{\partial x^i}{\partial t}\partial_{x^i},\frac{\partial x^j}{\partial t}\partial_{x^j}\right)}dt
    = \int_a^b \sqrt{g_{ij} \frac{\partial x^i}{\partial t} \frac{\partial x^j}{\partial t}}dt.
\]
</p>