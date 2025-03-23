---
layout: page
title: Covariant Derivative
section: Covariant Derivative
---

# Covariant Derivative

Given a smooth manifold \\(M\\) with connection \\(\nabla\\), we often use the connection to differentiate a vector field \\(X\\) along a curve \\(\gamma(t)\\) over \\(M\\) by \\(\nabla\_{\dot{\gamma}(t)}X\\). Using the notation \\(X(t) := X\_{\gamma(t)}\\), we can compute this expression in coordinates to be
\\[
\begin{align}
    \nabla\_{\dot{\gamma}(t)} X
    &= \nabla\_{\dot{\gamma}(t)}(X^j \partial\_j)\\\\\
    &= (\dot{\gamma}(t) X^j) \partial\_j + X^j \nabla\_{\dot{\gamma}^i(t) \partial\_i} \partial\_j\\\\\
    &= (\dot{X}^k(t) + X^j(t)\dot{\gamma}^i(t) A\_{ij}^k(\gamma(t)))\partial\_k
\end{align}
\tag{CD}
\label{eq:cd-coord}
\\]
where \\(A\_{ij}^k\\) are the connection coefficients defined by \\(\nabla\_{\partial\_i}\partial\_j = A\_{ij}^k \partial\_k\\). However, notice the expression (\ref{eq:cd-coord}) allows us to consider more generally any smooth \\(X: I \to TM\\) with \\(X(t) \in T\_{\gamma(t)} M\\), which is called a *vector field along \\(\gamma\\)*. Note in particular this allows \\(X(t\_1) \neq X(t\_2)\\) even if \\(\gamma(t\_1) = \gamma(t\_2)\\), which is often a necessary generalization.

**Def (Covariant derivative).** The *covariant derivative* \\(D\_t X\\) of a vector field \\(X\\) along a curve \\(\gamma\\) is defined in local coordinates by (\ref{eq:cd-coord}).

## Properties of covariant differentiation

The covariant derivative enjoys serval nice properties. Indeed, suppose a vector field \\(V\\) along a curve \\(\gamma\\) is *extendible*, meaning \\(V(t) = \widetilde{V}\_{\gamma(t)}\\) for a vector field \\(\widetilde{V}\\) over \\(M\\). Then, because the coordinate expression of \\(D\_t V\\) is defined exactly to be \\(\nabla\_{\dot{\gamma}(t)} V\\), we have by definition
\\[
    D\_t V = \nabla\_{\dot{\gamma}(t)} \widetilde{V}.
    \tag{1}
    \label{eq:extension}
\\]

As the coordinate definition of covariant differentiation is defined by the coordinate expression of the connection, the covariant derivative, like the connection, is linear over \\(\mathbb{R}\\). Indeed, take vector fields \\(V\\) and \\(W\\) over a curve \\(\gamma\\) together with \\(a, b \in \mathbb{R}\\) and compute
\\[
\begin{align}
    D\_t(a V(t) + b W(t))
    &= ((a \dot{V}^k(t) + b\dot{W}^k(t)) + (aV^j(t) + bW^j(t)) \dot{\gamma}^i(t) A^k\_{ij}) \partial\_k\\\\\
    &= a(\dot{V}^k + V^j(t) \dot{\gamma}^i(t) A^k\_{ij})\partial\_k
    + b(\dot{W}^k(t) + W^j(t) \dot{\gamma}^i(t) A^k\_{ij})\partial\_k
    = aD\_t V + bD\_t W.
\end{align}
\tag{2}
\label{eq:linearity}
\\]
Finally, covariant differentiation, like the connection, enjoys a product rule. Take a function \\(f: I \to \mathbb{R}\\) and compute
\\[
\begin{align}
    D\_t(fV)
    &= \left\( \frac{d }{d t}(f(t) V^k(t)) + f(t) \dot{\gamma}^i(t) V^j(t) A^k\_{ij} \right\) \partial\_k \\\\\
    &= (f'(t) V^k(t) + f(t)\dot{V}^k(t) + f(t) \dot{\gamma}^i(t) V^j(t) A^k\_{ij}) \partial\_k\\\\\
    &= f'(t)V^k(t)\partial\_k + f(t)\left\( \dot{V}^k(t) + \dot{\gamma}^i(t) V^j(t) A^k\_{ij}\right\)\partial\_k
    = fV + fD\_t V.
\end{align}
\tag{3}
\label{eq:product-rule}
\\]

We summarize these important properties in the following proposition.

**Prop (Properties of \\(\mathbf{D\_t}\\)).** The covariant derivative \\(D\_t\\) over a curve \\(\gamma\\) satisfies the following properties.
1. For any extension of \\(V\\) to a vector field \\(\widetilde{V}\\) over \\(M\\), we have
\\[
    D\_t V = \nabla\_{\dot{\gamma}(t)} \widetilde{V}.
\\]
2. Linearity over over \\(\mathbb{R}\\). For any vector fields \\(V, W\\) over \\(\gamma\\) and \\(a,b \in \mathbb{R}\\):
\\[
    D\_t(a V(t) + b W(t)) = aD\_t V + bD\_t W.
\\]
3. Product rule. For any vector field \\(V\\) over \\(\gamma\\) and \\(f: I \to \mathbb{R}\\):
\\[
    D\_t(fV) = fV + fD\_t V.
\\]
Furthermore, the properties above uniquely characterize \\(D\_t\\).

*Proof.* We have already verified these properties above in (\ref{eq:extension}), (\ref{eq:linearity}), (\ref{eq:product-rule}) respectively, so it only remains to prove these properties uniquely characterize \\(D\_t\\) along a curve \\(\gamma\\). Indeed, take a vector field \\(V(t)\\) along \\(\gamma\\) and choose some time \\(t\_0\\). Then in local coordinates near \\(\gamma(t\_0)\\) write \\(V(t) = \left.V^j(t) \partial\_j\right\|\_{\gamma(t)}\\). Now use the above properties, noting that \\(\left.\partial\_j\right\|_{\gamma(t)}\\) extends to \\(\partial\_j\\), to compute
\\[
\begin{align}
    D\_tV(t)
    &= D\_t(V^j(t) \left.\partial\_j\right\|\_{\gamma(t)})\\\\\
    &= \dot{V}^j(t) \left.\partial\_j\right\|\_{\gamma(t)} + V^j(t) D\_t \left.\partial\_j\right\|\_{\gamma(t)}\\\\\
    &= \dot{V}^j(t) \left.\partial\_j\right\|\_{\gamma(t)} + V^j(t) \nabla\_{\dot{\gamma}^i(t) \partial\_i} \left.\partial\_j\right\|\_{\gamma(t)}\\\\\
    &= (\dot{V}^k(t) + \dot{\gamma}^i(t) V^j(t) A^k\_{ij}(\gamma(t))) \left.\partial\_k\right\|\_{\gamma(t)}.
\end{align}
\\]
Thus from these properties we recover the coordinate formula for \\(D\_t\\).
<div style="text-align: right"> \(\square\) </div>

<!-- note that we technically need to verify locality to justify going into coordinates? -->