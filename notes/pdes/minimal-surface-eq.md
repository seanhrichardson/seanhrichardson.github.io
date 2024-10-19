---
layout: page
title: Minimal Surface Equation
---

<!-- 
PRE-REQS:
- calculus of variations
    - the basic idea
    - at least one other simpler example
    - the fundamental lemma of calculus of variations in R^n
- linear algebra: 
    - vectors
    - determinants
    - square root of determinant formula for area spanned by m parallelograms in R^n.
- multivariable calculus:
    - gradient
    - divergence
    - integrals
    - computing areas of surfaces.
    - IBP for vectors
        - uses Stoke's theorem for divergence.
    - familiarity with \partial_{x^i} notation for basis vectors... or change this?
 -->

<!-- not sure if I should use \\(\partial_i\\) or \\(\mathbf{e}_i\\) notation...-->


## Minimal Surfaces

<!-- TODO: explain minimal surfaces... motivation -->

<!-- TODO: put some conditions on Omega somewhere... maybe mention  -->

<!-- TODO: too many details taking away from the big picture. Hide more details in exercises and such. -->

<!-- /\*insert nice pictures of minimal surfaces here.\*/ -->

#### Area Functional

We aim to create a criteria for a surface to be a minimal surface, but first we need to know how to compute the area of a surface. Consider a subset \\(\Omega \subset \mathbb{R}^n\\) and a function \\(u: \Omega \to \mathbb{R}^n\\). Graphing this function creates an \\(n\\)-dimensional surface \\(S\\) in \\(\mathbb{R}^{n+1}\\), and we want a formula for the area \\(A(u)\\) of this surface This graphed surface \\(S\\) can be more precisely expressed as the image of the function \\(\widetilde{u}: \mathbb{R}^{n} \to \mathbb{R}^{n+1}\\) defined by \\(\widetilde{u}(x^1, \cdots, x^n) = (x^1, \cdots, x^n, u(x^1, \cdots, x^n))\\) for some coordinates \\((x^1, \cdots, x^n)\\) on \\(\mathbb{R}^n\\). Recall we can compute the area of this surface using these coordinates by the formula
\\[
    A(u) = \int_{\Omega} dV = \int_{\Omega} \sqrt{\det G} dx^1 \cdots dx^n
\\]
where \\(G\\) is the matrix defined by
\\[ G = 
    \begin{pmatrix}
        \langle \partial_{x^1} \widetilde{u} , \partial_{x^1} \widetilde{u}\rangle & \cdots &  \langle \partial_{x^1} \widetilde{u} , \partial_{x^n} \widetilde{u}\rangle\\\\\
        \vdots & \ddots & \vdots \\\\\
         \langle \partial_{x^n} \widetilde{u} , \partial_{x^1} \widetilde{u}\rangle & \cdots &  \langle \partial_{x^n} \widetilde{u} , \partial_{x^n} \widetilde{u}\rangle
    \end{pmatrix}.
\\]

Computing the determinant of the above matrix is difficult. However, formula \\(dV = \sqrt{\det G} dx^1 \cdots dx^n\\) for computing the volume element works for *any* choice of coordinates \\((x^1, \cdots, x^n)\\), which we can take advantage. In fact, for each point \\(p \in \mathbb{R}^n\\), we choose convenient coordinates to compute the volume form \\(dV\\) at \\(p\\). We will choose the coordinate axis \\(y^1\\) to be in the direction of \\(\nabla u\\) and choose the rest of the coordinates \\(y^2, \cdots, y^n\\) to be orthogonal to the axis \\(y^1\\). Now let \\(\\{\mathbf{e}\_1, \cdots, \mathbf{e}\_n\\}\\) be the corresponding orthornormal basis where \\(\mathbf{e}\_i\\) points in the direction in which the \\(y^i\\) variable increases so that \\(\mathbf{e_1} = \nabla u / \\|\nabla u\\|\\), which allows us to quickly compute 
\\[
    \partial\_{y^1}u = \langle \mathbf{e}\_1 , \nabla u\rangle = \langle \nabla u / \\|\nabla u\\| , \nabla u\rangle = \\|\nabla u\\|.
\\]
Additionally, if \\(i \neq 2\\), then we simply have
\\[
    \partial_{y^i}u = \langle \mathbf{e}\_i , \nabla u\rangle = \\|\nabla u\\|\langle \mathbf{e}\_i , \mathbf{e}\_1 \rangle = 0.
\\]
This drastically simplifies the matrix \\(G\\) so that
\\[
    G = 
    \begin{pmatrix}
        \|\nabla u\|^2 & 0 & 0 & \cdots & 0\\\\\
            0         & 1 & 0 & \cdots & 0\\\\\
            0    & 0 & 1 & \cdots & 0\\\\\
            \vdots & \vdots & \vdots & \ddots & \vdots\\\\\
            0  & 0 & 0 & \cdots & 1
    \end{pmatrix}.
\\]

**Exercise.** Show that under these coordinates \\(G\\) does indeed simplify into the above form.

Thus we find \\(dV = \sqrt{1 + \\|\nabla u\\|^2} dy^1 \cdots dy^n\\) at each point. Because \\(dy^1 \cdots  dy^n = dx^1 \cdots dx^n\\) and the expression \\(\sqrt{1 + \\|\nabla u\\|^2}\\) is independent of coordinates, we can write \\(dV = \sqrt{1 + \\|\nabla u\\|^2} dx^1 \cdots dx^n\\) using our original global coordinates \\((x^1, \cdots, x^n)\\). Therefore we can express the area functional with the formula
\\[
    A(u) = \int_{\Omega} \sqrt{1 + \\|\nabla u\\|^2} dx^1 \cdots dx^n.
\\]

<!-- TODO: ALTERNATE PROOF (see notes) -->

#### Variation of the Area Functional

When is the graph of a function \\(u: \Omega \to \mathbb{R}\\) a minimal surface for \\(\Omega \subset \mathbb{R}^n\\)? By definition, this is when \\(u\\) is a critical point of the area functional. That is, given any other smooth function \\(\varphi: \Omega \to \mathbb{R}\\) satisfying \\(\varphi\|\_{\partial \Omega} = 0\\), then \\(\left.\frac{d }{d \varepsilon}\right\|\_{\varepsilon = 0} A(u + \varepsilon \varphi) = 0\\). Let's explore the consequences of this assumption in order to find a more conveneient equivalent condition. For this, compute the following by bringing the derivative inside the integral and taking derivatives.
\\[
\begin{align}
    \left.\frac{d }{d \varepsilon}\right\|\_{\varepsilon = 0} A(u + \varepsilon \varphi)
    &= \left.\frac{d }{d \varepsilon}\right\|\_{\varepsilon = 0} \int_{\Omega} \sqrt{1 + \\|\nabla (u + \varepsilon \varphi)\\|^2} dx^1 \cdots dx^n\\\\\
    &= \int_{\Omega} \left.\frac{d }{d \varepsilon}\right\|\_{\varepsilon = 0} \sqrt{1 + \\|\nabla (u + \varepsilon \varphi)\\|^2} dx^1 \cdots dx^n\\\\\
    &= \int_{\Omega} \frac{\langle \nabla u , \nabla \varphi\rangle}{\sqrt{1 + \\|\nabla u\\|^2}}dx^1 \cdots dx^n
\end{align}.
\\]
**Exercise.** Verify the last step in the above computation by using the chain rule and the product rule.

<!-- LINK OR HAVE HIDDEN SECTION ON THIS INTEGRATION BY PARTS FORMULA. -->
Next, recall the integration by parts formula
\\[
    \int_{\Omega} \langle \nabla f , X\rangle dV = \int_{\partial \Omega} f \langle X , N\rangle dA - \int_{\Omega} f \operatorname{div} X dV.
\\]
where \\(N\\) is the outwards pointing normal vector. We can use this to compute to further simplify our expression, noting the condition \\(\varphi\|\_{\partial \Omega} = 0\\) will ensure the boundary terms vanish.
\\[
\begin{align}
    \left.\frac{d }{d \varepsilon}\right\|\_{\varepsilon = 0} A(u + \varepsilon \varphi) 
    &= \int_{\Omega} \frac{\langle \nabla u , \nabla \varphi\rangle}{\sqrt{1 + \\|\nabla u\\|^2}}dx^1 \cdots dx^n\\\\\
    &=  \int_{\Omega} \left\langle \nabla \varphi , \frac{\nabla}{\sqrt{1 + \\|\nabla\\|^2}} u\right\rangle dx^1 \cdots dx^n\\\\\
    &= - \int_{\Omega} \varphi \operatorname{div}\left(\frac{\nabla u}{\sqrt{1 + \\|\nabla u\\|^2}}\right)dx^1 \cdots dx^n.
\end{align}
\tag{1}
\label{eq:chain}
\\]
Therefore, under the assumption \\(u\\) defines a minimal surface and so \\(\left.\frac{d }{d \varepsilon}\right\|\_{\varepsilon = 0} A(u + \varepsilon \varphi) = 0\\), then we have
\\[
    \begin{align}
        \int_{\Omega} \varphi \operatorname{div}\left(\frac{\nabla u}{\sqrt{1 + \\|\nabla u\\|^2}}\right)dx^1 \cdots dx^n = 0.
    \end{align}
\\]
However, by the fundamental lemma of calculus of variations, the only way the above expression can be true for *all* smooth functions \\(\varphi: \Omega \to \mathbb{R}\\) satisfying \\(\varphi\|\_{\partial \Omega} = 0\\) is if
\\[
    \operatorname{div}\left(\frac{\nabla u}{\sqrt{1 + \\|\nabla u\\|^2}}\right) = 0.
    \tag{2}
    \label{eq:min-surface}
\\]
This partial differential equation is called the *minimal surface equation*. It is also clear from the chain of equalities in (\ref{eq:chain}) that if (\ref{eq:min-surface}) is true, that then \\(\left.\frac{d }{d \varepsilon}\right\|\_{\varepsilon = 0} A(u + \varepsilon \varphi) = 0\\) and so \\(u\\) defines a minimal surface equation. Therefore, \\(u\\) defines a minimal surface exactly when it satisfies the minimal surface equation, making this equation very important to study.