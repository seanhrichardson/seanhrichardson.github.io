---
layout: page
section: NOTES
title: Class Equation
---

## The Class Equation

#### Idea
Groups act on themselves by conjugation. The orbits of this group action partition the group, so the order of the group is the sum of the orders of the orbit. In particular, for a group $G$, there are $|Z(G)|$ trivial orbits of order $1$, then we count the sizes of the remaining bigger orbits.

#### Statement
Let $G$ be a finite group and let $g_1, g_2, \dots, g_r$ be the representatives of the conjugacy classes (orbits under conjugation) that are not in the center of $G$. Then,
\\[|G| = |Z(G)| + \sum_{i=1}^{r}|G:C_G(a)|\\]

#### Proof
As equivalence classes, conjugacy classes partition the group. We count the order of the group by iterating over the conjugacy classes and counting the number of elements in each class. Recall that the order of some element $a$ is given by $|G:G_a|$. In the case of conjugation, we have $G_a = C_G(a)$, so consider $|G:C_G(a)|$. Further, if an element $a$ is in the center, then $C_G(a) = G$, thus the conjugacy class of $a$ is of size $1 = |G:G|$. Summing the $Z(G)$ conjugacy classes of order $1$ and $|G:C_G(g_i)|$ for the remaining distinct conjugacy classes, each represented by some $g_i$, gives the class equation.