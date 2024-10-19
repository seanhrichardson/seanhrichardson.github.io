---
layout: page
title: Forms
---

## Forms

#### The Trouble with Integrating Functions

Given some manifold $M$, let's try to define the integral of a function $\int_U f$ over some region $A \subset M$. We could try taking a map $\varphi$ to coordinates $(x^i)$ and define
\\[
    \int_{A} f = \int_{\varphi(A)} f dx^1\cdots dx^n
\\]
However, this answer will depend on the coordinate chart. For example, if $f \equiv 1$, then this definition simply returns the volume of $\varphi(A) \subset \mathbb{R}^n$, which certainly depends on the chart.

The problem is that we have no notion of lengths, areas, or volumes on the manifold $M$, so it doesn't make sense to integrate function. Our goal is to find something that does make sense to integrate.

#### Integrating Covector Fields

In the case of integrating over a smooth curve over a manifold $M$, we are actually already familiar with the right objects to integrate: covector fields!

Given a covector field $\omega$ over the manifold $M$, we can take a parametrization $\gamma(t)$ with $a \leq t \leq b$ of the curve and define
\\[
    \int_{\operatorname{Im}(\gamma)} \omega = \int_{a}^b \omega(\partial_t) dt.
\\]
A valid concern is that this might depend on the parametrization. To check that this definition is indeed well-defined, take another parametrization, which we can write as $(\gamma \circ G)(s)$ with $c \leq s \leq d$ for some diffeomorphism $G: [c,d] \to [a,b]$. Then compute /\*using change of variables formula\*/ /\*$G$ technically needs to preserve orientation\*/
\\[
    \int_{c}^d \omega((\gamma \circ G)'(s))ds 
    = \int_{c}^d \omega(DG \circ \gamma'(G(s)))ds
    = \int_{c}^d \omega(\gamma'(G(s)))\det(DG)ds
    = \int_{a}^b \omega(\gamma'(t))dt
\\]
where crucially we have $\omega(DG \circ \gamma'(G(s))) = \omega(\gamma'(G(s)))\det(DG)$ because in this one-dimensional case, the map $DG$ is simply multiplication by $\det(DG)$.

In fact, the crucial property here that covectors have is that given some linear transformation on tangent vectors $T: \mathbb{R} \to \mathbb{R}$, we have $\omega(Tv) = \det(T)\omega(v)$. This allows us to interpret the evaluation $\omega(v)$ as the "weighted length" of the vector $v$, for the length of the stretched vector $\omega(Tv)$ is precisely the stretch factor times the length of the original vector $\det(T)\omega(v)$. Then, once we have a notion of length of the tangent vectors at each point, we can construct a notion of length of curves by integrating as above.

/\*note this is signed length\*/

<!-- That is, if we apply some transformation $T$ to a vector $v$, we get some stretched vector $Tv$.  -->

<!-- Luckily, the evaluation $\omega(Tv)$ streteches by precisely this stretch factor $\det(T)$, which allows us to get the same result regardless of how we parametrize. This property $\omega(Tv) = \det(T)\omega(v)$ demonstrates that covectors factor in the length of a vector. -->

#### Wedge Product Property

Taking inspiration from integrating covector fields, in order to define a notion of area or volume on the manifold, we should start by defining a notion of area or volume for vectors. In particular, given tangent vectors $v_1, \cdots, v_d$, we want a $d$-tensor $\omega$ such that $\omega(v_1, \cdots, v_d)$ can be interpreted as the volume of the parallelotope spaned by $v_1, \cdots, v_d$. However, if we stretch all these vectors by a linear transformation $T$, we need the volume of the stretched parallelotope $\omega(Tv_1, \cdots, Tv_d)$ to be the product $\det(T)\omega(v_1, \cdots, v_d)$ of the stretch factor of this transformation with the original volume. This is not the case for all tensors $\omega$, but those vectors that satisfy this make up an important subspace.

/\*visual of stretching? Perhaps allow user to mess with etries of $T$ and see parallelotope get stretched?\*/

/\*specift covariant covectors where appropriate\*/

<!---
#### Trying to Integrate over Higher Dimensional Surfaces

We could integrate over covector fields because they measure tangent vectors and provide some sense of length. If we attempt to integrate over some $d$-dimensional subspace of a manifold, we want something that measures $d$ seperate vectors and so we consider a $d$-tensor field.

Let's try to extend the definition for covector fields to tensor fields and see what properties this tensor field must satisfy for our definition to be well-defined.

Given a $d$-tensor field $\omega$ over a manifold $M$, let $P(t_1, \cdots, t_d)$ be some parametrization of a $d$-dimensional region $R \subset M$ where $(t^1, \cdots, t^d) \in D$. Then, we can try to define
\\[
    \int_R \omega = \int_{D} \omega(\partial_{t^1}P(t^1, \cdots, t^n), \cdots, \partial_{t^n}P(t^1, \cdots, t^n))dt^1\cdots dt^n.
\\]
Let's see when this is well-defined. Consider another parametrization and write it as $P \circ G$ for diffeomorphism $G: B \to A$. If this is definition is well-defined, we must have
\\[
    .
\\] -->