---
layout: page
section: NOTES
title: Real Analysis
---

## Linear Algebra

#### Vector Spaces
Fundamental definitions: *vector space*, *(linear) subspace*, *linear combination*, *span*, *linearly independent*, *linear dependent*, *basis*, *dimension*, *codimension*,  *quotient space*.

Other definitions: *direct sum*, *complementary subspaces*, *affine subspace*.

**Lemma.** The dimension of a space is well-defined.

#### Linear Maps
Fundamental definitions: *linear map*, *kernel (i.e. null space)*, *image*, *(linear) isomorphism*.

Other definitions: *linear functional*, *affine map*.

**Lemma (defining map with basis).** For basis $\\{e\_i\\}_{i=1}^n \subset V$ and any elements $\\{w\_i\\}\_{i=1}^n$, there exists unique linear map $T: V \to W$ satisfying $T(e\_i) = w\_i$.

**Lemma.** A linear map is injective exactly when its kernel is $\\{0\\}$.

**Universal Property of Quotient Space.** For linear map $T: V \to W$, there exists linear map $\widetilde{T}: V/S \to W$ such that $\widetilde{T} \circ \pi = T$ if and only if $S \subset \ker T$ where $\pi: V \to V/S$ is the canonical projection.

#### Matrices
Fundamental definitions: *rank*, *nullity*.

Other definitions: *transpose*, *symmetric*, *skew-symmetric*.

**Matrix of linear map w.r.t bases.** Given linear map $T: V \to W$ together with bases $\\{e\_i\\}\_{i=1^n} \subset V$ and $\\{f\_j\\}\_{j=1^m} \subset W$, then $T(e\_i) = \sum A\_i^j f\_j$ for each $i$. Taking $A = (A_i^j)$ defines a matrix that agrees with $T$ in the desired way.

**Transition matrix.** Given space $V$ with bases $\\{e\_i\\}$ and $\\{\widetilde{e}\_j\\}$, then let
$e\_i = \sum\_{j=1}^n B^j\_i \widetilde{e}\_j$, hence $B = (B^j\_i)$ defines a matrix that transitions from vector representations with respect to $\\{\widetilde{e}\_j\\}$ to those with respect to $\\{e\_i\\}$ in the desired way.

**Prop.** Given linear map $T: V \to W$ and corresponding matrix $A$ with respect to bases $\\{e_i\\}$ and $\\{f_j\\}$. Then, if $B$ is the transition matrix from $\\{e_i\\}$ to $\\{\widetilde{e}_i\\}$ and $C$ is the transition matrix from $\\{f_j\\}$ to $\\{\widetilde{f}_j\\}$. Then $CAB^{-1}$ is the matrix for $T$ with respect to $\\{\widetilde{e}_i\\}$ and $\\{\widetilde{f}_j\\}$.

**Proposition.** column rank = null rank.

**Proposition (Canonical form for linear map).** TODO (B.20) in Lee smooth manifolds.

**Rank-Nullity Theorem.** For linear map $T: V \to W$ we have $\dim V = \operatorname{rank} T + \operatorname{nullity} T$.

**Proposition.** Given $A$ a matrix, $\operatorname{rank} A \geq k$ if and only if some $k \times k$ submatrix of $A$ is nonsingular.

#### Determinant

Definitions: *minor*, *cofactor*, *block upper triangular*

**Def (determinant).** Given $n \times n$ matrix $A = (A^i_j)$, then
\\[\det A = \sum_{\sigma \in S_n} \operatorname{sgn} A_1^{\sigma(1)} \cdots A_n \sigma_n^{\sigma(n)}\\]

**Properties of Determinant.**
1. Scaling a column by $c$ scales the determinant by $c$.
1. Swapping columns changes the sign of the determinant.
1. The determinant is unchanged by adding a scalar multiple of one column to another.
1. $\det(AB) = (\det A)(\det B)$
1. The matrix representation linear map $T: V \to V$ has the same determinant regardless of the choice of basis.

**Def.** Given matrix $A$, consider matrix $M_i^j$ obtained by deleting the $i$th row and $j$th, then $\det M_i^j$ is called a *minor* of $A$ and $\operatorname{cof}_i^j = (-1)^{i+j} M_i^j$ is a *cofactor*.

**Expansion by minors (i.e. standard recursive computation of determinant).**
TODO

**Cramer's Rule (i.e. determinant shortcut to compute  inverse of a matrix).**
TODO

**Prop.** Determinant of upper triangular matrix is product of diagonal entries.

**Prop.** The determinant of a block upper triangular matrix is the product of the determinants of the diagonal matrices.

#### Inner Products and Norms.
Fundamental defs: *inner product*, *projection*, *norm*

defs: *length*, *angle between vectors (defined using inner product)*, *orthornormal basis*, *Hermetian inner product*, *linear isometry*, *orthogonal complement*

**Def (Inner product).** An inner product is a map $V \times V \to \mathbb{R}$ that satisfies symmetry, bilinearity, and positive definiteness.

**Def (Norm).** A norm is a map $V \to \mathbb{R}$ that satisfies positivity, homogeneity, and the triangle inequality.

**Def (Frobenious Norm).** A norm on matrices obtained by taking $m \times n$ matrix space to be Euclidean space $\mathbb{R}^{mn}$.

**Cauchy-Schwarz inequality.**

**Gram-Schmidt Algorithm.** Given any basis $\\{f\_i\\}$, this is an inductive construction of an orthornormal basis $\\{e\_i\\}$. At step $k$, add the (normalization) of the following orthogonal component
\\[f\_{k} - \operatorname{proj}\_{\operatorname{span}(e\_1, \cdots, e\_{k-1})} f\_{k}\\]

#### Direct Product and Direct Sum

Defs: *direct product*, *direct sum*.

**Universal Property of the Direct Product.**
TODO

**Universal Property of the Direct Sum.**
TODO
