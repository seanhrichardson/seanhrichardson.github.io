---
layout: page
title: Wave Equation
---

## The Wave Equation

TODO: Reorder this to separate wave equation from IVP

#### Wave Equation Statement
What functions \\(u: \Omega \times \mathbb{R}_t \to \mathbb{R}\\) for \\(\Omega \subset \mathbb{R}_x^n\\) satisfy the following?
\\[
    \Delta_x u(\mathbf{x},t) = \frac{\partial^2}{\partial t^2}u(\mathbf{x},t).
\\]
This question is called the "wave equation", for a function \\(u\\) models a wave in nature if and only if it satisfies this equation.

#### Wave Equation IVP Statement
What functions \\(f: \Omega \times \mathbb{R}\_t \to \mathbb{R}\\) for \\(\Omega \subset \mathbb{R}\_x^n\\) satisfy the following?
\\[\begin{align}
    \Delta\_x u(x,t) &= \frac{\partial^2}{\partial t^2}u(x,t)\\\\\
    u(x,0) &= u\_0(x)\\\\\
    \left.\frac{\partial u}{\partial t}\right\|_{t=0} &= u\_1(x)
\end{align}\\]
for some \\(u_0, u_1: \Omega \to \mathbb{R}\\).

This question is called the "wave equation initial value problem", for the solution to this equation will model a wave with a prescribed initial position and velocity.

#### Derivation
Sound waves propogate the particles in the air. Let the vector \\(\mathbf{v}(x,t)\\) denote the velocity of the air at position \\(x\\) and time \\(t\\). Additionally, let \\(u(x,t)\\) be the density of the air at position \\(x\\) and time \\(t\\). 

As the air moves around, the density changes. To be precise, Stoke's theorem tells us the change in density of the air is related to the vector field \\(\mathbf{v}\\) by
\\[
    \frac{\partial u}{\partial t} = - \alpha \operatorname{div}(\mathbf{v}).
\\]

However, as the density of the air changes, the particles accelerate towards less dense regions. In particular, energy increases proportionally with the pressure, so the pressure acts as a potential function and therefore
\\[
    \frac{\partial \mathbf{v}}{\partial t} = - \beta \operatorname{grad}(u).
\\]

Then taking divergence of both sides and substituting yields /\*connect \\(\alpha, \beta\\) to \\(c\\)\*/
\\[
    \Delta u(x,t) = \frac{1}{c^2} \frac{\partial^2}{\partial t^2}u(x,t).
\\]
/\*change units so that \\(c = 1\\).\*/

#### 1D Wave Equation Solution
For this section, we will assume \\(u \in C^2\\). Then the wave equation becomes
\\[\begin{align}
    0 
    = \left(\frac{\partial^2 t}{\partial t^2} - \frac{\partial^2}{\partial x^2}\right)u(x,t)
    = \left(\frac{\partial }{\partial t} - \frac{\partial }{\partial x}\right)\left(\frac{\partial }{\partial t} + \frac{\partial }{\partial x}\right)u(x,t)
\end{align}\\]

The idea is to do a change of variables \\((x,t) \to (\eta, \xi)\\) so that we get something like
\\[
    \frac{\partial }{\partial \eta} = \left(\frac{\partial }{\partial t} - \frac{\partial }{\partial x}\right)
    \quad \text{and} \quad
    \frac{\partial }{\partial \xi} = \left(\frac{\partial }{\partial t} + \frac{\partial }{\partial x}\right),
\\]
which would greatly simplify equation /\*todo: number\*/.

The simple choice of \\(\eta = x-t\\) and \\(\xi = x+t\\) accomplishes something similar. Indeed, because \\(x = \frac{1}{2}(\eta + \xi)\\) and \\(t = \frac{1}{2}(\eta - \xi)\\) we get
\\[
\begin{align}
    \frac{\partial }{\partial \eta} &= \frac{\partial t}{\partial \eta}\frac{\partial }{\partial t} + \frac{\partial x}{\partial \eta}\frac{\partial }{\partial x} = -\frac{1}{2}\left(\frac{\partial }{\partial t} - \frac{\partial }{\partial x}\right)\\\\\
     \frac{\partial }{\partial \xi} &= \frac{\partial t}{\partial \xi}\frac{\partial }{\partial t} + \frac{\partial x}{\partial \xi}\frac{\partial }{\partial x} = \frac{1}{2}\left(\frac{\partial }{\partial t} + \frac{\partial }{\partial x}\right)\\\\\
\end{align}
\\]

Changing variables therefore reduces the problem to the much simpler equation
\\[
    -4\frac{\partial }{\partial \eta}\frac{\partial }{\partial \xi}u(\eta, \xi) = 0.
\\]
Integrating with respect to \\(\eta\\) and then with respect to \\(\xi\\) reveals that \\(u(\eta, \xi) = f(\eta) + g(\xi)\\) /\*elaborate\*/. Or, changing back to \\((x,t)\\) variables, \\(u(x,t) = f(x-t) + g(x+t)\\). 

/\*verify that the above is actually a solution\*/

In other words, every wave is the composition of a traveling wave going left and a traveling wave going right.
/\*visual for this.\*/

#### 1D IVP Solution

Now consider the extra information we have about the initial values of \\(u(x,t)\\).
\\[\begin{align}
    u(x,0) &= u\_0(x)\\\\\
    \left.\frac{\partial u}{\partial t}\right\|_{t=0}(x) &= u\_1(x).
\end{align}\\]

We can use the above to get an exact formula for \\(u(x,t)\\) by plugging in \\(u(x,t) = f(x-t) + g(x+t)\\) to the initial value information.
\\[\begin{align}
    f(x)+g(x) &= u\_0(x)\\\\\
    -f'(x)+g'(x) &= u_1(x)
\end{align}\\]
Integrating the second equation yields the new system for some constant \\(C\\).
\\[\begin{align}
    f(x)+g(x) &= u\_0(x)\\\\\
    -f(x)+g(x) &= \int_{0}^{x}u_1(s)ds + C
\end{align}\\]
Now we can solve for \\(f(x)\\) and \\(g(x)\\) and we get
\\[\begin{align}
    f(x) &= \frac{1}{2}\left(u\_0(x)-\int_0^{x}u_0(s)ds+C\right)\\\\\
    g(x) &= \frac{1}{2}\left(u\_0(x)+\int_0^{x}u_0(s)ds-C\right)
\end{align}\\]
Now that we know \\(f(x)\\) and \\(g(x)\\), we can write down a formula for \\(u(x,t) = f(x-t)+g(x+t)\\).
\\[
    u(x,t) = \frac{1}{2}\left(u_0(x-t)+u_0(x+t)\right)+\frac{1}{2}\int_{x-t}^{x+t}u_0(s)ds
\\]
The constant \\(C\\) even conveniently cancels and we have deduced *d'Alembert's formula*.

We have deduced that if a solution \\(u(x,t)\\) to the wave equation with initial values exist, it *must* be of the form given in d'Alembert's formula. Consequently, any solution must be unique.

However, we technically still must check that d'Alembert's formula does solve the wave equation initial value problem. Plugging the formula in reveals it works an so we know a solution exists!

#### 1D IVP Solution with Standing Waves

#### 1D IVP Solution for Distributions
