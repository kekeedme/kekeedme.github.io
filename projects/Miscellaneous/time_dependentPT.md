# Quantum Mechanical Time-Dependent Perturbation Theory

Time-dependent perturbation theory is a useful tool to understand, calculate and predict the time evolution of a quantum system
subject to an external perturbation. Perturbation theoretic methods are used when perturbations to the system of interests are said to be small.
It thus becomes important to understand when a perturbation can be considered small in order to determine if the use of TD-PT is a viable option 
for the question at hand.  

Let us consider the example of an isolated atom in its ground electronic state. In addition to their kinetic energies, the electrons in the atom
interact with one another and the nucleus through the Coulomb potential. The interplay between the kinetic energies of the particles and the interaction
potentials define the state of the atom. Indeed, the total energy (kinetic and potential) of the particles in the atom are described in 
the Hamiltonian $\hat{H}_0$ of the system, and since the Coulomb potential is time-independent, we can solve the [time-independent Schrödinger equation](SchrodingerEQ.md)
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
which will drive our system from one of the stationary states $\psi_n$ to another, with a given probability. For instance, if the system was initially in the state $\psi_n$, that is to say that the perturbation will cause a time-dependent oscillation in the probability of measuring energies associated to states $\psi_n$ or $\psi_m$. Hence, the first step, is to obtain an expression for these probabilities (i.e. for $c_m$ ) as a function of the perturbation $V(t)$.  

With the presence of $V(t)$, the Hamiltonian of the system changes. Indeed, the new Hamiltonian, $\hat{H}(t)$ will be a a sum of the time-independent Hamiltonian $\hat{H}_0$ and the 
perturbation $V(t)$. The Schrödinger equation then reads:

$$
\begin{align}
\tag{3}
i\hbar\frac{\partial \Psi_{atom}(r,t)}{\partial t}&=\hat{H}(t)\Psi_{atom}(r,t)\\
&\text{with}\\
\hat{H}(t)&=\hat{H}_0+V(t)
\end{align}
$$

That the perturbation is considered small means that the eigenstates obtained when the time-independent Schrödinger equation, the set  \{ $\psi_n$ \}, are still valid solutions. It is 
just that the perturbation will drive the system from one of these states to another. As a such, we can use our expansion (equation 1) for $\Psi_{atom}(r,t)$ in equation 3.

$$
\begin{align}
\tag{3}
i\hbar\sum_n \psi_n(r) \frac{\partial }{\partial t}\left[c_n(t)e^{\frac{-iE_nt}{\hbar}}\right]&=\hat{H}_ 0\sum_n c_n(t)\psi_n(r)e^{\frac{-iE_nt}{\hbar}} + V(t)\sum_n c_n(t)\psi_n(r)e^{\frac{-iE_nt}{\hbar}}\\
\\
\tag{3.1}
i\hbar\sum_n \psi_n(r) \left[\dot{c_n}(t)e^{\frac{-iE_n t}{\hbar}}+c_n(t)\left(\frac{-iE_n}{\hbar}\right)e^{\frac{-iE_nt}{\hbar}}\right]&=\sum_n\left[ E_n c_n(t)\psi_n(r)e^{\frac{-iE_nt}{\hbar}} + c_n(t)V(t)\psi_n(r)e^{\frac{-iE_nt}{\hbar}}\right]\\
\tag{3.2}
\sum_n \psi_n(r) \left[i\hbar\dot{c_n}(t)e^{\frac{-iE_n t}{\hbar}}+c_n(t)\left(E_n e^{\frac{-iE_nt}{\hbar}}\right)\right]&=\sum_n\left[ E_n c_n(t)\psi_n(r)e^{\frac{-iE_nt}{\hbar}} + c_n(t)V(t)\psi_n(r)e^{\frac{-iE_nt}{\hbar}}\right]\\
\tag{3.3}
\sum_n \psi_n(r) \left[i\hbar\dot{c_n}(t)e^{\frac{-iE_n t}{\hbar}}\right]&=\sum_n\left[c_n(t)V(t)\psi_n(r)e^{\frac{-iE_nt}{\hbar}}\right]\\
\\
\text{multiplying}  &\text{by $\psi^*_ m$ and integrating}\\
\\
\tag{3.4}
i\hbar\sum_n\dot{c_n}(t)e^{\frac{-iE_n t}{\hbar}} \int_D{\psi^ *_ m(r)\psi_n(r)dr}&=\sum_n c_n(t)e^{\frac{-iE_nt}{\hbar}}\int_D{\psi^ *_ m(r)V(t)\psi_n(r) dr}\\
\tag{3.5}
i\hbar\dot{c_m}(t)e^{\frac{-iE_m t}{\hbar}}&=\sum_n c_n(t)e^{\frac{-iE_nt}{\hbar}}\int_D{\psi^ * _ m(r)V(t)\psi_n(r) dr}\\
\tag{3.6}
i\hbar\dot{c_m}(t)&=\sum_n e^{\frac{i\left(E_m-E_n\right)t}{\hbar}} c_n(t) V_ {mn}(t)\\
\tag{3.7}
\dot{c_m}(t)&=\frac{-i}{\hbar}\sum_n e^{i\omega t}c_n(t)V_{mn}(t)
\end{align}
$$

In going from equation 3 to 3.1 we simply used the fact that the set  \{ $\psi_n$ \} are eigenstates of $\hat{H}_ 0$ on the right hand side, while on the left hand side, we use the product rule to take the derivative of the two time-dependent factors (note that $\dot{c_n}(t)=\frac{dc_n(t)}{dt}$ ). In equation 3.2, on the left hand side, we distributed the $i\hbar$ term such that we could cancel the $\psi_n$ times the second term with the first term of the right hand side, which is how we obtained equation 3.3. We used what we have learned from equation 2 to obtain equation 3.4. We took advantage of the fact that the set  \{ $\psi_n$ \} is an [orthonormal](SchrodingerEQ.md) set, as a result, the integral on the left hand side evaluates to zero
except when $\psi_m=\psi_n$. The orthonormality kills the sum. We also multiply both sides by the complex conjugate of the exponential factor of the left hand side, and obtain equation 3.6. We define the frequency $\omega = \frac{E_m-E_n}{\hbar}$.  

Importantly, note how the integral on the right hand side does not *necessarily* vanish. It shows us that through the interaction potential $V(t)$ the eigenstates couple, which can lead to a state to state transition. We also used the shorthand $V_{mn}(t)$ for the integral on the right hand side. 
Note how for equation 3.7, we have obtained a general expression for the time derivative of $c_m(t)$, but what we really want is to obtain the probability amplitude ( $|c_m(t)|^2$ ) that the system would return energies $E_m$ associated to the state $\psi_m$. We sometimes say *the probability that the system is found in the state* $\psi_m(r)$. 
Achieving this goal is dependent on the problem at hand, but let us suppose that the system was prepared in the state $\psi_n(r)$, and thus $c_n(t_0)=1$. As a result, we can integrate
equation 3.7 to obtain an expression for $c_m(t)$, and further use equation 2 to obtain the probability that the system will be found in state $\psi_m(r)$.

$$
\begin{align}
\tag{4}
c_m(t)&=\frac{-i}{\hbar}\int_0^t{e^{i\omega t'}V_{mn}(t')dt'}\\
\tag{4.1}
\vert c_m(t)\vert ^2&=\vert \frac{-i}{\hbar}\int_0^t{e^{i\omega t'}V_{mn}(t')dt'}\vert ^2
\end{align}
$$

The result we have obtained in 4.1 is an approximation to first order. We can typically get a better approximation to higher order, which will do in another post.  
One important factor that we did not emphasize here, and which again depends on the problem we are considering is the duration of the perturbation. In the case of a monochromatic radition field, we typically obtain an oscillation of the probability amplitudes between the states such that if the perturbation is turned on for a certain duration, we can successfully drive the system to the upper state, but if we live the perturbation past that time it will drive the system back to the initial state and so on. Hence the system would oscillates between the two states at a characteristic frequency. The frequency, the duration of the perturbation which will ensure that the system is found on the upper state can be calculated using 4.1 with the appropriate $V(t)$.

### Further Reading 
- Schatz, G,C.; Ratner, M.A., Quantum Mechanics in Chemistry. Dover; pp.57
- Griffits, D.J., Introduction to Quantum Mechanics, Second Edition. Pearson; pp.299
