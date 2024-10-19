---
layout: page
title: Ergodicity
---

/\*TODO: make sure have plenty of examples that display "chaotic behavior"\*/

/\*perhaps have an entirely seperate page dedicated to chaotic behavior?\*/

## Ergodicity

/\*give an example of a chaotic system?\*/

/\*change motivation for ergodicity and move this to the pointwise ergodic theorem page. It's too much to require the proof of the pointwise ergodic theorem just to motivate the definition of ergodicity...\*/

#### Time and space averages

/\*mention Boltzmann's ergodic hypothesis somewhere below\*/

Many dynamical systems that we encounter display "chaotic behavior" after a long enough time -- the phase space gets all "mixed up" in an unpredictable way. Given such a chaotic system, a natural question is if the phase space gets *uniformly* mixed up. That is, given some arbitrary initial state of our system and allowing a significant amount of time to elapse, are all possible elements of the phase space equally likely for our system to now reach? Let's try to formulate this property mathematically, starting with the discrete time case.

We need a finite invariant measure on our phase space to formulate a statement with probability, so we consider a measure-preserving dynamical system \\(T: X \to X\\) preserving a finite measure \\(\mu\\) on \\(X\\). Now consider a region \\(A \subset X\\) of the phase space. Fixing some initial state \\(x \in X\\), the probability that \\(T^k(x)\\) lands in the region \\(A\\) for large \\(k\\) is given by the time average
\\[
    \lim_{n \to \infty} \frac{1}{n} \sum_{k = 0}^{n-1} \chi_A(T^k(x))
\\]
where \\(\chi_A\\) is the indicator function. Under the ergodic hypothesis, we expect the probability that \\(T^k(x)\\) occupies the region \\(A\\) to be the proportion \\(\mu(A)/\mu(X)\\) of the phase space \\(A\\) takes up. In fact, we can formulate this hypothesis more generally by substituting an arbitrary measurable function for the indicator function \\(\chi_A\\). Indeed, given a measurable function \\(f: X \to \mathbb{R}\\), consider the *time average*
\\[
     \lim_{n \to \infty} \frac{1}{n} \sum_{k = 0}^{n-1} f(T^k(x)).
     \label{eq:time-average}
     \tag{T}
\\]
We will compare this to the *space average* for a function \\(f \in L^1(X)\\) given by
\\[
    \frac{1}{\mu(X)}\int_{X} f d\mu.
    \label{eq:space-average}
    \tag{S}
\\]

#### Existence of time average

/\*TODO: prove existence of time average\*/