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
the electron is localized on the acceptor, and is $|\phi_3\rangle$ in our model. Lastly, the state in which the electron is localized on the bridge corresponds to the higher energy state 
$|\phi_2\rangle$.

## The Dynamics

Let us consider the case where the system starts entirely at state $\phi_1$, that is $c_1=1$ and $c_2=c_3=0$ at $t=0$.
As stated in the introduction (equations 1.4-1.6), the states that are coupled are $\phi_1$ and $\phi_2$ , and  $\phi_2$ and $\phi_3$.  

Suppose we start with a minimum coupling value of $V=1$, and an energy difference of $\Delta >0$. At the beginning of the dynamics, population progressively transfers from state 
$\phi_1$ to state $\phi_2$. The dynamics from the perspective of state $\phi_2$ are interesting because as this state gets populated, it transfers
population back to states $\phi_1$ and to $\phi_3$, with the same coupling strength and the same energy difference. This particular interplay between states makes it impossible for the population at state $\phi_2$ to ever rise to 1. Interestingly, the population at state $\phi_2$ can never reach a value of 1 even if the energy difference $\Delta =0$; that is, even if all three states are degenerate. This observation further emphasizes the importance of the coupling term in driving the dynamics between states.  
In addition, the back and forth transfer between states $\phi_1$ and $\phi_2$ allow us to observe oscillations ("beating") on the population curve of $\phi_1$. However, the damped oscillation observed for state $\phi_1$ is due to an effective population transfer to state $\phi_3$. Furthermore, because of the coupling between states 
$\phi_2$ and $\phi_3$, we also observe the "beating" oscillations on the population curve of $\phi_3$. Hence, the net effect we observe over one period of oscillation is: From a population value of 1, oscillation on the population curve of state $\phi_1$, with the curve decreasing over time, with a concomitant rise of oscillations on the curve of state $\phi_3$ with the curve increasing over time until it reaches a value of 1.   
Increasing the value of the coupling increases the number of oscillations in a given time interval.  

It is informative to compare this system with the two-level system we have addressed previously. The dynamics of the three-level system approaches that of the 
two-level system when $\frac{V}{\Delta}<<1$. However, in the two-level case, we do not observe "beating" on the population curve of any of the states because of the abscence of coupling to a third state. Hence the transition between the two states happens "smoothly".
