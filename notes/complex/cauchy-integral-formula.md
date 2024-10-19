---
layout: page
title: Cauchy Integral Formula
---

## Cauchy Integral Formula

An important property of a holomorphic function \\(f(z)\\) is the component functions \\(u\\) and \\(v\\) are *harmonic* where \\(f(x+iy) = u(x+iy) + iv(x+iy)\\). That is, \\(\Delta u = \Delta v = 0\\) where \\(\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\\) is the Laplacian. 

**Exercise.** Use the Cauchy-Riemann equations to verify the component functions \\(u\\) and \\(v\\) are harmonic.

**Solution.** /\*hide this\*/ 
\\[
    \frac{\partial^2 u}{\partial x^2} 
    = \frac{\partial }{\partial x} \left( \frac{\partial v}{\partial y} \right) 
    = \frac{\partial }{\partial y} \left( \frac{\partial v}{\partial x} \right) 
    = \frac{\partial }{\partial y}\left( -\frac{\partial u}{\partial y} \right)
    = -\frac{\partial^2 u}{\partial y^2}
\\]
/\*todo do \\(v\\)\*/

Many physical phenomenon are modeled with harmonic functions, so these functions are well studied and well understood. Importantly, these functions satisfy the *mean value property*: the average value of a harmonic function over a circle is always the value of the function at the center of the circle. Because the components of holomorphic functions are harmonic, holomorphic functions also satisfy the mean value property. This property can be nicely rephrased using only complex analysis as follows
\\[
    f(z)
    = \frac{1}{2\pi}\int_{\theta = 0}^{2\pi} f(z + e^{i\theta})d\theta = \frac{1}{2\pi i} \int\_{\gamma} \frac{f(\zeta)}{\zeta - z} d \zeta
\\]
where we made the change of variables \\(\zeta = z + e^{i\theta}\\) and the curve \\(\gamma\\) is the circle of radius \\(1\\) centered at \\(z\\). The above is called *Cauchy's integral formula*. Although we used the mean value property to motivate this formula, the Cauchy integral formula can be proved using only complex analysis (in particular the cachy integral theorem) as follows.

**Theorem (Cauchy Integral Formula).** Let \\(f\\) be a holomorphic function defined on a connected open subset \\(U \subset \mathbb{C}\\), let \\(z \in U\\) be a point, and let \\(\partial D_r(z)\\) be the circular path of radius \\(r\\) centered at \\(z\\) and oriented counter-clockwise. Then,
\\[
    f(z) = \frac{1}{2\pi i}\int_{\partial D\_r(z)} \frac{f(\zeta)}{\zeta - z} d\zeta.
\\]

*Proof.* We will study the integral
\\[
    \int_{\partial D_r(z)} \frac{f(\zeta)}{\zeta - z}d\zeta.
\\]
Note the integrand \\(f(\zeta)/(\zeta - z)\\) is holomorphic on the annulus \\(A^r_{\varepsilon}(z)\\) of outer radius \\(r\\) and inner radius \\(\varepsilon > 0\\) centered at \\(z\\). Therefore we have
\\[
    \int_{\partial D_r(z)} \frac{f(\zeta)}{\zeta - z}d\zeta =  \int_{\partial D_{\varepsilon}(z)} \frac{f(\zeta)}{\zeta - z}d\zeta
\\]
because Cauchy's theorem implies
\\[
    0 = \int_{\partial A^r_{\varepsilon}(z)} \frac{f(\zeta)}{\zeta - z}d\zeta = \int_{\partial D_r(z)} \frac{f(\zeta)}{\zeta - z}d\zeta - \int_{\partial D_{\varepsilon}(z)} \frac{f(\zeta)}{\zeta - z}d\zeta.
\\]
This is true for every \\(\varepsilon > 0\\) and therefore we can write
\\[
    \int_{\partial D_r(z)} \frac{f(\zeta)}{\zeta - z}d\zeta
    = \lim_{\varepsilon \to 0} \int_{\partial D_{\varepsilon}(z)} \frac{f(\zeta)}{\zeta - z}d\zeta.
\\]
By continuity we should be able to replace \\(f(\zeta)\\) with \\(f(z)\\) inside the integrand. Formally, we parametrize the difference to get
\\[
    \begin{align}
    \lim\_{\varepsilon \to 0} \int_{\partial D_{\varepsilon}(z)} \frac{f(\zeta) - f(z)}{\zeta - z} d \zeta
    &= \lim_{\varepsilon \to 0}\int_{0}^{2\pi} \frac{f(z+\varepsilon e^{i t}) - f(z)}{\varepsilon e^{i t}} i\varepsilon e^{i t} dt\\\\\
    &= i \lim_{\varepsilon \to 0} \int_{0}^{2\pi} f(z + \varepsilon e^{i     t}) - f(z) dt\\\\\
    &= i \int_{0}^{2\pi} \lim_{\varepsilon \to 0} f(z + \varepsilon e^{i t}) - f(z) dt = 0
    \end{align}
\\]
where we used that \\(f(z + \varepsilon e^{i t}) - f(z)\\) is uniformly bounded for small \\(\varepsilon\\) to exchange the limit and the integral, and we used continuity to conclude \\(\lim_{\varepsilon \to 0} f(z + \varepsilon e^{i t}) = f(z)\\). Therefore, continuing our computation, 
\\[
    \begin{align}
    \int_{\partial D_r(z)} \frac{f(\zeta)}{\zeta - z}d\zeta
    &= \lim_{\varepsilon \to 0} \int_{\partial D_{\varepsilon}(z)} \frac{f(\zeta)}{\zeta - z}d\zeta\\\\\
    &= \lim_{\varepsilon \to 0} \int_{\partial D_{\varepsilon}(z)} \frac{f(\zeta) - f(z)}{\zeta - z} d \zeta + \lim_{\varepsilon \to 0}\int_{\partial D_{\varepsilon}(z)} \frac{f(z)}{\zeta - z}d\zeta\\\\\
    &= f(z) \lim_{\varepsilon \to 0} \int_{\partial D_{\varepsilon}(z)} \frac{1}{\zeta - z}d\zeta
    = 2\pi i f(z)
    \end{align}
\\]
where the last equality follows from the computation
\\[
    \begin{align}
        \int\_{\partial D_{\varepsilon}(z)} \frac{1}{\zeta - z} d\zeta
        = \int_{0}^{2\pi} \frac{1}{e^{i t}}i e^{i t} = 2\pi i.
    \end{align}
\\]


**Theorem. (General Cauchy Integral Formula).** /\*todo: Talk about above for a general path. Maybe talk about winding number?\*/