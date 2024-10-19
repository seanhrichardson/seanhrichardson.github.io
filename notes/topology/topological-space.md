---
layout: page
title: Topological Spaces
---

## Topological Spaces

Recall that a metric space \\((X,d)\\) has the following notion of an *open set*. We say \\(U \subset X\\) is open if for all \\(x \in U\\), there exists some \\(\varepsilon > 0\\) such that the open ball \\(\\{x' \in X: d(x,x') < \varepsilon\\}\\) is a subset of \\(U\\). Recall these open sets are related to continuous functions by the following.

*A function \\(f: X \to Y\\) between two metric spaces is continuous if and only if for each open set \\(U \subset Y\\), the preimage \\(f^{-1}(U)\\) is open.*

**Exercise.** If you are not familiar with the above statement, prove it.

That is, we only need to know the open sets to understand continuous functions. The field of topology generalizes the notion of metric spaces by abandoning the idea of a metric and replacing it with a "topology", which only contains the information on which sets are open. Then we can still define a notion of "continuous function" using the above. In fact, we will see that we can define convergence of sequences, compactness, connectedness, and many other notions using only open sets. There are many important spaces that can be given a natural topology but cannot be given a metric that agrees with this topology, so this generalization is essential. Furthermore, abandoning the extraneous structure of metric spaces and studying objects with only open sets is a cleaner and more elegant approach.

Recall that in a metric space \\(X\\), the space \\(X\\) is open, the empty set \\(\emptyset\\) is open, the union of open sets remains open, and the intersection of finitely many open sets also remains open. We require open sets in a topology to follow these same rules.

**Def. (Topological space)** A *topological space* is any space \\(X\\) together with a collection \\(\mathcal{T}\\) (called the *topology*) of subsets of \\(X\\) (called the *open sets*) that satisfy the following properties.
1. The union of arbitrarily many open sets is open. That is, if \\(\\{U\_{\alpha}\\}\_{\alpha \in A} \subset \mathcal{T}\\), then \\(\bigcap_{\alpha \in A}U_{\alpha} \in \mathcal{T}\\).
2. The intersection of finitely many open sets is open. That is, if \\(U_1, \cdots, U_n \subset \mathcal{T}\\), then \\(U_1, \cdots, U_n \in \mathcal{T}\\).
3. The emptyset is open, and the entire space is open. That is, \\(\emptyset, X \in \mathcal{T}\\).

Below are some examples of topological spaces.

**Discrete Topology.** Given any set \\(X\\), let the topology \\(\mathcal{T}\\) be the power set \\(\mathcal{P}(X)\\). This is called the *discrete topology* on \\(X\\).

**Trivial Topology.** Give any set \\(X\\), define the topology by \\(\mathcal{T} = \\{\emptyset, X\\}\\).

**Metric Topology.** Let \\((X,d)\\) be a metric space. Then let \\(\mathcal{T}\\) be the collection of all open sets in the metric space.

**Exercise.** Check that each of the spaces above is indeed a topological space. That is, ensure the topology \\(\mathcal{T}\\) satisfies properties (1), (2), and (3) above.

**Exercise.** Given a set \\(X\\), find a metric \\(d\\) on \\(X\\) so that the metric topology on \\(X\\) is the discrete topology.

Next, motivated by our discussion in the first paragraph, we can define what it means for a function between topological spaces to be continuous.

**Def. (Continuous function).** Let \\(f: X \to Y\\) be a map between two topological spaces. Then \\(f\\) is *continuous* if for every open subset \\(U\\) of \\(Y\\), the set \\(f^{-1}(U)\\) is an open subset of \\(X\\).

<!-- optional -->
Properties (1), (2), and (3) above are essential for the notion of continuity in topoological spaces to be a meaningful generalization of continuity in metric spaces. Suppose we have a metric space \\(Y\\), a space \\(X\\) with "open sets" that do not satisfy (1), (2), and (3), and a function \\(f: X \to Y\\). Then because \\(Y\\), being a metric space, does satisfy properties (1), (2), and (3) above together with the definition of continuity and the following exercise, it would be difficult for any \\(f\\) to be a continuous function. Hence we require properties (1), (2), and (3).

**Exercise.** Show that if \\(f: X \to Y\\), then \\(f^{-1}(Y) = X\\) and \\(f^{-1}(\emptyset) = \emptyset\\). Additionally, given a collection of sets \\(A_{\alpha} \subset Y\\), show \\(f^{-1}(\bigcup_{\alpha}A_{\alpha}) = \bigcup_{\alpha}f^{-1}(A_{\alpha})\\) and \\(f^{-1}(\bigcap_{\alpha}A_{\alpha}) = \bigcap_{\alpha}f^{-1}(A_{\alpha})\\).
<!-- optional -->

Recall that in metric spaces we also have "closed sets", which are exactly complements of open sets. This allows us to easily define closed sets 

**Def. (Closed set).** In a topological space \\(X\\), a set \\(A \subset X\\) is closed if \\(X \smallsetminus A\\) is open.

Closed sets have many uses, including the following alternate way to test continuity.

**Theorem.** A function \\(f: X \to Y\\) between topological spaces is open if and only if for every closed set \\(A \subset Y\\), the set \\(f^{-1}(A)\\) is closed in \\(X\\).

*Proof.* If \\(f\\) is continuous and \\(A \subset Y\\) is closed, then \\(f^{-1}(A)^c = f^{-1}(A^c)\\) is open, so \\(f^{-1}(A)\\) is closed. Conversely, suppose \\(f^{-1}(A) \subset X\\) is closed whenever \\(A \subset Y\\) is closed. Then if \\(U \subset Y\\) is open, \\(f^{-1}(U)^c = f^{-1}(U^c)\\) is closed, so \\(f^{-1}(U)\\) is open. Thus \\(f\\) is continuous.