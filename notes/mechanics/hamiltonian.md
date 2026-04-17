---
layout: page
title: Hamiltonian
---

<!-- TODO: below I say "if FL is a diffeomorphism", but maybe should say bundle ism? idk -->

<!-- TODO: proofread because there are some typos -->

# Hamiltonian Mechanics

## Hamiltonian System from Lagrangian System

Recall a *Lagrangian System* is a Riemannian manifold \\((M, g)\\) together with a *Lagrangian* \\(L: TM \to \mathbb{R}\\). Then a curve \\(\gamma(t)\\) over \\(M\\) is a solution to the Lagrangian system if it satisfies the *Euler-Lagrange equations*, which is given in coordinates \\((x^1, \cdots, x^n, v^1, \cdots, v^n)\\) over \\(TM\\) by
\\[
    \frac{\partial L}{\partial x^i}(\gamma(t), \dot{\gamma}(t)) - \frac{d }{d t} \frac{\partial L}{\partial v^i}(\gamma(t), \dot{\gamma}(t)) = 0.
\\]

Next, recall a Lagrangian \\(L: TM \to \mathbb{R}\\) over the bundle \\(TM\\) induces the *Legendre transform* \\(\mathbb{F}L: TM \to T^{\*}M\\) by differentiating over the fibers:
\\[
    \langle \mathbb{F}L(v) , w \rangle
    := \left.\frac{d }{d t}\right\|\_{t=0} L(v+tw)
    = \frac{\partial L}{\partial v^i}(x,v) w^i.
    <!-- \tag{\\(\star\\)}
    \label{eq:legendre} -->
\\]
Equivalently, we could define \\(\mathbb{F}L(v) = \frac{\partial L}{\partial v^i}(x,v) dx^i\\), and we call the covector \\(\xi(x,v) = \mathbb{F}L(v)\\) the ***generalized momentum*** \\(\xi(x,v)\\), which satisfies \\(\xi\_i(x,v)  = \frac{\partial L}{\partial v^i}(x,v)\\). For many choices of Lagrangians in practice, we will find the Legendre transform to be a diffeomorphism \\(\mathbb{F}L: TM \to T^{\*}M\\). In this case, we obtain a nice duality if we can find a function \\(H: T^{\*}M \to \mathbb{R}\\) that induces Legendre transform \\(\mathbb{F}H: T^\*M \to T^{\*\*}M \simeq TM\\) so that \\(\mathbb{F}H = \mathbb{F}L^{-1}\\). That is, we need
\\[
\begin{align}
    w = \mathbb{F}H(\mathbb{F}L(w))
    = \mathbb{F}H\left(\frac{\partial L}{\partial v^i}(x,w)dx^i\right)
    = \frac{\partial H}{\partial \xi^i}(\xi(x,w)) \partial\_i.
\end{align}
\\]
That is, we need to find a function \\(H: T^\*M \to \mathbb{R}\\) so that \\(w = \frac{\partial H}{\partial \xi^i}(\xi(x,w)) \partial\_i\\). By analyzing this condition, one can derive the *Hamiltonian* function
\\[
    H(x, \xi) = \langle \xi , v(x, \xi)\rangle - L(x, v(x, \xi))
    \tag{H}
    \label{eq:hamiltonian}
\\]
where \\(v(x, \xi) = \mathbb{F}L^{-1}\\); that is, \\(v(x, \xi(x, w)) = w\\). We can verify this function works by computing
\\[
\begin{align}
    \frac{\partial H}{\partial \xi\_i} = v^i(x, \xi) + \xi\_j \frac{\partial v^j}{\partial \xi\_i} - \frac{\partial L}{\partial \xi\_i}
    = v^i(x, \xi) + \xi\_j \frac{\partial v^j}{\partial \xi\_i} - \frac{\partial L}{\partial v^j} \frac{\partial v^j}{\partial \xi\_i}
    = v^i(x, \xi)
\end{align}
\\]
where in the last step we used \\(\frac{\partial L}{\partial v^j} = \xi\_j\\). Therefore, we find the Hamiltonian function \\(H\\) indeed satisfies the desired property:
\\[
    \frac{\partial H}{\partial \xi\_i}(x,w)\partial\_i = v(x, \xi(x,w)) = w.
\\]
Next, recall a Lagrangian system is governed by the system of differential equations
\\[
    \begin{align}
            \dot{x}^i &= v^i, \\\\\
            \frac{d }{d t} \frac{\partial L}{\partial v^i} &= \frac{\partial L}{\partial x^i}.
    \end{align}
    \tag{L}
    \label{eq:lagrangian}
\\]
We now use the Legendre transform \\(\mathbb{F}H: T^\*M \to TM\\) to pull back the above system of equations onto the cotangent bundle. Let \\(v(x, \xi) = \mathbb{F}H = \mathbb{F}L^{-1}\\\) so that the pullback of the first equation in \eqref{eq:lagrangian} becomes
\\[
    \dot{x}^i = v^i(x,\xi) = \frac{\partial H}{\partial \xi\_i}.
\\]
Next use \\(\frac{\partial L}{\partial v^i}(x,v) = \xi^i(x,v)\\) to compute the pullback of the second equation of \eqref{eq:lagrangian} to be
\\[
\begin{align}
    \dot{\xi}^i = \dot{\xi}^i(x,v(x, \xi)) 
    = \frac{d }{d t} \frac{\partial L}{\partial v^i}(x, v(x, \xi))
    = \frac{\partial L}{\partial x^i}(x, v(x, \xi)).
\end{align}
\\]
Next note the Legendgre transform \\(v(x, \xi)\\) has no dependence on \\(x\\) by definition, so in particular \\(\frac{\partial v(x, \xi)}{\partial x^i} = 0\\). Therefore, by differentiating \eqref{eq:hamiltonian} we find
\\[
    \frac{\partial H}{\partial x^i}(x, \xi) = -\frac{\partial L}{\partial x^i}(x, v(x, \xi)).
\\]
Therefore, we find the pullback of the Lagrangian system differential equations onto the cotangent bundle is given by *Hamilton's equations*
\\[
\begin{align}
    \dot{x}^i &= \frac{\partial H}{\partial \xi\_i}\\\\\
    \dot{\xi}^i &= -\frac{\partial H}{\partial x^i}.
\end{align}
\\]

## Hamiltonian System
A ***Hamiltonian system*** is a Riemannian manifold \\((M, g)\\) together with a ***Hamiltonian*** \\(H: T^\*M \to \mathbb{R}\\). Then a curve \\((x(t), \xi(t))\\) in the cotangent bundle \\(T^\*M\\) is a solution to the Hamiltonian system if it satisfies ***Hamilton's equations***
\\[
\begin{align}
    \dot{x}^i &= \frac{\partial H}{\partial \xi\_i}\\\\\
    \dot{\xi}^i &= -\frac{\partial H}{\partial x^i}.
\end{align}
\\]

By the above derivation, a Lagrangian system over \\((M, g)\\) with Lagrangian \\(L: TM \to \mathbb{R}\\) induces a Hamiltonian system so long as the *Legendre transform* \\(\mathbb{F}L: TM \to T^*M\\) is a diffeomorphism. In this case, the Hamiltonian is given by
\\[
    H(x, \xi) = \langle \xi , v(x, \xi)\rangle - L(x, v(x, \xi))
\\]
where \\(v(x, \xi) = \mathbb{F}L^{-1}(x, v) = \mathbb{F}H(x, v)\\).

/\*TODO: derive nice conditions for when we will indeed have a diffeomorphism... convexity, positive-definitite quadratic form, etc?\*/

/\*TODO: in the case \\(L(x,v) = K(x,v) - V(x)\\) or something, derive the Hamiltonian?\*/