# On the Zero-Point Energy of the Ground State of the Quantum Harmonic Oscillator
In the classical harmonic oscillator, we know that when the oscillator is at rest, that is it's momentum $p=0$, and 
it is at the equilibrium position $x=x_0$, its total energy is zero since its kitenic and potential energies are zero. This state corresponds
to the lowest energy state the oscillator can have. We know for the quantum mechanical oscillator, the lowest energy state, the ground state,
as an energy of $E=\frac{\hbar\omega}{2}$. It is informative to think through where this non-zero quantum of energy comes from. Does it come
from the potential energy, kinetic energy or both?
In order to carry on with the analysis, we will review a few definitions first and then try to understand the source of this energy.

## Review of Dirac Notation 
We will perform a quick overview of Dirac notation in this section to facilitate notation for what we want to achieve in this post. 
Let $\mathbf{v}$ be a vector with two complex components $a$ and $b$ and $\mathbf{v}^{\dagger}$ be its conjugate transpose in a $l^2$-normed vector space 
(one in which we can compute the lenght of the vectors using the Euclidean norm). In Dirac notation,
the vectors are written as:

$$
\begin{align}
\tag{1.1}
\mathbf{v}=
\begin{pmatrix}
a \\ 
b
\end{pmatrix}
= |v\rangle \\
\mathbf{v}^{\dagger}=
\begin{pmatrix}
a^ * b^ *
\end{pmatrix}
=\langle v|
\end{align}
$$

where $|v\rangle$ is called a *ket* and its conjugate transpose, $\langle v|$, is called a *bra*. If the vector space is equipped with an
inner product, we write the inner product between the two vector as: 

$$
\begin{align}
\tag{1.2}
\langle v|v\rangle = \left(a\cdot a^ *+b \cdot b^ * \right)= \left(a^2+b^2 \right)
\end{align}
$$


We observe that equation 1.2 also provides a way to calculate square of 
the norm (square modulus) of the vector $|v\rangle$.

Recall that operators are represented by matrices once a proper basis is defined, and they, in general, act on vectors to produce other vectors.
Let $\hat{O}$ be the matrix representation of an operator in our complex vector space. Let us have $\hat{O}$ act on $|v_1\rangle$ to produce a new vector $|v_2\rangle$.
We simply write

$$
\begin{align}\tag{1.3}
\hat{O}|v_1\rangle = |v_2\rangle
\end{align}
$$

Let $|e\rangle$ be an eigenvector of $\hat{O}$ with eigenvalue $e$. Let us also require that the norm of $|e\rangle$ be unity. We can write 
the eigenvalue equation:

$$
\begin{align}
\tag{1.4}
\hat{O}|e\rangle &= e|e\rangle \\  
&\text{and} \\
\langle e|\hat{O}|e\rangle &= e
\end{align}
$$

Lastly, from equation 1.1 we have that $\left(|v\rangle\right)^{\dagger} = \langle v|$. The Hermitian conjugate, $\hat{O}^{\dagger}$, of an operator $\hat{O}$ is defined such that: 

$$
\begin{align}
\tag{1.5}
\left(\hat{O}|v\rangle\right)^{\dagger} = \langle v|\hat{O}^{\dagger}
\end{align}
$$

Equation 1.5 tells us when $\hat{O}$ operates on *ket* $|v\rangle$, the complex conjugate of the answer we obtain is equal the result of the hermitian conjugate $\hat{O}^{\dagger}$ acting on the *bra* $\langle v|$. 
In particular, if $|v\rangle$ is an eigenvector of $\hat{O}$ with a **real** eigenvalue $\lambda$, then:

$$
\begin{align}
\tag{1.6}
\left(\hat{O}|v\rangle\right)^{\dagger} =\lambda^{*}=\lambda \\
\tag{1.7}
\langle v|\hat{O}^{\dagger}= \lambda^{ *}=\lambda\\
\therefore \hat{O}|v\rangle=\langle v|\hat{O}^{\dagger}
\end{align}
$$

## Calculating Expectaction Value of Operators and Variance
In quantum mechanics, physical observables are represented by Hermitian matrices. We can obtain the expectation value, the average we would obtain if we performed the experiment multiple times, of a given operator. Let $\hat{A}$ be an Hermitian matrix representing a given physical observable, and let the set $\psi_n(r)$ be normalized state functions of a given system.
The expectation value of $\hat{A}$ is given by:

$$
\begin{align}
\tag{2.1}
&\langle \hat{A}\rangle=\int_{all space}{\psi^*_n(r)\hat{A}\psi_n(r)}dr \\
&\text{in Dirac notation} \\
\tag{2.2}
&\langle \hat{A}\rangle=\langle \psi_n(r)|\hat{A}|\psi_n(r)\rangle
\end{align}
$$

In equation 2.1, I have written *all space* as the limit of integration because the physics of the problem will determine the specific limits of integration to be used. For example, in the case of the particle in the box, the limits of integration would be the boundaries of the box, while for the Harmonic Oscillator, the limits would be $\pm \infty$. Note, however, that in the case of the Dirac equation, the notation is the same regardless of the limits of integration. We only need to worry about them when we perform the actual calculation. We can make a similar observation for the normalization of the wavefunctions, that is: 

$$
\begin{align}
\tag{2.3}
\int_{all space}{\psi_m(r)\psi_n(r)}dr&=\delta_ {mn}, \quad
\text{with $\delta_{mn}=1$ for m=n or $\delta_{mn}=0$ otherwise}\\
&\text{in Dirac notation}\\
\tag{2.4}
\langle \psi_n(r)|\psi_n(r)\rangle&=\delta_ {mn}
\end{align}
$$

Since the experiment outcomes are expectaction values, we may want to determine the variance, $\sigma_\alpha^2$, associated with a given observable $\alpha$. The variance is given by: 

$$
\begin{align}
\tag{2.5}
\sigma_\alpha^2=\langle \alpha^2\rangle - \langle \alpha\rangle ^2
\end{align}
$$

In other words, the variance is the difference between the expectation value of the square of the observable and the square of the expectation value.

## Determining the Variance in Position and Momentum for the Ground State of the Harmonic Oscillator
What we want to do now is to determine the average position and momentum when the oscillator is in the ground state $\psi_0(x)$. In order to do this we will calculate the expectation values of the position and momentum operator using equation 2.1. We will, however, express the position and momentum operators using the creation and annihilation operators we defined [previously](algebraicQHO.md). Rewriting the operators in this way and using Dirac notation will allow us to calculate these expectation values much faster without having to explicitly compute the integrals.

### Position and Momentum Operators in Terms of Creation and Annihilation Operators
We recall that the creation $\hat{a}^{\dagger}$ and annihilation $\hat{a}$ operators are defined as:

$$
\begin{align}
\tag{3.1}
\hat{a}^{\dagger}=\frac{1}{\sqrt{2\hbar m\omega}}\left(m\omega x- i\hat{p}\right)\\
\tag{3.2}
\hat{a}=\frac{1}{\sqrt{2\hbar m\omega}}\left(m\omega x+ i\hat{p}\right)
\end{align}
$$

From 3.1 and 3.2 we can express the position and momentum operators as: 

$$
\begin{align}
\tag{3.3}
\hat{x}=\frac{\hbar}{\sqrt{2\hbar m\omega}}\left(\hat{a}+\hat{a^{\dagger}}\right)\\
\tag{3.4}
\hat{p}=\frac{-i\hbar m\omega}{\sqrt{2\hbar m\omega}}\left(\hat{a}-\hat{a^{\dagger}}\right)
\end{align}
$$

For simplicity, we can look at the special case where $\hbar=m=\omega=1$. Looking at this makes our manipulations simpler, but
is not a problem because we know the results we will get at the end will be constant multiples of the coefficients we have in 3.3 and 3.4 for the position and momentum respectively. When we use this simplification, we can rewrite 3.3 and 3.4 as:

$$
\begin{align}
\tag{3.5}
\hat{x}=\frac{1}{\sqrt{2}}\left(\hat{a}+\hat{a^{\dagger}}\right)\\
\tag{3.6}
\hat{p}=\frac{-i}{\sqrt{2}}\left(\hat{a}-\hat{a^{\dagger}}\right)
\end{align}
$$

## Calculating the Expectaction Values in Position and Momentum
The expectation value, $\langle \hat{x}\rangle$, of position in the ground state of the Harmonic Oscillator in Dirac notation is given by: 

$$
\begin{align}
\tag{3.7}
\langle \hat{x}\rangle=\frac{1}{\sqrt{2}}\langle \psi_0|\hat{a}+\hat{a}^{\dagger}|\psi_0\rangle
\end{align}
$$

