---
layout: page
title: L2 spaces
---

## \\(L^2\\) spaces

#### Fourier Series Motivation

Consider a continuous periodic function \\(f\\) and note by periodicity we can consider \\(f(\theta)\\) as a function on the circle \\(f: \mathbb{S}^1 \to \mathbb{C}\\). Recall such a function has fourier series decomposition
\\[
    f(\theta) = \sum_{k = -\infty}^{\infty} a_k e^{ik\theta}, \quad \quad a\_k = \frac{1}{2\pi} \int_{0}^{2\pi}f(\theta)e^{-ik\theta}d\theta.
\\]
Notice this decomposition resembles writing a vector in terms of an orthornormal basis. Indeed, the coefficients \\(a\_k\\) are defined as integrals of the form \\(\int_{S^1} f \overline{g}\\) which plays the role of an inner product. Due to the inequality
\\[
    \left\|\int\_{\mathbb{S}^1}f\overline{g}\right\| < \int\_{\mathbb{S}^1}|f|^2\int\_{\mathbb{S}^1}|g|^2,
\\]
this inner product is guaranteed to exist so long as \\(u\\) and \\(v\\) are in the space
\\[
    L^2(\mathbb{S}^1) = \left\\{u \text{ measurable} : \int_{\mathbb{S}^1}|u|^2 < \infty\right\\}.
\\]
The natural inner product on this space is denoted by
\\[
    \langle f , g\rangle = \int_{\mathbb{S}^1} f \overline{g}.
\\]
With this insight, notice that the functions \\(e^{ik\theta}\\) seem to play the role of the orthornormal basis in the Fourier decomposition, and indeed we can compute that \\(\int_{0}^{2\pi} |e^{ik\theta}|^2 d\theta = 2\pi < \infty\\) and that \\(\int_{0}^{2\pi} e^{ik\theta}e^{-il\theta} d\theta = 0\\) for \\(k \neq l\\).

#### \\(L^2\\) Spaces

More generally, given a measure space \\((X, \mu)\\) we can consider the vector space of functions defined by
\\[
    L^2(X) := \left\\{f \text{ measurable } : \int_{X} f d\mu < \infty \right\\}
\\]
together with the inner product
\\[
    \langle f , g\rangle := \int_X f\overline g d\mu.
\\]
This generalization has many applications throughout mathematics. For example: \\(L^2(\mathbb{R}^n)\\) is a natural domain for the Fourier transform, /\*QM, PDES, ... ?\*/

/\*verify is a vector space\*/

/\*verify is an inner product\*/

#### \\(L^2(X)\\) as a metric space

/\*talk about topology, continuous functions, etc.\*/

/\*completeness of metric?\*/