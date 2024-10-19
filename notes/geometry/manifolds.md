---
layout: page
title: Manifolds
---
<!-- 
pre reqs: 
- basic topology
- subspace topology
-->


<!-- TODO:
This is written for Riemannian manifolds, but this can be greatly shortened if the goal is only topological manifolds. -->

## Manifolds

/\*perhaps explain big picture why mathematicians are interested in manifolds\*/

/\*some visual examples wiwth pictures\*/

All of the above examples have one important property: a neighborhood each point \\(p\\) of an \\(n\\) dimensional manifold \\(M \subset \mathbb{R}^m\\) locally "looks like" \\(\mathbb{R}^n\\). Precisely defining what a manifold requires speciying what we mean by "looks like". If we are only interested in the topology of the manifold, then we can use the notion of homeomorphism to precisely define what we mean by "looks like" as follows.


/\*possibly do not give definition of locally Euclidean now... do it later in the topological manifold section. For now, just say every point has a neighborhood homeomorphic to an open subset of \\(\mathbb{R}^n\\)\*/

**Def. (Locally Euclidean).** A topological space \\(X\\) is *locally Euclidean of dimension \\(n\\)* if for each \\(p \in X\\), there exists an open set \\(U \subset X\\) containing \\(p\\) that is homeorphic to an open subset \\(U \subset \mathbb{R}^n\\).

With this definition in hand, we can give a formal definition of manifold.

**Extrinsic definition of topological manifold.** A subset \\(M \subset \mathbb{R}^m\\) is an *\\(n\\)-dimensional manifold* if \\(M\\) is locally Euclidean of dimension \\(n\\).

/\*some concrete examples with verification they are topological manifolds\*/

However, while the above definition is what /\*Gauss used? give some history?\*/, it has the limitation of requiring a manifold to be a subset of \\(\mathbb{R}^m\\) for some \\(m\\); that is, it is an *extrinsic* definition. Instead, the modern approach to manifold theory is to define manifolds as mathematical objects in their own right satisfying particular properties; that is, an *intrinsic* definition. This intrinsic approach has a few advantages.

1. All manifolds *can* be realized as subsets of \\(\mathbb{R}^m\\), but for some manifolds, it is unnatatural to do so. The modern definition allows the flexibility to define these manifolds in more convenient ways, we just need to check that it satisfies the necessary properties.
2. Proving results about manifolds in general will be easier because the relevant properties will be more readily available. Furthermore, it will be more clear what properties are responsible for the theorem, providing us with a deeper understanding.
3. Requiring manifolds to subsets of \\(\mathbb{R}^m\\) as in the extrinsic definition provides extraneous information and structure that is often more distracting than useful.

In fact, the modern approach defines several different types of manifolds. For example,
* A *topological manifold* is any topological space that could come from a manifold as defined above.
* A *smooth manifold* is a topological manifold with some extra structure that allows us to do calculus on the manifold (for example, differentiating functions on the manifold).
* A *Riemannian manifold* is a smooth manifold with some extra structure that gives the manifold geometry: angles, lenths, areas, etc.

Distinguishing between manifolds with different levels of structure is useful in light of point (2) above: if we prove a theorem for topological manifolds, then only the topology of the manifold is relevant. However, if we prove a theorem for Riemannian manifolds, then the result likely depends on the geometry of the manifold.

However, there is one major disadvantage with this modern approach: if I gave you the intrinsic definitions for topological, smooth, and Riemannian manifolds right now, they would make no sense. Thus we will use slowly build towards these definitions.