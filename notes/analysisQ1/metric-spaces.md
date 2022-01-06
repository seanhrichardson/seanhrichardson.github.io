---
layout: page
section: NOTES
title: Metric Spaces
---

## Metric Spaces
**Theorem.** In a metric space, the following are equivalent.
1. The space is separable.
2. The space is second countable.
3. The space is Lindelöf.

*Proof.*<br>

**Theorem.** In a metric space, the following are equivalent.
1. Complete & Totally Bounded
2. Sequentially Compact
3. Compact

*Proof.* <br>
$(2) \implies (1). $ Assume the space is sequentially compact. First, note each Cauchy sequence has a convergent subsequence; the limit of this subsequence will be the limit of the Cauchy sequence, giving completeness. Next, suppose for contradiction the space is not totally bounded, then there exists an $r > 0$ such that we can define a sequence $\\{x_i\\}$ inductively such that each $x_k$ rests in the following nonempty (by assumption) set.
\\[X \setminus \bigcup_{i < k} B(x_i,r)\\]
But then $\\{x_i\\}$ has no convergent subsequence.

$(1) \implies (2). $ Assume the space is complete and totally bounded. Consider any sequence $\\{x_i\\}$ and construct a subsequence as follows. 

$(1) + (2) \implies (3). $

$(3) \implies (2). $

test

test

test