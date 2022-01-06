---
layout: page
section: NOTES
title: Lagrange's Theorem
---

## Langrange's Theorem

#### Statement
The order of a subgroup divides the order of the larger group.

#### Proof
Let $H$ be a subgroup of group $G$; we examine the structure of cosets of $H$. In particular, assume two cosets $g_1H$ and $g_2H$ share any element, that is, $g_1h_1 = g_2h_2$ for some $g_1, g_2 \in G$ and $h_1, h_2 \in H$. Then any element of the first coset $g_1h$ can be expressed as $g_2(h_2h_1^{-1}h)$ and thus is an element of the second coset. Therefore, we can conclude that any two cosets either share no elements or are the same.

Further, every element $g \in G$ is certainly contained in the coset $gH$, thus $G$ must be partitioned into cosets -- all of which have the order of $H$.