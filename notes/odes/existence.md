---
layout: page
title:
---

## Existence of Solutions to ODES

#### The Initital Value Problem

Consider an open subset \\(U \subset \mathbb{R}^n\\) and suppose we have a vector field \\(V: U \to \mathbb{R}^n\\) defined over this subset. Then, given a point \\(c \in \mathbb{R}^n\\), we are interesed in finding a solution curve \\(y: (-\varepsilon, \varepsilon) \to \mathbb{R}^n\\) such that \\(y(0) = c\\). To be precise, we are looking for a solution for the initial value problem
\\[
    \begin{cases}
        \dot{y}^i(t) = V^i(y^1(t), \cdots, y^n(t))\\\\\
        y^i(0) = c^i.
    \end{cases}
    \tag{\\(\star\\)} \label{eq:ode}
\\]
for \\(i = 1, \cdots, n\\).

/\*visual for \\(V\\), \\(y\\), \\(U\\), etc.\*/

#### Picard Iteration

By integrating the ODE in (\ref{eq:ode}) then using the corresponding boundary conditions we find that \\(y(t)\\) is a solution if and only if it satisfies the integral equation
\\[
    y^i(t) = c^i + \int_0^t V^i(y(s))ds.
\\]
This motivates considering *Picard's operator*
\\[
    Iy(t) = c  + \int_0^t V(y(s))ds \tag{P} \label{eq:picard-op}
\\]
where the integral of the vector \\(V(y(s))\\) is the vector consisting of integrals of each \\(V^i(y(s))\\). Then \\(y(t)\\) is a solution if and only if \\(Iy = y\\). That is, solutions are precisely the fixed points of Picard's operator. In fact, if you play around with Picard's operator, you will find that if you start with some incorrect guess \\(y\_0(t)\\) of the solution satisfying \\(y\_0(t) = c\\), then \\(y\_1 := Iy\_0\\) is closer to the actual solution. The method of *Picard iteration* is to create the sequence \\(y\_k(t)\\) defined iteratively by \\(y\_{k+1} = I_{k}y\\) to approximate the solution. Amazingly, if \\(V\\) is nice enough, this method will always work! Furthermore, by proving that this method always converges to a solution we can prove that every ODE of the form (\ref{eq:ode}) will have a solution!

/\*numerical approximation animations\*/

#### Existence of a Solution

**Theorem (Existence of ODE Solutions).** Suppose we have an open subset \\(U \subset \mathbb{R}^n\\), a locally Lipschitz continuous vector field \\(V: U \to \mathbb{R}^n\\), and we are given \\(x\_0 \in U\\). Then there exists \\(\varepsilon > 0\\) and \\(U_0 \subset U\\) containing \\(x\_0\\) such that for every \\(c \in U\\) there exists a \\(C^1\\) map \\(y: (-\varepsilon, \varepsilon) \to U\\) satisfying the initial value problem (\ref{eq:ode}).

/\*TODO: cite ISM\*/

*Proof.* We will show Picard's operator (\ref{eq:picard-op}) is a contraction and therefore will have a fixed point by the Banach fixed point theorem /\*todo: page on Banach fixd point theorem\*/. We will do this by carefully constructing a complete metric space of potential solutions functions that \\(I\\) acts on. First, however, we construct \\(\varepsilon\\) and \\(U\_0\\). We will want our codomain to contained in a closed set to ensure completenesss, so choose \\(r > 0\\) small enough such that \\(\overline{B}\_{r}(x\_0) \subset U\\), then take \\(\delta < r/2\\) and define \\(U\_0 = B_{\delta}(x\_0)\\). Furthermore, we will need a small domain to ensure Picard's operator is a well-defined contraction on our space. For this, recall that by \\(V\\) Lipschitz continuous there is a constant \\(C\\) such that
\\[
    |V(y) - V(\widetilde{y})| \leq C|y-\widetilde{y}| \quad \text{for all } \quad y, \widetilde{y} \in U,
\\]
and let \\(M\\) be the supremum of \\(V\\) on the compact set \\(\overline{B}\_{r}(x\_0)\\).
We will later see that we need \\(\varepsilon > 0\\) small enough so that
\\[
    \varepsilon < \min\left(\frac{r}{2M}, \frac{1}{C}\right).
\\]
Now for each \\(c \in U_0\\), we define the metric space \\(\mathcal{F}\_c\\) of potential solutions to be all continuous functions \\(y: (-\varepsilon, \varepsilon) \to \overline{B}\_{r}(x\_0)\\) such that \\(y(0) = c\\) and equip this space with the metric
\\[
    d(y, \widetilde{y}) := \sup_{t \in (-\varepsilon, \varepsilon)}|y(t) - \widetilde{y}(t)|.
\\]
We will also define the "norm" \\(\\|y\\| := \sup_{t \in (-\varepsilon, \varepsilon)}|y(t)|\\) so that we can write \\(d(y, \widetilde{y})\\) as \\(\\|y-\widetilde{y}\\|\\). Note each \\(\mathcal{F}\_c\\) is a complete metric space /\*make exercise\*/. Now define Picard's operator \\(I: \mathcal{F}\_c \to \mathcal{F}\_c\\) by 
\\[
    Iy(t) = c  + \int_0^t V(y(s))ds \tag{P}.
\\]
We only need to check \\(I\\) maps \\(\mathcal{F}\_c\\) into itself and that it is a contraction. Indeed, for any \\(y \in \mathcal{F}\_c\\) and \\(t \in (-\varepsilon, \varepsilon)\\) observe that \\(Iy(t) \in \overline{B}\_{r}(x\_0)\\) by
\\[
    \begin{align}
        |Iy(t) - x\_0| &= \left\|c + \int\_{0}^tV(y(s))ds - x\_0\right\|\\\\\
        &\leq |c-x\_0| + \int\_{0}^t|V(y(s))|ds\\\\\
        &\leq \delta + M\varepsilon < r
    \end{align}
\\]
where we used the definition of \\(\varepsilon\\) in the last step. Thus \\(I: \mathcal{F}\_c \to \mathcal{F}\_c\\) is well-defined. Next, \\(I\\) is a contraction by
\\[
    \begin{align}
        \\|Iy - I\widetilde{y}\\|
        &= \sup\_{t \in (-\varepsilon, \varepsilon)}\left\|\int\_{0}^tV(y(s))ds - \int\_{0}^tV(\widetilde{y}(s))ds\right\|\\\\\
        &\leq \sup\_{t \in (-\varepsilon, \varepsilon)}\int\_{0}^t\left\|V(y(s)) - V(\widetilde{y}(s))\right\|ds\\\\\
        &\leq \sup\_{t \in (-\varepsilon, \varepsilon)}\int\_{0}^t C\|y(s)-\widetilde{y}(s)\|ds \leq C\varepsilon\\|y-\widetilde{y}\\| < \\|y-\widetilde{y}\\|
    \end{align}
\\]
again by the definition of \\(\varepsilon\\). Therefore by the Banach fixed point theorem, for each \\(c \in U\_0\\), there exists a \\(y \in \mathcal{F}\_c\\\) such that \\(Iy = y\\). By differentiating, we find \\(y\\) satisfies (\ref{eq:ode}).