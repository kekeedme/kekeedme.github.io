# A Brief Discussion on Unitary Evolution

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
Matrices defined on real vector spaces (where the vectors are defined over the field of real numbers) 
with the same properties  are
called orthogonal matrices, and are denoted $\mathbf{O}$. I have made a more detailed posts on orthogonal matrices
on the math section of [this document](/projects/quantumdynamics/Quantum_dynamics_two_levelsystem.pdf)

## Unitary Evolution

The wavefunction in the Schrodinger equation is a complex quantity. The equation itself is linear. 
The wavefunction can be viewed as a complex vector defined on a complex vector space equipped with an inner product (which gives us
the norm of the wavefunction i.e the probability density associated with the wavefunction). 
In addition, the wavefunction is a time-evolving quantity. Suppose the wavefunction,$|\Psi(r,t)\rangle$, 
has a given norm at $t=0$ on the entire
subspace over which it is defined. Then it must retain the same norm at a later time $t$.(I have a demonstration of this [here](../Miscellaneous/slides/Prob_densisty_current_momentum.pdf))
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
i\hbar\frac{\partial|\Psi(r,t)\rangle}{\partial t}&=H(r,t)|\Psi(r,t)\rangle \\
\tag{10}
i\hbar\frac{\partial\hat{U}(t)}{\partial t}|\Psi(r,t=0)\rangle&=H(r,t)\hat{U}(t)|\Psi(r,t=0)\rangle \\
\tag{11}
i\hbar\frac{\partial\hat{U}(t)}{\partial t}&=H(r,t)\hat{U}(t)
\end{align}
$$

Equation 11 is a first-order differential equation in $\hat{U}(t)$, hence, the solution is: 

$$
\begin{align}
\tag{12}
\hat{U}(t)=\exp\left(\frac{-i}{\hbar}\int_0^t H(r,t') ~dt'\right)
\end{align}
$$

If $H(r,t)$ is time independent, it can be taken out of the integral, and the integral evaluates to $t$.
Hence for a time-independent Hamiltonian, the unitary evolution operator is:

$$
\begin{align}
\tag{13}
\hat{U}(t)=\exp\left(\frac{-i}{\hbar}Ht\right)
\end{align}
$$

The expression obtained in equation 13 is the same we obtained for the time-dependent coefficients
in the equation 1.12 [here](/twolevel.md).
We can thus use it to obtain an expression for the state $|\Psi(r,t)\rangle$ at all times from the initial state $|\Psi_0(r,t_0)\rangle$

