---
layout: page
section: NOTES
title: Group theory
---
## Group Theory

* "Right" definitions of group properties
* Lagrange's theorem
* Cayley's theorem
* Universal property for quotients
* First isomorphism theorem
* Second isomorphism theorem
* Third isomorphism theorem

**Class equation.**
If $G$ acts on $X$ and $X$ finite,
\\[|X| = \sum_{x \in \text{ orbit reps}} \[G: G_x\]\\]

*proof.*
Because the orbits partition the set, and $\|Gx\| = \[G: G_x\]$ we have
\\[|X| = \sum_{x \in \text{ orbit reps}}|Gx| = \sum_{x \in \text{ orbit reps}}\[G: G_x\]\\]

* Sylow theorems

**Theorem 1.** If a prime $p\mid\|G\|$, then there exists a $p$-Sylow subgroup $H < G$.

*proof.* Lemma: If $(m,p)=1$, then $(\binom{p^nm}{p^n}, p) = 1$.

Let $\|G\| = p^nm$ with $(m,p)=1$, let $\Omega = \{X \subset G \mid \|X\| = p^n\}$ be all subsets of order $p$, and consider the group action $G \times \Omega \to \Omega$ given by $(g,X) \mapsto gX$, yielding the corresponding class equation

\\[\|\Omega\| = \sum_{x\text{ orbit reps}} \|G: G_x\|\\]

Note $p \nmid \|\Omega\|$ by lemma, thus $p \nmid \|G:G_X\| = \frac{\|G\|}{\|G_X\|}$ for some $X$. But then by $p^n \mid \|G\|$ we must have $p^n \mid \|G_X\|$. Further for $x \in X$, $\|G_x \cdot x\| \leq \|X\| = p^n$, thus $\|G_x\| = p^n$.

**Theorem 2.**
- Any two $p$-Sylow subgroups of $G$ are conjugate.
- If $Q < G$ is a Sylow $p$-subgroup, and $p < G$ is any $p$-subgroup, then there exists $g \in G$ such that $gPg^{-1} \subset Q$.

**Theorem 3.** Let $N_p$ be the number of $p$-Sylow subgroups in $G$.
- $N_p \equiv 1$ (mod $p$)
- $N_p \mid \|G\|$
- $N_p = 1 \iff$ Any $p$-Sylow subgroup is normal

*proof.*

* Direct product construction
* Direct product recognition theorem
* Structure of finite abelian groups
* Semidirect product construction
* Semidirect product recognition
* Equivalent definitions of solvable group
* Equivalent definitions of nilpotent group
* Structure of finite nilpotent groups
* Zassenhaus lemma
* Schreier's theorem
* Jordan-Hölder theorem
* Free group construction
* Universal property for free groups
* Free product construction and universal property
* Amalgamates product construction and universal property
