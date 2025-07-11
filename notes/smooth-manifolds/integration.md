---
layout: page
title: Forms
---

# Integration

## The Trouble with Integrating Functions

Given some manifold $M$, let's try to define the integral of a function $\int_U f$ over some chart $U \subset M$. A first (incorrect) attempt could be to take the chart \\(\varphi: U \to \mathbb{R}^k\\) to coordinates $(x^i)$ and define
\\[
    \int_{A} f = \int_{\varphi(A)} f dx^1\cdots dx^n
\\]
However, this answer will depend on the coordinate chart. For example, if $f \equiv 1$, then this definition simply returns the volume of $\varphi(A) \subset \mathbb{R}^n$, which certainly depends on the chart.

The problem is that we have no notion of lengths, areas, or volumes on a general smooth manifold $M$, so it doesn't make sense to integrate functions. Our goal is to find something that does make sense to integrate.

## Integrating covector Fields

In the case of integrating over a smooth 1-dimensional (sub)manifold \\(M\\), we are actually already familiar with the right objects to integrate: covector fields!

Given a covector field \\(\omega\\) over the manifold \\(M\\), suppose we have a coordinates \\(t\\) with chart \\(\varphi: \Sigma \to [a,b]\\) and define
\\[
    \int_{\Sigma} \omega := \int_{a}^b \omega(\partial_t) dt.
\\]
A valid concern is that this might depend on the choice of chart. To examine this, suppose we have alternate coordinates \\(s\\) with chart \\(\Psi: \Sigma \to [c,d]\\) and take the transition map \\(F := \varphi \circ \psi^{-1}.\\)
<!-- add commutative diagram? -->
Now use 
\\[
    \begin{align}
        \int\_c^d \omega(\partial\_s)ds
        &= \int\_c^d \omega(F'(s)\partial\_t)ds
        = \int\_c^d \omega(\partial\_t)F'(s)ds\\\\\
        &= \int\_{F(c)}^{F(d)}\omega(\partial\_t)dt
        = 
        \begin{cases}
            \int\_{a}^b \omega(\partial\_t)dt & \text{if \\(F\\) preserves orientation}\\\\\
            \int\_{a}^b \omega(\partial\_s)ds & \text{if \\(F\\) reverses orientation}.
        \end{cases}
    \end{align}
\\]
In this context, we say \\(F\\) *preserves orientation* if \\(F(c) = a\\) and \\(F(d) = b\\) and \\(F\\) *reverses orientation* if \\(F(c) = b\\) and \\(F(d) = a\\). This computation ensures the integral of a covector is well-defined up to orientation. Intuitively, this integral is weighted by the velocity \\(\partial\_t\\) of the parametrization, so while a faster parametrization integrates over a smaller domain, the integrand increases to compensate so the integral is independent of the parametrization.

## Integrating differential forms

More generally, the correct integrand for a \\(k\\)-dimensional smooth (sub)manifold \\(M\\) must increase proportionally with how quickly the parametrization covers area or volume. Specifically, recall that for a transition map \\(F: \mathbb{R}^k \to \mathbb{R}^k\\) between coordinates \\(F: (x^1, \cdots, x^k) \mapsto (y^1, \cdots, y^k)\\), integrals change like \\(dx^1 \cdots dx^k = \det DF \cdot dy^1 \cdots dy^k\\), so the correct object to integrate must scale like \\(\det\\) under a change of variables. Recall exterior forms satisfy such a transformation rule: given \\(k\\)-form \\(\omega \in \Lambda^k(V^*)\\) for \\(V\\) a \\(k\\)-dimensional vector space, we have \\((T^\* \omega)(v\_1, \cdots, v\_k) = \det T \cdot \omega(v\_1, \cdots, v\_k)\\) for \\(T: V \to V\\) linear.
 <!--cite the above  -->

Thus the correct object to integrate over \\(M\\) is an alternating covariant \\(k\\)-tensor field \\(\omega\\), which is called a *differential \\(k\\)-form* or just a *\\(k\\)-form*. Indeed, assume for now \\(M\\) is covered by one chart \\(\varphi: M \to \widetilde{U} \subset \mathbb{R}^k\\), which gives coordinates \\(x = (x^1, \cdots, x^k)\\). Then define
\\[
    \int\_M \omega := \int\_{\widetilde{U}} \omega(\partial\_{x^1}, \cdots, \partial\_{x^k})dx^1 \cdots dx^k
\\]
where the coordinate vector fields \\(\partial\_{x^i} := D\varphi^{-1}(\partial\_i)\\) are the pushforward of the standard basis \\(\partial\_i\\) on \\(\mathbb{R}^k\\). To see this is well-defined (up to orientation) take another smooth chart \\(\psi: M \to \widetilde{V} \subset \mathbb{R}^k\\) giving coordinates \\(y = (y^1, \cdots, y^k)\\), which induces coordinate vector fields \\(\partial\_{y^i} := D\psi^{-1}(\partial\_i)\\). 

Now take the transition map \\(F := \varphi \circ \psi^{-1}\\).

<!-- 
To check that this definition is indeed well-defined, take another parametrization, which we can write as $(\gamma \circ G)(s)$ with $c \leq s \leq d$ for some diffeomorphism $G: [c,d] \to [a,b]$. Then compute /\*using change of variables formula\*/ /\*$G$ technically needs to preserve orientation\*/
\\[
    \int_{c}^d \omega((\gamma \circ G)'(s))ds 
    = \int_{c}^d \omega(DG \circ \gamma'(G(s)))ds
    = \int_{c}^d \omega(\gamma'(G(s)))\det(DG)ds
    = \int_{a}^b \omega(\gamma'(t))dt
\\]
where crucially we have $\omega(DG \circ \gamma'(G(s))) = \omega(\gamma'(G(s)))\det(DG)$ because in this one-dimensional case, the map $DG$ is simply multiplication by $\det(DG)$. -->

<!-- In fact, the crucial property here that covectors have is that given some linear transformation on tangent vectors $T: \mathbb{R} \to \mathbb{R}$, we have $\omega(Tv) = \det(T)\omega(v)$. This allows us to interpret the evaluation $\omega(v)$ as the "weighted length" of the vector $v$, for the length of the stretched vector $\omega(Tv)$ is precisely the stretch factor times the length of the original vector $\det(T)\omega(v)$. Then, once we have a notion of length of the tangent vectors at each point, we can construct a notion of length of curves by integrating as above.

/\*note this is signed length\*/ -->

<!-- That is, if we apply some transformation $T$ to a vector $v$, we get some stretched vector $Tv$.  -->

<!-- Luckily, the evaluation $\omega(Tv)$ streteches by precisely this stretch factor $\det(T)$, which allows us to get the same result regardless of how we parametrize. This property $\omega(Tv) = \det(T)\omega(v)$ demonstrates that covectors factor in the length of a vector. -->

## Wedge Product Property



<!-- Taking inspiration from integrating covector fields, in order to define a notion of area or volume on the manifold, we should start by defining a notion of area or volume for vectors. In particular, given tangent vectors $v_1, \cdots, v_d$, we want a $d$-tensor $\omega$ such that $\omega(v_1, \cdots, v_d)$ can be interpreted as the volume of the parallelotope spaned by $v_1, \cdots, v_d$. However, if we stretch all these vectors by a linear transformation $T$, we need the volume of the stretched parallelotope $\omega(Tv_1, \cdots, Tv_d)$ to be the product $\det(T)\omega(v_1, \cdots, v_d)$ of the stretch factor of this transformation with the original volume. This is not the case for all tensors $\omega$, but those vectors that satisfy this make up an important subspace.

/\*visual of stretching? Perhaps allow user to mess with etries of $T$ and see parallelotope get stretched?\*/

/\*specift covariant covectors where appropriate\*/ -->

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