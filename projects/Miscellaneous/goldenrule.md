# Time-dependent Perturbation Theory Treatment of a Transition Driven by an Oscillatory Frequency

Let us suppose that our system is described by a wavefunction $\Psi(x,t)$, which can be written as a superposition of eigenstates  
  \{ $\psi_n$ \}, much like we have seen [here](time_dependentPT.md). Furthermore, suppose that we prepare the system in the eigenstate $\psi_n$, 
this means that $c_n(t=0)=1$. We now ask, what is the probability of the quantum state transitioning from state $\psi_n$ to $\psi_m$ under 
the influence of a driving potential $V(t)$?  The general answer to this question is given by
equation $4.1$ from the post on the [introduction to time-dependent perturbation theory](time_dependentPT.md). Namely:

$$
\begin{align}
\tag{1}
|c_m(t)|^2&=|\frac{-i}{\hbar}\int_0^t{e^{\frac{i\omega t'}{\hbar}}V_{mn}(t')dt'}|^2
\end{align}
$$
