---
layout: page
title: Tangent Vectors
---

## Tangent Vectors

#### Vector Fields in \\(\mathbb{R}^n\\)

Recall the concept of a *vector field* \\(V\\) in \\(\mathbb{R}^n\\). At each point \\(p \in \mathbb{R}^n\\), we place a vector \\(V_p \in \mathbb{R}^n\\). Importantly, notice that in such vector fields, we use Euclidean space \\(\mathbb{R}^n\\) in two fundamentally different ways. Firstly, as a space containing *points* \\(p \in \mathbb{R}^n\\) in which the *manifold structure* of \\(\mathbb{R}^n\\) is most relevant, and secondly as a *vector space* at every point \\(p\\) called the *tangent space at \\(p\\)*, which is the space that the *tangent vector* \\(V_p\\) is an element of.

/\*figure of vector field, tangent vector, tangent space\*/

In this section, we work towards defining tangent vectors on an arbitrary smooth \\(n\\)-manifold \\(M\\). Observe that simply associating some \\(V_p \in \mathbb{R}^n\\) to a point \\(p \in M\\) no longer works, for it is unclear what direction such a vector points in! This strategy only worked for \\(M = \mathbb{R}^n\\) because of the extra structure of \\(\mathbb{R}^n\\) (in particular, the ability to compare vectors based at different points by translating). For a general smooth manifold \\(M\\), we need a different strategy.

#### Extrinsic Tangent Vectors

To build intuition, we will first study tangent vectors on an extrinsically defined \\(n\\)-manifold \\(M \subset \mathbb{R}^m\\). We have already discussed the case of \\(M = \mathbb{R}^n\\): at each point \\(p \in \mathbb{R}^n \subset \mathbb{R}^m\\), the tangent space at \\(p\\), denoted \\(T_p\mathbb{R}^n\\), is simply a copy of \\(\mathbb{R}^n \subset \mathbb{R}^m\\) (now considered as a vector space and a linear subspace of a copy of \\(\mathbb{R}^m\\)). 

/\*picture of below for \\(M = \mathbb{S}^2\\)\*/

We can carry over our understanding of tangent spaces on \\(\mathbb{R}^n\\) to a general extrinsically defined \\(n\\)-manifold \\(M \subset \mathbb{R}^m\\) by using and that \\(M\\) locally looks like \\(\mathbb{R}^n\\). Given \\(p \in M\\), there will be a neighborhood \\(U\\) of \\(M \subset \mathbb{R}^m\\), a neighborhood \\(V\\) of \\(\mathbb{R}^n \subset \mathbb{R}^m\\), and a diffeomorphism \\(\varphi: V \to U\\) such that \\(\varphi(0) = p\\). By definition of diffeomorphism, this will extend to a diffeomorphism \\(\varphi: \widetilde{V} \to \widetilde{U}\\) between open subsets of \\(\mathbb{R}^m\\). Then, we can simply define \\(T_pM\\) to be the subspace given by the image \\(D\varphi_0(T_0\mathbb{R}^m) \subset \mathbb{R}^m\\) where \\(D\varphi\\) is the Jacobian of \\(\varphi\\). Visually, this literally gives the subspace of all vectors tangent ("parallel") to the surface at \\(p\\).

#### Motivation for Intrinsic Definition
As seen by the use of the Jacobian above, tangent vectors on are closely connected to differentiation; this connection will allow us to intrinsically define vectors on smooth manifolds and is why a smooth structure is necessary for the notion of tangent vectors. Two more important such connectections are as follows, letting \\(M \subset \mathbb{R}^n\\) be an extrinsically defined \\(n\\)-manifold and \\(p \in M\\).
1. Given a smooth curve \\(\gamma: \mathbb{R} \to M \subset \mathbb{R}^m\\) with \\(\gamma(0) = p\\), the velocity vector \\(\gamma'(0) \subset \mathbb{R}^m\\) will be an element of the tangent space \\(T_pM\\).
2. Given a smooth function \\(f: M \to \mathbb{R}\\) and a tangent vector \\(v \in T_pM\\), we can compute the derivative of \\(f\\) in the direction of \\(v\\), denoted \\(\nabla_v\\). For example, simply extend \\(f\\) to an open set \\(\widetilde{U} \supset M\\) of \\(\mathbb{R}^m\\), then compute \\(\nabla_vf := (D_pf) v\\).

**Exercise.** Show the definition of \\(\nabla_v\\) above is independent of the choice of extension of \\(f\\).

<!-- by choosing a smooth curve \\(\gamma: \mathbb{R} \to M\\) with \\(\gamma(0) = p\\) and \\(\gamma'(0) = v\\), then computing \\((f \circ \gamma)'(0)\\). -->

The above properties of tangent vectors motivates two possible intrinsic definition of tangent vectors.
1. Tangent vectors are the velocities of smooth curves.
2. Tangent vectors are the directional derivatives of smooth maps.

In fact, both approaches for a formal definition work! While (1) is more visual, we will go with (2) because the definition is technically easier, and directional derivatives on manifolds are extremely useful, so it is conveient to think of tangent vectors as a literal directional derivative operation. To educate our formal intrinsic defintion, we first study the properties of directional derivatives defined extrinsically.

For the following, \\(M \subset \mathbb{R}^m\\) remains an extrinsically defined smooth manifold and fix a point \\(p \in M\\). Note that the directional derivative operation is linear; indeed, if \\(f,g: M \to \mathbb{R}\\) are smooth functions, \\(\alpha, \beta \in \mathbb{R}\\) are real numbers, and \\(v \in T_pM\\) is a tangent vectors, we can compute
\\[
    \nabla_{v}(\alpha f + \beta g) = D_p(\alpha f + \beta g) v = \alpha (D_p f) v + \beta (D_p g) v = \alpha \nabla_v f + \beta \nabla_v g.
\\]
Furthermore, we see directional derivatives satisfy the following product rule:
\\[
    \nabla_{v}(fg) = D_p(fg) v = (f(p)D_pg + g(p)D_pf)v = f(p)(D_pg)v + g(p)(D_pf)v = f(p) \nabla_v g + g(p) \nabla_v f.
\\]

#### Intrinsic Definition
We are finally ready to intrinsically define tangent vectors. For this sectioin, let \\(M\\) be a smooth manifold (defined intrinsically) and fix a point \\(p \in M\\). We now define the notion of a *derivation*, which is simply another name for the directional derivative.

/\*is continuity important or implied anywhere?\*/

**Def (derivation).** A linear map \\(v: C^{\infty}(M) \to \mathbb{R}\\) is called a *derivation at \\(p\\)* if it satisfies the product rule
\\[
    v(fg) = f(p)vg + g(p)vf \quad \text{for all } f,g \in C^{\infty}(M).
\\]

As planned, we now define the *tangent space at \\(p\\)* to be the vector space of all derivations (which represent directional derivatives), and each derivation is interpreted as a *tangent vector*.

**Def (tangent space).** The set of all derivations of \\(C^{\infty}(M)\\) at \\(p\\) is called the *tangent space to \\(M\\) at \\(p\\)* and is denoted by \\(T_pM\\). An element \\(v \in T_pM\\) is called a *tangent vector at \\(p\\)*.

**Prop.** Each tangent space \\(T_pM\\) is a vector space.

*Proof.* Let \\(v,w \in T_pM\\) be tangent vectors and let \\(\alpha, \beta \in \mathbb{R}\\) be real numbers. Then addition of tangent vectors is defined to be the linear map \\((v+w)f := vf + wf\\). Scalar multiplication on tangent vectors is defined to be the linear map \\((\alpha v) f := \alpha (vf)\\). Importantly, observe that the linear combination of tangent vectors will still satisfy the product rule and therefore remain a tangent vector:
\\[\begin{align}
    (\alpha v + \beta w)(fg) 
    &= \alpha v(fg) + \beta w(fg)\\\\\
    &= \alpha f(p)vg + \alpha g(p) vf + \beta f(p) wg + \beta g(p) wf\\\\\
    &= f(p)(\alpha v + \beta w)g + g(p)(\alpha v + \beta w)f.
\end{align}\\]

**Exercise.** Complete the above proof.

**Prop. (dimension of the tangent space).** If \\(M\\) is an \\(n\\)-dimensional smoooth manifold, the tangent space \\(T_pM\\) at each \\(p \in M\\) is an \\(n\\)-dimensional vector space.

*Proof.* /\*TODO\*/