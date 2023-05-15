## 2-Level System (Oscillation forever) Part 1
<div align="justify">
In this section, we explore the dynamics of a 
two-level quantum system. 
Specifically, it consists of a system 
in which all other degrees of freedom are ignored, 
and we are only interested in the transition 
between two states of the system 
(e.g two electronic states, or two possible spin states, or two possible molecular configurations etc…). 
This consideration means that for our problem,
we need two basis states, 
which will span the entire 2-dimensional complex space in which our system “exists”. 
Hence the wavefunction describing our system will 
be a linear combination of these 
two basis states.</div>

#### We begin by describing our basis states:

$\phi_1(r)$ and $\phi_2(r)$  are orthonormal states, that is:

$$
\begin{align}
\tag{1.1}
\langle \phi_1|\phi_1 \rangle=\langle \phi_2|\phi_2 \rangle=1 \\
\tag{1.2}
\langle \phi_1|\phi_2 \rangle=\langle \phi_2|\phi_1\rangle=0
\end{align}
$$

(Recall that 
$\langle\phi_1|\phi_1\rangle=\int \phi_1^\*\left(r\right)\phi_1\left(r\right)dr=1$ , 
with $\phi_1^{*}$ complex conjugate of $\phi_1$ )

#### The Hamiltonian:

-In addition, the states $|\phi_1\rangle$ and $|\phi_2\rangle$ 
are eigenstates of the Hamiltonian, 
that is: 

$$
\begin{align}
\tag{1.3}
H_0|\phi_1\rangle=E_1|\phi_1\rangle \\
H_0|\phi_2\rangle=E_2|\phi_2\rangle
\end{align}
$$

-From these considerations, 
we can see that the Hamiltonian will be a 
diagonal $2\times 2$ Hermitian matrix.  

-Indeed, we can construct it as:

$$
\begin{align}
H_0&=E_1|\phi_1\rangle \langle\phi_1|+E_2 |\phi_2\rangle \langle\phi_2| \\
H_0&=\begin{pmatrix}E_1 & 0 \\\ 0 & E_2 \end{pmatrix}
\end{align}
$$

-Now, we introduce a real, time-independent energy coupling term $V$ 
which couples the two states to each other (but not to themselves). 
The new hamiltonian can be written $H=H_0 + V$. The two basis states
are not eigenfunctions of $H$. We can find the eigenfunctions of $H$
by diagonalizing the new hamiltonian. We will do this a bit later, 
as it is not necessary to visualize the oscillatory dynamics of the system.  

-Since our basis states constitute a complete set, we can express the wavefunction of our system as 
linear combination of the basis states:

$$
\begin{align}
\tag{1.5}
\Psi(r,t)=c_1(t)\phi_1(r)+c_2(t)\phi_2(r)
\end{align}
$$

-Notice how the time-dependence of the wavefunction is contained in the coefficients.  In addition, we know that the probability for our system 
to be in a given basis state $\phi$ is given by $c(t)^*c(t)=|c|^2$.
Hence it will be informative to obtain an expression for the coefficients.

-The time-dependent Schrödinger equation (TDSE) reads:

$$
\begin{align}
\tag{1.6}
i\hbar\frac{\partial\Psi(r,t)}{\partial t}&=H(r,t)\Psi(r,t)\\
\tag{1.7}
i\hbar\frac{\partial \left\[c_1(t)\phi_1+c_2(t)\phi_2\right]}{\partial t}&=H(r,t)\left\[c_1(t)\phi_1+c_2(t)\phi_2\right]
\end{align}
$$


