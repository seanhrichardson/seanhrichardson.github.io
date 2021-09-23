---
layout: page
section: NOTES
title: Bézout's Identity
---

## Bézout's Identity

#### Theorem (Bézout's Identity)
Take integers $a$ and $b$. Then, there exists integers $x$ and $y$ such that $ax + by = \gcd(a,b)$.

#### Proof
The construction of such integers $x$ and $y$ is given by the Euclidean algorithm. Indeed, apply the Euclidean algorithm to $a$ and $b$

\\[\\begin{align}
a &= q_1b + r_1 \\\\ b &= q_2r_1 + r_2 \\\\ r_1 &= q_3r_2 + r_3 \\\\ &\vdots \\\\ r_{n-2} &= q_n r_{n-1} + r_{n} \\\\ r_{n-1} &= q_{n+1}r_{n} \\end{align}\\]

Recall $r_n = \gcd(a,b)$ and we can rewrite $r_n = r_{n-2} + (-q_n)r_{n-1}$. Further, assume have $r_n$ a linear combination of $r_{k}$ and $r_{k+1}$, that is, $r_n = r_{k}x + r_{k+1}y$. Then, using $r_{k-1} = q_k r_k + r_{k+1}$ to isolating $r_{k+1}$ and substitute, we find $r_n = r_{k-1}y + r_{k}(x-q_ky)$ and thus $r_n$ would then be a linear combination of $r_{k-1}$ and $r_{k}$. Thus by induction we can conclude $r_n$ is a linear combination of $a$ and $b$.