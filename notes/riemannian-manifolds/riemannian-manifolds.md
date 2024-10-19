---
layout: page
title: Riemannian Manifolds
---

## Riemannian Manifolds

Consider the sphere as a subset of Euclidean space \\(\mathbb{S}^2 \subset \mathbb{R}^3\\). This extrinsic description of the sphere gives the sphere *geometry*. In particular,
1. We can compute the *length* of a path \\(\gamma: [0,1] \to \mathbb{S}^2\\).
2. If \\(\alpha, \beta: \mathbb{R} \to \mathbb{S}^2\\) are two curves that intersect on the sphere, we can calculate the *angle* that they meet at.
3. Regions of \\(\mathbb{S}^2\\), such as the upper hemisphere, have an *area*.

/\*give pictures\*/

The framework of smooth manifolds allows us to intrinsically study the topology and smooth structure of the sphere, but provides no way to encode the geometric information that is provided by the extrinsic description. The notion of a *Riemannian manifold* is a smooth manifold with some extra structure that encodes geometry. Before giving the definition, let's investigate what extra structure we need to give to a smooth manifold \\(M\\) to describe this geometry.

Let's begin by considering angles. If the two curves \\(\alpha, \beta: \mathbb{R} \to \mathbb{S}^2 \subset \mathbb{R}^3\\) intersect at \\(\alpha(0) = \beta(0)\\), then the angle of their intersection is defined by the angle between the extrinsic tangent vectors \\(\alpha'(0)\\) and \\(\beta'(0)\\) /\*picture\*/. We can take motivation from this for the general case of an intrinsically defined smooth manifold \\(M\\). Consider curves \\(\alpha, \beta: \mathbb{R} \to M\\) intersecting at \\(\alpha(0) = \beta(0) = p \in M\\), noting the tangent vectors \\(\alpha'(0)\\) and \\(\beta'(0)\\) are elements of the same tangent space \\(T_p(M)\\). We wish we could define the angle of intersection between \\(\alpha\\) and \\(\beta\\) to be the angle between \\(\alpha'(0)\\) and \\(\beta'(0)\\), which we could do with some extra structure that defines the angles of between vectors in the tangent space.

Next recall that the length of a curve \\(\gamma: [0,1] \to \mathbb{S}^2 \subset \mathbb{R}^3\\) is calculated extrinsically by
\\[
    \operatorname{Length}(\gamma) = \int_{0}^1 \|\gamma'(s)\|ds
    \label{eq:length}
    \tag{1}
\\]
where \\(|\gamma'(s)|\\) is the length of the extrinsic tangent vector \\(\gamma'(s) \subset \mathbb{R}^3\\). Taking motivation from this, then given our smooth manifold \\(M\\), if we have a notion of lengths of tangent vectors, then we could *define* the length of a curve \\(\gamma: [0,1] \to M\\) by (\ref{eq:length}). Thus the length of tangent vectors also encodes important geometry. 

To summarize, the lengths of tangent vectors and angles between tangent vectors encodes the geometry of lengths and angles between curves. From linear algebra, recall that an *inner product* on a vector space provides a notion of lengths and angles between vectors. Thus the extra structure we want to give our manifold \\(M\\) to describe geometric features is an inner product on each tangent space \\(T_p(M)\\) for all \\(p \in M\\). This inner product \\(g\_p: T\_pM \times T\_pM \to \mathbb{R}\\) is called a *Riemannian metric* \\(g\\), which we are now ready to define.

**Def. (Riemannian metric).** A *Riemannian metric* on a smooth manifold \\(M\\) is an inner product \\(g\_p: T\_pM \times T\_pM \to \mathbb{R}\\) for all \\(p \in M\\) that varies smoothly with \\(p\\) (for all smooth vector fields \\(X,Y\\) on \\(M\\), the function \\(g_p(X,Y): M \to \mathbb{R}\\) is smooth).

Given tangent vectors \\(v, w \in T\_pM\\), the inner product \\(g\_p(v,w)\\) is also denoted by \\(\langle v , w\rangle\_g\\). Similarly, the norm \\(\sqrt{g\_p(v,v)}\\) of a vector is often denoted by \\(\|v\|\_g\\). Recall that inner products are covariant 2-tensors. /\*smooth this out\*/ Indeed, in our case the Riemannian metric is a bilinear map \\(g\_p: T\_pM \times T\_pM \to \mathbb{R}\\) and therefore, by universal property of the tensor product, can be interpreted as a linear function \\(g\_p: T\_pM \otimes T\_pM \to \mathbb{R}\\). Furthermore, because this function varies smoothly with time, this defines a smooth covariant 2-tensor field \\(g\\) on \\(M\\). This motivates the following alternate definition of the Riemannian metric, which makes our smooth manifold theory more useful.

**Def. (Riemannian metric).** A *Riemannian metric* on a smooth manifold \\(M\\) is a smooth, covariant 2-tensor field \\(g\\) whose value \\(g\_p\\) at each \\(p \in M\\) is an inner product on \\(T_pM\\).

**Exercise.** Prove that both definitions of a Riemannian metric are equivalent.

When a smooth manifold \\(M\\) is given the extra structure of a Riemannian metric \\(g\\), we get a *Riemannian manifold* -- the object that the subject of *Riemannian geometry* studies. This data is often written as the pair \\((M,g)\\).

**Def. (Riemannian manifold).** A smooth manifold \\(M\\) together with a Riemannian metric \\(g\\) is called a *Riemannian manifold*.

The notion of a Riemannian manifold is a way to intrinsically define geometric objects just as we hoped. We are now ready to jump into the field of Riemannian geometry.

