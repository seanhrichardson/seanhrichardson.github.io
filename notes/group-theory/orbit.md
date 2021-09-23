---
layout: page
section: NOTES
title: Orbit
---

## Orbit

#### Definition
Take a group action $. : G \times A \to A$. Then, for any $a \in A$, the *orbit of $a$* is the equivalence class
$\\{g.a \mid g \in G\\}$

#### Theorem
The order of an equivalence class $[a]$ is $|G: G_a|$ where $G_a$ is the stabilizer of $a$ under the group action.

#### Proof
Consider the function between elements of $|[a]|$ and cosets of $G_a$ given by $g.a \mapsto gG_a$; we claim this is a bijection. Indeed, if $g_1G_a = g_2G_a$, then $g_1 = g_2s$ for $s \in G_a$. Thus, $g_1.a = (g_2s).a = g_2.(s.a) = g_2.a$, giving injectivity of the function. Next, take any coset $gG_a$; the function will map $g.a$ to this coset giving surjectivity.