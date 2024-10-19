---
layout: page
title: Spectral Theorm for Matrices
---

<!-- 
PRE REQS
- Orthogonal decomposition of a vector space.
- dimension of a vector space
- Hermitian matrices definition and motivation
- Eigenstuff definition and motivation

- first proof:
    - fundamental theorem of algebra / existence of complex eigenvalues

- second proof:
    - compactness theorem (for metric spaces or topological spaces)
    - Lagrange's multiplier theorem (todo)

 -->

## Spectral Theorem

#### Statement
**Spectral Theorem.** Suppose \\(V\\) is a finite dimensional vector space, and let \\(T: V \to V\\) be a self-adjoint map. Then \\(V\\) has an orthornomal basis of eigenfunctions of \\(T\\).

#### Proof 1
In the following proof, we use that \\(T\\) is self-adjoint two derive two important properties of \\(T\\). First, that the eigenvalues of \\(T\\) are real. Second, that if \\(T(E) \subset E\\), then \\(T(E^{\perp}) \subset E^{\perp}\\).

**Proof.**
Recall that \\(T\\) will always have an eigenvalue. Indeed, recall eigenvalues are precisely the roots of the characteristic polynomial \\(p(\lambda) := \det(T - \lambda I)\\), and the fundamental theorem of algebra promises \\(p(\lambda)\\) will always have some (possibly complex) root \\(\lambda_1\\). Luckily, the fact that \\(T\\) is self-adjoint ensures this eigenvalue \\(\lambda_1\\) will be real. Indeed, let \\(v_1\\) be some eigenvector corresponding to \\(\lambda_1\\) and compute
\\[
    \lambda_1 \langle v_1 , v_1\rangle 
    = \langle \lambda_1 v_1 , v_1\rangle 
    = \langle Tv_1 , v_1 \rangle
    = \langle v_1 , Tv_1 \rangle
    = \langle v_1 , \lambda_1 v_1\rangle
    = \bar{\lambda_1} \langle v_1 , v_1\rangle.
\\]
Therefore \\(\lambda_1 = \bar{\lambda_1}\\) and so \\(\lambda_1\\) is real. Now let \\(E\\) be the eigenspace of \\(\lambda_1\\), decompose \\(V = E \oplus E^{\perp}\\), and consider the restricted operator \\(T: E^{\perp} \to V\\). If we can show \\(T(E^{\perp}) \subset E^{\perp}\\), then the theorem follows by repeating the argument for \\(T: E^{\perp} \to E^{\perp}\\) and inducting. Indeed, we have \\(T(E) \subset E\\) by \\(E\\) the eigenspace of \\(\lambda\\). Therefore, for any \\(x \in E^{\perp}\\) and \\(z \in E\\) we find, using \\(T\\) is self-adjoint, \\(\langle Tx , z \rangle = \langle x , Tz\rangle = 0\\) and so \\(Tx \in E^{\perp}\\).

#### Proof 2
<!-- This proof could be preperation for infinite dimensional case. -->
**Proof.** Note that by \\(T\\) self-adjoint, the inner product \\(f(x) = \langle Tx , x\rangle\\) is real. Furthermore, this inner product is continuous is \\(x\\), so by continuity and compactness, the image \\(f(\\{x: \\|x\\| = 1\\})\\) has some maximum \\(f(y)\\). By Lagrange's multiplier theorem, such a maximizing vector \\(y\\) must satisfy \\(\nabla (y^{\dagger}Ty) = \lambda \nabla (y^{\dagger} y)\\) for some \\(\lambda \in \mathbb{R}\\). Therefore, using the product rule, we find that for all \\(z \in V\\),
\\[\begin{align}
0 = \langle \nabla (y^{\dagger}Ty) - \nabla (y^{\dagger} y) , z \rangle 
= \cdots
= 2z^{\dagger}\left(\frac{T+T^{\dagger}}{2}y - \lambda y\right).
\tag{1} \label{eq:product-rule}
\end{align}\\]

**Exercise.** Carry out the product rule computation above.

Because (\ref{eq:product-rule}) above holds for all \\(z \in V\\), we conclude that \\(\frac{1}{2}(T+T^{\dagger})y = \lambda y\\) and so by \\(T\\) self-adjoint, \\(Ty = \lambda y\\). That is, the real value \\(\lambda\\) given by Lagrange's multiplier theorem is an eigenvalue of \\(T\\). 

Now let \\(E\\) be the eigenspace of \\(\lambda\\), decompose \\(V = E \oplus E^{\perp}\\), and consider the restricted operator \\(T: E^{\perp} \to V\\). If we can show \\(T(E^{\perp}) \subset E^{\perp}\\), then the theorem follows by repeating the argument for \\(T: E^{\perp} \to E^{\perp}\\) and inducting. Indeed, we have \\(T(E) \subset E\\) by \\(E\\) the eigenspace of \\(\lambda_1\\). Therefore, for any \\(x \in E^{\perp}\\) and \\(z \in E\\) we find, using \\(T\\) is self-adjoint, \\(\langle Tx , z \rangle = \langle x , Tz\rangle = 0\\) and so \\(Tx \in E^{\perp}\\).

