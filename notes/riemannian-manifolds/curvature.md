---
layout: page
title: Curvature
---

## The Riemann Curvature Tensor

#### Definition

The curvature of a Riemannian manifold is encoded in the Riemann curvature tensor.

**Def (Riemann Curvature Tensor).** The *Riemann curvature tensor* is the map 
\\[R: \Gamma(TM) \times \Gamma(TM) \times \Gamma(TM) \to \Gamma(TM) \\]
defined by
\\[
    R(X,Y)Z = \nabla\_{X}\nabla\_{Y}Z - \nabla\_Y\nabla\_X - \nabla\_{[X,Y]}Z.
\\]

This tensor encodes the extent to which a Riemannian manifold fails to be flat and the extend to which parallel transport fails to commute. In fact, by measuring the failure of parallel transport to commute, one is naturall led to this curvature tensor as described here /\*link to motivation\*/. In this page, however, we reverse the logic: we begin with this definition of the curvature tensor and formally prove results about this curvature tensor. First, one should check that this indeed definess a tensor.

**Exercise.** Prove that the curvature tensor as defined above is a tensor.

#### Curvature measures the non-commutativity of parallel transport

/\*todo\*/

#### Curvature is the obstruction to local flatness

/\*todo... do this proof\*/

#### The curvature tensor in coordinates

/\*todo... goal is:\*/

\\[
    R\_{ijk}^l = \partial\_i\Gamma^l\_{jk} - \partial\_j \Gamma^{l}\_{ik} + \Gamma^m\_{jk}\Gamma^l\_{im} - \Gamma\_{ik}^m\Gamma^l\_{jm}
\\]

#### Symmetries of the curvature tensor

/\*todo\*/

#### Other notions of curvature

/\*ricci curvature (motivation?)\*/

/\*scalar curvature\*/

/\*sectional curvature\*/

#### Curvature in Low Dimensions

/\*forms of curvature tensor in dimensions 1,2,3,4\*/