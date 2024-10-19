---
layout: page
title: Heat Diffusion Equation
---

## The Heat Diffusion Equation

#### Derivation from Brownian Motion

The heat equation is also known as the diffusion equation, for it also models the diffusion of small particles throughout space. Small particles are randomly jostled by larger particles, colliding millions of times per second and so are being constantly pushed in randomly changing directions. First let's establish some principles for how these particles move.

1. For a change in time \\(\tau\\), the probability any particle moves \\(\mathbf{x}\\) is modeled by a probability distribution \\(B_{\tau}(\mathbf{x})\\).
1. A particle is equally likely to move in any direction, so we have radial symmetry, written \\(B_{t}(\mathbf{x}) = \phi_{t}(\\|\mathbf{x}\\|)\\), for each probability distribution.
1. The movements of small particles are independent.

Our goal is to determine how the density \\(\rho(x,t)\\), which we assume to be smooth, evolves over time. The last bullet implies the density \\(\rho(x,t)\\) of particles evolves according to the convolution
\\[
    \rho(\mathbf{x},t+\tau) = \rho(\mathbf{x},t) \ast_x B_{\tau}(x) = \int_{\mathbb{R}^n} B_t(\mathbf{\delta}) \rho(\mathbf{x} + \boldsymbol{\delta},t)dV(\boldsymbol{\delta}).
\\]
We can show that the density \\(\rho\\) of particles will obey the heat equation by following Einstein's argument in his famous paper *Investigations on the Theory of Brownian Movement*. First apply Taylor expansions in the \\(t\\) and \\(x\\) variables to compute
\\[
    \begin{align}
        \rho(x,t) + \tau \frac{\partial \rho}{\partial t} + o(\tau^2)
        &= \rho(x,t+\tau)\\\\\
        &= \int_{\mathbb{R}^n} B_{\tau}(\boldsymbol{\delta}) \rho(\mathbf{x} + \boldsymbol{\delta},t)dV(\boldsymbol{\delta})\\\\\
        &= \int_{\mathbb{R}^n} B_{\tau}(\boldsymbol{\delta}) (\rho(x,t) + \langle \operatorname{grad}(\rho) , \boldsymbol{\delta}\rangle + \frac{1}{2}\langle \operatorname{Hess}(\rho) \boldsymbol{\delta} , \boldsymbol{\delta} \rangle + \cdots) dV(\boldsymbol{\delta})\\\\\
        &= \rho(x,t)\int_{\mathbb{R}^n} B_{\tau}(\boldsymbol{\delta})dV(\boldsymbol{\delta})
        + \operatorname{grad}(\rho) \cdot \int_{\mathbb{R}^n} B_{\tau}(\boldsymbol{\delta}) \boldsymbol{\delta} dV(\boldsymbol{\delta})
        + \frac{1}{2}\int_{\mathbb{R}^n} B_{\tau}(\boldsymbol{\delta}) \frac{1}{2}\langle \operatorname{Hess}(\rho) \boldsymbol{\delta} , \boldsymbol{\delta} \rangle dV(\boldsymbol{\delta}) + \cdots
    \end{align}
\\]
Because \\(B_{\tau}(\boldsymbol{\delta})\\) is a probability distribution, we must have that \\(\int_{\mathbb{R}^n} B_t(\boldsymbol{\delta})dV(\boldsymbol{\delta}) = 1\\). Furthermore, by the symmetry of \\(B_{\tau}\\), we have \\(\int_{\mathbb{R}^n} B_{\tau}(\boldsymbol{\delta}) = 0\\). To evaluate the last integral, compute
\\[
    \begin{align}
    \frac{1}{2}\int_{\mathbb{R}^n} B_{\tau}(\boldsymbol{\delta}) \frac{1}{2}\langle \operatorname{Hess}(\rho) \boldsymbol{\delta} , \boldsymbol{\delta} \rangle dV(\boldsymbol{\delta})
    &= \frac{1}{2}\int_{0}^{\infty}\int_{S^{n-1}} r^2 \langle \operatorname{Hess} \mathbf{v} , \mathbf{v} \rangle \phi_{\tau}(r) dS(\mathbf{v})dr\\\\\
    &= \frac{1}{2}\int_{0}^{\infty}r^2 \phi_{\tau}(r) dr \int_{S^{n-1}} \langle \operatorname{Hess} \mathbf{v}, \mathbf{v} \rangle dS(\mathbf{v})\\\\\
    &= \frac{1}{2}\operatorname{Var}(\phi_\tau) \cdot C \cdot \operatorname{Trace}(\operatorname{Hess}(\rho)) = \beta \operatorname{Var}(\phi_\tau) \cdot \Delta_x \rho
    \end{align}
\\]
where we used that \\(\int_{S^{n-1}} \langle A\mathbf{v} , \mathbf{v} \rangle ds(V) = \frac{1}{n}\operatorname{Vol}(S^{n-1})\operatorname{Trace}(A)\\). Substitute this result into the earlier computation, divide by \\(\tau\\), and take \\(\tau \to 0\\). By studying the variance and higher order moments of \\(\phi_t\\), one can show second order term will remain constant and the higher order terms will approach \\(0\\). This leaves us with the diffusion equation
\\[
    \frac{\partial \rho}{\partial t} = \alpha \Delta_x \rho.
\\]

We can similarly think of small packets of heat being tranferred by particles randomly colliding and exchanging energy, then heat is also constatly and randomly changing directions. The same analysis above then applies to heat and yields the heat equation.

#### S