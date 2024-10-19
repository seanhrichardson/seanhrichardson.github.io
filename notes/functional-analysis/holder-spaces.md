---
layout: page
title: Hölder Spaces
section: Hölder Spaces
---

# Motivation via Arzelà-Ascoli

Suppose we have a sequence of functions \\(u\_n\\) and wish to prove that this sequence converges uniformly (we often encounter this, for example, when solving PDEs). If we are working on a compact subset \\(X \subset \mathbb{R}^n\\), the Arzelà-Ascoli theorem provides a convenient criteria for uniform convergence: pointwise boundedness and equicontinuity. Recall these are defined as follows, letting \\(C(X)\\) denote the space of continuous functions \\(X \to \mathbb{R}\\).

**Def (pointwise boundedness).** A subset \\(\mathcal{F} \subset C(X)\\) is *pointwise bounded* if for all \\(x \in X\\), the set \\(\\{u(x): u \in \mathcal{F}\\} \subset \mathbb{R}\\) is bounded.

**Def (equicontinuity).** A subset \\(\mathcal{F} \subset C(X)\\) is *equicontinuous* if for all \\(x \in X\\) and \\(\varepsilon > 0\\), there exists \\(\delta > 0\\) such that \\(\\|x-y\\| < \delta\\) implies we have the bound \\(\|u(x) - u(y)\| < \varepsilon\\) for all \\(u \in \mathcal{F}\\).

Importantly, given such a \\(x\\) and \\(\varepsilon\\) as above, the same \\(\delta\\) must work for all \\(u \in \mathcal{F}\\). Keep in mind the subset \\(\mathcal{F}\\) above is often simply a sequence \\(u_n\\) of continuous functions. The Arzelà-Ascoli theorem then promises

**Theorem (Arzelà-Ascoli).** If \\(\mathcal{F} \subset C(X)\\) is equicontinuous and pointwise bounded, then there exists a subsequence \\(u_k \subset \mathcal{F}\\) such that \\(u_k \to u \in C(X)\\) uniformly.

Equicontinuity is generally harder than pointwise boundedness to verify when using Arzelà-Ascoli. A convenient sufficient condition for equicontinuity is there exists a fixed \\(C > 0\\) so that
\\[
    \|u(x) - u(y)\| \leq C \\|x-y\\| \tag{1} \label{eq:lipshitz}
\\]
for all \\(u \in \\mathcal{F}\\). This immediately implies equicontinuity because for any \\(\varepsilon > 0\\) we can simply take \\(\\|x-y\\| < \varepsilon/C\\). However, an even weaker sufficient condition which is often easier to check is that for some fixed \\(\alpha \in (0,1]\\) there exists \\(C > 0\\) such that 
\\[
    \|u(x) - u(y)\| \leq C \\|x-y\\|^{\alpha} \tag{2} \label{eq:holder}
\\]
for all \\(u \in \mathcal{F}\\). In this case, we get equicontinuity by taking \\(\\|x-y\\| < (\varepsilon/C)^{1/\alpha}\\) for any given \\(\varepsilon > 0\\). If \\(u\\) satisfies (\ref{eq:lipshitz}), it is called *Lipshitz continuous* and if \\(u\\) satisfies (\ref{eq:holder}), it is called *\\(\alpha\\)-Hölder continuous*. This terminology is due to the following exercise.

**Exercise.** Show that if \\(u: \mathbb{R}^n \to \mathbb{R}\\) satisfies either (1) or (2), it is a continuous function.

Given an \\(\alpha\\)-Hölder continuous function \\(u: X \to \mathbb{R}\\), the minimum constant \\(C\\) is given by the *\\(\alpha\\)-Hölder semi-norm*
\\[
    [u]\_{\alpha} := \sup\_{x \neq y}\frac{|u(x) - u(y)|}{\\|x-y\\|^{\alpha}}.
\\]
This semi-norm is convenient because \\(\\{ [u]\_{\alpha}: u \in \mathcal{F}\\}\\) bounded implies \\(\mathcal{F}\\) is equicontinuous. Additionally, note that if \\(\\{ \\|u\\|_{\sup}: u \in \mathcal{F}\\}\\) is bounded, then \\(\mathcal{F}\\) is pointwise bounded where \\(\\| \cdot \\|\_{\sup}\\) denotes the uniform norm. This motivates defining the *\\(\alpha\\)-Hölder norm*
\\[
    \\|u\\|\_{\alpha} := \\|u\\|\_{\sup} + [u]\_{\alpha}
\\]
because if \\(\\{\\|u\\|\_{\alpha}: u \in \mathcal{F}\\}\\) is bounded, then \\(\mathcal{F}\\) is equicontinuous and pointwise bounded, so Arzelà-Ascoli applies and there exists \\(u\_k \in \mathcal{F}\\) such that \\(u\_k \to u \in C(X)\\) uniformly.

# Hölder spaces

The point is the \\(\alpha\\)-Hölder norm \\(\\|\cdot\\|\_{\alpha}\\) is useful because it allows us to conclude uniform convergence due to Arzelà-Ascoli. We can rephrase this oberservation using the language of functional analysis, which begins by considering the function space of \\(\alpha\\)-Hölder continuous functions.

**Def (Hölder space).** Given a subset \\(\Omega \subset \mathbb{R}^n\\), the *Hölder space* \\(C^{\alpha}(\Omega)\\) for some \\(\alpha \in (0,1]\\) is
\\[
    C^{\alpha}(\Omega) := \\{u \in C(\Omega) : \\|u\\|\_{\alpha} < \infty\\}.
\\]

**Prop.** The *Hölder space* \\(C^{\alpha}(\Omega)\\) is a Banach space

# Compact embedding theorems

/\*recall motivation for Holder spaces... rephrase in terms of compact embeddings\*/

\\(C^{0, \alpha} \to C^0\\)

\\(C^{0, \alpha} \to C^{0, \beta}\\)

\\(C^{k, \alpha} \to C^{k}\\) /\*hopefully using earlier embedding\*/

\\(C^{k, \alpha} \to C^{k, \beta}\\) /\*hopefully using earlier embedding\*/