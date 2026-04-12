---
layout: page
title: Topological Manifolds
---

# Topological Manifolds

/\*big picture why mathematicians are interested in manifolds\*/

/\*some visual examples with pictures of manifolds\*/

All of the above examples have one important property: a neighborhood each point \\(p\\) of an \\(n\\) dimensional manifold \\(M \subset \mathbb{R}^m\\) locally "looks like" \\(\mathbb{R}^n\\). Precisely defining what a manifold requires speciying what we mean by "looks like". If we are only interested in the topology of the manifold, then we define "looks like" using the notion of homeomorphism.

/\*note on smooth and Riemannian manifolds...\*/

## Review of Topology

Consider the sphere \\(\mathbb{S}^2 := \\{(x,y,z) \in \mathbb{R}^3 : x^2 + y^2 + z^2 = 1\\}\\) as a subspace of \\(\mathbb{R}^3\\) with topology given by the "subspace topology". That is, a set \\(U \subset \mathbb{S}^2\\) is open if for all \\(p \in U\\), there is some small ball centered at \\(p\\) and of radius \\(\varepsilon > 0\\) so that \\(B\_{\varepsilon}(p) \cap \mathbb{S}^2 \subset U\\). 

/\*TODO... DEFINE WHAT I NEED LATER... IDEALLY I ONLY REQUIRE BASIC TOPOLOGY PAGE...\*/

/\*PERHAPS HIGHLIGHT LOCAL HOMEOMORPHISM BETWEEN \\(\mathbb{S}^2\\) and \\(\mathbb{R}^2\\)?\*/

## Extrinsic Definition of Topological Manifolds
/\*some motivation...\*/

A subset \\(M \subset \mathbb{R}^m\\) is a ***topological manifold*** of dimension \\(n\\) if every \\(p \in M\\) has a neighborhood \\(U \subset M\\) homeomorphic to an open subset \\(V \subset \mathbb{R}^n\\).

/\*some examples and non-examples\*/

## Intrinsic Definition of Topological Manifolds

However, while the above definition is what /\*Gauss used? give some history?\*/, it has the limitation of requiring a manifold to be a subset of some "ambient Euclidean space" \\(\mathbb{R}^m\\). That is, it is an *extrinsic* definition. Instead, the modern approach to manifold theory is to define manifolds as mathematical objects in their own right satisfying particular properties; that is, an *intrinsic* definition. This intrinsic approach has a few advantages.
1. All manifolds *can* be realized as subsets of \\(\mathbb{R}^m\\), but for some manifolds, it is unnatatural to do so. The modern definition allows the flexibility to define these manifolds in more convenient ways, we just need to check that it satisfies the necessary properties.
2. Proving results about manifolds in general will be easier because the relevant properties will be more readily available. Furthermore, it will be more clear what properties are responsible for the theorem, providing us with a deeper understanding.
3. Requiring manifolds to subsets of \\(\mathbb{R}^m\\) as in the extrinsic definition provides extraneous information and structure that is often more distracting than useful.

However, the extrinsic approach has the singular advantage of a relatively simple and intuitive definition whereas understanding the intrinsic definition of topological manifolds requires some more motivation and patience. However, the work is worth it for the reasons listed above.

A first naive atempt to give an intrinsic definition of topological manifold is to simply consider any locally Euclidean topological space \\(X\\). However, removing the requirement of an ambient Euclidean space allows for some strange spaces such as the "line with two origins".

**Example.** /\*LINE WITH TWO ORIGINS... define, show locally Euclidean but convergence is not unique\*/

/\*todo: for those familiar with quotient topology, note we can define this as a quotient.\*/

/\*Hausdorff\*/

/\*2nd countable\*/