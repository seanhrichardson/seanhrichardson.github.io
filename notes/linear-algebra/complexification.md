---
layout: page
title: Complexification
section: Complexification
---

# Complexification

We often encounter a situation where we have a real vector space \\(V\\) and a complex vector space \\(W\\) together with a real linear map \\(L: V \to W\\), meaning
\\[
    L(\alpha v) = \alpha L(v)
\\]
for all \\(\alpha \in \mathbb{R}\\) and \\(v \in V\\). However, it would be nicer and provide more structure if we had a *complex* linear map. Thus we wish to naturally extend \\(V\\) to a complex vector space \\(\widetilde{V}\\) and extend \\(L\\) to a complex linear map \\(L: \widetilde{V} \to W\\). One way to accomplish this is to define the *complexiciation* \\(\mathbb{C} V := V \otimes\_{\mathbb{R}} \mathbb{C}\\) (i..e the tensor product between \\(V\\) and \\(\mathbb{C}\\) when considered as real vector spaces) together with the natural embedding \\(\iota: v \mapsto v \otimes 1\\). Indeed, we may now define a natural complex-linear map \\(\widetilde{L}: \mathbb{C} V \to W\\) by \\(\widetilde{L}(v \otimes \alpha) := \alpha L(v)\\), which then extends uniquely to \\(\mathbb{C} V\\) by linearity. In other words, we have defined a complex linear \\(\widetilde{L}: \mathbb{C} V \to W\\) such that \\(\widetilde{L} \circ \iota = L\\); that is, such that the following diagram commutes.

/\*TODO... diagram\*/

In fact, this choice of \\(\widetilde{L}\\) is canonical by the following proposition.

**Prop 1.** Fix a real vector space \\(V\\), then consider a complex vector space \\(W\\) together with a real-linear map. Taking \\(\widetilde{V} := \mathbb{C}V\\) the complexification of \\(V\\), then there exists a unique complex linear map such that \\(\widetilde{L}: \widetilde{V} \to W\\) such that \\(\widetilde{L} \circ \iota = L\\).

*Proof.* For uniqueness, consider any complex-linear map \\(\widetilde{L}: \widetilde{V} \to W\\) such that \\(\widetilde{L} \circ \iota = L\\). But then 
\\[
  \widetilde{L}(v \otimes \alpha)
  = \widetilde{L}(\alpha(v \otimes 1))
  = \alpha (\widetilde{L} \circ \iota)(v)
  = \alpha L(v).
\\]
That is, \\(\widetilde{L}\\) must satisfy \\(\widetilde{L}(v \otimes \alpha) = \alpha L(v)\\), which has a unique complex-linear extension to \\(\mathbb{C} V\\). For existence, define \\(\widetilde{L}\\) to be precisely this unique complex-linear extension satisfying \\(\widetilde{L}(v \otimes \alpha) = \alpha L(v)\\).

In fact, Property 1 uniquely characterizes \\(\mathbb{C} V\\), which is summarized as follows:

**Thm (Universal property of complexification).** Fix a real vector space \\(V\\). Then the complexification \\(\mathbb{C} V\\) of \\(V\\) is the unique complex vector space satisfying Proposition 1.

*Proof.* We have already proven \\(\mathbb{C} V\\) satisfies Proposition 1. For uniqueness, suppose \\(\widetilde{V}\_1\\) and \\(\widetilde{V}\_2\\) are two vector spaces satisfying Proposition 1. Indeed, by applying Proposition 1 to the real-linear map \\(\iota\_1: V \to \widetilde{V}\_2\\) yields a complex linear map \\(B: \widetilde{V}\_1 \to \widetilde{V}\_2\\) such that \\(B \circ \iota\_2 = \iota\_1\\). In the same way, applying Proposition 1 to the real-linear map \\(\iota\_2: V \to \widetilde{V}\_1\\) yields a complex linear map \\(A: \widetilde{V}\_2 \to \widetilde{V}\_1\\) such that \\(B \circ \iota\_1 = \iota\_2\\). Therefore 
\\[
    (B \circ A) \circ \iota\_1 = B \circ \iota\_2 = \iota\_1
    \tag{\\(\star\\)}
    \label{eq:up}.
\\]
But note \\(\operatorname{Id}: \widetilde{V}\_1: \widetilde{V}\_1\\) satisfies \\(\operatorname{Id} \circ \iota\_1 = \iota\_1\\) and by the uniqueness in Proposition 1 and (\ref{eq:up}), we must have \\(B \circ A = \operatorname{Id}\\). Similarly, \\(A \circ B = \operatorname{Id}\\) and therefore \\(\widetilde{V}\_1 \cong \widetilde{V}\_2\\).
<!-- todo... elaborate on this last part? -->

/\*add figure...\*/