# Expectation Values and Hermitian Operators

When we introduced the [Schrodinger equation](SchrodingerEQ.md) we saw that, when the system was prepared in the superposition of states, i.e $\Psi(r,t)$,
the expansion coefficients $c_n$ were related to the probability of measuring a particular 
eigenvalue (in this case the energy of the stationary state $\psi_n$) that we denoted $E_n$. Therefore, every time we prepare a system in
state $\Psi(r,t)$, we can only predict the probability of measuring a certain energy $E_n$, by calculating $|c_n|^2$.   
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

As a result, the diagonal entries of a hermitian matrix are **real** and the off-diagonal entries are **complex conjugate** of one another.

## Calculating Expectation Value
Given a wavefunction $\Psi(r,t)$ describing the state of a system, and the operator $\hat{A}$ describing a physical observable of interest, 
the expectation value, $\langle \hat{A}\rangle$, of the observable is given by:

$$
\begin{align}
\tag{5}
\langle \hat{A}\rangle=\frac{\int_{D}{\Psi^ *(r,t)\hat{A}\Psi(r,t) dr}}{\int_{D}{\Psi^ * (r,t)\Psi(r,t) dr}}
\end{align}
$$

where the denominator equation 5 is the normalization condition, therefore, if $\Psi(r,t)$ is already normalized then the denominator is $1$.  
We can take the example of
the wavefunction prepared in the normalized state $\Psi_n(r,t)=\phi_n(t)\psi_n(r)$ (thus $c_n=1$ ),  and we wish to find the expectation value of the energy. Using equation 5, we obtain:

$$
\begin{align}
\tag{6}
\langle \hat{H}\rangle&=\int_{D}{\phi_n ^ * (t)\psi_n ^ * (r) \hat{H}\phi_n(t)\psi_n(r) dr}\\
\tag{6.1}
\langle \hat{H}\rangle&=E_n\int_{D}{\phi_n ^ * (t)\psi_n ^ * (r)\phi_n(t)\psi_n(r) dr}\\
\tag{6.2}
\langle \hat{H}\rangle&=E_n\int_{D}{\psi_n ^ * (r)\psi_n(r) dr}\\
\tag{6.3}
\langle \hat{H}\rangle&=E_n
\end{align}
$$

In equation 6.1 we evaluated the hamiltonian on its eigenstate $\psi_n$ to obtain the energy $E_n$. Then we took advantage in 6.2 of the fact that $\phi_n^ *(t)\phi_n=1$, as we have [seen](SchrodingerEQ.md). Finally we used of the fact that the eigenstates are normalized, which means that the integral also evalulates to $1$.  
The result we obtain tells us (i) that if the system is prepared in the state $\psi_n$ then we are sure to measure energy $E_n$ and (ii) that the energy of stationary states are constant as we lose the time-dependence of the total wavefunction when we multiplied by the complex conjugate. To reiterate, if the system was in a superposition of states, we would only be able to report on the probability ( $|c_n|^2$ of measuring a particular $E_n$, since when in the superposition, the system does not have a definite energy. The average will would obtain upon performing multiple measurements would be the weighed average of the stationary state energies, weighed by the coefficients.

## Variance
Since the experiment outcomes are expectaction values, we may want to determine the variance, $\sigma_\alpha^2$, associated with a given observable $\alpha$. The variance is given by: 

$$
\begin{align}
\tag{7}
\sigma_\alpha^2=\langle \alpha^2\rangle - \langle \alpha\rangle ^2
\end{align}
$$

In other words, the variance is the difference between the expectation value of the square of the observable and the square of the expectation value.

For the case where the system is in the state $\Psi_n(r,t)=\phi_n(t)\psi_n(r)$, we can determine the variance in energy by determining the expectation value of the square of the energy $\langle \hat{H}^2\rangle$ and then the square of the expectation value $E_n^2$.
We obtain:

$$
\begin{align}
\tag{8}
\sigma_\hat{H}^2&=\langle \hat{H}^2\rangle - \langle \hat{H}\rangle ^2\\
\tag{8.1}
\sigma_\hat{H}^2&=\int_{D}{\psi_n ^ * (r) \hat{H^2}\psi_n(r) dr}-E_n^2\\
\tag{8.2}
\sigma_\hat{H}^2&=E_n\int_{D}{\psi_n ^ * (r) \hat{H}\psi_n(r) dr}-E_n^2\\
\tag{8.3}
\sigma_\hat{H}^2&=E_n^2\int_{D}{\psi_n ^ * (r)\psi_n(r) dr}-E_n^2\\
\tag{8.4}
\sigma_\hat{H}^2&=E_n^2-E_n^2=0
\end{align}
$$

where from 8 to 8.1 we have again used the fact that $\phi_n^ *(t)\phi_n=1$. From 8.2 to 8.3, we exploit that $\hat{H^2}$ consists of applying the operator $\hat{H}$ twice. Secondly, we used the fact that the $\psi_n$ are normalized functions in going to 8.4.  
As expected, since we prepared the system in state $\Psi_n(r,t)=\phi_n(t)\psi_n(r)$, we should obtain the energy $E_n$ with certainty. Thus, there should not be any spread in the measured in energy value for this initial condition.  

Calculating the spread in the expectation value of observables can teach us a lot about quantum systems, and quantum mechanics in itself. For instance, we can see in the case of an harmonic oscillator there is a an uncertainty in both the position and the momentum of the oscillator even in its lowest energy state. The consequence is that the lowest energy state cannot be zero, since the system is always fluctuating. This fact is strongly related to the dispersion principle of Heinsenberg. I disuss this in more details [on this post](QuantumHOscillator.md)
