---
layout: page
title: Arzela-Ascoli
---

## Arzelà-Ascol Theorem

/\*background todo:
* compact metric spaces are separable
* compact metric spaces are complete
* uniformly cauchy sequences over complete metric spaces converge uniformly
* continuous functions converging uniformly converges to a continuous function  
\*/

/\*can also consider codomain \\(\mathbb{C}\\)\ without any change*/

/\*motivation... give counterexamples for \\([0,1] \to \mathbb{R}\\) to motivate why we consider pointwise bounded and uniform equicontinuity\*/

/\*todo... upgrade this result to compact Hausdorff spaces as in Folland\*/

**Def.** Given a metric space \\(X\\), a collection of continuous of functions \\(\mathcal{F} \subset C(X)\\) is said to be *pointwise bounded* if for each \\(x \in X\\), the subset \\(\\{f(x): f \in \mathcal{F}\\}\\) is bounded in \\(\mathbb{R}\\). 

<!-- **Def.** Given a metric space \\(X\\), a collection of continuous of functions \\(\mathcal{F} \subset C(X)\\) is said to be *uniformly equicontinuous* if for all \\(\varepsilon > 0\\), there exists some \\(\delta > 0\\) so that \\(d(x,y) < \delta\\) ensures the same bound \\(\|f(x)-f(y)\| < \varepsilon\\) for *every* \\(f \in \mathcal{F}\\).

/\*say that we can weaken assumption to equicontinuous for compact sets\*/ -->

**Def.** Given a metric space \\(X\\), a collection of continuous of functions \\(\mathcal{F} \subset C(X)\\) is said to be *equicontinuous* if for all \\(x \in X\\) and \\(\varepsilon > 0\\), there exists some \\(\delta > 0\\) so that \\(d(x,y) < \delta\\) ensures the same bound \\(\|f(x)-f(y)\| < \varepsilon\\) for *every* \\(f \in \mathcal{F}\\).

<!-- **Lemma.** If \\(X\\) is a compact metric space and \\(\mathcal{F} \subset C(X)\\) is an equicontinuous family of functions, then \\(\mathcal{F}\\) is uniformly equicontinuous.

*Proof.* /\*TODO\*/ -->

**Theorem.** Consider a compact metric space \\(X\\) and an equicontinuous and pointwise bounded family \\(\mathcal{F} \subset C(X)\\). Then there exists a sequence \\(\\{f\_k\\} \subset \mathcal{F}\\) that converges uniformly \\(f\_k \to f \in C(X)\\).

*Proof.* By \\(X\\) a compact metric space, it is separable, so take a countabale dense subset \\(\{x\_i\} \subset X.\\) We will construct a subsequence that converges on every \\(x\_i\\) by the following "diagonalization argument". Indeed, by pointwise boundedness, we find \\(\\{f(x\_1): f \in \mathcal{F}\\}\\) is bounded, so there exists a subsequence \\(\\{f\_{n\_1}\\} \subset \mathcal{F}\\) such that \\(f\_{n\_1}(x\_1)\\) converges. Next, observe \\(\\{f\_{n\_1}(x\_2)\\}\\) is also bounded by pointwise boundedness and so there exists a subsequence  \\(\\{f\_{n\_2}\\} \subset \\{f\_{n\_1}\\}\\) such that \\(f\_{n\_2}(x\_2)\\) converges (note that \\(f\_{n\_2}(x\_1) \subset f\_{n\_1}(x\_1)\\) still converges). Continuing in this way we can construct sequences \\(f\_{n\_1} \supset f\_{n\_2} \supset f\_{n\_3} \supset \cdots\\) such that \\(f\_{n\_m}(x\_i)\\) converges for all \\(i \leq m\\). In order to construct a single sequence that converges on *all* \\(x\_k\\), we define the sequence \\(f\_{k}\\) so that \\(f\_k\\) is the \\(k\\)th term in the \\(k\\)th sequence \\(f\_{n\_k}\\). That is, when the terms in the sequences \\(f\_{n\_m}\\) are arranged into a grid as picture below /\*todo\*/, the sequence \\(f\_{k}\\) is the "diagonal" of this grid. Importantly, \\(f\_k\\) has the property that \\(f\_k(x\_i)\\) converges for every \\(x\_i\\) /\*todo or leave as exrecise\*/. 

Now we use equicontinuity to verify this sequence \\(f\_k\\) converges uniformly on \\(X\\). Recall that because \\(X\\) is a compact metric space, it is complete /\*todo\*/. Thus to verify \\(f\_k\\) converges uniformly, it suffices to show \\(f\_k\\) is uniformly Cauchy. Indeed, fix \\(\varepsilon > 0\\) and apply equicontinuity to each \\(x\_i\\) to obtain \\(\delta\_i\\) so that \\(d(x\_i, y) < \delta\_i\\) promises \\(\|f(x\_i) - f(y)\| < \varepsilon/3\\) for all \\(f \in \mathcal{F} \supset \\{f\_k\\}\\). By the compactness of \\(X\\), there is some \\(K > 0\\) such that the finite collection of balls \\(\\{B\_{\delta\_i}(x\_i): i \leq K\\}\\) cover \\(X\\). Next, because for all \\(i \leq K\\), the sequence \\(f_k(x\_i)\\) converges, it is Cauchy and so there exists \\(N\_i\\) so that \\(n,m > N\_i\\) ensures \\(\|f_n(x\_i) - f\_m(x\_i)\| < \varepsilon/3\\). We can now take \\(N = \max(N\_1, \cdots, N\_k)\\) and consider any \\(n,m > N\\) in order to show \\(f\_k\\) is uniformly Cauchy. Indeed, for any \\(y \in X\\), we know there exists some \\(x\_i\\) with \\(d(y,x\_i) < \delta\_i\\) and therefore
\\[
    \|f\_n(y) - f\_m(y)\|
    \leq \|f\_n(y) - f\_n(x\_i)\|
    + \|f\_n(x\_i) - f\_m(x\_i)\|
    + \|f\_m(x\_i) - f\_m(y)\|
    < \varepsilon/3 + \varepsilon/3 + \varepsilon/3 = \varepsilon
\\]
Thus we have \\(f\_k\\) is uniformly Cauchy and therefore converges uniformly to a continuous function /\*todo\*/.

<div style="text-align: right"> \(\square\) </div>