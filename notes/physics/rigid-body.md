---
layout: page
title: Rigid Body Dynamics
---

## Rigid Body Dynamics

TODO: Define what a rigid body is

TODO: Do this is the language of manifolds, SO(3), Hamiltonian, etc. if possible

#### Angular Momentum

Consider a rigid body \\(B\\) with angular velocity \\(\boldsymbol{\omega}\\). We aim to compute the angular momentum about the center of mass, which we declare to be the origin.

/\*optional... define \\(I\\) as a bilinear map...\*/

Note a particle at position \\(\mathbf{r}\\) will have velocity \\(\mathbf{v}(\mathbf{r})\\) = \\(\mathbf{r} \times \boldsymbol{\omega}\\). By integrating over the contribution of all particles, we compute that the angular momentum of \\(B\\) about the origin will be given by

\\[
\begin{align}
   \mathbf{L} 
   &= \int_{B} \boldsymbol{\omega} \times \mathbf{v}(\mathbf{r}) \operatorname{dm}(\mathbf{r})\\\\\
   &= \int_{B} \boldsymbol{\omega} \times (\mathbf{r} \times \boldsymbol{\omega}) \operatorname{dm}(\mathbf{r})\\\\\
   &= \int_{B} \mathbf{r}(\mathbf{r} \cdot \boldsymbol{\omega}) - \\|\mathbf{r}\\|^2\boldsymbol{\omega} \operatorname{dm}(\mathbf{r})\\\\\
   &= \int_{B} \mathbf{r} \mathbf{r}^T \boldsymbol{\omega} - \\|\mathbf{r}\\|^2\operatorname{Id}\boldsymbol{\omega} \operatorname{dm}(\mathbf{r})\\\\\
   &= \left(\int_{B} \mathbf{r} \mathbf{r}^T - \\|\mathbf{r}\\|^2\operatorname{Id} \operatorname{dm}(\mathbf{r})\right) \boldsymbol{\omega}
   = I\boldsymbol{\omega}
\end{align}
\\]
where \\(I\\) is the real-valued, symmetric \\(3 \times 3\\) matrix given by
\\[
    I = \int_{B} \mathbf{r} \mathbf{r}^T - \\|\mathbf{r}\\|^2\operatorname{Id} \operatorname{dm}(\mathbf{r}).
\\]

#### Conservation of Angular Momentum and Euler's Equations

TODO: Derive Euler's equations. This requires reconciling the body frame and the space frame, and appealing to the spectral theorem.

#### Conservation of Energy

#### Intermediate Axis Theorem
Two ways: By conservation of energy and analysis of Euler's equations.