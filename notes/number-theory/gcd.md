---
layout: page
section: NOTES
title: gcd
---

## Greatest Common Divisor

#### Definition
Take two integers \\(a\\) and \\(b\\). Then, the *greatest common divisor* of \\(a\\) and \\(b\\) is an integer \\(d\\) such that \\(d \mid a,b\\) and so that for any other integer \\(d'\\) with \\(d' \mid a,b\\), we have \\(d \mid d'\\). The greatest common divisor is denoted \\(\gcd(a,b)\\) or often just \\((a,b)\\).

#### Existence
The existence of \\(\gcd(a,b)\\) for any integers \\(a\\) and \\(b\\) is shown through the Euclidean Algorithm.

#### Uniqueness
If for integers \\(a\\) and \\(b\\) we have two gcd's, \\(d_1\\) and \\(d_2\\), then we have \\(d_1 \mid d_2\\) and \\(d_2 \mid d_1\\) by definition, giving uniqueness up to associates.