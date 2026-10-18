# Query complexity of controlled reflection noise

This file proves the fixed-error oracle-query classification for the [controlled target model](model.md). The upper bound uses [channel stability](channel_stability.md) and unitary-channel learning. The lower bound is an explicit two-qubit protocol with adjustable mixed replacements; its physical realization is described further in [mixed resets](mixed_resets.md).

<a id="query-theorem"></a>

## 1. Exact theorem and access model

The retained target system has dimension four. Let $`U`$ be an unknown Hermitian unitary involution:

```math
U=U^\dagger,\qquad U^2=I_4.
```

One oracle query is an ordinary application of controlled-$`U`$,

```math
\mathcal O_U
=|0\rangle\langle0|\otimes I_4
+|1\rangle\langle1|\otimes U.
```

An uncontrolled application of $`U`$ uses one such query with the control in $`|1\rangle`$. Known integer powers reduce to $`I_4`$ or $`U`$ by parity, and inverse access uses the same oracle. Matrix entries and entrywise-conjugate oracles are not supplied.

The target is

```math
\Phi_U
=
\mathcal C_r\circ e^{t_r\mathcal L_U}\circ
\mathcal C_{r-1}\circ\cdots\circ
\mathcal C_1\circ e^{t_1\mathcal L_U}\circ\mathcal C_0,
```

where

```math
\mathcal L_U=\mathrm{Ad}_U-\mathrm{Id},
\qquad
t_k\geq0,
\qquad
\sum_{k=1}^{r}t_k=T.
```

The rate is normalized to one and there is no Hamiltonian during these intervals. The finite sequence of control channels and durations is known. Each $`\mathcal C_k`$ is CPTP on the same four-dimensional retained system and is independent of $`U`$. Initial and terminal controls are allowed and charged:

```math
E_{\mathrm{used}}
=\sum_{k=0}^{r}\kappa(\mathcal C_k)
\leq E.
```

Here $`\kappa`$ is the [entropy-decrease capacity](entropy_capacity.md#definition), with natural logarithms. This is an **at-most-$`E`$** promise on the specified target controls.

The simulator must implement the full, unconditioned channel on arbitrary unknown input, including an untouched reference, within unhalved diamond error $`0.01`$. Its oracle-query count must be bounded on every execution. Its own auxiliary memory, measurements, probe preparation, known controls, resets, and classical processing are unrestricted. The known target controls and other known finite-dimensional operations are executable to any required accuracy without unknown-oracle queries. Their gate count and classical cost are outside the query measure.

Let $`Q_4(T,E,0.01)`$ be the worst-case bounded-query complexity over targets with this promise.

**Theorem.** Uniformly for every real $`T\geq1`$ and $`E\geq0`$,

```math
\boxed{
Q_4(T,E,0.01)
=
\Theta\!\left(\min\left\{T,\sqrt{T(1+E)}\right\}\right).
}
```

The constants are independent of the number of control boundaries. The theorem is a worst-case statement about oracle queries at this fixed accuracy. It does not assert the same cost for every target or a sublinear total runtime.

## 2. A bounded direct-trajectory upper bound

For one interval,

```math
\begin{aligned}
e^{t\mathcal L_U}
&=e^{-t}\sum_{n=0}^{\infty}\frac{t^n}{n!}
\mathrm{Ad}_{U^n}\\
&=\mathbb E_{N\sim\mathrm{Pois}(t)}
\mathrm{Ad}_{U^N}.
\end{aligned}
```

Expand each interval this way and keep the known controls in their prescribed order. The complete target is exactly the mixture over independent counts
$`N_k\sim\mathrm{Pois}(t_k)`$ of those controlled trajectories.

Their total jump count is

```math
J=\sum_{k=1}^{r}N_k
\sim\mathrm{Pois}(T).
```

This distribution is independent of the number of intervals. One may sample $`J`$ first and then sample the interval counts conditionally from the multinomial distribution with probabilities $`t_k/T`$. Each trajectory requires at most $`J`$ unknown queries. The involution identity can reduce a run of repeated $`U`$ applications to its parity, which can only lower this count.

An expected jump count by itself would not prove the bounded-query theorem. Set

```math
M=\lceil10T\rceil.
```

If the classically selected trajectory has $`J>M`$, implement a fixed known channel, such as the identity, instead. Otherwise implement the trajectory and every prescribed control. The oracle-query count is now at most $`M`$ on every branch.

For a Poisson variable of mean $`T`$, the exponential-moment bound gives

```math
\begin{aligned}
\Pr(J>M)
&\leq\Pr(J\geq10T)\\
&\leq
\exp\!\left[-(10\log10-9)T\right]\\
&<10^{-6},
\qquad T\geq1.
\end{aligned}
```

Replacing a mixture component of total probability $`a`$ by another CPTP channel changes the diamond norm by at most $`2a`$. Thus this truncation contributes less than $`2\cdot10^{-6}`$ error. Sampling and known-operation precision can use part of the remaining $`0.01`$ allowance without adding unknown queries.

The implementation is an unconditioned CPTP mixture; it uses no quantum postselection. It proves

```math
Q_4(T,E,0.01)=O(T).
```

<a id="learning-upper-bound"></a>

## 3. Learning upper bound with phase alignment

The required learning result is [Haah–Kothari–O'Donnell–Tang, Theorem 1.1](../references/RELATED_WORK.md#hkot2023): for a $`d`$-dimensional unitary $`W`$, at most $`O(d^2/\zeta)`$ ordinary forward applications suffice to output a unitary estimate $`V`$ such that

```math
\mathbb E\left[
\|\mathrm{Ad}_V-\mathrm{Ad}_W\|_\diamond^2
\right]\leq\zeta^2.
```

The expectation is over the estimation error. The oracle count is bounded. The same source, Proposition 1.6, bounds projective operator distance by unitary-channel diamond distance.

### 3.1 Learn an anchored unitary

Use one supplied controlled-$`U`$ call to apply the eight-dimensional unitary

```math
W=\mathrm{diag}(I_4,U).
```

Run the learning procedure on auxiliary probes, keeping the unknown target input and its reference untouched. The known identity block will fix the otherwise undetermined global phase of the unitary estimate.

For a particular estimate $`V`$, write

```math
\delta
=\|\mathrm{Ad}_V-\mathrm{Ad}_W\|_\diamond.
```

There is a scalar phase $`z`$ with

```math
\|V-zW\|_{\mathrm{op}}\leq\delta.
```

The algorithm does not need to know $`z`$ or $`\delta`$; they are used only to prove the accuracy of the following explicit fit.

### 3.2 Fit a reflection for every estimate

Let $`V_{00}`$ be the upper-left four-dimensional block of $`V`$. Define

```math
\alpha=\frac14\mathrm{Tr}V_{00},
\qquad
w=
\begin{cases}
\alpha/|\alpha|,&\alpha\ne0,\\
1,&\alpha=0.
\end{cases}
```

Let $`K`$ be the lower-right block of $`w^*V`$, and put

```math
H=\frac{K+K^\dagger}{2},
\qquad
U'=\mathrm{sign}(H),
```

assigning sign $`+1`$ to zero eigenvalues. Every estimate produces a Hermitian involution $`U'`$.

We claim the pointwise estimate

```math
\boxed{\|U'-U\|_{\mathrm{op}}\leq6\delta.}
```

First suppose $`\delta<1/3`$. Compression to the identity block and the trace bound give

```math
|\alpha-z|\leq\delta,
```

so $`\alpha\ne0`$. Normalization changes the phase by at most twice this error:

```math
|w-z|
\leq|w-\alpha|+|\alpha-z|
=\bigl|1-|\alpha|\bigr|+|\alpha-z|
\leq2\delta.
```

Therefore

```math
\|w^*V-W\|_{\mathrm{op}}\leq3\delta,
\qquad
\|H-U\|_{\mathrm{op}}\leq3\delta.
```

Because $`3\delta<1`$ and the spectrum of $`U`$ is contained in $`\{-1,+1\}`$, every eigenvalue of $`H`$ lies within $`3\delta`$ of one of these two points, with the same sign. Consequently

```math
\|\mathrm{sign}(H)-H\|_{\mathrm{op}}\leq3\delta,
```

and the claimed $`6\delta`$ estimate follows by the triangle inequality.

If $`\delta\geq1/3`$, use the trivial distance between two reflections:

```math
\|U'-U\|_{\mathrm{op}}\leq2\leq6\delta.
```

This also covers the arbitrary choice when $`\alpha=0`$, which can occur only when $`\delta\geq1`$. There is no discarded bad-estimation event. In particular,

```math
\mathbb E\|U'-U\|_{\mathrm{op}}^2
\leq36\zeta^2.
```

### 3.3 Implement and average the fitted target

For each estimate, implement the same specified control sequence with $`U'`$ in place of $`U`$. This is a known CPTP target channel, denoted $`\Phi_{U'}`$. It needs no further unknown-oracle calls. In particular, a known reflection interval can be implemented by applying $`U'`$ with probability $`(1-e^{-2t_k})/2`$ and doing nothing otherwise, then applying the known boundary control.

The [stability theorem](channel_stability.md#main-theorem) gives, for every estimate,

```math
\|\Phi_{U'}-\Phi_U\|_\diamond
\leq
\sqrt T\,\|U'-U\|_{\mathrm{op}}
\left[1+\sqrt{4\log4+2E}\right].
```

Because learning occurred on independent probes, the actual channel on the unknown input is the average

```math
\overline\Phi_U=\mathbb E_V\Phi_{U'(V)}.
```

Convexity of the norm and Cauchy–Schwarz therefore imply

```math
\begin{aligned}
\|\overline\Phi_U-\Phi_U\|_\diamond
&\leq\mathbb E_V\|\Phi_{U'}-\Phi_U\|_\diamond\\
&\leq
6\zeta\sqrt T
\left[1+\sqrt{4\log4+2E}\right].
\end{aligned}
```

Choose, for example,

```math
\zeta=
\frac{0.01}{
12\sqrt T\left[1+\sqrt{4\log4+2E}\right]
}.
```

This allocates half the error to learning and leaves half for known synthesis and classical sampling precision. No high-probability amplification or confidence logarithm is needed.

The learning dimension is eight, a constant. Thus

```math
Q_4(T,E,0.01)
=O\!\left(\sqrt{T(1+E)}\right).
```

Choosing the better of this algorithm and the bounded direct algorithm proves the theorem's upper bound.

<a id="lower-bound"></a>

## 4. Explicit target family for the lower bound

The coherent recovery mechanism has precedents in [informative-noise error correction](../references/RELATED_WORK.md#chen2024) and [gauge-reset metrology](../references/RELATED_WORK.md#liu2026). The finite target below makes its duration, dimension, capacity, and output separation explicit.

### 4.1 One reflection on two qubits

Use a syndrome qubit $`S`$ and logical qubit $`L`$. Define

```math
\begin{aligned}
U_\theta
&=\cos\theta\,X_S\otimes I_L
-\sin\theta\,Y_S\otimes Z_L\\
&=
|0\rangle\langle1|_S\otimes e^{i\theta Z_L}
+|1\rangle\langle0|_S\otimes e^{-i\theta Z_L}.
\end{aligned}
```

The two Pauli terms are Hermitian involutions and anticommute. Hence $`U_\theta`$ is a Hermitian involution. The same anticommutation gives

```math
(U_\theta-U_0)^2
=4\sin^2(\theta/2)I,
```

so

```math
\|U_\theta-U_0\|_{\mathrm{op}}
=2|\sin(\theta/2)|
\leq|\theta|.
```

The corresponding controlled oracles have exactly the same operator distance. This estimate uses explicit representatives, so access to a controlled global phase does not evade it.

### 4.2 Exact duration and controls

For the supplied real $`T\geq1`$, set

```math
N=\lfloor T\rfloor,
\qquad
\Delta=\frac TN.
```

Then

```math
1\leq\Delta<2,
\qquad
\frac T2\leq N\leq T.
```

Use exactly $`N`$ noisy intervals of length $`\Delta`$. Each is followed by the known replacement

```math
\mathcal R_b(\rho_{SL})
=\tau_b\otimes\mathrm{Tr}_S\rho_{SL},
\qquad
\tau_b=\frac{I+bZ}{2}.
```

The initial control is the identity. The final replacement is included, so the target contains exactly $`N`$ charged replacements.

For any input,

```math
S(\rho_{SL})-S(\mathcal R_b(\rho_{SL}))
=S(S\mid L)_\rho-S(\tau_b)
\leq\log2-S(\tau_b).
```

Equality holds for a product input with the syndrome maximally mixed. Thus

```math
\kappa(\mathcal R_b)
=e(b)=\log2-h\!\left(\frac{1+b}{2}\right).
```

The positive-coefficient expansion

```math
e(b)=\sum_{k=1}^{\infty}
\frac{b^{2k}}{(2k-1)(2k)}
```

follows by integrating $`e'(b)=\mathrm{artanh}b`$. Its first coefficient is $`1/2`$ and all coefficients sum to $`\log2`$. Therefore

```math
\frac{b^2}{2}\leq e(b)\leq(\log2)b^2,
\qquad
E_{\mathrm{used}}=Ne(b).
```

### 4.3 Exact logical coherence

Write

```math
p=\frac{1-e^{-2\Delta}}2,
\qquad
p_0=\frac{1-e^{-2}}2.
```

Then $`p_0\leq p<1/2`$, and the interval channel is exactly

```math
e^{\Delta\mathcal L_{U_\theta}}
=(1-p)\mathrm{Id}+p\mathrm{Ad}_{U_\theta}.
```

Choose the same known input under both oracle hypotheses:

```math
\rho_{\mathrm{in}}
=\tau_b\otimes|+\rangle\langle+|_L.
```

This choice witnesses the difference of two channels. It does not insert an uncharged initial replacement of an arbitrary target input.

For any logical state $`\rho`$, a noisy interval followed by $`\mathcal R_b`$ produces $`\tau_b\otimes\mathcal F_{\theta,b}(\rho)`$, where

```math
\begin{aligned}
\mathcal F_{\theta,b}(\rho)
={}&(1-p)\rho\\
&+\frac{p(1+b)}2e^{-i\theta Z}\rho e^{i\theta Z}
+\frac{p(1-b)}2e^{i\theta Z}\rho e^{-i\theta Z}.
\end{aligned}
```

Thus each cycle multiplies the logical off-diagonal entry by

```math
f_b(\theta)
=1-p+p\cos(2\theta)-ipb\sin(2\theta).
```

After all $`N`$ cycles the output is $`\tau_b\otimes\rho_L(\theta)`$, with

```math
\rho_L(\theta)
=\frac12
\begin{pmatrix}
1&f_b(\theta)^N\\
\overline{f_b(\theta)}^{\,N}&1
\end{pmatrix}.
```

At $`\theta=0`$, the logical output remains $`|+\rangle\langle+|`$. Subtracting these two matrices gives

```math
\boxed{
\|\Phi_{U_\theta}(\rho_{\mathrm{in}})
-\Phi_{U_0}(\rho_{\mathrm{in}})\|_1
=|f_b(\theta)^N-1|.
}
```

This is the full unconditioned output. There is no bath record, syndrome transcript, or selected measurement branch.

## 5. Uniform finite separation in every budget regime

### 5.1 A positive-polarization estimate

Suppose $`Nb^2\geq1`$, and choose

```math
\theta=\frac1{2Nb}.
```

Then $`0<\theta\leq1/2`$. Write $`f_b(\theta)=A-iB`$. Using $`1-\cos(2\theta)\leq2\theta^2`$,

```math
A\geq1-2p\theta^2.
```

By Bernoulli's inequality,

```math
|f_b(\theta)|^N
\geq A^N
\geq1-2pN\theta^2
\geq1-\frac p2
\geq\frac34.
```

Moreover, $`\sin(2\theta)\geq\theta`$ on this interval, and

```math
p b\theta\leq B\leq2p b\theta=\frac pN.
```

The ratio $`B/A`$ is at most $`p/[N(1-p/2)]\leq2/3`$. Set $`\varphi=\arctan(B/A)`$. For $`0\leq x\leq1`$, $`x/2\leq\arctan x\leq x`$, so

```math
\frac p4
\leq N\varphi
\leq\frac{p}{1-p/2}
\leq\frac23<\frac\pi2.
```

Consequently,

```math
\begin{aligned}
|f_b(\theta)^N-1|
&\geq|\mathrm{Im}f_b(\theta)^N|\\
&=|f_b(\theta)|^N\sin(N\varphi)\\
&\geq\frac34\sin(p_0/4)\\
&>0.08.
\end{aligned}
```

The estimate is uniform over all real $`T\geq1`$ and every allowed positive polarization satisfying $`Nb^2\geq1`$.

### 5.2 Zero polarization

For $`b=0`$, replacement by $`I/2`$ is unital and has capacity zero. The coherence is real:

```math
f_0(\theta)=1-2p\sin^2\theta.
```

Choose

```math
\theta=\frac1{2\sqrt N}.
```

Then $`0<\theta\leq1/2`$ and $`f_0(\theta)>0`$. Since $`\sin\theta\geq2\theta/\pi`$ on $`[0,\pi/2]`$,

```math
\begin{aligned}
1-f_0(\theta)^N
&\geq1-\exp[-2pN\sin^2\theta]\\
&\geq1-\exp[-2p_0/\pi^2]\\
&>0.08.
\end{aligned}
```

The zero-budget witness uses a second-order change in dephasing. It does not require a nonzero first derivative at the baseline.

### 5.3 Choose the polarization using the supplied budget

Use

```math
b=
\begin{cases}
0,&0\leq E<\log2,\\
\sqrt{E/(N\log2)},&\log2\leq E<N\log2,\\
1,&E\geq N\log2.
\end{cases}
```

When $`N=1`$, the middle case is empty.

The first case uses zero capacity and the zero-polarization angle. In the middle case,

```math
Ne(b)\leq N(\log2)b^2=E,
\qquad
Nb^2=\frac E{\log2}\geq1.
```

The positive-polarization estimate applies with $`\theta=1/(2Nb)`$. In the last case, pure resets use $`N\log2\leq E`$, and the angle is $`1/(2N)`$. Thus every construction obeys the at-most-$`E`$ promise and has output gap strictly larger than $`0.08`$.

Let

```math
\mathcal R(T,E)=\min\{T,\sqrt{T(1+E)}\}.
```

The inverse separation angle has the required order in all cases. For $`E<\log2`$, it is $`2\sqrt N=\Theta(\sqrt T)`$, while $`\mathcal R(T,E)=\Theta(\sqrt T)`$. In the middle range it is

```math
\frac1\theta=2\sqrt{\frac{NE}{\log2}},
```

and $`E\geq\log2`$, $`N\geq T/2`$ imply $`1/\theta=\Omega(\mathcal R(T,E))`$. In the final range, $`1/\theta=2N\geq T\geq\mathcal R(T,E)`$. The constants are universal, including at the boundaries and for $`1\leq T<2`$.

## 6. Oracle hybrid lower bound

Consider any simulator with at most $`q`$ unknown-oracle queries on every execution. Its known operations, measurements, and auxiliary state preparations may depend on the supplied target controls and durations, but are common to the two unknown-oracle hypotheses constructed above.

For unitary oracles $`V,W`$ and an arbitrary state with reference,

```math
(V\otimes I)\rho(V^\dagger\otimes I)
-(W\otimes I)\rho(W^\dagger\otimes I)
```

has trace norm at most $`2\|V-W\|_{\mathrm{op}}`$, by the same two-term expansion used in the [elementary channel cap](channel_stability.md). Known CPTP interleavings contract trace distance. Telescoping one oracle replacement at a time therefore bounds the simulator's endpoint output difference by

```math
2q\|\mathcal O_{U_\theta}-\mathcal O_{U_0}\|_{\mathrm{op}}
\leq2q|\theta|.
```

Adaptive measurements and branching do not invalidate this argument. Retaining their outcomes in a dilation gives a common circuit, and a bounded-query algorithm can be padded to $`q`$ slots using controlled calls that act trivially on unused branches. The simulator's workspace is unrestricted. Since the supplied reflection is its own inverse, allowing inverse calls changes nothing in the bound.

Feed the same known witness input into the simulator at the two endpoints. Diamond approximation error $`0.01`$ at each endpoint can reduce their exact target gap by at most $`0.02`$. Hence

```math
0.08
<
0.02+2q|\theta|.
```

It follows that

```math
q>\frac{0.03}{|\theta|}
=\Omega\!\left(\min\{T,\sqrt{T(1+E)}\}\right).
```

Together with the two upper bounds, this completes the theorem.

## 7. What the resource classification specifies

The target dimension is fixed at four in both the theorem and its lower bound. Its rate remains one, and its noise intervals contain one supplied reflection. Linear query hardness when $`E=\Omega(T)`$ therefore does not require a growing graph, growing target Hilbert space, or a hidden small jump rate.

The capacity budget belongs to the prescribed target controls. It does not bound the simulator's entropy production, learning probes, or memory. The lower construction uses $`N=\Theta(T)`$ replacement operations even when $`E`$ is small; weak polarization changes their capacity, not their number.

The result classifies controlled targets. A single autonomous reflection interval has an exact parity mixture and admits a one-query implementation. The additional specified interventions are part of the problem defined here.

The result fixes diamond error at $`0.01`$. No optimal dependence on a variable precision parameter is claimed. It also leaves the cost of known synthesis and the number of supplied controls outside the oracle count. These distinctions, along with the comparison to informative-noise metrology, are developed in [interpretation](interpretation.md) and [related work](../references/RELATED_WORK.md).
