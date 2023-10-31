# On the Zero-Point Energy of the Ground State of the Quantum Harmonic Oscillator
In the classical harmonic oscillator, we know that when the oscillator is at rest, that is it's momentum $p=0$, and 
it is at the equilibrium position $x=x_0$, its total energy is zero since its kitenic and potential energies are zero. This state corresponds
to the lowest energy state the oscillator can have. We know for the quantum mechanical oscillator, the lowest energy state, the ground state,
as an energy of $E=\frac{\hbar\omega}{2}$. It is informative to think through where this non-zero quantum of energy comes from. Does it come
from the potential energy, kinetic energy or both?
In order to carry on with the analysis, we will review a few definitions first and then try to understand the source of this energy.

## Review of Dirac Notation 
We will perform a quick overview of Dirac notation in this section to facilitate notation for what we want to achieve in this post. 
Let $\mathbf{v}$ be a vector with two complex components $a$ and $b$ and $\mathbf{v}^{*}$ be its conjugate transpose in a $l^2$-normed vector space 
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
\mathbf{v}^{*}=
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

Recall that operators a represented by matrices once a proper basis is defined, and they, in general, act on vectors to produce other vectors.
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


