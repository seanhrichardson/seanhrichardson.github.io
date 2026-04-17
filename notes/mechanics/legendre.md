---
layout: page
title: Legendre Transform
---

# Legendre Transfrom

Recall an inner product \\(\langle \cdot , \cdot\rangle\\) on a vector space \\(V\\) induces a natural isomorphism \\(\flat: V \to V^{\*}\\) by
\\[
    v^{\flat}(w) = \langle v , w\rangle.
\\]
An equivalent way of formulating this isomorphism uses the energy function \\(L: V \to \mathbb{R}\\) defined by
\\[
    L(v) = \frac{1}{2}\langle v , v\rangle.
\\]
Then, we can consider the isomorphism \\(\mathbb{F}L: V \to V^\*\\) induced from this function by
\\[
    \mathbb{F}L(v): w 
    \mapsto \left.\frac{d }{d t}\right\|\_{t=0} L(v+tw).
    \tag{\\(\star\\)}
    \label{eq:legendre}
\\]
Indeed, this is exactly equivalent to \\(\flat: V \to V^{\*}\\) 
\\[
    \left.\frac{d }{d t}\right\|\_{t=0} L(v+tw)
    = \left.\frac{d }{d t}\right\|\_{t=0} \frac{1}{2}\langle v + tw, v + tw\rangle
    = \langle v , w\rangle.
\\]
Sometimes (in particular in Lagrangian mechanics), the more natural object might be some energy function \\(L: V \to \mathbb{R}\\) rather than an inner product. In this case, we define the ***Legendre transform*** \\(\mathbb{F}L: V \to V^\*\\) by \eqref{eq:legendre}.


<!-- TODO: address conditions for hyperregular, etc... -->

<!-- TODO: also address involutivity and derive "Hamiltonian" -->

<!-- TODO: also in coordinates? -->

<!-- TODO: address generalization to bundles? -->