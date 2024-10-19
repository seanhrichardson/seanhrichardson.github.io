---
layout: page
title: Pseudo-differential operators
---
#### Motivation
Recall that a differential operator \\(P: C_c^{\infty}(\Omega) \to C^{\infty}(\Omega)\\) is something of the following form, written in multi-index notation.
\\[
    P(x,D)u = \sum\_{\|\alpha\| \leq m} a_{\alpha}(x)D^{\alpha}u
\\]
where \\[
    D^{\alpha} = \left(\frac{1}{i}\partial_{1}\right)^{\alpha_1}\cdots\left(\frac{1}{i}\partial_{n}\right)^{\alpha_n}
\\]

An alternate way to write differential operators is through the Fourier transform. In particular, we can write
\\[
    u(x) = \mathscr{F}^{-1}(\hat{u}(\xi))
    = \frac{1}{(2\pi)^n}\int e^{i x \cdot \xi} \hat{u}(\xi) d\xi
\\]
And so
\\[
\begin{align}
    P(x,D)u &= \sum\_{\|\alpha\| \leq m} a_{\alpha}D^{\alpha}\frac{1}{(2\pi)^n}\int e^{i x \cdot \xi} \hat{u}(\xi) d\xi\\\\\
    &= \frac{1}{(2\pi)^n} \int e^{ix \cdot \xi} \left(\sum_{\|\alpha\| \leq m} a_{\alpha}(x) \xi^{\alpha}\right)\hat{u}(\xi)d\xi
\end{align}
\\]
To summarize, we can write 
\\[
    P(x,D)u = \frac{1}{(2\pi)^n} \int e^{ix \cdot \xi} a(x,\xi) \hat{u}(\xi)d\xi
\\]
where \\(a(x,\xi)\\) is called the *symbol* of \\(P(x,D)\\) and is given by
\\[
    a(x,\xi) = \sum_{\|\alpha\| \leq m} a_{\alpha}(x) \xi^{\alpha}
\\]
The form for \\(P(x,D)u\\) given in /\*refer to eqn.\*/ reveals a new way to define operators.

**Exercise.** Find the symbol \\(p(x,\xi)\\) for the operator \\(\frac{d^n}{d x^n}: C^{\infty}_c(\mathbb{R}) \to C^{\infty}(\mathbb{R})\\).

**Solution.** \\(p(x,\xi) = \xi^n\\).

**Exercise.** Find the symbol \\(p(x,\xi)\\) for the Laplace operator \\(\Delta: C^{\infty}_c(\mathbb{R}^n) \to C^{\infty}(\mathbb{R}^n)\\).

**Solution.** \\(p(x,\xi) = \|\xi\|^2\\).

#### Definition
A *pseudo-differential operator* \\(P(x,D)\\) acts on functions \\(u \in \mathscr{S}\\) by
\\[
    P(x,D)u = \frac{1}{(2\pi)^n} \int e^{ix \cdot \xi} p(x,\xi) \hat{u}(\xi)d\xi.
\\]
However, we need some restrictions on the symbol \\(p(x,\xi)\\). We require \\(p \in C^{\infty}(\Omega_x \times \mathbb{R}^n_{\xi})\\) and one extra condition so that /\*justify why need this condition\*/. In particular, we require there to exists some \\(m \in \mathbb{R}\\) such that for any multi-indices \\(\alpha, \beta\\) and compact \\(K \subset \Omega\\) there is constant \\(C_{\alpha, \beta, K} > 0\\) so that over \\(K\\) we have
\\[
    \|\partial_x^{\alpha}\partial_{\xi}^{\beta}p(x,\xi)\| \leq C_{\alpha, \beta, K}(1+\|\xi\|)^{m-\|\beta\|}
\\]
In this case the symbol \\(p(x,\xi)\\) is said to be *a symbol of order $m$* and the pseudo-differential operator is said to be of order $m$.

Furthermore, we let \\(S^m(\Omega)\\) denote the set of symbols of order \\(m\\) over \\(\Omega\\) and we let \\(\Psi^m(\Omega)\\) denote the set of pseudo-differential operators of order \\(m\\).

#### ???
**Exercise.** Show that a differential operator of order \\(m\\) is a pseudo-differential operator of order \\(m\\).

**Solution.** As discussed previously, a differential operator has symbol \\(p(x,\xi) = \sum_{\|\mu\| \leq m} a_{\mu}(x) \xi^{\mu}\\); we must show this symbol is of order \\(m\\).

Take multi-indices \\(\alpha,\beta\\) and compact set \\(K \subset \Omega\\). Then over \\(K\\) we find
\\[
\begin{align}
    \left\|\partial^{\alpha}\_x\partial^{\beta}\_{\xi}p(x,\xi)\right\|
    &= \left\|\partial^{\alpha}\_x\partial^{\beta}\_{\xi}\sum_{\|\mu\| \leq m} a_{\mu}(x) \xi^{\mu}\right\|\\\\\
    &= \left\|\sum\_{\|\mu\| \leq m}(\partial_x^{\alpha}a_{\mu}(x))(\partial_{\xi}^{\beta}\xi^\mu)\right\|\\\\\
    &\leq \max_{\|\alpha\| \leq m} \sup_{x \in K} \|\partial_x^{\alpha}a_{\mu}(x)\|\sum_{\|\mu\| \leq m}\frac{\mu!}{\beta!}|\xi^{\mu-\beta}\|\\\\\
    &\leq m!\max_{\|\alpha\| \leq m} \sup_{x \in K} \|\partial_x^{\alpha}a_{\mu}(x)\|\sum_{\|\mu\| \leq m}|\xi^{\mu-\beta}\|
\end{align}
\\]
Thus it suffices to get a bound \\(\|\xi^{\mu-\beta}\| \leq C_{\beta}(1+\|\xi\|)^{m-\|\beta\|}\\).
For this, apply the weighted AM-GM inequlity /\*link page\*/ to get
\\[
\begin{align}
    \|\xi^{\mu-\beta}\| 
    &\leq \left|\frac{1}{\|\mu-\beta\|}\sum_{i=1}^n(\mu_i-\beta_i)\xi_i\right|^{|\mu-\beta|}\\\\\
    &\leq \left|\sum_{i=1}^n\xi_i\right|^{\|\mu\|-\|\beta\|}
    \leq C\|\xi_i\|^{|\mu|-|\beta|}
    \leq C(1+\|\xi_i\|)^{|\mu|-|\beta|}
    \leq C(1+\|\xi_i\|)^{m-|\beta|}
\end{align}
\\]

/\*note that we can assume \\(\beta < \mu\\) otherwise get \\(0\\)\*/


/\*It seems it might also be possible to do this through the multinomial theorem?\*/

#### Extend to distributions
A pseudo differential operator \\(P: \mathscr{S}'(\Omega) \to \mathscr{S}'(\Omega)\\) 