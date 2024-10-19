---
layout: page
title: Intrinsic Definition of Smooth Manifolds
---

## Intrinsic Definition of Smooth Manifolds

Recall we developed the following extrinsic definition of a *smooth manifold*.

**Extrinsic definition of smooth manifold.** A subset \\(M \subset \mathbb{R}^m\\) is an \\(n\\)-dimensional smooth manifold if every point of \\(M\\) has a neighborhood diffeomorphic to an open subset of \\(\mathbb{R}^n \subset \mathbb{R}^m\\).

We now want to develop an *intrinsic definition*, which will be much more convenient to work with when developing the theory of smooth manifolds. To do so, we will identify the key structures and properties of smooth manifolds when defines extrinsically, then piece together these properties into a definition.

Firstly, a smooth manifold \\(M \subset \mathbb{R}^m\\) is a topological space with the subspace topology and so we ask: what properties must this space have? Some such properties are as follows.
* \\(M\\) must be Hausdorff as a subspace of the Hausdorff space \\(\mathbb{R}^m\\).
* \\(M\\) must be \\(2\\)nd countable as a subspace of the \\(2\\)nd countable space \\(\mathbb{R}^m\\).
* \\(M\\) is locally Euclidean. Indeed, each point of \\(M\\) has a neighborhood \\(U\\) diffeomorphic to an open subset of \\(\mathbb{R}^n \subset \mathbb{R}^m\\). This same diffeomorphism must also be a homeomorphism between \\(U\\) and an open subset of \\(\mathbb{R}^n\\). /\*maybe explain this a bit more as it is used later?\*/

The three bullet points above are precisely the requirements for a topological space to be an \\(n\\)-dimensional topological manifold. Thus a smooth \\(n\\)-manifold \\(M\\) has the topological structure of a topological manifold. 

However, an extrinsically defined smooth manifold \\(M \subset \mathbb{R}^m\\) has additional "smooth structure" provided by the local diffeomorphisms promised in the definition. For example, given \\(f: \mathbb{R}^k \to M\\) there is a neighborhood \\(U \subset M\\) of \\(f(0)\\) with a diffeomorphic "coordinate chart" \\(\phi: U \to V \subset \mathbb{R}^n \subset \mathbb{R}^m\\). Then we can define \\(f\\) to be "smooth" if \\(\phi \circ f: \mathbb{R}^k \to V \subset \mathbb{R}^n\\) is smooth in the Euclidean sense. Furthermore, the derivative of \\(f\\) at \\(0\\) can be represented "in coordinates" by \\(D(\phi \circ f)(0)\\), the Jacobian matrix at \\(0\\).

This definition of "smooth" comes with a major concern: what if we have two coordinate chart diffeomorphisms \\(\phi: U \to V\\), \\(\psi: U' \to V'\\) such that \\(f(0)\\) is contained in the intersection \\(U \cap U'?\\) The worry is that \\(\phi \circ f\\) could be smooth while \\(\psi \circ f\\) is not smooth, which would signify this definition of smooth is ill-defined. Luckily we will see this is not the case because these coordinate charts are diffeomorphisms, not simply homeomorphisms. Indeed, by simply recalling the definition of diffeomorphism between arbitrary subsets, there exists diffeomorphisms \\(\Phi: \mathcal{U} \to \mathcal{V}\\) and \\(\Psi: \mathcal{U}' \to \mathcal{V}'\\) between open subsets of \\(\mathbb{R}^m\\) extending \\(\phi\\) and \\(\psi\\) respectively. Thus \\(\Phi \circ \Psi^{-1}: V' \to V\\) is a diffeomorphism and thus \\(\phi \circ \psi^{-1}: V' \to V\\) is a diffeomorphism. Thus if \\(\phi \circ f\\) is a smooth, so is \\(\psi \circ f = (\phi \circ \psi^{-1}) \circ \psi \circ f\\) and vice versa, so "smoothness" is well-defined.

In the above argument, the key property we derived that allows for a well-defined definition of smoothness is that the "transition map" \\(\phi \circ \psi^{-1}\\) is smooth between open subsets of \\(\mathbb{R}^n\\). Putting this all together, we are finally ready to intrinsically define a smooth manifold \\(M\\) to be a topological manifold that is covered by "coordinate charts" with diffeomorphic "transition maps".

**Intrinsic definition of smooth manifold.** An *\\(n\\)-dimensional smooth manifold* is a topological manifold \\(M\\) of dimension \\(n\\) together with an open cover \\(\{U_{\alpha}\}\\) of \\(M\\) and homeomorphisms \\(\varphi_{\alpha}: U_{\alpha} \to V_{\alpha}\\) where each \\(V_{\alpha}\\) is an open subset of \\(\mathbb{R}^n\\), and the transition maps \\(\varphi_{\alpha} \circ \varphi_{\beta}^{-1}\\) are diffeomorphisms.

The homeomorphisms \\(\varphi_{\alpha}\\) are called *coordinate charts*, the entire collection \\(\varphi_{\alpha}: U_{\alpha} \to V_{\alpha}\\) is called an *atlas*, and when \\(\varphi_{\alpha} \circ \varphi_{\beta}^{-1}\\) is a diffeomorphism, we say \\(\varphi_{\alpha}\\) and \\(\varphi_{\beta}\\) are *smoothly compatible*.

/\*possibly talk about "smooth structure" and "maximal atlas"\*/