# Expectation Values and Hermitian Operators

When we introduced the [Schrodinger equation](SchrodingerEQ.md) we saw that, when the system was prepared in the superposition of states, i.e $\Psi(r,t)$,
the expansion coefficients $c_n$ were related to the probability of measuring a particular 
eigenvalue (in this case the energy of the stationary state $\psi_n$) that we denoted $E_n$. Therefore, every time we prepare a system in
state $\Psi(r,t)$, we can only predict the probability of measuring a certain energy $E_n$.  
Let us consider that we performed a measurement on $\Psi(r,t)$, and
measured the energy $E_n$. If we perform a subsequent measurement on the same system, we will again measure $E_n$. This observation
tells us that the first measurement "*collapsed*" the initial superposition of states to a definite state $\psi_n$, 
and we are sure to measure its energy on a subsequent
measurement.  

If, however, we identically prepare multiple systems in the same superposition of states $\Psi(r,t)$, when we perform the energy measurement
on each of these replica, we will obtain a spread in energy values ( $E_ns$ weighed by their probability $|c_n|^2$). Hence, the best we can 
do is to report the *average* or *expectation* value that we obtained from the measurements.  

## Hermitian Operators
We have seen in the [Schrodinger equation](SchrodingerEQ.md) 
that the observable of energy was represented by the Hamiltonian operator $\hat{H}$. In fact, in quantum mechanics, all physical observables
are represented by linear operators. When these operators act on the wavefunction describing the state of the system, we are able to calculate the
expectation value of this particular observable. Recall, however that wavefunctions are complex quantities, and the operators can also be complex
but the result of physical
measurements are real numbers. Hence, this requires that the operators representing physical observables to be *hermitian*. The reason is because
the eigenvalue of hermitian operators are real.

A hermitian operator is equal to its conjugate transpose. For instance, let $\hat{A}$ be an operator, and $\hat{A}^{\dagger}$ its conjugate
transpose, then for $\hat{A}$ to be hermitian, means:

$$
\begin{align}
\tag{1}
\hat{A}=\hat{A}^{\dagger}
\end{align}
$$

Furthermore, let $a$ be the eigenvalue of the operator $\hat{A}$ with eigenfunction $\psi$, $a^ *$ that of $\hat{A}^{\dagger}$ 
and let $\psi^ *$ be the complex conjugate of $\psi$. This implies:

$$
\begin{align}
\tag{2}
\hat{A}\psi&=a\psi\\
\hat{A}^{\dagger}\psi^ *&=a^ *\psi^ * = a\psi^ *
\end{align}
$$

### Hermitian Operators as Matrices
The linear operators can often be represented as square matrices once a suitable basis is chosen. Let us consider a general square matrix 
representing operator $\hat{A}$ and its conjugate tranpose:

$$
\begin{align}
\tag{3}
\hat{A}&=\begin{pmatrix} a & b\\\
c & d
\end{pmatrix}\\
\hat{A}^{\dagger}&=\begin{pmatrix} a^ * & c^ *\\\
b^ * & d^ *
\end{pmatrix}
\end{align}
$$

If $\hat{A}$ is hermitian, then it is equal to $\hat{A}^{\dagger}$, which means that the matrix entries must be such that $a = a^ *$, 
$d=d^ *$ and $c^ * =b$ and $b^ * =c$. 
Therfore, for a hermitian matrix $\hat{A}$, we get:

$$
\begin{align}
\tag{4}
\hat{A}&=\begin{pmatrix} a & b\\\
c & d
\end{pmatrix}\\
\hat{A}^{\dagger}&=\begin{pmatrix} a & b\\\
b^ * & d
\end{pmatrix}
\end{align}
$$
