---
layout: page
title: Gravity
---
/\*classical view\*/

/\*include visuals\*/

/\*this is just an outline, needs elaboration\*/

/\*below is a more sophisticated view to gravity than learned in physics classes\*/

The trajectory of an object in three dimensional space is represented by a path \\(\gamma(t)\\).

If this object is near some mass, the gravitational pull will accelerate \\(\gamma\\). In particular, the mass has a *gravitational field* vector field \\(\mathbf{F}\\) associated to it that determines the acceleration of the object by \\(\frac{d^2}{d t^2}\gamma(t) = \mathbf{F}\\).

There exists some potential function \\(\Phi\\) satisying \\(\grad{\phi} = \mathbf{F}\\). This potential function determines \\(\mathbf{F}\\), which in turn determines how the path \\(\gamma(t)\\) accelerates. That is, \\(\Phi\\) determines how gravity acts.

For the situation of a single point mass at \\((0,0,0)\\), the vector field \\(\mathbf{F}\\) is defined on \\(\mathbb{R} \setminus \\{0\\}\\) and satisfies \\(\div(\mathbf{F}) = 0\\) on this domain. Therefore \\(\Delta \Phi = \div(\grad{\Phi}) = \div(\mathbf{F}) = 0\\).

Therefore the potential function of a single point mass at \\(\mathbf{0}\\) determines some potential function \\(\Phi\\) on \\(\mathbb{R} \sm \{\mathbf{0}\}\\) that holds the key to determining the trajectory of nearby objects. Furthermore, we know \\(\Phi\\) satisfies the *Poisson equation*
\\[\Delta \Phi = 0,\\] 
which is actually enough to /\*mostly\*/ determine \\(\Phi\\). Indeed, solving this yields
\\[
    \Phi(\mathbf{x}) = \frac{a}{|\mathbf{x}|}
\\]

/\*then use this form to derive laws of gravity\*/