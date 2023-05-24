# A Brief Discussion on Unitary Evolution

## Unitary Transformation

<div align ="justify">

Within a given vector space, a unitary operation is an operation that preserves the inner product between vectors 
in that space. For instance, consider a vector $|v_1\rangle$
in a complex vector space, equipped with an inner product. The inner product within this space 
is defined as:

$$
\begin{align}
\tag{1}
\langle v_1|v_1\rangle
\end{align}
$$

where, $\langle v_1| = |v_1\rangle^\*$, 
with $|v_1\rangle^\*$ being the conjugate transpose of the vector $|v_1\rangle$.
Let $\hat{U}$ be an operator that acts on the vectors of our vector space. 
When we define basis vectors for our space, $\hat{U}$ is represented by a matrix.
It acts on the vectors under matrix multiplication:

$$
\begin{align}
\tag{2}
\hat{U}|v_1\rangle = |v_2\rangle
\end{align}
$$

The operator can also act on the complex conjugate of the vectors in the space. In order to do this, 
we need to take the conjugate transpose of the matrix that represents it. As a result we get:

$$
\begin{align}
\tag{3}
\langle v_1|\hat{U}^{\dagger}=\langle v_2|
\end{align}
$$

Stating that $\hat{U}$ preserves the inner product when it operates on vectors in the space means:

$$
\begin{align}
\tag{4}
\langle v_1|v_1\rangle&=\langle v_2|v_2\rangle\\
\langle v_1|v_1\rangle&=\langle v_1|\hat{U}^{\dagger}\hat{U}|v_1\rangle
\end{align}
$$

Equation 4 tell us that $\hat{U}^{\dagger}\hat{U}=\mathbf{1}$, where $\mathbf{1}$ is the identity matrix.
From this consideration, 
we learn that the conjugate transpose, $\hat{U}^{\dagger}$, is also equal to the inverse of $\hat{U}$.

</div>
