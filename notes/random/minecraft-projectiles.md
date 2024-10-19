---
layout: page
title: Minecraft Projectiles
description: A description and derivation of explicit and accurate equations of motion for minecraft projectiles.
---

## Minecraft Projectile Motion

#### Results
The horizontal position $r(t)$ and the vertical position in $y(t)$ measured in blocks of a launched projectile $t$ ticks after launch is given by the following equations
\\[\begin{align}
    x(t) &= \frac{v\cos\phi}{\alpha}(1-e^{-\alpha t})\\\\\
    y(t) &= h - \frac{g}{\alpha}t + \frac{g-\alpha v\sin\phi}{\alpha^2}(1-e^{-\alpha t}).
\end{align}\\]
where $g$ is the acceleration of gravity, $v$ is the launch velocity, $\alpha$ is the air resistance coefficient, $h$ is the height at which the projectile is launched, and $\phi$ is the pitch the projectile was launched. Furthermore, we can manipulate these equations to get a time independent equation with the vertical position $y$ in terms of the horizontal position $r$.
\\[
    y = h+\frac{g}{\alpha^2}\log\left(1-\frac{\alpha}{v\cos\phi}r\right)+\left(\frac{g-\alpha v \sin\phi}{\alpha v \cos\phi}\right)r
\\]

The above equations can be used to model the motion of a variety of projectiles including enderpearls, arrows, and even llama spit. For instance, given a particular projectile and a desired horizontal distance and height, we can solve for the pitch $\phi$ in the time independent equation to get a powerful aimbot. This could be done in a <a href="/files/aimbot.py">few lines of python</a>.

For player launched projectiles, the height $h$ is $1.52$ blocks above the blocks the player is standing on and the air resistance is $\alpha = 0.01$ tick$^{-1}$. However, the launch velocity $v$ and acceleration of gravity $g$ depends on the particular projectiles, so I have listed a <a href="#tables">table</a> of these values at the end of this page.

#### Visual
Plotting these equations in Desmos gives the following curves. Feel free to mess with the settings to see how different projectiles behave.
<iframe src="https://www.desmos.com/calculator/vnl4tjlsps" style="min-height:500px" width="100%"></iframe> 

#### Pseudocode
Where did these equations come from? The starting point is analyzing how the minecraft code treats projectiles. Assuming the projectile we are considering has gravity and is not in water, the minecraft code is summarized in the following pseudocode (the <a href="#minecraft-code">actual code</a> is attached at the end of this page).
<pre>
<code>//update position:
pi = projectile.getPosition()
vi = projectile.getVelocity()
pf = pi+vi
projectile.setPosition(pf)
//update velocity:
g = projectile.getGravity()
gravityVector = (0, g, 0)
alpha = 0.01
vf = vi - alpha*vi - gravityVector
projectile.setVelocity(vf)
</code>
</pre>
The standard unit of time in Minecraft is a tick (0.05 seconds) and the game updates every tick. The standard unit of distance is a block. Hence the positions in the above code are 3-vectors using the units of blocks, the velocities are 3-vectors in units of blocks/tick, and gravityVector is a downwards pointing vector with magnitude representing the acceleration of gravity in blocks/tick$^2$. We can think of alpha a drag coefficient with tick$^{-1}$ units.

#### Modeling Projectiles with a Differential Equation
We aim to compute the position $p(t) = (x(t), y(t), z(t))$ as a fuction of time. Note that Minecraft uses the velocity to update the position in the above code. In particular, if $v(t)$ is the velocity of the projectile over time, we have
\\[
    \frac{d p}{d t} = v
\\]
as expected.

That is, in order to compute the position $p(t)$ we need to first find the velocity $v(t) = (\dot{x}(t), \dot{y}(t), \dot{z}(t))$. For this, examine how Minecraft updates the velocity in the above pseudocode. Letting $\alpha$ be the drag coefficient and letting $g$ be the acceleration of gravity of the projectile, the below differential equations give the change in velocity of the projectile.

\\[
\begin{align}
    \frac{d \dot{x}}{d t} = -\alpha \dot{x} \hspace{1cm}
    \frac{d \dot{y}}{d t} = -\alpha \dot{y} - g \hspace{1cm}
    \frac{d \dot{z}}{d t} = -\alpha \dot{z}
\end{align}
\\]

#### Solving the Differential Equations
By relabeling the coordinate axes if necessary, we can assume that the projectile has initial position $(0,0,0)$ and initial velocity $v = (v_x, v_y, 0)$ in the $x,y$ plane. In this case, we have the trivial solutions $\dot{z}(t) = 0$ and $z(t) = 0$. Thus it only remains to consider the $x$ and $y$ directions. 

Next we solve for $x(t)$. Indeed, by using the standard separation of variables method we manipulate each side of the equation to get a candidate for $\dot{x}(t)$ as follows.
\\[
\begin{align}
    \frac{d \dot{x}}{d t} &= -\alpha \dot{x}\\\\\
    \int_{s = 0}^t \frac{1}{\dot{x}}\frac{d \dot{x}}{d s}ds &= -\int_{s = 0}^{t}\alpha dt\\\\\
    \log(\dot{x}(t)) - \log(\dot{x}(0)) &= -t\alpha\\\\\
    \dot{x}(t) &= v_x e^{-\alpha t}
\end{align}
\\]
Note $\dot{x}(t) = v_x e^{-\alpha t}$ satisfies the differential equation and so is a valid solution. Armed with the function $\dot{x}(t)$, we can compute $x(t)$ by integrating once more.
\\[\begin{align}
    \int_{s=0}^t\dot{x}ds &= \int_{s=0}^tv_x e^{-\alpha s}ds\\\\\
    x(t) &= \frac{v_x}{\alpha}(1-e^{-\alpha t})
\end{align}\\]

We now solve for $y(t)$ using the remaining differential equation to first solve for $\dot{y}$. We are given
\\[
    \frac{d \dot{y}}{d t} = -\alpha \dot{y} - g 
    \implies 
    \alpha \dot{y} + \frac{d \dot{y}}{d t} = -g
\\]
Solving differential equations of this form requires the integrating factors technique. We manipulate the equation by multiplying both sides by a function $\mu(t)$ and see what happens.
\\[
    \alpha \mu \dot{y} + \mu\frac{d \dot{y}}{d t} = -g\mu
\\]
The key observation of the integrating factors technique is that if $\dot{\mu} = \alpha \mu$, then the left hand side of the above will simplify greatly to \\(\frac{d (\mu \dot{y})}{d t}\\) by undoing the product rule. Therefore, we will choose $\mu(t) = e^{\alpha t}$ so that we indeed have $\dot{\mu} = \alpha \mu$. With this, we can compute what such a solution must be:
\\[\begin{align}
    \alpha e^{\alpha t} \dot{y} + e^{\alpha t}\frac{d \dot{y}}{d t} &= -ge^{\alpha t}\\\\\
    \frac{d}{d t}(e^{\alpha t} \dot{y}) &= -ge^{\alpha t}\\\\\
    \int_{s=0}^{t}\frac{d}{d s}(e^{\alpha s} \dot{y})ds &= \int_{s=0}^{t} -ge^{\alpha s} ds\\\\\
    e^{\alpha t}\dot{y} - v_y &= -\frac{g}{\alpha}(e^{\alpha t} - 1)\\\\\
    \dot{y} &= -\frac{g}{\alpha} + \frac{\alpha v_y+g}{\alpha}e^{-\alpha t}\\\\\
\end{align}\\]
The above does indeed satisfy the differential equation and initial conditions and so is a solution. Integrating once more yields the solution for $y(t)$.
\\[\begin{align}
    \int_{s=0}^{t}\dot{y}ds &= \int_{s=0}^{t}-\frac{g}{\alpha} + \frac{\alpha v_y+g}{\alpha}e^{-\alpha s}ds\\\\\
    y(t) &= -\frac{g}{\alpha}t + \frac{\alpha v_y+g}{\alpha^2}(1-e^{-\alpha t})
\end{align}\\]

To summarize, we found that if $r$ is the horizontal direction that the projectile is thrown, then
\\[\begin{align}
    r(t) &= \frac{v_x}{\alpha}(1-e^{-\alpha t})\\\\\
    y(t) &= -\frac{g}{\alpha}t + \frac{\alpha v_y+g}{\alpha^2}(1-e^{-\alpha t}).
\end{align}\\]

We can add to these results to make them more practical. For example, each projectile is launched at a fixed velocity $v$, so if it is thrown at an angle $-\phi$ above the horizontal, then we can write $v_x = v\cos\phi$ and $v_y = -v\sin\phi$ (this is the pitch angle you can see on the F3 menu). Furthermore, we can slightly shift coordinates to let $h$ be the heigh that the projectile is launched from. This yields the equations stated in the first section:
\\[\begin{align}
    r(t) &= \frac{v\cos\phi}{\alpha}(1-e^{-\alpha t})\\\\\
    y(t) &= h -\frac{g}{\alpha}t + \frac{g-\alpha v\sin\phi}{\alpha^2}(1-e^{-\alpha t}).
\end{align}\\]

Next, we can condense these equations by solving for $t$ in terms of the horizontal position $r$.
\\[
  t = -\frac{1}{\alpha}\log\left(1-\frac{\alpha}{v\cos\phi}r\right)
\\]
Then we can substitute this $t$ value into the equation for the vertical position $y$ and simplify to get
\\[
  y = h+\frac{g}{\alpha^2}\log\left(1-\frac{\alpha}{v\cos\phi}r\right)+\left(\frac{g-\alpha v \sin\phi}{\alpha v \cos\phi}\right)r
\\]


#### Actual Minecraft Code
<pre id = "minecraft-code">
<code>//The relevant code below can be found in ThrowableProjectile.java
//under the tick() function when using DecompilerMC for 1.16.1
object = this.getDeltaMovement();
double d = this.getX() + ((Vec3)object).x;
double d2 = this.getY() + ((Vec3)object).y;
double d3 = this.getZ() + ((Vec3)object).z;
this.updateRotation();
if (this.isInWater()) {
    for (int i = 0; i < 4; ++i) {
        float f2 = 0.25f;
        this.level.addParticle(ParticleTypes.BUBBLE, d - ((Vec3)object).x * 0.25,
        d2 - ((Vec3)object).y * 0.25, d3 - ((Vec3)object).z * 0.25, 
        ((Vec3)object).x, ((Vec3)object).y, ((Vec3)object).z);
    }
    f = 0.8f;
} else {
    f = 0.99f;
}
this.setDeltaMovement(((Vec3)object).scale(f));
if (!this.isNoGravity()) {
    Vec3 vec3 = this.getDeltaMovement();
    this.setDeltaMovement(vec3.x, vec3.y - (double)this.getGravity(), vec3.z);
}
this.setPos(d, d2, d3);
</code>
</pre>

#### Projectile Velocity and Gravity Values
<div id = "tables"></div>
Player launched projectiles have an air resistance coefficient $\alpha = 0.01$ tick$^{-1}$ and at a height of $h = 1.52$ above the block the player is standing on. However, the launch velocity $v$ and the acceleration of gravity $g$ depend on the particular projectile:
 <table>
  <tr>
    <th>Object</th>
    <th>Launch velocity</th>
    <th>Acceleration of gravity</th>
  </tr>
  <tr>
    <td>Fully drawn bow</td>
    <td>3.0 blocks/tick</td>
    <td>0.05 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Crossbow</td>
    <td>3.15 blocks/tick</td>
    <td>0.05 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Trident</td>
    <td>2.5 blocks/tick</td>
    <td>0.05 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Splash Potion</td>
    <td>0.5 blocks/tick</td>
    <td>0.05 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Enderpearl</td>
    <td>1.5 blocks/tick</td>
    <td>0.03 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Snowball</td>
    <td>1.5 blocks/tick</td>
    <td>0.03 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Egg</td>
    <td>1.5 blocks/tick</td>
    <td>0.03 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Experience Bottle</td>
    <td>0.7 blocks/tick</td>
    <td>0.07 blocks/tick$^2$</td>
  </tr>
</table>

#### Mob Projectile Velocity and Gravity Values
The same laws of physics govern a variety of mob-launched items, including the following:
 <table>
  <tr>
    <th>Object</th>
    <th>Launch velocity</th>
    <th>Acceleration of gravity</th>
  </tr>
  <tr>
    <td>Llama spit</td>
    <td>1.5 blocks/tick</td>
    <td>0.06 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Skeleton arrow</td>
    <td>1.6 blocks/tick</td>
    <td>0.03 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Witch potion</td>
    <td>0.75 blocks/tick</td>
    <td>0.05 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Snowgolem snowball</td>
    <td>1.6 blocks/tick</td>
    <td>0.03 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Drowned trident</td>
    <td>1.6 blocks/tick</td>
    <td>0.05 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Illusioner arrow</td>
    <td>1.6 blocks/tick</td>
    <td>0.05 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Pillager crossbow</td>
    <td>1.6 blocks/tick</td>
    <td>0.05 blocks/tick$^2$</td>
  </tr>
  <tr>
    <td>Piglin</td>
    <td>1.6 blocks/tick</td>
    <td>0.05 blocks/tick$^2$</td>
  </tr>
</table>