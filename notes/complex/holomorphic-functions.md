---
layout: page
title: Holomorphic functions
---

## Holomorphic functions

When extending functions to the complex plane, extra structure and patterns emerge. For example, let us take a closer look at the maps given by \\(e^z\\), \\(\sin z\\), and \\(\sqrt{z}\\).

/\*show pictures here.\*/

Notice that the above complex functions take the coordinate lines from the input to curves that still meet at right angles in the output (except for some interesting behavior at \\(0\\)). This property is certainly not true of general maps \\(\mathbb{R}^2 \to \mathbb{R}^2\\) (consider \\((x,y) \mapsto (x, x+y)\\) for example), and is the first hint of the special structure complex functions satisfy. The reason for this is the following fact, which has profound consequences.

*The derivative of each point of the above complex functions is given by a complex number.*

Complex analysis in large part studies complex functions whose derivative at each point is a complex number. This is a surprisingly strong property that almost all familiar functions, when extended to the complex plane, satisfy. Thus this is a crucial property to study to better understand complex functions - even when we are only interested in real arguments.

#### Derivative of a complex function

If a complex function satisfies the crucial property of having a complex derivative at each point, it is called "holomorphic". Many familiar complex functions satisfy this property, and so we can learn a lot by studying holomorphic complex functions generally. The formal definition of holomorphic, which is nearly identical to the real version of differentiability, is given below

**Def (holomorphic).** Consider a complex function \\(f: \mathbb{C} \to \mathbb{C}\\) and a point \\(w \in \mathbb{C}\\). If the limit 
\\[
    f'(w) := \lim\_{z \to w} \frac{f(z) - f(w)}{z-w}
\\]
exists, then \\(f\\) is *holomorphic at \\(w\\)*, and \\(f'(w)\\) is the *complex derivative of \\(f\\) at \\(w\\)*. If \\(f\\) is holomorphic at every point \\(w \in \mathbb{C}\\), then we say \\(f\\) is *holomorphic*.

Note that in the above limit, \\(z\\) is a complex number that may approach \\(w\\) from any direction and thus for the above limit to exist, the limit must be independent of the direction that \\(z\\) approaches \\(w\\) -- a fairly strong condition. Derivatives are often understood as "the best linear approximation", and the following proposition reformulates the complex derivative as the unique complex number so that the linear map given from multiplication by this number is the best linear approximation.

**Prop.** A complex function \\(f: \mathbb{C} \to \mathbb{C}\\) is holomorphic at \\(w\\) if and only if there exists a complex number \\(f'(w)\\) such that if \\(h\\) is any complex number with \\(h \to 0\\), then
\\[
    \frac{f(w+h) - f(w) - f'(w)h}{|h|} \to 0.
    \tag{&#9733;}
    \label{eq:holo}
\\]
If such a \\(f'(w)\\) exists, it is unique and equivalent to the derivative of \\(f\\) at \\(w\\).

**Exercise.** Prove the above proposition.

The above reformulation is easily compared to (one of) the defintions of the derivative of a real function \\(F: \mathbb{R}^2 \to \mathbb{R}^2\\) given as follows.

**Def.** A function \\(F: \mathbb{R}^2 \to \mathbb{R}^2\\) is said to be *differentiable at \\((x,y)\\)* if there exists a \\(2 \times 2\\) matrix \\(DF((x, y))\\) such that for any row vector \\(h \in \mathbb{R}^2\\) with \\(h \to (0,0)\\), then
\\[
    \frac{F((x,y) + h) - F((x,y)) - DF((x,y)) h^T}{|h|} \to 0.
    \tag{&#9830;}
    \label{eq:diff}
\\]
If such a matrix \\(DF((x, y))\\) exists, it is called the *Jacobian of \\(F\\) at \\((x,y)\\)*. 

Furthermore, recall that if the Jacobian exists at \\((x,y)\\), then the partial derivatives also exist at \\((x,y)\\) and make up the entries of the Jacobian. That is, if \\(F(x,y) = (u(x,y), v(x,y))\\), then
\\[ DF(x,y) = 
    \begin{pmatrix}
        \left.\frac{\partial u}{\partial x}\right|\_{(x,y)} & \left.\frac{\partial u}{\partial y}\right|\_{(x,y)}\\\\\
        \left.\frac{\partial v}{\partial x}\right|\_{(x,y)} & \left.\frac{\partial v}{\partial y}\right|\_{(x,y)}
    \end{pmatrix}.
\\]

We are now equipped to compare holomorphicity of functions \\(\mathbb{C} \to \mathbb{C}\\) to differentiability of functions \\(\mathbb{R}^2 \to \mathbb{R}^2\\), leading to the following result.

**Thm (Cauchy-Riemann Equations).** Let \\(f(z)\\) be holomorphic at \\(x\_0 + iy\_0 = z\_0 \in \mathbb{C}\\) and write \\(f(x+iy) = u(x+iy) + iv(x+iy)\\). Then the following *Cauchy-Riemann equations* are satisfied:
\\[
    \left.\frac{\partial u}{\partial x}\right|\_{(x\_0,y\_0)} = \left.\frac{\partial v}{\partial y} \right|\_{(x\_0,y\_0)}
    \quad \text{and} \quad 
    \left.\frac{\partial v}{\partial x}\right|\_{(x\_0,y\_0)} = - \left.\frac{\partial u}{\partial y}\right|\_{(x\_0,y\_0)}.
\\]

*Proof.* Recall there exists a complex number \\(f'(z_0) = p + iq\\) that satisfies (\ref{eq:holo}) as \\(h \to 0\\). This complex number defines a linear map \\(h \mapsto f'(z\_0)h\\) on \\(\mathbb{C}\\), which we can rewrite as a matrix transformation on \\(\mathbb{R}^2\\). Indeed, define the matrix \\(DF((x\_0,y\_0))\\) by
\\[
    DF((x\_0,y\_0)) 
    = \begin{pmatrix}
        p  & -q\\\\\
        q & p
    \end{pmatrix}.
\\]
A quick computation confirms the linear map \\(h^T \mapsto DF((x\_0,y\_0))h^T\\) on \\(\mathbb{R}^2\\) corresponds to the map \\(h \mapsto f'(z\_0)h\\). Therefore, as \\(h \to 0\\), this \\(DF((x\_0,y\_0))\\) satisfies (\ref{eq:diff}), so the Jacobian exists, hence the partial derivatives exist, and in particular \\(p = \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}\\) and \\(q = \frac{\partial v}{\partial x} = -\frac{\partial u}{\partial y}\\), so the Cauchy-Riemann equations are satisfied. 
<div style="text-align: right"> \(\square\) </div>

*The Cauchy-Riemann equations simply encode that the derivatative is a complex number: the Jacobi matrix should represent multiplication by a complex number.*

/\*discuss converse... TODO do multivariable real analysis on this site\*/