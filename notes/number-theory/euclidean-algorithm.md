---
layout: page
section: NOTES
title: Euclidean Algorithm
---

## Euclidean Algorithm

#### Motivation
For two integers \\(a\\) and \\(b\\) apply Euclidean division \\(a = bq + d\\) and note \\(\gcd(a,b) = \gcd(b,d)\\). Indeed, we clearly have \\(\gcd(b,d) \mid a,b\\), giving \\(\gcd(b,d) \mid \gcd(a,b)\\). Further, rearranging \\(a-bq = d\\) quickly gives \\(\gcd(a,b) \mid b,d\\), which gives \\(\gcd(a,b) \mid \gcd(b,d)\\). Thus, \\(\gcd(a,b)\\) and \\(\gcd(b,d)\\) are equivalent (up to associates).

This step equates finding the gcd of two numbers to finding the gcd of two smaller numbers. The Euclidean algorithm applies this step repeatedly until the gcd emerges trivially.

#### Proof of GCD Existence Using Euclidean Algorithm
Take two integers \\(a\\) and \\(b\\) and repeatedly apply Eudlicean division as outlined below.

\\[\\begin{align}
a &= q_1b + r_1 \\\\ b &= q_2r_1 + r_2 \\\\ r_1 &= q_3r_2 + r_3 \\\\ &\vdots \\\\ r_{n-2} &= q_n r_{n-1} + r_{n} \\\\ r_{n-1} &= q_{n+1}r_{n} \\end{align}\\]

It is implicitly assumed above that the Euclidean algorithm will terminate with \\(r_{n+1} = 0\\). This is indeed the case, for positive remainders will be distinct \\(b > r_1 > r_2 > \cdots > r_k > \cdots\\), thus a remainder must eventually hit \\(0\\), justifying the assumption.

Importantly, \\(r_n = \gcd(a,b)\\). Indeed, two quick inductive arguments show that \\(r_n \mid a,b\\) and if \\(d \mid a,b\\), then \\(d \mid r_n\\).

