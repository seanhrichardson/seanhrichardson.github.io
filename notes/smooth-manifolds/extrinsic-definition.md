---
layout: page
title: Extrinsic Definition of Smooth Manifolds
---

## Smooth Manifolds

/\*TODO: define diffeomorphism between subsets of \\(\mathbb{R}^n\\) in some earlier page\*/

/\*some visual pictures of manifolds (perhaps no need for explanation)\*/

Manifolds are subsets of some Euclidean space \\(\mathbb{R}^m\\) that locally "looks like" some \\(\mathbb{R}^n\\). For topological manifolds, which only have information about the topology, the formal notion of "looks like" is given by homeomorphisms. We want *smooth manifolds* to encode the differentiability of the manifold, so we instead use the notion of diffeomorphism.

Recall /\*link\*/ 

**Def. (Diffeomorphism between subsets of \\(\mathbb{R}^n\\)).** /\*TODO... give this definition\*/ 

We are now ready to give an extrinsic definition of a smooth manifold.

**Extrinsic definition of smooth manifold.** A subset \\(M \subset \mathbb{R}^m\\) is an \\(n\\)-dimensional smooth manifold if every point of \\(M\\) has a neighborhood diffeomorphic to an open subset of \\(\mathbb{R}^n \subset \mathbb{R}^m\\).

/\*give some concrete examples... smooth graph, \\(\mathbb{S}^2\\), maybe \\(\mathbb{T}^2\\), etc. give arguments verifying they are manifolds.\*/

However, modern mathematics has done away with defining manifolds *extrinsically* (as subsets of \\(\mathbb{R}^m\\)). Instead, we favor defining manifolds *intrinsically*, as mathematical objects in their own right. We will now work towards developing an intrinsic definition of smooth manifolds. While the extrinsic definition is more intuitive, the intrinsic definition will be easier to work with when formally studying manifolds.