---
layout: page
title: Pullback of Distribution by Diffeomorphism
---

## Pullback of Distribution by Diffeomorphism

/\*motivation\*/

Consider a diffeomorphism \\(f: U \to V\\) between open subsets \\(U, V \subset \mathbb{R}^n\\). Given a smooth function \\(u \in C^{\infty}(V)\\), recall the *pullback of \\(u\\) by \\(f\\)* is the map \\(f^\*u := u \circ f \in C^{\infty}(U)\\). We would like to extend this notion of pullback to distributions. Indeed, let's examine how the pullback \\(f^\*u\\) of a smooth function acts on a test function \\(\phi \in C_c^{\infty}(U)\\). Compute, making the change of variables \\(y = f(x)\\) the relation
\\[
    \langle f^*u , \phi\rangle 
    = \int\_U (u \circ f)(x) \phi(x) dx 
    = \int\_V u(y) \phi(f^{-1}(y)) \det Df^{-1} dy
    = \langle u , \phi \circ f^{-1} \det Df^{-1}\rangle.
\\]

This expression provides a way for us to extend the notion of pullback to distributions.

**Def.** Given a diffeomorphism \\(f: U \to V\\) between open subsets \\(U, V \subset \mathbb{R}^n\\) and a distribution \\(u \in D'(V)\\), define the *pullback of \\(u\\) by \\(f\\)* to be the distribution \\(f^\*u \in D'(V)\\) defined by
\\[
    \langle f^\*u , \phi\rangle = \langle u , \phi \circ f^{-1} \det Df^{-1}\rangle.
\\]
/\*todo: maybe absolute values in definition and computation\*/


/\*todo: verify continuity so that this is a distribution. todo: argue this is the unique continuous linear extension\*/

/\*References: mostly Friedlander ch. 11 and ch. 7. Perhaps also Hormander I ch. 8\*/

#### Wave Front Set

/\*todo: see my notes, but will have...\*/

\\[
    WF(f^\*u) = \\{(x, df\_x^T\eta): (f(x), \eta) \in WF(u)\\}
\\]