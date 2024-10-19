---
layout: page
title: Dynamical Systems
---

## Dynamical Systems

#### Motivation

/\*TODO: general motivation. Specific motivation will usually be whatever dynamical system the reader needs to study.\*/

#### Continuous time dynamical system

In general, we are interested in mathematical systems made up of the following ingredients.
* A set \\(X\\) called the *phase space*. An element of \\(X\\) represents a possible state of the system.
* A family of bijections \\(\varphi\_t: X \to X\\) called the *evolution law*, parametrized by \\(t \in \mathbb{R}\\). If the system is in a particular state \\(x \in X\\), then it is understood that the system will be in the state \\(\varphi\_t(x)\\) after time \\(t\\). Thus these evolution laws must satisfy \\(\varphi_t \circ \varphi_s = \varphi_{t+s}\\) for all \\(s,t \in \mathbb{R}\\).

The pairing of a phase space \\(X\\) with a time evolution law \\(\varphi\_t: X \to X\\) for \\(t \in \mathbb{R}\\) is called a *continuous time dynamical system*. Such a dynamical system is often written as simply \\(\varphi\_t: X \to X\\).

/\*is there more to say? maybe give examples here?\*/

#### Discrete time dynamical system

Often times we encounter "discrete time dynamical systems" in which the evolution law happens in discrete "jumps". In the discrete case, the ingredients are even simpler and are given as follows.
* A set \\(X\\) called the *phase space*. Again, an element of \\(X\\) represents a possible state of the system.
* A bijection \\(f: X \to X\\) called the *evolution law*. If the system is in state \\(x \in X\\), then after one jump it will be in state \\(f(x)\\), so after \\(n\\) jumps it will be in state \\(f^n(x)\\).

Then the pairing of the evolution law \\(f: X \to X\\) with the phase space \\(X\\) is called a *discrete time dynamical system*. Even if you are ultimately interested in studying continuous time dynamical systems, the theory of discrete time dynamical systems is extremely useful. This is in part for pedagogical reasons: the simplest examples to demonstrate various phenomenon in dynamical systems are often discrete. Secondly, however, given an continuous time dynamical system \\(\varphi_t: X \to X\\), we can choose some small time \\(t_0 \in \mathbb{R}\\) and get the simpler discrete time dynamical system \\(\varphi_{t_0}: X \to X\\), which often closely mdoels the dynamics of the continuous system and is easier to study.

#### Examples

/\*TODO... classic examples. Perhaps each example has its own page, though.\*/