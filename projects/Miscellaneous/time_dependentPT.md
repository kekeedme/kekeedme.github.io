# Quantum Mechanical Time-Dependent Perturbation Theory

Time-dependent perturbation theory is a useful tool to understand, calculate and predict the time evolution of a quantum system
subject to an external perturbation. Perturbation theoretic methods are used when perturbations to the system of interests are said to be small.
It thus becomes important to understand when a perturbation can be considered small in order to determine if the use of TD-PT is a viable option 
for the question at hand.  

Let us consider the example of an isolated atom in its ground electronic state. In addition to their kinetic energies, the electrons in the atom
interact with one another and the nucleus through the Coulomb potential. The interplay between the kinetic energies of the particles and the interaction
potentials define the state of the atom. Indeed, the total energy (kinetic and potential) of the particles in the atom are described in 
the Hamiltonian $H_0$ of the system, and since the Coulomb potential is time-independent, we can solve the [time-independent Schrödinger equation](SchrodingerEQ.md)
with such an Hamiltonian to obtain the set of eingenstates \{ $\psi_n$ \} that the atom
can occupy, with $\psi_0$ being the lowest energy state (the ground state). Note also that the total wavefunction describing the atom will be a
[linear combination](SchrodingerEQ.md) of these eigenstates: 

$$
\begin{align}
\tag{1}
\Psi_{atom}\left(r,t\right)=\sum_n c_n(t)\psi_n(r)e^{\frac{-iE_nt}{\hbar}}
\end{align}
$$

Recall that the coefficients are of physical importance
because $|c_n|^2$ is the probability of measuring the energy $E_n$ corresponding to eigenstate $\psi_n$, and that we determine the $c_n$ by 
exploiting the [orthogonality](SchrodingerEQ.md) of the eingstates. Indeed we obtain:

$$
\begin{align}
\tag{2}
c_n&=\int_D{\psi_n^ * (r)\Psi(r)dr}\\
&\text{and}\\
|c_n|^2&=\left(\int_D{\Psi^ *(r,t) \psi_n(r)dr}\right)\left(\int_D{\psi_n^ *(r) \Psi(r,t)dr}\right)
\end{align}
$$

## Introduction of a Time-Dependent Perturbation
Let us perturb our system with a time-dependent perturbation $V(t)$. This perturbation could be particle-particle collision, or the interaction of our system with a radiation field for instance. If the electromagnetic field does not significantly distort the coulomb potential that the electrons and nuclei experience within a molecule or an atom, we consider the perturbation small. Typically, as long as the light flux is smaller than $10^{15}~ W\cdot cm^2$ this approximation is valid. Hence, we condisder the perturbation as an interaction
which will drive our system from one of the stationary states $\psi_n$ to another, with a given probability. For instance, if the system was initially in the state $\psi_n$, that is to say that the perturbation will cause a time-dependent oscillation in the probability of measuring energies associated to states $\psi_n$ or $\psi_m$. Hence, the first step, is to obtain an expression for these probabilies (i.e. for $c_m$ ) as a function of the perturbation $V(t)$.  


