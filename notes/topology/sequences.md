---
layout: page
title: Sequences
---

## Convergent Sequences

**Exercise.** Given a metric space \\((X,d)\\) and a sequence \\(x_k \in X\\), prove that \\(x_k \to x \in X\\) if and only if for every open set \\(U\\) containing \\(x\\), there exists an \\(N \in \mathbb{N}\\) such that \\(x_k \in U\\) for all \\(k \geq N\\).
<details><summary><b>Solution</b></summary>
<p>First suppose \(x_k \to x\) and consider any open \(U \subset X\) containing \(x\). Then by definition there exists some open ball \(B_{\varepsilon}(x) \subset U\). By definition of convergence we can choose \(N \in \mathbb{N}\) such that for all \(k \geq N\) we have \(x_k \in B_{\varepsilon} \subset U\).</p>

<p>Conversely, suppose for every open set \(U\) containing \(x\), there exists an \(N \in \mathbb{N}\) such that \(x_k \in U\) for all \(k \geq N\) and choose any \(\varepsilon > 0\). Then by assumption, there exists some \(N\) such that for all \(k \geq N\) we have \(x_k \subset B_{\varepsilon}(x)\), so \(x_k \to x\).</p>
</details>

**Definition.** Given a topological space \\(X\\) and a sequence \\(x_k \in X\\), we say \\(x_k\\) *converges* to \\(x\\), written \\(x_k \to x\\), if for every open set \\(U\\) containing \\(x\\), there exists some \\(N \in \mathbb{N}\\) such that \\(x_k \in U\\) for all \\(k \geq N\\).