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
Given three vector spaces $V$, $W$, and $X$ a *bilinear map* is a function $b: V \times W \to X$ that is linear in each entry:
* $b(\alpha v + \beta v', w) = \alpha b(v, w) + \beta b(v', w)$
* $b(v, \alpha w + \beta w') = \alpha b(v, w) + \beta b(v, w')$

For example, important operations like the dot product is a bilinear map $\mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ and the cross product is a bilinear map $\mathbb{R}^3 \times \mathbb{R}^3 \to \mathbb{R}^3$.

In linear algebra, we spend much more time studying linear maps than bilinear maps, so it would be nice to turn a bilinear map into linear map between vector spaces. However, this would require expanding our domain $V \times W$ into a single vector space. This is precisely what the *tensor product* $V \otimes W$ is designed to do. The tensor product bundles together two vector spaces $V$ and $W$ into a new vector space $V \otimes W$ so that we can think of a bilinear map $b: V \times W \to X$ as a new linear map $L_b: V \otimes W \to X$. 
1. We want a way to map a bilinear map $b: V \times W \to X$ into a new linear map $L_b: V \otimes W \to X$.
2. Ideally, we would have $V \times W \subset V \otimes W$ so that we can think of a pair $(v,w) \in V \times W$ as being a vector in $V \otimes W$. Let's write this corresponding vector $v \otimes w \in V \otimes W$.
3. We want the new linear map $L_b$ to behave the same as the bilinear map $b$ on $V \times W$. That is, $b(v,w) = L_b(v\otimes w)$.

Let's examine what the tensor product $V \otimes W$ will need to look like to meet our demands. Firstly, $V \otimes W$ is a vector space that contains pairs $v \otimes w$ corresponding to $(v,w) \in V \times W$. But how does addition and scalar multiplication work in this vector space? Firstly, note that for all bilinear maps $L_b$ we require
\\[
\begin{align}
    L_b(v \otimes w + v\otimes w') &= L_b(v \otimes w) + L_b(v \otimes w') &\text{by linearity of } L_b \\\\\
    &= b(v,w)+b(v,w') &\text{by (3) above}\\\\\
    &= b(v,w+w') &\text{by bilinearity of } b\\\\\
    &= L_b(v \otimes (w+w')) &\text{by (3) above}
\end{align}
\\]
The only chance we have to ensure $L_b(v \otimes w + v\otimes w') = L_b(v \otimes (w+w'))$ for *all* bilinear maps $b$ is to declare addition in the tensor product $V \otimes W$ to satisfy
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
Thus we need $L_b(\alpha(w \otimes w)) = L_b((\alpha v) \otimes w)$ for all $b$, which we ensure by declaring
\\[
    \alpha \cdot (v \otimes w) = (\alpha v) \otimes w = v \otimes (\alpha w)
\\]
Collecting our findings, we have
1. $v \otimes w + v\otimes w' = v \otimes (w+w')$
1. $v \otimes w + v'\otimes w = (v+v') \otimes w$
1. $\alpha \cdot (v \otimes w) = (\alpha v) \otimes w = v \otimes (\alpha w)$

Notice that with these rules, there is no way to simplify $v_1 \otimes w_1 + v_2 \otimes w_2$ to a single element of the form $v \otimes w$. But that is fine, we can just declare the whole sum $v_1 \otimes w_1 + v_2 \otimes w_2$ and *all* similar linear combinations to be an element in the vector space $V \otimes W$ to keep it closed under addition. Let's try to combine this all into a definition.

#### What is the tensor product?
Putting together our findings from the previous section, consider the set of (formal) linear combinations of $V \times W$. We can try to formally write this down as
\\[
   S = \\{\alpha_1 v_1 \otimes w_1 + \cdots + \alpha_k v_k \otimes w_k: \alpha_i \in \mathbb{R}, (v_i,w_i) \in V \times W\\}
\\]
However, we also want the following equivalences
1. $v \otimes w + v\otimes w' = v \otimes (w+w')$
1. $v \otimes w + v'\otimes w = (v+v') \otimes w$
1. $\alpha \cdot (v \otimes w) = (\alpha v) \otimes w = v \otimes (\alpha w)$

Thus define an equivalence relation $\sim$ that identifies the above. We then define the tensor product $V \otimes W$ to be the set $S/\sim$ of equivalence classes.

To make $V \otimes W$ a vector space, we add two (equivalence classes of) linear combinations by combining them into a single linear combination:
\\[
    \begin{align}
    &(\alpha_1 v_1 \otimes w_1 + \cdots + \alpha_n v_n \otimes w_n) + (\alpha_1' v_1' \otimes w_1' + \cdots + \alpha_n' v_n' \otimes w_n') \\\\\
    &= \alpha_1 v_1 \otimes w_1 + \cdots \alpha_n v_n \otimes w_n + \alpha_1' v_1' \otimes w_1' + \cdots + \alpha_n' v_n' \otimes w_n'
    \end{align}
\\]
Similarly, we scale linear combination by scaling each term:
\begin{align}
    \beta(\alpha_1 v_1 \otimes w_1 + \cdots + \alpha_n v_n \otimes w_n) = (\beta\alpha_1) v_1 \otimes w_1 + \cdots + (\beta\alpha_n) v_n \otimes w_n.
\end{align}
These definitions of scaling and addition are indeed well-defined and so we have a vector space!
 <!-- However, we have only motivated the definition up until this point, so we should check that this indeed works. -->

<!-- #### Does the tensor product do what it should do?
Given two vector spaces $V$ and $W$, let us recap what the tensor product vector space $V \otimes W$ should do.
1. We want an inclusion $V \times W \hookrightarrow V \otimes W$ where the vector corresponding to $(v,w)$ is denoted $v \otimes w$.
1. For each bilinear map $b: V \times W \to X$, there should exist a unique linear map $L_b: V \otimes W \to X$ such that $L_b(v \otimes w) = b(v,w)$. -->

#### What is the best definition for the tensor product?
The description of the tensor product above is a mouthful and therefore can be difficult to use in practice. However, remember that our goal of the tensor product was to simply translate bilinear maps into linear maps. That is, instead of describing what the tensor product *is* it is much faster to describe what the tensor product *does*. In fact, there is the following alternate definition of the tensor product that defines in to be the unique thing that satisfies a certain "universal property".

**Def.** Given two vector spaces $V$ and $W$, the *tensor product* $V \otimes W$ is the unique vector space such that there is a bilinear inclusion $\iota: V \hookrightarrow W \to V \otimes W$ and the following universal property is satisfies: for any vector space $X$ and bilinear map $b: V \times W \to X$, there is a unique linear map $L_b: V \otimes W \to X$ such that $L_b \circ \iota = b$.

While this definition is quick, it still remains to prove that the tensor product under this definition exists and that it is unique. The proof of existence uses the 


The proof of uniqueness uses the construction we made in the previous section, so we have already done most of the work! The requirement of an inclusion map $\iota: V \times W \to V \otimes W$ is provided by the correspondence $\iota: (v,w) \mapsto v \otimes w$ described earlier. Hence the requirement that $L_b \circ \iota = b$ is precisely that $L_b(v \otimes w) = b(v,w)$, which is what motivated our previous construction. However, our previous discussion what only motivation and is not a substitute for a formal proof, but you are now prepared to consult a linear algebra textbook for formal proofs of the existence and uniqueness of the tensor product when defined with the universal property.