# Algebraic Method for the Quantum Mechanical Harmonic Oscillator
In this section, we will use an algebraic method to obtain the quantum mechanical harmonic oscillator eigenstates and energies. In doing so, we will define the so-called ladder (or in some context, creation and annihilation) operators. These operators have a nice property: namely, by operating on one harmonic oscillator eigenstate, they can generate another. Obtaining the ladder operators can be considered as an interesting result in itself, because understanding how they work on one quantum state to generate another, we begin to get a small glimpse at the "mechanics" of a different formalism of quantum mechanics called second quantization. Second quantization is beyond the scope of this post, but, if you learn it, you will see that similarly to how the ladder operators allow us to obtain one quantum state from anoter, so do creating and anhilation operators in second quantization.  
In the following, we will present the 1-dimensional time-independent Schrödinger equation (TISE) for a harmonic oscillator. We will see how we can attempt to factor the Hamiltonian and from there, define the ladder operators and use them to obtain the eingstate and energies we seek.

## The Harmonic Oscillator Hamiltonian and the Schrödinger Equation 
The Hamiltonian, $\hat{H}$, of the system is defined as the sum of the kinetic energy of the particle undergoing oscillatory motion and its potential energy. For a particle of mass $m$ under the harmonic potential, $V(x)=\frac{1}{2}kx^2$, the Hamiltonian reads: 

$$
\begin{align}
\tag{1}
\hat{H} &= \frac{-\hbar^2}{2m}\frac{d^2}{dx^2}+\frac{1}{2}k\hat{x}^2\\
&=\frac{-\hbar^2}{2m}\frac{d^2}{dx^2}+\frac{m\omega^2\hat{x}^2}{2}
\end{align}
$$

where we have used our result from [before](QuantumHOscillator.md), namely that $\omega=\sqrt{\frac{k}{m}}$. We can now write the TISE, $\hat{H}\psi(x)=E\psi(x)$, using the Hamiltonian as:

$$
\begin{align}
\tag{2}
\frac{-\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}+\frac{m\omega^2\hat{x}^2}{2}\psi(x)=E\psi(x)
\end{align}
$$

We need to recall that in 1-D the momentum operator is $\hat{p}=\frac{\hbar}{i}\frac{d}{dx}$, and the position operator $\hat{x}=x$. We can rewrite the Hamiltonian as $\hat{H}=\frac{\hat{p}^2}{2m}+\hat{V}$. Doing so allows us to rewrite the Schrödinger equation as:

$$
\begin{align}
\tag{3}
\frac{1}{2m}\left(\hat{p}^2+\left(m\omega x\right)^2\right)\psi(x)=E\psi(x)
\end{align}
$$

We now see that the Hamiltonian is of the form $a^2+b^2$ up to a constant factor. We can factor the sum of the squares as $\left(a+ib\right)\left(a-ib\right)$. This observation suggest that we should attempt to factor the Hamiltonian using these two factors:

$$
\begin{align}
\tag{4}
\hat{a}^{\dagger}=\frac{1}{\sqrt{2\hbar m\omega}}\left(m\omega x- i\hat{p}\right)\\
\hat{a}=\frac{1}{\sqrt{2\hbar m\omega}}\left(m\omega x+ i\hat{p}\right)
\end{align}
$$

The $\frac{1}{\sqrt{2}}$ factor is a result of factoring the $\frac{1}{2}$ of the Hamiltonian. The additional $\sqrt{m\omega\hbar}$ in the denominator help make the quantities $\hat{a}^{\dagger}$ and $\hat{a}$ dimensionless, and will greatly simply the expressions we will obtain later.  
Notice that the operators $\hat{a}^{\dagger}$ and $\hat{a}$ are i) complex conjugate of one another, ii) are dimensionless iii) and are formed from operators which represent physical observables, (position and momentum), but do not represent physical observables themselves. They are referred to as ladder operators. Importantly, they do not [commute](commutationQM) with one another. Indeed:

$$
\begin{align}
\tag{4.1}
\left[\hat{a},\hat{a}^{\dagger}\right] = 1
\end{align}
$$

Since our aim was to factor the Hamiltonian, we should explore the product of $\hat{a}$ and $\hat{a}^{\dagger}$:

$$
\begin{align}
\tag{5}
\hat{a}\hat{a}^{\dagger} &= \frac{1}{2m\omega\hbar} \left(m\omega x+i\hat{p}\right) \left(m\omega x-i\hat{p}\right)\\
&=\frac{1}{2m\omega\hbar} \left[\hat{p}^2+\left(m\omega x\right)^2-im\omega \left(x\hat{p}-\hat{p}x\right)\right]
\end{align}
$$

Notice that $\left(x\hat{p}-\hat{p}x\right)$ is the [commutator](commutationQM.md) between the position and momentum operator, and recall that the commutator is $\left[\hat{x},\hat{p}\right]=i\hbar$. We rewrite our product as: 

$$
\begin{align}
\tag{5.1}
\hat{a}\hat{a}^{\dagger}&=\frac{1}{2m\omega\hbar} \left[\hat{p}^2+\left(m\omega x\right)^2-im\omega \left[\hat{x},\hat{p}\right]\right]\\
&=\frac{1}{2m\omega\hbar} \left[\hat{p}^2+\left(m\omega x\right)^2+\right]\frac{1}{2}
\end{align}
$$

We thus see that the product $\hat{a}\hat{a}^{\dagger}=\frac{1}{\hbar\omega}\hat{H}+\frac{1}{2}$. We could have easily explored the product $\hat{a}\hat{a}^{\dagger}$, and we would have obtained $\hat{a}\hat{a}^{\dagger}=\frac{1}{\hbar\omega}\hat{H}-\frac{1}{2}$. This observation allows us to rewrite the Hamiltonian as: 

$$
\begin{align}
\tag{6}
\hat{H}&=\hbar\omega\left(\hat{a}\hat{a}^{\dagger}-\frac{1}{2}\right) \\ 
&\text{or}\\
\tag{6.1}
\hat{H}&=\hbar\omega\left(\hat{a}^{\dagger}\hat{a}+\frac{1}{2}\right)
\end{align}
$$

We have obtain the Hamiltonian in terms of the ladder operators, but we may wonder about the benefits of having done so. However, before doing so, I would like to take small detour. If you wish to continue on with solving the problem, do skip this next section, and [continue](#obtaining-the-energies)

## Number Operator
We know, from the [series method](seriesQHO.md) post that the allowed energies of the harmonic oscillator are given by the expression:

$$
\begin{align}
\tag{A}
E_n=\hbar\omega\left(n+\frac{1}{2}\right)
\end{align}
$$

If we compare this expression with what we have obtained for the Hamiltonian in equation 6.1, we can draw an intereting parallel. Indeed, we know that the energies are eigenvalues of the Hamiltonian, and are given by a number $n=0,1,2...$ plus $\frac{1}{2}$. In addition, we have managed to write the Hamiltonian as a sum of an operator, the produt $\hat{a}^{\dagger}\hat{a}$, plus $\frac{1}{2}$. Therefore, we see that the integers $n$ are eigenvalues of the operator $\hat{a}^{\dagger}\hat{a}$. We can thus define $\hat{a}^{\dagger}\hat{a}=\hat{N}$, we call it the number operator. This observation is interesting because we recall that $n$ keeps track of the oscillator state or mode $\left(\psi_n(x)\right)$ we are in, and allows to calculate the energy of this mode using expression A. As a result, we can label each state or mode with the eigenvalues of $\hat{N}$. If we use Dirac notation, $|\psi_0(x)\rangle$, $|\psi_1(x)\rangle$... $|\psi_n(x)\rangle=$  $|0\rangle$, $|1\rangle$... $|n\rangle$.

## Obtaining the Energies
Let us rewrite the Schrödinger equation in terms of the ladder operators, in addition, let us consider that the $\psi(x)$ are already eingenstates of the Hamiltonian:
