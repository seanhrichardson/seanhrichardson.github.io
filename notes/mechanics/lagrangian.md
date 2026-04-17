---
layout: page
title: Lagrangian
---

# Introduction to Lagrangian Systems

## Lagrangian System from Newtonian System

Consider some Newtonian system, which consists of a Riemannian manifold \\((M, g)\\) together with a force \\(F: TM \to TM\\) so that trajectories \\(\gamma(t)\\) are governed by Newton's equation
\\[
    D\_t \dot{\gamma}(t) = F(\gamma(t), \dot{\gamma}(t)).
\\]

Next, recall that given some *Lagrangian* \\(L: TM \to \mathbb{R}\\), the trajectories \\(\gamma: [a, b] \to M\\) that minimize the *action* integral
\\[
    S[\gamma] = \int\_a^{b} L(\gamma(t), \dot{\gamma}(t)) dt
\\]
must satisfy the [Euler-Lagrange equation], which is given in local coordinates \\((x^1, \cdots, x^n, v^1, \cdots, v^n)\\) on \\(TM\\) by
\\[
    \frac{\partial L}{\partial x^i}(\gamma(t), \dot{\gamma}(t)) - \frac{d }{d t} \frac{\partial L}{\partial v^i}(\gamma(t), \dot{\gamma}(t) = 0.
\\]
This raises a natural question: given a Newtonian system, is there a choice of function \\(L(x,v)\\) so that the Euler-Lagrange equation is equivalent to Newton's equation? For example, recall from the derivation of the [geodesic equation] that if we take our Lagrangian to be the kinetic energy \\(K(x,v) := \frac{1}{2}g\_x(v,v)\\) so that we consider the *energy functional*
\\[
    S[\gamma] = \frac{1}{2}\int\_a^b g\_{\gamma(t)}(\dot{\gamma}(t), \dot{\gamma}(t)) dt.
\\]
Then by the same computations as in the derivation of the [geodesic equation] we would find that
\\[
    \left(\frac{\partial K}{\partial x^i}(\gamma(t), \dot{\gamma}(t)) - \frac{d }{d t} \frac{\partial K}{\partial v^i}(\gamma(t), \dot{\gamma}(t)) \right)dx^{i}
    = \cdots 
    = -(D\_t \dot{\gamma}(t))^{\flat}.
    \tag{K}
    \label{eq:kinetic}
\\]
That is, the geodesic equation \\(D\_t \dot{\gamma}(t) = 0\\) is simply the Euler-Lagrange equation corresponding to the Newtonian system with trivial forcing term \\(F = 0\\). Furthermore, a Lagrangian can be found for a conservative force \\(F(x)\\), meaning \\(F = -\operatorname{grad} V\\) for some function \\(V: M \to \mathbb{R}\\), which implies \\(F^{\flat} = -dV\\). Indeed, first observe
\\[
    \left(\frac{\partial V}{\partial x^i}(\gamma(t), \dot{\gamma}(t)) - \frac{d }{d t} \frac{\partial V}{\partial v^i}(\gamma(t), \dot{\gamma}(t)) \right)dx^{i} 
    = \frac{\partial V}{\partial x^i}(\gamma(t), \dot{\gamma}(t)) dx^i = dV = -F^{\flat}(x).
    \tag{V}
    \label{eq:potential}
\\]
Therefore, by taking the Lagrangian \\(L(x,v) = K(x,v) - V(x)\\) and combining \eqref{eq:kinetic} and \eqref{eq:potential} we find
\\[
    \left(\frac{\partial L}{\partial x^i}(\gamma(t), \dot{\gamma}(t)) - \frac{d }{d t} \frac{\partial L}{\partial v^i}(\gamma(t), \dot{\gamma}(t)) \right)dx^{i} 
    = (F(x) - D\_t \dot{\gamma}(t))^{\flat}.
\\]
Therefore, the Euler-Lagrange equations for this choice of Lagranagian recovers Newton's law
\\[
    D\_t \dot{\gamma}(t) = F(\gamma(t)).
\\]

## Lagrangian System

In general, a ***Lagrangian system*** is a Riemannian manifold \\((M, g)\\) together with a ***Lagrangian*** \\(L: TM \to \mathbb{R}\\). Then a curve \\(\gamma(t)\\) over \\(M\\) is a solution to the Lagrangian system if it satisfies the Euler-Lagrange equation in coordinates
\\[
    \frac{\partial L}{\partial x^i}(\gamma(t), \dot{\gamma}(t)) - \frac{d }{d t} \frac{\partial L}{\partial v^i}(\gamma(t), \dot{\gamma}(t)) = 0.
\\]
This defines a flow \\(\varphi\_t: TM \to TM\\) over the phase space by \\(\varphi\_t(x,v) = (\gamma(t), \dot{\gamma}(t))\\) where \\(\gamma(t)\\) is the unique solution to the Lagrangian system with \\(\gamma(0) = x\\) and \\(\dot{\gamma}(0) = v\\). Importantly, solutions \\(\gamma(t)\\) to a Larangian system are critical points of the ***action***
\\[
    S[\gamma] = \int\_a^{b} L(\gamma(t), \dot{\gamma}(t)) dt.
\\]

/\*TODO... perhaps analysis of when this will be a minimzer vs just a critical point\*/

<!-- REFERENCES: -->
<!-- arnold mechanics -->
<!-- 2016-do-prince-new-progress-in-the-inverse-problem-in-the-calculus-of-variations.pdf  -->
<!-- zenkov-the-inverse-problem-of-the-calculus-of-variations.pdf -->
<!-- (for above two, note that general problem of finding Lagrangian system from Newtonian system is active area of research) -->
