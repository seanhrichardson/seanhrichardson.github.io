---
layout: page
title: Topological Manifold
---

<!-- prereqs:
- manifolds
- basic topology
- sequences? -->

## Topological Manifold

Recall our extrinsic definition of a topological manifold below, noting *locally Euclidean* /\*link?\*/ means that every point has a neighborhood homeomorphic to a subset of \\(\mathbb{R}^n\\). 

**Extrinsic definition of topological manifold.** A subset \\(M \subset \mathbb{R}^m\\) is called an *\\(n\\)-dimensional manifold* if \\(M\\) is locally Euclidean of dimension \\(n\\).

Our goal in this section is to provide an equivalent definition for topological manifold as simply a topological space that satisfies particular properties, removing the dependence of this definition on \\(\mathbb{R}^m\\). For this, we first study properties of a manifold.

<!-- below section is on Hausdorff spaces, hopefully indepedent of manifolds... could potentially move this to the topology section? Although I think here is better for the manifold sequence? -->

/\*could avoid sequences and \*/

General topological spaces \\(X\\) can be quite poorly behaved in having so few open sets such that a sequence \\(x_n\\) converges to multiple points! For example, if \\(X\\) has the trivial topology, then any sequences \\(x_n\\) converges to every point! For many purposes, this is absurd and so we will want our space \\(X\\) to satisfy some property that ensures there are enough open sets so that this does not happen. One such property is *Hausdorff*, which in the formal definition below esnures that open sets are able to distinguish between distinct points.

**Def (Hausdorff).** A topological space is *Hausdorff* is for any two distinct points \\(p,q \in X\\) there exists an open set \\(U_p\\) containing \\(p\\) and an open set \\(U_q\\) containing \\(q\\) that are disjoint; that is, \\(U_p \cap U_q = \emptyset\\).

/\*any metric space (for example) is Hausdorff\*/

/\*this indeed ensures sequences converge to unique points\*/

/\*subspace of Hausdorff space is Hausdorff\*/

<!-- -->

Note that any manifold \\(M \subset \mathbb{R}^m\\) must be Hausdorff. Indeed, \\(\mathbb{R}^m\\) is Hausdorff because it is a metric space and therefore \\(M\\) is Hausdorff because it is a subspace of a Hausdorff space.

<!-- below section is on 2ns countable spaces spaces, hopefully indepedent of manifolds... could potentially move this to the topology section? Although I think here is better for the manifold sequence? -->


/\*think of better motivation: bellow is better motivation for first countable spaces... also would be preferable to avoid sequences...\*/

In metric spaces, we have a convenient sequence definition of continuity: \\(f: X \to Y\\) is continuous if \\(x_n \to x\\) implies \\(f(x_n) \to f(x)\\). However, a general topological space \\(X\\) can have so many open sets that the sequence definition of continuity does not work. /\*give example?\*/. One property that guarantees this definition works is the notion of \\(2nd\\) countability.

/\*etc.........\*/

/\*Eucliden space is 2ns countable\*/

/\*subspace of 2nd countable space is 2nd countable\*/

<!---->

Thus we have concluded that a manifold \\(M\\), in addition to being locally Euclidean, is also Hausdorff and 2nd countable. In fact, it has been shown /\*cite and say hard proof\*/ that if a topological space \\(X\\) is locally Euclidean, Hausdorff, and 2nd countable, then this topology arises from some some topological manifold as defined extrinsically. In other words, the following intrinsic definition identifies precisely the same topological spaces as the extrinsic definition.

**Intrinsic definition of topological manifold.** A topological space \\(M\\) is a *topological manifold* if it is locally Euclidean, Hausdorff, and 2nd countable.