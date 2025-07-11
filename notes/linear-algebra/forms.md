---
layout: page
title: Exterior Forms
section: Exterior Forms
---

# Exterior Forms

## Signed volume

<!-- change all notation to \Lambda^k -->

/\*perhaps use \\(\mathbb{R}^k\\) here?\*/

Recall the volume of the paralleltope in \\(\mathbb{R}^n\\) defined by vectors \\(v\_1, \cdots, v\_n \in \mathbb{R}^n\\) is given by \\(\|\det(v\_1, \cdots, v\_n)\|\\) where
\\[
    \det(v\_1, \cdots, v\_n)
    = 
    \det \begin{pmatrix}
        v\_1^1 & \cdots & v\_n^1 \\\\\
        \vdots & \ddots & \vdots \\\\\
        v\_1^n & \cdots & v\_n^n
    \end{pmatrix}
    = \sum_{\sigma \in S\_n} \operatorname{sgn}(\sigma)v^{\sigma(1)}\_1 \cdots v^{\sigma(n)}\_n.
    \tag{1}
    \label{eq:det}
\\]
The above sum is over the symmetric group \\(S\_n\\), which consists of all permutations \\(\sigma\\) on \\(n\\) elements, and \\(\operatorname{sgn}(\sigma)\\) denotes the sign of the permutation. However, it is nicer and more descriptive (and more useful for applications such as integration) to remove the absolute value and consider the *signed volume* \\(\det(v\_1, \cdots, v\_n)\\). Furthermore, recall the determinant enjoys the following nice properties, which follows from examining (\ref{eq:det}). 
1. Multilinearity: for any vectors \\(v\_1, \cdots, v\_n, u, w\\) and scalars \\(\alpha, \beta\\), we have
\\[
    \det(v\_1, \cdots, \alpha u + \beta w, \cdots, v\_n)
    = \alpha \det(v\_1, \cdots, u, \cdots, v\_n) + \beta \det(v\_1, \cdots, w, \cdots, v\_n).
\\]
2. Alternating: for an vectors \\(v\_1, \cdots, v\_n, u, w\\), swapping two entries reverses the sign by
\\[
    \det(v\_1, \cdots, v\_j, \cdots, v\_i, \cdots, v\_n) = -\det(v\_1, \cdots, v\_i, \cdots, v\_j, \cdots, v\_n).
\\]

Note this expression for signed volume in \\(\mathbb{R}^n\\) is dependent on the decomposition using basis \\(\{E\_1, \cdots, E\_n\}\\). More precisely, the signed volume is dependent on the projections \\(\pi^i: \mathbb{R}^n \to \operatorname{span}(E\_i)\\), which becomes obvious when we rewrite
\\[
     \det(v\_1, \cdots, v\_n)
    = 
    \det \begin{pmatrix}
        \pi^1(v\_1) & \cdots & \pi^1(v\_n) \\\\\
        \vdots & \ddots & \vdots \\\\\
        \pi^n(v\_1) & \cdots & \pi^n(v\_n)
    \end{pmatrix}.
    \tag{2}
    \label{eq:proj}
\\]
Thus there are many choices of signed volume in \\(\mathbb{R}^n\\) depending on the particular choice of orthonormal basis. However, all choices are multilinear and alternating. 

## Exterior forms

Thus, given vector space \\(V\\), we are interested in multilinear alternating maps \\(\omega: V \times \cdots \times V \to \mathbb{R}\\) with \\(k\\) copies of \\(V\\) (where \\(k\\) is not necessarily the dimension). That is, we require
1. Multilinearity: for any vectors \\(v\_1, \cdots, v\_n, u, w\\) and scalars \\(a, b\\), we have
\\[
    \omega(v\_1, \cdots, \alpha u + \beta w, \cdots, v\_n)
    = a \omega(v\_1, \cdots, u, \cdots, v\_n) + b \omega(v\_1, \cdots, w, \cdots, v\_n).
\\]
2. Alternating: for an vectors \\(v\_1, \cdots, v\_n, u, w\\), swapping two entries reverses the sign by
\\[
    \omega(v\_1, \cdots, v\_j, \cdots, v\_i, \cdots, v\_n) = -\omega(v\_1, \cdots, v\_i, \cdots, v\_j, \cdots, v\_n).
\\]

The space of all such alternating linear maps \\(V \times \cdots \times V \to \mathbb{R}\\) forms a vector subspace of \\(L(V, \cdots, V; \mathbb{R})\\), which is the vector space of multilinear maps \\(V \times \cdots \times V \to \mathbb{R}\\). We denote this subspace by \\(\Lambda^k(V^\*)\\) and we call an element \\(\omega\\) of this vector space *an exterior \\(k\\)-form*, or just *a \\(k\\)-form* for short. 

Additionally, recall this space of multilinear maps \\(V \times \cdots \times V \to \mathbb{R}\\) taking \\(k\\) inputs is in isomorphism with the sace of covariant \\(k\\)-tensors \\(V^\* \otimes \cdots \otimes V^\* \simeq L(V \times \cdots \times V, \mathbb{R})\\).
<!-- cite this -->
Therefore we can identify \\(\Lambda^k(V^\*)\\) with its image in \\(V^\* \otimes \cdots \otimes V^\*\\) under this isomorphism; we will call this image subspace *the space of alternating covariant \\(k\\)-tensors*.

## Elementary properties of exterior forms

Next we get familiar with exterior forms by exploring some basis but important properties.

**Prop.** Given \\(\omega \in \Lambda^k(V^*)\\), we have \\(\omega(v\_1, \cdots, v\_k) = 0\\) if and only if the entries \\(v\_1, \cdots, v\_k\\) are linearly dependent.

*Proof.* 

**Cor.** \\(\omega(v\_1, \cdots, v\_k) = 0\\) if there are repeated entries \\(v\_i = v\_j\\) for some \\(i, j\\).

## Wedge product

For an arbitrary vector space \\(V\\), we may define exterior forms by noting the construction (\ref{eq:proj}) in \\(\mathbb{R}^k\\) only relies on a distinguished choice of the \\(k\\) projection covectors \\(\pi^1, \cdots, \pi^k\\). Thus given \\(k\\) covectors \\(\omega^1, \cdots, \omega^k\\) we may define their *wedge product* \\(\omega^1 \wedge \cdots \wedge \omega^k \in \Lambda^k(V^*)\\) by
\\[
    \omega^1 \wedge \cdots \wedge \omega^k(v_1, \cdots, v_n)
    = 
    \det \begin{pmatrix}
        \omega^1(v\_1) & \cdots & \omega^1(v\_k) \\\\\
        \vdots & \ddots & \vdots \\\\\
        \omega^k(v\_1) & \cdots & \omega^k(v\_k)
    \end{pmatrix}.
    \tag{3}
    \label{eq:wedge}
\\]
This wedge product defines an alternating multilinear map by the properties of the columns of the determinant. However, by looking at the rows of the determinant, note the construction of the wedge product itself is multilinear and alternating in the following sense:
1. Multilinearity: given covectors \\(\phi, \psi, \omega^1, \cdots, \omega^k \in V^*\\) and scalars \\(\alpha, \beta\\), we have
\\[
    \omega^1 \wedge \cdots \wedge (\alpha \phi + \beta \psi) \wedge \cdots \wedge \omega^k
    =  \alpha (\omega^1 \wedge \cdots \wedge \phi \wedge \cdots \wedge \omega^k) + \beta (\omega^1 \wedge \cdots \wedge \psi \wedge \cdots \wedge \omega^k).
\\]
2. Alternating: given covectors \\(\phi, \psi, \omega^1, \cdots, \omega^k \in V^*\\)
\\[
    \omega^1 \wedge \cdots \wedge \omega^j \wedge \cdots \wedge \omega^i \wedge \cdots \wedge \omega^k 
    = -\omega^1 \wedge \cdots \wedge \omega^i \wedge \cdots \wedge \omega^j \wedge \cdots \wedge \omega^k.
\\]

## Basis for exterior forms

Given a finite dimensional vector space \\(V\\) with basis \\(E\_1, \cdots, E\_n\\), the wedge product allows us to construct a basis for \\(\Lambda^k(V^\*)\\). Indeed, we consider the dual basis \\((\varepsilon\_1, \cdots, \varepsilon\_n)\\) for \\(V^\*\\) and we construct a basis from elements of the form \\(\varepsilon^{i\_1} \wedge \cdots \wedge \varepsilon^{i\_k}\\). Due to the alternating property of the wedge product, we can reorder each such wedge product up to sign, so we impose the restriction that the indices are increasing \\(i\_1 < i\_2 < \cdots < i\_k\\) to get a basis.

**Prop.** The set \\(\\{\varepsilon^{i\_1} \wedge \cdots \wedge \varepsilon^{i\_k} : i\_1 < \cdots < i\_k\\}\\) forms a basis for \\(\Lambda^k(V^*)\\).

*Proof.* For linear independence, suppose \\(\sum\_{i\_1 < \cdots < i\_k} A\_{i\_1 \cdots i\_k} \varepsilon^{i\_1} \wedge \cdots \wedge \varepsilon^{i\_k} = 0\\), then take any \\(j\_1 < \cdots < j\_k\\) increasing and compute
\\[\begin{align}
    0 &= \left\( \sum\_{i\_1 < \cdots < i\_k} A\_{i\_1 \cdots i\_k}\varepsilon^{i\_1} \wedge \cdots \wedge \varepsilon^{i\_k}  \right\)\left\(E\_{j\_1}, \cdots, E\_{j\_k}\right\)\\\\\
    &= \sum_{i\_1 < \cdots < i\_k} A\_{i\_1 \cdots i\_k} 
    \det \begin{pmatrix}
        \delta^{i\_1}\_{j\_1} & \cdots & \delta^{i\_1}\_{j\_k}\\\\\
        \vdots & \ddots & \vdots\\\\\
        \delta^{i\_k}\_{j\_k} & \cdots & \delta^{i\_k}\_{j\_k}.
    \end{pmatrix}
    = A\_{j\_1 \cdots j\_k}
\end{align}\\]
Note in the last line we used that the determinant is only nonzero if the sets \\(\\{i\_1, \cdots, i\_k\\}\\) and \\(\\{j\_1, \cdots, j\_k\\}\\) are equal in which case the matrix is the identity and the determinant is \\(1\\).

To show this basis spans \\(\Lambda^k(V^*)\\), take any exterior \\(k\\)-form \\(A: V \times \dots \times V \to \mathbb{R}\\), then define coefficients \\(A\_{i\_1 \cdots i\_k} := A(E\_{i\_1}, \cdots, E\_{i\_k})\\) and consider
\\[
    A' := \sum\_{i\_1 < \cdots < i\_k} A\_{i\_1 \cdots i\_k} \varepsilon^{i\_1} \wedge \cdots \wedge \varepsilon^{i\_k}.
\\]
We claim \\(A' = A\\). Indeed, choose \\(j\_1 < \cdots < j\_k\\), then by the same computation as the above,
\\[
    A'(E\_{j\_1}, \cdots, E\_{j\_k})
    = \left\(\sum\_{i\_1 < \cdots < i\_k} A\_{i\_1 \cdots i\_k} \varepsilon^{i\_1} \wedge \cdots \wedge \varepsilon^{i\_k}\right\)(E\_{j\_1}, \cdots, E\_{j\_k})
    = A\_{j\_1 \cdots j\_k}
    = A(E\_{j\_1}, \cdots, E\_{j\_k}).
\\]
Thus \\(A\\) and \\(A'\\) agree on tuples \\((E\_{j\_1}, \cdots, E\_{j\_k})\\) with \\(j\_1 < \cdots < j\_k\\).

## Change under linear transformation

Recall the signed volume of the parallelotope spanned by vectors \\(v\_1, \cdots, v\_n \in \mathbb{R}^n\\) is given by \\(\det(v\_1, \cdots, v\_n)\\). Further recall if we apply a linear transformation \\(T: \mathbb{R}^n \to \mathbb{R}^n\\) to the parallelotope, the volume is scaled by a factor of \\(\det T\\):
\\[
    \det(Tv\_1, \cdots, Tv\_n) = \det T \cdot \det(v\_1, \cdots, v\_n).
\\]
More generally, given an \\(n\\)-dimensional vector space \\(V\\), an exterior \\(n\\)-form \\(\omega \in \Lambda^n(V^\*)\\) is called a *volume form*. Volume forms measure the volumes of parallelotopes of the same dimension as the ambient space and a version of the above relation holds for volume forms in general. 
<!-- Before stating this, however, we importantly note that given a basis \\(\varepsilon^1, \cdots, \varepsilon^n\\) for \\(V^*\\), the corresponding basis for \\(\Lambda^n(V^\*)\\) is simply \\(\varepsilon^1 \wedge \cdots \wedge \varepsilon^n\\) and thus \\(\Lambda^n(V^\*)\\) is one-dimensional. -->

**Prop.** Given an \\(n\\)-dimensional vector space \\(V\\), volume form \\(\omega \in \Lambda^n(V^\*)\\), and linear transformation \\(T: V \to V\\), we have
\\[
    \omega(Tv\_1, \cdots, Tv\_n) = \det T \cdot \omega(v\_1, \cdots, v\_n).
    \tag{4}
    \label{eq:scaling}
\\]

(Recall from linear algebra \\(\det T\\) denotes the determinant of the corresponding matrix with respect to any choice of basis as this value is basis independent).

*Proof.* Fix a basis \\((E\_i)\\) for \\(V\\) and take the corresponding dual basis \\((\varepsilon^i)\\) for \\(V^\*\\). Note it suffices to check \eqref{eq:scaling} taking each \\(v\_i\\) to be some basis vector \\(E\_j\\) because both sides of the equation are multlinear, so the more general equality holds by multilinearity. Furthermore, we may assume our inputs are some permutation of the basis vectors \\(v\_i = E\_{\sigma(i)}\\) for otherwise on basis vector input would be repeated twice, making both sides trivially \\(0\\). In fact, it suffices to assume \\(v\_i = E\_i\\) because both sides of \eqref{eq:scaling} alternating and so once this case is proved, we may use the alternating property to achieve the equality for any permutation of basis vectors. Now write the basis representations \\(\omega = \alpha \varepsilon^1 \wedge \cdots \wedge \varepsilon^n\\) for scalar \\(\alpha\\) and write \\(TE\_i = \sum T\_i^j E\_j\\). Then compute
\\[
    \omega(TE\_1, \cdots, TE\_n) 
    = \sum T\_1^{i\_1} \cdots T\_n^{i\_n} \alpha \varepsilon^1 \wedge \cdots \wedge \varepsilon^n (E\_{i\_1}, \cdots, E\_{i\_n}).
\\]
Note each summand above will vanish if there are repeated indices, so only permutations \\(\sigma\\) in the symmetric group \\(S\_n\\) remain, giving
\\[
\begin{align}
     \omega(TE\_1, \cdots, TE\_n) 
    &= \alpha \sum\_{\sigma \in S\_n} T\_1^{\sigma(1)} \cdots T\_n^{\sigma(n)} \varepsilon^1 \wedge \cdots \wedge \varepsilon^n(E\_{\sigma(1)}, \cdots, E\_{\sigma(n)})\\\\\
    &= \alpha \sum_{\sigma \in S\_n} \operatorname{sgn} \sigma T\_1^{\sigma(1)} \cdots T\_n^{\sigma(n)} = \alpha \cdot \det T.
\end{align}
\\]
In the above we used that \\(\varepsilon^1 \wedge \cdots \wedge \varepsilon^n(E\_{\sigma(1)}, \cdots, E\_{\sigma(n)}) = \operatorname{sgn} \sigma\\) 
<!-- explain this? -->
and the definition of determinant. 
<!-- cite the determinant definition-->
Thus the proof is complete by noting 
\\[\omega(E\_1, \cdots, E\_n) = \alpha \varepsilon^1 \wedge \cdots \wedge \varepsilon^n(E\_1, \cdots, E\_n) = \alpha.\\]

## Forms as alternating tensors
<!-- note this section is necessary for differential geometry so that I can define the bundle \Lambda^k(T^*M) as a subbundle of \bigotimes^k(T^*M) -->

Recall the space of \\(k\\)-forms \\(\Lambda^k(V^\*)\\) is defined the subspace of all multilinear maps \\(L(V \times \cdots \times V, \mathbb{R})\\) that are alternating. Furthermore, recall this space of multilinear maps is in isomorphism with the sace of covariant \\(k\\)-tensors \\(V^\* \otimes \cdots \otimes V^\* \simeq L(V \times \cdots \times V, \mathbb{R})\\).
<!-- cite this -->
Therefore we can identify \\(\Lambda^k(V^\*)\\) with its image in \\(V^\* \otimes \cdots \otimes V^\*\\) under this isomorphism; we will call this subspace *the space of alternating \\(k\\)-forms*, and in this section we investigate this subspace. In other words, we will investigate how to express exterior forms as covariant tensors through this identification. To begin, we compute this expression for the wedge product:
\\[
    \begin{align}
    (\omega^1 \wedge \cdots \wedge \omega^k)(v\_1, \cdots, v\_n)
    &= \det \begin{pmatrix}
        \omega^1(v\_1) & \cdots & \omega^1(v\_k) \\\\\
        \vdots & \ddots & \vdots \\\\\
        \omega^k(v\_1) & \cdots & \omega^k(v\_k)
    \end{pmatrix}\\\\\
    &= \sum_{\sigma \in S\_n} \operatorname{sgn}(\sigma)\omega^{\sigma(1)}(v\_1) \cdots \omega^{\sigma(n)}(v\_n)
    = \sum_{\sigma \in S\_n} \operatorname{sgn}(\sigma)\omega^{\sigma(1)} \otimes \cdots \otimes \omega^{\sigma(n)}(v\_1, \cdots, v\_n).
    \end{align}
\\]
That is, we have the identification
\\[
    \omega^1 \wedge \cdots \wedge \omega^k = \sum_{\sigma \in S\_n} \operatorname{sgn}(\sigma)\omega^{\sigma(1)} \otimes \cdots \otimes \omega^{\sigma(n)}.
    \tag{4}
    \label{eq:wedge-as-tensor}
\\]
Because wedge products of the form \\(\omega^1 \wedge \cdots \wedge \omega^k\\) span \\(\Lambda^k(V^*)\\), the expression (\ref{eq:wedge-as-tensor}) .... 
<!-- TODO... finish this thought. Maybe "we will see later wedge products span ...." if I reorder? -->

/\*TODO... finish this thought.\*/