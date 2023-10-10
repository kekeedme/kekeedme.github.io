# Simple Three-Level Quantum System

For this discussion, we will, as was done in the original paper, consider a simple three-level quantum system. Our system will consists of three basis states
that are eigenfunctions to the Hamiltonian, $\hat{H}_0$, of the non-interacting system.
I use the qualifier "simple" because: (i) two of the states are degenerate, that is they have the same energy. We label these states as $|\phi_1\rangle$ and
$|\phi_3\rangle$. (ii) the degenerate states are not coupled to each other, 
but are coupled to a third state, higher in energy, through the coupling $\hat{V}$. We label the high energy state $|\phi_2\rangle$. 
Lastly, the coupling strength between states $|\phi_1\rangle$ and $|\phi_2\rangle$
is equal to that between $|\phi_2\rangle$ and $|\phi_3\rangle$. If we summarize the conditions outlined thus far, mathematically, 
we obtain the relations for the energy of the individuals states in the non-interacting limit:

$$
\begin{align}
\tag{1.1}
\langle\phi_1|\hat{H}_0|\phi_1\rangle &=\langle\phi_3|\hat{H}_0|\phi_3\rangle =E \\
\tag{1.2}
\langle\phi_2|\hat{H}_0|\phi_2\rangle &= E_2\\
\tag{1.3}
E_2&>E;
\end{align}
$$

and we obtain the following coupling equations: 

$$
\begin{align}
\tag{1.4}
\langle\phi_1|\hat{V}|\phi_2\rangle &=V_{12}=V_{21}^* \\
\tag{1.5}
\langle\phi_2|\hat{V}|\phi_3\rangle &= V_{23}=V_{32}^*\\
\tag{1.6}
\langle\phi_1|\hat{V}|\phi_3\rangle &=\langle\phi_3|\hat{V}|\phi_1\rangle =0
\end{align}
$$


The authors of the original paper point out that a system such as the one we described, is an apt model for a three-level system with a donor-bridge-acceptor (D-B-A)
molecular triad. In this case, the donor and acceptor are degenerate states. Specifically, the donor state corresponds to the triad being photoexcited, with the excitation
localized on one of the molecules. This locally excited state corresponds to state $|\phi_1\rangle$ in our example. This state is degenerate with the charge-transfer state in which,
the electron is localized on the acceptor, while the positive charge (the hole) is localized on the initially excited moiety; this is $|\phi_3\rangle$ in our model. Lastly, the state in which the electron is localized on the bridge, while the hole remains on the initially excited moiety corresponds to the higher energy state 
$|\phi_2\rangle$.

## The Dynamics

Let us consider the case where the system starts entirely at state $\phi_1$, that is $c_1=1$ and $c_2=c_3=0$ at $t=0$.
As stated in the introduction (equations 1.4-1.6), the states that are coupled are $\phi_1$ and $\phi_2$ , and  $\phi_2$ and $\phi_3$.  

Suppose we start with a minimum coupling value of $V=1$, and an energy difference of $\Delta >0$. At the beginning of the dynamics, population progressively transfers from state 
$\phi_1$ to state $\phi_2$. 

<figure>
    <img src="/projects/quantumdynamics/images/three-level.png" alt="figure">
    <figcaption>Figure 1. Oscillation of the probability of measuring the system in state 1 (blue), 2 (orange) or three (green) as a function of time, when the system starts from state 1. 
</figcaption>
</figure>     

The dynamics from the perspective of state $\phi_2$ are interesting because as this state gets populated, it transfers
population back to states $\phi_1$ and to $\phi_3$, with the same coupling strength and the same energy difference. This particular interplay between states makes it impossible for the population at state $\phi_2$ to ever rise to 1. Interestingly, the population at state $\phi_2$ can never reach a value of 1 even if the energy difference $\Delta =0$; that is, even if all three states are degenerate. This observation further emphasizes the importance of the coupling term in driving the dynamics between states.  
In addition, the back and forth transfer between states $\phi_1$ and $\phi_2$ allow us to observe oscillations ("beating") on the population curve of $\phi_1$. However, the damped oscillation observed for state $\phi_1$ is due to an effective population transfer to state $\phi_3$. Furthermore, because of the coupling between states 
$\phi_2$ and $\phi_3$, we also observe the "beating" oscillations on the population curve of $\phi_3$. Hence, the net effect we observe over one period of oscillation is: From a population value of 1, oscillation on the population curve of state $\phi_1$, with the curve decreasing over time, with a concomitant rise of oscillations on the curve of state $\phi_3$ with the curve increasing over time until it reaches a value of 1.   
Increasing the value of the coupling increases the number of oscillations in a given time interval.  

It is informative to compare this system with the two-level system we have addressed previously. The dynamics of the three-level system approaches that of the 
two-level system when $\frac{V}{\Delta}<<1$. However, in the two-level case, we do not observe "beating" on the population curve of any of the states because of the abscence of coupling to a third state. Hence the transition between the two states happens "smoothly".

The other case we can consider is if we were to start the dynamics from state $\phi_2$, that is $c_2=1$ and $c_1=c_3=0$. Due to the equal coupling between
$\phi_2$ and $\phi_1$ and between $\phi_2$ and $\phi_3$, the population will be distributed from $\phi_2$ to the other states equally (overlay perfectly on the figure). Additionally, the population only decays to zero for $\phi_2$ if $\Delta =0$ and when $c_1^2=c_3^2=0.5$.

<figure>
    <img src="/projects/quantumdynamics/images/three-level-from2.png" alt="figure">
    <figcaption>Figure 2. Oscillation of the probability of measuring the system in state 1 (blue), 2 (orange) or three (green) as a function of time, when the system starts from state 2.
</figcaption>
</figure>

## Mathematics Needed for The Script and the Plots

The mathematics we need to understand and model the system are not very different than what we have seen for the two-level case. Our total wavefunction
exists in a space that is entirely spanned by the three-basis states (when all other degrees of freedom are ignored). This consideration implies that we are working with a 3-D state space. As a result, our basis states need to be 3 dimensional. Since the operators will be represented in the chosen three-state
basis, we will obtain $3\times 3$ matrices. We define the basis states:  

$$
\begin{align}
\tag{1.7}
\phi_1=\begin{pmatrix}1\\\ 0\\\ 0\end{pmatrix} \quad and \quad 
\phi_2=\begin{pmatrix}0\\\ 1\\\ 0\end{pmatrix} \quad and \quad 
\phi_3=\begin{pmatrix}0\\\ 0\\\ 1\end{pmatrix}
\end{align}
$$

Constructing $\Psi_0(r,t_0)$ as a linear combination of the basis states:

$$
\begin{align}
\tag{1.8}
\Psi_0(r,t_0)=\frac{1}{\sqrt{c_1^2+c_2^2+c_3^2}}\begin{pmatrix}c_1\\\ c_2\\\ c_3\end{pmatrix}
\end{align}
$$

where $\frac{1}{\sqrt{c_1^2+c_2^2+c_3^2}}$ is a normalizing constant.  
Constructing $\Psi(r,t)$ from $\Psi_0(r,t_0)$, and the Hamiltonian, we get:

$$
\begin{align}
\tag{1.9}
\Psi(r,t)=\exp\left(\frac{-i}{\hbar}Ht\right)\Psi_0(r,t_0)
\end{align}
$$

with the non-interacting Hamiltonian defined as: 

$$
\begin{align}
\tag{1.10}
H_0&=E|\phi_1\rangle \langle\phi_1|+E_2 |\phi_2\rangle \langle\phi_2|+E |\phi_3\rangle \langle\phi_3| \\
H_0&=\begin{pmatrix}E & 0 & 0 \\\ 0 & E_2 & 0 \\\ 0 & 0 & E \end{pmatrix}
\end{align}
$$

In order to construct the interaction Hamiltonian, we add the coupling term $V$ using the equations 1.4-1.6, such that the interacting matrix is:

$$
\begin{align}
\tag{1.11}
H_I&=|\phi_1\rangle V_{12} \langle\phi_2|+ |\phi_2\rangle V_{21} \langle\phi_1|+ |\phi_2\rangle V_{23} \langle\phi_3|+ |\phi_3\rangle V_{32} \langle\phi_2| \\
H_I&=\begin{pmatrix}0 & V_{12} & 0 \\\ V_{21} & 0 & V_{23} \\\ 0 & V_{32} & 0 \end{pmatrix}
\end{align}
$$

The total Hamiltonian is defined as $H=H_0+H_I$. We can also write a "difference" Hamiltonian, $H_{diff}$ , where we subtract $E \cdot \mathbf{1}$ from the total Hamiltonian, where $\mathbf{1}$ is the $3\times 3$ identity matrix. As such, $H_{diff}$ ,can be written as:

$$
\begin{align}
\tag{1.12}
H_{diff}&=\begin{pmatrix}0 & V_{12} & 0 \\\ V_{21} & \Delta & V_{23} \\\ 0 & V_{31} & 0 \end{pmatrix}
\end{align}
$$

In order to evaluate the population of each state as a function of time, we determine the magnitude squared of each time-dependent coefficient, in the same manner
as we have done for the two-level system:

$$
\begin{align}
\tag{1.13}
|c|^2&=\langle \phi|\Psi(r,t)\rangle \langle \Psi(r,t) | \phi\rangle
\end{align}
$$

One final remark is that it is convenient to use $H_{diff}$ in constructing the total wavefunction (equation 1.9) because this allows us to directly manipulate the energy difference as a parameter in our simulations.
