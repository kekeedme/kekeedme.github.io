# Quantum Mechanical Time-Dependent Perturbation Theory

Time-dependent perturbation theory is a useful tool to understand, calculate and predict the time evolution of a quantum system
subject to an external perturbation. Perturbation theoretic methods are used when perturbations to the system of interests are said to be small.
It thus becomes important to understand when a perturbation can be considered small in order to determine if the use of TD-PT is a viable option 
for the question at hand.  

Let us consider the example of an isolated atom in its ground electronic state. In addition to their kinetic energies, the electrons in the atom
interact with one another and the nucleus through the Coulomb potential. The interplay between the kinetic energies of the particles and the interaction
potentials define the state of the atom. Indeed, the total energy (kinetic and potential) of the particles in the atom are described in 
the Hamiltonian $H_0$ of the system, and since the Coulomb potential is time-independent, we can solve the time-independent Schrödinger equation
with such an Hamiltonian to obtain the set of eingenstates \{ $\psi_n$ \} that the atom
can occupy, with $\psi_0$ being the lowest energy state (the ground state). Note also that the total wavefunction describing the atom will be a
linear combination of these eigenstates: 

$$
\begin{align}
\tag{1}
\Psi_{atom}\left(r,t\right)=\sum_n c_n(t)\psi_n(r)
\end{align}
$$

Recall that the coefficients are of physical importance
because $|c_n|^2$ is the probability of measuring the energy $E_n$ corresponding to eigenstate $\psi_n$. When determine the $c_n$ by 
exploiting the [orthogonality](projects/Miscellaneous/ZPE.md/#Calculating-Expectaction-Value-of-Operators-and-Variance) of the eingstates. Indeed we obtain:

$$
\begin{align}
\tag{2}
\Psi_{atom}\left(r,t\right)=\sum_n c_n(t)\psi_n(r)
\end{align}
$$
