---
layout: page
title: Fundamental Group
---

## Fundamental Group

If we suspect two topological spaces are homeomorphic, we have a simple method to prove so: construct a homeomorphism. However, how do we show two spaces are *not* homeomorphic? That is, how can we prove for certain there does not exist a homeomorphism between two spaces? One solution is to use a *topological invariant* -- a method of associating a mathematical object (such as a number or group) to the space so that homeomorphic objects recieve the same mathematical object. Then in order to prove two topological spaces are not equal, it suffices to prove their corresponding mathemathematical objects are not equal, which should be much easier.

The *fundamental group* is one such mathematical object that we can associate with a topological space \\(X\\). The fundamental group for \\(X\\), denoted \\(\pi_1(X)\\), is a group (as the same suggests). Then given another topological space \\(Y\\), in order to prove \\(X\\) and \\(Y\\) are not homeomorphic, it suffices to prove \\(\pi_1(X)\\) and \\(\pi_1(Y)\\) are not isomorphic. This strategy can be used to prove \\(\mathbb{R}^2\\) and \\(\mathbb{R}^2 \smallsetminus \{0\}\\) are not homeomorphic.

/\*explain fundamental group intuitively with pictures. Make sure to use same language used as motivation below\*/

/\*todo... pictures!\*/

#### Homotopy Equivalence of Paths

The notion of path homotopy formalizes what it means to "deform one path into another" as is required in the definition of the fundamental group.

**Def (Path homotopy).** Given two paths \\(\alpha, \beta: I \to X\\) on a topological space \\(X\\), a *path homotopy* from \\(\alpha\\) to \\(\beta\\) is a continuous map \\(H: I \times I \to X\\) such that \\(H(s,0) = \alpha(s)\\) and \\(H(s,1) = \beta(s)\\). If there exists a path homotopy from \\(\alpha\\) to \\(\beta\\) we say \\(\alpha\\) and \\(\beta\\) are *path homotopic* or *path homotopy equivalent*.

/\*give examples with visuals\*/

/\*define path homotopy fixed at the endpoints\*/

**Prop.** Path homotopy equivalence forms an equivalence relation on the set of all paths.

**Exercise.** Prove the proposition above. /\*TODO?\*/

Recall /\*remember to define this earlier...\*/ a *loop based at \\(p\\)* is a continuous map \\(\gamma: I \to X\\) such that \\(p = \gamma(0) = \gamma(1)\\). In order to define the fundamental group, we really want equivalence classes given by the following homotopy equivalence on loops. /\*explain this a bit more...\*/

**Def (Homotopy equivalence of loops fixing base point).** Consider two loops \\(\alpha, \beta: I \to X\\) on a topological space and let \\(p = \alpha(0) = \beta(0) = \alpha(1) = \beta(1)\\) be the base point of the loop. We say \\(\alpha\\) and \\(\beta\\) are *homotopy equivalent relative to the base point* if there exists a path homotopy \\(H: I \times I \to X\\) from \\(\alpha\\) to \\(\beta\\) such that \\p = (H(0,t) = H(1,t)\\).

**Prop. (Fundamental group elements).** Given a point \\(p\\) in a topological space \\(X\\), homotopy equivalence of loops fixing the base point forms an equivalence relation on the set of all loops based at \\(p\\). We call the set of all such equivalence classes *the fundamental group elements*, denoted \\(\pi_1(X,p)\\)*.

**Exercise.** Prove the proposition above.

We will make the set of equivalence classes \\(\pi_1(X,p)\\) defined above into a group in the followings section.

#### Fundamental Group

/\*give intuition again...\*/

**Def. (Path Multiplication).** /\*define this on paths... will prove invariance below\*/

**Def. (Fundamental Group).** Given a point \\(p\\) in a topological space \\(X\\), the *fundamental group* \\(\pi\_1(X, p)\\) is the set of fundmantal group elements described above (equivalence classes of loops) with the group operation given by path multiplication as defined above.

**Theorem.** The fundamental group is a well-defined group.

*Proof.* Show  

**Prop.** Take two points \\(p,q\\) in a topological space \\(X\\). If \\(X\\) is path connected, then \\(\pi_1(X,p) \simeq \pi_1(X,q)\\).

*Proof.* /\*TODO\*/

If the topological space \\(X\\) under consideration is path connected, we will often denote \\(\pi_1(X,p)\\) by simply \\(\pi_1(X)\\), dropping the particuar point as the above proposition reveals any choice of point provides the same group (up to isomorphism).

/\*define simply connected\*/

#### Examples

/\*prove \\(\R^n\\) gives trivial FG\*/

/\*talk about what \\(\mathbb{S}, \mathbb{T}^2\\) should be\*/

However, we can not yet formally prove \\(\pi_1(\mathbb{S}) \simeq \mathbb{Z}\\) and \\(\mathbb{T}^2 \simeq \mathbb{Z}^2\\). Doing so would require identifying the loop homotopy classes, which in turn requires proving two loops are *not* homotoptic relative to the base point. After all this work, it at first seems we have a similar problem that we discussed at the beginning: how do we show that two loops are *not* homotopic relative to the base point? Luckily, there are strategies for computing the fundamental group.