---
layout: page
title: Maxwell's Equations
---

<!-- todo... in order to do this properly, I need more special relativity and electrstatics background -->

# Maxwell's Equations

<!-- TODO... I MIGHT HAVE TO REWRITE THIS AND REARRANGE IDEAS... PERHAPS START WITH THE ELECTRIC FIELD E FROM THE PERSPECTIVE OF ONE PARTICLE, THEN GO FROM THERE USING BELOW IDEAS IN A DIFFERENT ORDER? -->

<!-- TODO... ALTERNATIVELY, FOLLOW ELECTROSTATICS REASONING? PERHAPS FIRST DEFINE FARADAY 2-TENSOR AS SOME SORT OF FORCE AS IN ELECTROSTATICS? -->


## Charge in Space-Time

<!-- TODO: I STILL DON'T TOTALLY UNDERSTAND WHEN I SHOULD THINK OF SPACE-TIME AS A MANIFOLD AND WHEN AS A VECTOR SPACE... I SHOULD ADJUST BELOW TO AGREE WITH WHATEVER IS CORRECT 
... I think for a lot of this we are considering R^{3+1} as a manifold, but with a flat Minkowski metric
-->

We observe ***charged particles***, each of which we model as a *world line* \\(\gamma: \mathbb{R} \to \mathbb{R}^{3+1}\\) in Minkowski space-time \\((\mathbb{R}^{3+1}, \eta)\\) together with an associated real number \\(q\\) called the ***charge***. This formulation follows from the experimental observation of ***invariance of charge***, which states that all observers measure the same value \\(q\\) of charge for each charged particle (this should not be taken for granted as mass, for example, does not enjoy the same invariance). Consequently, each observer will agree on the amount of charge \\(Q\\) crossing some hypersurface \\(\Sigma\\) in space-time. For example, if this hypersurface \\(\Sigma\\) is a space-like region, then \\(Q\\) is simply the amount of charge in the volume \\(\Sigma\\). On the other hand, if we have a decomposition \\(\Sigma = I \times A\\) into some time-like interval \\(I\\) and a space-like area \\(A\\), then \\(Q\\) represents the amount of charge that has crossed through \\(A\\) over this time interval.

<!-- TODO: BELOW TECHNICALLY BOUNCED BETWEEN DISCRETE PARTICLES AND CONTINUOUS 3-FORM, SO NEED TO CLARIFY AND CORRECT THIS... (perhaps want to integrate in a similar philosphy to what iva does) -->
Because every observer agrees on the quantity of charge \\(Q(\Sigma)\\) associated to each hypersurface \\(\Sigma\\) in space-time, we can define a \\(3\\)-form \\(J\\), called the ***four-current*** over \\(\mathbb{R}^{3+1}\\) by
\\[
    \int\_{\Sigma} J = Q(\Sigma).
\\]
We will assume the restriction of \\(J\\) to any spacelike hyperplane is compactly supported, which corresponds to a system in which each observer only sees charge in some finite region of space. Furthermore, as implictly assumed into our model of charged particles, we experimentally ***conservation of charge***, which states that a charged particle \\(\gamma(t)\\) exists for all time and its charge \\(q\\) does not change. Therefore, given a compact \\(\Omega\\) of spacetime, we must have
\\[
    \int_{\partial \Omega} J = 0
\\]
because the charge \\(q\\) associated to each charged particle must both enter and leave \\(\Omega\\). Therefore, by Stoke's theorem we conclude
\\[
    \int_{\Omega} dJ = \int_{\partial \Omega} J = 0 \quad \text{for all compact } \Omega \subset \mathbb{R}^{3+1} \implies dJ = 0.
\\]
<!-- TODO:  -->

/\*TODO: perhaps derive continuity equations here?\*/

## The Faraday 2-form

<!-- TODO: rephrase/redo this so it is correct... the point is there is a natural / "canonical" potential, which we call F -->

<!-- possibly useful: https://mathoverflow.net/questions/489272/weak-hodge-decomposition-of-compactly-supported-smooth-forms-on-non-compact-mani?noredirect=1&lq=1 -->

<!-- TODO: I need the input that any harmonic form that is compactly supported for any spacial hyperplane must be identically 0... this is some PDE input... perhaps assume this below, and study this separately later. -->

<!-- TODO: I could rephrase this so that I never refer to an original choice of G and use more abstract theory and isomorphisms? Possibly rephrase if it would significantly simplify. -->

We have the four-current \\(J\\), a closed 2-form that is compactly supported over space-like hypersurfaces. Thus by the *de Rham cohomology* of \\(\mathbb{R}^{3+1}\\), it is also exact and we can write \\(J = d G\\) for some \\(2\\)-form \\(G\\). This choice of potential \\(G\\) is not unique, but the Minkowski metric \\(\eta\\) provides a canonical choice of potential over spacetime \\(\mathbb{R}^{3+1}\\) (this is related to the *Hodge decomposition* over compactly supported manifolds from *Hodge theory*).

<!-- TODO: need to make some of the terms below more precise... -->
**Theorem.** Given a closed \\(3\\)-form \\(J\\) over Minkowski space-time that is compactly supported over every space-like hypersurface, there exists a unique \\(2\\)-form \\(F\\) called the ***Faraday 2-form*** that vanishes at spacial infinity and satisfies ***Maxwell's equations***
\\[
    \begin{cases}
        d\star F = J\\\\\
        dF = 0.
    \end{cases}
\\] 

/\*TODO: name these laws\*/

/\*TODO: derive the other two and conclude that \\(E\\) must be the electric field from electrostatics\*/

<!-- Perhaps first do and understand Hodge decomposition before completing this proof -->
*Proof.* /\*TODO... this is a PDE result...\*/

<div style="text-align: right"> \(\square\) </div>

The relation \\(d \star F = J\\) is called the ***Gauss–Ampère law*** and  \\(dF = 0\\) is called the ***Gauss–Faraday*** law. Furthermore, because *de Rham cohomology* implies closed forms are exact over \\(\mathbb{R}^{3+1}\\), we can write \\(F = dA\\) for an ***electromagnetic four-potential*** \\(A\\) (which is not uniquely defined).

## Charge and Current Density

<!-- TODO: I STILL DON'T TOTALLY UNDERSTAND WHEN I SHOULD THINK OF SPACE-TIME AS A MANIFOLD AND WHEN AS A VECTOR SPACE... I SHOULD ADJUST BELOW TO AGREE WITH WHATEVER IS CORRECT -->

Consider an observer \\((p, \partial\_t)\\) in space-time, which induces a splitting of the tangent space \\(T\_p \mathbb{R}^{3+1}\\) into a time and space component \\(\mathbb{R} \oplus \mathbb{R}^{3}\\). Let \\(dt\\) and \\(\operatorname{vol}\_{\mathbb{R}^3}\\) be the induced volume forms for time \\(\mathbb{R}\\) and space \\(\mathbb{R}^3\\) respectively. Thus we get the splitting of the four-current \\(3\\)-form into
\\[
    J = \rho - j \wedge dt
\\]
Then over a region \\(V \subset \mathbb{R}^3\\) of the observers space, they measure the charge \\(Q\\) over \\(V\\) to be
\\[
    Q = \int_{V} J = \int_V \rho = \int_V \rho(x) d\operatorname{vol}\_{\mathbb{R}^3}.
\\]
The observer calls this 3-form \\(\rho\\) the ***charge density***. 
<!-- todo: note this agrees with classical definition in electrostatics? -->
Similarly, over a surface \\(\Sigma = I \times A\\) such that \\(I\\) agrees with the observers time direction and \\(A\\) agrees with space, we find the charge \\(Q\\) that passes through \\(A\\) in the time interval \\(I\\) is
\\[
    Q = \int_{I \times A} J = \int_I \int_A j \wedge dt = \int_I dt \int_A j = |I| \int_A j.
\\]
<!-- note: below is \beta ism in Lee's notation -->
<!-- TODO: note this agrees with classical definition in electrostatics -->
The observer calls this \\(2\\)-form \\(j\\) the ***current density***.
<!-- TODO: note continuity equation here? -->

## Electric and Magnetic Fields

Next, note the Faraday tensor splits with respect to an observer \\((p, \partial\_t)\\) as
\\[
    F = E \wedge dt + B
\\]
for some \\(1\\)-form \\(E\\), which is called the ***electric field*** and a \\(2\\)-form \\(B\\) called the ***magnetic field***. Next, note the observer \\(\partial_t\\) induces a splitting \\(\eta = -dt^2 + g\\) of the metric into a metric \\(dt^2\\) on the observer's time and a metric \\(g\\) on the observer's space. Let \\(\ast\\) denote the Hoge star operator on the observers space \\(\mathbb{R}^3\\) induced by \\(g\\). Then compute
<!-- TODO: elaborate on below computation (signs are tricky here, so this should be done carefully... there could be sign errors below) -->
\\[
    \star F = \star(E \wedge dt) + \star B
    = \ast E - \ast B \wedge dt.
\\]
Next, let \\(\mathbf{d}\\) denote the exterior derivative over the observers space \\(\mathbb{R}^3\\) and compute
\\[
    d \star F = \mathbf{d} \ast E +  \partial\_t E \wedge dt - \mathbf{d} \ast B \wedge dt.
\\] 

Therefore, by \\(d \star F = J\\) we find
\\[
    \mathbf{d} \ast E +  (\partial\_t E - \mathbf{d} \ast B) \wedge dt = \star F = J = \rho - j \wedge dt,
\\]
and therefore we conclude the two relations
\\[
\begin{align}
\mathbf{d} \ast E &= \rho \\\\\
\mathbf{d} \ast B &= \partial\_t E + j.
\end{align}
\\]

/\*TODO: name these\*/

/\*TODO: derive the other two\*/

/\*TODO: conclude \\(E\\) satisfies PDE and boundary conditions uniquely defining classical electric field and therefore is the same\*/

## Lorentz Force Law

/\*TODO: derive the Lorentz force law from \\(\partial\_t F = E\\) is force per unit charge for each observer\*/

/\*TODO: this requires some special relativity and I think a translation between the observers time and proper time\*/


<!-- TODO: derive relationship between electric field and charge density so we know what electric field is... -->

<!-- TODO: input some electrostatics -->

## References

<span style="display:none">
{% cite purcell-morin %}
{% cite 1912-page %}
{% cite 2013-sattinger %}
</span>

<!-- https://mathoverflow.net/questions/132879/hodge-decomposition-in-minkowski-space -->

{% bibliography --cited %}

/\*TODO: cite Hehl-Obukhov book and their expository paper\*/