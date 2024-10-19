---
layout: page
title: Covering Maps
---

## Covering Maps

<!-- MOTIVATION AND ROUTE 1: COMPUTING FUNDAMENTAL GROUPS OF QUOTIENT SPACES -->

/\*discuss the fundmantal groups of \\(\mathbb{S}^1\\) and \\(\mathbb{T}^2\\) with pictures\*/

We suspect that \\(\pi_1(\mathbb{S}) \simeq \mathbb{Z}\\) and \\(\mathbb{T}^2 \simeq \mathbb{Z}^2\\). However, the proving so would require identifying the loop homotopy classes, which in turn requires proving two loops are *not* homotoptic relative to the base point. However, there is a technique to compute these homotopy classes, which stems from the observation that \\(\mathbb{S}^1 \simeq \mathbb{R}/\mathbb{Z}\\) and we suspect \\(\pi_1(\mathbb{S}) \simeq \mathbb{Z}\\). Similarly, \\(\mathbb{T}^2 \simeq \mathbb{R^2}/\mathbb{Z}^2\\) and we suspect \\(\pi_1(\mathbb{T}^2) \simeq \mathbb{Z}^2\\). This is no coincidence: we will see that the maps \\(q: \mathbb{R} \to \mathbb{S}^1\\) and \\(q: \mathbb{R^2} \to \mathbb{T}^2\\) are instances of *covering maps* and we can learn a lot about the fundamental groups of \\(\mathbb{S}^1\\), \\(\mathbb{T}^2\\), and many other spaces through covering maps.

#### Covering Maps

/\*Study spaces \\(X/G\\) for \\(G\\) some group first. Show this has the following properties (the following properties are the ones needes for proofs and slightly more general... ?)\*/

/\*why do we need connectectivity conditions on \\(E\\)?\*/

**Def (Covering Map).** A surjective continuous map \\(q: E \to X\\) from a connected and locally path connected topological space \\(E\\) to an arbitrary topological space \\(X\\) is a *covering map* if it satisfies the following condition. For all \\(p \in X\\), there must exist a neighborhood \\(U \subset X\\) containing \\(p\\) such that \\(q^{-1}(U)\\) is a disjoint union of connected open subsets of \\(E\\), each of which is mapped homeomorphically to \\(U\\) by \\(q\\).

/\*motivation for lifts, path lifting property, etc.\*/

**Thm (Path lifting property).** Let \\(q: E \to X\\) be a covering map and \\(\gamma: I \to X\\) a continuous path. Then, given a point \\(e \in q^{-1}(\gamma(0))\\), there exists a unique lift \\(\widetilde{\gamma}: I \to E\\) of \\(\gamma\\) such that \\(\widetilde{\gamma}(0) = e\\). 

*Proof.* For existence, begin by defining \\(\widetilde{\gamma}(0) = e\\). Next, cover \\(\gamma(I)\\) with evenly covered neighborhoods \\(\\{U_{\alpha}\\}\\), then by compactness there exists some Lebesgue number \\(\frac{1}{n}\\) such that each \\(\gamma([\frac{k}{n}, \frac{k+1}{n}])\\) is contained in some evenly covered neighborhood \\(U_k\\). Begin by defining \\(\widetilde{\gamma}(0) = e\\) and construct the rest inductively as follows. First take the inductive hypothesis to be that we have a lift \\(\widetilde{\gamma}_k: [0, \frac{k}{n}] \to E\\) of the restriction \\(\gamma: [0, \frac{k}{n}] \to X\\) such that \\(\widetilde{\gamma}_k(0) = e\\). Next, choose the evenly covered neighborhood \\(U_k \subset X\\) and the corresponding \\(V_k \ni \\widetilde{\gamma}_k(\frac{k}{n})\\) so that \\(q: V_k \to U_k\\) is a homeomorphism. Then let \\(\sigma_k: U_k \to V_k\\) be the inverse of \\(q\\) and define \\(\widetilde{\gamma}' := \sigma_k \circ \gamma: [\frac{k}{n}, \frac{k+1}{n}] \to E\\), noting this construction ensures \\(q \circ \widetilde{\gamma}' = \gamma\\) and that \\(\widetilde{\gamma}_k(\frac{k}{n}) = \widetilde{\gamma}'(\frac{k}{n})\\). Therefore we can glue \\(\widetilde{\gamma}\_k\\) and \\(\widetilde{\gamma}'\\) into the lift \\(\widetilde{\gamma}\_{k+1}: [0, \frac{k+1}{n}] \to E\\) of \\(\gamma: [0, \frac{k+1}{n}] \to X\\) with \\(\widetilde{\gamma}(0) = e\\). This inductive process eventually yields the desired lift \\(\widetilde{\gamma}\_n: I \to E\\).

For uniqueness, suppose \\(\gamma'\\) and \\(\widetilde{\gamma}\\) are any two such lifts and define the subset \\(\mathcal{A} := \\{x \in I: \widetilde{\gamma}(x) = \gamma'(x)\\}\\) with the goal of showing \\(\mathcal{A} = I\\). By \\(I\\)  connected, it suffices to show \\(\mathcal{A}\\) is open, closed, and nonempty. Our assumption gives \\(\widetilde{\gamma}(0) = e = \gamma'(0)\\) thus \\(0 \in \mathcal{A}\\), giving \\(\mathcal{A}\\) is nonempty. For openness, take \\(x \in \mathcal{A}\\) and let \\(U \subset X\\) be an evenly covered neighborhood of \\(\gamma(x)\\). Thus there exists a neighborhood \\(V \subset E\\) of \\(\widetilde{\gamma}(x) = \gamma'(x)\\) such that \\(q: V \to U\\) is a diffeomorphism. Thus by \\(q\\) is injective over \\(V\\) and by
\\[
    q \circ \widetilde{\gamma}(x) = \gamma(x) = q \circ \gamma'(x),
\\]
we have \\(\widetilde{\gamma}(x) = \gamma'(x)\\) when \\(\\widetilde{\gamma}(x), \gamma'(x) \in V\\) and hence for all \\(x \in \gamma^{-1}(U)\\). Finally, closedness follows because \\(\mathcal{A}\\) is defined using a closed condition. Indeed, formally take \\(x \in \mathcal{A}^c\\) so that \\(\widetilde{\gamma}(x) \neq \gamma'(x)\\). Then by \\(E\\) Hausdorff, take disjoint neighborhoods \\(\widetilde{V}, V' \subset E\\) containing \\(\widetilde{\gamma}(x)\\) and \\(\gamma'(x)\\) respectively. Therefore we have the open neighborhood \\(\widetilde{\gamma}^{-1}(\widetilde{V}) \cap \gamma'^{-1}(V') \subset \mathcal{A}^c\\) 'of \\(x\\), so \\(\mathcal{A}^c\\) is open and we conclude \\(\mathcal{A}\\) is closed.
<div style="text-align: right"> \(\square\) </div>