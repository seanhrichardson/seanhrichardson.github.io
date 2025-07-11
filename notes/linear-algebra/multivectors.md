---
layout: page
title: Multivectors
section: Multivectors
---

# Multivectors

## Forms as alternating tensors

Recall the space of \\(k\\)-forms \\(\Lambda^k(V^\*)\\) is defined the subspace of all multilinear maps \\(L(V \times \cdots \times V, \mathbb{R})\\) that are alternating. Furthermore, recall this space of multilinear maps is in isomorphism with the sace of covariant \\(k\\)-tensors \\(V^\* \otimes \cdots \otimes V^\* \simeq L(V \times \cdots \times V, \mathbb{R})\\).
<!-- cite this -->
Therefore we can identify \\(\Lambda^k(V^\*)\\) with its image in \\(V^\* \otimes \cdots \otimes V^\*\\) under this isomorphism and we call this subspace *the space of alternating covariant \\(k\\)-tensors* and in this section we investigate this subspace. In other words, we will investigate how to express exterior forms as covariant tensors through this identification. To begin, we compute this expression for the wedge product:
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
Because wedge products of the form \\(\omega^1 \wedge \cdots \wedge \omega^k\\) span \\(\Lambda^k(V^*)\\), we may use linear combiations of the expression (\ref{eq:wedge-as-tensor}) to identify any exterior \\(k\\)-form with the corresponsing covariant alternating \\(k\\)-tensor.
<!-- TODO... finish this thought. Maybe "we will see later wedge products span ...." if I reorder? -->

Taking motivation from this formulation, we consider the corresponding subspace for *contravariant* \\(k\\)-tensors. Indeed, take vectors \\(v_1, \cdots, v_k\\) of an arbitrary vector space \\(V\\) and define the *wedge product* as the contravariant \\(k\\)-tensor
\\[
    v_1 \wedge \cdots \wedge v_k := \sum_{\sigma \in S\_n} \operatorname{sgn}(\sigma)v_{\sigma(1)} \otimes \cdots \otimes v_{\sigma(n)} \in \bigotimes\nolimits^k V.
\\]
In the covariant case the wedge products span the subspace of alternating covariant \\(k\\)-tensors. Thus we may define the *space of contravariant alternating \\(k\\)-tensors* \\(\Lambda^k(V)\\) to be the subspace
\\[
    \Lambda^k(V) := \operatorname{span}\_{\mathbb{R}}\\{v\_1 \wedge \cdots \wedge v\_k : v\_i \in V\\} \subset \bigotimes\nolimits^k V.
\\]
Elements of the subspace \\(\Lambda^k(V)\\) are called *\\(k\\)-multivectors*.

<!-- TODO... move this: -->
<!-- Once again, note this definition provides our two key properties:
1. Multilinearity: given vectors \\(u, w, v^1, \cdots, v^k \in V\\) and scalars \\(\alpha, \beta\\), we have
\\[
    v^1 \wedge \cdots \wedge (\alpha u + \beta w) \wedge \cdots \wedge v^k
    =  \alpha (v^1 \wedge \cdots \wedge u \wedge \cdots \wedge v^k) + \beta (v^1 \wedge \cdots \wedge w \wedge \cdots \wedge v^k).
\\]
2. Alternating: given vectors \\(u, v, v^1, \cdots, v^k \in V\\)
\\[
    v^1 \wedge \cdots \wedge v^j \wedge \cdots \wedge v^i \wedge \cdots \wedge v^k 
    = -v^1 \wedge \cdots \wedge v^i \wedge \cdots \wedge v^j \wedge \cdots \wedge v^k.
\\]

Now we may define the space of *alternating tensors* \\(\Lambda^k(V) \subset V^{\otimes k}\\) to be the subspace spanned by such wedge products:

\\[
    V^{\otimes k} \supset \Lambda^k(V) := \left\\{\sum\_{i\_1 < \cdots < i\_k} \alpha^{i\_1 \cdots i\_k} v\_{i\_1} \wedge \cdots \wedge v\_{i\_k}\\ : v\_{1}, \cdots, v\_{n} \in V \text{ and } \alpha^{i\_1 \cdots i\_k} \in \mathbb{R}\right\\}.
\\]
Because the alternating property above allows reordering up to only a sign change, it suffices to consider *increasing* linear combinations \\(i\_1 < \cdots < i\_k\\) as we have done above. In fact, after fixing a basis for \\(V\\), we can use increasing linear combinations form a basis for \\(\Lambda^k(V)\\):

**Prop.** Let \\(\\{E\_1, \cdots E\_n\\}\\) be a basis for \\(V\\). Then 
\\(\\{E\_{i\_1} \wedge \cdots \wedge E\_{i\_k} : i\_1 < \cdots < i\_k\\}\\)
forms a basis for \\(\Lambda^k(V)\\).

*Proof.* /\*TODO (possible just show linear independence for two wedge products, then claim the argument generalizes for simplicity of notation)\*/


Furthermore, note that given distinct increasing indices \\(i\_1 < \cdots < i\_k\\) and \\(j\_1 < \cdots < j\_k\\) as above, the wedge products \\(v\_{i\_1} \wedge \cdots \wedge v\_{i\_k}\\) and \\(v\_{j\_1} \wedge \cdots \wedge v\_{j\_k}\\) are linearly independent as tensors

In fact, the same argument generalizes  -->

<!-- todo... how do I show linear independence of these general wedge products? -->

<!-- need to rethink how I define \Lambda^k... I have control over this. -->

<!-- at some point, give direct definition of wedge product as the subset of allternating tensors -->

## Alternating tensors as a quotient space

/\*re-define as a quotient space? Not sure if this is necessary yet, but might be easier and more general?\*/

## Elementary properties of multivectors

## Basis for the space of multivectors

## Geometric interpretation of wedge product

We can view a wedge product \\(v\_1 \wedge \cdots \wedge v\_k\\) as the parallelotope spanned by \\(v\_1, \cdots v\_k\\), and we are interested in two key geometric properties: the subspace spanned by the parallelotope, and the oriented volume of the parallelotope. 

/\*this section is to build intuition and to motivate the next section...\*/

/\*give 2D example\*/

/\*give 3D example\*/

/\*define norm, which gives area of parallelotope\*/

**Prop.** Two wedge products \\(v\_1 \wedge \cdots \wedge v\_k\\) and \\(w\_1 \wedge \cdots \wedge w\_k\\) are equivalent if and only if the corresponding parallelotopes span the same subspace and have the same oriented volume.

/\*TODO... quick verification of this. Doesn't need to be in the Prop, proof format. \*/

## Universal property of wedge product

/\*need to define alternating multilinear map in general... give cross product as an example?\*/

Consider the wedge product map \\(a: (v_1, \cdots, v\_k) \mapsto v\_1 \wedge \cdots \wedge v\_k\\) between spaces \\(a: V \times \cdots \times V \to \Lambda^k(V) \subset \bigotimes^k V\\). Once again, recall the multilinearity and alternating properties of the wedge product, which translate to the following properties of the map \\(a\\):

1. Multilinearity: 
\\[
    a(v\_1, \cdots, \alpha u + \beta w, \cdots, v\_k) = \alpha a(v\_1, \cdots, u , \cdots, v\_k) + \beta a(v\_1, \cdots, w, \cdots, v\_k).
\\]
2. Alternating: 
\\[
    a(v\_1, \cdots, v\_i, \cdots, v\_j, \cdots, v\_k) = -a(v\_1, \cdots, v\_j, \cdots, v\_i, \cdots, v\_k).
\\]

Recall the tensor product of vector spaces is designed as the perfect space to smush mulitlinear maps into linear maps as revealed by the corresponding universal property. In the same way, we can interpret the space of alternating tensors is the perfect domain to smush alternating multilinear maps into a linear map from a genuine vector space.

**Prop (Universal property of wedge product).** Given a vector space \\(V\\) The space of alternating tensors \\(\Lambda^k(V)\\) satisfies the following universal property. Given an alternating multilinear map \\(\omega: V \times \cdots \times V \to W\\), there exists a unique linear map \\(L: \Lambda^k(V) \to W\\) such that \\(L \circ a = \omega\\).

<!-- TODO: commutative diagram -->

/\*the below proof assusmes \\(V\\) is finite dim'l. Can I write a proof without this?\*/

*Proof.* Note for any vectors \\(v\_1, \cdots, v\_k \in V\\) we require
\\[
    L(v\_1 \wedge \cdots \wedge v\_k) = (L \circ a)(v\_1, \cdots, v\_k) = \omega(v\_1, \cdots, v\_k).
\\]
Now fix a basis \\((E\_1, \cdots, E\_n)\\) for \\(V\\), consider the induced basis for \\(\Lambda^k(V)\\), and note the requirement \\(L(E\_{i\_1} \wedge \cdots \wedge E\_{i\_k}) = \omega(E\_{i\_1}, \cdots, E\_{i\_k})\\) combined with linearity uniquely defines the map \\(L\\). Indeed, given \\(A \in \Lambda^k(V)\\) with basis expression \\(A = \sum_{i\_1 < \cdots < i\_k} A^{i\_1 \cdots i\_k} E\_{i\_1} \wedge \cdots \wedge E\_{i\_k}\\) we define
\\[
    L(A) 
    = L\left\( \sum_{i\_1 < \cdots < i\_k} A^{i\_1 \cdots i\_k} E\_{i\_1} \wedge \cdots \wedge E\_{i\_k} \right\)
    = \sum_{i\_1 < \cdots < i\_k} A^{i\_1 \cdots i\_k} \omega(E\_{i\_1}, \cdots, E\_{i\_k}).
\\]
Because \\(L\\) is defined as a linear extension from a basis of \\(\Lambda^k(V)\\), the map \\(L\\) will be linear. Furthermore, note by definition \\(L \circ a = \omega\\) on tuples \\((E\_{i\_1}, \cdots, E\_{i\_k})\\) with \\(i\_1 < \cdots < i\_k\\), then because both \\(L \circ a\\) and \\(\omega\\) are alternating multilinear maps, this equality extends to all tuples \\((v\_1, \cdots, v\_k) \in V \times \cdots \times V\\).
<!-- TODO: possibly elaborate on last point of the above -->
<div style="text-align: right"> \(\square\) </div>

In fact, this uniiversal property uniquely characterizes \\(\Lambda^k(V)\\), which is formalized in the following proposition. 

**Prop.** \\(\Lambda^k(V)\\) is the unique vector space (up to isomorphism) satisfying the universal property of the wedge product.

*Proof.* 
<!-- TODO but this will be like every other such proof -->

<div style="text-align: right"> \(\square\) </div>

<!-- the algebra... maybe a different page. -->