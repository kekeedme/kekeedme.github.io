# Series Method for the Quantum Mechanical Harmonic Oscillator
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
 
 *Please take a look at the great math ressource I link to below, if you would like to further work on and understand the series method to diff.eq*

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

Note that i) $\xi$ is a dimensionless quantity, and ii) we could also treat it as an operator because it is the product of a constant times the position operator. What is interesting about realizing this, is that we could define a similar dimensionless operator using the momentum and use the two operators to solve the problem without any need to solve differential equations, as Dirac did. We will come back to this point later in the [second post](algebraicQHO.md). For now, we will continue with the series method.

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

- Recall that any function $f(x)=e^{\pm x^2}$ as its first derivative equal to $\frac{df}{dx}=\pm 2x\cdot e^{\pm x^2}$ 
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

The second consideration with this approach is that we need all the series to be in terms of $\xi^n$. Notice how for the first derivative term, we do not need to make any adjustements because of the factor $\xi$ in front. We only need to adjust the second derivative term. We thus shift the second series up by two units, thereby turning: $n-1$ into $n+1$, and $n$ into $n+2$ and $a_n$ into $a_{n+2}$. Substituting the appropriate series into our equation 4.7, and factoring out $\xi$, we obtain:  

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

Let us take a moment to understand the recursion relation. It tells us that we will get two sets of coefficients. Indeed, we will get a set from even values of $n$, and another set for odd values of $n$. This fact tells us that our function $f(\xi)$ is actually a sum of even solutions $f_ {even}(\xi)=a_o+a_2\xi^2+...$ and odd $f_ {odd}(\xi)=a_1\xi+a_3\xi^3+...$ solutions. **These solutions are independent from each other**. Morever, we would have to determine $a_0$ to generate all following sets of even-labeled coefficients, and $a_1$ to generate all odd-labeled coefficients using the recursion relation in equation 4.9.  

### Obtaining the Allowed Energies (Eigenvalues)
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
E_n=\hbar\omega\left(n+\frac{1}{2}\right) ~\text{for $n=0,1,2$,...}
\end{align}
$$

Equation 5.1 is one of the most import results as it provides the allowed energies (eigenvalues) for the system. Hence we are halfway through what we set out to do.  
Now we will determine the eigenstates, the wavefunction that describe the state of the oscillator for each of the energies given by equation 5.1

### Obtaining the Wavefunctions (Eigenstates)

In order to determine the eigenstates, we have to remember that the overall solutions are divided into an even and an odd set. Secondly, we have to use the allowed values for $\epsilon$ together with the recursion relation to obtain the appropriate coefficients. Let us look at a few examples.  

Firstly, let us rearrange the recursion relation with the expression for $\epsilon$ found above (eq. 5):

$$
\begin{align}
\tag{5.2}
a_{n+2}=\frac{-2\left(n_{allowed}-n\right)a_n}{\left(n+1\right)\left(n+2\right)}
\end{align}
$$

- Now, let us say that the highest allowed value of $n_{allowed}=0$, then from equation 5.2, we see that the series will only have the coefficient $a_0$, and we choose $a_1=0$ to eliminate the odd part from this set, such that we only get the even solution. Hence our solution for $n=0$, is $\psi_0(\xi)=a_oe^{\frac{-xi^2}{2}}$. Our additional requirement that the wavefunction must be normalized, would allow us to find the value of $a_0$.  

- Now consider that the highest allowed value of $n_{allowed}=1$. We have to calculate with the recursion twice, once for $n=0$, while keeping $n_{allowed}=1$, and once for $n=n_{allowed}=1$. In the first case, we have to choose $a_0=0$ such as to eliminate even solutions from the odd set. In the second case, we find $a_3=0$ because $n=n_{allowed}=1$. So our first odd solution will have one term, and is of the form $\psi_1(\xi)=a_1\xi e^{\frac{-\xi^2}{2}}$.

- Let us now do this final example for $n_{allowed}=2$. We would have to do three calculations one for each value of $n=0,1,2$. But, in the process we will chose $a_1=0$ again to eliminate the odd set. Hence we already know for $n=1$ the result will be zero. For $n=0$, we find $a_2=-2a_0$. For $n=2$, we obtain $a_4=0$. Hence the wavefunction will have two terms, one with coefficient $a_2$, and another with coefficient $a_0$, but since we have already written $a_2$ in terms of $a_0$, our wavefunction is of the form, $\psi_2(\xi)=a_0\left(1-2\xi^2\right)e^{\frac{-\xi^2}{2}}$.


In each of our solutions, we have seen that they are a product of an exponential function times a polynomial. The polynomial so obtained are Hermite polynomials, and we will denote them $H_n(\xi)$. So, we are practically done. The wavefunctions for the Harmonic oscillator of the form: $\psi_n(\xi)=AH_n(\xi)e^{\frac{-\xi^2}{2}}$.  

The domaine of the harmonic oscillator wavefunctions is $]-\infty,\infty[$. We thus would have to normalize the wavefunctions by integrating $\psi_n(\xi)^*\psi_n(\xi)$ over this range. One additional information is that Hermite polynomials are orthogonal under the integral (or inner product):

$$
\begin{align}
\tag{6}
\int_{-\infty}^{\infty}{e^{\frac{-\xi^2}{2}}H_n(\xi)H_m(\xi)=\delta_{mn}} \quad \text{with $\delta_{mm}=1$ or 0 otherwise}
\end{align}
$$

Equation 6 shows that the wavefunctions form an orthogonal set, as they should, since they are eigenfunctions of the Hamiltonian. As we have stated before, we can use the orthogonality condition to determine the normalization coefficients. To wrap it all up, the normalized wavefunctions of the harmonic oscillator are given by:

$$
\begin{align}
\tag{7}
\psi_n(x)=\left(\frac{m\omega}{\pi\hbar}\right)^{\frac{1}{4}}\frac{1}{\sqrt{2^nn!}}H_n\left(\sqrt{\frac{m\omega}{\hbar}}x\right)e^{\frac{-m\omega}{\hbar}x^2}
\end{align}
$$

where we have used our initial definition of $\xi=\sqrt{\frac{m\omega}{\hbar}}x$ to write the wavefunctions in terms of $x$.

### Further Reading on
#### Quantum harmonic oscillator 
- Griffits, D.J., Introduction to Quantum Mechanics, Second Edition. Pearson; pp.52
#### Mathematics
- There is an absolutely wonderful mathematical ressource built by professor [Paul Dawkins](http://www.math.lamar.edu/faculty/dawkins/dawkins.aspx) of Lamar University.  
- This ressource can be found [on this link](https://tutorial.math.lamar.edu/)
- Professor Dawkins'notes on using the series solution to solving differential equation can be found [on this link](https://tutorial.math.lamar.edu/Classes/DE/SeriesSolutions.aspx)
