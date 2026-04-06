---
layout: page
section: TOPOLOGY
title: Topology
---


# Introduction to Topology
<!-- GIVE A LITTLE INTRODUCTION HERE AND PERHAPS SOME NICE ANIMATIONS GIVING INTUITION OF TOPOLOGY -->

<!-- will give some background and ideas that are important to meaninfully study topology while motivating the formal definition -->

<!-- by the time we get to the end, you will understand why the definition of topology is the "correct" definition... this is the goal. -->

<!-- As part of the introduction, give the definition of a topological space and emphasize that the point of these notes / this video is to explain where this definitioin comes from, what it means, and why it is natural. -->

<!-- Also mention that this "motivation" lesson can be watched any time and you do not necessarily need to understand all the ideas... However, this is a complete motivation... -->

## Continuous functions on the real numbers
Topology is designed to study continuous functions. Intuitively, a continuous function \\(f: \mathbb{R} \to \mathbb{R}\\) with inputs and outputs on the real numbers \\(\mathbb{R}\\) is a function without any "jumps" or as a function that you can draw without lifting your pen from the paper. Many useful functions that arise often in practice are continuous:

/\*animation that phases through \\(x^2, e^x, 2x \\), arbitrary continuous looking function.\*/

A function is "continuous" if a small change to \\(x\\) only results in a small change in \\(f(x)\\). If a very small change in \\(x\\) can result in a large change in \\(f(x)\\), then this is when we have a "jump" so the function is "discontinuous".

/\*TODO: animation that phases through discontinuous functions\*/

The definition of continuity simply formalizes this concept. Recall we say a function \\(f: \mathbb{R} \to \mathbb{R}\\) is ***continuous at \\(\mathbf{x\_0}\\)*** if for every small \\(\varepsilon > 0\\), there is a small \\(\delta > 0\\) so that \\(\|x-x_0\| < \delta\\) ensures \\(\|f(x) - f(x\_0)\| < \varepsilon\\). In other words, this definition says if we specify some small positive value \\(\varepsilon > 0\\), we can always find a small positive value \\(\delta\\) so that changing \\(x\\) by \\(\delta\\) changes \\(f(x)\\) by no more than \\(\varepsilon\\), which formalizes this "small change to \\(x\\) only results in a small change to \\(f(x)\\)" philosphy. If \\(f: \mathbb{R} \to \mathbb{R}\\) is continuous at every input point \\(x\_0 \in \mathbb{R}\\), then we say the whole function \\(f\\)  is ***continuous***. 

/\*TODO: animate this... perhaps using one of the examples from above?\*/

**Exercise.**  Verify that \\(f(x) = 2x\\) is continuous.

**Exercise.**
Argue that the following function \\(f: \mathbb{R} \to \mathbb{R}\\) is *not* continuous.
\\[
    f(x) =
    \begin{cases}
        x - 1   \quad   \text{if}   \quad   x \leq 0,\\\\\
        x + 1   \quad   \text{if}   \quad   x > 0.
    \end{cases}
\\]

<!-- BELOW COULD BE SAID OUTLOUD? -->

<!-- Note if a function \\(f: \mathbb{R} \to \mathbb{R}\\) is continuous at \\(x\_0\\) and we want to approximate the value of \\(f(x\_0)\\) to within some designated small error \\(0.1\\), then there will be some \\(\delta > 0\\) so that \\(f(x)\\) is a satisfactory approximation so long as \\(x\\) is within \\(\delta\\) of \\(x\_0\\). Thus continuous functions are extremely useful for practical applications such as /\*TODO: list some approximation\*/.  -->

<!-- An important property of continuous functions is that outputs converge in a predictable way: the limit of a sequence of output is simply the output of the limit of the inputs. That is, if we have some convergent sequence \\(x_n \to x\\), then we have convergence \\(f(x_n) \to f(x)\\). 

/\*TODO: animate this concept\*/

In fact, this property is an equivalent definition of continuity, which you can try to prove in the challenging exercise below. This predictable convergence allows for outputs of continuous functions to be easily approximated (which has practical applications), and is important in calculus as limits are the basis of calculus.

**Exercise (challenging).** Prove a function \\(f: \mathbb{R} \to \mathbb{R}\\) is continuous at \\(x\_0\\) if and only if for every convergent sequence \\(x\_n \to x\_0\\), we have \\(f(x\_n) \to f(x\_0)\\). -->

## Continuous functions on higher dimensional Euclidean space

More generally, we can consider functions \\(f: \mathbb{R}^m \to \mathbb{R}^n\\) from Euclidean space of dimension \\(m\\) to that of dimension \\(n\\). For example, consider the following function \\(f: \mathbb{R}^2 \to \mathbb{R}\\).

/\*TODO: function that approximates elevation chart of Tahoma and animate\*/

As animated above, slightly changing the input still only results in a small change in output, so we should also consider this function to be "continuous". We can similarly consider the function \\(R: \mathbb{R}^2 \to \mathbb{R}^2\\) given by \\(R(x,y) = (-y, x)\\), which rotates the plane by \\(\pi/2\\) and observe a small change in input only results in a small change in output.

/\*animate this\*/

To define continuity formally, we first recall the Euclidean distance between two points \\(x, y \in \mathbb{R}^n\\) for \\(x = (x\_1, \cdots, x\_n)\\) and \\(y = (y\_1, \cdots, y\_n)\\) is given by the Pythagorean formula
\\[
    d(x,y) = \sqrt{(x\_1 - y\_1)^2 + \cdots + (x\_n - y\_n)^2}.
\\]

Now we define a function \\(f: \mathbb{R}^m \to \mathbb{R}^n\\) to be ***continuous*** at \\(x\_0 \in \mathbb{R}^m\\) if for every \\(\varepsilon > 0\\), there exists some \\(\delta > 0\\) so that \\(d(x,x_0) < \delta\\) ensures \\(d(f(x),f(x\_0)) < \varepsilon\\). If \\(f: \mathbb{R} \to \mathbb{R}\\) is continuous at every input point \\(x\_0 \in \mathbb{R}^m\\), then we say the whole function \\(f\\)  is ***continuous***. 

**Exercise.**
Verify the rotation \\(R: \mathbb{R}^2 \to \mathbb{R}^2\\) given by \\(R(x,y) = (-y, x)\\) is continuous.

**Exercise.**
Show the following function \\(f: \mathbb{R}^2 \to \mathbb{R}^2\\) is *not* continuous:
\\[
    f(x, y) =
    \begin{cases}
        (x-1, y) \quad \text{if} \quad x < 0, \\\\\
        (x+1, y) \quad \text{if} \quad x \geq 0.
    \end{cases}
\\]
/\*TODO: animate this function\*/

Note this distance function has several important properties. For any points \\(x, y, z \in \mathbb{R}^n\\), it satisfies
<!-- TODO: possibly interpret these -->
1. Non-negativity: \\(d(x,y) \geq 0\\).
2. Definiteness: \\(d(x,y) = 0\\) if and only if \\(x = y\\). 
3. Symmetry: \\(d(x,y) = d(y, x)\\). 
4. Triangle Inequality: \\(d(x, y) + d(y, z) \leq d(x,z)\\).

/\*animation for triangle inequality\*/

## Metric Spaces

Note all we need to define continuity is a notion of distance. A "metric space" is simply a set \\(X\\) with some notion of distance, which will allow us to define continiuty. Formally, given a set \\(X\\), a function \\(d: X \times X \to \mathbb{R}\\) is called a ***metric*** if for all \\(x, y, z \in X\\), it behaves like a distance function:
1. Non-negativity: \\(d(x,y) \geq 0\\).
2. Definiteness: \\(d(x,y) = 0\\) if and only if \\(x = y\\). 
3. Symmetry: \\(d(x,y) = d(y, x)\\). 
4. Triangle inequality: \\(d(x, y) + d(y, z) \leq d(x,z)\\).

Then the pairing of the set \\(X\\) together with the metric \\(d\\) is called a ***metric space***. Sometimes we write this pairing by \\((X, d)\\).

For example, Euclidean space \\(\mathbb{R}^n\\) together with the Euclidean distance function defined above is a metric space. As a second example, the ***taxicab metric*** \\(d_1: \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}\\) is defined by
\\[
    d_1(x,y) = \|x\_1 - y\_1\| + \|x\_2 - y\_2\|
\\]
for \\(x = (x\_1, x\_2)\\) and \\(y = \(y\_1, y\_2)\\).

**Excercise.** Prove the taxicab metric is a metric on \\(\mathbb{R}^2\\).

<!-- hide the below... -->

**Solution.** For any \\(x, y, z \in \mathbb{R}^2\\), compute:
1. Non-negativity:
\\[
    d\_1(x,y) = \|x\_1 - y\_1\| + \|x\_2 - y\_2\| \geq 0.
\\]
2. Definiteness:
\\[
    d\_1(x,y) = 0 \iff \|x\_1 - y\_1\| + \|x\_2 - y\_2\| = 0 \iff x\_1 = y\_1, x\_2 = y\_2 \iff x=y.
\\]
3. Symmetry:
\\[
    d\_1(x,y) = \|x\_1 - y\_1\| + \|x\_2 - y\_2\| = \|y\_1 - x\_1\| + \|y\_2 - x\_2\| = d\_1(y, x).
\\]
4. Triangle Inequality: use the inequality \\(\|a + b\| \leq \|a\| + \|b\|\\) to compute
\\[\begin{align}
    d\_1(x,z) &= \|x\_1 - z\_1\| + \|x\_2 - z\_2\| \\\\\
    &= \|(x\_1 - y\_1) + (y\_1 - z\_1)\| + \|(x\_2 - y\_2) + (y\_2 - z\_2)\| \\\\\
    &\leq \|x\_1 - y\_1\| + \|y\_1 - z\_1\| + \|x\_2 - y\_2\| + \|y\_2 - z\_2\|\\\\\
    &\leq \|x\_1 - y\_1\| + \|x\_2 - y\_2\| + \|y\_1 - z\_1\| + \|y\_2 - z\_2\|\\\\\
    &= d(x,y) + d(y,z).
\end{align}\\]

Given metric spaces \\((X, d_X)\\) and \\((Y, d_Y)\\), we say a map \\(f: X \to Y\\) between two metric spaces is ***continuous*** at \\(x_0 \in X\\) if for all \\(\varepsilon > 0\\), there exists \\(\delta > 0\\) so that
\\( d\_X(x, x\_0) < \delta\\) implies \\(d\_Y(f(x), f(x\_0)) < \varepsilon\\).

**Example.** Any continuous function \\(f: \mathbb{R}^n \to \mathbb{R}^m\\) is continuous as a function between metric spaces with the Euclidean metric (because the definitions are the same).

**Exercise.** Prove the rotation map \\(f: \mathbb{R}^2 \to \mathbb{R}^2\\) given by \\(f(x,y) = (-y, x)\\) is continuous if \\(\mathbb{R}^2\\) (both the domain and codomain) is given the taxicab metric.

**Solution.** 
Fix \\(x\_0 = (x\_1, x\_2) \in \mathbb{R}^2\\) and \\(\varepsilon > 0\\). Then note for \\(y = (y\_1, y\_2) \in \mathbb{R}^2\\):
\\[
\begin{align}
    d(f(x\_0), f(y)) 
    &= d((-x\_2, x\_1), (-y\_2, y\_1))\\\\\
    &= \|(-x\_2 - (-y\_2))\| + \|x\_1 - y\_1\|\\\\\
    &= \|x\_1 - y\_1\| + \|x\_2 + y\_2\|\\\\\
    &= d(x\_0, y).
\end{align}
\\]
Thus if \\(d(x\_0, y) < \varepsilon\\), then \\(d(f(x\_0, f(y))) < \varepsilon\\).
*Note in this simple example, "the \\(\delta\\)" is equal to \\(\varepsilon\\).*

Given a metric space \\((X, d)\\), we define the ***open ball*** of radius \\(r\\) centered at \\(x\_0 \in X\\) as the set of all points that are of distance less than \\(r\\) to \\(x\_0\\):
\\[
    B\_r(x\_0) := \\{x \in X : d(x, x\_0) < r\\}
\\]

**Example.** In the metric space \\(\mathbb{R}^2\\) with the Euclidean metric \\(d\_2\\), consider the open ball of radius \\(1\\) centered at the origin \\((0,0)\\). Then because 
\\[
    d\_2((x\_1, x\_2), (0,0)) = (x\_1 - 0)^2 + (x\_2 - 0)^2 = x\_1^2 + x\_2^2,
\\]
this open ball is the set
\\[
    B^{d\_2}\_1((0,0)) = \\{(x\_1, x\_2) \in \mathbb{R}^2 : x\_1^2 + x\_2^2 < 1\\}.
\\]
That is, this set is the standard open ball of radius \\(1\\) centered at the origin:

/\*illustrate the above\*/

**Exercise.** In the metric space \\(\mathbb{R}^2\\), draw the open ball of radius \\(1\\) centered at \\((0,0)\\) with respect to the taxicab metric \\(d\_1\\).

**Solution.** Note
\\[
    d\_1((x\_1, x\_2), (0,0)) = \|x\_1 - 0\| + \|x\_2 - 0\| = \|x\_1\| + \|x\_2\|.
\\]
Therefore, this open ball is the set
\\[
    B^{d\_1}\_1((0,0)) = \\{(x\_1, x\_2) \in \mathbb{R}^2 : \|x\_1\| + \|x\_2\| < 1\\}.
\\]
Visually, this is a rotated square of sidelength \\(\sqrt{2}\\) centered at the origin:

/\*illustrate the above\*/

**Exercise.** Prove a function \\(f: X \to Y\\) between metric spaces \\((X, d\_X)\\) and \\((Y, d\_Y)\\) is continuous at \\(x\_0 \in X\\) if and only if for all \\(\varepsilon > 0\\), there exists \\(\delta > 0\\) such that
\\[
    f^{-1}(B_{\varepsilon}(f(x\_0))) \subset B_{\delta}(x\_0).
\\]

**Solution.** 

**Exercise (challenge).** 
Is it possible to find a metric space \\((X, d)\\) and a function \\(f: X \to \mathbb{R}^2\\) or \\(f: \mathbb{R}^2 \to X\\) so that any of the following are possible?
1. \\(f: X \to \mathbb{R}^2\\) is continuous with the Euclidean metric \\(d\_2\\), but not the taxicab metric \\(d\_1\\).
2. \\(f: X \to \mathbb{R}^2\\) is continuous with the taxicab metric \\(d\_1\\), but not the Euclidean metric \\(d\_2\\).
3. \\(f: \mathbb{R}^2 \to X\\) is continuous with the Euclidean metric \\(d\_2\\), but not the taxicab metric \\(d\_1\\).
4. \\(f: \mathbb{R}^2 \to X\\) is continuous with the taxicab metric \\(d\_1\\), but not the Euclidean metric \\(d\_2\\).

**Solution.** No -- such a function is impossible in every case. Let \\((X, d)\\) be any metric space, and first suppose \\(f: \mathbb{R}^2 \to X\\) is continuous with respect to \\(d\_2\\). Then by definition, for each \\(x\_0 \in \mathbb{R}^2\\) and any \\(\varepsilon > 0\\), there exists some \\(\delta > 0\\) such that \\(d_2(x\_0, x) < \delta\\) guarantees \\(d(f(x\_0), f(x)) < \varepsilon\\). However, note \\(B^{d\_1}\_{\delta}(x\_0) \subset B^{d\_2}\_{\delta}(x\_0)\\) as pictured below:

/\*(picture)\*/

Therefore, \\(d\_1(x\_0, x) < \delta\\) implies \\(d\_2(x\_0, x) < \delta\\), which in turn implies \\(d(f(x\_0), f(x)) < \varepsilon\\) and so \\(f: \mathbb{R}^2 \to X\\) will also be continuous with respect to \\(d\_1\\). 
<!--  -->
Similary, suppose \\(f: X \to \mathbb{R}^2\\) is continuous with respect to \\(d\_1\\) and fix \\(x\_0 \in X\\) and \\(\varepsilon > 0\\). Then by definition there exists \\(\delta > 0\\) such that \\(d(x\_0, x) < \delta\\) implies \\(d_1(f(x\_0), f(x)) < \varepsilon\\), but by \\(B^{d\_1}\_{\varepsilon}(x\_0) \subset B^{d\_2}\_{\varepsilon}(x\_0)\\), this in turn implies \\(d_2(f(x\_0), f(x)) < \varepsilon\\) and therefore \\(f: X \to \mathbb{R}^2\\) is continuous with repsect to \\(d\_2\\).

we will argue \\(d\_1(x\_0, x) < \delta\\) implies \\(d\_2(x\_0, x) < \delta\\), which would imply \\(d(f(x\_0), f(x)) < \varepsilon\\) and therefore \\(f: \mathbb{R}^2 \to X\\) has to also be continuous with respect to the taxicab metric. Indeed, visually we can see the set of all points \\(x\\) with \\(d\_1(x\_0, x) < \delta\\) is a subset of the set of all points with 
/\*\*/
\\[
\begin{align}
    d\_1(x,y)^2 &= (\|x\_1 - y\_1\| + \|x\_2 - y\_2\|)^2\\\\\
    &= (x\_1 - x\_2)^2 + 2\|x\_1 - y\_1\| \cdot \|x\_2 - y\_2\| + (y\_1 - y\_2)^2\\\\\
    &\leq (x\_1 - x\_2)^2 + (y\_1 - y\_2)^2
    = d\_2(x,y)^2.
\end{align}
\\]

A subset \\(U \subset X\\) is ***open*** if for every \\(x \in U\\), there exists some small \\(\varepsilon > 0\\) so that \\(B_{\varepsilon}(x) \subset U\\). 

Open sets are useful because they provide an alternative characterization of continuity:

**Theorem.** A function \\(f: X \to Y\\) between two metric spaces is continuous if and only if for every open subset \\(U \subset Y\\), the preimage \\(f^{-1}(U) \subset X\\) is open.

/\*TODO: illustrate this to give intuition\*/

/\*prove this theorem\*/

Thus the only necessary data to determine if a function is continuous between two metric spaces is the collection of open sets in each space. Given a metric space \\(X\\), the collection of all open sets
\\[
    \mathcal{T} = \\{U \subset X : U \text{ is open}\\}
\\]
is called the ***topology*** of \\(X\\). Note \\(\mathcal{T}\\) is a subset of the power set \\(\mathcal{P}(X)\\) of \\(X\\). Finally, note the collection of open sets satisfy the following important properties.

**Prop.** Let \\((X, d)\\) be a metric space. Then:
1. The union of open sets of \\(X\\) is an open set.
2. The finite intersection of open sets of \\(X\\) is open.
3. The empty set \\(\varnothing\\) and the entire set \\(X\\) are both open.

*Proof.* 
/\*TODO\*/

/\*todo mention Euclidean metric and taxicab have the same open sets and therefore same topology\*/

## Topological Spaces

Again, the only necessary data to determine if a function is continuous between two metric spaces is the collection of open sets in each space; that is, the topology. A "topological space" generalizes metric spaces by only giving a set a topology and nothing else, which is sufficient to define continuity (in fact, we will see later that a topology is in some sense the *minimal* possible data we can give to define continuity).
<!-- removing extraneous information is useful and clarifying... -->

A ***topological space*** is a set \\(X\\) together with a collection \\(\mathcal{T} \subset \mathcal{P}(X)\\) (called the ***topology***) of subsets of \\(X\\) (called the ***open sets***) that satisfy
1. Given any collection \\(\\{U_{\alpha}\\}\_{\alpha \in A} \subset \mathcal{T}\\) of open sets, their union is open: \\(\bigcup_{\alpha \in A} U_{\alpha} \in \mathcal{T}\\).
2. Given a finite collection \\(U_1, \cdots, U_n\\) of open sets, their intersection is open: \\(\bigcap\_{i = 1}^n U\_{i} \in \mathcal{T}\\).
3. The open set is open and the entire space is open: \\(\varnothing, X \in \mathcal{T}\\).

/\*any metric space example... again note Euclidean and taxicab are the same as topological spaces... define the metric space\*/

As another example, consider the ***Sierpiński topology*** on the set \\(X = \\{0, 1\\}\\) given by the topology \\(\mathcal{T} = \\{\varnothing, \\{1\\}, \\{1,2\\}\\}\\).

**Exercise.** Verify the Sierpiński topology satisfies the definition of a topology.

While many topological spaces arise as the metric topology of some metric, there are also many useful topological spaces that do not correspond to the metric topology of any metric space. Indeed, the Sierpiński topology is an instance of this.

**Exercise.** Argue there is no metric on \\(X = \\{0,1\\}\\) whose metric topology is the Sierpiński topology.

The following definition of continuity should not be a surprise as this is the motivation for the notion of a topological space. We say a map \\(f: X \to Y\\) between topological spaces is ***continuous*** if for every open subset \\(U \subset Y\\), its preimage \\(f^{-1}(U)\\) is open.

**Exercise.** Given any topological spaces \\(X\\) and \\(Y\\), prove that the constant map \\(f: X \to Y\\) given by \\(f(x) = y\\) for some fixed \\(y \in Y\\) is continuous.

Given any set \\(Y\\), the ***trivial topology*** is the topology \\(\mathcal{T} = \\{\varnothing, Y\\}\\). That is, only the empty set \\(\varnothing\\) and the full space are open.

**Exercise.** Verify the trivial topology satisfies the definition of a topology.

**Exercise.** Given a set \\(Y\\) with the trivial topology and any topological space \\(X\\), prove any map \\(f: X \to Y\\) is continuous.

**Exercise.** Prove that if \\(X\\) has at least two elements, the trivial topology is not the metric topology of any metric on \\(X\\).

Given any set \\(X\\), the ***discrete topology*** is simply the power set \\(\mathcal{T} = \mathcal{P}(X)\\). That is, every set is open.

**Exercise.** Verify the discrete topology on a set \\(X\\) satisfies definition of a topology.

**Exercise.** Given a set \\(X\\) with the discrete topology and any topological space \\(Y\\), prove any map \\(f: X \to Y\\) is continuous.

## On the definition of topological spaces

In this section, I remark on why the definition of a topological space is natural and important to study.
First, recall the definition of topology required open sets to satisfy three properties:
1. the union of open sets is open,
2. the finite intersection of open sets is open, and
3. the empty set and the full space are open.

These are natural properties to require as the collection of open sets in any metric space satisfy these three properties. However, these properties are in fact essential for the definition of continuity in a topological space to be a meaningful definition of continuity for metric spaces. To see this, first observe the following:

**Exercise.** If \\(f: X \to Y\\) is a map between sets and \\(\\{U_{\alpha}\\}_{\alpha \in A} \subset Y\\) is a collection of sets in Y, then:
1. \\(f^{-1}(\bigcup_{\alpha \in A} U_{\alpha}) = \bigcup_{\alpha \in A}f^{-1}(U_{\alpha})\\),
2. \\(f^{-1}(\bigcap_{\alpha \in A} U_{\alpha}) = \bigcap_{\alpha \in A}f^{-1}(U_{\alpha})\\), and
3. \\(f^{-1}(Y) = X\\) and \\(f^{-1}(\varnothing) = \varnothing\\).

Considering the above results, suppose \\(X\\) is a topological space, \\(Y\\) is any metric space, and \\(f: X \to Y\\) is any continuous function. Then, because \\(\varnothing\\) and \\(Y\\) are open in \\(Y\\), the definition of continuity forces \\(X = f^{-1}(Y)\\) and \\(\varnothing = f^{-1}(\varnothing)\\) to be open in \\(X\\). It is for this reason we definethe empty set and the full space to be open; if they were not open, this would be an obstruction to there existing *any* continuous function \\(f: X \to Y\\) to a metric space \\(Y\\). Similarly, because open sets are closed under unions and finite intersections in metric spaces, points by points (1) and (2) above, we should require these same conditions in our definition of a topological space; otherwise, this would be an obstruction to defining continuous functions into metric spaces.
<!-- 
in this second case, there still could be continuous functions, but this would make them hard to define...
also, note historically, topology was originally defined with more conditions on the open sets, but over time this was found to be the most general definition that still has enough structure.
-->

Next, I follow up with the claim that, in some sense, a topology is the minimal necessary information to determine if a function is continuous. This is not true for metric spaces: we saw the Euclidean metric on \\(\mathbb{R}^2\\) and the taxicab metric on \\(\mathbb{R}^2\\) will result in exactly the same functions \\(f: X \to \mathbb{R}^2\\) and \\(g: \mathbb{R}^2 \to X\\) being continuous. However, knowledge of all continuous maps out of a topological space uniquely determines the topology by the following exercise.

**Exercise (challenge).** Suppose we give a set \\(X\\) two topologies so that \\(f: X \to Y\\) is continuous in the first topology if and only if \\(f: X \to Y\\) is continuous with respect to the second topology for all topological spaces \\(Y\\) and all functions \\(f: X \to Y\\). Then, the two topologies are identical.

/\*prove this using Sierpiński topology... perhaps first give a hint?\*/

/\*TODO: little conclusion on applications of topology... function spaces, manifolds, \*/