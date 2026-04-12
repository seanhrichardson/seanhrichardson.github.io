---
layout: page
title: Topology
---

<!-- TODO: -->
<!-- all visuals -->
<!-- hide solutions -->

<!-- FIX NOTATION: -->
<!-- perhaps decide between d_1, d_2 vs. d, d' and make this standard -->

# Topology

/\*historical / visual / intuitive introduction\*/

/\*motivate/emphasize "continuous" functions...\*/

## Topological equivalence of metric spaces

<!-- NOTE: REQUIRE METRIC SPACES AS A PRE-REQ FOR THIS... REVIEWING METRIC SPACES IS NOT A "STORY" AND I WANT TO TELL A STORY... -->

The motivation for topology is in acquiring a better understanding of "continuous maps" between metric spaces. Recall a metric space is a set \\(X\\) together with some "metric" \\(d: X \times X \to \mathbb{R}\\) that computes the distance between two points and satisfies the metric space axioms. 
<!-- link to metric space page... -->
For example, the Euclidean plane \\(\mathbb{R}^2\\) together with the ***Euclidean metric*** \\(d\_2: \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}\\) defined by
\\[
    d\_2((x\_1, y\_1), (x\_2, y\_2)) = \sqrt{(x\_2 - x\_1)^2 + (y\_2 - y\_1)^2}
\\]
forms a metric space. This metric encodes our typical understanding of two-dimensional distance. 

/\*visual for this Euclidean plane\*/

As a second example of a metric space, consider the Euclidean plane \\(\mathbb{R}^2\\), but now with the ***taxicab metric*** \\(d\_1: \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}\\) defined by
\\[
    d\_1((x\_1, y\_1), (x\_2, y\_2)) = \|x\_2 - x\_1\| + \|y\_2 - y\_1\|.
\\]
Note this metric encodes the distance required to travel between two points if we are only allowed to move in the coordinate directions --- similar to how taxicabs in a city can only move in the direction of the street grid, which is where this metric gets its name. 

/\*visual for taxicab\*/

The most fundamental example of a metric space is the real line \\(\mathbb{R}\\) with metric \\(d(x\_1,x\_2) = \|x\_2-x\_1\|\\), which is simply the standard distance between two points \\(x\\) and \\(y\\) on the number line.

/\*visual for real number line\*/

Intuitively, a function is "continuous" if nearby points are mapped to nearby points: there is no "tearing" in which points are "ripped" away from eachother. For a function \\(f \colon X \to Y\\) from a metric space \\((X, d\_X)\\) to another metric space \\((Y, d\_Y)\\), recall continuity can be formally defined. A function \\(f: X \to Y\\) is ***continuous*** if for every \\(x \in X\\) and \\(\varepsilon > 0\\), we can find some \\(\delta > 0\\) such that \\(d\_X(x, z) < \delta\\) implies \\(d\_Y(f(x), f(x)) < \varepsilon\\).

<!-- note: can change this projection to x or y in the video... whatever works better. -->
**Example.** Consider the projection function \\(\pi: \mathbb{R}^2 \to \mathbb{R}\\) defined by \\(\pi(x, y) = y\\). Then this is continuous as a function from the metric space \\((\mathbb{R}^2, d\_2)\\) with the Euclidean metric to \\(\mathbb{R}\\) with the standard metric.

<details markdown="1">
<summary><i>Solution.</i></summary>
To see that \\(\pi\\) is continuous, consider any point \\((x,y) \in \mathbb{R}^2\\) and some small \\(\varepsilon > 0\\). Then we want to find some small \\(\delta\\) so that \\(d_2((x,y), (x', y)) < \delta\\) gurantees \\(d(\pi((x,y)),\pi((x', y'))) < \varepsilon\\). It helps to study this map visually:

/\*give visual representation of the balls\*/.

From the above visuals, we can see the choice of taking \\(\delta\\) to be \\(\varepsilon\\) itself should work. Indeed, note that if
\\(d_2((x,y), (x', y)) < \varepsilon\\), then because \\(\|y-y'\|^2 \leq (x-x')^2 + (y-y')^2\\), we find that
<!-- perhaps should explain the below more... -->
\\[
    \|y-y'\| \leq \sqrt{(x-x')^2 + (y-y')^2}.
\\]
But then by our definition of the metric \\(d\_2\\) together with our assumption of \\(d_2((x,y), (x', y)) < \varepsilon\\), we find 
\\[
    \|y-y'\| \leq \sqrt{(x-x')^2 + (y-y')^2} = d_2((x,y), (x', y)) < \varepsilon.
\\]
And therefore \\(\|y-y'\| < \varepsilon\\). This is exactly what we want to show because by the definition of the metric \\(d\\) and the projection \\(\pi\\) we can conclude
\\[
    d(\pi((x,y)),\pi((x', y'))) = \|y-y'\| < \varepsilon.
\\]
<div style="text-align: right"> // </div>
</details>


As illustrated in the visuals from the previous example, it was useful to consider a "ball" of all points within some distance \\(\delta\\) of our central point \\((x,y)\\).
Given a metric space \\((X, d)\\), we define the ***open ball*** \\(B^d_{\delta}(x)\\) of radius \\(r\\) centered at \\(x\\) for some \\(x \in X\\) to be the set
\\[
    B^d_{\delta}(x) := \\{x' \in X : d(x, x') < \delta\\}.
\\]

/\*TODO: show visuals of open ball for \\(d\_2\\), then \\(d\\), then \\(d\_1\\). Perhaps include commentary too\*/

Recall by definition, for a function \\(f: X \to Y\\) between two metric spaces \\((X, d\_X)\\) and \\((Y, d\_Y)\\) to be continuous, for every \\(x \in X\\) and \\(\varepsilon > 0\\), we need to find some \\(\delta > 0\\) such that \\(d\_X(x, x') < \delta\\) guarantees \\(d_Y(f(x), f(x')) < \varepsilon\\). In other words, we need to find some \\(\delta > 0\\) such that \\(x' \in B^{d_X}\_\delta(x)\\) guarantees \\(f(x') \in B^{d_Y}_{\varepsilon}(f(x))\\).

/\*picture of the above\*/

Therefore, an equivalent formulation of the definition of continuity is that for every \\(x \in X\\) and \\(\varepsilon > 0\\), we need to find \\(\delta > 0\\) so that \\(B^{d_Y}\_{\delta}(x) \subset f^{-1}(B^{d\_Y}\_{\varepsilon}(f(x)))\\), which we record below.

**Proposition.** A function \\(f: X \to Y\\) between two metric spaces \\((X, d\_X)\\) and \\((Y, d\_Y)\\) is continuous if and only if for every \\(x \in X\\) and \\(\varepsilon > 0\\), there exists \\(\delta > 0\\) so that \\(B^{d_X}\_{\delta}(x) \subset f^{-1}(B^{d\_Y}\_{\varepsilon}(f(x)))\\).

To practice this formulation of continuity, we prove the above projection is also continuous with respect to the taxicab metric.

**Exercise.** Prove the projection \\(\pi: \mathbb{R}^2 \to \mathbb{R}\\) defined by \\(\pi(x, y) = x\\) is contininuous if \\(\mathbb{R}^2\\) is given the taxicab metric \\(d\_1\\).

<details markdown="1">
<summary><i>Solution.</i></summary>
 Given a point \\((x,y) \in \mathbb{R}^2\\) and \\(\varepsilon > 0\\), we need to show there exists a \\(\delta > 0\\) such that \\(B^{d_1}\_{\delta}((x,y)) \subset \pi^{-1}(B^{d}\_{\varepsilon}(\pi(x, y)))\\). By unraveling the definition of \\(\pi\\) and \\(B^{d}\_{\varepsilon}\\), we can rewrite the set
\\[
    \pi^{-1}(B^{d}\_{\varepsilon}(\pi(x, y)))
    = \\{(x',y') \in \mathbb{R}^2 : |y - y'| < \varepsilon\\},
\\]
which we can visualize as follows. 

/\*TODO: visual of preimage.\*/

This visual suggests \\(B^{d_1}\_{\varepsilon}((x,y)) \subset \pi^{-1}(B^{d}\_{\varepsilon}(\pi(x, y)))\\). Indeed, note
\\[
\begin{align}
    B^{d_1}\_{\varepsilon}((x,y))
    &= \\{(x',y') : |x' - x| + |y - y'| < \varepsilon\\}\\\\\
    &\subset \\{(x',y') \in \mathbb{R}^2 : |y - y'| < \varepsilon\\}
    = \pi^{-1}(B^{d}\_{\varepsilon}(\pi(x, y))).
\end{align}
\\]
<div style="text-align: right"> // </div>
</details>

We have seen that \\(\pi: \mathbb{R}^2 \to \mathbb{R}\\) is continuous both with respect to the Euclidean metric \\(d\_2\\) and with respect to the taxicab metric \\(d\_1\\), which raises the following interesting question.

**Puzzle.** Is it possible to find a map \\(f: \mathbb{R}^2 \to \mathbb{R}\\) that is continuous with respect to the Euclidean metric \\(d\_2\\), but not the taxicab metric \\(d\_1\\)? What about continuous with respect to \\(d\_1\\) but not \\(d\_2\\)?

<!-- todo: possibly give formal arguments for ball inclusions? (hidden?) -->

<details markdown="1">
<summary><i>Solution.</i></summary>

If such a map \\(f: \mathbb{R}^2 \to \mathbb{R}\\) existed, then there would need to be some point \\(p \in \mathbb{R}^2\\) and \\(\varepsilon > 0\\) such that there is some \\(\delta\_2\\) satisfying \\(B_{\delta\_2}^{d\_2}(p) \subset f^{-1}(B^{d}\_{\varepsilon}(f(p)))\\) and yet there is no \\(\delta\_1 > 0\\) so that \\(B_{\delta\_1}^{d\_1}(p) \subset f^{-1}(B^{d}\_{\varepsilon}(f(p)))\\). However, we can observe visually that we have the inclusion
\\(
    B_{\delta\_2}^{d\_1}(p) \subset B_{\delta\_2}^{d\_2}(p):
\\)

/\*illustration of this inclusion\*/

Therefore, the choice of \\(\delta\_1 = \delta\_2\\) gives
\\[
    B_{\delta\_2}^{d\_1}(p) \subset B_{\delta\_2}^{d\_2}(p) \subset f^{-1}(B^{d}\_{\varepsilon}(f(p))).
\\]
and so this situation is impossible. In other words, if \\(f: \mathbb{R}^2 \to \mathbb{R}\\) is continuous with respect to \\(d\_2\\) it is also continuous with respect to \\(d\_1\\).

Now we address the converse question. Suppose \\(f: \mathbb{R}^2 \to \mathbb{R}\\) is continuous with respect to \\(d\_2\\). Note it is *not* true that 
\\(B_{\delta}^{d\_1}(p) \subset B_{\delta}^{d\_2}(p)\\), but it is true that
\\(B\_{\delta/\sqrt{2}}^{d\_1}(p) \subset B_{\delta}^{d\_2}(p)\\), which is good enough to make the same argument. 

/\*illustration of ball inclusion\*/

Indeed, \\(f: \mathbb{R}^2 \to \mathbb{R}\\) is continuous with respect to \\(d\_2\\), then for any \\(p \in \mathbb{R}^2\\) and \\(\varepsilon > 0\\), there exists some \\(\delta\\) such that \\(B_{\delta}^{d\_2}(p) \subset f^{-1}(B^{d}\_{\varepsilon}(f(p)))\\). But then for the choice of \\(\delta/\sqrt{2}\\) we also have
\\[
    B\_{\delta/\sqrt{2}}^{d\_1}(p) \subset B_{\delta}^{d\_2}(p) \subset f^{-1}(B^{d}\_{\varepsilon}(f(p))).
\\]
Therefore, \\(f\\) is also continuous with respect to \\(d\_1\\). Thus it is not possible to find any such \\(f \colon \mathbb{R}^2 \to \mathbb{R}\\) in either case.
<div style="text-align: right"> // </div>
</details>

The key to the above solution to the first part of the above puzzle is in observing that the the taxicab ball \\(B^{d\_1}\_{r}(p)\\) fits inside the Euclidean open ball \\(B^{d\_2}\_{r}(p)\\):
\\[
    B\_{r}^{d\_1}(p) \subset B\_{r}^{d\_2}(p):
\\]
/\*picture\*/

For the second part of the puzzle, the key is in observing that given the taxicab ball \\(B^{d\_1}\_{r}(p)\\), the Euclidean ball of smaller radius \\(r/\sqrt{2}\\) fits inside the taxicab ball:
\\[
    B\_{r/\sqrt{2}}^{d\_1}(p) \subset B_{r}^{d\_2}(p)
\\]
/\*picture\*/

<!-- TODO: perhaps change below notation to \delta and \eps in whatever way they are applied later -->
This argument will work so long as we have the following condition.
If two metrics \\(d\\\) and \\(d'\\) on a metric space \\(X\\) have the property that given an open ball \\(B^{d'}\_\{r'\}(p)\\), we can find a smaller open ball \\(B^{d}\_{r}(p) \subset B^{d'}\_\{r'\}(p)\\) and for each open ball \\(B^{d}\_{s}(p)\\), we can find a smaller open ball \\(B^{d'}\_{s'}(p) \subset B^{d}\_\{s\}(p)\\), then we say \\(d\_1\\) and \\(d\_2\\) are ***topologically equivalent***. Then, by the same ideas as above, topologically equivalent metrics will induce exactly the same continuous maps.

**Proposition.** If \\(d\\) and \\(d'\\) are topologically equivalent metrics on \\(X\\), they induce the same continuous maps.

<details markdown="1">
<summary><i>Proof.</i></summary>

We could verify this by argument as above, but instead observe the identity map \\(\operatorname{Id}: (X, d) \to (X, d')\\) will be continuous. Indeed, note for any \\(x \in X\\) and ball \\(B^{d'}\_{\varepsilon}(x)\\), we can find a smaller ball so that
\\[
    B^{d}\_{\delta}(x) \subset B^{d'}\_{\varepsilon}(x).
\\]
But because \\(\operatorname{Id}^{-1}(B^{d'}\_{\varepsilon}(\operatorname{Id}(x))) = B^{d'}\_{\varepsilon}(x)\\), this is precisely the open ball formulation of continuity of \\(\operatorname{Id}\\). Therefore, because the composition of continuous function is continuous, we find:
\\[
\begin{align}
    f: (X, d') \to Y \text{ continuous } &\implies f \circ \operatorname{Id}: (X, d) \to Y \text{ continuous},\\\\\
    f: Y \to (X, d) \text{ continuous } &\implies \operatorname{Id} \circ f: (X, d') \to Y \text{ continuous}.
\end{align}
\\]
By reversing the roles of \\(d\\) and \\(d'\\) and applying the same reasoning, \\(\operatorname{Id}: (X, d') \to (X, d)\\) will be continuous and therefore
\\[
\begin{align}
    f: (X, d) \to Y \text{ continuous } &\implies f \circ \operatorname{Id}: (X, d') \to Y \text{ continuous},\\\\\
    f: Y \to (X, d') \text{ continuous } &\implies \operatorname{Id} \circ f: (X, d) \to Y \text{ continuous}.
\end{align}
\\]
In other words, \\((X, d)\\) and \\((X, d')\\) have exactly the same continuous maps.
<div style="text-align: right"> \(\square\) </div>
</details>

**Exercise.** Prove topological equivalence is an equivalence relation.

<details markdown="1">
<summary><i>Solution.</i></summary>
First observe that \\((X, d)\\) is topologically equivalent to itself because \\(B^{d}\_{\varepsilon}(x) \subset B^{d}\_{\varepsilon}(x)\\). Next, note if \\((X, d)\\) is topologically equivalent to \\((X, d')\\), then \\((X, d')\\) is topologically equivalent to \\((X, d)\\) by the symmetry in the definition. Finally, suppose \\((X, d)\\) is topologically equivalent to \\((X, d')\\), which in turn is topologically equivalent to \\((X, d'')\\). Then by applying the definitions of topological equivalence, there exists smaller balls \\(B^{d'}\_{\varepsilon'}(x) \subset B^{d''}\_{\varepsilon''}(x)\\) and \\(B^{d}\_{\varepsilon}(x) \subset B^{d'}\_{\varepsilon'}(x)\\), which implies we can find a ball 
\\[B^{d}\_{\varepsilon}(x) \subset B^{d''}\_{\varepsilon''}(x).\\]
Repeating this argument in reverse will give for any ball \\(B^{d}\_{\delta}(x) > 0\\) a smaller ball
\\[
    B^{d''}\_{\delta''}(x) \subset B^{d}\_{\delta}(x).
\\]
Thus \\((X, d)\\) is topologically equivalent to \\((X, d'')\\).
</details>

## Open sets

As a first step to understanding topological equivalence, consider a set \\(X\\) with two topologically equivalent metrics \\(d\\) and \\(d'\\). Then if we know the metric \\(d\\), what can we say about the metric \\(d'\\)? That is, how does this relationship constrain the two metrics?

To begin, take a point \\(x \in X\\) and an open ball \\(B^{d'}\_{\varepsilon}(x)\\); then, while \\(B^{d'}\_{\varepsilon}(x)\\) is not necessarily a ball with respect to the metric \\(d\\), the equivalence of metrics promises a small ball \\(\delta > 0\\) so that \\(B^{d}\_{\delta}(x) \subset B^{d'}\_{\varepsilon}(x)\\). In fact, we can say something similar for any point \\(y \in B^{d'}\_{\varepsilon}(x)\\). Indeed, first choose some small \\(\widetilde{\varepsilon} > 0\\) so that \\(B^{d'}\_{\widetilde{\varepsilon}}(y) \subset B^{d'}\_{\varepsilon}(x)\\). For example, we could choose \\(\widetilde{\varepsilon} = \varepsilon - d(x,y)\\), which is positive by \\(d(x,y) < \varepsilon\\), and we can verify that for any \\(z \in B^{d'}\_{\widetilde{\varepsilon}}(y)\\) we have 
\\[
    d(x,z) \leq d(y,z) + d(x,y) < \widetilde{\varepsilon} + d(x,y) = \varepsilon - d(x,y) + d(x,y) = \varepsilon,
\\]
which implies \\(B^{d'}\_{\widetilde{\varepsilon}}(y) \subset B^{d'}\_{\varepsilon}(x)\\). Therefore by the equivalence of metrics again, there exists some \\(\widetilde{\delta} > 0\\) so that 
\\[
    B^{d}\_{\widetilde{\delta}}(y) \subset B^{d'}\_{\widetilde{\varepsilon}}(y) \subset B^{d'}\_{\varepsilon}(x).
\\]
That is, while \\(B^{d'}\_{\varepsilon}(x)\\) is not necessarily a ball with respect to \\(d\\), it has an interesting property: for any point \\(y \in B^{d'}\_{\varepsilon}(x)\\), we can find a small ball \\(B^{d}\_{\widetilde{\delta}}(y)\\) with respect to \\(d\\) so that \\(B^{d}\_{\widetilde{\delta}}(y) \subset B^{d'}\_{\varepsilon}(x)\\). This is a constraint on what open balls with respect to the metric \\(d'\\) can look like imposed by the metric \\(d\\). This contraint on \\(B^{d'}\_{\varepsilon}(x)\\) is that it is "open" with respect to the metric \\(d\\).

Given a metric space \\((X, d)\\), a subset \\(U \subset X\\) is called ***open*** if for every point \\(y \in U\\), there exists a small ball \\(B^{d}\_{\varepsilon}(y)\\) so that \\(B^{d}\_{\varepsilon}(y) \subset U\\).

In reflecting on the above argument that \\(B^{d'}\_{\varepsilon}(x)\\) must be open with respect \\(d\\), note the only property we used about \\(B^{d'}\_{\varepsilon}(x)\\) is that given \\(y \in B^{d'}\_{\varepsilon}(x)\\), we could find a small ball \\(B^{d'}\_{\widetilde{\varepsilon}}(y) \subset B^{d'}\_{\varepsilon}(x)\\). But this is exactly the definition of open with respect to the \\(d'\\) metric! That is, by the exact same argument, we could have argued that any \\(U\\) that is open with respect to \\(d'\\) is also open with respect to \\(d\\), which we formalize below.

**Proposition.** If \\(d\\) and \\(d'\\) are topologically equivalent metrics on \\(X\\), then \\(d\\) and \\(d'\\) produce the same open sets.

*Proof.* First suppose \\(U \subset X\\) is open with respect to \\(d'\\), so by the definition of open, there is a ball \\(B^{d'}\_{\varepsilon}(x) \subset U\\). Next, by the definition of topological equivalence, there is a ball \\(B^{d}\_{\delta}(x) \subset B^{d'}\_{\varepsilon}(x)\\). But putting this together impies
\\[
    B^{d}\_{\delta}(x) \subset B^{d'}\_{\varepsilon}(x) \subset U
\\]
and therefore \\(U\\) is also open with respect to \\(d\\). By repeating this argument with \\(d\\) and \\(d'\\) swapped, we conclude any \\(V \subset X\\) that is open with respect to \\(d\\) is also open with respect to \\(d'\\).
<div style="text-align: right"> \(\square\) </div>

We have found one contraint topological equivalence puts on the metrics. In fact, this constraint exactly classifies topological equivalence because the converse is also true, which we prove below.

**Proposition.** If \\(d\\) and \\(d'\\) have the same open sets, then \\(d\\) and \\(d'\\) are topologically equivalent.

*Proof.* Take any point \\(x \in X\\) and open ball \\(B^{d'}\_{\varepsilon}(x)\\). Then because \\(B^{d'}\_{\varepsilon}(x)\\) is open with respect to \\(d'\\), our assumption promises it is open with respect to \\(d\\) and therefore we can find a small ball \\(B^{d}\_{\delta}(x) \subset B^{d'}\_{\varepsilon}(x)\\). Repeating this argument with \\(d\\) and \\(d'\\) flipped gives the definition of topological equivalence.
<div style="text-align: right"> \(\square\) </div>

Combining the above two results gives the following important alternate characterization of topological equivalence.

**Theorem.** \\(d\\) and \\(d'\\) are topologically equivalent if and only if they have the exact same open sets.

## Continuity using open sets

Our original motivation for topological equivalence was to identify metrics that induce the same continuous maps. Next, we found the open set data is enough to determine topological equivalence. Therefore, we should expect that this open set data should encode continuity. Indeed, taking the open ball characterization of continuity and considering arbitrary open sets, we arrive at the following characterization of continuity.

**Proposition.** A map \\(f: X \to Y\\) between metric spaces is continuous if and only if \\(f^{-1}(U) \subset X\\) is open for every open \\(U \subset Y\\).
<!-- in video, just do quick visual motivating proof first and perhaps skip the formal proof -->

*Proof.* First suppose \\(f: X \to Y\\) is continuous. Then take some open \\(U \subset Y\\) and consider a point \\(x \in f^{-1}(U)\\), which is equivalent to \\(f(x) \in U\\). By \\(U\\) open, there exists some small open ball \\(B\_{\varepsilon}(f(x)) \subset U\\), and by \\(f\\) continuous, there exists some small open ball 
\\[
    B\_{\delta}(x) \subset f^{-1}(B_{\varepsilon}(f(x))) \subset f^{-1}(U).
\\]
Therefore, \\(U\\) is open in \\(X\\). Conversely, suppose \\(f^{-1}(U)\\) is open for every open \\(U \subset Y\\). For any \\(x \in X\\), consider some small open ball \\(B\_{\varepsilon}(f(x)) \subset Y\\). Then the assumption implies \\(f^{-1}(B\_{\varepsilon}(f(x)))\\) is open, so there exists some small ball \\(B\_{\delta}(x) \subset f^{-1}(B\_{\varepsilon}(f(x)))\\), which implies \\(f: X \to Y\\) is continuous.

## Topological spaces

Recall we determined two metrics \\(d\\) and \\(d'\\) over a space \\(X\\) will yield exactly the same continuous functions \\(X \to Y\\) and \\(Y \to X\\) if they are topologically equivalent. From our subsequent investigations, we found the collection of open sets encode this notion of topological equivalence; furthermore, the collection of open sets is the only necessary data to determine if a function is continuous between two metric spaces. Given a metric space \\(X\\), the collection of all open sets
\\[
    \mathcal{T} = \\{U \subset X : U \text{ is open}\\}
\\]
is called the ***topology*** of \\(X\\). Note \\(\mathcal{T}\\) is a subset of the power set \\(\mathcal{P}(X)\\) of \\(X\\). Finally, note the collection of open sets satisfy the following important properties.

<!-- in video, prove these one by one and then state this proposition... -->

**Proposition.** Let \\((X, d)\\) be a metric space. Then:
1. The union of open sets of \\(X\\) is an open set.
2. The finite intersection of open sets of \\(X\\) is open.
3. The empty set \\(\varnothing\\) and the entire set \\(X\\) are both open.

*Proof.*
1. Take any collection \\(\\{U_{\alpha}\\}\_{\alpha \in \mathcal{A}}\\) of open sets and consider the union \\(\bigcup\_{\alpha \in \mathcal{A}} U_{\alpha}\\). Then any point \\(x \in \bigcup\_{\alpha \in \mathcal{A}} U\_{\alpha}\\) is by definition an element \\(x \in U\_{\alpha}\\) for some particular \\(\alpha \in \mathcal{A}\\). But then by \\(U\_{\alpha}\\) open, there is some open ball
\\[
    B\_{\varepsilon}(x) \subset U\_{\alpha} \subset \bigcup\_{\alpha \in \mathcal{A}} U\_{\alpha}.
\\]
Therefore \\(\bigcup\_{\alpha \in \mathcal{A}} U_{\alpha}\\) is open.
2. Take any finite collection \\(U\_1, \cdots, U\_n\\) of open sets and consider the intersection \\(\bigcap\_{k=1}^n U\_k\\). Then any point \\(x \in \bigcap\_{k=1}^n U\_k\\) is an element \\(x \in U\_k\\) for each \\(k = 1, 2, \cdots, n\\). Therefore, because each \\(U\_k\\) is open, there is an \\(\varepsilon\_k > 0\\) such that \\(B\_{\varepsilon\_k}(x) \subset U\_k\\) for each \\(k = 1, 2, \cdots, n\\). But then these values \\(\varepsilon\_1, \varepsilon\_2, \cdots, \varepsilon\_n\\) must have some minimum \\(\varepsilon\_k\\) for some particular \\(k\\), which implies \\(B\_{\varepsilon\_k}(x) \subset U\_1, \cdots, U\_n\\) and therefore \\(B\_{\varepsilon\_k}(x) \subset \bigcap\_{k=1}^n U\_k\\). Thus \\(\bigcap\_{k=1}^n U\_k\\) is open.
3. Take any \\(x \in X\\) and note \\(B\_{\varepsilon}(x) \subset X\\) for any choice of \\(\varepsilon\\), so \\(X\\) is open. To show \\(\varnothing\\) is open, we must check every element of \\(\varnothing\\) satisfies the open ball condition. However, because \\(\varnothing\\) has no elements, this is true by default (i.e. this is "vacuously" true).

Again, the only necessary data to determine if a function is continuous between two metric spaces is the collection of open sets in each space; that is, the topology. A "topological space" generalizes metric spaces by only giving a set a topology and nothing else, which is sufficient to define continuity (in fact, we will see later that a topology is in some sense the *minimal* possible data we can give to define continuity).
<!-- removing extraneous information is useful and clarifying... -->

A ***topological space*** is a set \\(X\\) together with a collection \\(\mathcal{T} \subset \mathcal{P}(X)\\) (called the ***topology***) of subsets of \\(X\\) (called the ***open sets***) that satisfy
1. Given any collection \\(\\{U_{\alpha}\\}\_{\alpha \in A} \subset \mathcal{T}\\) of open sets, their union is open: \\(\bigcup_{\alpha \in A} U_{\alpha} \in \mathcal{T}\\).
2. Given a finite collection \\(U_1, \cdots, U_n\\) of open sets, their intersection is open: \\(\bigcap\_{i = 1}^n U\_{i} \in \mathcal{T}\\).
3. The open set is open and the entire space is open: \\(\varnothing, X \in \mathcal{T}\\).

<!-- check history below -->
The definition of a topological space evolved over time with mathematicians eventually agreeing on the above formulation. In truth, the open sets in a metric space have additional structure that is not reflected in the three properties above and the original definition of a "topological space" by Hausdorff in 1914 required some of this extra structure. However, mathematicians found useful spaces that did not fit into this original definition and so removed this extra structure and landed on the above definition, which is the most general definition.

**Example.** Any metric space \\((X, d)\\) is also a topological space by considering the set \\(X\\) together with its topology \\(\mathcal{T}\\) of opens sets induced by the metric. This is called the ***metric topology***.

<!-- below in some order: -->

<div style="text-align: right"> // </div>

Another topology is given by defining *all* sets to be open.

**Example.** Consider any set \\(X\\) with the topology \\(\mathcal{P}(X)\\) given by the power set of \\(X\\), which is called the ***discrete topology***. Then:
1. If all sets are open, then any union \\(\bigcup_{\alpha \in A} U_{\alpha}\\) of open sets will still be open.
2. Similarly, any finite intersection \\(\bigcap\_{i = 1}^n U\_{i}\\) will be open because all sets are open.
3. The empty set \\(varnothing\\) and the full set \\(X\\) will be open as they are elements of the power set.

<div style="text-align: right"> // </div>

**Exercise.** Given any set \\(X\\), find a metric on \\(X\\) so that the metric topology is the discrete topology.

<details markdown="1">
<summary><i>Solution.</i></summary>
Note that, in particular, every individual point \\(\\{x\\} \subset X\\) is an open set. Therefore, we need to find a metric \\(d\\) so that for small enough \\(\varepsilon > 0\\) we have \\(B^{d}\_{\varepsilon}(x) \subset \\{x\\}\\). That is, for every \\(x\\), we require there to be some distance \\(\varepsilon > 0\\) so that no points are with distance \\(\varepsilon\\) from \\(x\\). One way of accomplishing this is with the ***discrete metric***
\\[
    d(x,y) =
    \begin{cases}
        0 & \text{if } x = y,\\\\\
        1 & \text{otherwise}.
    \end{cases}
\\]
We verify that with this metric every arbitrary \\(U \subset X\\) is open. Indeed, take some point \\(x \in U\\) and observe that because the only point within distance \\(1/2\\) from \\(x\\) is the point \\(x\\) itself we have
\\[
    B^{d}\_{1/2}(x) = \\{x\\} \subset U.
\\]
<div style="text-align: right"> // </div>
</details>

However, a topology is more general than a metric: not every topology is the metric topology of some metric.

**Example.** Given any set \\(X\\), the ***trivial topology*** is defines *only* \\(\varnothing\\) and \\(X\\) to be open. That is, we take the topology \\(\mathcal{T} = \\{\varnothing, X\\}\\). Notice:
1. Any union using only the sets \\(\\{\varnothing, X\\}\\) will be either \\(\varnothing\\) or \\(X\\).
2. Any intersection using only the sets \\(\\{\varnothing, X\\}\\) will be either \\(\varnothing\\) or \\(X\\).
3. The empty set \\(\varnothing\\) and the full set \\(X\\) are open by.

<div style="text-align: right"> // </div>

**Exercise.** Prove the trivial topology of a set \\(X\\) (containing at least 2 elements) is not the metric topology of any metric.

<details markdown="1">
<summary><i>Solution</i>.</summary>
Suppose for contradiction the trivial topology is the metric topology of some metric \\(d\\). Then consider two distinct elements \\(x, y \in X\\), which implies \\(d(x,y) > 0\\) by the definition of a metric. Therefore,
\\[
    y \notin B^{d}\_{d(x,y)/2}(x).
\\]
However, because open balls are open sets in a metric space, we have found the open set \\(B^{d}\_{d(x,y)/2}(x)\\) contains \\(x\\), but does not contain \\(y\\). Therefore we have found an open set that it is neither \\(\varnothing\\) nor \\(X\\), a contradiction.

<div style="text-align: right"> // </div>
</details>

**Exercise.** The set with two elements \\(X = \\{0, 1\\}\\) with topology \\(\mathcal{T} = \\{\varnothing, \\{1\\}, \\{0,1\\}\\}\\) is called ***Sierpiński space***. Verify this is a topology.

<details markdown="1">
<summary><i>Solution.</i></summary>
1. Any union consisting of only the sets \\(\\{\varnothing, \\{1\\}, \\{0,1\\}\\}\\) will again be one of these three sets.
2. Any intersection consisting of only the sets \\(\\{\varnothing, \\{1\\}, \\{0,1\\}\\}\\) will again be one of these three sets.
3. The emptyset \\(\varnothing\\) and the full space \\(X = \\{0,1\\}\\) are open by definition.
<div style="text-align: right"> // </div>
</details>

## On the definition of topological space

In this section, I remark on why the definition of a topological space is natural and important to study.
First, recall the definition of topology required open sets to satisfy three properties:
1. the union of open sets is open,
2. the finite intersection of open sets is open, and
3. the empty set and the full space are open.

These are natural properties to require as the collection of open sets in any metric space satisfy these three properties. However, these properties are in fact essential for the definition of continuity in a topological space to be a meaningful definition of continuity for metric spaces. To see this, first observe the following:

**Exercise.** If \\(f \colon X \to Y\\) is a map between sets and \\(\\{U_{\alpha}\\}_{\alpha \in A} \subset Y\\) is a collection of sets in Y, then:
1. \\(f^{-1}(\bigcup_{\alpha \in A} U_{\alpha}) = \bigcup_{\alpha \in A}f^{-1}(U_{\alpha})\\),
2. \\(f^{-1}(\bigcap_{\alpha \in A} U_{\alpha}) = \bigcap_{\alpha \in A}f^{-1}(U_{\alpha})\\), and
3. \\(f^{-1}(Y) = X\\) and \\(f^{-1}(\varnothing) = \varnothing\\).

/\*TODO: solution.\*/

Considering the above results, suppose \\(X\\) is a topological space, \\(Y\\) is any metric space, and \\(f: X \to Y\\) is any continuous function. Then, because \\(\varnothing\\) and \\(Y\\) are open in \\(Y\\), the definition of continuity forces \\(X = f^{-1}(Y)\\) and \\(\varnothing = f^{-1}(\varnothing)\\) to be open in \\(X\\). It is for this reason we define the empty set and the full space to be open; if they were not open, this would be an obstruction to there existing *any* continuous function \\(f: X \to Y\\) to a metric space \\(Y\\). Similarly, because open sets are closed under unions and finite intersections in metric spaces, points by points (1) and (2) above, we should require these same conditions in our definition of a topological space; otherwise, this would be an obstruction to defining continuous functions into metric spaces.
<!-- 
in this second case, there still could be continuous functions, but this would make them hard to define...
also, note historically, topology was originally defined with more conditions on the open sets, but over time this was found to be the most general definition that still has enough structure.
-->

Next, I follow up with the claim that, in some sense, a topology is the minimal necessary information to determine if a function is continuous. This is not true for metric spaces: we saw the Euclidean metric on \\(\mathbb{R}^2\\) and the taxicab metric on \\(\mathbb{R}^2\\) will result in exactly the same functions \\(f: X \to \mathbb{R}^2\\) and \\(g: \mathbb{R}^2 \to X\\) being continuous. However, knowledge of all continuous maps out of a topological space uniquely determines the topology by the following exercise.

**Puzzle.** Is it possible to give a set \\(X\\) two different topologies that induce the same continuous functions?

<details markdown="1">
<summary><i>Solution.</i></summary>
Because the notion of topology was motivated by topological equivalence, which in turn was motivated by requiring the same behavior of continuous functions, we should expect distinct topologies induce distinct behavior of continuous functions. To prove this, we prove we can reconstruct the topology from the knowledge of all continuous functions. To determine if some \\(U \subset X\\) is open, consider the set \\(\\{0,1\\}\\) with the Sierpiński topology \\(\mathcal{T} = \\{\varnothing, \\{1\\}, \\{0,1\\}\\}\\) together with the function
\\[
    f\_{U} =
    \begin{cases}
        0 &\text{if } x \notin U,\\\\\
        1 &\text{if } x \in U.
    \end{cases}
\\]
Then if \\(f\_{U}\\) is continuous, then \\(U = f\_{U}^{-1}(1)\\) is open because \\(\\{1\\}\\) is open. On the other hand, if \\(f\_U\\) is not continuous, this must be because one of the sets
\\[
    f^{-1}(\varnothing) = \varnothing, \quad f^{-1}(1) = U, \quad f^{-1}(\\{1,2\\}) = X
\\]
has failed to be open. Because \\(\varnothing\\) and \\(X\\) must be open, we conclude \\(U\\) is not open. Therefore, we are able to determine the topology of \\(X\\) from these continuous functions.
<div style="text-align: right"> // </div>
</details>

/\*TODO: little conclusion on applications of topology... function spaces, manifolds, \*/