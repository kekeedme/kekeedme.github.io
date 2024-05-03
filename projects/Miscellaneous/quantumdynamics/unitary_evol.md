# A Brief Discussion on Unitary Evolution

I want to start with a brief discussion on unitary operation and evolution. I will then make the connection with the discussion of
the two-level system dynamics 
that we have seen. In particular, how one can phenomenologically simulate the decay of the dynamics by modifying the evolution operator, thereby putting an end to the oscillatory 
behavior of the system.

## Unitary Transformation


Within a given vector space, a unitary operation is an operation that preserves the inner product between vectors 
in that space. For instance, consider a vector $|v_1\rangle$
in a complex vector space, equipped with an inner product. The inner product within this space 
is defined as:

$$
\begin{align}
\tag{1}
\langle v_1|v_1\rangle
\end{align}
$$

where, $\langle v_1| = |v_1\rangle^\*$, with $|v_1\rangle^\*$ being the conjugate transpose of the vector $|v_1\rangle$.
Let $\hat{U}$ be an operator that acts on the vectors of our vector space. 
When we define basis vectors for our space, $\hat{U}$ is represented by a matrix.
It acts on the vectors under matrix multiplication:

$$
\begin{align}
\tag{2}
\hat{U}|v_1\rangle = |v_2\rangle
\end{align}
$$

The operator can also act on the complex conjugate of the vectors in the space. In order to do this, 
we need to take the conjugate transpose of the matrix that represents it. As a result we get:

$$
\begin{align}
\tag{3}
\langle v_1|\hat{U}^{\dagger}=\langle v_2|
\end{align}
$$

Stating that $\hat{U}$ preserves the inner product when it operates on vectors in the space means:

$$
\begin{align}
\tag{4}
\langle v_1|v_1\rangle&=\langle v_2|v_2\rangle\\
\langle v_1|v_1\rangle&=\langle v_1|\hat{U}^{\dagger}\hat{U}|v_1\rangle
\end{align}
$$

Equation 4 tell us that $\hat{U}^{\dagger}\hat{U}=\mathbf{1}$, where $\mathbf{1}$ is the identity matrix.
From this consideration, 
we learn that the conjugate transpose, $\hat{U}^{\dagger}=\hat{U}^{-1}$.
Matrices defined on real vector spaces (where the vectors are defined over the field of real numbers, hence the matrix entries are real numbers) 
with the same properties as $\hat{U}$ are
called orthogonal matrices, and are denoted $\mathbf{O}$. I have made a more detailed posts on orthogonal matrices
on the math section of [this document](Quantum_dynamics_two_levelsystem.pdf).

## Unitary Evolution

The wavefunction in the Schrodinger equation is a complex quantity. The equation itself is linear. 
The wavefunction can be viewed as a complex vector defined on a complex vector space equipped with an inner product (which gives us
the norm of the wavefunction i.e the probability density associated with the wavefunction). 
In addition, the wavefunction is a time-evolving quantity. Suppose the wavefunction,$|\Psi(r,t)\rangle$, 
has a given norm at $t=0$ on the entire
subspace over which it is defined. Then it must retain the same norm at a later time $t$.(I have a demonstration of this [here](../slides/Prob_densisty_current_momentum.pdf))
We can define an operator, $\hat{U}(t,t_0)$, which acts on the wavefunction at $t_0$, and returns the wavefunction at a later time $t$:

$$
\begin{align}
\tag{5}
|\Psi(r,t)\rangle=\hat{U}(t,t_0)|\Psi(r,t_0)\rangle
\end{align}
$$

### Properties of the Evolution Operator: 

#### Unitarity 

It preserves the norm of the wavefunction, and thus:

$$
\begin{align}
\tag{6}
\langle\Psi(r,t)|\Psi(r,t)\rangle= \langle\Psi(r,t_0)|\hat{U}^{\dagger}(t,t_o)  \hat{U}(t,t_0)|\Psi(r,t_0)\rangle=1
\end{align}
$$

Where we again observe the property that $\hat{U}(t,t_0)^{\dagger}\hat{U}(t,t_0)=\mathbf{1}$.

#### Continuity

$$
\begin{align}
\tag{7}
|\Psi(r,t)\rangle=\hat{U}(t,t)|\Psi(r,t)\rangle
\end{align}
$$

The operator acting on the wavefunction at a time $t$, when it is already at time $t$, gives the wavefunction back again. 
As such, the evolution operator acts as the identity operator: $\hat{U}(t,t)=\mathbf{1}$.

#### Composition 

$$
\begin{align}
\tag{8}
|\Psi(r,t_2)\rangle=\hat{U}(t_2,t_0)|\Psi(r,t_0)\rangle
\end{align}
$$

or 

$$
\begin{align}
\tag{8}
|\Psi(r,t_2)\rangle=\hat{U}(t_2,t_1) \hat{U}(t_1,t_0)|\Psi(r,t_0)\rangle
\end{align}
$$

Hence, we have $\hat{U}(t_2,t_0)=\hat{U}(t_2,t_1) \hat{U}(t_1,t_0)$.

We can obtain an expression for the evolution operator, by using the time-dependent Schrodinger equation (TDSE).
In order to do so, we will insert equation 5 into the TDSE:

$$
\begin{align}
\tag{9}
i\hbar\frac{\partial|\Psi(r,t)\rangle}{\partial t}&=\hat{H}(r,t)|\Psi(r,t)\rangle \\
\tag{10}
i\hbar\frac{\partial\hat{U}(t)}{\partial t}|\Psi(r,t_0)\rangle&=\hat{H}(r,t)\hat{U}(t)|\Psi(r,t_0)\rangle \\
\tag{11}
i\hbar\frac{\partial\hat{U}(t)}{\partial t}&=\hat{H}(r,t)\hat{U}(t)
\end{align}
$$

Equation 11 is a first-order differential equation in $\hat{U}(t)$, hence, the solution is: 

$$
\begin{align}
\tag{12}
\hat{U}(t)=\exp\left(\frac{-i}{\hbar}\int_0^t \hat{H}(r,t') ~dt'\right)
\end{align}
$$

The expression obtained in equation 12 is not always valid. I invite you to read my friend Dr. Joshua Going's post on the [Magnus expansion](https://joshuagoings.com/2017/06/15/magnus/) to read about the general treatment of such differential equations involving matrices.
We can look at the particular case where, the Hamiltonian is not dependent on time.
If $\hat{H}(r,t)$ is time independent, it can be taken out of the integral, and the integral evaluates to $t$.
Hence for a time-independent Hamiltonian, the unitary evolution operator is:

$$
\begin{align}
\tag{13}
\hat{U}(t)=\exp\left(\frac{-i}{\hbar}\hat{H}t\right)
\end{align}
$$

The expression obtained in equation 13 is the same as the exponential factor we obtained in the expression for the time-dependent coefficients
in the equation 1.12 [here](/twolevel.md). As a result, in our [two-level](/twolevel.md) system, 
the evolution operator was evolving our total wavefunction in time, by acting on the time-dependent coefficients. 
This observation is consistent with the system we studied. Recall that we were simulating the dynamics between two stationary states. That is, 
states $|\phi_1\rangle$ and $|\phi_2\rangle$ were not changing with time. What was time-dependent, was their relative weight (i.e their coefficients)
to the total wavefunction of the system. As such, the evolution operator dictated how the occupation of the states $|\phi_1\rangle$ and $|\phi_2\rangle$ changed with time.
We can thus use it to obtain an expression for the state $|\Psi(r,t)\rangle$ at all times from the initial state $|\Psi_0(r,t_0)\rangle$.

## The Link Between The Unitary Evolution and Ending the Oscillatory Dynamics

As we have seen in the [two-level](/twolevel.md) dynamics, 
the probability of finding the system in stationary states $|\phi_1\rangle$ or $|\phi_2\rangle$ oscillates indefinitely with time. 
One way to end the oscillation is through the presence of an energy dissipation mechanism.  

Imagine every time the system transitions to
 state $|\phi_2\rangle$ it loses energy. We can simulate this by making the evolution operator non-unitary. As a result, the norm of the total 
 wavefunction will not be preserved. We can make it so the norm decreases with time, which would phenomenologically (without specifying the exact physical cause of the energy dissipation) simulate a decay in the dynamics of the two-level system, ending the oscillation. This method is what the orginal authors, 
 professors [Beratan](https://beratanlab.chem.duke.edu/) and [Polizzi](https://www.polizzilab.org/) showed in the [mathematica](https://pubs.acs.org/doi/10.1021/acs.jchemed.5b00662) notebook.    
 Recall from equations 12 and 13 that $\hat{U}(t)$ depends on $\hat{H}(r,t)$. The Hamiltonian, $\hat{H}(r,t)$,
 is represented by a hermitian matrix, meaning that it is a square matrix equal to its own conjugate transpose $\left(\hat{H}=\hat{H}^{\dagger}\right)$.  
 In fact, every unitary matrix can be written as complex exponential of a hermitian matrix, that is: $\hat{U}=\exp{i\hat{H}}$, where $\hat{H}$ is a hermitian matrix.
 If we make the Hamiltonian non-hermitian, then $\hat{U}(t)$ will lose its unitary property. Indeed, by introducing a dissipation factor $-i\Gamma$,
 in the expression for the Hamiltonian in our two-level system, we can phenomenologically simulate the end of the oscillations (the $i$ makes the Hamiltonian non-hermitian).  
 
 In the python code, 
 I introduced this term, following the example of the authors, on the diagonal of the Hamiltonian matrix as $E_2-i\Gamma$, to show that the system loses some energy (proportional to $\Gamma$) every time it reaches state $|\phi_2\rangle$. The dissipation term, can of course be simulating energy loss from state $|\phi_1\rangle$ instead.
 The below figure shows a representative example where the system starts in state $|\phi_2\rangle$. I encourage you to play with the simulation, either using
 [my python](https://github.com/kekeedme/qdwtd/blob/main/two_levelsystem_withending.py) code or in the original [mathematica notebook](https://pubs.acs.org/doi/10.1021/acs.jchemed.5b00662).
 
 <figure>
    <img src="/projects/quantumdynamics/images/dynamics_dissipation.png" alt="figure">
    <figcaption>Figure 1. Oscillation of the probability of measuring the system in state 1 (blue) or 2 (orange) as a function of time  </figcaption>
</figure>   
