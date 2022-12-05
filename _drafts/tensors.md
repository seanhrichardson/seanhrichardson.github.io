---
layout: page
section: NOTES
title: S2
permalink: /tensors.html
---
## Tensors

<!-- Given vector spaces $V$, $W$, and $X$ we can consider the set $L(V,W;X)$ of *all* bilinear maps $V \times W \to X$. In fact, because a bilinear map $T$ is a function, we can scale it by a real number $\alpha$ to get a new bilinear map $\alpha T$ by the simple rule
\\[
    (\alpha T)(v,w) = \alpha \cdot T(v,w).
\\]
Similarly, we can add two different bilinear maps $T$ and $T'$ together to get a new bilinear map $T+T'$ defined by the rule
\\[
    (T+T')(v,w) = T(v,w) + T'(v,w).
\\]
Because we can nicely scale and add elements of the set of bilinear maps $L(V,W;X)$, we can think of $L(V,W;X)$ as a vector space, which is very useful! -->

#### What should the tensor product do?
Given three vector spaces $V$, $W$, and $X$ a *bilinear map* is a function $T: V \times W \to X$ that is linear in each entry:
* $b(\alpha v + \beta v', w) = \alpha b(v, w) + \beta b(v', w)$
* $b(v, \alpha w + \beta w') = \alpha b(v, w) + \beta b(v, w')$

For example, important operations like the dot product and cross product are bilinear maps.

We want the tensor product to bundle together two vector spaces $V$ and $W$ into a new vector space $V \otimes W$ so that we can think of a bilinear map $b: V \times W \to X$ as a new linear map $L_b: V \otimes W \to X$. This would be quite helpful because we know more about bilinear maps than linear maps. Formally,
1. We want a way to map a bilinear map $b: V \times W \to X$ into a new linear map $L_b: V \otimes W \to X$.
2. Hopefully a pair $(v,w) \in V \times W$ will have a corresponding element $v \otimes w \in V \otimes W$.
3. Ideally, $b(v,w) = L_b(v\otimes w)$.

Let's examine what the tensor product $X \times Y$ will need to look like to meet our demands. Firstly, it is a vector space that contains pairs $v \otimes w$ corresponding to $(v,w) \in V \times W$. But how does addition and scalar multiplication work in this vector space? Firstly, note that for all bilinear maps $L_b$ we require
\\[
\begin{align}
    L_b(v \otimes w + v\otimes w') &= L_b(v \otimes w) + L_b(v \otimes w) &\text{by linearity of } L_b \\\\\
    &= b(v,w)+b(v,w') &\text{by (3) above}\\\\\
    &= b(v,w+w') &\text{by bilinearity of } b\\\\\
    &= L_b(v \otimes (w+w')) &\text{by (3) above}
\end{align}
\\]
The best way to ensure $L_b(v \otimes w + v\otimes w') = L_b(v \otimes (w+w'))$ for *all* bilinear maps $b$ is to declare addition in the tensor product $V \otimes W$ to satisfy
\\[
    v \otimes w + v\otimes w' = v \otimes (w+w').
\\]
For the same reason we declare
\\[
    v \otimes w + v'\otimes w = (v+v') \otimes w.
\\]
Now let's examine scalar multiplication with the same strategy. We find that
\\[
\begin{align}
    L_b(\alpha(w \otimes w)) = \alpha L_b(v \otimes w) = \alpha b(v,w) = b(\alpha v, w) = L_b((\alpha v) \otimes w)
\end{align}
\\]
Thus we need $L_b(\alpha(w \otimes w)) = L_b((\alpha v) \otimes w)$ for all $b$, which can best ensure by declaring
\\[
    \alpha \cdot (v \otimes w) = (\alpha v) \otimes w = v \otimes (\alpha w)
\\]
Collecting our findings, we have
1. $v \otimes w + v\otimes w' = v \otimes (w+w')$
1. $v \otimes w + v'\otimes w = (v+v') \otimes w$
1. $\alpha \cdot (v \otimes w) = (\alpha v) \otimes w = v \otimes (\alpha w)$

Notice that with these rules, there is no way to simplify $v_1 \otimes w_1 + v_2 \otimes w_2$ to a single element of the form $v \otimes w$. But that is fine, we just declare the whole sum $v_1 \otimes w_1 + v_2 \otimes w_2$ and *all* similar linear combinations to be an element in the vector space $V \otimes W$ to keep it closed under addition. We define this in the next section.

#### What is the tensor product?
Putting together our findings from the previous section, consider the set of (formal) linear combinations of $V \times W$. Formally, this is the set
\\[
   S = \\{\alpha_1 v_1 \otimes w_1 + \cdots \alpha_n v_n \otimes w_n: \alpha_i \in \mathbb{R}, (v_i,w_i) \in V \times W\\}
\\]
However, we also want the following equivalences
1. $v \otimes w + v\otimes w' = v \otimes (w+w')$
1. $v \otimes w + v'\otimes w = (v+v') \otimes w$
1. $\alpha \cdot (v \otimes w) = (\alpha v) \otimes w = v \otimes (\alpha w)$

Thus define an equivalence relation $\sim$ that identifies the above. We then define the tensor product $V \otimes W$ to be the set $S/\sim$ of equivalence classes.

To make $V \otimes W$ a vector space, we add two linear combinations by combining them into a single linear combination:
\\[
    \begin{align}
    &(\alpha_1 v_1 \otimes w_1 + \cdots + \alpha_n v_n \otimes w_n) + (\alpha_1' v_1' \otimes w_1' + \cdots + \alpha_n' v_n' \otimes w_n') \\\\\
    &= \alpha_1 v_1 \otimes w_1 + \cdots \alpha_n v_n \otimes w_n + \alpha_1' v_1' \otimes w_1' + \cdots + \alpha_n' v_n' \otimes w_n'
    \end{align}
\\]
Similarly, we scale linear combination by scaling each term:
\begin{align}
    \beta(\alpha_1 v_1 \otimes w_1 + \cdots + \alpha_n v_n \otimes w_n) = (\beta\alpha_1) v_1 \otimes w_1 + \cdots + (\beta\alpha_n) v_n \otimes w_n
\end{align}

#### What is the best definition for the tensor product?
The description of the tensor product above is a mouthful and therefore can be difficult to use in practice. However, remember that our goal of the tensor product was to simply translate bilinear maps into linear maps. That is, instead of describing what the tensor product *is* it is much faster to describe what the tensor product *does*. In fact, there is the following alternate definition of the tensor product that defines in to be the unique thing that satisfies a certain "universal property".

**Def.** Given two vector spaces $V$ and $W$ the *tensor product* $V \otimes W$ is the unique vector space such that there is a bilinear inclusion $\iota: V \times W \to V \otimes W$ and the following universal property is satisfies: for any vector space $X$ and bilinear map $b: V \times W \to X$, there is a unique linear map $L_b: V \otimes W \to X$ such that $L_b \circ \iota = b$.

While this definition is quick, it still remains to prove that the tensor product exists and that it is unique. The proof of uniqueness uses the construction we made in the previous section, so we have already done most of the work! The requirement of an inclusion map $\iota: V \times W \to V \otimes W$ is provided by the correspondence $\iota: (v,w) \mapsto v \otimes w$ described earlier. Hence the requirement that $L_b \circ \iota = b$ is precisely that $L_b(v \otimes w) = b(v,w)$, which is what motivated our previous construction. However, our previous discussion what only motivation and is not a substitute for a formal proof, but you are now prepared to consult a linear algebra textbook for formal proofs of the existence and uniqueness of the tensor product when defined with the universal property.