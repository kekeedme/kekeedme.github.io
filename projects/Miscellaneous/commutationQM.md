# A Brief Discussion on Commutation in Quantum Mechanics
In standard quantum mechanics, a physical system is represented by a state vector (wavefunction) $|\psi\rangle$ and physical observables are represented by linear operators $\hat{A}$ that act on the $|\psi\rangle$. The result of physical measurements are the eignevalues of the operator associated with the measurement. Since the results of a physical measurement are real, and the operators can be complex, they must be Hermitian (i.e equal to their conjugate transpose, $\hat{A}^{\dagger}=\hat{A}$) since Hermitian operators have real eigenvalues.  
If we perform two subsequent measurements on a physical system, this operation would be described by two operators $\hat{A}$ and $\hat{B}$, each corresponding to one of the measurements, acting on the state vector $|\psi\rangle$. If, for instance, we perform the measurement corresponding to operator $\hat{A}$ first, and then performed the one corresponding to operator $\hat{B}$, we would write this as:

$$
\begin{align}
\tag{1}
\hat{B}\hat{A}|\psi\rangle
\end{align}
$$

Similarly, if we performed the measurements in the reverse order, we would represent the two physical processes by the operation $\hat{A}\hat{B}|\psi\rangle$. We might be interested in knowing if the two orders in which we performed the measurement are equivalent, that is if they would yield the same answer. 
One way to check mathematically would be to substract the two operations, and if they are equivalent, we would obtain zero:

$$
\begin{align}
  \tag{2}
    \hat{A}\hat{B}|\psi\rangle -\hat{B}\hat{A}|\psi\rangle&=0 ~\text{if equivalent.}\\
  \tag{2.1}
    \left(\hat{A}\hat{B} -\hat{B}\hat{A}\right)|\psi\rangle&=0 
\end{align}
$$

Equation 2 would be satisfied if the wavefunction $|\psi\rangle$ is an eigenvector of $\hat{A}$ and $\hat{B}$, because the action of either operators on $|\psi\rangle$ would not change it. We would simply get some constant times the vector back again.  
The quantity inside the parentheses is called the commuator of the two operators. It is written as:

$$
\begin{align}
\tag{3}
\left[\hat{A},\hat{B}\right]= \left(\hat{A}\hat{B} -\hat{B}\hat{A}\right)
\end{align}
$$

If the commutator of two operator yields zero, it implies that the order in which the operations (measurements) are performed does not matter, we would get the same result. In addition, it further implies that the two operators have the same set of eigenvectors (this is a general result in Algebra not just physics). 
If however, the commutator is non-zero, then the order of the operation matters, because the first operation changes the vector, such that the second operation is acting on a different vector than we started with. We can write this as:

-$\hat{B}\hat{A}|\psi\rangle=\hat{B}|\phi\rangle$ where $\hat{A}|\psi\rangle=|\phi\rangle$.
-$\hat{A}\hat{B}|\psi\rangle=\hat{B}|\Xi\rangle$ where $\hat{B}|\psi\rangle=|\Xi\rangle$.

It turns out in quantum mechanics, the non-commutativity of certain operators is of significant consequences to the description of physical systems. They are related to the uncertainties in measuring both observables. We will not develop this further in this post. We will dedicate a different post to the uncertain principle. But we will determine how to calculate the commutator of certain operators.

## If the wavefunction is an Eigenvector of the Operators
If we wish to compute the commutator between these two operators, we apply equation 3 onto a test function $\psi\rangle$. Let us consider the case where $|\psi\rangle$ is an eigenvector of $\hat{A}$ with real eigenvalue $a$ and of $\hat{B}$ with real eigenvalue $b$: $\hat{A}|\psi\rangle=a|\psi\rangle$ and $\hat{B}|\psi\rangle=b|\psi\rangle$. Applying equation 3 onto $\psi\rangle$, we obtain:

$$
\begin{align}
\tag{4}
\left[\hat{A},\hat{B}\right]|\psi\rangle&= \left(\hat{A}\hat{B} -\hat{B}\hat{A}\right)|\psi\rangle\\
&= ba|\psi\rangle -ab|\psi\rangle \\
&=\left(ba-ab\right)|\psi\rangle=0
\end{align}
$$ 

## If the Wavefunction is not an Eigenvector of the Operators
If the wavefunction is not an eigenvector of the operators, when the Let us look at the example between the 1-dimensional position $\hat{x}=x$ and momentum operators $\hat{p}=-i\hbar\frac{d}{dx}$. :

$$
\begin{align}
\tag{5}
\left[\hat{x},\hat{p}\right]|\psi\rangle&= \left(\hat{x}\hat{p} -\hat{p}\hat{x}\right)|\psi\rangle\\
&=\hat{x}\hat{p}|\psi\rangle -\hat{p}\hat{x}|\psi\rangle\\
&=x\left(-i\hbar\frac{d}{dx}|\psi\rangle\right) +i\hbar\frac{d}{dx}\left(x|\psi\rangle\right)
\end{align}
$$

Notice that in the first term, we take the derivative of the function $\psi\rangle$ and then multiply it by $-i\hbar x$, while in the second term, we multiply the function $\psi\rangle$ by $x$ first, and then take the derivative of the product. Hence we need to apply the chain rule to the second term. When we perform the appropriate operations we obtain: 

$$
\begin{align}
\tag{5.1}
-i\hbar x\left(\frac{d}{dx}|\psi\rangle\right) +i\hbar\left(|\psi\rangle+x\frac{d}{dx}|\psi\rangle\right)=i\hbar |\psi\rangle
\end{align}
$$

Hence, we observe that 1-dimensional momentum and position operators do not commute. In fact, when we apply to the commutation relation onto a function, we observe that the function picks up a factor of $i\hbar$. We say that the commutator of the 1-dimensional momentum and position operators is $i\hbar$, specifically:

$$
\begin{align}
\tag{6}
\left[\hat{x},\hat{p}\right]=i\hbar
\end{align}
$$

Can you use what we have discussed here to show that the momentum along the y-direction commutes with the position operator in the x-direction, namely that: $[\hat{x},\hat{p_{y}}]=0$? In fact, the linear momentum operator along a given spatial direction commutes with any other position operator along an orthogonal spatial direction. This fact is sometimes summarized by the relation:

$$
\begin{align}
\tag{7}
\left[\hat{x_i},\hat{p_j}\right]=i\hbar\delta_{ij}
\end{align}
$$

where the index $i,j$ label the spatial directions.
