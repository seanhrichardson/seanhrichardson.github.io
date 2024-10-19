---
layout: page
title: Wave Front Set
---

## Wave Front Set

/\*TODO: be consistent between "rapidly decreasing" and "Schwartz function"... are these the same? Can you have rapidly decreasing distribution?\*/

Consider a continuous function \\(u \in C^0(\mathbb{R}^n)\\) that is smooth in some regions of \\(\mathbb{R}^n\\) but not smooth in others. We often want to characterize the region that \\(u\\) fails to be smooth /\*contextualize why\*/. We call this region the *singular support of \\(u\\)*, formally defined to be the smallest closed subset such that \\(u\\) is smooth its complement, and denoted \\(\operatorname{singsupp} u\\). The "wave front set" is a refinement of the notion of singular support, which encodes not just *where* \\(u\\) fails to be smooth, but also somehow identifies directions \\(u\\) fails to be smooth in. The idea of the wave front set stems from the following observation.

**Prop.** Given a distribution with compact support \\(u \in \mathcal{E}'(\mathbb{R}^n)\\), then \\(u \in C^{\infty}(\mathbb{R}^n)\\) if and only if its Fourier transform is a Schwartz function \\(\hat{u} \in \mathscr{S}(\mathbb{R}^n)\\).

*Proof.* If \\(u\\) is smooth, then \\(u\\) is a Schwartz function \\(u \in \mathscr{S}(\mathbb{R}^n)\\) because \\(u\\) has compact support. Thus \\(\hat{u} \in \mathscr{S}(\mathbb{R}^n)\\) because the Fourier transform takes Schwartz functions to Schwartz functions. Conversely suppose \\(\hat{u}\\) is rapidly decreasing. Then \\(\xi^{\alpha} \hat{u} \in L^2(\mathbb{R}^n)\\), so we can express the partial derivatives of \\(u\\) by
\\[
    \partial^{\alpha}u(x) = (2\pi)^{-n} \int\_{\mathbb{R}^n} e^{i\langle x , \xi\rangle} \xi^{\alpha} \hat{u}(\xi) d\xi.
\\]
Furthermore, the integrand is dominated by \\(\xi^{\alpha} \hat{u}(\xi)\\) for all \\(x\\), so by the dominated convergence theorem, \\(\partial^{\alpha}u(x)\\) is continuous for any \\(\alpha\\); in other words, \\(u\\) is smooth. 
<div style="text-align: right"> \(\square\) </div>

/\*maybe break up below more similar to Friedlander and introduce \\(\Sigma(u)\\) notation\*/

By the above proposition, \\(u\\) fails to be smooth because there is a particular direction in frequency space such that \\(\hat{u}\\) fails to be rapidly decreasing. It is more descriptive to identify these "problematic directions" in addition to the singular support. Indeed, the directions that are *not* problematic can be described by those \\(\xi \in \mathbb{R}^n\\) such that there exists a bump function \\(\psi \in C_c^{\infty}(\mathbb{R}^n \smallsetminus \\{0\\})\\) constant in each radial direction (i.e. \\(\psi\\) is homogenous of degree \\(0\\): \\(\psi(r\xi) = \psi(\xi)\\)) such that \\(\psi \hat{u}\\) is rapidly decreasing. Furthermore, each \\(x \in \operatorname{singsupp}u\\) generates its own problematic directions. We can distinguish between these problematic directions by first taking a bump function \\(\varphi\\) with small support and \\(\varphi(x) = 1\\), then identifying the problematic directions of \\(\varphi u\\). Combining these ideas, we can define the wave front set which identifies all the pairs \\((x,\xi)\\) such that \\(\xi\\) is a problematic direction corresponding to \\(x\\).

**Def (wave front set).** Given \\(u \in \mathcal{E}'(\mathbb{R}^n)\\) a distribution with compact support, we define the *wave front set* of \\(u\\), denoted \\(WF(u)\\), to be the following set (note the complement symbol).
\\[
    \begin{align}
    WF(u) = &\\{
        (x,\xi) : \text{there exists } \varphi \in C\_c(\mathbb{R}^n) \text{ with } \varphi(x) = 1 
         \text{ and } \psi \in C\_c^{\infty}(\mathbb{R}^n \smallsetminus \{0\}) \text{ where } \psi(x) = 1 \\\\\
         &\text{ and } \psi \text{ homogenous of degree } 0
         \text{ such that } \psi \widehat{\varphi u} \text{ is rapidly decreasing}
        \\}^c   .
    \end{align}
\\]

/\*TODO: Friedlander 11.1.2 / Hormander 8.1.1. Perhaps an exercise with solution?\*/

/\*TODO: formally verify projection is sungular support\*/

/\*mention somewhere that WF set makes it easier to argue function is smooth because we know what directions we need to fix. Particularly because of the nice relationships between wave front set and psi-dos.\*/