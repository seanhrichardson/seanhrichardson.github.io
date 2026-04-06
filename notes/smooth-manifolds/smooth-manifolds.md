---
layout: page
title: Smooth Manifolds
section: NOTES
---

# Smooth Manifolds

Manifolds are subsets of some Euclidean space \\(\mathbb{R}^m\\) that locally "looks like" some \\(\mathbb{R}^n\\). For topological manifolds, which only have information about the topology, the formal notion of "looks like" is given by homeomorphisms. We would like to define "smooth manifolds" so that we may do calculus over these manifolds in the same way we do calculus overs \\(\mathbb{R}^n\\), so we instead use the notion of "diffeomorphism" to preserve this calculus structure of \\(\mathbb{R}^n\\). 

<!-- some examples for MC -->

/\*TODO: define diffeomorphism\*/

Consider some topological \\(n\\)-manifold \\(M\\) and a topological embedding \\(\iota: M \to \mathbb{R}^m\\). We are interested in the following question: when can one do calculus on the surface of \\(M\\) in the same way we can for \\(\mathbb{R}^n\\)? For example, given a curve \\(\gamma: \mathbb{R} \to M \subset \mathbb{R}^m\\) and a smooth function \\(f: \mathbb{R}^m \to \mathbb{R}\\), we would like to compute the derivative 
\\[
    \frac{d }{d t}(f \circ \gamma)(t) = \sum_i \frac{\partial f}{\partial x^i} \frac{d x^i}{d t} = Df \cdot \gamma'(t).
    \tag{\\(\star\\)}
    \label{eq:chain-rule}
\\]
However, note computing such a derivative requires \\(\gamma'(t)\\) to exist and computing higher derivatives requires \\(\gamma(t)\\) to be smooth (that is, all derivatives should exist). Note that a surface such as a cone with a "sharp point" will not have as many smooth curves as usual in \\(\mathbb{R}^n\\): a curve passing through the sharp point can only be smooth if it slows down to \\(0\\) velocity while passing though this point, which makes it impossible to "do calculus" in that we cannot compute any derivative of a function at this point as in \eqref{eq:chain-rule}. The issue is that this sharp point does not "look like" \\(\mathbb{R}^n\\) in the sense of preserving derivatives.

<!-- TODO: ideally, I would like to find some logic that allows for *constructing* slice charts that avoids Boman's theorem (although one way using Boman's is by considering a Frolicher space structure) -->
