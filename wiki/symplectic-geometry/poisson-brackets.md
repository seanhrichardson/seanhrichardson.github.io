---
layout: page
title: Poisson Brackets
---

# Poisson Brackets

Systems in physics often have conserved quantities such as energy, momentum, angular momentum, etc. In a *Hamiltonian system* \\((M, \omega, H)\\), we call \\(f \in C^{\infty}(M)\\) a ***conserved quantity*** if it is invariant under the Hamiltonian flow, meaning \\(X\_H f = 0\\) for \\(X\_H\\) the generator of the Hamiltonian flow. We can reformulate this condition by introducing the vector field \\(X\_f\\) over \\(M\\) characterized by \\(i\_{X\_f} \omega = df\\). Then, observe
\\[
    X\_H f = df(X\_H) = i\_{X\_f}\omega(X\_H) = \omega(X\_f, X\_H).
\\]
Therefore,
\\[
    f \text{ a conserved quantity} \iff \omega(X\_f, X\_H) = 0.
\\]
This characterization has a useful symmetry, which we formalize by introducing the ***Poisson bracket*** \\(\\{\cdot, \cdot\\}: C^{\infty}(M) \times C^{\infty}(M) \to \mathbb{R}\\) defined by
\\[
    \\{f, g\\} := \omega(X\_f, X\_g) = X\_g f.
\\]
The Poisson bracket also naturally appears in showing Hamiltonian vector fields are closed under the Lie bracket. This has important implications as the natural class of infinitesimal symmetries over a symplectic manifolds are the Hamiltonian vector fields, and the following lemma implies the Hamiltonian vector fields form a Lie algebra.

**Lemma.** Hamiltonian vector fields are closed under the Lie bracket. In particular, \\([X\_f, X\_g] = X\_\{\\{g, f\\}\}\\).

*Proof.* We prove \\(i\_{[X\_f, X\_g]}\omega = d\\{g, f\\}\\) by pairing both sides with a vector field \\(Y\\). Indeed, compute
\\[
\begin{align}
    (i\_{[X\_f, X\_g]} \omega)(Y)
    = \omega([X\_f, X\_g], Y)
    = \omega(\mathcal{L}\_{X\_f} X\_g, Y)
    = \mathcal{L}\_{X\_f} \omega(X\_g, Y) - \omega(X\_g, \mathcal{L}\_{X\_f}Y)
\end{align}
\\]
where the last follows from the product rule for the Lie derivative. Next, use the definition of \\(X\_g\\) to rewrite both terms above and continue this equality chain:
\\[
\begin{align}
    (i\_{[X\_f, X\_g]} \omega)(Y)
    &= X\_f dg(Y) - dg([X\_f, Y])
    = X\_f Yg - X\_f Yg + YX\_f g\\\\\
    &= Y dg(X\_f)
    = Y\omega(X\_g, X\_f)
    = d\\{g, f\\}(Y).
\end{align}
\\]
<div style="text-align: right"> \(\square\) </div>

Consequently, under the identification \\(f \mapsto X\_f\\) between a smooth function \\(f \in C^{\infty}(M)\\) and the corresponding Hamiltonian vector field, we find
\\[
    \\{g, f\\} \mapsto X\_{\\{g, f\\}} = [X\_f, X\_g].
\\]
This identification between the Poisson bracket and the Lie bracket implies the Poisson bracket is a Lie algebra.

**Corollary.** The Poisson bracket \\(\\{\cdot, \cdot\\}\\) forms a Lie algebra.

<!-- TODO: some proof explanation? -->

{% cite griffiths1999 %} testing

## References

{% bibliography --cited %}