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
    \|u(x) - u(y)\| \leq C \\\|x-y\\\| \tag{1} \label{eq:lipshitz}
\\]
for all \\(u \in \\mathcal{F}\\). This immediately implies equicontinuity because for any \\(\varepsilon > 0\\) we can simply take \\(\\|x-y\\| < \varepsilon/C\\). However, an even weaker sufficient condition which is often easier to check is that for some fixed \\(\alpha \in (0,1]\\) there exists \\(C > 0\\) such that 
\\[
    \|u(x) - u(y)\| \leq C \\\|x-y\\\|^{\alpha} \tag{2} \label{eq:holder}
\\]
for all \\(u \in \mathcal{F}\\). In this case, we get equicontinuity by taking \\(\\\|x-y\\\| < (\varepsilon/C)^{1/\alpha}\\) for any given \\(\varepsilon > 0\\). If \\(u\\) satisfies (\ref{eq:lipshitz}), it is called *Lipshitz continuous* and if \\(u\\) satisfies (\ref{eq:holder}), it is called *\\(\alpha\\)-Hölder continuous*. This terminology is due to the following.

**Proposition.** If \\(u: X \to \mathbb{R}\\) satisfies either (1) or (2), it is a continuous function.

*Proof.* Suppose \\(u\\) is \\(\alpha\\)-Hölder continuous with Hölder constant \\(C > 0\\). Then or any \\(\varepsilon > 0\\), taking \\(\\\|x-y\\\| < (\varepsilon/C)^{1/\alpha}\\) guarantees
\\[
    \|u(x)-u(y)\| \leq C\\|x-y\\|^{\alpha} < \varepsilon.
\\]
<div style="text-align: right">\(\square\)</div>

Given an \\(\alpha\\)-Hölder continuous function \\(u: X \to \mathbb{R}\\), the minimum constant \\(C\\) is given by the *\\(\alpha\\)-Hölder semi-norm*
\\[
    [u]\_{\alpha} := \sup\_{x \neq y}\frac{|u(x) - u(y)|}{\\\|x-y\\\|^{\alpha}}.
\\]
This semi-norm is convenient because \\(\\{ [u]\_{\alpha}: u \in \mathcal{F}\\}\\) bounded implies \\(\mathcal{F}\\) is equicontinuous. Additionally, note that if \\(\\{ \\\|u\\\|_{\sup}: u \in \mathcal{F}\\}\\) is bounded, then \\(\mathcal{F}\\) is pointwise bounded where \\(\\\| \cdot \\\|\_{\sup}\\) denotes the uniform norm. This motivates defining the *\\(\alpha\\)-Hölder norm*
\\[
    \\\|u\\\|\_{\alpha} := \\\|u\\\|\_{\sup} + [u]\_{\alpha}
\\]
because if \\(\\{\\\|u\\\|\_{\alpha}: u \in \mathcal{F}\\}\\) is bounded, then \\(\mathcal{F}\\) is equicontinuous and pointwise bounded, so Arzelà-Ascoli applies and there exists \\(u\_k \in \mathcal{F}\\) such that \\(u\_k \to u \in C(X)\\) uniformly.

# Hölder spaces over a compact subset

The point is the \\(\alpha\\)-Hölder norm \\(\\\|\cdot\\\|\_{\alpha}\\) is useful because it allows us to conclude uniform convergence due to Arzelà-Ascoli. We can rephrase this oberservation using the language of functional analysis, which begins by considering the function space of \\(\alpha\\)-Hölder continuous functions.

**Def (Hölder space).** For a compact subset \\(X \subset \mathbb{R}^n\\) and \\(\alpha \in (0,1]\\), the *Hölder space* \\(C^{\alpha}(X)\\) is
\\[
    C^{\alpha}(X) := \\{u \in C(X) : \\\|u\\\|\_{\alpha} < \infty\\}.
\\]

It is over \\(C^{\alpha}(X)\\) that \\([\cdot]\_{\alpha}\\) is a semi-norm and \\(\\\|\cdot\\\|\_{\alpha}\\) is a norm, which we prove below.

**Proposition.** \\([\cdot]\_{\alpha}\\) is a semi-norm over \\(C^{\alpha}(X)\\).

*Proof.* First we check positive homogeneity
\\[
    [cu]\_{\alpha} 
    = \sup\_{x \neq y}\frac{|cu(x) - cu(y)|}{\\\|x-y\\\|^{\alpha}}
    = \|c\|\cdot\sup\_{x \neq y}\frac{|u(x) - u(y)|}{\\\|x-y\\\|^{\alpha}}
    = \|c\|\cdot[u]\_{\alpha}.
\\]
Next we check the triangle inequality
\\[
    [u+v]\_{\alpha}
    = \sup\_{x \neq y}\frac{|(u+v)(x) - (u+v)(y)|}{\\\|x-y\\\|^{\alpha}}
    \leq \sup\_{x \neq y}\frac{|u(x) - u(y)|}{\\\|x-y\\\|^{\alpha}}
    + \sup\_{x \neq y}\frac{|v(x) - v(y)|}{\\\|x-y\\\|^{\alpha}}
    \leq [u]\_{\alpha} + [v]\_{\alpha}.
\\]
<div style="text-align: right"> \(\square\) </div>

**Proposition.** \\(\\\|\cdot\\\|\_{\alpha}\\) is a norm over \\(C^{\alpha}(X)\\).

*Proof.* Positive homogeneity of \\(\\\|\cdot\\\|\_{\alpha}\\) follows immediately from that of \\([\cdot]\_{\alpha}\\) and \\(\\\|\cdot\\\|\_{\sup}\\):
\\[
    \\\|cu\\\|\_{\alpha} 
    = \\\|cu\\\|\_{\sup} + [cu]\_{\alpha}
    = \|c\| \cdot (\\\|u\\\|\_{\sup} + [u]\_{\alpha})
    = \|c\|\cdot\\\|u\\\|\_{\alpha}.
\\]
Similarly, the triangle inequality of \\(\\\|\cdot\\\|\_{\alpha}\\) follows from that of \\([\cdot]\_{\alpha}\\) and \\(\\\|\cdot\\\|\_{\sup}\\):
\\[
    \\\|u+v\\\|\_{\alpha} 
    = \\\|u+v\\\|\_{\sup} + [u+v]\_{\alpha}
    \leq  \\\|u\\\|\_{\sup} + [u]\_{\alpha} + \\\|v\\\|\_{\sup} + [v]\_{\alpha}
    = \\\|u\\\|\_{\alpha} + \\\|v\\\|\_{\alpha}.
\\]
Finally, positive definiteness of \\(\\\|\cdot\\\|\_{\alpha}\\) follows from the positive definiteness of \\(\\\|\cdot\\\|\_{\sup}\\). Indeed, if \\(0 = \\\|u\\\|\_{\alpha} = \\\|u\\\|\_{\sup} + [u]\_{\alpha}\\) then we must have \\(\\\|u\\\|\_{\sup} = 0\\), implying \\(u = 0\\).
<div style="text-align: right"> \(\square\) </div>

**Proposition.** The inclusion \\(C^{\alpha}(X) \hookrightarrow C^{0}(X)\\) is a continuous embedding.

*Proof.* 

**Proposition.** The *Hölder space* \\(C^{\alpha}(X)\\) is a Banach space.

*Proof.* Take a Cauchy sequence \\(u\_k \in C^{\alpha}(X)\\). Then 


## Compact embedding theorems
