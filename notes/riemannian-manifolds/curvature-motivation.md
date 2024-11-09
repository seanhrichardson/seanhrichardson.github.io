---
layout: page
section: NOTES
title: Curvature Motivation
---

# Motivation for the Riemann Curvature Tensor

<!-- /\*todo: animations for this page (parallel transport, etc.)\*/

/\*\\approximation \\(P_t X_p - X_q \approx t \nabla_{\dot{\gamma}(0)}X\\) might be off by a negative...?\*/ -->

<!-- ## Noncommutativity of Parallel Transport -->

## Studying Isometries

An important questions in Riemannian geometry is: given two Riemannian manifolds, are they isometric? A first step to answering this extremely hard problem is to consider the following local question: given two different coordinate neighborhoods of Riemannian manifolds, are they isometric? This is still extremely hard, but a more reasonable place to start is: when does a point on a Riemannian manifold have a *flat neighborhood* (a neighborhood isometric to a neighborhood of \\(\mathbb{R}^n\\))? This question was answered by Riemann and the investigation of this problem naturally gives rise to the *Riemann curvature tensor*, which precisely encodes the extent to which a manifold fails to be flat at every point.

## (Non)commutativity of Parallel Transport

First, notice that parallel transport in \\(\mathbb{R}^n\\) is path independent: for example, transporting a vector along the \\(x^1\\) axis, then the \\(x^2\\) axis will yield the same vector as transporting along \\(x^2\\), then \\(x^1\\). Thus path independence of parallel transport is a necessary condition for a neighborhood to be flat. Importantly, path-independence of parallel transport is also sufficient, for it allows us to construct flat coordinates as follows. Begin with an orthornormal basis \\(\\{e_i\\}\\) of \\(T\_pM\\), then if parallel transport is path-independent in a neighborhood \\(U\\) of \\(p\\), transporting this basis along any choice of paths yields the same frame \\(E_i\\) in \\(U\\), implying each \\(E_i\\) is parallel in *every direction*. Because parallel transport preserves inner product, this frame is orthornormal. We only need to check that \\(E\_i\\) is a coordinate frame, which occurs precisely when \\(E\_i\\) is a commuting frame; indeed, because each \\(E_i\\) is parallel in every direction, we have \\(\nabla_X E_i = 0\\) for any \\(X\\) and so we compute
\\[
    [E\_i, E\_j] = \nabla_{E\_i}E\_j - \nabla_{E\_j}E\_i = 0 - 0 = 0.
\\]

Thus we study the path-dependence of parallel transport. We quantify this by investigating the noncommutativity of parallel transport around small squares. Consider the square \\(I \times I \to M\\) parametrized by \\((s,t)\\) such that \\(p\\) corresponds to \\((0,0)\\) and choose some tangent vector \\(v \in T\_p M\\). Then we compare the following two methods of transporting \\(v\\) to the point \\((\varepsilon, \delta)\\). We could first transport \\(v\\) in the \\(s\\) direction from \\((0,0)\\) to \\((\varepsilon, 0)\\), which we denote \\(P^{(0,0)}\_{(\varepsilon,0)}v \in T\_{(\varepsilon,0)}\\), then transport this vector in the \\(t\\) direction from \\((\varepsilon, 0)\\) to \\((\varepsilon, \delta)\\) to get \\(P\_{(\varepsilon,\delta)}^{(\varepsilon,0)}P^{(0,0)}\_{(\varepsilon,0)}v \in T\_{(\varepsilon,\delta)}M\\). Alternatively, we could first transport \\(v\\) in the \\(t\\) direction from \\((0,0)\\) to \\((0, \delta)\\) yielding \\(P^{(0,0)}\_{(0,\delta)}v \in T\_{(0,\delta)}\\), then transport this vector in the \\(s\\) direction from \\((0, \delta)\\) to \\((\varepsilon, \delta)\\) resulting in \\(P\_{(\varepsilon,\delta)}^{(0,\delta)}P^{(0,0)}\_{(0,\delta)}v \in T\_{(\varepsilon,\delta)}M\\). The difference between these two methods is quantified by

\\[
    P\_{(\varepsilon,\delta)}^{(\varepsilon,0)} P\_{(\varepsilon,0)}^{(0,0)} v - P\_{(\varepsilon,\delta)}^{(0,\delta)} P\_{(0,\delta)}^{(0,0)} v.
\\]
We now compute a Taylor approximation of this difference. One trick to simplify this computation is to extend \\(v\\) to any vector field \\(X\\), then compare the value of \\(X\\) to the parallel transport of \\(v\\) along each of the four segments, giving
\begin{align}
    &P\_{(\varepsilon,\delta)}^{(\varepsilon,0)} P\_{(\varepsilon,0)}^{(0,0)} X_{(0,0)} - P\_{(\varepsilon,\delta)}^{(0,\delta)} P\_{(0,\delta)}^{(0,0)} X_{(0,0)}.\\\\\
    &= (P\_{(\varepsilon,\delta)}^{(\varepsilon,0)}(P\_{(\varepsilon,0)}^{(0,0)}X\_{(0,0)} - X\_{(\varepsilon,0)})
    - (P\_{(\varepsilon,\delta)}^{(0,\delta)}X\_{(0,\delta)} - X\_{(\varepsilon,\delta)}))\\\\\
    &- (P\_{(\varepsilon,\delta)}^{(0,\delta)}(P\_{(0,\delta)}^{(0,0)}X\_{(0,0)} - X\_{(0,\delta)})
    - (P\_{(\varepsilon,\delta)}^{(\varepsilon,0)}X\_{(\varepsilon,0)} - X\_{(\varepsilon,\delta)})).
\end{align}
Recall that the parallel transport \\(P\_t\\) of a vector field \\(X\\) from \\(p\\) to \\(q\\) along a curve \\(\gamma: [0, \varepsilon] \to M\\) is approximated by \\(P_t X_p - X_q \approx t \nabla_{\dot{\gamma}(0)}X\\). Applying this approximation to the above yields
\begin{align}
    &P\_{(\varepsilon,\delta)}^{(\varepsilon,0)} P\_{(\varepsilon,0)}^{(0,0)} X_{(0,0)} - P\_{(\varepsilon,\delta)}^{(0,\delta)} P\_{(0,\delta)}^{(0,0)} X_{(0,0)}.\\\\\
    &\approx \varepsilon(P\_{(\varepsilon,\delta)}^{(\varepsilon,0)}(\nabla\_{\partial\_s}X)\_{(\varepsilon, 0)}
    - (\nabla\_{\partial_s}X)\_{(\varepsilon, \delta)})
    - \delta(P\_{(\varepsilon,\delta)}^{(0, \delta)}(\nabla\_{\partial\_t}X)\_{(0, \delta)}
    - (\nabla\_{\partial_t}X)\_{(\varepsilon, \delta)})\\\\\
    &\approx \varepsilon\delta (\nabla_{\partial\_t}\nabla_{\partial\_s} X - \nabla_{\partial\_s}\nabla_{\partial\_t} X).
\end{align}

In the above computation, we used the approximation \\(P_t X_p - X_q \approx t \nabla_{\dot{\gamma}(0)}X\\), but even if we had used the full Taylor expansion, we will find that the above is precisely the quadratic term of the Taylor expansion of our original expression.

**Exercise.** Compute the exact Taylor expansion of the difference in parallel transports and verify the quadratic term is the same as our approximation above.

Thus this difference \\(\nabla_{\partial\_t}\nabla_{\partial\_s} X - \nabla_{\partial\_s}\nabla_{\partial\_t} X\\) approximates the failure of parallel transport around small squares parametrized by \\((s,t)\\) to commute and hence is a natural obstruction to a point having a flat neighborhood. To get more obstructions, we could choose coordinates \\((x^k)\\) and study the failure for parallel transport to commute around the small coordinate square parametrized by \\((x^i, x^j)\\) for any \\(i,j\\), which would be approximated by \\(\nabla_{\partial\_{i}}\nabla_{\partial\_{j}} X - \nabla_{\partial\_{j}}\nabla_{\partial\_{i}} X\\). This difference for all such pairs \\((i,j)\\) gives more obstructions to local flattness (in fact, we will prove later these are the *only* obstructions). Next, we can encode these differences \\(\nabla_{\partial\_{i}}\nabla_{\partial\_{j}} X - \nabla_{\partial\_{j}}\nabla_{\partial\_{i}} X\\) in a coordinate-independent way by extending to a tensor field. In fact, note these differences are already tensorial in \\(X\\).

**Exercise.** Verify that \\(\nabla_{\partial\_{i}}\nabla_{\partial\_{j}} X - \nabla_{\partial\_{j}}\nabla_{\partial\_{i}} X\\) is tensorial in \\(X\\) by computing 
\\[
    \nabla_{\partial\_{i}}\nabla_{\partial\_{j}} (fX) - \nabla_{\partial\_{j}}\nabla_{\partial\_{i}} (fX) 
    = f(\nabla_{\partial\_{i}}\nabla_{\partial\_{j}} X - \nabla_{\partial\_{j}}\nabla_{\partial\_{i}} X)
\\]

We now extend \\(\nabla_{\partial\_{i}}\nabla_{\partial\_{j}} X - \nabla_{\partial\_{j}}\nabla_{\partial\_{i}} X\\) to a tensor field \\(R\\) that takes \\(3\\) vector fields and outputs \\(1\\) vector field. We know how this vector field should behave on the coordinate frame: \\(R(\partial_{i}, \partial_{j})Z = \nabla_{\partial\_{i}}\nabla_{\partial\_{j}} Z - \nabla_{\partial\_{j}}\nabla_{\partial\_{i}} Z\\) for some vector field \\(Z\\). Thus we extend this to a tensor taking as input arbitrary vector fields \\(X = X^i\partial_i\\) and \\(Y = Y^j\partial_j\\) by defining
\\[
    R(X, Y)Z = X^iY^jR(\partial_i, \partial_j)Z 
    = X^iY^j\nabla_{\partial\_{i}}\nabla_{\partial\_{j}} Z - Y^jX^i\nabla_{\partial\_{j}}\nabla_{\partial\_{i}} Z
\\]
This is the *Riemann curvature tensor*, which will encodes all obstructions to a manifold being locally flat. In fact, we can rewrite the Riemann curvature tensor in a form that is independent of coordinates. Indeed, notice the terms appearing in the Riemann curvature tensor are components of \\(\nabla\_X\nabla\_Y Z\\) and \\(\nabla\_Y\nabla\_X Z\\) after product rule:
\begin{align}
    \nabla\_X\nabla\_Y Z 
    &= \nabla\_{X^i\partial_i}\nabla\_{Y^j\partial_j} Z 
    = X^iY^j\nabla\_{\partial_i}\nabla\_{\partial_j} Z + X^i\partial\_iY^j\nabla_{\partial_j}Z\\\\\
    &\text{and}\\\\\
    \nabla\_Y\nabla\_X Z 
    &= \nabla\_{Y^j\partial_j}\nabla\_{X^i\partial_i} Z 
    = Y^jX^i\nabla\_{\partial_j}\nabla\_{\partial_i} Z + Y^j\partial\_jX^i\nabla_{\partial_i}Z
\end{align}
Thus using the above identities, we can rewrite the curvature tensor in a coordinate independent form as
    \begin{align}
        & X^iY^j\nabla_{\partial\_{i}}\nabla_{\partial\_{j}} Z - Y^jX^i\nabla_{\partial\_{j}}\nabla_{\partial\_{i}} Z\\\\\
        &= \nabla\_X\nabla\_Y Z - X^i\partial\_iY^j\nabla_{\partial_j}Z 
        - \nabla\_Y\nabla\_X Z 
        + Y^j\partial\_jX^i\nabla_{\partial_i}Z\\\\\
        &=  \nabla\_X\nabla\_Y Z - \nabla\_Y\nabla\_X Z - \nabla\_{X^i\partial_iY^j \partial_j - Y^j\partial_jX^i \partial_i}Z\\\\\
        &= \nabla\_X\nabla\_Y Z - \nabla\_Y\nabla\_X Z - \nabla\_{[X,Y]}Z
    \end{align}
Therefore we have derived a coordinate free expression for the Riemann curvature tensor! This expression makes for a much better formal definition to work with.

**Def (Riemann Curvature Tensor).** The *Riemann curvature tensor* is the \\((3,1)\\) tensor \\(R(X,Y)Z := \nabla^2\_{X,Y} Z - \nabla^2\_{Y,X} Z\\). 

By how we derived this expression, we expect this to encode obstructions to a manifold being locally flat and to quantify the failure for parallel transport to commute. This is indeed the case and we can now reverse the logic of this derivation to formally prove these properties.


<!-- 
#### Noncommutativity of Parallel Transport

/\*describe the intuition...\*/

/\*maybe replace with \\(\delta\\) and \\(\varepsilon\\)\*/ /\*explain below more\*/

/\*maybe make the below argument visually as intuition\*/

\\[
\begin{align}
    &P\_\{(S,T)}^\{(S,0)} P\_\{(S,0)}^\{(0,0)} X\_{(0,0)} - P\_\{(S,T)}^\{(0,T)} P\_\{(0,T)}^\{(0,0)}X\_{(0,0)}\\\\\
    &= ((X\_{(S,T)} - P\_\{(S,T)}^\{(0,T)}X\_{(0,T)})
    - P\_\{(S,T)}^\{(S,0)}(X\_{(S,0)} - P\_\{(S,0)}^\{(0,0)}X\_{(0,0)}))\\\\\
    &- ((X\_{(S,T)} - P\_\{(S,T)}^\{(S,0)}X\_{(S,0)})
    - P\_\{(S,T)}^\{(0,T)}(X\_{(0,T)} - P\_\{(0,T)}^\{(0,0)}X\_{(0,0)}))\\\\\
    roughly equal to... (not exact because of parallel transport)
    &\approx \int\_{0}^S (D_s X)\_{(s,T)} ds - \int\_{0}^S (D_s X)\_{(s,0)} ds 
    - \left(\int\_{0}^T (D\_t X)\_{(S,t)} dt - \int\_{0}^T (D\_t X)\_{(0,t)} dt\right)\\\\\
    &= \int\_{0}^S \int\_{0}^T (D\_tD\_s X)\_{(s,t)} dt ds
    -  \int\_{0}^T \int\_{0}^S (D\_tD\_s X)\_{(s,t)} ds dt\\\\\
    &= \int\_{0}^S \int\_{0}^T (D\_tD\_s X)\_{(s,t)} - (D\_sD\_t X)\_{(s,t)} dt ds\\\\\
    &\approx st (D\_tD\_s X - D\_sD\_t X)\_{(0,0)}
\end{align}
\\]

**Thm (Curvature and Parallel Transport).** /\*todo\*/

*Proof.* /\*TODO\*/ -->