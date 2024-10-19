---
layout: page
title: C0
---

## Space of continuous functions

/\*motivation: want space of continuous functions and want topology determined by uniform convergence (because of some nice properties of uniform convergence probably?)\*/

**Def. (\\(C^0\(X\)\\)).** /\*TODO\*/

/\*verify norm, etc.\*/

**Theorem.** \\(C^0(X)\\) is complete and hence is a Banach space.

*Proof.* Take a Cauchy sequence \\(f\_n \in C^0(X)\\). We first construct the function this sequence should converge to pointwise, then we verify we indeed have uniform convergence and that this function is continuous. Indeed, note that for each \\(x \in X\\) the sequence \\(f\_n(x) \in \mathbb{R}\\) is Cauchy because \\(\|f\_n(x) - f\_m(x)\| \leq \\|f\_n - f\_m\\|\\), and \\(f\_n\\) is Cauchy. Thus by the completeness of \\(\mathbb{R}\\), we find that for each \\(x \in X\\), the sequence \\(f\_n(x)\\) converges to some \\(f(x) \in \mathbb{R}\\). This defines a natural candidate function \\(f: X \to \mathbb{R}\\) so that \\(f\_n(x) \to f(x)\\) for every point \\(x \in X\\). We now show \\(f\_n \to f\\) with respect to the \\(C^0\\) norm. Indeed, for any \\(\varepsilon > 0\\), use \\(\\{f\_n\\}\\) Cauchy to choose \\(N > 0\\) such that \\(m,n > N\\) ensures \\(\|f\_n - f\_m\| < \varepsilon\\). Because \\(f\_n(x) \to f(x)\\), and this bound holds as \\(n \to \infty\\), we should be able to replace \\(f\_n\\) with \\(f\\) in this bound. Formally, note we have the following uniform bound for all \\(x \in X\\):
\\[
    \|f(x) - f\_m(x)\| = \lim_{n \to \infty}\|f\_n(x) - f\_m(x)\| \leq \lim_{n \to \infty} \\|f\_m - f\_n\\| < \varepsilon.
\\]
Thus \\(f\_n \to f\\) uniformly. It only remains to show \\(f\\) is indeed continuous, which will follow because \\(f\\) is arbitrary and uniformly close to the continuous functions \\(f\_n\\). Indeed, for any \\(x \in X\\) and \\(\varepsilon > 0\\), take some \\(n\\) such that \\(\\|f - f\_n\\| < \varepsilon/3\\). Then by \\(f\_n\\) continuous, take the promised \\(\delta > 0\\) such that \\(d(x,y) < \delta\\) ensures \\(\|f\_n(x) - f\_n(y)\| < \varepsilon/3\\). Then we have
\\[
    \|f(x) - f(y)\| 
    \leq \|f(x) - f\_n(x)\| + \|f\_n(x) - f\_n(y)\| + \|f\_n(y) - f(y)\| 
    < \varepsilon/3 + \varepsilon/3 + \varepsilon/3 
    = \varepsilon.
\\]
<div style="text-align: right"> \(\square\) </div>