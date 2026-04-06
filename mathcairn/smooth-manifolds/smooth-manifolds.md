---
layout: page
title: Smooth Manifolds
section: NOTES
---

# Smooth Manifolds

## Motivating the extrinsic definition

Smooth manifolds arise as "smooth" subsets of \\(\mathbb{R}^m\\) that locally "look like" \\(\mathbb{R}^n\\) such as the following examples:

/\*TODO: give some pictures and examples of manifolds\*/
<!-- sphere, torus, plane R^2 \subset R^3,  -->

Smooth manifolds are designed so that we can do calculus over these manifolds in the same way we do calculus over \\(\mathbb{R}^n\\). For example, consider a path \\(\gamma: \mathbb{R} \to \mathbb{S}^2 \subset \mathbb{R}^3\\) and a function \\(f: \mathbb{R}^3 \to \mathbb{R}\\). Then by multivariable calculus methods, we may compute \\(\frac{d }{d t} (f \circ \gamma)(t)\\).

**Exercise.** Compute \\(\frac{d }{d t} (f \circ \gamma)(t)\\) for \\(f(x,y,z) = z\\) and \\(\gamma(t) = (\cos t, 0, \sin t)\\) using the chain rule.
<!-- TODO... also perhaps comment we *could* directly compute f \circ \gamma first, but this avoids doing calculus "on" the sphere -->

Note in the computation above, we use the chain rule 
\\[\frac{d }{d t} f(x(t), y(t), z(t)) = \frac{\partial f}{\partial x} \frac{d x}{d t} + \frac{\partial f}{\partial y} \frac{d y}{d t} + \frac{\partial f}{\partial z} \frac{d z}{d t},\\]
which only works because the derivative of the curve \\(\gamma'(t) = (x'(t), y'(t), z'(t))\\) exists, which is related to what we mean by "smooth". In contrast, consider the cone \\(z(x,y) = 1 - \sqrt{x^2 + y^2}\\), which has the "sharp point" \\((0,0,1)\\):

/\*TODO: picture of cone\*/

In this example, there are not as many differentiable curves staying on the surface of the cone and passing through this "sharp point" as we would expect in \\(\mathbb{R}^n\\). For example, the curve \\(\gamma(t) = (t, 0, 1 - \|t\|)\\) passes through \\((0,0,1)\\), but is not differentiable at \\(t = 0\\).

**Exercise.** Verify \\(\gamma(t) = (t, 0, 1 - \|t\|)\\) is not differentiable at \\(t = 0\\).

**Exercise.** Find a differentiable curve \\(\gamma(t)\\) on the surface of the cone that passes through \\((0,0,1)\\).

<!-- give visual hint of such a function in the video -->
 
This sharp point makes it difficult to do calculus on the surface of the cone and therefore we do not want to include this in our definition of smooth manifold. Some other problematic surfaces we want to avoid are the following:

/\*TODO: some more non-example pictures.\*/

This is in contrast to the sphere, torus, and plane, which do not have any problematic points, allowing us to do calculus on these surfaces in the same way we do calculus on \\(\mathbb{R}^2\\). In fact, the reason we can do calculus in the same way as \\(\mathbb{R}^2\\) is that we can locally identify each of these surfaces with \\(\mathbb{R}^2\\) in a way that respects differentiation, which allows us to do calculus on each of these surfaces as though it literally is \\(\mathbb{R}^2\\). For example, in the case of the sphere, we consider the *spherical coordinates* map
\\[
    G(r, \theta, \phi) = (r\sin\phi\cos\theta, r\sin\phi\sin\theta, r\cos\phi)
\\]

/\*TODO: animation of this map\*/

In particular, note these coordinates map the plane \\(\\{(r, \theta, \phi): r = 1, \theta \in (0, 2\pi), \phi \in (0, \pi)\\}\\) to (most of) the sphere \\(\mathbb{S}^2 \subset \mathbb{R}^3\\).

/\*TODO: animate mapping to sphere?\*/

Furthermore, if we restrict to \\(\theta \in (0, 2\pi)\\) and \\(\phi \in (0, \pi)\\), then this spherical coordinates map is a bijection onto its image and has a well-defined inverse.

**Exercise.** Find the inverse to the spherical coordinates map \\(G(r, \theta, \phi)\\).

Roughly, the inverse to the spherical coordinates map is given by
\\[
    F(x, y, z) = (\sqrt{x^2 + y^2 + z^2}, \arctan(y/x), \arccos(z/\sqrt{x^2+y^2+z^2}))
\\]
Technically, the above is only valid for \\(\theta \in [0, \pi/2)\\) /\*note on the \\(\theta\\) argument and maybe define \\(\operatorname{atan2}\\)\*/

<!-- perhaps specify domain below... -->
<!-- \\(F: \mathbb{R}^2 \smallsetminus \\{(x,y,z) : x \geq 0, y = 0\\} \to (0, \infty) \times (0, 2\pi) \times (0, \pi)\\). -->
This map \\(F\\) allows for an identification between the sphere \\(\mathbb{S}^2\\) and the flat plane \\(\\{(r,\theta,\phi) : r = 1, \theta \in (0, 2\pi), \phi \in (0, \pi)\\}\\), which allows us to (locally) do calculus on \\(\mathbb{S}^2\\) as if it were simply \\(\mathbb{R}^2\\). Indeed, denote \\(G\\) by \\(F^{-1}\\) and let \\(f(x,y,z) = z\\) and \\(\gamma(t) = (\cos t, 0, \sin t)\\) be the same curves from above. Earlier, we computed the derivative of \\(f \circ \gamma\\), but note we can rewrite this composition as
\\[
    f \circ \gamma = (f \circ F^{-1}) \circ (F \circ \gamma) = \widetilde{f} \circ \widetilde{\gamma}
\\]
where \\(\widetilde{\gamma} := F \circ \gamma\\) and \\(\widetilde{f} := f \circ F^{-1}\\). In particular, the curve \\(\widetilde{\gamma}\\) maps into the flat plane \\(\\{(r,\theta,\phi) : r = 1, \theta \in (0, 2\pi), \phi \in (0, \pi)\\}\\) and the function \\(\widetilde{f}\\) takes this same space as input. That is, this identification \\(F\\) allows us to work entirely in \\((r, \theta, \phi)\\) coordinates where the sphere is simply a flat plane. 

/\*TODO: picture of all mappings \\(\widetilde{f}, f, \widetilde{\gamma}, \gamma, F, F^{-1}\\) in commutative diagram\*/

/\*TODO: make the below an exercise\*/
Under this identiciation, \\(\widetilde{f}\\) is
\\[
    \widetilde{f}(r, \theta, \phi) 
    = f(F^{-1}(r, \theta, \phi)) 
    = F(r\sin\phi\cos\theta, r\sin\phi\sin\theta, r\cos\phi)
    = r \cos \phi.
\\]

/\*TODO: make the below an exercise\*/
In the same way, the curve \\(\widetilde{\gamma}\\) is
\\[
    \widetilde{\gamma}(t)
    = F(\gamma(t))
    = F(\cos t, 0, \sin t)
    = (\sqrt{\cos^2 t + \sin^2 t}, \arctan(0), \arccos(\sin t))
    = (1, 0, t + \pi/2).
\\]
Recall we previously used the chain rule to compute \\((f \circ \gamma)'(t) = \cos t\\). Alternatively, because  \\(\widetilde{f} \circ \widetilde{\gamma} = f \circ \gamma\\), we could use \\(\widetilde{f}\\) and \\(\widetilde{\gamma}\\) to compute this same derivative.

**Exercise.** Use the chain rule to compute \\((\widetilde{f} \circ \widetilde{\gamma})'(t)\\).

As expected, because \\(\widetilde{f} \circ \widetilde{\gamma} = f \circ \gamma\\), we compute the same derivative although we are working entirely in spherical coordinates \\((r, \theta, \phi)\\), which "flattens" the sphere. The reason this identification works is that the maps \\(F\\) and \\(F^{-1}\\) are (continuously) differentiable. More generally, if we are interested in higher order derivatives, we want *all* derivatives to exist and we call such a function "smooth". Formally, a function \\(\varphi: U \to \mathbb{R}^n\\) for an open subset \\(U \subset \mathbb{R}^m\\) is ***smooth*** if all partial derivatives \\(\frac{\partial \varphi^l}{\partial x^i}, \frac{\partial^2 \varphi^l}{\partial x^i \partial x^j}, \frac{\partial^3 \varphi^l}{\partial x^i \partial x^j \partial x^k}, \cdots\\) exist and are continuous.

**Exercise.** Verify \\(F\\) and \\(F^{-1}\\) are smooth maps.

In our case *both* \\(F\\) and \\(F^{-1}\\) are smooth, which is what allows for this identificaton that respects (repeated) differentiation and allows us to perform all our calculus computation in \\((r, \theta, \phi)\\) coordinates if we like; we call such an \\(f\\) a "diffeomorphism". Formally, a map \\(\varphi: U \to V\\) between open sets \\(U, V \subset \mathbb{R}^n\\) is a ***diffeomorphism*** if it is a smooth, bijective map with smooth inverse \\(\varphi^{-1}\\). In general, it is the existence of a diffeomorphism that maps our manifold to flat \\(\mathbb{R}^n\\) space that allows us to do calculus on our manifold as if it were simply \\(\mathbb{R}^n\\).

/\*TODO: picture of generic manifold being mapped to flat plane\*/

Formally, we say a subset \\(M \subset \mathbb{R}^m\\) is a ***smooth manifold*** if every \\(p \in M\\) has a neighborhood \\(U \subset \mathbb{R}^m\\) and a diffeomorphism \\(\varphi: U \to V \subset \mathbb{R}^m\\) that maps the manifold to \\(M\\) to the standard embedding of \\(\mathbb{R}^n \subset \mathbb{R}^m\\). That is, \\(\varphi(U \cap M) = V \cap \\{x \in \mathbb{R}^{m} : x^{n+1} = \cdots = x^m = 0\\}\\).

This diffeomorphism \\(\varphi\\) ensures we can always do calculus over the surface of \\(M\\) because we can simply identify out manifold with \\(\mathbb{R}^n\\) and do calculus on \\(\mathbb{R}^n\\) as usual. However, note the above definition is an "extrinsic" description of smooth manifolds. That is, we require our manifold \\(M\\) be a subset of some "ambient" space \\(\mathbb{R}^m\\) in the same way we describe the sphere \\(\mathbb{S}^2 = \{(x,y,z) \in \mathbb{R}^3: x^2 + y^2 + z^2 = 1\}\\) as a subset of the ambient space \\(\mathbb{R}^3\\).

## Motivating the intrinsic definition

/\*TODO: note that in the above, we only need \\(f\\) defined on the manifold... this is better.\*/

/\*TODO: motivative intrinsic formulation... give pros and cons\*/

/\*TODO derive intrinsic formulation\*/

<!-- some examples for MC -->

