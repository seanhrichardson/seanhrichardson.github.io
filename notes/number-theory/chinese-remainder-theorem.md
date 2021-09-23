---
layout: page
section: NOTES
title: Chinese Remainder Theorem
---

## Chinese Remainder Theorem

#### Statement
Take coprime integers $m$ and $n$. Then, for any choice of integers $a$ abnd $b$, there exists an integer $c$ such that $c \equiv a \text{ mod } n$ and $c \equiv b \text{ mod } n$. Further, $c$ is unique mod $mn$.

#### Proof
By Bézout's identity, there exist integers $u$ and $v$ such that $um + vn = 1$. Then, $c = aum + bvn$ works. Indeed,
\\[c = bum + avn \equiv aum + avn = a(um + vn) \equiv a \text{ mod }m\\]
\\[c = bum + avn \equiv bum + bvn = b(um + vn) \equiv b \text{ mod }n\\]

$c$ remains a valid solution after reducing mod $mn$. Thus, we have a surjection $\mathbb{Z}_{mn} \mapsto \mathbb{Z}_m \times \mathbb{Z}_n$, and because these sets have the same number of elements, we conclude this is an injection, which gives the uniqueness claim.