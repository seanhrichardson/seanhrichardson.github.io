---
layout: page
title: Jacobi Equation
---

## The Jacobi Equation

<!-- /\*visual motivation: hyperbolic space, sphere, etc....\*/ -->

Consider a family of geodesics \\(\Gamma\_s(t)\\) parametrized by \\(s\\), which determines vector fields \\(\partial\_t\\) and \\(\partial\_s\\).
<!-- explain how these V.F's are determined -->
As we move along the geodesic \\(\gamma(t) = \Gamma\_0(t)\\), the acceleration of nearby geodesics is determined by the geometry of the manifold and can be computed by
\\[
\begin{align}
    D\_t^2 \partial\_s 
    = \nabla\_{\partial\_t}\nabla\_{\partial\_t} \partial\_s
    = \nabla\_{\partial\_t}\nabla\_{\partial\_s} \partial\_t
    = \nabla\_{\partial\_s}\nabla\_{\partial\_t} \partial\_t - R(\partial\_s, \partial\_t)\partial\_t
    = - R(\partial\_s, \partial\_t)\partial\_t.
\end{align}
\\]
Indeed, we see the acceleration of nearby geodesics is determined by the Riemann curvature tensor.

/\*define jacobi field\*/

/\*todo... 10.4 every jacobi field is the variation of a geodesic\*/

/\*the point is that jacobi fields (defined concretely via the jacobi equation) are easier to work with than variations\*/

/\*existence of jacobi fields... 10.2\*/

/\*something with tangential and normal jacobi fields as a way to simplify\*/

#### Conjugate Points