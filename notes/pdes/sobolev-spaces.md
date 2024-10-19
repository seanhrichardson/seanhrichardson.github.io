---
layout: page
title: Sobolev Spaces
---

## Sobolev Spaces

#### Motivation

Consider a differential operator \\(P\\) of order \\(k\\) on \\(\mathbb{R}^n\\). To make use of the tools of functional analysis, we can consider \\(P\\) to be a bounded linear operator between Banach spaces \\(P: C^k(\mathbb{R}^n) \to C^0(\mathbb{R}^n)\\) or perhaps as a continuous linear operator \\(P: C^{\infty}(\mathbb{R}^n) \to C^{\infty}(\mathbb{R}^n)\\). However, none of these spaces are Hilbert spaces, which limits the available tools from functional analysis. 

The "Sobolev space" \\(H^k(\mathbb{R}^n)\\) is the space designed such that we can take our codomain be the Hilbert space \\(L^2(\mathbb{R}^n)\\); that is, we will consider \\(P\\) as a bounded operator \\(P: H^k(\mathbb{R}^n) \to L^2(\mathbb{R}^n)\\). The space \\(H^k(\mathbb{R}^n)\\) we are seeking is the largest space such that applying any differential operator \\(Q\\) of order \\(k\\) to an element \\(u \in H^k(\mathbb{R}^n)\\) results in \\(Qu \in L^2(\mathbb{R}^n)\\). This will be the space of all distributions \\(u \in D'(\mathbb{R}^n)\\) such that \\(\partial^{\alpha}u \in L^2(\mathbb{R}^n)\\) for \\(\|\alpha\| \leq k\\). We formally define \\(H^k(\mathbb{R}^n)\\) below and we will even see that \\(H^k(\mathbb{R}^n)\\) itself can be made into a Sobolev space, which will allow us to consider \\(P\\) as the bounded map between Sobolev spaces -- the best scenario we could ask for.

**Def (Sobolev Space \\(H^k\\)).** Given \\(k \in \mathbb{Z}\\), the *Sobolev space of order \\(k\\) over \\(\mathbb{R}^n\\)*, denoted \\(H^k(\mathbb{R}^n)\\), is the subspace of distributions
\\[
    H^k(\mathbb{R}^n) := \\{u \in D'(\mathbb{R}^n) : \partial^{\alpha}u \in L^2(\mathbb{R}^n) \text{ for } \|\alpha\| \leq k\\}.
\\]

