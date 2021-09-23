---
layout: page
section: NOTES
title: Linear Diophantine Equations
---

## Linear Diophantine Equations

#### The Equation
Given integers $a, b, c$ a linear Diophantine equation seeks for integral solutions to $ax + by = c$.

#### Solution
If $\gcd(a,b) \mid c$, then the equation has infinite solutions. Otherwise, the equation has no solution for $\gcd(a,b)$ would divide the left side but not the right.

When solutions exist, a first solution $ax_0 + by_0 = c$ can be found by scaling up Bézout's identity. The infinite remaining solution are parametrized by
\\[a\left(x_0 + \frac{b}{(a,b)}k\right) + b\left(y_0 - \frac{a}{(a,b)}k\right) = c\\]
for all integral $k$.

This parametriation clearly gives valid solutions. For justification that this accounts for all possible solutions, consider any solution $ax + by = c$. Combining this with $ax_0 + by_0 = c$ and gives $ax+by = ax_0 + by_0$ and some algebra gives
\\[\frac{a}{(a,b)}(x-x_0) = \frac{b}{(a,b)}(y-y_0)\\]
Thus, we are restricted to $\frac{b}{(a,b)} \mid x-x_0$. The above parametrization accounts for all possible such solutions in $x$, then pairs each to the corresponsing uniquelly defined solution in $y$.