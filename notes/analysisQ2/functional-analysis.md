---
layout: page
section: NOTES
title: Real Analysis
---
## Functional Analysis

#### Normed Vector Space (Folland 5.1)
Basic definitions: *linear space (i.e. vector space)*, *normed linear space*, *norm*, *semi-norm*, *equivalent norms*, *norm topology (i.e. strong topology)*, *Banach space*, *convergent series*, *absolutely convergent series*, *subspace*, *quotient space*, *linear map*, *bounded linear map*, *continuous linear map*, 

Other definitions: *Hamel basis*, *Scheuder basis*, *unconditional Scheuder basis*, *equicontinuous*, $l^1(\mathbb{N})$, $l^{\infty}(\mathbb{N})$.

Examples of Banach spaces: $L^1(\mu)$, $L^p(\mu)$, $C([0,1])$. Non-example: $C_c(\mathbb{R})$.

**Theorem 5.1.** A normed linear space $(X, \\|\cdot\\|)$ is complete iff every absolutely convergent series converges to an element in $X$.

*Proof (Folland pg. 152).* If $X$ is complete, then because the partial sums of some absolutely convergent series is Cauchy, the series converges. Conversely, suppose every absolutely convergent series converges. Consider Cauchy sequence $\\{x_n\\}$ and note it is sufficient to show a subsequence $\\{x_{n_k}\\}$ converges. Indeed, we can choose $n_k$ such that $m,n > n_k$ ensures $\\|x_n-x_m\\| < 2^{-k}$. Then, the series $(x_{n_1}) + (x_{n_2}-x_{n_1}) + (x_{n_3}-x_{n_2}) + \cdots$ is absolutely convergent, hence convergent, and is equivalent to the subsequence $x_{n_k}$.

**Lemma.** Every linear space has a Hamel basis.

*Proof.* TODO (HW)

**Thm (Arzelà–Ascoli).** $(X,\rho)$ compact metric space, and $\mathcal{F} \subset C(X)$ equicontinuous and pointwise bounded. Then, $\mathcal{F}$ is precompact.

*Proof.* TODO (supposedly a $3 \varepsilon$ and diagonal construction argument).

**Examples.**
1. $l^1(\mathbb{N})$ is a separable Banach space. *Has normed linear space structure, is complete by Riez-Fischer, is separable by considering the set of all sequences in $\mathbb{Q}$ with only finitely many nonzero terms*.
1. $l^{\infty}(\mathbb{N})$ is non separable. *TODO: diagonal construction*.