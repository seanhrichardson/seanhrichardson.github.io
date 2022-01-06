---
layout: page
section: NOTES
title: Euclidean Division
---

## Euclidean Division

#### Euclidean Division
Given two integers \\(a\\) and \\(b\\), there exists unique integers \\(q\\) and \\(r\\) such that \\(a = qb + r\\) and \\(0 \leq r < b\\).

#### Proof
Take the set of all integral q,r pairs satisfying \\(a = qb + r\\) and \\(r \geq 0\\). Note this set is nonempty as \\(q = 0\\) and \\(r = a\\) suffices. Next, take a q,r pair with minimal \\(r\\). Note if \\(r \geq b\\), then \\(a = (q-1)b+(r-b)\\) contradicts the minimality of \\(r\\), giving existence.

Assume two pairs \\(q, r\\) and \\(q', r'\\) satisfying the hypotheses. Then, we find \\(b \mid a-r, a-r'\\), giving \\(b \mid r - r'\\), imlpying \\(r = r'\\), which in turn gives \\(q = q'\\).