---
layout: page
title: Measure Theory Motivation
---

## Why Study Measure Theory?

/\*TODO: brief summary of what measure theory is.\*/

#### A nicer notion of integration

The Riemann integral has some serious problems. For example, consider the following sequence of functions. Letting \\(\\{q\_k\\}\\) be an enumeration of all the rational numbers between \\(0\\) and \\(1\\), define
\\[
    f\_n(x) =
    \begin{cases}
        1 \quad \text{if} \quad x \in \\{q_k\\}_{k=1}^n\\\\\
        0 \quad \text{otherwise}.
    \end{cases}
\\]
Under Riemannian integration, we find \\(\int\_{0}^1 f\_n(x) dx = 0\\) for all \\(n\\). However, this sequence of functions converges to
\\[
    f(x) =
    \begin{cases}
        1 \quad \text{if} \quad x \in \mathbb{Q}\\\\\
        0 \quad \text{otherwise}.
    \end{cases}
\\]
Unfortunately, the function \\(f(x)\\) is not Riemann integrable; that is, \\(\int_0^1 f(x) dx\\) is undefined. However, \\(f(x)\\) is simply the \\(0\\) function with only the rational points moved, so "almost all" points remain unmoved and so it feels as though we should have \\(\int\_0^1 f(x) dx = 0\\). Lebesgue found a new way to define integration so that this is the case. The first step to defining such an integral is to develop a precise theory of defining the "mass" of subsets of \\(\mathbb{R}\\), then using this theory to define integration. For example, the subset \\(\mathbb{Q} \subset \mathbb{R}\\) of rationals leaves out "almost every" point in \\(\mathbb{R}\\) and so should have "\\(0\\) mass" and is therefore negligible, which will allow the statement \\(\int_0^1 f(x) dx = 0\\) to make sense. This theory that precisely quantifies the "mass" or "measure" if subsets of \\(\mathbb{R}\\) is the subject of *measure theory*.

In fact, Lebesgue's integration as defined by measure theory will make it so that in most reasonable situations we have
\\[
    \lim\_{n \to \infty} \int g\_n(x) dx = \int \lim\_{n \to \infty} g\_n(x) dx,
\\]
which will allow us to think of the space of Lebesgue-integrable functions as a *complete metric space*, which is extremely convenient when studying functions -- for example in the context of PDEs or Fourier analysis.

#### Fourier Series Motivation
/\*TODO: some sort of Fourier series motivation\*/

#### Probablility Theory

/\*TODO: a probability theory motivation for measure theory\*/