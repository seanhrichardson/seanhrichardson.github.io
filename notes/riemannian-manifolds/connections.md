---
layout: page
title: Connections
section: Connections
---

# Connections

## Differentiating vector fields in \\(\mathbb{R}^n\\)

Given a path \\(\gamma(t)\\) in \\(\mathbb{R}^n\\), we know we can represent its velocity by
\\[
    \dot{\gamma}(t) = \dot{\gamma}^i(t) \partial\_i.
\\]
Furthermore, in the case of \\(\mathbb{R}^n\\), we understand the acceleration of the curve \\(\gamma(t)\\) to be given by
\\[
    \ddot{\gamma}(t) = \frac{d }{d t}\left(\dot{\gamma}^i(t) \partial\_i\right) = \ddot{\gamma}^i(t) \partial\_i.
\\]
In computing the acceleration, we are differentiating a vector field. More generally in \\(\mathbb{R}^n\\), we understand the derivative of some vector field \\(X\\) in the direction \\(v \in T\_p\mathbb{R}^n\\) at point \\(p\\), which we denote \\(\nabla\_v X\\), to be
\\[
    \nabla\_v X = \left.\frac{d }{d t}\right\|\_{t=0}X(\gamma(t)) = \left.\frac{d }{d t}\right\|\_{t=0}X^i(\gamma(t))\partial\_i = v(X^i)\partial\_i.
\\]
where \\(\gamma(t)\\) is a smooth curve such that \\(\dot{\gamma}(0) = v\\). This directional derivative enjoys the following nice properties:

1. First, the directional derivative is linear with respect to the direction. Indeed, for any vectors \\(v,w\\) based at point \\(p \in \mathbb{R}^n\\), real numbers \\(a,b\\), and vector field \\(X\\) we find
\\[
    \nabla\_{av + bw}X
    = (av + bw)X^i \partial\_i
    = avX^i\partial\_i + bwX^i\partial\_i
    = a\nabla\_vX + b\nabla\_wX.
\\]
2. Second, this directional derivative is linear with respect to the vector fields. Indeed, for any vector \\(v\\) based at \\(p \in \mathbb{R}^n\\), any real numbers \\(a,b\\), and any vector fields \\(X,Y\\) that
\\[
    \nabla\_v(aX + bY)
    = v(aX^i + bY^i)\partial\_i
    = avX^i\partial\_i + bvY^i\partial\_i
    = a\nabla\_vX + b\nabla\_vY
\\]
3. Finally, we have a product rule. For any vector \\(v\\) at point \\(p \in \mathbb{R}^n\\), vector field \\(X\\), and smooth function \\(f\\) we find
\\[
    \nabla\_v(fX)
    = v(fX^i)\partial\_i
    = (vf)X^i\partial\_i + f(vX^i)\partial\_i
    = (vf)X + f\nabla\_vX
\\]

## The problem with differentiating vector fields on manifolds
However, the definition of the directional derivative of a vector field \\(X\\) in direction \\(v\\)
\\[
    \left.\frac{d }{d t}\right\|\_{t=0} X(\gamma(t)) = \lim_{t \to 0}\frac{X(\gamma(t)) - X(\gamma(0))}{t}
\\]
does not make sense on a general smooth manifold! The vectors \\(X(\gamma(t))\\) and \\(X(\gamma(0))\\) belong to the two different tangent spaces \\(T\_{\gamma(t)}M\\) and \\(T\_{\gamma(0)}M\\), so it does not make sense to subtract them. Note that in the case of \\(\mathbb{R}^n\\), there is a natural identification between different tangent spaces \\(T\_p\mathbb{R}^n\\) and \\(T\_q\mathbb{R}^n\\) by simply translating the vectors. However, this a consequence of having a nice coordinate frame \\((\partial\_i)\\), for we are naturally identifying \\(v^i\partial_i \in T\_p\mathbb{R}^n\\) with \\(v^i\partial_i \in T\_q\mathbb{R}^n\\). In order to differentiate vector fields on manifolds, we need more structure on the manifold.

<!-- /\* TODO: perhaps an example demonstrating how coordinates change with respect to themselves\*/ -->

<!-- /\*emphasize that in \\(\mathbb{R}^n\\), we are using that \\(\partial_i\\) does not change with respect to \\(\partial_j\\)\*/ -->

## Connections
We are looking to define a directional derivative operation \\(\nabla\_v X\\) on a general smooth manifold. Formally, we are looking for a map \\(\nabla: T\_pM \times \Gamma(TM) \to T\_pM\\) varying smoothly with \\(p\\). If this map is denoted \\(\nabla: (v, X) \mapsto \nabla\_vX\\), we want \\(\nabla\\) to satisfy the following three properties we expect from a directional derivative. In the following, \\(a,b \in \mathbb{R}\\) are real numbers, \\(v,w \in T\_pM\\) are vectors based at \\(p\\), and \\(X,Y \in \Gamma(TM)\\) are vector fields on the manifold.

1. Linearity with respect to the direction:
\\[
    \nabla\_{av + bw}X = a\nabla\_vX + b\nabla\_wX.
\\]
2. Linearity with respect to the vector field:
\\[
    \nabla\_v(aX + bY) = a\nabla\_vX + b\nabla\_vY.
\\]
3. Product rule:
\\[
    \nabla\_v(fX) = (vf)X + f\nabla\_vX.
\\]

Such a map \\(\nabla: T\_pM \times \Gamma(TM) \to T\_pM\\) varying smoothly with \\(p\\) that satisfies the three properties above is called a *connection*. Equivalently, we can consider two vector fields \\(X,Y\\) and say \\(\nabla\_X Y\\) is vector field such that \\((\nabla\_X Y)(p) = \nabla\_{X(p)} Y\\) so that we now have a map \\(\nabla: \Gamma(TM) \times \Gamma(TM) \to \Gamma(TM)\\). The directional derivative \\((\nabla\_X Y)\\) corresponding to a connection is called the *covariant derivative* of \\(Y\\) in the direction of \\(X\\). The main question, however, is how do we choose which connection to use? In general, there are many connections on a smooth manifold: choose any coordinate frame \\((\partial\_i)\\) and decide the derivative of each coordinate frame in the direction of all the other coordinate frames at every point. That is, choose functions \\(A_{ij}^k\\) such that
\\[
    \nabla\_{\partial\_i}\partial\_j = A_{ij}^k \partial\_k.
\\]
Then given any arbitrary vector fields \\(X = X^i\partial\_i\\) and \\(Y = Y^j\partial\_j\\), we can determine what the covariant derivative \\(\nabla\_XY\\) should be by
\\[
    \nabla\_X Y 
    = \nabla\_{X^i \partial\_i}(Y^j \partial\_j)
    = X^i((\partial\_iY^j)\partial\_j + Y^j \nabla\_{\partial\_i}\partial\_j)
    = X^i(\partial\_iY^k + Y^jA_{ij}^k)\partial\_k.
    \label{eq:As}
    \tag{A}
\\]
For any smooth functions \\(A_{ij}^k\\) that we choose, the above formula in fact defines a connection.
<!-- TODO: define connection coefficients -->

**Exercise.** Verify that for any smooth functions \\(A_{ij}^k\\), the formula (\ref{eq:As}) defines a connection by checking the three necessary properties are satisfied.

Thus there are many possible connections on a general smooth manifold. For some intuition for connections, note that choosing a connection gives us a sense of acceleration on our manifold. Given a curve \\(\gamma(t)\\), it's velocity at each point along the curve is given by the tangent vectors \\(\dot{\gamma}(t)\\). Then the acceleration should be the change of \\(\dot{\gamma}(t)\\) in direction \\(\dot{\gamma}(t)\\). That is, the *acceleration* of \\(\gamma(t)\\) is defined to be \\(\ddot{\gamma}(t) = \nabla\_{\dot{\gamma}(t)}\dot{\gamma}(t)\\).