---
layout: page
section: NOTES
title: Chapter 2
---

## Chapter 2


First, know the fundamental definitions: *open set*, *closed set*, *topological space*, *continuos*, *homeomorphism*, *homeomorphic*, *open map*, *closed map*, *Hausdorff*, *basis*, *second countable*, 

Additional definitions include *neighborhood of a point*, *neighborhood of a subset*, *closure*, *interior*, *exterior*, *boundary*, *limit point*, *isolated point*, *dense*, *convergent sequence*, *limit of a sequence*, *finer*, *coarser*, *local homeomorphism*, 

Some fundamental topological spaces include *discrete topology*, *trivial topology*, *metric topology*, *Euclidean topology*, *unit interval*, *open unit ball*, *closed unit ball*, *unit circle*, *unit $n$-sphere*, 

See **Proposition 2.8.** for equivalent conditions for determining when a point is in the interior, exterior, boundary, closure, and other related results.

**Proposition 2.17.** The constant map, the identity map, the restriction of a continuous function to an open subset, and the composition of continuous functions are all continuous.

**Proposition 2.19 (Continuity is a Local Property)** $f: X \to Y$ continuous iff every point in $X$ has a neighborhood such that $f$ restricts to a continuous function.

*Proof.* If $f$ continuous, then take neighborhoods to be $X$ itself.
Conversely, if $f$ is continuous over neighborhoods $\\{V\_x\\}\_{x \in X}$,
 then for any open $U \subset Y$, we have $f^{-1}(U) = \bigcup_{x \in X} f^{-1}(U) \cap V_x = \bigcup_{x \in X} f^{-1}|_{V_x}(U)$ is open.

**Proposition 2.31.** Local homeomorphisms are continuous and open and bijective local homeomorphisms are homeomorphisms.

Note Hausdorff spaces are designed such that limit points are unique and finite subsets are closed (**Proposition 2.37**).

**Basis Criterion (pg. 33)** Given basis $\mathcal{B}$, a set is open iff for each $p \in U$, there exists $B \in \mathcal{B}$ such that $p \in B \subset U$.

**Proposition 2.43 (Suffices to check basis for continuity).** Given basis $\mathcal{B}$ for $Y$, a map $f: X \to Y$ is continuous if and only if $f^{-1}(B)$ is open for all $B \in \mathcal{B}$.