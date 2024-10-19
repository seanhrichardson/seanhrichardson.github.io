---
layout: page
title: Levi-Civita Connection
---

## Levi-Civita Connection

On a Riemannian manifold, there is a natural choice for which connection to use. Choosing a connection is choosing a sense of acceleration on our manifold. For a Riemannian manifold \\(M\\), a natural choice is to agree that geodesics have \\(0\\) accelertaion. Indeed, geodesics are paths that go in a "straight line" without changing velocity. Thus we would like a connection \\(\nabla\\) such that for any geodesic \\(\gamma(t)\\) we have \\(\nabla\_{\dot{\gamma}(t)}\dot{\gamma}(t) = 0\\). If we have \\(\gamma(t) = (x^1(t), \cdots, x^n(t))\\) in local coordinates, this requirement is equivalent to
\\[
\begin{align}
    0 
    &= \nabla\_{\dot{\gamma}(t)} \dot{\gamma}(t)\\\\\
    &= \nabla\_{\dot{\gamma}(t)} (\dot{x}^j(t)\partial\_j)\\\\\
    &= \dot{\gamma}(t)(\dot{x}^j(t))\partial\_j + \dot{x}^j(t)\nabla\_{\dot{\gamma}(t)} \partial\_j\\\\\
    &= \ddot{x}^j(t)\partial\_j + \dot{x}^j(t)\nabla\_{\dot{x}^i\partial\_i} \partial\_j\\\\\
    &=  (\ddot{x}^k(t) + \dot{x}^i\dot{x}^j(t)A_{ij}^k) \partial\_k.
\end{align}
\\]
That is, this is equivalent to
\\[
    \ddot{x}^k(t) + \dot{x}^i\dot{x}^j(t)A_{ij}^k = 0 \quad \text{for all } k.
\\]
Thus we want to choose our functions \\(A_{ij}^k\\) so that all geodesics satisfy the above equation. However, comparing the above equation to the geodesic equation, we realize that this will always be true if we choose \\(A_{ij}^k = \Gamma_{ij}^k\\) to be the Christoffel symbols! Therefore, on a Riemannian manifold we should define our connection in coordinates by setting
\\[
    \nabla\_{\partial\_i}\partial\_j = \Gamma_{ij}^k \partial\_k.
    \tag{C}
    \label{eq:lc-coords}
\\]
This definition, however, opens one important question: does this choice of connection rely on the choice of coordinates? The answer is no, which we will prove by later defining this natural connection in a coordinate independent way. The resulting connection is called the "Levi-Civita connection".

Recall the connection for Euclidean space \\(\mathbb{R}^n\\) is given by
\\[
    \nabla\_{X}Y = XY^i\partial\_i.
\\]
This *Euclidean connection* satisfies the product rule
\\[
    \nabla\_{Z}\langle X , Y\rangle
    = \nabla\_{X} \left(\sum_{i}X^iY^i\right)
    = \sum_{i}(XZ^i)Y^i + X^i(ZY^i)
    = \langle \nabla\_Z X , Y\rangle + \langle X , \nabla\_ZY\rangle.
\\]
Additionally, observe that for any vector fields \\(X,Y\\) over \\(\mathbb{R}^n\\), we can compute the difference of the Euclidean connection \\(\nabla\_X Y - \nabla\_Y X\\) to be
\\[
   \nabla\_X Y - \nabla\_Y X
   = XY^i\partial\_i - YX^i\partial\_i
   = (XY^i - YX^i) \partial\_i. 
\\]
But this is juts the Lie bracket \\([X,Y]\\). That is, the Euclidean connection satisfies the commutator relation
\\[
    \nabla\_X Y - \nabla\_Y X = [X,Y].
    \tag{S}
    \label{eq:symmetry}
\\]

It turns out that for a Riemannian manifold \\(M\\), the Levi-Civita connection defined in local coordinates by (\ref{eq:lc-coords}) also satisfies the commutator relation (\ref{eq:symmetry}) as well as the following product rule with respect to the metric \\(g\\).
\\[
    \nabla\_Z\langle X , Y\rangle\_g = \langle \nabla\_Z X , Y\rangle\_g + \langle X , \nabla\_Z Y\rangle\_g.
    \tag{M}
    \label{eq:compatibility}
\\]
A connection satisfying (\ref{eq:symmetry}) is called *symmetric* and a connection satisfying the product rule (\ref{eq:compatibility}) is said to be *compatible with the metric*. We begin by showing the symmetry which is simply a coordinate computation.

**Prop.** The Levi-Civita connection as defined in coordinates by (\ref{eq:lc-coords}) is symmetric.

*Proof.* Compute
\\[
\begin{align}
    \nabla\_X Y - \nabla\_Y X
    &= \nabla\_{X^i \partial\_i}(Y^j \partial\_j) - \nabla\_{Y^j\partial\_j}(X^i \partial\_i)\\\\\
    &= X^i((\partial\_iY^j)\partial\_j + Y^j \nabla\_{\partial\_j}\partial\_i)
    -  Y^j((\partial\_jX^i)\partial\_i + X^i \nabla\_{\partial\_i}\partial\_j)\\\\\
    &= (XY^j\partial\_j - YX^i\partial\_i) + X^iY^j(\nabla\_{\partial\_j}\partial\_i - \nabla\_{\partial\_i}\partial\_j)\partial\_k\\\\\
    &= [X,Y] + X^iY^j(\Gamma\_{ij}^k - \Gamma\_{ji}^k)\partial\_k.
\end{align}
\\]
Then the result follows from \\(\Gamma\_{ij}^k = \Gamma\_{ji}^k\\) which we can see from the definition of Christoffel symbols:
\\[
    \Gamma\_{ij}^k = \frac{1}{2}g^{kl}(\partial\_ig\_{jl} + \partial\_jg\_{li} - \partial\_lg\_{ij})
\\]
<div style="text-align: right"> \(\square\) </div>

Next we show the Levi-Civita connection as defined in coordinates is compatible with the metric, which follows from a substantially longer coordinate computation.

**Prop.** The Levi-Civita connection as defined in coordinates by (\ref{eq:lc-coords}) is compatible with the metric.

*Proof.* First we expand out the right side of (\ref{eq:compatibility}).
\\[
\begin{align}
    \langle \nabla\_Z X , Y\rangle + \langle X , \nabla\_Z Y\rangle
    &= \langle \nabla\_{Z^k \partial\_k}(X^i \partial\_i) , Y^j\partial\_j \rangle
    + \langle X^i \partial\_i , \nabla\_{Z^k \partial\_k}(Y^j \partial\_j)\rangle\\\\\
    &= Z^k(Y^j\langle \partial\_k X^i\partial\_i + X^i \nabla\_{\partial\_k}\partial
    \_i , \partial\_j\rangle
    + X^i\langle \partial\_i , \partial\_kY^j \partial\_j + Y^j \nabla\_{\partial\_k}\partial\_j\rangle)\\\\\
    &= Z^k(Y^j\langle (\partial\_kX^l + X^i\Gamma_{ik}^l)\partial\_l , \partial\_j\rangle
    + X^i \langle \partial\_i , (\partial\_kY^l + Y^j\Gamma\_{kj}^l)\partial\_l\rangle)\\\\\
    &= Z^kY^j(\partial\_kX^l + X^i\Gamma\_{ik}^l)g\_{lj}
    + Z^kX^i(\partial\_kY^l + Y^j\Gamma\_{kj}^l)g\_{il}\\\\\
    &= Z^k(Y^j\partial\_kX^lg\_{lj} + X^i\partial\_kY^l g\_{il}) + Z^kX^iY^j(\Gamma\_{ik}^lg\_{lj} + \Gamma\_{kj}^lg\_{il}).
\end{align}
\\]
Next we expand out the left size of (\ref{eq:compatibility}). 
\\[
    \nabla\_Z\langle X , Y\rangle
    = Z^k \partial\_k\langle X^i \partial\_i , Y^j \partial\_j\rangle
    = Z^k \partial\_k(X^i Y^j g\_{ij})
    = Z^k(Y^j\partial\_kX^ig\_{ij} + X^i\partial\_kY^jg\_{ij})
    + Z^kX^iY^j\partial\_kg\_{ij}.
\\]
Note these expansions are quite similar, and we see that in fact the right and left sides of (\ref{eq:compatibility}) are equal so long as we can show
\\[
    \partial\_kg\_{ij} = \Gamma\_{ik}^lg\_{lj} + \Gamma\_{kj}^lg\_{il}.
\\]
Indeed, to show this we use the definition of the Christoffel symbols
\\[
    \Gamma\_{ij}^k = \frac{1}{2}g^{kl}(\partial\_ig\_{jl} + \partial\_jg\_{li} - \partial\_lg\_{ij})
\\]
and apply the matrix \\(g\_{km}\\) to both sides to conclude
\\[
    \Gamma\_{ij}^k g\_{km} = \frac{1}{2}(\partial\_ig\_{jm} + \partial\_jg\_{mi} - \partial\_mg\_{ij}).
\\]
Thus using the above expression twice we can compute
\\[
    \Gamma\_{ik}^lg\_{lj} + \Gamma\_{kj}^lg\_{il}
    = \frac{1}{2}(\partial\_ig\_{kj} + \partial\_kg\_{ji} - \partial\_jg\_{ik})
    + \frac{1}{2}(\partial\_kg\_{ji} + \partial\_jg\_{ik} - \partial\_ig\_{kj})
    = \partial\_kg\_{ij}
\\]
as needed.
<div style="text-align: right"> \(\square\) </div>

It turns out that these two properties -- symmetry and metric compatibility -- are quite special. In fact, on a Riemannian manifold there will only be one connection that satisfies both properties.

**Prop. (Fundamental Theorem of Riemannian Geometry).** For any Riemannian manifold \\(M\\), there exists a unique connection \\(\nabla\\) that is both symmetric and compatible with the metric. This connection is called the *Levi-Civita connection*.

*Proof.* /\*TODO: follow Lee\*/