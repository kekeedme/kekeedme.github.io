
# 2-Level System (Oscillation forever) Part 1

In this section, we explore the dynamics of a 
two-level quantum system. 
Specifically, it consists of a system 
in which all other degrees of freedom are ignored, 
and we are only interested in the transition 
between two states of the system 
(e.g two electronic states, or two possible spin states, or two possible molecular configurations etc...). 
This consideration means that for our problem,
we need two basis states, 
which will span the entire 2-dimensional complex space in which our system "exists". 
Hence the wavefunction describing our system will 
be a linear combination of these 
two basis states.
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
\tag{1.4}
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
i\hbar\frac{\partial\Psi(r,t)}{\partial t}&=H(r,t)\Psi(r,t)
\end{align}
$$

Inserting 1.5 in 1.6, we obtain:

$$
\begin{align}
\tag{1.7}
i\hbar\frac{\partial \left[c_1(t)\phi_1+c_2(t)\phi_2\right]}{\partial t}&=H(r,t)\left[c_1(t)\phi_1+c_2(t)\phi_2\right]
\end{align}
$$

We can determine an expression for the time-evolution of each time-dependent coefficients, 
$c_1(t)$ or $c_2(t)$ by multiplying the TDSE by the complex conjugate of the corresponding stationary-state and integrating
(in Dirac notation this amounts to multiplying by the bra ($\langle\phi_1|$ to obtain $c_1(t)$ for instance). Doing so for $\dot{c_1}(t)$ (recall any variable $\dot{q}(t)=\frac{dq}{dt}$) in Dirac notation we get:

$$
\begin{align}
\tag{1.8}
i\hbar\left[\frac{\partial c_1(t)}{\partial t}\langle\phi_1|\phi_1\rangle+\frac{\partial c_2(t)}{\partial t}\langle\phi_2|\phi_1\rangle\right]=c_1(t)\langle\phi_1|H(r,t)|\phi_1\rangle+c_2(t)\langle\phi_1|H(r,t)|\phi_2\rangle
\end{align}
$$

exploiting orthornamility, we obtain:

$$
\begin{align}
\tag{1.9}
i\hbar\frac{\partial c_1(t)}{\partial t}=c_1(t)\langle\phi_1|H(r,t)|\phi_1\rangle+c_2(t)\langle\phi_1|H(r,t)|\phi_2\rangle
\end{align}
$$

We do the same procedure with $\langle\phi_2|$ 
to obtain an expression for $\dot{c_2}(t)$:

$$
\begin{align}
\tag{1.10}
i\hbar\frac{\partial c_2(t)}{\partial t}=c_2(t)<\phi_2|H(r,t)|\phi_2>+c_2(t)<\phi_2|H(r,t)|\phi_1>
\end{align}
$$

We can write this system of equations in matrix form:

$$
\begin{align}
\tag{1.11}
i\hbar \frac{\partial}{\partial t}\begin{pmatrix} c_1 (t)\\ c_2(t) \end{pmatrix}=\begin{pmatrix}E_1 & V_{12} \\\ V_{21} & E_2 \end{pmatrix} \begin{pmatrix}c_1 (t)\\ c_2 (t)\end{pmatrix}
\end{align}
$$

In our exemple, the Hamiltonian matrix is independent of time and we can write:

$$
\begin{align}
\tag{1.12}
i\hbar \frac{\partial \mathbf{c}}{\partial t}=\mathbf{H} \mathbf{c}
\end{align}
$$

with $\mathbf{c}(t)=\exp\left(\frac{-i}{\hbar} \mathbf{H}t\right)\mathbf{c}(0)$  
where $\mathbf{c}$ is a column vector and $\mathbf{H}$ a matrix.  
We can see if there is no interaction energy between states ($V_{21}=V_{12}=0$), then the transition probability for a given state will be constant ($|c|^2=cst$), the state remains in a stationary state and does not oscillate (which would give us the non-interacting two-state system we started with). 

## What is Needed for the Script and Plots
We define our basis vectors, in this case we use the standard basis in two-dimensions:

$$
\begin{align}
\tag{1.13}
\phi_1=\begin{pmatrix}1\\\0\end{pmatrix} \quad and \quad 
\phi_2=\begin{pmatrix}0\\\1\end{pmatrix}\end{align}
$$

Constructing $\Psi_0(r,t_0)$ as a linear combination of the basis states:

$$
\begin{align}
\tag{1.14}
\Psi_0(r,t_0)=\frac{1}{\sqrt{c_1^2+c_2^2}}\begin{pmatrix}c_1\\\ c_2\end{pmatrix}
\end{align}
$$

where $\frac{1}{\sqrt{c_1^2+c_2^2}}$ is a normalizing constant.  
Constructing $\Psi(r,t)$ from $\Psi_0(r,t_0)$, and our Hamiltonian defined in equation 1.11, we get:

$$
\begin{align}
\tag{1.15}
\Psi(r,t)=\exp\left(\frac{-i}{\hbar}Ht\right)\Psi_0(r,t_0)
\end{align}
$$

To evaluate $c_1(t)$, we only need to take the inner product of $\langle \phi_1|$
with $|\Psi(r,t)\rangle$. Thus, 

$$
\begin{align}
\tag{1.16}
c_1(t)=\langle \phi_1|\Psi(r,t)\rangle \quad and \quad c_1(t)^*=\langle \Psi(r,t) | \phi_1\rangle
\end{align}
$$

This allows us to write:  

$$
\begin{align}
\tag{1.17}
|c_1|^2=\langle \phi_1|\Psi(r,t)\rangle \langle \Psi(r,t) | \phi_1\rangle
\end{align}
$$

and following a similar procedure for $|c_2|^2$, we obtain:

$$
\begin{align}
\tag{1.18}
|c_2|^2=\langle \phi_2|\Psi(r,t)\rangle \langle \Psi(r,t) | \phi_2\rangle
\end{align}
$$

Using expressions 1.13 to 1.18 is all that is needed to write a script 
and make animated plots of the probability ($|c_1|^2$ and $|c_2|^2$)
that the system would be found in state $|\phi_1\rangle$ or $|\phi_2\rangle$ upon measurement.
This is the point at which the original authors of the mathematica notebook stop, and also where I stop in [my python script](https://github.com/kekeedme/qdwtd/blob/main/two_levelsystem.py)
When we make these plots, we see that the probability oscillates with time forever (see the graph below)
