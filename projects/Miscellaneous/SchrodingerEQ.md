# The Schrödinger Equation

The Schrödinger equation is a linear partial differential equation, which describes the time-evolving states of non-relativistic (traveling at velocities
much smaller than the speed of light) particles. The variable in this differential equation is the complex, time-dependent
quantity known as the wavefunction, typically denoted $\Psi(r,t)$. The Schrödinger equation for a single-particle system in 3 dimensions is given by: 

$$
\begin{align}
\tag{1}
i\hbar\frac{\partial \Psi(r,t)}{\partial t} &= \frac{-\hbar}{2m}\nabla^2 \Psi(r,t) + \hat{V}(r,t) \Psi(r,t)\\
&\text{with $\nabla^2$ the Laplace operator}\\
\nabla^2&=\left(\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}\right)
\end{align}
$$

where the left-hand side describes the time-dependence of the equation and the right hand-side is a sum of the kinetic energy of the particle,
given by the kinetic energy operator, $\frac{-\hbar}{2m}\nabla^2$, and the potential energy $\hat{V}(r,t)$ which describes the interactions the particle
is subjected to. The sum of the kinetic and potential energy operator consists of the Hamiltonian of the system and is often represented with
the symbol $\hat{H}$. Using this notation, the Schrödinger equation can be written more succinctly as:

$$
\begin{align}
\tag{2}
i\hbar\frac{\partial \Psi(r,t)}{\partial t} = \hat{H}(r,t) \Psi(r,t)
\end{align}
$$

The wavefunction has a few properties we should highlight:
 - $\Psi(r,t)$, and its derivative must be a continous over its domain.
 - $\Psi(r,t)\rightarrow 0$ as $r\rightarrow \pm\infty$.
 - $\Psi(r,t)$ must be square integrable (this follows from condition 2).
Namely, the integral of the absolute square of $\Psi(r,t)$ over any interval $\[a,b]\$ of its domaine must be a finite number $\int_{a}^{b} |\Psi(r,t)|^2 d\tau = A$.
Where $|\Psi(r,t)|^2 = \Psi(r,t)^* \Psi(r,t)$, (with $\Psi(r,t)^* $ being the complex conjugate of $\Psi(r,t)$ ).
This particular condition is due to the statistical interpretation of the wavefunction also known as the Born rule, namely that the probability of finding the particle in the interval $\[a,b]\$ at time $t$ is given by $\int_{a}^{b} |\Psi(r,t)|^2 d\tau$.
This condition tells us that $|\Psi(r,t)|^2$ is a *probability density*.

- $\Psi(r,t)$ must be normalized over its domaine: $\int_{D} |\Psi(r,t)|^2 d\tau = 1$ since the particle has to be somewhere. The
domain is determined by the physics of the system.

When we want to study a system (single or many-body) in quantum mechanics, we typically have to write the Hamiltonian of the system, 
and solve equation 1 with appropriate boundary conditions. This procedure is not trivial, and the ease or difficulty in solving the equation is 
heavily dependent on the potential term $\hat{V}(r,t)$.
In addition, a great number of problems of interests are not soluble analytically. Hence it is necessary to develop efficient numerical methods
to solve the equation.  
One of the initial steps in studying a quantum system is to differentiate wether we are analyzing a dynamical process 
(i.e time-evolving) or a time-independent process. If the process is time-independent, which explicitly means that the potential (and thus the Hamiltonian)
does not depend on time, we work with a different form of the Schrödinger equation, which posseses time-independent solutions (stationary states). Morever, even when studying dynamical processes, 
it is sometimes possible to study the stationary states of the system first, and then treat the dynamical interactions as perturbations 
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
label them $\psi_n(r)$, where $n$ is an integer. It is important to note that each $\psi_n(r)$ has a corresponding $E_n$ (each eigenfunction its eigenvalue). It is also possible for two eigenfunctions $\psi_n(r)$ and $\psi_m(r)$ to have the same eigenvalue $E_n$. Such eigenfunctions are said to be **degenerate**. 

[^1]: we also use the term eigenvectors (linear algebra) and or eigenstates (in quantum mechanics)


## Properties of The Eigenfunctions
The eigenfunctions of an operator are orthogonal to one another under the inner product (the inner product of two distinct eigenfunction yields zero). In addition, we typically 
normalize the eigenfunctions (the inner product of an eigenfunction with itself yields one) because this ensures that the total probability that a system is in a quantum state (say $\psi_n(r)$) is $1$. The orthogonality of the functions, in addition to them being normalized make them orthonormal functions. We write the orthonormality condition as: 

$$
\begin{align}
\tag{8}
\int_{all space}{\psi_m(r)^*\psi_n(r)}dr&=\delta_ {mn} \quad
\text{with $\delta_{mn}=1$ for m=n or $\delta_{mn}=0$ otherwise}
\end{align}
$$

This property implies that they form a set of linearly independent functions (basis functions), which we can use to describe any other function in the vector space spanned by these basis functions, through an appropriate linear combination. As a perhaps familiar example, this fact is akin to using the set of orthogonal unit vectors $\left(\hat{i},\hat{j},\hat{k}\right)$ to describe any vector in real 3-D space. For instance:

$$
\begin{align}
\tag{9}
\vec{v}=\begin{pmatrix} 3\\ 
4\\ 
6 \end{pmatrix} = \left(3\hat{i}+4\hat{j}+6\hat{k}\right)
\end{align}
$$

The main differences with the above example is that the vector spaces spanned by the eigenfunctions are complex vector spaces, and are infinite dimensional (meaning that we need an infinite amount of basis functions to span the entire space).
They are a type of **Hilbert space**. From this consideration, we can say that any state function $\Psi(r)$ in the Hilbert space can be written as a linear combination of the basis eigenfunctions as:

$$
\begin{align}
\tag{10}
\Psi(r)=\sum_n^{\infty} c_n \psi_n (r)
\end{align}
$$

Equation 10 is knowns as the *completeness relation*, and the $c_n$ are expansion coefficients. Since the eigenfunctions are orthonormal, we can obtain the value of any $c_m$ by taking the inner product of the basis function $\psi_m(r)$ with the total wavefunction in 10, and exploting the ortnornamility property (equation 8) to kill the sum:

$$
\begin{align}
\tag{11}
\int_D{\psi_m^* (r)\Psi(r)}dr&=\sum_n^{\infty} c_n \int_D{\psi_m(r)^*\psi_n (r)}dr=c_m\\
c_m&=\int_D{\psi_m^ * (r)\Psi(r)dr}
\end{align}
$$

The expansion coefficients are related to a physical fact.
Namely, their absolute square $|c_n|^2$ gives the propability of obtaining the eigenvalue $E_n$ associated to the eigenfunction $\psi_n(r)$ upon performing a measurement.

## The Solution to the Time-Dependent Schrödinger Equation for a Time-Independent Hamiltonian

The wavefunction in equation 10 is also part of our solution to the Schrödinger equation for a time-independent Hamiltonian. Indeed, due to the fact that the Schrödinger equation is a linear equation, if one of the eigenfunctions ($\psi_n(r)$) is solution to the time-independent equation, so is a linear combination of the eigenfunctions.
This observation is referred to as the **superposition principle**. 
Equation 10 is the more general state in which the quantum system could be (before measuring it). This fact is the reason why we do not a priori know which eigenvalue we will measure, but can only know the probability ($|c_n|^2$) of measuring the eigenvalue $E_n$, unless of course, the system was prepared in the $\psi_n(r)$ to begin with, then we know with certainty that a measurement will return $E_n$.

Now, to construct the time-dependent solution, we need to recall that we guessed the product $\phi(t)\psi(r)$ as a solution. All we need to do is to multiply each eigenfunction in equation 10 by the appropriate $\phi_n(t)$ where each $\phi_n(t)$ obtains the index because of the eigenvalues $E_n$. As such equation equation 7 becomes: $\phi_n(t) = e^{\frac{-iE_n}{\hbar}t}$. The solution to the time-dependent Schrödinger for the time-independent Hamiltonian is thus:

$$
\begin{align}
\tag{12}
\Psi(r,t)=\sum_n^{\infty} c_n e^{\frac{-iE_n}{\hbar}t}\psi_n (r)
\end{align}
$$

We have highlighted that this method of finding a general solution to the Schrödinger equation is for the particular case of a time-independent process, yet, from equation 12, we see that the wavefunction does have a time-dependence through $\phi_n(t)$. The key is that, the general solution to the Schrödinger equation is **not** time-independent, only the individual stationary states $\phi_n(t)\psi_n(r)$ are. One could ask how are the stationary states independent of time, if they possess the time-dependent complex phase $\phi(t)$? The reason is because the probability density of these states, as well as the [expectation values](ZPE.md) calculated from them do not vary in time.

Consider a system prepared in the following state $\Psi_n(r,t)=\phi_n(t)\psi_n(r)$, and we want to determine its probability density.

$$
\begin{align}
\tag{13}
\Psi_n(r,t)^* \Psi_n(r,t)&=\phi_n^* (t)\phi_n(t)\psi_n^* (r)\psi_n(r)\\
|\Psi_n(r,t)|^2&=|\psi_n^2(r)|=|\Psi_n(r)|^2
\end{align}
$$

where we have used the fact that $\phi_n^*(t)\phi_n(t)=e^{\frac{iE_n-iE_n}{\hbar}t}=1$, and the last equal sign is just to show that the time-dependence of the state drops when we take the absolute square of the wavefunction for that state.  
One way we could think about the wavefunction in equation 13 is like a vector rotating in Hilbert space as a function of time (because of $\phi(t)$ ), but its length does not change. As such the $\phi_n(t)$ functions act as [unitary operators](unitaryevol.md) that merely change the phase of the $\Psi_n(r,t)$ as a function of time.  

There are lots of problems in which we are only interested in determining the eigenstates (time-independent problems) of the system. For instance
quantum chemists do this all the time to determine the electronic structure of atoms and molecules. Indeed, the familiar orbitals of the hydrogen atom consists of solutions 
to eq.6 for the spherically symmetric Coulomb potential.

Time-dependent processes, where the potential term, $\hat{V}$, in the Hamiltonian is explicitely time-dependent are studied using various methods. As mentioned, it is possible sometimes to treat the time-dependent potential as an interaction that will perturb the system from one stationary state to another, and in some other cases, oter non-perturbative methods have to be used or developped. 
