---
layout: page
title: Special Relativity
---

# Special Relativity

<!-- perhaps rephrase some of the below to emphasize I am working on a vector space... emphasize this linearization at some point? perhaps rephrase observers as a choice of basis? -->

<!-- TRY TO SHORTEN AND SIMPLIFY THE BELOW LOGIC. -->

<!-- TODO: REPLACE BELOW WITH \ETA -->

<!-- TODO: maybe an observer should be a time-like vector (p, v) in tangent space? -->

Experimentally, we find all observers measure the speed of light to be the same speed \\(c\\), so we choose coordinates so that \\(c = 1\\). However, even observers that are moving relative to eachother will measure the same light beam to be moving at speed \\(c\\), which defies our intuition for how we expect velocities to add. From a few axioms, we can deduce how velocities should add and derive the rules of special relativity.

We consider an ***event*** to be a point \\((x, y, z)\\) in space at a particular time \\(t\\) and we define ***space-time*** to be the space \\(\mathbb{R} \times \mathbb{R}^{3} = \mathbb{R}^{3+1}\\) of all events. An observer moving at constant speed in space will consider themselves to be stationary, so we define an ***observer*** to be a choice of coordinates \\((t, x, y, x)\\) on space-time moving along the \\(t\\)-axis. While observers will not agree on coordinates, we find 
1. All observers measure the same speed of light \\(c\\).
2. /\*TODO: principle of relativity\*/

/\*TODO: note we will linearize and treat \\(\mathbb{R} \times \mathbb{R}^{3}\\) as a vector space\*/

Consider two observers at the same point in space-time, which corresponds to coordinates \\((t, x, y, z)\\) and \\((\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z})\\) where the both coordinates agree on the point \\((0,0,0,0)\\). Then, note that by the universality of the speed of light, \\((t, x, y, z)\\) must observe a pulse of light starting from this origin at time \\(t = 0\\) to be in the set
\\[
    Z = \left\\{(t, x, y, z) : -t^2 + x^2 + y^2 + z^2 = 0\right\\}.
\\]
By the same reasoning, \\((\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z})\\) observes the same pulse of light to be in the set
\\[
    \widetilde{Z} = \left\\{(\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z}) : -\widetilde{t}^2 + \widetilde{x}^2 + \widetilde{y}^2 + \widetilde{z}^2 = 0\right\\}.
\\]
Note \\(Z\\) and \\(\widetilde{Z}\\) describe the same set in different coordinates and so \\(Z = \widetilde{Z}\\). A convenient way to rewrite this finding is to define the bilinear form \\(m: \mathbb{R}^{3+1} \times \mathbb{R}^{3+1} \to \mathbb{R}\\) in coordinates \\((t, x, y, z)\\)
\\[
    m((t\_1, x\_1, y\_1, z\_1), (t\_2, x\_2, y\_2, z\_2)) = -t\_1t\_2 + x\_1x\_2 + y\_1y\_2 + z\_1z\_2
\\]
together with bilinear form \\(\widetilde{m}: \mathbb{R}^{3+1} \times \mathbb{R}^{3+1} \to \mathbb{R}\\) in coordinates \\((\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z})\\) defined by
\\[
    \widetilde{m}((\widetilde{t}\_1, \widetilde{x}\_1, \widetilde{y}\_1, \widetilde{z}\_1), (\widetilde{t}\_2, \widetilde{x}\_2, \widetilde{y}\_2, \widetilde{z}\_2)) = -\widetilde{t}\_1\widetilde{t}\_2 + \widetilde{x}\_1\widetilde{x}\_2 + \widetilde{y}\_1\widetilde{y}\_2 + \widetilde{z}\_1\widetilde{z}\_2.
\\]
Then the statement \\(Z = \widetilde{Z}\\) can be rewritten as
\\[
    \\{v \in \mathbb{R}^{3+1}: m(v,v) = 0\\} = \\{v \in \mathbb{R}^{3+1}: \widetilde{m}(v,v) = 0\\}.
\\]
That is, the zero sets of \\(m(v,v)\\) and \\(\widetilde{m}(v,v)\\) are identical. This is quite restrictive and indeed, the following lemma implies these two forms must be exactly equal.

**Lemma.** These bilinear forms are equal: \\(m = \widetilde{m}\\).

*Proof.* /\*TODO... I might want to first prove \\(m = \alpha\widetilde{m}\\) in this lemma, then separately argue the constant is \\(1\\)\*/.

Therefore, we find all observers agree on this symmetric bilinear map \\(m: \mathbb{R}^{3+1} \times \mathbb{R}^{3+1} \to \mathbb{R}\\) called the ***Minkowski metric*** which with respect to any observer \\((t, x, y, z)\\) has the form
\\[
    m = -dt^2 + dx^2 + dy^2 + dz^2.
\\]

<!-- TODO perhaps briefly argue here that any observer with the same Minkowski metric must observe the same speed of light? -->

Furthermore, recall we call a symmetric bilinear map \\(q: V \times V\\) over a vector space \\(V\\) ***non-degenerate*** if the map \\(\hat{q}: V \to V^*\\) defined by
\\[
    \hat{q}(v)(w) = q(v,w)
\\]
is an isomorphism.

**Lemma.** The Minkowski metric \\(m\\) is non-degenerate.

*Proof*. /\*TODO.\*/

Recall a non-degenerate, symmetric, bilinear map is called a ***scalar product***. Furthermore, /\*TODO\*/

<!-- TODO: REFERENCE SOME SCALAR PRODUCT THEORY.... CLASSIFY POSSIBLE MINKOWSKI METRICS BY SCALAR METRICS OF SIGNATURE 1 (SEE LEE R-M pg. 40) -->

<!-- TODO: POSSIBLY END THIS PAGE WITH DEFINITIOIN OF MINKOWSKI SPACE-TIME AND PICK UP FORMAL MATHEMATICAL TREATMENT ELSEWHERE? -->

## Minkowski Spacetime

A scalar product \\(\eta\\) over \\(\mathbb{R}^{3+1}\\) with signature \\((3,1)\\)  is called a ***Minkowski metric*** and the pairing \\((\mathbb{R}^{3+1}, m)\\) is called ***Minkowski spacetime***. 

<!-- TODO: use Minkowski metric to compute relative velocities between observers -->

## Lorentz Transformations

A ***Lorentz transformation*** over Minkowski space-time \\((\mathbb{R}^{3+1}, \eta)\\) is a linear transformation \\(L: \mathbb{R}^{3+1} \to \mathbb{R}^{3+1}\\) that preserves the Minkowski metric, meaning \\(L^*\eta = \eta\\).

<!-- TODO: DERIVE FORM FOR LORENTZ TRANSFORMATION -->



<span style="display:none">
{% cite stavrov-gr %}
{% cite sachs-wu %}
<!-- TODO tong general relativity -->
</span>

## References

{% bibliography --cited %}