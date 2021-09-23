---
layout: page
section: NOTES
title: Normalizer
---

## Normalizer

#### Definition
For a subset $A$ of a group $G$, the normalizer of $A$ in $G$ is the set $N_A(G)$ of elements in $G$ that would allow for $A$ to be normal in $N_A(G)$. That is,
\\[N_A(G) = \\{x \in G | xax^{-1} \in A~~\forall a \in A\\}\\]

#### Verification the normalizer is a subgroup
We apply the subgroup criterion. First, note that the identity is in the normalizer, ensuring the normalizer is nonempty. 

Next, take $x, y \in N_A(G)$. Note that the mapping $A \rightarrow A$ given by $a \mapsto yay^{-1}$ is a bijection. Thus, if for all $a \in A$ we have $yay^{-1} \in A$ then the inverse of the bijection promises $y^{-1}ay \in A$ for all $a \in A$. So for any given $a \in A$, we have $(xy^{-1})a(xy^{-1})^{-1} = x(y^{-1}ay)x^{-1} = xa'x^{-1}$ for some $a' \in A$, giving $xa'x^{-1} \in A$   and so $(xy^{-1})a(xy^{-1})^{-1} \in A$.