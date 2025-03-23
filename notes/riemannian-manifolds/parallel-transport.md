---
layout: page
title: Parallel Transport
section: Parallel Transport
---

# Parallel Transport

Consider a smooth manifold \\(M\\) with connection \\(\nabla\\) and smooth curve \\(\gamma: I \to M\\). The connection \\(\nabla\\) induces a covariant derivative \\(D_t\\), which allows us to differentiate along \\(\gamma\\). This in turn provides a notion of a "constant" vector field along \\(\gamma\\) if its covariant derivative is \\(0\\). Equivalently, this provides a natural way to "connect" tangent spaces along \\(\gamma\\) by moving one tangent space to another in a constant way (in fact, this is why \\(\nabla\\) is called a "connection"). This notion of "constant" is formalized in the following definition.

**Def. (Parallel Vector field)** A vector field \\(X\\) over a curve \\(\gamma: I \to M\\) is *parallel* if its covariant derivative \\(D_t\\) along \\(\gamma\\) is identically zero: \\(D_t X = 0\\).

Given a curve \\(\gamma: [t\_0, t\_1] \to M\\) We may now identify \\(v \in T\_{\gamma(t_0)}\\) with an element of \\(T_{\gamma(t\_1)}\\) by extending \\(v\\) to a parallel vector field \\(X\\). That is, by choosing a vector field \\(X\\) along \\(\gamma\\) such that \\(X(t\_0) = v\\) and \\(D_t X = 0\\). In local coordinates, this is the requirement that
\\[
    \begin{cases}
        X^k(t_0) = v^k, \\\\\
        0 = D_t X = \dot{X}^k(t) \partial\_k + \dot{\gamma}^i X^j A^{k}\_{ij} \partial\_k
    \end{cases}
    \tag{1}
    \label{eq:pt-ode}
\\]
where \\(A^{k}\_{ij}\\) are the connection coefficients. Thus by the existence, uniqueness, and smoothness of ODEs, there exisits a unique smooth solution \\(X(t)\\) although there is some technical work to formally verify this (see Lee *Introduction to Riemannian manifolds* Theroem 4.31).

**Def. (Parallel transport)** Given a smooth curve \\(\gamma: [t\_0, t\_1] \to M\\) and an initial vector \\(v \in T\_{\gamma(t\_0)}M\\), the unqiue solution \\(X\_v(t) \in T\_{\gamma(t)}M\\) is called the *parallel transport of \\(v\\)*. The *parallel transport map* \\(P\_{t\_0, t\_1}^{\gamma}M: T\_{\gamma(t\_0)} \to T\_{\gamma(t\_1)}\\) is given by \\(P^{\gamma}\_{t\_0, t\_1}v = X\_v(t)\\).

## Parallel Frames

When doing computations involving parallel transport along a curve, it is often convenient to work with "parallel frames", defined as follows.

**Def. (Parallel frame).** A frame \\(E\_i\\) along a curve \\(\gamma: I \to M\\) is called a *parallel frame* if all the vector fields \\(E\_i\\) are parallel along \\(\gamma\\); that is, \\(D\_t E_i = 0\\). Note such a parallel frame always exists by choosing a basis \\(v\_i \in T\_{\gamma(t\_0)}\\) for \\(t\_0 \in U\\), then extending each \\(v\_i\\) to a parallel vector field \\(E\_i\\) along \\(\gamma\\) by parallel transport. When working with covariant differentiation or parallel transport of a vector field \\(X(t)\\) along a curve \\(\gamma\\), writing \\(X(t) = X^i(t) E_i(t)\\) in terms of this parallel frame often simplifies computation. For example, by product rule of covariant differentiation and \\(D\_t E\_i = 0\\), we get the simple relation
\\[
    D\_t X(t)
    = D\_t (X^i(t) E_i(t))
    = \frac{d }{d t} X^i(t) E_i + X^i(t) D\_t E\_i = \left\(\frac{d }{d t} X^i(t)\right\) E\_i.
    \tag{2}
    \label{eq:frame-expression}
\\]

## Parallel transport determines the connection

Thus we have seen connection provides covariant differentiation along curves, giving a notion of "constant" along curves, which allows for the notion of parallel transport to identify tangent spaces along a curve. In fact, a connection an a notion of parallel transport is like "the chicken and the egg" -- the parallel transport conversely uniquely determines the underlying connection and the covariant differentiation. Indeed, recall the problem that motivated the connection: because \\(X(t_0)\\) and \\(X(t)\\) lie in different tangent spaces, there is no canonical way to differentiate vector fields on a manifold. However, given a parallel transport map \\(P^{\gamma}\\), we can transport \\(X(t)\\) to share the same vector space as \\(X(t_0)\\), then we have no problem differentiating to define a covariant derivative by
<!-- TODO: link the connection page -->
\\[
    D\_t X(t\_0)
    = \left.\frac{d }{d t}\right\|\_{t=t\_0} P^{\gamma}\_{t,t\_0} X(t)
    = \lim\_{t \to t\_0} \frac{P^{\gamma}\_{t,t\_0} X(t) - X(t\_0)}{t-t\_0}.
    \tag{3}
    \label{eq:pt-covariant-der}
\\]

**Prop (\\(\mathbf{P^{\gamma}}\\) determines \\(\mathbf{D\_t}\\)).** Suppose a covariant derivative \\(D\_t\\) over a smooth manifold \\(M\\) induces parallel transport map \\(P^{\gamma}\\) over a curve \\(\gamma\\). Then \\(D\_t\\) may be recovered from \\(P^{\gamma}\\) by (\ref{eq:pt-covariant-der}).

*Proof.* We verify (\ref{eq:pt-covariant-der}) by a computation using a parallel frame \\((E\_i)\\) along \\(\gamma\\). Indeed, write \\(X(t) = X^i(t)E\_i(t)\\) and compute
\\[
    \left.\frac{d }{d t}\right\|\_{t=t\_0} P\_{t,t\_0}^{\gamma} X(t)
    = \left.\frac{d }{d t}\right\|\_{t=t\_0} X^i(t) P^{\gamma}\_{t,t\_0} E\_i(t)
    = \left.\frac{d }{d t}\right\|\_{t=t\_0} X^i(t) E\_i(t\_0)
    = \dot{X}^i(t\_0) E\_i(t\_0)
    = D\_tX(t\_0).
\\]
where we used (\ref{eq:frame-expression}) in the last step.

Similarly, parallel transport determines the connection \\(\nabla\\). Indeed, given vector fields \\(X\\) and \\(Y\\) over \\(M\\), to compute \\(\nabla\_X Y \|\_p\\) choose a curve \\(\gamma(t)\\) such that \\(\gamma'(0) = X\_p\\). Then, using (\ref{eq:pt-covariant-der}) we have the relation
\\[
    \nabla\_X Y\|\_p = D\_t Y(0) = \left.\frac{d }{d t}\right\|\_{t=0}P\_{t,0}^{\gamma} Y\_{\gamma(t)}.
\\]