---
layout: page
section: NOTES
title: The Subgroup Criterion
---

## The Subgroup Criterion

#### Statement
Let $H$ be a subset of a group $G$. Then, $H$ is a subgroup of $G$ if and only if
* $H$ is nonempty.
* For any two elements $x, y \in H$, $xy^{-1} \in H$.

#### Proof
Assume a subset $H$ of group $G$ satisfies the subset criterion. We take the group operation to be the same as $G$, which we already know is associative. Because $H$ has at least one element $x$, $H$ must contain the identity by $1 = xx^{-1}$. Thus, $H$ is closed under inversion, for if $x \in H$, then $x^{-1} = 1\cdot x^{-1}$ is in $H$. Finally, note that $H$ is indeed closed under the group operation, for if $x,y \in H$, then $y^{-1}$ in $H$, thus $xy = x(y^{-1})^{-1}$ is in $H$.

Conversely, if $H$ is a subgroup, then the first criterion follows by $1 \in H$ and the second follows by closure of inverses and the group operation. 