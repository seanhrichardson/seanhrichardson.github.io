---
layout: page
title: Pseudo-differential operators
section: Pseudo-differential operators
---

# Bessel Potential

Consider the PDE
\\[
    (1-\Delta)u = f \quad\quad \text{in } \mathbb{R}^n.
\\]
We can take the Fourier transform of both sides and solve for the Fourier transform \\(\hat{u}(\xi)\\) of the solution.
\\[
    (1+|\xi|^2)\hat{u}(\xi) = \hat{f}(\xi) \implies \hat{u}(\xi) = \frac{1}{1+|\xi|^2} \hat{f}(\xi).
\\]
Taking the inverse Fourier transform \\(\mathcal{F}^{-1}\\) of the solution allows us to solve for the solution
\\[
    u(x) = \mathcal{F}^{-1}\left(\frac{1}{1+|\xi|^2}\hat{f}(\xi)\right).
\\]
In other words, this PDE can be solved with the *Bessel Potential* operator
\\[
    Bf := \mathcal{F}^{-1}\left(\frac{1}{1+|\xi|^2}\hat{f}(\xi)\right),
\\]
which inverts the differential operator \\((1-\Delta)\\). Such "pseudodifferential operators" appear frequently when trying to invert differential operators.

# Definition of Pseudodifferential Operators

Consider some order \\(m\\) differential operator \\(P(x,D) = \sum_{|\alpha| \leq m} a_{\alpha}(x)D^{\alpha}\\) on \\(\mathbb{R}^n\\) with \\(a_{\alpha}(x)\\) smooth and all derivatives \\(\partial^{\beta}a_{\alpha}(x)\\) bounded. Use that the Fourier transform intertwines differentiation and multiplication to compute
\begin{align}
    P(x,D)u
    &= P(x,D)\mathcal{F}^{-1}(\hat{u}(\xi))
    = \sum_{|\alpha| \leq m} a_{\alpha}(x)D^{\alpha}\mathcal{F}^{-1}(\hat{u}(\xi))\\\\\
    &= \mathcal{F}^{-1}\left(\sum_{|\alpha| \leq m} a_{\alpha}(x)\xi^{\alpha}\hat{u}(\xi)\right)
    = \mathcal{F}^{-1}\left(p(x,\xi)\hat{u}(\xi)\right)
\end{align}
where the polynomial \\(p(x,\xi) := \sum_{|\alpha| \leq m} a_{\alpha}(x) \xi^{\alpha}\\) is the *(full) symbol*. The above gives
\\[
    P(x,D)u = \mathcal{F}^{-1}\left(p(x,\xi)\hat{u}(\xi)\right).
\\]
That is, applying a differential operator to a function is equivalent to multiplying it's Fourier transform by the symbol. In other words, the Fourier transorm intertwines the differential operator and this principle symbol:
\\[
    P(x,D)\mathcal{F}^{-1} = \mathcal{F}^{-1}p(x,\xi) 
    \quad \text{or} \quad
    \mathcal{F} \circ P(x,D) = p(x,\xi) \mathcal{F}.
\\]
We saw above that the differential operator \\((1-\Delta)\\) has symbol \\(1+|\xi|^2\\). The idea of pseudodifferential operators is to consider operators with non-polynomial symbols \\(p(x, \xi)\\). For example, we defined the Bessel potential operator above to have "symbol" \\((1+\|\xi\|^2)^{-1}\\). We ask the question then: what symbols can we use to define a nice operator?

Because we are working with Fourier transforms, one particularly important property of our differential operator \\(P(x,D)\\) is the mapping property \\(P(x,D): \mathscr{S}(\mathbb{R}^n) \to \mathscr{S}(\mathbb{R}^n)\\) where \\(\mathscr{S}(\mathbb{R}^n)\\) is Schwartz space. This mapping property is due to two properties of the symbol \\(p(x, \xi)\\).  

Firstly, the symbol \\(p(x,\xi) = \sum a_{\alpha}(x)\xi^{\alpha}\\) is smooth. This allows us to write the derivatives
\\[
    \partial_x^{\gamma}(P(x,D)u)
    = \partial_x^{\gamma} \mathcal{F}^{-1}(p(x, \xi))\hat{u}(\xi)
    = \int_{\mathbb{R}^n} \partial_x^{\gamma}(e^{ix \cdot \xi}p(x, \xi))\hat{u}(\xi)d\xi
\\]
in terms of the derivatives \\(\partial_x^{\gamma}(e^{ix \cdot \xi}p(x, \xi))\\), which after expanding by product rule relies on the derivatives \\(\partial\_x^{\alpha} p_x(x,\xi)\\) of the symbol.

Secondly, the above integrals are well-defined because for differential operators with symbol \\(p(x, \xi)\\), if \\(\hat{u}(\xi) \in \mathscr{S}(\mathbb{R}^n)\\), then \\(\partial^{\alpha}p(x,\xi) \hat{u}(\xi) \in \mathscr{S}(\mathbb{R}^n)\\). To see this, compute the bound
\begin{align}
    \|\partial_{\xi}^{\beta} \partial\_{x}^{\alpha} p(x,\xi)\|
    &= \left\|\partial_{\xi}^{\beta} \partial\_{x}^{\alpha} \sum_{|\mu| \leq m} a\_{\mu}(x)\xi^{\mu}\right\|\\\\\
    &\leq \sum\_{|\mu| \leq m} |\partial_x^{\alpha}a\_{\mu}(x)|\frac{\mu!}{\beta!}\|\xi\|^{\mu-\beta}
    \leq C\sum_{|\mu| \leq m}|\xi|^{\mu - \beta}
    \leq C_{\alpha, \beta} \langle \xi \rangle^{m - \|\beta\|}.
\end{align}
where \\(\langle \xi \rangle^2 = (1+|\xi|^2)\\) is the bracket notation and we used that \\(\partial_x^{\alpha}a_{\mu}\\) are bounded. Thus two key properties of the symbol \\(p(x,\xi)\\) of a differential operator are smoothness, and that we have the bound \\(\|\partial_{\xi}^{\beta} \partial\_{x}^{\alpha} p(x,\xi)\| \leq C_{\alpha, \beta} \langle \xi \rangle^{m - \|\beta\|}\\). We then consider a more general set of symbols \\(p(x, \xi)\\) that satisfy precisely these two properties as well as the corresponding class of operators.

**Def (Symbol class \\(S^m\\).)** Given some \\(m \in \mathbb{Z}\\), define the *symbol class* \\(S^m\\) of order \\(m\\) to be all \\(p \in C^{\infty}(\mathbb{R}\_x^{n} \times \mathbb{R}^n\_{\xi})\\) so that for all \\(\alpha, \beta\\) there exists \\(C_{\alpha, \beta} > 0\\) so that
\\[
    \|\partial_{\xi}^{\beta}\partial_{x}^{\alpha}p(x, \xi)\| \leq C_{\alpha, \beta}\langle \xi \rangle^{m-|\beta|}.
\\]

**Def (Pseudodifferential operator).** For some \\(p \in S^m\\), we define its *quantization* \\(P = \\operatorname{Op}(p)\\) to be the operator
\\[
    Pf(x) := (2\pi)^{-1}\int\_{\mathbb{R}^n} e^{ix \cdot \xi} p(x, \xi) \hat{f}(\xi)d\xi.
\\]
This operator \\(P\\) is called a *pseudodifferential operator of order \\(m\\)* and the set of all pseudodifferential operators of order \\(m\\) is denoted
\\(
    \Psi^m = \\{\operatorname{Op}(p): p \in S^m\\}.
\\)

Later we may consider an alternate bound on the derivatives of the symbols, but the symbol class as defined above is the most common and most closely resembles the bound on differential operators, which results in nice Sobolev mapping properties. Note that the definitions above immediately generalize to \\(m \in \mathbb{R}\\).



