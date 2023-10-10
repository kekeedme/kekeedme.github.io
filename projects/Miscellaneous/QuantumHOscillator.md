# Three Flavors of the Quantum Harmonic Oscillator

A harmonic oscillator is a physical system in which, the force required to restore the system to its equilibrium 
position is proportional to the displacement from equilibrium. Classically, the harmonic oscillator model is usually applied
to the oscillation about an equilibrium point of a mass attached to a spring.
In one dimension, if the equilibrium position is $x=0$, 
the restoring force will then be: 

$$
\begin{align}
\tag{1}
F_{x}=-kx
\end{align}
$$

where $k$ is the force constant, which can for example, be related to the stiffness of the spring.
The force being conservative (meaning that the work done by the force is independent of path, only dependent on the initial
and final position), we can determine the potential energy stored in the oscillator for a given displacement $x$. Indeed, in our 1-D case, the potential energy is related to a conservative force by the relation:

$$
\begin{align}
\tag{2}
\frac{dV}{dx}=-F_{x}
\end{align}
$$

As a result, we find that the potential energy stored in the oscillator is quadratic with respect to the displacement: 

$$
\begin{align}
\tag{3}
V=\frac{1}{2}kx^2
\end{align}
$$

For a classical system, in order to get the equation of motion for such an oscillator, we would need to solve Newton's second law of motion by setting the restoring force $F_{x}$ equal to the product of mass times acceleration (the second derivative of the position with respect to time):

$$
\begin{align}
\tag{4}
m\frac{d^2x}{dt^2}=-kx\\
\frac{d^2x}{dt^2}+\omega^2x=0
\end{align}
$$

notice that we have set $\frac{k}{m}=\omega^2$, where $\omega$ is the frequency of oscillation. Solving the ordinary second order differential equation leads to oscillatory solutions of position as a function of time of the type: $x(t) = A\cos{\left(\omega t\right)}$, for an initial displacement $A$ at $t=0$. I have outlined the steps to solving this differential equation [here]() for the interested reader.  

Solving equation (4) is important because it allows us to obtain a quantitative description of the motion of the oscillator as a function of time. In addition, there is no damping in our case (no friction) taking away energy from the system. As a result it will oscillate forever. Perhaps it is more important to understand the relation between the shape of the potential, and the force acting on the system.  
Indeed we observe that, whatever the magnitude of the displacement, the potential energy of the system will always be given by eq.3. This observation means that the restoring force will always be able to compensate for the displacement, thereby causing our system to be "trapped" in this potential. In practice, we know this is not the case. We know that at a certain point, the spring will break. As a result, we understand that we can only maintain the interplay between the restoring force and the displacement, for small enough displacements. But what does it mean for a displacement to be "small enough"? We can better understand this by looking at a more realistic potential superimposed over the harmonic potential.


