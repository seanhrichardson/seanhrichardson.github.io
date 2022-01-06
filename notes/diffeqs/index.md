---
layout: page
section: NOTES
title: Differential Equations
---

## Differential Equations

**Fundamental Theorem of Autonomous ODE's.**
Take $U \subset \mathbb{R}^n$ open, smooth $F: U \to \mathbb{R}^n$ (i.e. vector field) and consider the system of ODE's
\\[\begin{align}
\dot{x}^1(t) &= F^1(x^1(t), \cdots, x^n(t))\\\\\
&\vdots\\\\\
\dot{x}^n(t) &= F^1(x^1(t), \cdots, x^n(t))
\end{align}\\]

Then, for any $t_0 \in \mathbb{R}$ and $x_0 \in U$, there is neighborhood $J_0$ of $t_0$ and neighborhood $U_0$ of $x_0$ such that for each $(c^1, \cdots, c^n) \in U_0$, there exists a $C^1$ solution $x: J_0 \to U$ that satisfies the initial condition $x^i(t_0) = c^i$ and $x(t)$ is locally unique.

*(Additional smoothness result)* Furthermore, we get a smooth map $\theta: J_0 \times U_0 \to U$ defined by $\theta(t,c) = x(t)$, where $x(t)$ is the unique solution that satisfies the initial condition $x^i(t_0) = c^i$.

**Fundamental Theorem of Nonautonomous ODE's.** TODO (Lee thm D.6)

**Solving Separable Equations.** (separate then integrate)

**Propagator Method (i.e. integrating factors).** TODO

**Solving system of homogenous linear equations.** Begin with system $\mathbf{\dot{x}} = A \mathbf{x}$. 

Then compute the eigenvalues and eigenvectors $(\lambda_i, \mathbf{v_i})$ and note $e^{\lambda_i}t \mathbf{v_i}$ is a solution. Thus by linearity, 
\\[\mathbf{x}(t) = \sum_{i} \alpha_i e^{\lambda_i t} \mathbf{v_i}\\]
is a solution for any constants $\alpha_i$ and is in fact the general solution.