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

where, $k$ is the force constant, which can for example, be related to the stiffness of the spring.
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

notice that we have set $\frac{k}{m}=\omega^2$. Solving the ordinary second order differential equation in (4) leads to oscillatory solutions of position as a function of time of the type: $x(t) = A\cos{\left(\omega t\right)}$, for an initial displacement $A$ at $t=0$.


