---
layout: page
section: NOTES
title: Center
---

## Center of a Group

#### Definition
The center of a group $G$ is the set of elements that commute with all of $G$ and is denoted $Z(G)$. That is, 
\\[Z(G) = \\{x \in G \mid xgx^{-1} = g~~\forall g \in G\\}\\]

#### Verification the center is a subgroup
We apply the subgroup criterion to $Z(G)$. First, note that the idenity $1$ commutes with all elements, thus $Z(G)$ is nonempty. Next, take two elements of the center $x$ and $y$. Then, for any element $g \in G$ we have
\\[(xy^{-1})g = x(g^{-1}y)^{-1} = x(yg^{-1})^{-1} = xgy^{-1} = g(xy^{-1})\\]
and so $xy^{-1}$ commutes with all elements of $G$, completing the subgroup criterion.