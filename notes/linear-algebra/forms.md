---
layout: page
title: Forms
section: Forms
---

# Forms

## Signed volume

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
The above sum is over the symmetric group \\(S\_n\\), which consists of all permutations \\(\sigma\\) on \\(n\\) elements, and \\(\operatorname{sgn}(\sigma)\\) denotes the sign of the permutation. However, it is more descriptive (and more useful for applications such as integration) to remove the absolute value and consider the *signed volume* \\(\det(v\_1, \cdots, v\_n)\\). Furthermore, recall the determinant enjoys the following nice properties, which follows from examining (\ref{eq:det}). 
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

## Exterior forms and the wedge product

Thus, given a vector space \\(V\\), we are interested in the space of all multilinear alternating maps \\(V \times \cdots \times V \to \mathbb{R}\\) with \\(k\\) copies of \\(V\\), and we denote this space by \\(\bigwedge^k(V^\*)\\) (this choice of notation will become clear later). Note \\(\bigwedge^k(V^\*)\\) forms a vector space and elements of this vector space are called *exterior forms*.

For an arbitrary vector space \\(V\\), we may define exterior forms by noting the construction (\ref{eq:proj}) in \\(\mathbb{R}^k\\) only relies on a distinguished choice of the \\(k\\) projection covectors \\(\pi^1, \cdots, \pi^k\\). Thus given \\(k\\) covectors \\(\omega^1, \cdots, \omega^k\\) we may define their *wedge product* \\(\omega^1 \wedge \cdots \wedge \omega^k \in \bigwedge^k(V^*)\\) by
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

The wedge product is precisely the tool we need to make a basis for 

/\*should I leave this until later when I can talk about \\(\bigwedge^k(V)\\)?\*/

## Forms as alternating tensors

Recall the space of \\(k\\)-forms \\(\bigwedge^k(V^\*)\\) is defined the subspace of all multilinear maps \\(L(V \times \cdots \times V, \mathbb{R})\\) that are alternating. Furthermore, recall this space of multilinear maps is in isomorphism with the sace of covariant \\(k\\)-tensors \\(V^\* \otimes \cdots \otimes V^\* \simeq L(V \times \cdots \times V, \mathbb{R})\\).
<!-- cite this -->
Therefore we can identify \\(\bigwedge^k(V^\*)\\) with its image in \\(V^\* \otimes \cdots \otimes V^\*\\) under this isomorphism; we will call this subspace *the space of alternating covariant \\(k\\)-tensors*, and in this section we investigate this subspace. In other words, we will investigate how to express exterior forms as covariant tensors through this identification. To begin, we compute this expression for the wedge product:
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
Because wedge products of the form \\(\omega^1 \wedge \cdots \wedge \omega^k\\) span \\(\bigwedge^k(V^*)\\), the expression (\ref{eq:wedge-as-tensor}) s

## 