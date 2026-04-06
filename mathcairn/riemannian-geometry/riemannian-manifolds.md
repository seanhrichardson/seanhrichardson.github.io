---
layout: page
title: Riemannian Manifolds
---

<!-- TODO: -->
<!-- S^2 example -->
<!-- R^n -->
<!-- embedded manifold example -->
<!-- hide all solutions -->

# Riemannian Manifolds

Consider the unit sphere \\(\mathbb{S}^2 \subset \mathbb{R}^3\\) defined as all points \\((x,y,z)\\) with distance \\(1\\) from \\((0,0,0)\\); or equivalently, all points \\((x,y,z)\\) such that \\(x^2+y^2+z^2 = 1\\). This embedding of the sphere \\(\mathbb{S}^2\\) into Euclidean space \\(\mathbb{R}^3\\) gives the sphere *geometry*. In particular, we can explicitly compute:
1. The *length* of curves on the surface of the sphere.
2. The *angle* between intersecting curves.
3. The *area* of regions of the sphere.

/\*TODO: figure to represent the above (using explicit examples below)\*/

<!-- TODO: in video, can show the examples below visually  -->

**Warmup.** Find the length of the equator of the unit sphere. Note the equator can be parametrized by \\(\alpha(t) = (\cos t, \sin t, 0)\\) parametrized over \\(0 \leq t \leq 2\pi\\).

**Solution.** First note the length of the equator is \\(2\pi\\) as it is the circumference of a circle of radius \\(1\\). For later use, though, recall the multivariable calculus approach is to compute the length of \\(\alpha\\) by
\\[
    \operatorname{Length}(\alpha) = \int\_0^{2\pi} \|\alpha'(t)\| dt.
\\]
Then recall the velocity vector is given by
\\[
    \alpha'(t) 
    = \begin{pmatrix} \frac{d x}{d t} \\\\ \frac{d y}{d t}\\\\ \frac{d z}{d t}\end{pmatrix}
    = \begin{pmatrix} \frac{d }{d t} \cos t  \\\\ \frac{d }{d t} \sin t \\\\ \frac{d }{d t} 0 \end{pmatrix}
    = \begin{pmatrix} -\sin t  \\\\ \cos t \\\\ 0 \end{pmatrix}
\\]
Therefore, we can compute the length by
\\[
    \operatorname{Length}(\alpha) 
    = \int\_0^{2\pi} \|\alpha'(t)\| dt
    = \int\_0^{2\pi} \sqrt{(-\sin t)^2 + (\cos t)^2} dt
    = \int_0^{2\pi} 1 dt = 2\pi.
\\]

**Exercise.** Find the angle between the equator of the unit sphere and the "prime meridian" \\(\beta(t) = (\cos t, 0, \sin t)\\) parametrized over \\(0 \leq t \leq \pi\\).

**Solution.** Note \\(\alpha\\) lies in the plane \\(z = 0\\) while \\(\beta\\) lies in the plane \\(y = 0\\) and the angle between these planes, and hence the angle between the curves, is \\(\pi/2\\). Alternatively, we can compute the angle \\(\theta\\) between the velocity vectors at the intersection \\(\alpha(0) = (1, 0, 0) = \beta(0)\\). First we compute the velocity vectors themselves beginning with \\(\alpha'(0)\\):
\\[
    \alpha'(0) 
    = \left.\begin{pmatrix} \frac{d x}{d t} \\\\ \frac{d y}{d t} \\\\ \frac{d z}{d t} \end{pmatrix}\right\|\_{t=0}
    = \left.\begin{pmatrix} \frac{d }{d t}\cos t \\\\ \frac{d \sin t}{d t} \\\\ \frac{d }{d t} 0 \end{pmatrix}\right\|\_{t=0}
    = \left.\begin{pmatrix} -\sin t \\\\ \cos t \\\\ 0 \end{pmatrix}\right\|\_{t=0}
    = \begin{pmatrix} 0 \\\\ 1 \\\\ 0 \end{pmatrix}.
\\]
In the same way we compute \\(\beta'(0)\\):
\\[
    \alpha'(0) 
    = \left.\begin{pmatrix} \frac{d x}{d t} \\\\ \frac{d y}{d t} \\\\ \frac{d z}{d t} \end{pmatrix}\right\|\_{t=0}
    = \left.\begin{pmatrix} \frac{d }{d t}\cos t \\\\ \frac{d }{d t} 0  \\\\ \frac{d \sin t}{d t} \end{pmatrix}\right\|\_{t=0}
    = \left.\begin{pmatrix} -\sin t \\\\ 0 \\\\ \cos t \end{pmatrix}\right\|\_{t=0}
    = \begin{pmatrix} 0 \\\\ 0 \\\\ 1 \end{pmatrix}.
\\]
Now we can compute the dot product \\(\alpha'(0) \cdot \beta'(0) = 0\\) and see these vectors are perpendicular, so the angle between them is \\(\pi/2\\). We can explicitly compute this by recalling the angle \\(\theta\\) between these the tangent vectors \\(\alpha'(0)\\) and \\(\beta'(0)\\) satisfies
\\[
    \cos \theta 
    = \frac{\langle \alpha'(0), \beta'(0) \rangle}{\|\alpha'(0)\|\|\beta'(0)\|}
    = 0
\\]
where we used \\(\alpha'(0) \cdot \beta'(0) = 0\\). Thus by \\(\cos \theta = 0\\) we conclude \\(\theta = \pi/2\\).

<!-- TODO: link to the smooth manifold page... -->
Recall the sphere \\(\mathbb{S}^2 \subset \mathbb{R}^3\\) has the structure of a smooth manifold. 

/\*TODO... commentary/review of intrinsic smooth manifold structure, emphasizing it does not encode geometry and motivating this intrinsic framework/philosophy.... note the sphere loses this geometry...\*/

The idea behind a Riemannian manifold is a smooth manifold with additional structure that encodes geometric data such as lengths, angles, and areas. As we saw in the above exercises, the tangent vectors of curves (i.e. the velocity vectors) are key to computing lengths and angles. Over a smooth manifold \\(M\\), recall the vector space of all tangent vectors based at point \\(p \in M\\) is called the "tangent space" \\(T\_pM\\), which we can visualize as the plane tangent to the surface at \\(p\\).

/\*visual for the tangent space\*/

Note the angle between two curves \\(\alpha, \beta\\) over \\(M \subset \mathbb{R}^n\\) intersecting at \\(\alpha(0) = p = \beta(0)\\) is the angle between the tangent vectors \\(\alpha'(0), \beta'(0) \in T\_p M\\).

/\*visual for the above\*/

Similarly, recall the length of a curve \\(\gamma \colon [0, 1] \to M \subset \mathbb{R}^n\\) can be computed by integrating the speed of the curve over time.
\\[
    \operatorname{Length}(\gamma) = \int\_0^1 \|\gamma'(t)\| dt.
\\]

That is, to compute the geometric information such as the angle between curves or the length of a curve, we only need the lengths and angles between tangent vectors. Recall the length \\(\|v\|\\) of a vector and the angle \\(\theta\\) between vectors \\(v,w\\) is given by the inner product:
\\[
    \|v\|^2 = \langle v , v\rangle,
    \quad \quad \quad
    \cos \theta = \frac{\langle v , w\rangle}{\|v\|\|w\|}.
\\]
Therefore, an inner product on every tangent space defines lengths and angles in the tangent space, which in turn defines lengths of curves and the angle between curves. A Riemannian manifold is simply a smooth manifold with precisely this extra structure. A ***Riemannian metric*** \\(g\\) over a smooth manifold \\(M\\) is an inner product \\(g\_p: T\_p M \times T\_p M \to \mathbb{R}\\) for all \\(p \in M\\), varying smoothly with \\(p\\). The pair \\((M, g)\\) is called a ***Riemannian manifold***.

**Example.** Consider the standard representation of the sphere \\(\mathbb{S}^2\\) as a subset of \\(\mathbb{R}^3\\). That is, we consider the standard embedding \\(i: \mathbb{S}^2 \to \mathbb{R}^3\\) of smooth manifolds. Then for any point \\(x \in \mathbb{S}^2\\) and \\(v, w \in T\_x \mathbb{S}^2\\), this embedding allows us to represent these tangent vectors as living in \\(\mathbb{R}^3\\), which we write by \\(di\_x v\\) and \\(d i\_x w\\). Then we define the ***standard spherical metric*** \\(g^{\circ}\\) so that the inner product between \\(v\\) and \\(w\\) is the inner product between their corresponding vectors in \\(\mathbb{R}^3\\):
\\[
    g^{\circ}\_x(v, w) = \langle v , w\rangle = \langle di\_x v , di\_x w \rangle.
\\]
Note that because the inner product \\(\langle \cdot , \cdot \rangle\\) on \\(\mathbb{R}^3\\) is linear, symmetric, and positive-definite, \\(g^{\circ}\\) will also satisfy these properties and therefore will be an inner product at each point. Furthermore, note \\(g^{\circ}\_x\\) is defined as the composition of smooth functions and therefore will vary smoothly with \\(x\\). Therefore, \\(g^{\circ}\\) is a Riemannian metric and the pairing \\((\mathbb{S}^2, g)\\) is a Riemannian manifold.
<!-- TODO: note on why this is an inner product and why this "varies smoothly" -->
<span style="float: right"> // </span>

A quick comment on notation: given a Riemannian manifold \\((M, g)\\) and tangent vectors \\(v, w \in T\_p M\\), it is common to denote \\(g\_p(v,w)\\) as simply \\(g(v,w)\\) or as \\(\langle v , w\rangle\_g\\). Furthermore, "Riemannian metric" is often abbreviated to just "metric" in the field of Riemannian geometry in contexts when there is no risk of confusing this with the metric in a metric space (which is defined differently, but is related).

**Example.** Next consider Euclidean space \\(\mathbb{R}^n\\), which given coordinates \\((x^1, \cdots, x^n)\\), we can make into a Riemannian manifold by consiering the usual dot product. To formally define this in the language of smooth manifolds, consider the coordinate frame \\((\partial\_{x^1}, \cdots, \partial\_{x^n})\\) where each \\(\partial\_{x^i}\\) is the vector field where all vectors point are of unit length and pointing in the \\(x^i\\) direction.

/\*TODO: pictures\*/

Then we can write any two tangent vectors \\(v, w \in T\_x \mathbb{R}^n\\) by
\\[
    v = \sum_{i=1}^n v^i \partial\_{x^i} \quad \quad \text{and} \quad \quad w = \sum_{i=1}^n w^i \partial\_{x^i}.
\\]
This allows for us to define the ***Euclidean ***

then we define \\(\langle v , w\rangle\_g = \sum_{i = 1}^n v^i w^i\\), which is just the standard dot product.

<!-- TODO: some comment on the folllowing example? i.e. -->

**Example.** Suppose we have a smooth manifold \\(M\\) and any smooth embedding \\(i: M \to \mathbb{R}^n\\). Then for any 

/\*TODO: embedded submanifold of \\(\mathbb{R}^n\\)\*/

/\*TODO: talk about \\(g\\) as a 2-tensor field... perhaps denote bundle it is a field over?\*/