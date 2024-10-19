---
layout: page
title: Poisson Equation on Closed Manifold
---

## Poisson Equation on Closed Manifold

/\*
background todo (in order)
- poincare inequality
- harmonic functions on closed manifolds
- Riesz representation
- holder's inequality
\*/

/\*todo: all the below is in the real case... need to add conjugates to inner products for the complex case\*/

Recall the Poisson equation is
\\[
    \Delta u = f.
\\]
Given a closed (i.e. compact and without boundary) Riemannian manifold \\(M\\), we interpret this PDE so that \\(\Delta\\) represents ths Laplace-Beltrami operator, and \\(u\\) and \\(f\\) are functions over \\(M\\). In this page we answer the question: given \\(f \in C^{\infty}(M)\\) does there exist a \\(u \in C^{\infty}\\) solving \\(\Delta u = f?\\)

#### A necessary condition on \\(f\\)

First observe that for any functions \\(u\\) and \\(f\\) on \\(M\\) satisfying \\(\Delta u = f\\) we find by applying integration by parts that
\\[
    \begin{align}
        \int\_M f 
        = \int\_M \Delta u 
        = \int\_M 1 \cdot \operatorname{div}(\nabla u)
        = \int\_M \nabla(1) \cdot \nabla u
        = 0
    \end{align}
\\]
where \\(\nabla\\) represents the gradient. Thus for there to exist a solution to \\(\Delta u = f\\), we require \\(f\\) to satisfy \\(\int\_M f = 0\\). We will now prove that this condition is sufficient.

#### Existence of solution if \\(\int\_M f = 0\\)

**Theorem.** Given \\(f \in C^{\infty}(M)\\) on a closed Riemannian manifold \\(M\\) such that \\(\int\_M f = 0\\), there exists a solution \\(u \in C^{\infty}(M)\\) to the Poisson equation \\(\Delta u = f\\). Furthermore, this solution is unique up to a constant.

*Proof.* Now we assume \\(\int\_M f = 0\\) for \\(f \in C^{\infty}(M)\\) and show there exists some \\(u\\) such that \\(\Delta u = f\\). /\*summarize following technique\*/

Recall that (by the fundamental lemma of the calculus of variations), that \\(u \in C^{\infty}(M)\\) satisfies \\(\Delta u = f\\) if and only if \\(\int\_M \Delta u \varphi = \int\_M f \varphi\\) for all test functions \\(\varphi \in C^{\infty}(M)\\). By integration by parts, this is equivalent to \\(\int\_M \nabla u \cdot \nabla \varphi = \int\_M f \varphi\\). We use the Riesz representation theorem to show the existence of such a \\(u\\) by defining the inner product
\\[
    \langle u , v\rangle\_H := \int\_M \nabla u \cdot \nabla v
\\]
on the Hilbert space \\(H := \\{v \in H^1(M): \int\_M v = 0\\}\\), which consists of functions in the Sobolev space \\(H^1(M)\\) whose average value is \\(0\\). We will now prove that 
1. \\(\langle \cdot , \cdot \rangle\_H\\) is an inner product on \\(H\\).
2. The linear functional \\(\ell(\varphi) := \int\_M f \varphi\\) is a bounded linear operator on \\(H\\).

Note that once we prove the above, then by the Riesz representation theorem there exist a unique \\(u \in H\\) such that \\(\langle u , \varphi\rangle\_H = \ell(\varphi)\\) for all \\(\varphi\\). In other words, there exists \\(u \in H\\) such that 
\\[
    \int\_M \nabla u \cdot \nabla v = \int\_M f \varphi
\\]
and so we will have shown the existence of a weak solution \\(u \in H\\) so that \\(\Delta u = f\\) in the weak sense. Then by elliptic regularity /\*link\*/ we have that \\(u \in C^{\infty}(M)\\) and so \\(u\\) will be a classical solution.

Thus we turn towards showing \\(\langle \cdot , \cdot \rangle\_H\\) is an inner product on \\(H\\). Bilinearity and symmetry are immediate. For positive-definiteness, recall Poincaré's inequality that for \\(u \in H\\) we have /\*link\*/
\\[
    \int\_M \|u\|^2 \leq C\int\_M \|\nabla u\|^2
\\]
for some \\(C > 0\\). Thus if \\(\int\_M \|\nabla u\|^2 = 0\\), then \\(\int\_M \|u\|^2 = 0\\), which implies \\(u = 0\\).

Next we show \\(\ell: H \to \mathbb{R}\\) is a bounded linear functional. That \\(\ell\\) is linear is immediate, and we can show boundedness by applying Hölder's inequality, then Poincaré's inequality:
\\[
    \begin{align}
        \|\ell(\varphi)\|^2
        = \left\|\int\_M \varphi f\right\|^2 
        \leq \left(\int\_M \|\varphi f\|\right)^2
        \leq \int\_M \|f\|^2 \cdot \int\_M \|\varphi\|^2
        \leq \left( C \int\_M \|f\|^2 \right) \int\_M \|\varphi\|^2
    \end{align}.
\\]
Thus by \\(\langle \cdot , \cdot \rangle\_H\\) an inner product and \\(\ell\\) bounded, the Riesz representation theorem promises there is a unique \\(u \in H\\) such that \\(\Delta u = f\\) as explained above (and we will have \\(u \in C^{\infty}(M)\\) by Riesz representation).

Next we address the uniqueness of such a solution \\(u\\). Observe that a solution \\(u\\) to \\(\nabla u = f\\) is not unique because \\(u + c\\) for any constant \\(c\\) would also be a solution. However, it turns out this is the *only* way to get a new solution. Indeed, if \\(u\_1\\) and \\(u\_2\\) are two solutions \\(\Delta u\_1 = \Delta u\_2 = f\\), then \\(\Delta (u\_1 - u\_2) = 0\\); that is, the function \\(v := u\_1 - u\_2\\) is a harmonic function on \\(M\\). Recall that harmonic functions must be constant on a closed manifold because if \\(\Delta v = 0\\), then by integration by parts
\\[
    0 = \int\_M v \Delta v = \int\_M \|\nabla v\|\_g^2.
\\]
Hence \\(\nabla v = 0\\), so \\(v\\) is constant. Thus we have shown \\(u\_1\\) and \\(u\_2\\) can only differ by a constant.