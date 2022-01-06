---
layout: page
section: NOTES
title: Continuity
---

## Continuity

#### Epsilon-Delta Definition
Let $f$ be a real valued function. Given an input $x \in \mathbb{R}$, we say $f$ is continuous at $x$ if for any $\varepsilon > 0$ there exists $\delta > 0$ such that $|x-y| < \delta$ implies $|f(x)-f(y)| < \varepsilon$. We say $f$ is continuous if $f$ is continuous at all input points.

#### Convergent Sequence Definition
Let $f$ be a real valued function. Given an input $x \in \mathbb{R}$, we say $f$ is continuous at $x$ if for every sequence of inputs that converges to $x$, the corresponding sequence of outputs converges to $f(x)$.

#### Open Set Definition
Let $f$ be a real-valued function. We say $f$ is continuous if every open set in the output space has an open pre-image.

#### Closed Set Definition
Let $f$ be a real-valued function. We say $f$ is continuous if every closed set in the output space has a closed pre-image.

#### Equivalence of Definitions
First assume some function $f$ fulfills the $\varepsilon$-$\delta$ definition of continuity; I will shown $f$ fulfills the sequence definition. Fix an input $x$, consider some sequence $\{x_k\}$ that converges to $x$, and take $\varepsilon > 0$. By the $\varepsilon$-$\delta$ definition, there exists a $\delta$ such that $|x-y| < \delta$ implies $|f(x)-f(y)| < \epsilon$. Further, by the definition of convergence, there must exist some $N$ such that $i > N$ implies $|x - x_i| < \delta$. Thus $i > N$ additionally implies $|f(x) - f(x_i)| < \varepsilon$, thus $\{f(x_k)\}$ indeed converges to $f(x)$.

Next, assume some function $f$ fulfills the sequence definition; I wil show $f$ fulfills the closed set definition. Take any closed set $\overline{U}$ in the output and consider its preimage $f^{-1}(\overline{U})$. Then, let $\{x_k\}$ be a contained within $f^{-1}(\overline{U})$ that converges to some $x$. we hope to show $f^{-1}(\overline{U})$ contains the limit point $x$. Indeed, by assumption $\{f(x_k)\}$ must converge to $f(x)$ and by $\overline{U}$ closed, $f(x)$ is contained in $\overline{U}$. Thus, $x$ must be contained in the preimage.

Note that because the complement of a preimage is the preimage of the complement, if a function fulfills the open set definition, it must fulfill the closed set definition.

Finally, assume some function $f$ fulfills the open set definition. Fix an input $x$ and let $\varepsilon > 0$. Consider the open ball $B_{\varepsilon}(f(x))$ of radius $\varepsilon$ about $f(x)$. This ball's preimage $U$ must therefore be open. Note $x \in U$, and by definition of open set, there must be an open ball of some radius $\delta$ about $x$ contained in $U$, which we denote $B_{\delta}(x) \subset U$. Then, for any $y$ with $\|y-x\| < \delta$, we have $y \in U$ and thus $f(y) \in B_{\varepsilon}(f(x))$, or in other words, $\|f(y)-f(x)\| < \varepsilon$.