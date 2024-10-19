---
layout: page
title: Geodesic Equation
---

## Geodesics

*Given points \\(p\\) and \\(q\\) on a Riemannian maifold \\(M\\), what is the shortest path between \\(p\\) and \\(q\\)?*

The goal of this page is to discuss this geometric question. In exploring this question, we will come across a natural notion of "straight lines" which we call "geodesics".

#### Length Functional

Our goal is, out of all paths \\(\gamma: [a,b] \to M\\) satisfying \\(\gamma(a) = p\\) \\(\gamma(b) = q\\), find one with minimal length (if it exists). We denote the length of such a curve \\(\gamma\\) by
\\[
    L(\gamma) = \int_a^b \|\dot{\gamma}(t)\|\_g dt = \int_a^b \sqrt{g(\dot{\gamma}(t), \dot{\gamma}(t))}dt.
    \label{eq:length}
    \tag{L}
\\]
This function \\(L\\) is called the *length functional* -- it takes as input a curve and outputs the length of the curve. Our goal is to minimize \\(L\\) and find a corresponding minimizing curve. We must be careful, however, for such a minimum might not necessarily exist! For example, consider the points \\(p = (1,0)\\) and \\(q = (-1,0)\\) in the punctured plane \\(\mathbb{R}^2 \smallsetminus \\{0\\}\\). Then we can find a path \\(\gamma\\) connecting \\(p\\) and \\(q\\) with length \\(L(\gamma)\\) arbitrarily close to \\(1\\), but a path with length precisely equal to \\(1\\) is impossible to achieve as \\(\gamma\\) must avoid the hole at \\((0,0)\\). Furthermore, even if such a minumum does exist, it might not be unique. For example, consider the circle \\(\mathbb{S}^1 \subset \mathbb{R}^2\\) and again take \\(p = (1,0)\\) and \\(q = (-1,0)\\). Then there are two minimizing curves of length \\(\pi\\) connecting \\(p\\) and \\(q\\): one traversing the top of the circle and one traversing the bottom.

/\*pictures for above examples\*/

**Exercise.** Verify that one can find a path \\(\gamma: [a,b] \to \mathbb{R}^2 \smallsetminus \{0\}\\) connecting \\((1,0)\\) and \\((-1,0)\\) of length arbitrarily close to \\(1\\), but no path of length \\(1\\) exists.

#### Energy Functional

The square root in the length functional (\ref{eq:length}) is annoying to deal with. Thus we instead consider the *energy functional*
\\[
    E(\gamma) 
    = \frac{1}{2} \int_a^b \|\dot{\gamma}(t)\|^2\_g dt 
    = \frac{1}{2} \int\_a^b g(\dot{\gamma}(t), \dot{\gamma}(t))dt.
    \label{eq:energy}
    \tag{E}
\\]
Note that if a curve \\(\gamma\\) has constant speed \\(\|\dot{\gamma}(t)\| = c\\), then we have the following explicit relationship between energy and length:
\\[
    E(\gamma) 
    = \frac{1}{2} (b-a) \cdot c
    = \frac{1}{2} \frac{L(\gamma)^2}{b-a}.
\\]
Thus, when restricting to curves of constant speed, a curve minimizes the energy functional if and only if it minimizes the length functional. We will find later that a minimizer to the energy functional must necessarily have constant speed, so later we can drop this restriction in the "only if" direction.

#### Calculus of Variations

We have found that finding the shortest path between two points \\(p,q \in M\\) involves studying global minimizers to the energy functional (\ref{eq:energy}). As a first step, let's assume \\(p,q\\) are close enough so that they are in the same coordinate chart \\((x^i)\\). Furthermore, we will start by finding *local minimizer* to the energy functional (\ref{eq:energy}). To be precise, a curve \\(\gamma(t) = (x^1(t), \cdots, x^n(t))\\) in this context is a local minimizer of the energy functional if for any choice of smooth functions \\(f^i: \mathbb{R} \to \mathbb{R}\\) and small deviation curve \\(\gamma\_{\varepsilon} = (x^1(t) + \varepsilon f^1(t), \cdots, x^n(t) + \varepsilon f^n(t))\\), then \\(E(\gamma) \leq E(\gamma\_{\varepsilon})\\) for small \\(\varepsilon\\).

We will see that a curve in local coordinates \\(\gamma(t) = (x^1(t), \cdots, x^n(t))\\) is a critical point of the energy functional exactly when
\\[
    \ddot{x}^k + \sum_{ij} \frac{1}{2} g^{kl} \left(\frac{\partial g_{lj}}{\partial x^i} + \frac{\partial g_{il}}{\partial x^j} - \frac{\partial g_{ij}}{\partial x^l}\right)\dot{x}^i\dot{x}^j = 0 \quad \text{ for all } k.
    \label{eq:geodesic}
    \tag{G}
\\]
This system of differential equations (\ref{eq:geodesic}) is called the *geodesic equation*, which we will now derive.

#### Derivation from Scratch

/\*TODO: follow Iva's notes\*/

#### Derivation using Euler-Lagrange

For those familiar with the Euler-Lagrange equation /\*link\*/, we can use this result to derive the geodesic equation more quickly. Indeed, in this case our Lagrangian \\(\mathcal{L}\\) is
\\[
    \mathcal{L}(\gamma) = \frac{1}{2}g(\dot{\gamma}, \dot{\gamma}) = \frac{1}{2}g\_{ij}\dot{x}^i\dot{x}^j.
\\]
By Euler-Lagrange, the critical points of the energy functional are precisely those curves \\(\gamma(t) = (x^1(t), \cdots, x^n(t))\\) that satisfy the *Euler-Lagrange equation*
\\[
    \frac{\partial \mathcal{L}}{\partial x^l}(\gamma(t)) 
    + \frac{d }{d t} \frac{\partial \mathcal{L}}{\partial \dot{x}^l}(\gamma(t)) = 0
    \quad \text{for all } l
\\]
Thus all we must do is compute each term individually. Indeed, the first term simpliefies to
\\[
\begin{align}
    \frac{\partial \mathcal{L}}{\partial x^l}(\gamma(t)) 
    = \frac{\partial }{\partial x^l}\left(\frac{1}{2} g\_{ij} \dot{x}^i \dot{x}^j\right)
    = \frac{1}{2}\frac{\partial g\_{ij}}{\partial x^l} \dot{x}^i\dot{x}^j.
\end{align}
\\]
Then the second term simplifies to
\\[
\begin{align}
    \frac{d }{d t} \frac{\partial \mathcal{L}}{\partial \dot{x}^l}(\gamma(t))
    &= \frac{d }{d t} \frac{\partial}{\partial \dot{x}^l}\left(\frac{1}{2} g\_{ij} \dot{x}^i \dot{x}^j\right)\\\\\
    &= \frac{1}{2}\frac{d }{d t}(g\_{il}\dot{x}^i) \\\\\
    &= \frac{\partial g\_{il}}{\partial x^j} \frac{d x^j}{d t}\dot{x}^i + g\_{il}\ddot{x}^i\\\\\
    &= \frac{\partial g\_{il}}{\partial x^j} \dot{x}^i\dot{x}^j + g\_{il}\ddot{x}^i.
\end{align}
\\]
Combining our findings by substituting these expressions into the Euler-Lagrange equation (multiplied by \\(-1\\)), then rearranging we get
\\[
\begin{align}
   0 &= -\frac{1}{2}\frac{\partial g\_{ij}}{\partial x^l} \dot{x}^i\dot{x}^j
    + \frac{\partial g\_{il}}{\partial x^j} \dot{x}^i\dot{x}^j + g\_{il}\ddot{x}^i\\\\\
    &= g\_{il}\ddot{x}^i + \frac{1}{2}\left\(\frac{\partial g\_{lj}}{\partial x^i} + \frac{\partial g\_{il}}{\partial x^j} -\frac{\partial g\_{ij}}{\partial x^l}\right\) \dot{x}^i\dot{x}^j.
\end{align}
\\]
Applying the inverse matrix \\(g^{kl}\\) to both sides yields the geodesic equation
\\[
    \ddot{x}^k + \frac{1}{2}g^{kl}\left(\frac{\partial g_{lj}}{\partial x^i} + \frac{\partial g_{il}}{\partial x^j} - \frac{\partial g_{ij}}{\partial x^l}\right)\dot{x}^i\dot{x}^j = 0.
\\]

#### Definition of Geodesics
A curve \\(\gamma(t)\\) is a *geodesic* if, when written in any local coordinates \\(\gamma(t) = (x^1(t), \cdots, x^n(t))\\), it locally satisfies the *geodesic equations*
\\[
    \ddot{x}^k(t) + \dot{x}^i(t)\dot{x}^j(t)\Gamma_{ij}^k(x(t)) = 0, \quad 1 \leq k \leq n
\\]
where the functions \\(\Gamma_{ij}^k\\) are the *Christoffel symbols* and are given in coordinates by
\\[
    \Gamma_{ij}^k = \frac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})
\\]

#### Example: Straight Lines in the Plane

Consider a curve \\(\gamma(t) = (x(t), y(t))\\) on \\(\mathbb{R}^2\\) with \\(a \leq t \leq b\\). Now we consider a small pertubation \\(\gamma_{\varepsilon}(t)\\) of this curve that still has the same endpoints. One way to write such a small pertubation is \\(\gamma\_{\varepsilon}(t) = ((x(t)+\varepsilon f(t), y(t) + \varepsilon g(t))\\) for any choice of smooth functions \\(f(t)\\) and \\(g(t)\\) that satisfy \\(f(a) = f(b) = 0\\) and \\(g(a) = g(b) = 0\\). This last condition is to ensure \\(\gamma_{\varepsilon}(t)\\) has the same endpoints: \\(\gamma_{\varepsilon}(a) = \gamma(a)\\\) and \\(\gamma_{\varepsilon}(b) = \gamma(b)\\). 

/\*TODO: finish this\*/

/\*change notation above to go with below\*/

/\*evaluate everything below at \\(t\\)\*/

\\[
\begin{align}
0 = \frac{d }{d \varepsilon} E(\gamma_{\varepsilon})
= \frac{d }{d \varepsilon}\int_a^b \dot{x}^2\_{\varepsilon}(t) + \dot{y}^2\_{\varepsilon}(t)
\end{align}dt
= \int_a^b \frac{d }{d \varepsilon} \dot{x}^2\_{\varepsilon}(t) dt + \int_a^b \frac{d }{d \varepsilon} \dot{y}^2\_{\varepsilon}(t) dt
\\]

First compute
\\[
    \int_a^b \frac{d }{d \varepsilon} \dot{x}^2\_{\varepsilon}(t) dt
    = 2\int_a^b \dot{x}\_{\varepsilon} \frac{\partial^2 x}{\partial t \partial \varepsilon} dt
    = \left.\dot{x}\_{\varepsilon}\frac{\partial x}{\partial \varepsilon}\right\|_a^b - 2\int_a^b \ddot{x}\_{\varepsilon} \frac{\partial x}{\partial \varepsilon} dt
    = - 2\int_a^b \ddot{x}\_{\varepsilon} \frac{\partial x}{\partial \varepsilon} dt
\\]
/\*explain boundary terms\*/

An identical computation shows 
\\[
    \int_a^b \frac{d }{d \varepsilon} \dot{y}^2\_{\varepsilon}(t) dt = - 2\int_a^b \ddot{y}\_{\varepsilon} \frac{\partial y}{\partial \varepsilon} dt.
\\]

Therefore 
\\[
    0 = \int_a^b \ddot{x}\_{\varepsilon} \frac{\partial x}{\partial \varepsilon} dt + \int_a^b \ddot{y}\_{\varepsilon} \frac{\partial y}{\partial \varepsilon} dt
\\]

/\*finish explanation\*/

/\*cite iva\*/