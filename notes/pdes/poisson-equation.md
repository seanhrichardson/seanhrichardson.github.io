---
layout: page
title: Poisson's Equation
---

## Poisson's Equation

#### Motivation
/\*motivation... gravitational potential\*/

/\*"Green’s Representation Formula" as in Iva's notes.\*/

/\*Example... solution to \\(\Delta \Phi = \delta\\) models planetary motion/black hole.\*/

#### Deriving the Fundamental Solution

A fundamental solution to the Laplacian is a function \\(\phi(y)\\) such that \\(\Delta \phi = \delta\\) for the dirac delta distribution \\(\delta(y)\\). Then a solution to the Poisson equation \\(\Delta u = f\\) is conveniently given by \\(u = f \ast \phi\\) because
\\[
    \Delta u = \Delta(f \ast \phi) = f \ast \Delta \phi = f \ast \delta = f
\\]

Such a fundamental solution \\(\phi\\) must satisfy \\(\Delta \phi = 0\\) on \\(\mathbb{R}^n \smallsetminus 0\\) by the definition \\(\Delta \phi = \delta\\). Furthermore, by this definition and the radial symmetry of \\(\delta\\), we must have radial symmetry in the solution \\(\phi(x) = v(r(x))\\) for some function \\(v\\) over \\(\mathbb{R}\\) and \\(r(x) = \|x\|\\). By using the polar form of the Laplacian we find that on \\(\mathbb{R}^n \smallsetminus 0\\),
\\[
    0 = \Delta u = \frac{\partial^2 v}{\partial r^2} + \frac{n-1}{r} \frac{\partial v}{\partial r} = v^{\prime \prime}(r) + \frac{n-1}{r}v'(r),
\\]
and therefore
\\[
    \frac{d }{d r}\log\|v'(r)\| = \frac{v^{\prime \prime}(r)}{v'(r)} = \frac{1-n}{r},
\\]
hence we get \\(v'(r) = ar^{1-n}\\) for some constant \\(a\\). Then we conclude that for some constants \\(b\\) and \\(c\\)
\\[
    v(r) = 
    \begin{cases}
        b \log r + c, & n = 2\\\\\
        br^{2-n} + c, & n \geq 3.
    \end{cases}
\\]
We also require \\(\int_{\mathbb{R}^n} \Delta \phi = 1\\) and it is convenient to choose constants so that \\(\lim_{r \to 0} \phi(r) = 0\\) to ensure \\(\phi\\) is integrable. Therefore we consider the candidate funamental solution
\\[
    \phi(x) =
    \begin{cases}
        -\frac{1}{2\pi}\log\|x\|, & n=2\\\\\
        \frac{1}{(2-n)\omega_n}|x|^{2-n}, & n\geq 3.
    \end{cases}
\\]
where \\(\omega_n\\) is the area of the unit sphere in \\(\mathbb{R}^n\\).

#### Verifing the Fundamental Solution
It still remains to verify the above is indeed a fundamental solution. 

/\*TODO\*/

#### General Solution

#### Application to Gravity