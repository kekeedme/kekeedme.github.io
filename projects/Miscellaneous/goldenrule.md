# Time-dependent Perturbation Theory Treatment of a Transition Driven by an Oscillatory Frequency

Let us suppose that our system is described by a wavefunction $\Psi(r,t)$, which can be written as a superposition of eigenstate
  \{ $\psi_n$ \}, much like we have seen [here](time_dependentPT.md). Furthermore, suppose that we prepare the system in the eigenstate $\psi_n$, 
this means, we have as an initial condition, that $c_n(t=0)=1$, and as expected, the total probability being equal to $1$. Indeed, $|c_n|^2+|c_m|^2=1$.  
We now ask, what is the probability of the quantum state transitioning from state $\psi_n$ to $\psi_m$ under 
the influence of a driving potential $V(t)$ ?  To answer this question, we would have to solve two coupled differential equations (equation $3.7$ from the post on the [introduction to time-dependent perturbation theory](time_dependentPT.md) ). However, we will make our first approximation and consider the perturbation to be small. By doing so, we can insert the zeroth order value of $c_n(t)=1$ in equation $3.7$ and integrate. This allows us to obtain the first-order expression for $c_m(t)$, of which we can take the square modulus to obtain the probability of measuring an observable corresponding to state $\psi_m$. Namely:

$$
\begin{align}
\tag{1}
\vert c_m(t)\vert ^2  = \vert \frac{-i}{\hbar}\int_0^t{e^{i\omega_0 t'}V_{mn}(t')dt'}\vert ^2 ~\because \omega_0 = \frac{E_m-E_n}{\hbar}, V_{mn}=\langle\psi_m|\psi_n\rangle
\end{align}
$$


Equation $3.7$ in the [previous post](time_dependentPT.md) was exact. The first appromixation we have made is to say that the perturbation is small. We will see explicitly what it means for it to be small. However, by arguing that it is small, it allowed us to consider that the population of the states does not change as the perturbation acts on our system, which is why we were able to simply insert the value of $c_n(t=0)$ into the expression for $\dot{c_m}(t)$ and perform the integral. This immediately raises the issue of non-conservation of the probability. Indeed, if in using this technique, we get a non-zero value for $c_m(t)$, then the sum $|c_n|^2+|c_m|^2\neq 1$. Altough this may sound problematic, that is the essence of the technique; it is to assume that the system barely or does not change, such that we can calculate more easily. But we will see that we do get good predictions from it, and that it gets really close to the exact results when the driving potential is small. This consideration also gives an indication as to how small the perturbation should be, for now, we can say it should be small enough that equation $4.1$ never reaches $1$, because the approximation we made at the beginning about the populations not really changing would not apply.
The probability is, however, conserved to first order. This statement means that if we take the potential term to zero in the first-order expression $4.1$, we recover $|c_n|^2+|c_m|^2=1$. Another question to consider, apart from the strenght of the perturbation, is the time-interval over which it is applied. I prefer to address this point in the next section where we introduce a time-dependent potential and calculate equation $4.1$.

# Perturbation from a Oscillating Potential

Suppose that the our potential $V(r,t)$ is given by a spatial part, and time-dependent part as follows:

$$
\begin{align}
\tag{2}
V(r,t) = V(r) \cos\left(\omega t\right)=
\frac{V(r)}{2}\left(e^{i\omega t} + e^{-i\omega t}\right)~ \because e^{\pm i\omega t} = \cos\left(\omega t\right) \pm i\sin\left(\omega t\right)
\end{align}
$$

Hence, we insert the exponential form of the potential into the expression for $c_m(t)$, perform the integration and then take the square modulus as indicated by equation $1$. When we do this we obtain:

$$
\begin{align}
\tag{3}
c_m(t)= \frac{-i}{2\hbar}\int_0^t V_{mn}\left(e^{i\omega t'} + e^{-i\omega t'}\right){e^{i\omega_0 t'}dt'}\\
=\frac{-iV_{mn}}{2\hbar} \int_0^t {e^{i\left(\omega + \omega_0\right) t'}+e^{i\left(\omega_0 - \omega\right) t'}dt'}\\
c_m(t)=\frac{-iV_{mn}}{2\hbar}\left[\frac{ e^{i\left(\omega + \omega_0\right) t'}-1}{\omega + \omega_0}+\frac{ e^{i\left(\omega_0 - \omega\right) t'}-1}{\omega_0 - \omega}\right]
\end{align}
$$

The probability for transitioning to the state $\psi_m$ is thus given by:

$$
\begin{align}
\tag{4}
P_{mn}(t)=\vert c_m(t)\vert^2=\frac{|V_{mn}|^2}{\left(2\hbar\right)^2} \left[\frac{ e^{i\left(\omega + \omega_0\right) t'}-1}{\omega + \omega_0}+\frac{ e^{i\left(\omega_0 - \omega\right) t'}-1}{\omega_0 - \omega}\right]^2
\end{align}
$$

Let us consider the fact that the oscillating frequency $\omega$ of the interacting potential matches the frequency $\omega_0$ associated to the energy difference between the two states of interests. In this case, called the *Bohr frequency condition*, the second term in equation $4$ dominates in the expression for $P_{mn}(t)$. In addition, if the frequency is of high magnitude, as is the case for electromagnetic radiation (e.g.\~ $10^{14}$ Hz for infrared radiation), the first term would still be small relative to the second term.  
In the case in which the first term would dominate would be when $\omega = -\omega_0$, and when one considers an interaction with an electromanegtic field, this case would correspond to an emission process.  

In the case in which the second term dominates, we can rewrite equation $4$ as:

$$
\begin{align}
\tag{5}
P_{mn}(t)=\frac{|V_{mn}|^2}{\left(2\hbar\right)^2} \left[\frac{ e^{i\left(\omega_0 - \omega\right) t'}-1}{\omega_0 - \omega}\right]^2
\end{align}
$$

We can factor a $e^{i\left(\omega_0-\omega\right)t'/2}$ out, to make use of $\sin(\theta/2)$.

---
**_NOTE:_1**  

- $e^{i\theta/2} = \cos(\theta/2) + i \sin(\theta/2)$ 
- $e^{-i\theta/2} = \cos(\theta/2) - i \sin(\theta/2)$
- Thus we have $e^{i\theta/2} - e^{-i\theta/2} = 2i\sin(\theta/2)$

---
Upon factoring a $e^{i\left(\omega_0-\omega\right)t'/2}$ we obtain: 

$$
\begin{align}
\tag{6}
P_{mn}(t)=\frac{|V_{mn}|^2}{\left(2\hbar\right)^2} \left[\frac{e^{i\left(\omega_0-\omega\right)t'/2}}{\omega_0-\omega}\left(e^{i\left(\omega_0-\omega\right)t'/2}-e^{-i\left(\omega_0-\omega\right)t'/2}\right)\right]^2
=\frac{|V_{mn}|^2}{\left(2\hbar\right)^2}\left[\frac{e^{i\left(\omega_0-\omega\right)t'/2}}{\omega_0-\omega}\left(2i\sin\left[(\omega_0-\omega \right)t'/2\right]\right]^2
\end{align}
$$

Since it is a square modulus (so we multiply by the complex conjugate) the probability is real. Hence, our final expression is: 

$$
\begin{align}
\tag{7}
P_{mn}(t)=\frac{|V_{mn}|^2}{\hbar^2}~ \frac{\sin^2\left[\left(\omega_0-\omega \right)t'/2\right]}{\left(\omega_0 -\omega\right)^2}
\end{align}
$$

##
<figure>
    <img src="P as a function of time.png" alt="figure">
    <figcaption>Figure 1. Oscillation of the probability of finding the system in the upper state as a function of the time over which the perturbation is applied.   
</figcaption>
</figure>

##
Notice how the $P_{mn}(t)$ oscillates in time. This automatically tells us something about the time-interval over which the perturbation should be applied. If the perturbation is left for long it will cause a transition to the upper, $|\psi_m\rangle$ state, but then stimulate a transition back to the lower, $|\psi_m\rangle$ state. The zeroes of $P_{mn}(t)$ as a function of time give us the time treshold at which the system would go back to the lower state. An expression for the zeroes can be obtained by simply setting the argument of the function equal to $n\pi$ with $n=0,1,2,3...$ and solving for time. We find that the probability of finding the system in the lower state occurs every $t=\frac{2n\pi}{\left(\omega_0-\omega\right)}$. Hence the perturbation should be applied for a time interval much shorter than the time that it takes to drive the system back to the initial state.  

Furthermore, we can look at $P_{mn}(t)$ as a function of the driving frequency, $\omega$. We see that the probability peaks *on resonance*, meaning when the driving frequency is equal to the fundamental frequency $\omega_0$ associated with the energy difference between the states.

##
<figure>
    <img src="P as a function of frequency.png" alt="figure">
    <figcaption>Figure 2. The probability of finding the system in the upper state as a function of the driving frequency peaks when the driving frequency is equal to the fundamental frequency.   
</figcaption>
</figure>

##

Notice how at resonance, the probablity is finite. Indeed, we can evaluate the expression for $P_{mn}(t)$ as the driving frequency becomes resonant, that is, as $\lim \left(\omega_0-\omega\right)\rightarrow 0$. We invoke l'Hôpital's rule and find that at resonance:

$$
\begin{align}
\tag{8}
P_{mn}(t)=\frac{|V_{mn}|^2}{4\hbar^2}t^2
\end{align}
$$


## Transitionning to a Continuum of States

Suppose that the frequency drives a transition to a continuum (closely spaced in energy) of states. In this case, our probability will be weighed by a density of states, $\rho(E)$, which corresponds to the number of states per energy.
Our total probability sum over all accessible states is:

$$
\begin{align}
\tag{9}
P_{mn}(t)=\frac{|V_{mn}|^2}{\hbar^2} \int_{states} \rho(E) \frac{\sin^2\left[\left(\omega_0-\omega \right)t'/2\right]}{\left(\omega_0 -\omega\right)^2} dE\\
\end{align}
$$

We can take the density out of the integral because the probability peaks at $\omega_0$, hence, it acts as a delta function that selects only the resonant energy. Hence only the value of the density of state at the final energy $E_m$ need to be considered. We can rewrite this integral over frequencies by substituting $dE\rightarrow \hbar d\omega$.

$$
\begin{align}
\tag{10}
P_{mn}(t)=\frac{|V_{mn}|^2}{\hbar^2} \hbar \rho(E_m)\int_{-\infty}^{\infty} \frac{\sin^2\left[\left(\omega_0-\omega \right)t'/2\right]}{\left(\omega_0 -\omega\right)^2} d\omega
\end{align}
$$

---
**_NOTE:_2**  
$\int_{-\infty}^{\infty} {\frac{sin^2(x)}{x^2} dx}=\pi$
---


Performing the substitution $x=\frac{\left(\omega_0-\omega\right)t'}{2}$ and evaluating the integral from $-\infty$ to $\infty$ (which is allowed since the probability vanishes far from resonance) and making use of **note 2**, we obtain:

$$
\begin{align}
\tag{11}
P_{mn}(t)=\frac{2\pi|V_{mn}|^2}{\hbar} \rho(E_m)t
\end{align}
$$

Notice how the oscillation also dissapears. We would obtain a similar result if we were driving the oscillation with an incoherent source of frequencies (such as incoherent light source), because then we would be driving the transition with a density of frequencies, and we would have to integrate over all driving frequencies.  
We see that to first-order, the probability in linearly dependent of time. 

## Fermi's Golden Rule

We can now ask of the rate of such a transition. In order to this, we can take the derivative of the probability as function of time. Noting $k = \frac{dP_{mn}(t)}{dt}$ as the rate, we obtain:

$$
\begin{align}
\tag{11}
k=\frac{2\pi|V_{mn}|^2}{\hbar} \rho(E_m)
\end{align}
$$

Hence to first order, we see that the transition rate is constant with respect to time, and is proportional to the square of the coupling term $|V_{mn}|$ and proportional to the density of states $\rho(E_m)$. This resul is known as **Fermi's Golden Rule**.
