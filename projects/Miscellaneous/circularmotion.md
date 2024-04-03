# Circular Motion
Suppose two point-like particles are interacting through an attractive interaction potential $V(r)$ which permeates space,the potential could be gravitational
due to the mass of the particles, or electric if the particles are oppositely charged. It does not really matter in this case, because we will 
not need the explicit expression for the potential. The interaction potential sets up a force between the two particles, given by:

$$
\begin{align}
\tag{1}
\vec{F} &= \nabla V(r)\\
\text{with}~ \nabla &= \left(\frac{\partial{}}{{\partial x}}\vec{i}+\frac{\partial{}}{{\partial y}}\vec{j}+\frac{\partial{}}{{\partial z}}\vec{k}\right)
\end{align}
$$

## Attraction Under No Tangential Velocity (Linear Motion)

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

where $m$ being the mass of the *test* particle, and $vec{p}$ is the linear momentum of the particle.

## Attraction in the Presence of Tangential Velocity (Circular Motion)