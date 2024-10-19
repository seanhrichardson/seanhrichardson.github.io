---
layout: page
title: PDES
---

#### PDEs
1. Laplace Equation
\\[
    \Delta u = 0.
\\]
1. Wave Equation
\\[
    (\partial_t^2 - \Delta) u = 0.
\\]
1. Heat Equation
\\[
    (\partial_t - \Delta) u = 0.
\\]
1. Schrödinger's Equation
\\[
    (i \partial_t + \Delta) u = 0.
\\]
1. Helmholtz's Eigenvalue Equation
\\[
    -\Delta u = \lambda u.
\\]
1. Poisson's Equation
\\[
    \Delta u = f
\\]
1. Minimal Surface Equation
\\[
    \operatorname{div}\left(\frac{Du}{(1+|Du|^2)^{1/2}}\right)
\\]

#### Systems of PDES
1. Cauchy-Riemann Equations
1. Maxwell's Equations
1. Euler's Flow Equations
1. Navier-Stoke's Flow Equations
1. Einstein Field Equations

#### Problems
1. Dirichlet Problem
\\[
    \begin{align}
        \Delta u(x) &= 0 \quad&&\text{for all } x \in \Omega\\\\\
        u(x) &= u_0(x) \quad&&\text{for all } x \in \partial \Omega
    \end{align}
\\]
1. Neumann Problem
1. Palteau Problem
1. Cauchy Problem
\\[
    \begin{align}
        (\partial_t - \Delta)u(t,x) &= 0 \quad&&\text{for all } (t,x) \in \mathbb{R}^{+} \times \mathbb{R}^3\\\\\
        u(0,x) &= u_0(x) \quad &&\text{for all } x \in \mathbb{R}^3
    \end{align}
\\]
1. IVP for wave equation.
1. IVP for heat equation.