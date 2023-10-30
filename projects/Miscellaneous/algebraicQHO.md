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

We need to recall that in 1-D the momentum operator is $\hat{p}=\frac{\hbar}{i}\frac{d}{dx}$, and the position operator $\hat{x}=x$. We can rewrite the Hamiltonian as $\hat{H}=\frac{\hat{p}^2}{2m}+\hat{V}(x)$. Doing so allows us to rewrite the Schrödinger equation as:

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

We thus see that the product $\hat{a}\hat{a}^{\dagger}=\frac{1}{\hbar\omega}\hat{H}+\frac{1}{2}$. We could have also explored the product $\hat{a}\hat{a}^{\dagger}$, and we would have obtained $\hat{a}\hat{a}^{\dagger}=\frac{1}{\hbar\omega}\hat{H}-\frac{1}{2}$. This observation allows us to rewrite the Hamiltonian as: 

$$
\begin{align}
\tag{6}
\hat{H}&=\hbar\omega\left(\hat{a}\hat{a}^{\dagger}-\frac{1}{2}\right) \\ 
&\text{or}\\
\tag{6.1}
\hat{H}&=\hbar\omega\left(\hat{a}^{\dagger}\hat{a}+\frac{1}{2}\right)
\end{align}
$$

We have obtain the Hamiltonian in terms of the ladder operators, but we may wonder about the benefits of having done so. However, before doing so, I would like to take small detour. If you wish to continue on with solving the problem, do skip this next section, and [continue](#obtaining-the-energies).

## Number Operator
We know, from the [series method](seriesQHO.md) post that the allowed energies of the harmonic oscillator are given by the expression:

$$
\begin{align}
\tag{A}
E_n=\hbar\omega\left(n+\frac{1}{2}\right)
\end{align}
$$

 If we compare this expression with what we have obtained for the Hamiltonian in equation 6.1, we can draw an interesting parallel.   
 Indeed, we know that the energies are eigenvalues of the Hamiltonian, and are given by a number $n=0,1,2...$ plus $\frac{1}{2}$, times $\hbar\omega$. In addition, we have managed to write the Hamiltonian as a sum of an operator, the produt $\hat{a}^{\dagger}\hat{a}$, plus $\frac{1}{2}$, times $\hbar\omega$. Therefore, we see that the integers $n$ are eigenvalues of the operator $\hat{a}^{\dagger}\hat{a}$. We can thus define $\hat{a}^{\dagger}\hat{a}=\hat{N}$, where $\hat{N}\psi(x)=n\psi(x)$.   
 We call $\hat{N}$ the number operator. This observation is interesting because we recall that $n$ keeps track of the oscillator state or mode $\left(\psi_n(x)\right)$ we are in, and allows to calculate the energy of this mode using expression A. As a result, we can label each state or mode with the eigenvalues of $\hat{N}$. If we use Dirac notation, $|\psi_0(x)\rangle$, $|\psi_1(x)\rangle$... $|\psi_n(x)\rangle=$  $|0\rangle$, $|1\rangle$... $|n\rangle$. This procedure allows us to specify which state (mode) our system occupies (in the simple case of a single-particle system). In a many-particle system, the number operator will be able to "count" the occupancy of each state composing the system, or equivalently specify which eingstates constitute the many-particle wavefunction. Such an analysis is used in second quantization.  

Although second quantization is not the subject of this post, I wanted to highlight that simply by learning the algebraic method of the quantum harmonic oscillator, we can slowly start to build an intuition for the formalism of second quantization. In addition, numerous authors choose to teach the quantization of the electromagnetic field by reviewing the quantum harmonic oscillator through the algebraic method, and extract useful operators from there such as the the creation and annihiliation operators, and the number operator. As a result, I thought it interesting to point out some of the aforementioned features in this post.

## Obtaining the Energies
Let us rewrite the Schrödinger equation in terms of the ladder operators. From equations 6 and 6.1 we can write:

$$
\begin{align}
\tag{7}
\hbar\omega\left(\hat{a}\hat{a}^{\dagger}-\frac{1}{2}\right)\psi(x)&=E\psi(x) \\
 &\text{or}\\
\tag{7.1}
\hbar\omega\left(\hat{a}^{\dagger}\hat{a}+\frac{1}{2}\right)\psi(x)&=E\psi(x)
\end{align}
$$

We recall that when an operator acts on a wavefunction, it yields a new function (provided the function is not an eigenvector of the operator). Suppose we have a set $`\{ \psi(x)\}`$ of eigenfunctions of the harmonic oscillator, and we apply the lowering operator to one of the eigenstates and so we get the function $\hat{a}\psi$. We ask, is the new function $\hat{a}\psi$ also an eigenstate of the Hamiltonian written in 7 ? 

$$
\begin{align}
\tag{8}
\hbar\omega\left(\hat{a}\hat{a}^{\dagger}-\frac{1}{2}\right)\hat{a}\psi&=\hbar\omega\left(\hat{a}\hat{a}^{\dagger}\hat{a}-\frac{1}{2}\hat{a}\right)\psi
\end{align}
$$

Recall from the commutation between $\hat{a}$ and $\hat{a}^{\dagger}$ that $\hat{a}^{\dagger}\hat{a}=\hat{a}\hat{a}^{\dagger}-1$. We can perform this substitution and factor $\hat{a}$ from equation 8 to obtain: 

$$
\begin{align}
\tag{8.1}
\hat{a}\left[\hbar\omega\left(\hat{a}\hat{a}^{\dagger}-1-\frac{1}{2}\right)\right]\psi&=\hat{a}\left[\left(H-\hbar\omega\right)\right]\psi\\
\tag{8.2}
\hat{a}\left[\left(H-\hbar\omega\right)\right]\psi&=\left(E-\hbar\omega\right)\hat{a}\psi
\end{align}
$$

where we have distributed the $\hbar\omega$ factor in the brackets to recover the Hamiltonian. Notice that this result shows that the wavefunctions generated by $\hat{a}\psi$ is also an eigenfunction of the Hamiltonian, provided that $\psi$ comes from the set of eigenfunctions. Importantly, the eigenvalues of $\hat{a}\psi$ are the eigenvalues of $\psi$ minus $\hbar\omega$. Hence, we see that the operator $\hat{a}$ yields another eigenfunction with a lower energy, hence the name lowering operator. Similarly, when we operate $\hat{a}^{\dagger}\psi$ we obtain another eigenfunction with eigenvalue $E+\hbar\omega$, hence the name raising operator.  

If we continuously apply the lowering operator on an eigenfunction at some point we should hit the ground state wavefunction, at which point, applying the lowering operator once more should yield zero. We automatically see that this gives us a recipe to obtain the ground state wavefunction, it will be the wavefunction such that $\hat{a}\psi_0(x)=0$.

## Obtaining the Wavefunctions
We can now determine the ground state wavefunction using the lowering operator: 

$$
\begin{align}
\tag{9}
&\hat{a}\psi_0(x)=
\frac{1}{\sqrt{2m\hbar\omega}}\left(m\omega x+i\hat{p}\right)\psi_0=0\\
&\frac{d\psi_0(x)}{dx}+\frac{m\omega x}{\hbar}\psi_0=0,\quad
\text{we guess $\psi_0(x)=e^{-\frac{m\omega x^2}{2\hbar}}$}\\
&e^{-\frac{m\omega x^2}{2\hbar}}\left(-\frac{m\omega x}{\hbar}+\frac{m\omega x}{\hbar}\right)=0\\
&\psi_0(x)=Ae^{-\frac{m\omega x^2}{2\hbar}}
\end{align}
$$

where $A$ is the normalizing factor, which we can obtain from: 

$$
\begin{align}
\tag{9.1}
|A|^2\int_{-\infty}^{\infty}{e^{-\frac{m\omega x^2}{\hbar}}dx}=1\\
|A|^2\sqrt{\frac{\pi\hbar}{m\omega}}=1\Rightarrow A=\left(\frac{m\omega}{\pi\hbar}\right)^{\left(\frac{1}{4}\right)}\\
\psi_0(x)=\left(\frac{m\omega}{\pi\hbar}\right)^{\left(\frac{1}{4}\right)}e^{-\frac{m\omega x^2}{2\hbar}}
\end{align}
$$

We have obtained the ground state wavefunction of the 1-D Harmonic oscillator. We see that the solution is the same we obtained from the [series method](seriesQHO.md). In addition, if we wanted to obtain the energies, we would simply apply the Hamiltonian to this wavefunction. Strategically, we would use the 6.1 form because we know that $\hat{a}\psi_0(x)=0$, and we would be left with $\frac{\hbar\omega}{2}\psi_0(x)$. Hence lowest allowed energie is $E_0=\frac{\hbar\omega}{2}$.  

Additionally, to get state $\psi_1$, we would simply raise the state $\psi_0$ once, that is $\psi_1(x)=a^{\dagger}\psi_0$, and we would need to apply the normalization condition to obtain the normalized wavefunction. We could continuously apply the raising operator to get higher states of the system. In general, we have,

$$
\begin{align}
\tag{10}
\psi_n(x)=A_n\left(\hat{a}^{\dagger}\right)^n\psi_0(x),\quad E_n=\hbar\omega\left(n+\frac{1}{2}\right)
\end{align}
$$

