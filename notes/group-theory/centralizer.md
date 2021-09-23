---
layout: page
section: NOTES
title: Centralizer
---

## Centralizer

#### Definition
Given a subset $A$ of a group $G$, the centralizer of $A$ in $G$ is the set of elements in $G$ that commute with all of $A$ and is denoted $C_G(A)$. That is,
\\[C_G(A) = \\{x \in G \mid xax^{-1} = a~~\forall a \in A\\}\\]

#### Verification the centralizer is a subgroup
We apply the subgroup criterion. Note that $1$ is in the centralizer, giving $C_G(A)$ is nonempty. Take $x,y \in C_G(A)$ and $a \in A$, noting that $yay^{-1} = a$ implies $y^{-1}ay = a$, we observe that $xy^{-1}$ is an element of the centralizer:
\\[(xy^{-1})a(xy^{-1})^{-1} = x(y^{-1}ay)x^{-1} = xax^{-1} = a\\]