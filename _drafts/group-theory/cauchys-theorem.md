---
layout: page
section: NOTES
title: Cauchy's Theorem
---

## Cauchy's Theorem

#### Statement
Let $G$ be a group and let $p$ be a prime that divides the order of $G$. Then there exists an element $g \in G$ of order $p$.

#### Proof
(Following the proof in *Abstract Algebra* by Dummit and Foote. Section 3.2 excercise 9)

Define the set 
\\[S = \\{(x_1, x_2, \dots, x_p) \mid \prod x_i = 1\\}\\]
and let $(x_1, \dots, x_p) \sim (y_1, \dots, y_p)$ denote that the first tuple is a cyclic permutation of the second. Note that a $S$ is closed under cyclic permutations and that $\sim$ defines an equivalence relation on $S$. Note that the equivalence class of $(x_1, x_2, \dots, x_p)$ is equivalent to the orbit under the group action $C_p \times S \to S$ defined by 
\\[\sigma^k.(x_1, x_2, \dots, x_p) = (x_{\sigma^k(1)}, x_{\sigma^k(2)}, \dots, x_{\sigma^k(p)})\\]
Let $H \leq C_p$ be the stabilizer of the group action, which must be of order $1$ or $p$. Because the orbit is of magnitude $|C_p: H|$, each orbit is of order $1$ or $p$. Note that an orbit is of order $1$ exactly when the element is of the form $(x,x,\dots,x)$. 

Note that $S$ has $\|G\|^{p-1}$ elements and so we find $\|G\|^{p-1} = k+pd$ where $k$ is the number of size $1$ classes and $k$ is the number of size $p$ classes. Note that $p$ must divide $k$ and by $(1,1,\dots,1)$ a class of size $1$, there must also be some nontrivial class $\\{(x,x,\dots,x)\\}$ of size one, promising $x^{p}=1$ as desired.