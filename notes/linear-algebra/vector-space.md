---
layout: page
section: NOTES
title: Vector Space
---

## Vector Space

#### Definition
A set $V$ together with a field $F$, addition $+: V \times V \to V$, and scalar multiplication $\cdot : F \times V \to V$ is a *vector space* if the following hold for all $\mathbf{u},\mathbf{v},\mathbf{w} \in V$ and $\alpha, \beta \in F$.
* $(\mathbf{u}+\mathbf{v})+\mathbf{w} = \mathbf{u}+(\mathbf{v}+\mathbf{w})$
* $\mathbf{u}+\mathbf{v} = \mathbf{v} + \mathbf{u}$
* There exists $\mathbf{0} \in V$ such that $\mathbf{0} + \mathbf{v} = \mathbf{v} = \mathbf{v} + \mathbf{0}$
* Given $\mathbf{v} \in V$, there exists $\mathbf{-v}$ such that $\mathbf{v}+(\mathbf{-v})=\mathbf{0}$
* $(\alpha+\beta)\mathbf{v}=\alpha \mathbf{v} + \beta \mathbf{v}$
* $(\alpha)(\mathbf{u} + \mathbf{v}) = (\alpha \mathbf{u}) + (\alpha \mathbf{v})$
* $\alpha(\beta)\mathbf{v} = (\alpha \beta)\mathbf{v}$
* $1\mathbf{v} = \mathbf{v}$ where $1$ is the multiplicative identity in $F$.