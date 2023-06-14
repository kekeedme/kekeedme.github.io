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
