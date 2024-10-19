---
layout: page
title: Sobolev Spaces
---

## Sobolev Spaces

#### Motivation

Consider the following boundary value problem for some open bounded region \\(\Omega \subset  \mathbb{R}^n\\) with smooth boundary and function \\(f \in C^{\infty}(\Omega)\\).
\\[\begin{cases}
    \Delta u - u = -f \quad &\text{in } \Omega\\\\\
    u = 0 \quad &\text{on } \partial \Omega.
\end{cases}
\tag{1}
\label{1}
\\]
Now we ask: does there exist some \\(u \in C_c^{\infty}(\Omega)\\) that satisfies the above? If so, is it unique? We can make use of the powerful tools of functional analysis to answer these difficult questions by reformulating the problem as follows. If a function \\(u \in C_c^{\infty}(\Omega)\\) satisfies \\(\Delta u = -f\\), then it must also satisfy
\\[
    \int_\Omega (\Delta u - u) \cdot v = - \int_\Omega f \cdot v \quad \text{for all } v \in C_c^{\infty}(\Omega).
    \tag{2}
    \label{2}
\\]
Such a function \\(u \in C_c^{\infty}(\Omega)\\) that satisfies the above is called a *weak solution*. However, it turns out that weak solutions and actual solutions are equivalent, as the following exercise shows.

**Exercise.** Show that any function \\(u \in C^{\infty}(\Omega)\\) that satisfies (\ref{1}) must be compactly supported.

**Exercise.** Show that a function \\(u \in C_c^{\infty}(\Omega)\\) satisfies (\ref{1}) (i.e is a classical solution) if and only if it satisfies (\ref{2}) (i.e. is a weak solution).

Thus it suffices to study these weak solutions. Furthermore, we can add useful symmetry to this weak solution formulation by applying integration by parts. Indeed, by doing so we find that \\(u \in C_c^{\infty}(\Omega)\\) satisfies (\ref{2}) if and only if
\\[
    \int_\Omega Du \cdot Dv + \int_\Omega u \cdot v = \int_\Omega f \cdot v \quad \text{for all } v \in C_c^{\infty}(\Omega).
    \tag{3}
    \label{3}
\\]

**Exercise.** Carry out the integration by parts as defined above.

We rewrite (\ref{3}) by defining a bilinear functional \\(B: C_c^{\infty}(\Omega) \times C_c^{\infty}(\Omega) \to \mathbb{R}\\) as
\\[
    B(u,v) = \int_\Omega Du \cdot Dv + \int_\Omega u \cdot v,
    \tag{4}
    \label{4}
\\]
and defining a linear functional \\(F: C_c^{\infty}(\Omega) \to \mathbb{R}\\) as \\(F(v) = \int_\Omega f \cdot v\\).

*Then, we are looking for \\(u \in C^{\infty}_c(\Omega)\\) such that \\(B(u,v) = F(v)\\) for all \\(v \in C\_c^{\infty}(\Omega)\\).*

Now for the key observation. If the bilinear form \\(B\\) were an inner product on some Hilbert space, and \\(F\\) were a continuous functional on that Hilbert space, then the existence and uniqueness of such a \\(u\\) is immediate by the Riesz representation theorem! Therefore we now turn our attention to constructing such a Hilbert space.

**Exercise.** Show \\(B: C_c^{\infty}(\Omega) \times C_c^{\infty}(\Omega) \to \mathbb{R}\\) is an inner product on the vector space \\(C_c^{\infty}(\Omega)\\).

**Exercise.** Show \\(F: C_c^{\infty}(\Omega) \to \mathbb{R}\\) is continuous under the norm \\(\\|\cdot\\|_{B} = \sqrt{B(\cdot, \cdot)}\\) induced by \\(B\\).

<details>
<summary><b>Solution.</b></summary>
Use the definition of \(F\), Cauchy-Schwarz, and the estimate \(\|v\|_{\mathcal{L}^2(\Omega)} \leq \|v\|_B\) to find
\[
    F(v) = (f,v)_{\mathcal{L}^2(\Omega)} \leq \|f\|_{\mathcal{L}^2(\Omega)}\|v\|_{\mathcal{L}^2(\Omega)} \leq \|f\|_{\mathcal{L}^2(\Omega)}\|v\|_B.
\]
</details>

By the above exercises, \\(B\\) is indeed an inner product and \\(F\\) is continuous in the induced topology, so the only remaining issue is that \\(C_c^{\infty}(\Omega)\\) is not a complete metric space under the metric induced by \\(B\\). However, this is easily solved by taking the completion. The completion of \\(C_c^{\infty}(\Omega)\\) under the inner product \\(B(\cdot,\cdot)\\) defined in (\ref{4}) will be a Hilbert space when given the same inner product \\(B(\cdot,\cdot)\\). This space is denoted by \\(H_0^1(\Omega)\\) and is an example of a Sobolev space. Then \\(F\\) extends to a continuous functional \\(F: H_0^1(\Omega) \to \mathbb{R}\\), and because \\(C_c^{\infty}(\Omega)\\) is dense in its completion \\(H_0^1(\Omega)\\), we can conclude the following.

*A solution \\(u \in C^{\infty}_c(\Omega)\\) solves (\ref{1}) if and only if \\(B(u,v) = F(v)\\) for all \\(v \in H_0^1(\Omega)\\).*

By the Riesz representation theorem, we know there exists a unique \\(u \in H_0^1(\Omega)\\) such that \\(B(u,v) = F(v)\\)! However, we don't know yet if \\(u\\) is smooth, just that it is in the completion \\(H_0^1(\Omega)\\) and so is the limit of a sequence smooth functions under the norm (\ref{4}). Still, this is substantial progress in the right direction: we know a unique solution exists and that it is in the space \\(H_0^1(\Omega)\\). In order to further understand the solution, we just need to study the Sobolev space \\(H_0^1(\Omega)\\) and understand its elements. This is what we now set out to do by developing the theory of Sobolev spaces.