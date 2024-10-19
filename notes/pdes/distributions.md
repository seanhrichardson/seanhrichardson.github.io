---
layout: page
title: Distributions
---

## Distributions

#### Motivation
/\*todo later when I understand applications better ... maybe use weak limits of \\(C^{\infty}\\) functions like in Stein and Shakarchi 103?\*/

/\*Maybe use some algebraic axioms and that \\(\delta\\) is the identity and so must be in there?\*/

/\*Similar ideas to Radon measures and Riesz representation, but has extra smooth structure?\*/

/\*Key: approximate solutions to PDES... distributions give completeness?\*

/\*Last footnote of: https://math.stackexchange.com/questions/3250241/why-are-sobolev-spaces-useful\*/

/\*Practically: want \\(D'\\) to be a large space and will later use things like \\(H^s\\) for PDEs...\*/

#### Test Functions
/\*Mention \\(X\\) is an open subset of \\(\mathbb{R}^n\\) somewhere\*/

/\*needs motivation... something about how this topology distinguishes between all derivatives, which should be necessary for distributions\*/

Consider the vector space \\(C^{\infty}_c(X)\\) with topology defined by \\(\varphi_n \to \varphi\\) when \\(\partial^{\alpha} \varphi_n \to \partial^{\alpha} \varphi\\) uniformly for all multi-indexes \\(\alpha\\).

#### Definition
The space \\(\mathcal{D}'(X)\\) of distributions on \\(X\\) is the space of all continuous linear functionals \\(C^{\infty}_c(X) \to \mathbb{C}\\).

Topology given by \\(u_n \to u\\) if and only if \\(u_n(\varphi) \to u(\varphi)\\) for all test functions \\(\varphi\\). /\*probably want this property... maybe use it in the motivation somehow?\*/

#### Examples

**Locally Integrable Functions.**
A function \\(f \in L^1_{\operatorname{loc}}(X)\\) defines a linear map \\(f^\*: C_c^{\infty} \to \mathbb{C}\\) by
\\[
    f^\*(\varphi) = \int f \varphi.
\\]
To check \\(f^*\\) is continuous, it suffices to check that if \\(\varphi_n \to 0\\) in \\(C_c^{\infty}(X)\\), then \\(f^\*(\varphi_n) \to 0\\). Indeed, if \\(\varphi_n \to 0\\) in \\(C_c^{\infty}(X)\\), then in particular, \\(\varphi_n \to 0\\) uniformly. Thus \\(f^\*(\varphi_n) = \int f \varphi_n \to 0\\).

**Dirac Delta Function.**
Given \\(y \in X\\), define the linear map \\(\delta_y: C_c^{\infty}(X) \to \mathbb{C}\\) by
\\[
    \delta_y(\varphi) = \varphi(y).
\\]
If \\(\varphi_n \to 0\\) in \\(C_c^{\infty}(X)\\), then \\(\varphi_n \to 0\\) uniformly, so \\(\delta_y(\varphi_n) = \varphi_n(y) \to 0\\). Thus \\(\delta_y\\) is continuous and so a distribution.

**Radon Measures.**
A Radon measure \\(\mu\\) on \\(X\\) defines a linear map \\(\delta_y: C_c^{\infty}(X) \to \mathbb{C}\\) by
\\[
    \mu^*(\varphi) = \int \varphi d\mu.
\\]
/\*TODO\*/