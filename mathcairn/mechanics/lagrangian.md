---
layout: page
title: Lagrangian
---

# Lagrangian

/\*relevant E-L review...\*/

/\*explanation of phase space via Newton's laws, etc...\*/

<!-- TODO: think if I want n=3 for a particle here, or if I should make this more general? -->

Suppose a particle (of mass \\(1\\)) of has trajectory \\(x(t) = (x^1(t), \cdots, x^n(t))\\) governed by various forces (gravity, electromagnetic forces, etc.) via Newton's laws. That is, the trajectory is governed by the system of second order differential equations
\\[
    \ddot{x}^k(t) = F^k(x,\dot{x})
\\]
for some force function \\(F(x,v)\\) depending on the position \\(x\\) and velocity \\(v\\) of the particle. /\*todo... some history\*/ had an amazing idea: what if we could find a function \\(L(x,v)\\) defined over the phase-space so that the Euler-Lagrange equations
\\[
    \frac{d }{d t} \frac{\partial L}{\partial v^k} - \frac{\partial L}{\partial x^k} = 0
\\]
is exactly equivalent to Newton's law above. Let's try to find such a \\(L(x,v)\\) beginning with the simple case \\(F = 0\\) representing no forces on the particle. Then, using \\(\dot{x} = v\\), Newton's equation is simply
\\[
    \dot{v}^k(t) = 0.
\\]
The only way the Euler-Lagrange equations can satisfy this is by
\\[
     \frac{d }{d t} \frac{\partial L}{\partial v^k} = \dot{v}^k
     \quad\quad \text{and} \quad\quad
     \frac{\partial L}{\partial x^k} = 0.
\\]
The second condition implies the Lagrangian has no dependence on position and so we look for a function \\(L(v)\\) satisfying the first condition. All such functions satisfying this can be explicitly derived, which is the content of the following exercise, but the most natural choice is
\\[
    L(x,v) = \frac{1}{2}\sum_{k=0}^{n}(v^k)^2.
\\]
Note this is simply the kinetic energy \\(K(v)\\) of the particle.
\\[
    .
\\]

**Exercise.** /\*TODO: derive all Lagrangians...\*/

/\*TODO: more general case... conservative force?\*/

