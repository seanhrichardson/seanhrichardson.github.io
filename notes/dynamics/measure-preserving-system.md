---
layout: page
title: Measure Preserving System
---

## Measure Preseving Dynamical Systems

#### Motivation

/\*TODO: general motivation in terms of Liouville measure from mechanics?\*/

/\*TODO: specific motivation\*/

#### Measure Preserving Systems

Often times, as discussed above, the dynamical system we are considering comes with a natural measure on the phase space that is preserved under the evolution law for the dynamical system. It is useful, therefore, to develop a theory for studying dynamical systems with this extra structure. Such systems are called "measure-preserving systems" and are characterized as follows.

**Def (measure-preserving discrete time dynamical system).** A *measure-preserving dynamical system* is a dynamical system \\(f: X \to X\\) such that \\((X, \mu)\\) is a measure space, and \\(f\\) is a measurable function that *preserves the measure*; that is, \\(\mu(f^{-1}(A)) = \mu(A)\\) for all measurable \\(A \subset X\\).

**Def (measure-preserving continuous time dynamical system).** A *measure-preserving dynamical system* is a dynamical system \\(\varphi_t: X \to X\\) such that \\((X, \mu)\\) is a measure space and, for all \\(t \in \mathbb{R}\\), \\(\varphi_t\\) is a measurable function that *preserves the measure*; that is, \\(\mu(\varphi_t^{-1}(A)) = \mu(A)\\) for all measurable \\(A \subset X\\).