---
layout: page
title: Function Space Motivation
---

## Functional Analysis Motivation

#### PDE Motivation

A classical PDE with many applications is Poisson's equation \\(\Delta u = f\\) where \\(\Delta\\) is the Laplace operator
\\[
    \Delta: C^{\infty}(\mathbb{R}^n) \to C^{\infty}(\mathbb{R}^n).
\\]
A key observation is that \\(C^{\infty}(\mathbb{R}^n)\\) are vector spaces and \\(\Delta\\) is a linear map between these vector spaces. That is, for any \\(f,g \in C^{\infty}(\mathbb{R}^n)\\) and \\(\alpha, \beta \in \mathbb{R}\\) we have \\(\Delta(\alpha f + \beta g) = \alpha \Delta f + \beta \Delta g\\). This vector space framework provides important insight into the Laplace equation. In fact, PDEs of the form \\(Pu = f\\) for some linear operator \\(P: C^{\infty}(\mathbb{R}^n) \to C^{\infty}(\mathbb{R}^n)\\) appear frequently in nature and studying properties of the linear operator \\(P\\) allows us to learn properties of the PDE \\(Pu = f\\). For example:
* Surjectivity of the operator \\(P: C^{\infty}(\mathbb{R}^n) \to C^{\infty}(\mathbb{R}^n)\\) corresponds to the existence of a solution \\(Pu = f\\).
* Injectivity of the operator \\(P: C^{\infty}(\mathbb{R}^n) \to C^{\infty}(\mathbb{R}^n)\\) corresponds to the uniqueness of a solution \\(Pu = f\\).
* More generally, the range of \\(P\\) reveals when there exists a solution to \\(Pu = f\\) and the kernel of \\(P\\) tells us to what extend a solution is unique.

Functional analysis is simply the study of vector spaces and some particular class of linear maps between them. However, note that our vector spaces are not necessarily finite dimensional, which is the key distinction between functional analysis and linear algebra.

#### Historical Motivation

/\*TODO... (by rework I mean add more down here)\*/