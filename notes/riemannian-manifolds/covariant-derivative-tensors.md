---
layout: page
title: Covariant Derivative on Tensors
section: Covariant Derivative on Tensors
---

# Covariant Derivative on Tensors

Consider a smooth manifold \\(M\\) with connection \\(\nabla\\), which allows for the differentiation of vector fields. Furthermore, recall that if \\(\nabla\\) induces parallel transport map \\(P^{\gamma}\_{t\_1, t\_0}: T\_{\gamma(t\_1)}M \to T\_{\gamma(t\_0)}M\\) along a curve \\(\gamma(t)\\), and this identification between tangent spaces allows us to recover \\(\nabla\\) by
\\[
    \nabla\_{\dot{\gamma}(0)} X = \left.\frac{d }{d t}\right\|\_{t=0} P\_{t,0}^{\gamma} X\_{\gamma(t)}.
\\]
In fact, the connection \\(\nabla\\) allows the differetiation of tensors, not just vector fields. 

## Differentiation of covectors

For example, to differentiate a covector field \\(\omega\\), we can use the dual map
\\[
    P^{\*}\_{0,t}: T^{\*}\_{\gamma(t)}M \to T^{\*}\_{\gamma(0)}M
\\]
to identify the cotangent spaces and define covariant differentiation by
\\[
    \nabla\_{\dot{\gamma}(0)} \omega := \left.\frac{d }{d t}\right\|\_{t=0} P^{\*}\_{0,t} \omega\_{\gamma(t)}.
\\]

Next we will explore the expression for this covariant derivative in terms of a parallel frame. Indeed, if \\(E\_i\\) is a parallel frame along \\(\gamma\\), then take the dual frame \\(\varepsilon^i\\), write \\(\omega = \omega\_i \varepsilon^i\\), and compute
\\[
    \nabla\_{\dot{\gamma}(0)} \omega 
    = \left.\frac{d }{d t}\right\|\_{t=0}P\_{0,t}^\*(\omega\_i \varepsilon^i)
    = \left.\frac{d }{d t}\right\|\_{t=0}\omega\_i P\_{0,t}^\*\varepsilon^i
    = \dot{\omega}\_i \varepsilon^i.
\\]
That is, taking \\(X = \gamma'(0)\\), then in terms of this parallel coframe we have the expression \\(\nabla\_{X} \omega = (X\omega\_i) \varepsilon^i\\), which resembles the expression \\(\nabla\_{X} Y = (XY^i)E\_i\\) for a vector field \\(Y\\). This allows us to compute a product rule
\\[
\begin{align}
    X(\omega(Y))
    &= X(\omega\_i Y^i)
    = (X\omega\_i)Y^i + \omega\_i X(Y^i)\\\\\
    &= (X\omega\_i)\varepsilon^i(Y^j E\_j) + \omega\_i \varepsilon^i((XY^j)E\_j)
    = (\nabla\_X \omega)(Y) + \omega(\nabla\_X Y).
\end{align}
\\]
In fact, this product rule provides a convenient characterization of the covariant derivative of covector fields by \\((\nabla\_X \omega)(Y) = X(\omega(Y)) - \omega(\nabla\_X Y)\\).

## Differentiation of tensors

Using identical logic, we can define the covariant derivative of a \\((k,l)\\) tensor \\(T\\) using the parallel transport map to identify the space \\(T^{(k,l)}T\_{\gamma(t)}M\\) with \\(T^{(k,l)}T\_{\gamma(0)}M\\), which will result in the expression
\\[
    \nabla\_X T = (X T^{i\_1 \cdots i\_k}\_{j\_1 \cdots j\_l})E\_{i\_1} \otimes \cdots \otimes E\_{i\_k} \otimes \varepsilon^{j\_1} \otimes \cdots \otimes \varepsilon^{j\_l}
    \tag{1}
    \label{eq:coord}
\\]
where \\(E\_i\\) is a parallel frame so that \\(\nabla\_{X} E\_i = 0\\) and \\(\varepsilon^i\\) is the dual coframe. We will use (\ref{eq:coord}) as our starting point to define covariant differentiation of tensors for now and explain the derivation from the parallel transport map at the end of this section. First take covector fields \\(\omega^1, \cdots, \omega^k\\) and vector fields \\(Y^1, \cdots, Y^l\\) and compute
\\[
\begin{align}
    \nabla\_X(T(\omega^1, \cdots, \omega^k, Y\_1, \cdots, Y\_l))
    &= \nabla\_X(T^{i\_1 \cdots i\_k}\_{j\_1 \cdots j\_l} \omega^1\_{i\_1} \cdots \omega^k\_{i\_k}Y\_1^{j\_1} \cdots Y\_l^{j\_l})\\\\\
    &= (XT^{i\_1 \cdots i\_k}\_{j\_1 \cdots j\_l})\omega^1\_{i\_1} \cdots \omega^k\_{i\_k}Y\_1^{j\_1} \cdots Y\_l^{j\_l}\\\\\
    &+ \sum\_{p=1}^k T^{i\_1 \cdots i\_k}\_{j\_1 \cdots j\_l}\omega^1\_{i\_1} \cdots X\omega^p\_{i\_p} \cdots \omega^k\_{i\_k}Y\_1^{j\_1} \cdots Y\_l^{j\_l}\\\\\
    &+ \sum\_{q=1}^l T^{i\_1 \cdots i\_k}\_{j\_1 \cdots j\_l}\omega^1\_{i\_1} \cdots\omega^k\_{i\_k}Y\_1^{j\_1} \cdots X Y\_q^{j\_q} \cdots Y\_l^{j\_l}\\\\\
\end{align}
\\]
Similarly to the case of covectors, the above reduces the product rule
\\[
\begin{align}
    &\nabla\_X(T(\omega^1, \cdots, \omega^k, Y\_1, \cdots, Y\_l))
    = (\nabla\_X T)(\omega^1, \cdots, \omega^k, Y\_1, \cdots, Y\_l)\\\\\
    &+ \sum\_{p=1}^k T(\omega^1, \cdots, \nabla\_X \omega^p, \cdots, \omega^k, Y\_1, \cdots, Y\_l)
    + \sum\_{q=1}^k T(\omega^1, \cdots, \omega^k, Y\_1, \cdots, \nabla\_X Y\_q, \cdots, Y\_l).
\end{align}
\\]
Note the above product provides a convenient coordinate-free characterization of the covariant derivative of tensor fields in terms of the covariant derivatove of vector and covector fields.

<!-- optional? or perhaps put this earlier... -->

<!-- /\*optional?\*/

\\[
\begin{align}
    \nabla\_{\dot{\gamma}(0)}T
    &:= \left.\frac{d }{d t}\right\|\_{t=0}(P\_{t,0} \otimes \cdots \otimes P\_{t,0} \otimes P^{\*}\_{0,t} \otimes \cdots \otimes P^{\*}\_{0,t})(T)\\\\\
    &= \left.\frac{d }{d t}\right\|\_{t=0}(P\_{t,0} \otimes \cdots \otimes P\_{t,0} \otimes P^{\*}\_{0,t} \otimes \cdots \otimes P^{\*}\_{0,t})(T^{i\_1 \cdots i\_k}\_{j_1 \cdots j\_l} E\_{i\_1} \otimes \cdots \otimes E\_{i\_k} \otimes \varepsilon^{j\_1} \otimes \cdots \otimes \varepsilon^{j\_l})\\\\\
    &= \left.\frac{d }{d t}\right\|\_{t=0} T^{i\_1 \cdots i\_k}\_{j_1 \cdots j\_l}(P\_{t,0} E\_{i\_1} \otimes \cdots \otimes P\_{t,0} E\_{i\_k} \otimes P^{\*}\_{0,t} \varepsilon^{j\_1} \otimes \cdots \otimes P^{\*}\_{0,t} \varepsilon^{j\_l})\\\\\
    &= \dot{T}^{i\_1 \cdots i\_k}\_{j_1 \cdots j\_l}(t) E\_{i\_1} \otimes \cdots \otimes E\_{i\_k} \otimes \varepsilon^{j\_1} \otimes \cdots \otimes \varepsilon^{j\_l}.
\end{align}
\\] -->

<!-- /\*TODO... derive product rule for tensor products? and perhaps give an alternative characterization?\*/ -->