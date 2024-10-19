---
layout: page
title: Tangent Bundle
---

## Tangent Bundle

We have seen that at each point \\(p\\) of a smooth manifold \\(M\\), there is a natural vector space \\(T_pM\\) called the *tangent space based at \\(p\\)* such that an element \\(v\\) of this tangent space can be interpreted as a tangent vector /\*link\*/ based at \\(p\\). Our next goal is to use collections of tangent vectors to extend the notion of a vector field to manifolds. For this, consider the union \\(TM := \bigsqcup\_{p \in M} T\_pM\\) of all tangent spaces together with the natural projection \\(\pi: TM \to M\\) given by \\(\pi: v_p \mapsto p\\) if \\(v\_p \in T\_pM\\). Next observe that a map \\(X: M \to TM\\) such that \\(\pi \circ X = \operatorname{Id}\_M\\) associates to each point \\(p \in M\\) a tangent vector \\(X(p) \in T_pM\\) based at \\(p\\) and hence can be interpreted as a vector field. Furthermore, recall that for vector fields over \\(\mathbb{R}^n\\), there is a notion of a "smooth vector field". In the case of manifolds, there is a natural smooth manifold structure of \\(TM\\) such that our map \\(X: M \to TM\\) is smooth precisely when in coordinate charts, the vector field \\(X\\) in coordinates is smooth in the usual sense. In this page we determine this natural topology and smooth structure to bestow upon \\(TM\\), then formally define and study the resulting smooth manifold.

#### Motivation for topology and smooth structure

We find the natural topology and smooth structure of the set \\(TM\\) equipped with projection \\(\pi: TM \to M\\) discussed above. For this, we begin by studying the local structure \\(\pi^{-1}(U)\\) for some coordinate chart \\(U \subset M\\). Note \\(\pi^{-1}(U) = U \times \mathbb{R}^n\\) as a set, for each element of \\(\pi^{-1}(U)\\) can be written \\((p,v_p)\\) for \\(p \in U\\) and \\(v\_p = v^i \left.\partial\_i \right\|\_p\\) in coordinates. Importantly, this set comes with natural projections \\(\pi: U \times \mathbb{R}^n \to U\\) and \\(\pi_i: U \times \mathbb{R}^n \to \mathbb{R}\\) for \\(1 \leq i \leq n\\). Traditionally, we understand a vector field \\(X: U \to U \times \mathbb{R}^n\\) to be smooth precisely when, given the expression \\(X = X^i(p) \left.\partial\_i\right\|\_p\\) in coordinates, each \\(X^i := \pi_i \circ X: U \to \mathbb{R}\\) is smooth as a map between Euclidean spaces. The additional observation that \\(\pi \circ X: U \to U\\) is simply the identity -- and hence is always smooth -- forces the space \\(\pi^{-1}(U)\\) to have the product smooth manifold structure of \\(U \times \mathbb{R}^n\\) by the universal property of smooth manifold products. Knowing the smooth manifold structure of \\(\pi^{-1}(U)\\) for all coordinate neighborhoods \\(U\\) allows us to build up the smooth manifold structure of \\(TM\\); formally, we require the inclusions \\(\pi^{-1}(U) \to TM\\) to be smooth embeddings.

#### Formal definition

