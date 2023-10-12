# Series Method to the Quantum Mechanical Harmonic Oscillator
In this section, we will use the series method to solve a second order differential equation of the type:

$$
\begin{align}
\tag{1}
P(x)\frac{d^2y}{dx^2}+Q(x)\frac{dy}{dx}+R(x)y = 0
\end{align}
$$

The series solution consits of stating that equation 1 has a solution that is a power series, that is: 

$$
\begin{align}
\tag{2}
y = \sum_n^{\infty} a_n \left(x-x_0\right)^n
\end{align}
$$

Our task is then to find the coefficients $a_n$ to completely describe $y$.  

In the following, we will present the 1-dimensional time-independent Schrödinger equation (TISE) for a harmonic oscillator. We will see that we can obtain an equation in the form of equation 1 and proceed to solve it using the series method.

## The Harmonic Oscillator Hamiltonian and the Schrödinger Equation 
The Hamiltonian, $\hat{H}$, of the system is defined as the sum of the kinetic energy of the particle undergoing oscillatory motion and its potential energy. For a particle of mass $m$ under the harmonic potential, $V(x)=\frac{1}{2}kx^2$, the Hamiltonian reads: 

$$
\begin{align}
\tag{3}
\hat{H} &= \frac{-\hbar^2}{2m}\frac{d^2}{dx^2}+\frac{1}{2}kx^2\\
&=\frac{-\hbar^2}{2m}\frac{d^2}{dx^2}+\frac{m\omega^2x^2}{2}
\end{align}
$$

where we have used our result from [before](QuantumHOscillator.md), namely that $\omega=\sqrt{\frac{k}{m}}$. We can now write the TISE, $\hat{H}\psi(x)=E\psi(x)$, using the Hamiltonian as:

$$
\begin{align}
\tag{4}
\frac{-\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}+\frac{m\omega^2x^2}{2}\psi(x)=E\psi(x)
\end{align}
$$

We perform a variable substitution that will give us a "neater" form of equation 4. We define the variable $\xi=\sqrt{\frac{m\omega}{\hbar}}x$. This definition allows us to write $x^2=\frac{\xi^2\hbar}{m\omega}$. We can rewrite the Hamiltonian in terms of $\xi$.

- the potential part of the Hamiltonian will turn into:

$$
\begin{align}
\tag{4.1.1}
\frac{m\omega^2x^2}{2}&=\frac{\xi^2\omega\hbar}{2}
\end{align}
$$

- the kinetic part will then be:

$$
\begin{align}
\tag{4.1.2}
\frac{-\hbar^2}{2m}\frac{d^2}{dx^2}=\frac{-\hbar^2}{2m}\cdot \frac{m\omega}{\hbar}\frac{d^2}{d\xi^2}=\frac{-\hbar\omega}{2}\frac{d^2}{d\xi^2}
\end{align}
$$

The TISE can thus be rewritten as: 

$$
\begin{align}
\tag{4.2}
\frac{\omega\hbar}{2}\left[-\frac{d^2\psi(\xi)}{d\xi^2}+\xi^2\psi(\xi)\right]=E\psi(\xi)\\
-\frac{d^2\psi(\xi)}{d\xi^2}+\xi^2\psi(\xi)=\frac{2E}{\omega\hbar}\psi(\xi)
\end{align}
$$

We can define the constant $\epsilon=\frac{2E}{\omega\hbar}$. From now, I will drop the notation $\psi(\xi)$ in favor of just $\psi$ for clarity, but do remember that it is a function of $\xi$. We can rewrite the equation as the following:

$$
\begin{align}
\tag{4.3}
\frac{d^2\psi}{d\xi^2}+\left(\epsilon-\xi^2\psi\right)=0
\end{align}
$$

We will proceed to solve equation 4.3, which will amount to finding solutions (eingenstates) $\psi$ and the allowed energies (eigenvalues) given by the obtained values of $\epsilon$ for our system. 

## Solving the Differential Equation

### The Asympotic Case
In solving differential equations such as the one obtained in equation 4.3, it is both mathematically and physically insigthful to first look at asymptotic cases. In this case, it corresponds to inspecting the differential equation at large displacements (large $x\equiv \xi$). At large displacements, $\xi$ dominates, so equation 4.3 turns into: 

$$
\begin{align}
\tag{4.4}
\frac{d^2\psi}{d\xi^2}-\xi^2\psi=0
\end{align}
$$

Recall that any function $f(x)=e^{\pm x^2}$ as its first derivative equal to $\frac{df}{dx}=\pm 2x\cdot e^{\pm x^2}$ 
and second derivative equal to $\frac{d^2f}{dx^2}=+4x^2\cdot e^{\pm x^2}$. We observe then that suitable guesses for the solution of equation 4.4 are $\phi_1=e^{\frac{\xi^2}{2}}$ and $\phi_2=e^{-\frac{\xi^2}{2}}$. As a result, a linear combination of these two functions is also a solution.  
The general solution is then:  

$$
\begin{align}
\tag{4.5}
\phi(\xi)&=Ae^{\frac{\xi^2}{2}}+Be^{-\frac{\xi^2}{2}},\quad \text{$Ae^{\frac{\xi^2}{2}}$ not normalizable, so choose A=0}\\
\phi(\xi)&=Be^{-\frac{\xi^2}{2}}
\end{align}
$$

The solution we have found dictates the behavior of our quantum oscillator at large displacements. Namely that our wavefunction goes to zero as $x\rightarrow \pm \infty$. Furthermore, the solution we seek (that for equation 4.3) is a product of the solution found in 4.5 times another function $f(\xi)$ which we still need to obtain. Hence we state that our solution has the form $\psi(\xi)=f(\xi)e^{-\frac{\xi^2}{2}}$. Let us then insert this guess for $\psi$ in equation 4.3.

### Solving with the Series Solution
We use our definition of $\psi$ to determine $\frac{d^2\psi}{d\xi^2}$. Using the chain rule and simplifying the expressions we obtain:

$$
\begin{align}
\tag{4.6}
\frac{d^2\psi}{d\xi^2}=e^{\frac{-\xi^2}{2}}\left[\frac{d^2f}{d\xi^2}-2\xi\frac{df}{d\xi}+f\cdot\left(\xi^2-1\right)\right]
\end{align}
$$

We introduce the expression we obtain in equation 4.6 into equation 4.3, distribute terms and simplify to obtain the differential equation:

$$
\begin{align}
\tag{4.7}
\frac{d^2f}{d\xi^2}-2\xi\frac{df}{d\xi}+f\cdot\left(\epsilon-1\right)=0
\end{align}
$$

We can now directly use the series method to solve equation 4.7. Notice that it has the same form as equation 1, with $P(\xi)=1$, $Q(\xi)=-2\xi$, $R(\xi)=\epsilon-1$. Now we will use the series solutions, namely guess that our function has the form of the infinite sum $f(\xi)=\sum_{n=0} a_n\xi^n$. Taking the first and second derivatives of $f$, we obtain:

$$
\begin{align}
\tag{4.7.1}
\frac{df}{d\xi}=\sum_{n=0}^{\infty} n a_n \xi^{n-1}~ \text{and}\\
\frac{d^2f}{d\xi^2}=\sum_{n=0}^{\infty} n\left(n-1\right) a_n \xi^{n-2}
\end{align}
$$

Notice that upon taking the first derivative, the series would start at $n=1$, but it is legal to start at $n=0$ since the first term would be zero, so it does not change the value of the series if we include it. Similary, for the second derivative, we would typically start at $n=2$, but the series evaluates to zero for $n=0$ and $n=1$, so it is acceptable to include these two first terms, as they too do not change the value of the series. It is important for the series that we obtain, as we attempt to solve differential equations, to start at the same index. This reason is why we choose to start all three series at $n=0$.    

The second consideration with this approach is that we need all the series to be in terms of $\xi^n$. Notice how for the first derivative term, we do not need to make any adjustements because of the factor $d\xi$ in front. We only need to adjust the second derivative term. We thus shift the second series up by two untis, thereby turning: $n-1$ into $n+1$, and $n$ into $n+2$ and $a_n$ into $a_{n+2}$. Substituting the appropriate series into our equation 4.7, and factoring out $\xi$, we obtain:  

$$
\begin{align}
\tag{4.8}
\sum_{n=0}^{\infty}\left[\left(n+1\right)\left(n+2\right)a_{n+2}-2na_n+a_n\left(\epsilon-1\right)\right]\xi^n=0
\end{align}
$$

For equation 4.8 to be zero, we set the coefficients of $\xi^n$ equal to zero. When we perform this, we obtain the following recursion relation:

$$
\begin{align}
\tag{4.9}
a_{n+2}=\frac{\left(2n+1-\epsilon\right)a_n}{\left(n+1\right)\left(n+2\right)}
\end{align}
$$

Let us take a moment to understand the recursion relation. It tells us that we will get two sets of coefficients. Indeed, we will get a set from even values of $n$, and another set for odd values of $n$. This fact tells us that our function $f(\xi)$ is actually a sum of even solutions $f_ {even}(\xi)=a_o+a_2\xi^2+...$ and odd $f_ {odd}(\xi)=a_1\xi+a_3\xi^3+...$ solutions. Morever, we would have to determine $a_0$ to generate all following sets of even-labeled coefficients, and $a_1$ to generate all odd-labeled coefficients using the recursion relation in equation 4.9.  

Our power series solution still has to be normalizable. This constraint means that the series must terminate. Hence, we could ask at which value of $n$ will the series terminate. Specifically, what maximum value of $n$ can we reach, such that $a_{n+2}=0$. The answer is that it is the value of $n$ that will make the prefactor in the numerator of 4.9 equal to zero. Hence we can solve:

$$
\begin{align}
\tag{5}
2n+1-\epsilon = 0\\
\epsilon = 2n_{allowed}+1
\end{align}
$$

Expression 5 gives us the allowed values of $\epsilon$ and consequently give us the allowed energies for our harmonic oscillator. Recall that we defined $\epsilon = \frac{2E}{\hbar\omega}$, as a result, the quantized energies of the harmonic oscillator are given by:

$$
\begin{align}
\tag{5.1}
E_n=\hbar\omega\left(n+\frac{1}{2}\right)
\end{align}
$$
