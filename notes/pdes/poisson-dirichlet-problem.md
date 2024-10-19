---
layout: page
title: Poisson Boundary Value Problem
---

## Poisson Boundary Value Problem

TODO: talk about conditions on \\(U\\), regularity of the boundary, etc.

\\[
    \begin{cases}
        \Delta u = f & \text{in } U \\\\\
        u = g & \text{on } \partial U
    \end{cases}
\\]

#### Temperature of a Surface in Equillibrium

TODO

#### Existence and Uniqueness

TODO... if not a nice argument for existence, can use the below section

#### Reducing to Dirichlet Problem

TODO: maybe capitalize fundamental solution to \\(\Phi\\)

We know how to solve the Poisson equation without the boundary conditions: we take a fundamental solution \\(\phi(x)\\) satisfying \\(\Delta \phi = \delta\\), then set \\(u = f \ast \phi\\). Unfortunately, this will not satisfy the boundary condition. However, if we can solve the Dirichlet problem for \\(U\\) and arbitrary boundary conditions, then we can correct the boundary conditions and solve the Poisson boundary value problem. We consider, for each \\(x \in U\\), the Dirichlet problem
\\[
    \begin{cases}
        \Delta \phi^{x}(y) = 0 & \text{on } U \\\\\
        \phi^{x}(y) = \phi(y-x) & \text{on } \partial U.
    \end{cases}
\\]
From studying the Dirichlet problem we know there exists a unique solution \\(\phi^{x}(y)\\) although it might be hard to explicitly find. Now define *Green's Function* \\(G(x,y) = \phi(y-x) - \phi^{x}(y)\\) and note \\(G(x,y)\\) will satisfy
\\[
    \begin{cases}
        \Delta_y G(x,y) = \delta_x & \text{for } y \in U \\\\\
        G(x,y) = 0 & \text{for } y \in \partial U.
    \end{cases}
\\]
That is, \\(G(x,y)\\) tweaks the fundamental solution so that it will not mess up the boundary conditions. Therefore the integral
\\[
    u_0(y) = \int_U G(x,y)f(x)dx
\\]
will satisfy (TODO: Laplacian condition needs verification... maybe can cite a Dirichlet result)
\\[
    \begin{cases}
        \Delta u_0 = f & \text{in } U\\\\\
        u_0 = 0 & \text{on } \partial U.
    \end{cases}
\\]
To add in correct boundary conditions, we only must solve one more Dirichlet problem for some \\(u_1(x)\\) satisfying
\\[
    \begin{cases}
        \Delta u_1 = 0 & \text{in } U\\\\\
        u_1 = g & \text{on } \partial U.
    \end{cases}
\\]
Then the function \\(u(x) = u_0(x) + u_1(x)\\) will solve the Poisson boundary value problem.

#### Rewriting the Solution with Green's Function

TODO: Think about if redefining Green's function 

In the previous section we used Green's function \\(G(x,y)\\) to define \\(u_0(x)\\) that solves the Poisson problem while vanishing at the boundary, then solved a Dirichlet problem to give a function \\(u_1(x)\\) with vanishing Laplacian and correct boundary values. The sum \\(u(x) = u_0(x) + u_1(x)\\) will then solve the Poisson boundary value problem. However, it turns out that by the properties of Green's function \\(G(x,y)\\), we can can also \\(G(x,y)\\) to find \\(u_1(x)\\), which conveniently reduces the entire solution to just finding \\(G(x,y)\\).

Indeed, note that for any function \\(u(x)\\), we have the following, remembering 
\\[
    \begin{align}
        u(x) &= (\delta \ast u)(x) = (\Delta \phi \ast u)(x) = \int_U \Delta \phi(y-x)u(y) dy
    \end{align}
\\]