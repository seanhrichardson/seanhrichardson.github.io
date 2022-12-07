---
layout: page
section: NOTES
title: S2
permalink: /semidirect-product.html
---

## Semidirect Product

#### Rotating and Translating the Plane
/\*notation will be cleaner later if I write this as the additive group of vectors in the plane \\(\mathbb{R}^2\\)\*/

Consider the group of translations on the plane. That is, for each vector $x$ in the plane, there is an element $T_x \in T$ that translates the plane by $x$. We can think of $T_x$ as a function \\(T_x: \mathbb{R}^2 \to \mathbb{R}^2\\) given by $T_x(z) = x+z$. Notice that first translating by a vector $x$ and then translating by a vector $y$ is the same as translating by $x+y$. Therefore, $T$ is a group under composition where $T_x \circ T_y = T_{x+y}$.

/\*visual\*/

Separately, consider the group $R$ of rotations on the plane. For every angle $\theta \in [0, 2\pi)$, there is an element $R_{\theta} \in R$ that rotates the plane counterclockwise by $\theta$. This mapping \\(R_{\theta}: \mathbb{R}^2 \to \mathbb{R}^2\\) can be expressed by the following matrix
\\[
    R_{\theta} = \begin{pmatrix}
        \cos(\theta) & \sin(\theta)\\\\\
        -\sin(\theta) & \cos(\theta)
    \end{pmatrix}.
\\]
Rotating by $\theta$ and then rotating by $\phi$ is the same as rotating by $\theta + \phi$ and so matrix composition turns $R$ into a group where $R_{\theta}R_{\phi} = R_{\theta+\phi}$.

/\*visual\*/

Now let us try to combine the translation group $T$ and the rotation group $R$ into a group $G$ of translations *and* rotations. An element of $G$ should be a pair $(T_x, R_{\theta})$ that first rotates the plane by $\theta$ and then translates the plane by $T_x$. That is, $(T_x, R_{\theta})$ is the composition \\(T_x \circ R_{\theta}: \mathbb{R}^2 \to \mathbb{R}^2\\) where $T_x \circ R_{\theta}(z) = x + R_{\theta}z$. In order for $G$ to be a group, we need to figure out how elements of $G$ compose together. That is, given a pair $(T_x, R_{\theta})$ and a pair $(T_y, R_{\phi})$, can we write down their composition as a pair? Applying $(T_y, R_{\phi})$ and then applying $(T_x, R_{\theta})$ is given by the composition $T_{x} \circ R_{\theta} \circ T_{y} \circ R_{\phi}$. Let's compute what this composition does:
\\[
    (x, R_{\theta}) \circ (y, R_{\phi})(z)
    = (x, R_{\theta}(y + R_{\phi}(z))
    = x + R_{\theta}(y+R_{\phi}(z))
    = (x+R_{\theta}y) + R_{\theta+\phi}(z).
\\]
That is, applying $(T_y, R_{\phi})$ and then $(T_x, R_{\theta})$ is equivalent to applying $(T_{x+R_{\theta}y}, R_{\theta+\phi})$. Therefore composition in this group is given by
\\[
    (x, R_{\theta}) \circ (y, R_{\phi}) = (x+R_{\theta}y, R_{\theta}R_{\phi})
\\]

#### Semidirect Product
/\*define\*/

/\*motivate/justify more abstractly?\*/

#### More Examples
/\*$D_{2n}$\*/
