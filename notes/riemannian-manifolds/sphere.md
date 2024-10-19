---
layout: page
section: RIEMANNIAN GEOMETRY
title: Riemannian Manifold
---

/\*Reframe: Don't go too much into theory...focus on computations?\*/

## Riemannian Metric on the Sphere

Riemannian geometry is a technique that allows us to do geometry *on* a curved surface. For example, consider the sphere.

/\*insert picture of sphere that we can rotate. (maybe overlaid with Earth map)\*/

Below are some geometric problems we will try to solve.
1. Given a line on the surface of the sphere, how can we find the length of the line?
1. Given two intersecting lines on the sphere, what is the angle between those two lines?
1. Given a region on the sphere, how can we find the area of that region?
1. Given two points on the sphere, what is the distance between those two points?
1. Given a line on the sphere, how do we know if it is straight?

We will answer (1), (2), and (3) on this page, but the techniques will generalize and allow us to eventually answer all of these questions for *any* surface, even higher dimensional ones!

#### Parametrization
Before we can answer any of the questions above, we first need to be able to describe the locations of points on the sphere. One way of doing this is with two angles: latitude and longitude. We will construct a way of associating points on the sphere with two numbers by taking inspiration from latitude and longitude.

/\*insert picture of sphere with latitude and longitude\*/

As in the figure above, we associate each point on the sphere with two angles $\theta$ and $\phi$.

Therefore each pair $\theta, \phi$ corresponds to a unique point on the sphere so long as $0 < \theta < 2\pi$ and $0 < \phi < \pi$. In other words, we have a function $T: (0, 2\pi) \times (0,\pi) \to S^2$ where $T$ takes as input a pair $(\theta, \phi)$ and outputs the corresponding point on the sphere. We will refer to such functions as *parametrizations* of the sphere and we will refer to the domain of the parametrization as a *chart*.

TODO: insert picture of chart to surface with world map.

/\*explain formula...\*/

\\[T(\theta, \phi) = (\cos\theta\sin\phi, \sin\theta\sin\phi, \cos\phi)\\]

Now that we can describe points on the sphere with their coordinates $(\theta, \phi)$ we can also describe lines and regions on the sphere by simply describing lines and regions on the coordinate chart.

Specifically, it will be easiest to trace out a line with parametric function \\(\gamma(t)\\) so that \\(\gamma(t)\\) gives \\((\theta, \phi))\\) value of the line at time \\(t\\). That is, \\(\gamma: [a,b] \to (0,2\pi) \times (0,\pi)\\).

#### Missing information from the chart
While the parametrization of the sphere is useful in describing points on the sphere, the chart loses crucial information that we need to answer our questions. For example:

1. The length of a line on the chart is not necessarily the length of the corresponding line on the sphere.
1. The angle between two lines on the chart is likely not the angle between the corresponding line on the sphere.
1. The area of a region of a chart is not necessarily the area of the corresponding region on the sphere.
1. The distance between two points on the chart is not necessarily the distance between two points on the sphere.
1. A straight line on the chart is not necessarily straight on the sphere.

/\*give some examples indicating that none of these are obvious from the map... put these into exercises?\*/

The problem is that while the chart provides a way of describing points on the sphere, it contains no information about the *geometry* of the sphere.

#### Velocity Vectors
So how do we encode the geometry of the sphere into the chart? Recall we can compute lengths of a curve $\gamma(t)$ with $a \leq t \leq b$ by using the length of the velocity vectors $\gamma'(t)$.
\\[
    \operatorname{length}(\gamma) =  \int_{a}^{b}\|\gamma'(t)\|dt 
\\]

Similarly, we can compute the angle between two curves $\gamma(t)$ and $s(t)$ by calculating the angle between the corresponding velocity vectors $v$ and $w$ of the curves at the intersection point. The key to correctly computing angles, lengths, and areas lies in connecting velocity vectors on the chart to velocity vectors on the sphere.

Consider some vector $v$ based at a coordinate point $(\theta, \phi)$. If the transformation $T$ has Jacobi matrix $DT$, then the vector $DT(v)$ is a the velocity vector *on the surface of the sphere* that corresponds to $v$.

**Exercise.** Show that the Jacobi matrix $DT$ for our parametrization
\\[T(\theta, \phi) = (\cos\theta\sin\phi, \sin\theta\sin\phi, \cos\phi)\\]
is given by
\\[
    /\*TODO\*/
\\]
<details><summary>Solution.</summary>
    /\*TODO\*/
</details>

#### Riemannian Metric
Given two vectors $v$ and $w$ based at some coordinates $(\theta, \phi)$ in the chart, the "correct angle" between $v$ and $w$ is the angle between the vectors $DT(v)$ and $DT(w)$. Similarly, the "correct length" of $v$ is the length of the vecor $DT(v)$.

/\*images demonstrating this.\*/

Recall that if we can deduce length of vectors and angles between vectors from a dot product, so to correctly define lengths and angles all we need to do is define the "correct dot product" between the vectors at that point. If $v$ and $w$ are vectors based at the coordinte $(\theta, \phi)$, the "correct dot product" between $v$ and $w$ is the dot product between $DT(v)$ and $DT(w)$!

/\*image demonstrating this.\*/

Defining such a dot product at *every* coordinate point $(\theta, \phi)$ is the fundamental idea of Riemannian geometry. If $v$ and $w$ are vectors at point $(\theta, \phi)$, the "correct dot product" between $v$ and $w$, denoted $g(v,w)$ is
\\[g(v,w) = DT_{(\theta,\phi)}(v) \cdot DT_{(\theta,\phi)}(w)\\]
This new dot product $g$ at each point $(\theta, \phi)$ is the *Riemannian metric* for the sphere. 

/\*change exericse to computing $DT$\*/

<details>
<summary>Exercise.</summary>
<p>
For practice, let's compute this inner product for the basis vectors $\{\partial_\theta, \partial_\phi\}$ at each point. At each point $(\theta, \phi)$ in the chart $[0, 2\pi] \times [0, \pi]$, use the definition above to compute the "correct dot product" between the basis vectors in the following ways.
<ol>
<li> $g(\partial_{\theta}, \partial_{\theta})$ </li>
<li> $g(\partial_{\theta}, \partial_{\phi})$ </li>
<li> $g(\partial_{\phi}, \partial_{\theta})$</li>
<li> $g(\partial_{\phi}, \partial_{\phi})$</li>
</ol>
</p>
</details>

<details>
<summary>Solution.</summary>
To apply the definition of the dot product $g$, we need to compute the Jacobi matrix $DT_{(\theta, \phi)}$ at each point. This is
/\*TODO\*/

\[DT =
\begin{pmatrix}
    \frac{\partial x}{\partial \theta} & \frac{\partial x}{\partial \phi}\\
    \frac{\partial y}{\partial \theta} & \frac{\partial y}{\partial \phi}
\end{pmatrix}
\]

\[g(\partial_\theta, \partial_\phi) = \]
</details>

TODO: make this exercise and hide it?


**Exercise**: ...........



#### Using the Riemannian Metric
TODO: discuss angles between vectors, lengths of vectors, lengths of lines, area of regions.

Let $\gamma:(a,b) \to (0, 2\pi) \times (0,\pi)$ be some curve in the chart. Then we can compute the length of $\gamma$ on the sphere by
\\[
\operatorname{length}(\gamma) 
= \int_{a}^{b}\|\gamma'(t)\|dt 
= \int_{a}^{b}\sqrt{g(\gamma'(t), \gamma'(t))}dt
\\]

Let $v$ and $w$ be two vectors in the chart. Then the angle $\theta$ between $v$ and $w$ on the sphere is given by
\\[
\cos(\theta) = \frac{g(v,w)}{|v||w|} = \frac{g(v,w)}{\sqrt{g(v,v)g(w,w)}}
\\]

Given a region $R$ in the chart, the area of the corresponing spherical region is given by
\\[
\operatorname{area}(R) = \int_{R}\sqrt{\det(g)}d\theta d\phi.
\\]

Therefore we have succesfully answered questions (1), (2), and (3) that we posed at the top of this document.

#### Covering the Whole Sphere
Our parametrization \\(T: (0, 2\pi) \times (0,\pi) \to S^2\\) comes with a huge limitation: it does not cover the whole sphere. There is a strip of points on the sphere that we are not able to describe. The best fix for this is to add another chart \\(R: (0, 2\pi) \times (0,\pi) \to S^2\\) that covers these missing points.

/\*show picture of this\*/

/\*compute this function\*/

/\*maybe explain why can't just use half-open interval... (hard to tell when sequences converge and what to).\*/

/\*explain that now things get more complicated... (smooth transition maps, metric needs to agree, etc.)\*/

/\*might want to go into more detail here...\*/

/\*perhaps mention earlier that the analysis before this section only works for part of the sphere\*/