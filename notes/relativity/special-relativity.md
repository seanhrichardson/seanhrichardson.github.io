---
layout: page
title: Special Relativity
---

# Special Relativity

## A problem with intuition

Suppose you are floating in space: isolated and not accelerating. 
<!-- give more description of what you see in space for fun -->
Then suppose you see me rapidly approaching you at speed \\(v\\). You shine a flashlight in my direction: how fast do I measure the light coming out of your flashlight moving? Experimental evidence confirms that both you and me will measure the light emiting from your flashlight to be the same speed: about \\(299,792,458\\) m/s, which we call \\(c\\). However, it is customary (and convenient) for mathematicians to choose coordinates so that \\(c = 1\\). But this is a problem: if I am rapidly moving towards you and you emit something moving at the speed of light, shouldn't I measure that this moves faster than the speed of light?

Let's describe this problem more precisely. We each experience various *events*: particular locations in space occuring at a particular time. However, we have two different ways of describing the places and times of these events. You have coordinates \\((t,x,y,z)\\) to indicate an event at point \\((x,y,z)\\) and ocurring at time \\(t\\). You consider yourself to be staionary and at position \\(x = y = z = 0\\), so from your perspective, you follow the \\(t\\) axis in your coordinates. However, I also consider myself to be stationary and I consider you to be moving quickly towards me. So I have my own coordinate system \\((\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z})\\) where my own position follows the \\(\widetilde{t}\\) axis. For simplicity, suppose you have choosen coordinates so that it appears I am moving towards you in only the \\(x\\) direction, and I have choosen coordinates so that it appears you are moving towards me in only the \\(\widetilde{x}\\) direction. In this case, you compute the speed of the shining light by \\({\Delta x}/{\Delta t}\\) and I compute the speed of the light by \\({\Delta \widetilde{x}}/{\Delta \widetilde{t}}\\). However, the problem is that you intuitively expect my coordinate system to be related to your coordinate system by the simple relation \\((\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z}) = (t, x+tv, y, z)\\); however, this intuition is *not true* for it incorrectly predicts that I measure the speed of light to be
\\[
    \frac{\Delta \widetilde{x}}{\Delta \widetilde{t}} = \frac{\Delta x + v\Delta t}{\Delta t} = c + v > c.
\\]
Therefore, the relation between your coordinates \\((t,x,y,z)\\) and my coordinates \\((\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z})\\) is not quite so intuitive. In order to correctly discover this relation, we should carefully lay out some axioms so that we are not fooled by incorrect intuition.

/\*possibly some Lorentz transformation visuals before formalizing...\*/

## Axioms

We both experience the world of events: particular moments at particular places in space. The space of events is called *space-time* which we consider to be the space \\(\mathbb{R}^{3+1}\\). Then different inertial observers close to eachother experience the same space \\(\mathbb{R}^{3+1}\\) of events, but each inertial observer might choose different coordinate axes so that coordinates \\((t,x,y,z)\\) have different meanings. However, we understand these coordinates to be choosen so that the inertial observer computes the velocity of objects by \\(\sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2}/\Delta t\\). In particular, each inertial observer considers themselves to be stationary with velocity \\(0\\) and therefore is moving in the positive \\(t\\) direction in their own coordinates. Furthermore, all coordinate systems must obey some axioms:
1. All inertial observers measure the same speed of light \\(c\\).
2. If an inertial observer is moving at speed \\(\|v\|\\) relative to you, then they observe you moving at the same speed \\(\|v\|\\) relative to them.<br><br>
We hope to study the relationship between different coordinate systems. That is, if you have coordinates \\((t,x,y,z)\\) and I use coordinates \\((\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z})\\), then what is the map \\(\mathbb{R}^{3+1} \to \mathbb{R}^{3+1}\\) given by \\((t,x,y,z) \mapsto (\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z})\\) such that, given a point in your coordinates, returns the the values in my coordinates that describe this same point. We make one more assumption.<br><br>
3. The change in coordinates \\((t,x,y,z) \mapsto (\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z})\\) is linear.

This final assumption is less convincing and indeed this final assumption is discarded in the theory of general relativity. However, we can continue forward with the understanding that the change of coordinates map we find is the linear approximation of the actual change of coordinates map, which is still useful and accurate enough in applications. 

## Invariance of the Interval

/\*state that we are located at the same point in space-time more clearly\*/

/\*Note: will use \\((t,z,y,z)\\) for coordinates. Can consider \\((\Delta t,\Delta z,\Delta y,\Delta z)\\) as the vector \\(\Delta t \partial\_t + \Delta x \partial\_x + \Delta y \partial\_y + \Delta z \partial\_z\\)\*/

Let's use these axioms to make some deductions about how our coordinate systems must be related. Indeed, by axiom (1), according to your coordinates \\((t,x,y,z)\\), you will measure light in the following set (remember we chose units so that the speed of light \\(c\\) is \\(1\\)).
\\[
    Z = \left\\{(\Delta t,\Delta x, \Delta y, \Delta z) : \frac{\Delta x^2 + \Delta y^2 + \Delta z^2}{\Delta t^2} = c = 1 \right\\}.
\\]
where we unserstand \\((\Delta t,\Delta x, \Delta y, \Delta z) = (t,x,y,z) - (t\_0, x\_0, y\_0, z\_0)\\) if the observer is located at point \\((t\_0, x\_0, y\_0, z\_0)\\). We can rewrite this as the zero set 
\\[Z = \\{(\Delta t,\Delta x, \Delta y, \Delta z) : -\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2 = 0\\}.\\]

By the same reasoning, if I am an inertial observer using coordinates \\((\tilde{t},\tilde{x},\tilde{y},\tilde{z})\\) and positioned in the same point in space-time as you, then I will measure light in the zero set 
\\[\tilde{Z} = \\{(\Delta \tilde{t},\Delta \tilde{x}, \Delta \tilde{y}, \Delta \tilde{z}) : - \Delta \tilde{t}^2 + \Delta \tilde{x}^2 + \Delta \tilde{y}^2 + \Delta \tilde{z}^2 = 0\\}.\\]

The sets \\(Z\\) and \\(\tilde{Z}\\) both describe the same region that light will be observered, they were simply defined using different coordinates; that is, we have the set equality \\(\tilde{Z} = Z\\), which is a substantial restriction on how our coordinates can be related. A convenient way to rewrite this finding is by defining a function \\(m: \mathbb{R}^{3+1} \times \mathbb{R}^{3+1} \to \mathbb{R}\\) in your coordinates \\((t,x,y,z)\\) as
\\[
    m((\Delta t\_1,\Delta x\_1,\Delta y\_1,\Delta z\_1),(\Delta t\_2,\Delta x\_2,\Delta y\_2,\Delta z\_2)) 
    = -\Delta t\_1\Delta t\_2 + \Delta x\_1\Delta x\_2 + \Delta y\_1\Delta y\_2 + \Delta z\_1\Delta z\_2,
\\]
and defining a function \\(\tilde{m}: \mathbb{R}^{3+1} \times \mathbb{R}^{3+1} \to \mathbb{R}\\) in my coordinates \\((\tilde{t},\tilde{x},\tilde{y},\tilde{z})\\) as
\\[
    \tilde{m}((\Delta \tilde{t}\_1,\Delta \tilde{x}\_1,\Delta \tilde{y}\_1,\Delta \tilde{z}\_1),(\Delta \tilde{t}\_2,\Delta \tilde{x}\_2,\Delta \tilde{y}\_2,\Delta \tilde{z}\_2)) = -\Delta \tilde{t}\_1\Delta \tilde{t}\_2 + \Delta \tilde{x}\_1\Delta \tilde{x}\_2 + \Delta \tilde{y}\_1\Delta \tilde{y}\_2 + \Delta \tilde{z}\_1\Delta \tilde{z}\_2.
\\]
Then our previous result \\(Z = \widetilde{Z}\\) can be re-written as
\\[
    \\{v \in \mathbb{R}^{3+1}: m(v,v) = 0\\} = \\{v \in \mathbb{R}^{3+1}: \widetilde{m}(v,v) = 0\\}.
\\]
In other words, the zero sets of \\(m(v,v)\\) and \\(\widetilde{m}(v,v)\\) are identical. Rewritting our findings in this way is helpful because we can apply the result of the following exercise.

/\*explain why quadratic form determines bilinear form\*/

/\*this is where we use linear relationship assumption... emphasize this.\*/

**Exercise.**
/\*TODO: bilinear forms with same zeroes will be scalar multiples.\*/

**Solution.**
/\*TODO.\*/

By the above exercise, we conclude that there is some constant \\(\alpha\\) so that \\(m(v,v) = \alpha \tilde{m}(v, v)\\) for all \\(v\\). I now argue that in fact \\(\alpha = 1\\). Indeed, by the principle of relativity, the constant \\(\alpha\\) can depend only on the relative speed between the coordinate systems \\((t,x,y,z)\\) and \\((\widetilde{t},\widetilde{x},\widetilde{y},\widetilde{z}).\\) Thus if I, using coordinates \\((\widetilde{t},\widetilde{x},\widetilde{y},\widetilde{z})\\), carried out the same computation from my point of view, I should conclude \\(\widetilde{m}(v,v) = \alpha m(v,v)\\) for the same constant \\(\alpha\\). This can only be the case if \\(\alpha = 1\\).

/\*todo: define this is the Minkowski metric here...\*/

/\*above is a little hand-wavy. try to make formal argument using (2)\*/

## Lorentz Transformations

Once again, suppose you have coordinates \\((t,x,y,z)\\) and I have coordinates \\((\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z})\\). Then we are interested in the change of coordinate map \\((t,x,y,z) \mapsto (\widetilde{t}, \widetilde{x}, \widetilde{y}, \widetilde{z})\\). However, we are acually interested in the linear approximation of this map, which formally is a map \\(L: \mathbb{R}^{3+1} \to \mathbb{R}^{3+1}\\) from a vector space to itself. As you are using coordinates \\((t,x,y,z)\\), we let the vector \\(\partial\_t\\) be the unit vector in the direction of the \\(t\\)-axis with respect to these coordinates: this observer moves in the direction \\(\partial\_t\\) along the \\(t\\)-axis. Similarly, \\(\partial\_x\\), \\(\partial\_y\\), and \\(\partial\_z\\) are the unit directions along the \\(x\\), \\(y\\), and \\(z\\) axes respectively so that \\(\\{\partial\_t, \partial\_x, \partial\_y, \partial\_z\\}\\) spans the vector space \\(\mathbb{R}^{3+1}\\)n. In the same way, I define vectors \\(\\{\partial\_\widetilde{t}, \partial\_\widetilde{x}, \partial\_\widetilde{y}, \partial\_\widetilde{z}\\}\\) to span the vector space \\(\mathbb{R}^{3+1}\\).

Suppose you are an inertial observer and I am a separate inertial observer moving at speed \\(v\\) relative to you. We will use the Minkowski metric derived earlier to decude how our coordinate systems must be related. Without loss of generality, you can choose a basis \\(\\{\partial_t, \partial_x, \partial_y, \partial_z\\}\\) so that you observe me moving in the positive \\(x\\) direction with velocity \\(v\\). That is,
\\[
    \partial\_{\widetilde{t}} = \frac{\partial\_t + v\partial\_x}{\sqrt{1-v^2}}.
\\]
I will also observe you going at velocity \\(v\\) relative to me and so without loss of generality, I can choose a basis \\(\\{\partial_\widetilde{t},\partial_\widetilde{x},\partial_\widetilde{y},\partial_\widetilde{z}\\}\\) so that I observe you moving in the negative \\(\widetilde{x}\\) direction with velocity \\(v.\\) That is,
\\[
    \partial\_{t} = \frac{\partial\_\widetilde{t} - v\partial\_\widetilde{x}}{\sqrt{1-v^2}}.
\\]
Combining the two equations above, we can conclude /\*TODO\*/
\\[
    \partial_{\widetilde{x}} = \frac{\partial_x + v\partial_t}{\sqrt{1-v^2}}.
\\]
/\*todo... actually not obvious that we can WLOG align \\(\partial\_y, \partial\_{\widetilde{y}}\\) and same for z's... have to argue this.\*/

/\*finish and write down general form of lorentz transformation\*/

\\[
    .
\\]

/\*next, argue that *any* linear transformation that preserves the Minkowski metric is the change of coordinates for some choice of inerrtial observers\*/

/\*therefore... the *Lorentz transformations*, defined as the space of linear transformations that preserrve the Minkowski norm, are important\*/

## Time Dilation and Length Contraction

## Minkowski Metric
In this section, we give space-time a metric \\(m\\) that accurately captures the behavior of physics, the *Minkowski metric*. This will allow us to apply all the tools from Riemannian geometry to study relativity.

The laws of physics remain the same regarldess of how fast an inertial observer is moving, so the most important property of such a metric \\(m\\) is that *all inertial observers must observe the same metric*. In other words, the metric should be invariant under Lorentz transformations.

/\*Note to self: Geometry of a sphere stays the same under rotations, etc. Geometry (i.e. laws of physics) stay the same under Lorentz transformations.\*/

In fact, there is only one metric (up to scaling) that is invariant under Lorentz transformations, the *Minkowski metric*.

**Def.** The *Minkowski metric* is given by
\\[
    m = dx^2-dt^2
\\]

/\*note somewhere not a Riemannian metric, but rather a pseudo-riemannian metric.\*/

/\*Below reasons why the Minkowski metric is a good choice and the only choice.\*/

**Exercise.** Show that the Minkowski metric is invariant under Lorentz transformations.

**Solution.** TODO

**Exercise.** Show that any symmetric, bilinear map \\(m: \mathbb{R} \times \mathbb{R} \to \mathbb{R}\\) that is invariant under Lorentz transformations and satisfies \\(m(\partial_x, \partial_x) = 1\\) needs to be the Minkowsi metric.

**Solution.** TODO

**Exercise.** Show that all isometries of space-time \\(\mathbb{R} \times \mathbb{R}\\) under the Minkowski metric are Lorentz transformations.

**Solution.** TODO

#### Using the Minkowski Metric
In addition to invariance under Lorentz transformations, the Minkowski metric is useful in that we can use it to compute relative velocities between observers, the time that passes on each observers clock, and /\*time dilation, length contraction?\*/

Given two inertial observers \\(\partial_t\\) and \\(\partial_{\tilde{t}}\\), the relative velocity \\(v\\) between them is given by
\\[
    v = \sqrt{1- \frac{1}{m(\partial_t, \partial_{\tilde{t}})^2}}.
\\]
**Exercise.** Prove the above formula.

**Solution.**  /\*TODO... use Lorentz transformation.\*/

/\*Proper time\*/
\\[
    \tau = \int_{a}^{b}\sqrt{-m(\dot{\gamma}, \dot{\gamma})}ds
\\]



Recall that 

/\*motivation below... optional?\*/

## Geodesics in Minkowski space-time

/\*Solve geodesic equations\*/

/\*Inertial observers are geodesic paths \\(\gamma\\) s.t \\(m(\dot{\gamma}, \dot{\gamma}) = -1\\)... maybe make this point earlier?\*/

/\*Jumping point into GR... observers in free-fall should also be inertial (motivate this), so the curvature should behave such that \*/

## Apendix: Invariance of Minkowski Form Argument

**Scalar Multiple.**

Recall that in our coordinates, the symmetric bilinear form \\(m: V \times V \to \mathbb{R}\\) defined to be, for \\(w = w^t\partial_t + w^i \partial_i\\), given by
\\[m(u,v) = -u^tv^t + u^1v^1+u^2v^2+u^3v^3.\\]
We defined another bilinear form \\(\tilde{m}: V \times V \to \mathbb{R}\\) in other coordinates. We know \\(\tilde{m}\\) is symmetric, and \\(\tilde{m}(v,v) = 0\\) exactly when \\(m(v,v) = 0\\). In our coordinates, separating the time and the space coordinates, we know \\(\tilde{m}\\) is of the form
\\[\widetilde{m}(u,v) = u^tv^t\widetilde{m}\_{t,t} + 2u^tv^i\widetilde{m}\_{t,i} + u^iv^j\widetilde{m}\_{i,j}\\]
for unknown coefficients \\(\widetilde{m}\_{\alpha,\beta}\\) with \\(\alpha, \beta \in \\{t,1,2,3\\}\\). We now strategically evaluate \\(\widetilde{m}\\) at particular vectors to find these coefficients.

In your coordinates, consider the vectors \\(w = \partial_t + \partial_1\\) and \\(w' = \partial_t - \partial_1\\) noting \\(m(w,w) = 0\\) and \\(m(w',w')\\). Hence \\(\widetilde{m}(w,w) = 0\\) and \\(\widetilde{m}(w',w') = 0\\). Therefore,
\\[
    0 = \widetilde{m}(w',w') - \widetilde{m}(w,w) = \cdots = 4\widetilde{m}\_{t,1}.
\\]
Thus \\(\widetilde{m}\_{t,1} = 0\\) and by the same argument \\(\widetilde{m}\_{t,i} = 0\\) for all \\(i\\), yielding the updated expression
\\[
    \widetilde{m}(u,v) = u^tv^t\widetilde{m}\_{t,t} + u^iv^j\widetilde{m}\_{i,j}.
\\]
Next, define new vectors \\(w = \partial_t + \frac{1}{\sqrt{2}}(\partial_1 + \partial_2)\\) and \\(w' = \partial_t + \frac{1}{\sqrt{2}}(\partial_1 - \partial_2)\\). Note again we have \\(m(w,w) = 0\\) and \\(m(w',w')\\), thus \\(\widetilde{m}(w,w) = 0\\) and \\(\widetilde{m}(w',w') = 0\\). Therefore, we can conclude
\\[
    0 = \widetilde{m}(w,w) = \widetilde{m}(w',w') = \cdots = \widetilde{m}_{1,2}
\\]
Therefore \\(\widetilde{m}\_{1,2} = 0\\) and by the same argument, \\(\widetilde{m}\_{i,j} = 0\\) for all \\(i \neq j\\) and so we have the updated expression
\\[
    \widetilde{m}(u,v) = u^tv^t\widetilde{m}\_{t,t} + u^1v^1\widetilde{m}\_{1,1}+u^2v^2\widetilde{m}\_{2,2}+u^3v^3\widetilde{m}\_{3,3}.
\\]
Finally, define \\(w = \partial_t + \partial_i\\) for any \\(i\\). Again we have \\(m(w,w) = 0\\), thus \\(\widetilde{m}(w,w) = 0\\) and so
\\[
    0 = \widetilde{m}(w,w) = \widetilde{m}\_{t,t} + \widetilde{m}\_{i,i},
\\]
thus \\(\widetilde{m}\_{i,i} = -\widetilde{m}\_{t,t}\\) for all \\(i\\). Thus, taking \\(\alpha = -\widetilde{m}\_{t,t}\\), we conclude
\\[
    \widetilde{m}(u,v) = \alpha (-u^tv^t + u^1v^1+u^2v^2+u^3v^3) = \alpha \cdot m(u,v)
\\]

**Constant is 1.**

We have found that \\(\widetilde{m}(v,v) = \alpha m(v,v)\\) for some constant \\(\alpha\\). I now argue we in fact have \\(\alpha = 1\\). Indeed, by the principle of relativity, the constant \\(\alpha\\) can depend only on the relative speed between the coordinate systems \\((t,x,y,z)\\) and \\((\widetilde{t},\widetilde{x},\widetilde{y},\widetilde{z})\\). That is, if the observer \\((\widetilde{t},\widetilde{x},\widetilde{y},\widetilde{z})\\) carried out the same computation from their point of view, they should conclude \\(m(v,v) = \alpha \widetilde{m}(v,v)\\) for the same constant \\(\alpha\\). This can only be the case if \\(\alpha = 1\\).

/\*explain \\(m\\) is an invariant and define as inner product\*/

## Lorentz Transformations

/\*explain: studying transormations between observer bases... showing these must be exactly the transformations that leave minkowski norm invariant\*/

