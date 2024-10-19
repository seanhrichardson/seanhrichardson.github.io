---
layout: page
title: Continuity in Metric Spaces
---

/\*Need some more motivation here, but for now will give the result and proof.\*/

**Prop.** Let \\((X,d\_x)\\) and \\((Y,d\_Y)\\) be metric spaces and \\(f: X \to Y\\). Then the following are equivalent:
1. For all \\(x \in X\\) and \\(\varepsilon > 0\\) there exists \\(\delta > 0\\) such that for all \\(x' \in X\\) with \\(d_X(x,x') < \delta\\) we have \\(d_Y(f(x),f(x')) < \varepsilon\\).
2. If \\(\\{x_n\\} \subset X\\) is a sequence such that \\(x_n \to x\\) for some \\(x \in X\\), then \\(f(x_n) \to f(x)\\) in \\(Y\\).
3. If \\(U \subset Y\\) is an open set in \\(Y\\), then \\(f^{-1}(U)\\) is an open set in \\(X\\).

*Proof.*

\\((1) \implies (3).\\) Suppose (1) is true and consider any open set \\(U \subset Y\\). Then for any \\(x \in f^{-1}(Y)\\), we have \\(f(x) \in Y\\) and so by the definition of open set, there exists an open ball \\(B_{\varepsilon}(f(x))\\) of radius \\(\varepsilon\\) and centered at \\(f(x)\\) such that \\(B_{\varepsilon}(f(x)) \subset Y\\). By assumption, there must exist some \\(\delta > 0\\) such that the open ball \\(B_{\delta}(x)\\) satisfies \\(f(B_{\delta}(x)) \subset B_{\varepsilon}(f(x)).\\) Therefore,
\\[
    B_{\delta}(x) \subset f^{-1}(f(B_{\delta}(x))) \subset f^{-1}(B_{\varepsilon}(f(x))) \subset f^{-1}(U).
\\]
That is, each \\(x \in U\\) has an open neighborhood contained in \\(U\\) and so \\(U\\) is open.

\\((3) \implies (2).\\) Suppose (3) holds and consider any sequence \\(\\{x_n\\} \subset X\\) such that \\(x_n \to x\\) for \\(x \in X\\). Next take any \\(\varepsilon > 0\\) and note \\(B_{\varepsilon}(f(x))\\) is an open set containing \\(f(x)\\), so by (3) \\(f^{-1}(B_{\varepsilon}(f(x)))\\) is an open set containing \\(x\\), thus there exists some \\(\delta > 0\\) such that \\(B_{\delta}(x) \subset f^{-1}(B_{\varepsilon}(f(x))).\\) By definition of convergence, there then exists some \\(N \in \mathbb{N}\\) such that \\(n > N\\) implies \\(x\_n \in B\_{\delta}(x)\\). But then if \\(n > N\\) we also have \\(f(x_n) \in B_{\varepsilon}(f(x))\\) by
\\[
    f(x_n) \in f(B_{\delta}(x)) \subset f(f^{-1}(B_{\varepsilon}(f(x)))) \subset B_{\varepsilon}(f(x)),
\\]
so \\(f(x_n) \to f(x)\\).

\\((2) \implies (1).\\) We show the contrapositive, so assume (1) is false. Then there will exist \\(x \in X\\), \\(\varepsilon > 0\\), and some number \\(x\_n\\) such that \\(d_X(x\_n,x) < \frac{1}{n}\\) and yet \\(d_Y(f(x\_n),f(x)) \geq \varepsilon\\) for all \\(n \in \mathbb{N}\\). However, then \\(\\{x_n\\}\\) is a sequence such that \\(x_n \to x\\) yet \\(f(x_n) \not\to f(x)\\), so (2) does not hold.
