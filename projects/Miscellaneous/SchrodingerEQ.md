# The Schrödinger Equation

The Schrödinger equation is a linear partial differential equation, which describes the stationary and time-evolving states of non-relativistic (traveling at velocities
much smaller than the speed of light) particles. The variable in the this differential equation is the complex, time-dependent
quantity known as the wavefunction, typically denoted $\Psi(r,t)$. The Schrödinger equation for a single-particle system takes is given by: 

$$
\begin{align}
\tag{1}
i\hbar\frac{\partial \Psi(r,t)}{\partial t} &= \frac{-\hbar}{2m}\nabla^2 \Psi(r,t) + \hat{V}(r,t) \Psi(r,t)\\
&\text{with $\nabla$ the Laplace operator}\\
\nabla&=\left(\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}\right)
\end{align}
$$

where the left-hand side describes the time-dependence of the equation and the right hand-side is a sum of the kinetic energy of the particle,
given by the kinetic energy operator, $\frac{-\hbar}{2m}\nabla^2$, and the potential energy $\hat{V}(r,t)$ which describes the interactions the particle
is subjected to. The sum of the kinetic and potential energy operator consists of the Hamiltonian of the system and is often represented with
the symbol $\hat{H}$. Using this notation, the Schrödinger equation can be written more succinctly as:

$$
\begin{align}
\tag{2}
i\hbar\frac{\partial \Psi(r,t)}{\partial t} = \hat{H}(r,t)) \Psi(r,t)
\end{align}
$$

When we want to study a system (single or many-body) in quantum mechanics, we typically have to write the Hamiltonian of the system, 
and solve equation 1 with appropriate boundary conditions. This procedure is not trivial, and the ease or difficulty in solving the equation is 
heavily dependent on the potential term $\hat{V}(r,t)$.
In addition, a great number of problems of interests are not soluble analytically. Hence it is necessary to develop efficient numerical methods
to solve the equation.  
One of the initial steps in studying a quantum system is to differentiate wether we are analyzing a dynamic process 
(i.e time-evolving) or a time-independent process. If the process is time-independent, which explicitly means that the potential (and thus the Hamiltonian)
does not depend on time, we work with a different form of the Schrödinger equation. Morever, even when studying dynamic processes, 
it is sometimes possible to study the stationary states of the system first, and then treat the dynamic interaction as perturbation 
that will drive the system from one stationary state to another.  
How, then do we get from equation 1 to the time-independent Schrödinger equation?

## The Time-Independent Schrödinger Equation
When the potential term of the Hamiltonian is independent of time, equation 1 becomes an equation in which the operator on the left-hand side is 
time-dependent, while the one on the right-hand side is not:

$$
\begin{align}
\tag{3}
i\hbar\frac{\partial \Psi(r,t)}{\partial t} = \frac{-\hbar}{2m}\nabla^2 \Psi(r,t) + \hat{V}(r) \Psi(r,t)
\end{align}
$$

when confronted with a partial differential equation such as eq.3, we can guess that the total wavefunction $\Psi(r,t)$ is a product of 
a time-dependent function $\phi(t)$ and a time-independent function $\psi(r)$:

$$
\begin{align}
\tag{4}
\Psi(r,t) = \phi(t)\psi(r)
\end{align}
$$

We insert our guess function into the Schrödinger equation, and divide through by the product $\psi(r)\phi(t)$: 

$$
\begin{align}
\tag{5}
\frac{i\hbar}{\phi(t)}\frac{d\phi(t)}{dt}=\frac{-\hbar^2}{2m\psi(r)}\nabla^2\psi(r)+V(r)
\end{align}
$$

The left-hand side is time-dependent while the right-hand side is not, yet, the equation tells us they are equal. When two sides
of an equation, which depend on different variables, are equal, it means that they are equal to a constant. Knowing that the Hamiltonian operator
represents the total energy, $E$, of the system, we can set that constant to $E$.  
Setting the right-hand side equal to $E$ and multiplying through by $\psi(r)$, we obtain the **time-independent** Schrödinger equation (TISE):

$$
\begin{align}
\tag{6}
\frac{-\hbar^2}{2m}\nabla^2\psi(r)+V(r)\psi(r)=E\psi(r)\\
\text{more compactly}\\
\hat{H}(r)\psi(r)=E\psi(r)
\end{align}
$$

Setting the left-hand side equal to $E$ multiplying through by $\phi(t)$, we obtain a first order ordinary differential equation, of which, 
the solution is: 

$$
\begin{align}
\tag{7}
\phi(t) = e^{\frac{-iE}{\hbar}t}
\end{align}
$$

We do not yet know the solutions to eq.6. As we have stated, they are dependent on the potential term. However, eq.6 is an eigenvalue equation,
an equation in which an operator acting on a function yields a constant times the function. The functions are known as eigenfunctions[^1]. It is 
generally the case that an operator possesses more than one eigenfunction. As a result, even if we do not know what they are for now, we can
label them $\psi_n(r)$, where $n$ is an integer. It is important to note that each $\psi_n(r)$ has a corresponding $E_n$. 

[^1]: we also use the term eigenvectors (linear algebra) and or eigenstates (in quantum mechanics)


## Properties of The Eigenfunctions
The eigenfunctions of an operator are orthogonal to one another under the inner product (their inner product yields zero). In addition, in quantum mechanics, we typically 
normalize the eigenfunctions (the inner product of an eigenfunction with itself yields one) because this ensures that the total probability that a system is in a quantum state is $1$. We write the orthonormality
condition as: 

$$
\begin{align}
\tag{2.3}
\int_{all space}{\psi_m(r)^*\psi_n(r)}dr&=\delta_ {mn} \quad
\text{with $\delta_{mn}=1$ for m=n or $\delta_{mn}=0$ otherwise}
\end{align}
$$

This property implies that they form a set of linearly independent functions (basis functions), and further means that we can use a linear combination of the
eigenfunctions to describe any other function in the space spanned by these basis functions.  

There are lots of problems in which we are only interested in determining the eigenstates (time-independent problems) of the system. For instance
quantum chemists do this all the time to determine the electronic structure of atoms and molecules. Indeed, the familiar orbitals of the hydrogen atom consists of solutions 
to eq.6 for the spherically symmetric Coulomb potential.
