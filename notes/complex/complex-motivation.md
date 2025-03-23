---
layout: page
title: Complex Motivation
---

# Complex Numbers

/\*complex numbers are a useful tool\*/

/\*took centuries to be widely accepted and recognized\*/

## Complex numbers are useful tools

Complex numbers are a useful tool in solving real problems. Historically, the first hints of the usefulness of complex numbers arose in the 16th century when mathematicians /\*names?\*/ found a formula to solve cubic equations. Through a change of variables, it turns out every cubic can be reduced to the form 
\\[x^3 = 3px + 2q\\]
for some real numbers \\(p\\) and \\(q\\), making cubics of this form important to study. Mathematicians /\*names?\*/ found that a solution \\(x\\) to these cubics is given by
\\[
    x = \sqrt[3]{q+\sqrt{q^2-p^3}} - \sqrt[3]{q-\sqrt{q^2-p^3}}.
\\]
This formula worked quite well. For example, a solution to \\(x^3 = 3x + 2\\) is now found quickly by inserting \\(p = 1\\) and \\(q = 1\\) to get
\\[
    x = \sqrt[3]{(1)+\sqrt{(1)^2 - (1)^3}} - \sqrt[3]{(1)-\sqrt{(1)^2 - (1)^3}} = 2,
\\]
and the computation \\((2)^3 = 3(2) + 2\\) verifies that \\(x = 2\\) is indeed a solution. Curiously, however, /\*names?\*/ found this formula did not always work. For example, /\*name\*/ studied the cubic \\(x^3 = 15x + 4\\), which when using \\(p = 5\\) and \\(q = 2\\) yields
\\[
    x = \sqrt[3]{2 + \sqrt{-121}} + \sqrt[3]{2-\sqrt{-121}}.
\\]
This process leaves us stuck with the square root of a negative number, which when solving quadratics indicates there is "no solution". However, notice this cubic does have the solution \\(x = 4\\) because \\((4)^3 - 15(4) = 4\\). To better understand this phenomenon, let's consider the much simpler cubic \\(x^3 = 3x\\), which is easy to solve without the use of a cubic formula. In this case, we get \\(p = 1\\) and \\(q = 0\\), so a solution *should* be given by
\\[
    x = \sqrt[3]{\sqrt{-1}} - \sqrt[3]{\sqrt{-1}}.
\\]
The above equation certainly "looks like" it should be \\(0\\) and interestingly, \\(x = 0\\) is a solution to \\(x^3 = 3x\\). However, in claiming \\(\sqrt[3]{\sqrt{-1}} - \sqrt[3]{\sqrt{-1}} = 0\\) we are allowing ourselves to preform operations such as addition and multiplication to \\(\sqrt{-1}\\). That is, *we are treating \\(\sqrt{-1}\\) as a number*. 

Expressions of the form \\(a + b\sqrt{-1}\\) show up naturally throughout mathematics (for example when solving \\(x^3 = 3x + 2\\)) and it is advantageous to treat these expressions as numbers, called *complex numbers*. Doing so will allow us to apply the cubic equation to \\(x^3 = 3x + 2\\) and in fact any cubic. Even though complex numbers do not represent anything physical, they are still a useful tool for solving real problems and are essential to study.