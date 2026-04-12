---
layout: page
title: Magnetic System
---

# Magnetic System

In Euclidean space \\(\mathbb{R}^3\\), recall the Lorentz force \\(F\\) on a particle of unit charge moving with velocity vector \\(v\\) through a magnetic field \\(B\\) is given by
\\[
   F = v \times B.
\\]
We will rewrite this in the language of multilinear algebra. As a first step, recall the cross product is given by \\((v \times B)^{\flat} = \star(v^{\flat} \wedge B^{\flat})\\) for the Hodge star operator \\(\star\\). To simplify this further, we make use of the following lemma.

**Lemma.** For an \\(n\\)-dimensional inner product space \\(V\\) with \\(v\in V\\) and \\(\alpha \in \Lambda^{k}(V^*)\\), we have
\\[
     \star(v^{\flat} \wedge \alpha) = (-1)^{k+1}i\_v(\star \alpha).
\\]

*Proof.* Let \\(d\operatorname{vol}\\) denote the volume form induced by the inner product \\(\langle \cdot , \cdot \rangle\\), and take some \\(\gamma \in \Lambda^{k+1}(V^*)\\). Then by the definition of the Hodge star and because the interior product \\(i\_v\\) is adjoint to the exterior product \\(v^{\flat} \wedge \cdot\\), we find
\\[
\begin{align}
    \gamma \wedge \star(v^{\flat} \wedge \alpha)
    = \langle \gamma , v^{\flat} \wedge \alpha \rangle d\operatorname{vol}
    = \langle i\_v \gamma, \alpha , \rangle d\operatorname{vol}
    = (i\_v \gamma) \wedge \star \alpha
\end{align}
\\]
where in the last step we used the definition of the Hodge star again. Now recall the Leibniz rule for interior product gives
\\[
    i\_v(\gamma \wedge \star \alpha) = i\_v \gamma \wedge \star \alpha + (-1)^{k} \gamma \wedge i\_v (\star \alpha).
\\]
But because the form \\(\gamma \wedge \star \alpha\\) has degree \\((k+1) + (n-k) = n+1\\), it is \\(0\\). Therefore, combining the above yields
\\[
    \gamma \wedge \star(v^{\flat} \wedge \alpha)
    = (i\_v \gamma) \wedge \star \alpha
    = (-1)^{k+1} \gamma \wedge i\_v (\star \alpha).
\\]
Because this holds for all \\(\gamma\\), we conclude \\(\star(v^{\flat} \wedge \alpha) = (-1)^{k+1}i\_v (\star \alpha)\\). Indeed, this last step follows because if for \\(\omega \in \Lambda^{n-k-1}\\) we have
\\[
    0 = \gamma \wedge \omega = \langle \gamma , \star^{-1}\omega\rangle d\operatorname{vol}
\\]
for all \\(\gamma\\), then \\(\star^{-1}\omega = 0\\), hence \\(\omega = 0\\).
<div style="text-align: right"> \(\square\) </div>

Using the above lemma in the case \\(\alpha = B^{\flat}\\), we have \\(k = 1\\) and therefore
\\[
    \star(v^{\flat} \wedge B^{\flat}) = i\_v\Omega
\\]
for the \\(2\\)-form \\(\Omega := i\_v(\star B^{\flat})\\), which encodes the magnetic field. Furthermore, recall that by the definition of divergence we have
\\[
    \operatorname{div}(B) = \star^{-1} d(\star B^{\flat}) = \star^{-1} d\Omega.
\\]
Therefore, Gauss's law for magnetism that \\(\operatorname{div} B = 0\\) (i.e. there are no magnetic monopoles) is equivalent to condition that \\(\Omega\\) is closed: \\(d\Omega = 0\\).

We define a ***magnetic system*** as a Riemananian manifold \\((M, g)\\) together with a closed \\(2\\)-form \\(\Omega\\), called the ***magnetic field***. Under such a magnetic system, a charged particle (of unit charge and unit mass) has trajectory \\(\gamma(t)\\) satisfying the ***Lorentz-Newton equation***
\\[
    D\_t \dot{\gamma}(t) = Y\_{\gamma(t)}(\dot{\gamma}(t))
\\]
for magnetic force \\(Y: TM \to TM\\) defined by \\(Y\_x(v) = (i\_v\Omega)^{\sharp}\\). The resulting flow \\(\varphi\_t: TM \to TM\\) over the phase space is called the ***magnetic flow***.

## Magnetic flow as a Lagrangian System

Next, we would like to express a magnetic system over manifold \\((M, g)\\) with magnetic field \\(\Omega\\) as a *Lagrangian system*. That is, we would like to find a Lagrangian \\(L: TM \to \mathbb{R}\\) such that the Lorentz-Newton equation is equivalent to the *Euler-Lagrange equation*
\\[
    \left(\frac{\partial L}{\partial x^i} - \frac{d }{d t} \frac{\partial L}{\partial v^i}\right)dx^i = 0
\\]
Recall that by the same computations as in the derivation of the *geodesic equation* we would find that for the kinetic energy \\(K(x,v) = \frac{1}{2}g\_x(v,v)\\) we have
\\[
    \left(\frac{\partial K}{\partial x^i}(\gamma(t), \dot{\gamma}(t)) - \frac{d }{d t} \frac{\partial K}{\partial v^i}(\gamma(t), \dot{\gamma}(t)) \right)dx^{i}
    = \cdots 
    = -(D\_t \dot{\gamma}(t))^{\flat}.
\\]
Therefore, a Lagrangian \\(L(x,v) = K(x,v) - V(x,v)\\) would reduce to the Lorentz-Newton equation so long as we have
\\[
    \left(\frac{\partial V}{\partial x^i} - \frac{d }{d t} \frac{\partial V}{\partial v^i} \right)dx^{i} 
    = -i\_v \Omega.
\\]
This is possible in the case \\(\Omega\\) is exact. Indeed, writing \\(\Omega = d\alpha\\), compute the right-hand side of the above in coordinates to be
\\[
    -i\_v d\alpha 
    = -i\_v \left( \frac{\partial \alpha\_j}{\partial x^i} -\frac{\partial \alpha\_i}{\partial x^j}\right)(dx^i \wedge dx^j)
    = \left( \frac{\partial \alpha\_j}{\partial x^i} -\frac{\partial \alpha\_i}{\partial x^j}\right) v^j dx^i.
\\]
Therefore, the choice of potential \\(V(x,v) = \alpha\_x(v) = \alpha\_i v^i\\) works because
\\[
\begin{align}
    \left(\frac{\partial V}{\partial x^i} - \frac{d }{d t} \frac{\partial V}{\partial v^i} \right)dx^{i}
    = \left( \frac{\partial \alpha\_j}{\partial x^i}v^j - \frac{d }{d t} \alpha\_i \right)dx^i
    = \left( \frac{\partial \alpha\_j}{\partial x^i}v^j - \frac{\partial \alpha\_i}{\partial x^j} \dot{x}^j \right)dx^i
    = \left( \frac{\partial \alpha\_j}{\partial x^i} - \frac{\partial \alpha\_i}{\partial x^j} \right) v^j dx^i
\end{align}
\\]
In summary, given a magnetic system over a Riemannian manifold \\((M, g)\\) such that the magnetic field \\(\Omega = d\alpha\\) is exact, then this is a Lagrangian system with Lagranian
\\[
    L(x,v) = K(x,v) - V(x,v) = \frac{1}{2}g\_x(v,v) - \alpha\_x(v).
\\]

## Magnetic flow as a Hamiltonian System

<!-- TODO: REDO A LOT OF THIS AND ALSO HAMILTONIAN MECHANICS AND SYMPLECTIC GEOMETRY PART... I AM IMPLICITLY USING THE IDENTIFICATION BETWEEN TANGENT AND COTANGENT SPACE PROVIDED BY THE METRIC WHEN I WRITE dx^i BUT I SHOULD BE USING THE IDENTIFICATION PROVIDED BY THE LEGENDRE TRANSFORM. I.E. I GET NEW COORDINATES FL(\partial_i), WHICH IS WHAT I SHOULD BE USING....

TRY TO WRITE THESE NEW COORDINATES BY p_i \varepsilon^i perhaps?
 -->

Now, we would like to express a magnetic system over manifold \\((M, g)\\) with magnetic field \\(\Omega\\) as a *Hamiltonian system*. In the case \\(\Omega = d\alpha\\) is exact, we know the magnetic system is modeled by a Lagrangian system with Lagrangian
\\[
    L(x,v) = K(x,v) - V(x,v) = \frac{1}{2}g\_x(v,v) - \alpha\_x(v).
\\]
/\*TODO: justify the Legendre transform will be a diffeomorhism, or note this is a positive-definite quadratic form, etc\*/

The resulting Hamiltonian system is therefore given by Hamiltonian
\\[
    H(x, \xi) = \langle v(x, \xi) , \xi\rangle - L(x, v(x, \xi))
\\]
for \\(v(x, \xi) = \mathbb{F}L^{-1}(x, \xi) = \mathbb{F}H(x, \xi)\\). To compute the Hamiltonian, first compute \\(\xi(x,v) =  \mathbb{F}L(x,v)\\):
\\[
    \xi(x,v)
    = \frac{\partial L}{\partial v^i}dx^i
    = (g\_{ij} v^j - \alpha\_i) dx^i
    = v\_{\flat} - \alpha.
\\]
Consequently, \\(v(x, \xi) = \xi^{\sharp} + \alpha^{\sharp}\\).
Therefore, the Hamiltonian is given by
\\[
\begin{align}
    H(x, \xi) 
    &= \langle v(x, \xi) , \xi\rangle - L(x, v(x, \xi))\\\\\
    &= \langle \xi^{\sharp} + \alpha^{\sharp} , \xi\rangle - \frac{1}{2} g(\xi^{\sharp} + \alpha^{\sharp}, \xi^{\sharp} + \alpha^{\sharp}) + \alpha(\xi^{\sharp} + \alpha^{\sharp})\\\\\
    &= g(\xi + \alpha, \xi) - \frac{1}{2} g(\xi + \alpha, \xi + \alpha) + g(\xi + \alpha, \alpha)\\\\\
    &= \frac{1}{2} g(\xi + \alpha, \xi + \alpha).
<!-- 
    &= g\_x(v(x, \xi), v(x, \xi)) - \alpha(v(x, \xi)) - \frac{1}{2}g\_x(v(x, \xi),v(x, \xi)) + \alpha(v(x, \xi))\\\\\
    &= \frac{1}{2}g\_x(v(x, \xi), v(x, \xi)) -->
\end{align}
\\]
Thus the Hamiltonian system for a magnetic system over a Riemannian manifold \\((M, g)\\) with exact magnetic field \\(\Omega = d\alpha\\) is modeled with Hamiltonian \\(H: T^*M \to \mathbb{R}\\) defined by
\\[
    H(x, \xi) = \frac{1}{2} g(\xi + \alpha, \xi + \alpha).
\\]

## Twisted Symplectic Structure

By the above derivation of the Hamiltonian for a magnetic field, we can model a magnetic system over Riemannian manifold \\((M, g)\\) with exact magnetic field \\(\Omega = d\alpha\\) as a Hamiltonian system over the cotangent bundle \\(\pi: T^\*M \to M\\) with canonical symplectic form \\(\omega\\) and Hamiltonian \\(H: T^\*M \to \mathbb{R}\\) given by
\\[
    H(x, \xi) = \frac{1}{2} g(\xi + \alpha, \xi + \alpha).
\\]
Now consider the vector bundle isomorphism \\(\Phi: T^\*M \to T^\*M\\) defined by
\\[
    \Phi: (x, p) \to (x, p - \alpha), \quad\quad \Phi^{-1}: (x, \xi) \to (x, \xi + \alpha).
\\]
The pullback of the Hamiltonian under this isomorphism simplifies to
\\[
    (\Phi^\* H)(x, p) = H(x, p - \alpha) = \frac{1}{2} g(p, p).
\\]
Then the canonical symplectic form \\(\omega = -d\tau\\) for tautological \\(1\\)-form \\(\tau\_{(x, \xi)} = d\pi\_{(x, \xi)}^\* \xi\\) pulls back under this isomorphism to
\\[
\begin{align}
    (\Phi^\*\omega)(x, p)
    = -d(d\pi^\* \Phi^\* p)
    = -d(d\pi^\*(p - \alpha))
    = -d(d\pi^\* p - d\pi^\* \alpha)
    = \omega + d(d\pi^\* \alpha)
    = \omega + d\pi^\*\Omega
\end{align}
\\]
where we used naturality of the exterior derivative under pullbacks and \\(\Omega = d\alpha\\) in the last step. That is, \\(\Phi: (T^\*M, \omega) \to (T^\*M, \omega + d\pi^\*\Omega)\\) is a symplectomorphism. Therefore, by pulling back our original Hamiltonian system \\((T^\*M, \omega)\\) and Hamiltonian \\(H\\) under this map, we arrive at a new Hamiltonian system. Furthermore, note that while this new Hamiltonian system was derived under the assumption \\(\Omega\\) is exact, any closed \\(\Omega\\) is locally exact, so this new Hamiltonian system will locally model an arbitary closed magnetic field \\(\Omega\\) everywhere, hence globally.

In particular, we find a magnetic system over Riemannian manifold \\((M, g)\\) with magnetic field given by closed 2-form \\(\Omega\\) can be modeled as a Hamiltonian system over the symplectic manifold \\(\pi: T^\*M \to M\\) with ***twisted symplectic form*** \\(\omega + d\pi^\*\Omega\\) (where \\(\omega\\) is the canonical symplectic form) together with Hamiltonian \\(H: T^\*M \to M\\) given by \\(H(x, p) = \frac{1}{2}g(p, p)\\).

Recall the Legendre transform originally idenfied velocity \\(v\\) with \\(\xi(x, v) = v^{\flat} - \alpha\\), and recall under the symplectomorphism \\(\Phi\\), we identify \\(\xi\\) with \\(p = \xi + \alpha\\). Thus under the composition of the Legendre transform with this symplectomorphism, we identify \\(v\\) with \\(p(x,v) = v^{\flat}\\).