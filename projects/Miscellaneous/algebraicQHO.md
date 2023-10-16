# Algebraic Method for the Quantum Mechanical Harmonic Oscillator
In this section, we will use an algebraic method to obtain the quantum mechanical harmonic oscillator eigenstates and energies. In doing so, we will define the so-called ladder operators. These operators have a nice property: namely, by operating on one harmonic oscillator eigenstate, they can generate another. Obtaining the ladder operators can be considered as a result in itself, because understanding how they work on one quantum state to generate another, we begin to get a small glimpse at the "mechanics" of a different formalism of quantum mechanics called second quantization. Second quantization is beyond the scope of this post, but, if you learn it, you will see that similarly to how the ladder operators allow us to obtain one quantum state from anoter, so do creating and anhilation operators in second quantization.  
In the following, we will present the 1-dimensional time-independent Schrödinger equation (TISE) for a harmonic oscillator. We will see how we can attempt to factor the Hamiltonian and from there, define the ladder operators and use them to obtain the eingstate and energies we seek.

## The Harmonic Oscillator Hamiltonian and the Schrödinger Equation 
The Hamiltonian, $\hat{H}$, of the system is defined as the sum of the kinetic energy of the particle undergoing oscillatory motion and its potential energy. For a particle of mass $m$ under the harmonic potential, $V(x)=\frac{1}{2}kx^2$, the Hamiltonian reads: 

$$
\begin{align}
\tag{1}
\hat{H} &= \frac{-\hbar^2}{2m}\frac{d^2}{dx^2}+\frac{1}{2}kx^2\\
&=\frac{-\hbar^2}{2m}\frac{d^2}{dx^2}+\frac{m\omega^2x^2}{2}
\end{align}
$$

where we have used our result from [before](QuantumHOscillator.md), namely that $\omega=\sqrt{\frac{k}{m}}$. We can now write the TISE, $\hat{H}\psi(x)=E\psi(x)$, using the Hamiltonian as:

$$
\begin{align}
\tag{2}
\frac{-\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}+\frac{m\omega^2x^2}{2}\psi(x)=E\psi(x)
\end{align}
$$

We need to recall that the momentum operator is $\hat{p}=\frac{\hbar}{i}\frac{d}{dx}$. In addition, much like it is done in classical mechanics, we can rewrite the Hamiltonian as $\hat{H}=\frac{\hat{p}^2}{2m}+\hat{V}$. Doing so allows us to rewrite the Schrödinger equation as:

$$
\begin{align}
\tag{3}
\frac{1}{2m}\left(\hat{p}^2+\left(m\omega x\right)^2\right)\psi(x)=E\psi(x)
\end{align}
$$

We now see that the Hamiltonian is of the form $a^2+b^2$ up to a constant factor. We can factor the sum of the squares as $\left(a+ib\right)\left(a-ib\right)$. This observation suggest that we could factor the Hamiltonian as:

$$
\begin{align}
\tag{4}
a_{\pm}=\frac{1}{\sqrt{2\hbar m\omega}}\left(m\omega x\mp ip\right)
\end{align}
$$
