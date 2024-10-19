---
layout: page
title: Complex Numbers
---

## Complex numbers

Expressions of the form \\(a + b\sqrt{-1}\\) show up naturally throughout mathematics (for example, in solving the cubic equation /\*link\*/), and it is useful to treat these expressions as numbers and establish rules for adding and multiplying these numbers. The number \\(\sqrt{-1}\\) is typically denoted by \\(i\\) where \\(i^2 = -1\\), which stands for *imaginary number*. An expression of the form \\(a + bi\\) is called a *complex number*.

Even though complex numbers do not represent anything physical, they are still a useful tool for solving real problems and are essential to study. Adding \\(\sqrt{-1}\\) improves our number system so that \\(\sqrt{z}\\) is always defined and so quadratics \\(x^2 = bx + c\\) always have a solution. In fact, we will see later that adding \\(\sqrt{-1}\\) ensures that *any* polynomial equation always has a solution, and other functions such as \\(\log z\\) will conveniently always be defined. You are already familiar with this sort of philosophy: adding negative numbers to the natural numbers ensures that subtraction is always defined; adding fractions to the integers ensures that division is always defined; adding irrational numbers to the rationals ensures that converging limits are always defined; adding \\(\sqrt{-1}\\) to the reals is the final improvement to our number system.

#### Operations on complex numbers

Consider two complex numbers \\(a + bi\\) and \\(\alpha + \beta i\\). Then addition is given by adding the *imaginary part* (the component of the number multiplied by \\(i\\)) and the *real part* (the components of the number that is not multiplied by \\(i\\)) separately. That is,
\\[
    (a + bi) + (\alpha + \beta i) = (a + \alpha) + (b + \beta)i.
\\]
The multiplication of complex numbers is given by distributing the multiplication as normal, then using that \\(i^2 = -1\\). That is,
\\[
    (a+bi)(\alpha + \beta i) = a\alpha + a \beta i + b \alpha i + b \beta i^2 = (a \alpha - b \beta) + (a \beta + b \alpha) i.
\\]
Subtraction is, as usual, the addition of a negative and so
\\[
     (a + bi) - (\alpha + \beta i) = (a - \alpha) + (b - \beta)i.
\\]
/\*division\*/

**Exercise.** /\*outline solution to cubic\*/

#### The complex plane

The set of all complex numbers is denoted by \\(\mathbb{C} := \\{x + iy: x,y \in \mathbb{R}\\}\\). The study of complex numbers becomes wonderfully visual when we associate each complex number \\(x+iy\\) with the point \\((x,y)\\) on the plane \\(\mathbb{R}^2\\); this correspondence is called the *complex plane*.

/\*visual for the complex plane.\*/

/\*operations on the complex plane\*/

/\*multiplication of complex numbers as a linear map on the plane... work towards the following\*/

Therefore, if \\(z = x + iy\\) is a complex number, then 

#### More operations on complex numbers

/\*re, im, modulus, conjugate, arg, etc.\*/

#### Analytic properties of the complex plane

/\*metric space, convergence, etc. (optional)\*/