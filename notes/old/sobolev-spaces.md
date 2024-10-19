---
layout: page
title: Sobolev Spaces
---

## Sobolev Spaces

/\*outline below... but I might need to learn more about Sobolev spaces and use them more before I can write this.\*/

/\*part of this must be that Sobolev spaces are Banach spaces while the space of distributions is not. Are Sobolev spaces the largest class of solutions while remaining in the Banach space category?*/

#### Example/Demonstration of Usefulness?

/\*mention conditions on \\(U\\)... maybe bounded and with smooth boundary?\*/

/\*Mention overall idea... encode boundary value problem into linear map.\*/

/\*Biggest part of this that is missing: I still don't appreciate the importance of the Sobolev norms/topology.\*/

Consider the boundary value problem
\\[\begin{cases}
    \Delta u = -f \quad &\text{in } U\\\\\
    u = 0 \quad &\text{on } \partial U.
\end{cases}
\tag{1}
\\]

We reformulate this problem as follows. If a function \\(u \in C^2\\) with \\(u\|_{\partial U} = 0\\) satisfies \\(\Delta u = -f\\), then it must also be a "weak solution" in the sense that
\\[
    \int_U \Delta u \cdot v = - \int_U f \cdot v \quad \text{for all } v \in C_c^{\infty}.
    \tag{2}
\\]

**Exercise.** Show that a function \\(u \in C^2\\) is a weak solution as above if and only if \\(\Delta u = -f\\).

We can now use integration by parts to reduce the order of derivatives we need to consider: we find that \\(u \in C^2\\) satisfies (2) if and only if
\\[
    \int_U Du \cdot Dv = \int_U f \cdot v \quad \text{for all } v \in C_c^{\infty}.
    \tag{3}
\\]

**Exercise.** Carry out the integration by parts as defined above.

That is, we define a bilinear functional \\(B: C^2(U) \times C_c^{\infty}(U) \to \mathbb{C}\\) by
\\[
    B(u,v) = \int_U Du \cdot Dv,
\\]
and we are looking for \\(u \in C^2\\) with \\(u\|\_{\partial U} = 0\\) such that \\(B(u,v) = (f,v)\_{\mathcal{L}^2}\\) for all \\(v \in C\_c^{\infty}\\).

This is a nice reformulation of the problem! However, note that by definition of the \\(C^2\\) topology, we say \\(u_k \to u\\) in \\(C^2\\) when \\(u_k \to u\\) uniformly, \\(\partial_i u_k \to u\\) uniformly, and \\(\partial_{ij} u_k \to u\\) uniformly. These are strong requirements and by the definition of \\(B(u,v)\\) there will be many sequences \\(u_k \in C_2\\) such that \\(B(u_k, v) \to B(u,v)\\) for some function \\(u\\), yet \\(u_k \not\to u\\) due to this strong topology. This can be disadvantageous: if we find \\(u_k \in C^2\\) and some function \\(u\\) such that \\(B(u_k,v) \to B(u,v) = (f,v)_{\mathcal{L}^2}\\) for all \\(v\\), then it is useful to regard \\(u\\) as a solution, even if it is not in \\(C^2\\) (for example, finding a fundamental solution to find other solutions). 

*Thus we want to redefine the topology so that \\(u_k \to u\\) if and only if \\(B(u_k,v) \to B(u,v)\\) for all \\(v\\)*.

/\*Not sure if the above is correct or not...\*/

/\*if true, this would provide widest possible class of solutions (which will make finding *a* solution easiest) while retaining the continuity of \\(B\\) (so we are still working in a nice category)\*/

Alternate route:

/\*This next step needs more motivation... why are we working with Sobolev spaces and why is the Sobolev norm the natural norm in this situation?\*/

/\*Maybe say: We now expand the functions \\(u\\) and \\(v\\) that we consider to the largest class possible class./\*

This bilinear functional \\(B\\) extends to a continuous bilinear map between Sobolev spaces \\(B: H_0^1(U) \times H_0^1(U) \to \mathbb{C}\\). We reformulate our problem as follows.

*We look for \\(u \in H\_0^1(U)\\) such that \\(B(u,v) = (f,v)_{\mathcal{L}^2}\\) for all \\(v \in H_0^1(U)\\).*

Expanding our domain for \\(u\\) should make it easier to determine if there is *any* solution, then we can separately determine the regularity of this solution. However, for the above to be a valid reformulation, we should check that if \\(u \in C^2(U)\\) with \\(u\|_{\partial U} = 0\\), then \\(u\\) solves the reformulation if and only if it solves the classical problem (1).

If \\(u \in C^2(U)\\) with \\(u\|\_{\partial U} = 0\\) satisfies the reformulated condition, then in particular \\(B(u,v) = (f,v)_{\mathcal{L}^2}\\) for all \\(v \in C_c^{\infty}(U)\\), so the previous discussion ensures \\(u\\) is a classical solution as in (1).

Conversely, if \\(u \in C^2(U)\\) with \\(u\|\_{\partial U} = 0\\) is a classical solution as in (1), then the discussion thus far demonstrates \\(B(u,v) = (f,v)\_{\mathcal{L}^2}\\) for all \\(v \in C\_c^{\infty}(U)\\). Therefore, by the continuity of \\(B\\) and \\((\cdot, \cdot)\_{\mathcal{L}^2}\\) and the density of \\(C\_c^{\infty}(U)\\) in \\(H_0^1(U)\\), we find the reformulation holds.

Importantly, recall that the restriction map \\(R: C(U) \to C(\partial U)\\) defined by \\(Rf = f\|\_{\partial U}\\) extends uniquely to a continuous linear map \\(R: H^{1}(U) \to H^{1/2}(\partial U)\\). Furthermore, recall the space \\(H_0^1(U)\\) is precisely \\(R^{-1}(0) \cap H^1(U)\\). Therefore the requirement that \\(u \in H^1_0(U)\\) builds in the boundary conditions of the original problem.

With this reformulation, we can make use of the tools of Functional Analysis to determine the existence and uniqueness of such a \\(u\\). In particular, we can use the Lax-Milgram Theorem in this instance. /\*TODO\*/

