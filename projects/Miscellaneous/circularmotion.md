# Circular Motion

Suppose two point-like particles are interacting through an attractive interaction potential $V(r)$ which permeates space. The potential could be gravitational
due to the mass of the particles, or electric if the particles are oppositely charged. It does not really matter in this case, because we will not need the explicit expression for the potential. 
The interaction potential sets up a force between the two particles given by:

$$
\begin{align}
\tag{1}
\vec{F} &= \vec{\nabla} V(r)\\
\vec{\nabla}&=\left(\frac{\partial}{\partial x}\vec{i}+\frac{\partial}{\partial y}\vec{j}+\frac{\partial}{\partial z}\vec{k}\right)
\end{align}
$$


## Attraction in the Absence of Tangential Velocity (Linear Motion)

Let us consider one of the particles as the *source* particle, as it generates the field, and the second particle the *test* particle, 
which comes to interact with the source. Let us first suppose the *test* particle does not have an initial velocity, but starts off at an 
initial position in the vicinity of the *source* particle, then it will *feel* a force of attraction by the source due to the potential set up
by the *source*. In this case, the *test* particle obtaines a non-zero velocity oriented at the *source* particle, it is accelerated by the force. 
Since its initial velocity was zero, its change in velocity is simply that acquired due to the force: $\Delta \vec{v} = \vec{v}_c\propto \vec{F}$.
In this sample example, the *test* particle would only fall onto the *source* particle. The equation of motion can be obtained from Newton's
second law: 

$$
\begin{align}
\tag{2}
\vec{F} = m\frac{\Delta \vec{v}_c}{\Delta t}=\frac{\Delta \vec{p}_c}{\Delta t}
\end{align}
$$

where $m$ is the mass of the *test* particle, and $\vec{p}$ is the linear momentum of the particle.

<figure>
    <img src="/projects/figures/two_particle_attraction.png" alt="figure" width=250 height=200>
    <figcaption>Figure 1. Source particle (blue) sets up an attractive potential, which attracts a test particle (red) with no tangential velocitiy. The test particle is simply accelerated towards the source with a linear acceleration proportional to the velocity oriented
    towards the center</figcaption>
</figure>

## Attraction in the Presence of Tangential Velocity (Uniform Circular Motion)

Let us now consisder the same two particles interacting through the same potential. However, in this scenario, the *test* particle 
has an initial velocity $\vec{v}_1$ oriented as shown in figure 2. The attractive force $\vec{F}$ from the *source* particle will cause the velocity of the *test* particle to change (rotate by $\theta$) in a given time interval ($\Delta t$ ). The change will be in the direction of the velocity vector, but not its magnitude (uniform). Since this change in velocity ( $\Delta \vec{v}$ ) is proportional to the force, the two vectors will be colinear and their norms will be multiples of one another ($F=m\frac{\Delta v}{\Delta t}$). Hence we can geometrically obtain the new velocity vector $\Delta \vec{v}_2$ at the later time $\Delta t$ by adding $\Delta \vec{v}$ to $\vec{v}_1$ (the operation $\vec{v}_2-\vec{v}_1=\Delta \vec{v}$ is shown on figure 2, left panel). After this initial change, the particle has velocity $\vec{v}_2$ oriented as shown. Since the force still acts on the particle, it will generate a change in $\vec{v}_2$. That change will always be colinear with $\vec{F}$ (dashed green arrow), and we will generate a new vector $\vec{v}_3$ and so on. As such an influence is exerted on the *test* particle, the net result will be a circular motion around the *source* particle.

<figure>
    <img src="/projects/figures/circular_motion.png" alt="figure" width=300 height=200>
    <figcaption>Figure 2. Source particle (blue) sets up an attractive potential, which attracts a test particle (red) with initial velocitiy. The force exerted on the test particle causes a velocity change, which changes the direction of the particle. The net result is a circular motion around the source particle.
    towards the center</figcaption>
</figure>

## Centripetal Acceleration and Force
In the picture of circular motion described above, we see that the force acts as to attract the particle towards the center of the circle. For this reason we call it a **centripetal** ("center seeking") force. The associated acceleration ($\frac{\Delta \vec{v}}{\Delta t}$) is the **centripetal** acceleration. There are a many ways to derive the expression for the centripetal acceleration and force, here we will do it by considering the geometry of isoceles and congruent triangles, and arc length. Later, we will do it with calculus.   

<figure>
    <img src="/projects/figures/triangles.png" alt="figure" width=300 height=200>
    <figcaption>Figure 3. Isoceles triangle formed from the radius of the circular orbit and the arc length (left panel). Isoceles triangle for from the velocity vectors and the change in velocity. Both triangles are similar.
    towards the center</figcaption>
</figure>

Consider the triangles in figure 3. They are taken from the exact same situation as in figure 2. On the left panel, we have an isoceles triangle with sides $r$, $\Delta s$, the arc length. Recall that the arc length is the radius times the angle swept by the arc (with $\theta$ in radians), this means that $\theta$ is:

$$
\begin{align}
\tag{3}
\theta = \frac{\Delta s}{r}
\end{align}
$$

Secondly, consider the triangle in the right panel. This triangle is constructed from the two velocity vectors $\vec{v}_1$ and $\vec{v}_2$ and the base $\Delta \vec{v}$. Note that the angle $\theta$ is the same as before because it is the angle by which $\vec{v}_1$ rotates to become $\vec{v}_2$. Since $\vec{v}_1$ and $\vec{v}_2$ have the same norm, the triangle is also an isoceles triangle.  

The last consideration is that, if we take the time interval to be small enough, then the arc length will also be small, and in that limit
it becomes equal to the distance $\Delta s = v\Delta t=\Delta r$. In addition since the isoceles triangles are similar the ratio of their bases to their sides are equal. Hence, if we put all this together, we get the following expressions: 

$$
\begin{align}
\tag{4}
\frac{\Delta s}{r} =\frac{\Delta r}{r}= \frac{\Delta v}{v}\\
\tag{4.1}
\Delta v=v\frac{\Delta r}{r}
\end{align}
$$

The expression in equation 4.1 can be used for $\Delta v$ in Newton's equation to express the norm of the force as:

$$
\begin{align}
\tag{5}
F=mv\frac{\Delta r}{r\Delta t}\\
\tag{5.1}
F=m\frac{v^2}{r}
\end{align}
$$

In equation 5.1, we have used the fact that we are performing our analysis for a very small time interval (as $\Delta t\rightarrow 0$) in that limit we obtain $\lim_{\Delta t \rightarrow 0}\frac{\Delta r}{\Delta t}=v$. Hence the norm of the centripetal acceleration is:

$$
\begin{align}
\tag{6}
a_c=\frac{v^2}{r}
\end{align}
$$

## Angular Momentum 
