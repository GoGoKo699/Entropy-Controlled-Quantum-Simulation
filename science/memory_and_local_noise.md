# Memory and local Hermitian noise

Independent one-spin dephasing gives an elementary sharpness example for the dimension dependence of [channel stability](channel_stability.md). A GHZ input and local parity readout suffice. The same family has an exact simulation algorithm and a matching query law, so its sensitivity and algorithmic costs can be compared directly.

This note also gives a construction using retained qubits and a limited number of pure resets. Its long-time behavior is sharp in the theorem's weighted Hermitian-jump metric. The required reduction of actual noise activity is stated explicitly; it does not imply the same lower bound for raw reflection queries.

## 1. Normalize the physical exposure

On $`n\geq1`$ spins, let

```math
B_j(\theta)=\cos\theta\,Z_j+\sin\theta\,X_j,
\qquad
\mathcal L_\theta=\frac1n\sum_{j=1}^n
\left(\operatorname{Ad}_{B_j(\theta)}-\mathrm{Id}\right).
```

Each jump is a Hermitian involution. The jumps commute because they act on different spins. The system dimension is $`d=2^n`$, the total rate is one, and physical local dephasing time is $`\tau=t/n`$.

For an opaque coherent SELECT over the $`n`$ reflections,

```math
\|\mathrm{SELECT}_\theta-\mathrm{SELECT}_0\|
=2|\sin(\theta/2)|\leq|\theta|.
```

The unknown common angle is supplied through the oracle, not as a classical matrix description. State preparation and readout below require no input-loading oracle.

Simultaneous local rate $`\gamma`$ on each spin instead gives

```math
\mathcal G_{\theta,\gamma}
=\gamma\sum_j(\operatorname{Ad}_{B_j(\theta)}-\mathrm{Id}),
\qquad \tau=\gamma T,\qquad t=n\gamma T.
```

Its total rate is $`n\gamma`$. In the weighted Hermitian-jump notation $`p_j=1/n`$, write $`H_j=\sqrt{n\gamma}\,B_j`$. The jump perturbation is then

```math
\eta=\sqrt{n\gamma}\,2|\sin(\theta/2)|.
```

Unit physical time at unit local rates and normalized time $`t=n`$ describe the same channel, with the corresponding rate and perturbation conversions.

## 2. Exact GHZ signal

Define $`|\pm_y\rangle=(|0\rangle\pm i|1\rangle)/\sqrt2`$, and prepare

```math
|\psi_n\rangle
=\frac{|+_y\rangle^{\otimes n}+i|-_y\rangle^{\otimes n}}{\sqrt2}.
```

Measure $`O=Z_1\cdots Z_n`$. A computational-basis GHZ with relative phase $`i`$, followed by $`SH`$ on each spin, prepares this input using $`O(n)`$ known gates. A nearest-neighbor CNOT chain suffices. Readout uses local $`Z`$ measurements followed by a classical XOR. No reference, intermediate control, reset, or environment measurement is used.

Set $`r=(1-e^{-2\tau})/2`$. The single-spin channel is exactly

```math
\mathcal D_{\theta,\tau}
=(1-r)\mathrm{Id}+r\operatorname{Ad}_{B(\theta)}.
```

Its adjoint sends $`Z`$ to $`aZ+bX`$, with

```math
a=1-2r\sin^2\theta,\qquad
b=2r\sin\theta\cos\theta.
```

In the $`Y`$ eigenbasis, $`aZ+bX`$ exchanges the two eigenvectors with amplitudes $`a\pm ib`$. The expectation is therefore

```math
\begin{aligned}
F_n(\theta,\tau)
&=\langle O\rangle_\theta
=\operatorname{Im}\bigl((1-r)+re^{2i\theta}\bigr)^n\\
&=\mathbb E_{K\sim\operatorname{Bin}(n,r)}\sin(2\theta K).
\end{aligned}
```

In particular,

```math
F_n(0,\tau)=0,\qquad
\partial_\theta F_n(0,\tau)=2nr=n(1-e^{-2\tau}).
```

At normalized time $`t=n`$, choose $`\theta=1/(2n)`$. Since $`0\leq K/n\leq1`$, concavity of sine gives

```math
F_n(1/(2n),1)
\geq\frac{1-e^{-2}}2\sin1>0.36.
```

This expectation difference lower-bounds both output trace norm and channel diamond norm. With $`\log d=n\log2`$ and $`\eta=2|\sin(\theta/2)|`$,

```math
\liminf_{\theta\to0}
\frac{\|e^{n\mathcal L_\theta}-e^{n\mathcal L_0}\|_\diamond}
{\sqrt{n\log d}\,\eta}
\geq\frac{1-e^{-2}}{\sqrt{\log2}}.
```

Thus the stability theorem's factor of order $`\sqrt{\log d}`$ is necessary even for commuting one-spin jumps. The entanglement is entirely in the sensor input; an external reference is unnecessary. This family uses $`n`$ jump types.

## 3. Entropy and the separable-probe comparison

At the zero-angle hypothesis, the $`2^n`$ vectors $`Z_S|\psi_n\rangle`$, indexed by subsets $`S\subseteq[n]`$, are orthonormal. Any nonempty proper product of $`Z_j`$ flips only part of a $`Y`$-basis branch and has zero overlap with the original GHZ support. The full product exchanges the two branches; their relative phase $`i`$ makes that overlap zero too.

The output eigenvalues are therefore the Bernoulli-product probabilities

```math
r^{|S|}(1-r)^{n-|S|},
```

and its entropy is exactly

```math
S\!\left(e^{t\mathcal L_0}
|\psi_n\rangle\langle\psi_n|\right)=n h(r).
```

At $`t=n`$, this uses a constant fraction of the maximum entropy $`n\log2`$. At infinite time it reaches that maximum. The calculation identifies the finite memory into which the noise deposits entropy.

A separable-probe bound shows the role of the GHZ input. For one site a Stinespring isometry is

```math
W_\theta
=\sqrt{1-r}\,|0\rangle_E\otimes I
+\sqrt r\,|1\rangle_E\otimes B_\theta.
```

For any one-site input, including a private reference, a common purification gives output root fidelity at least

```math
1-r(1-\cos\theta).
```

This follows by taking the real part of the purification overlap: $`B_0B_\theta=\cos\theta\,I+i\sin\theta\,Y`$. For a product of $`n`$ site-and-private-reference blocks, root fidelities multiply. The fidelity–trace-norm inequality yields

```math
\begin{aligned}
\|\rho_\theta-\rho_0\|_1
&\leq2\sqrt{1-[1-r(1-\cos\theta)]^{2n}}\\
&\leq2\sqrt{2nr(1-\cos\theta)}
\leq2\sqrt{nr}\,|\theta|.
\end{aligned}
```

Convexity extends this estimate to mixtures separable across those blocks, even with an arbitrary joint final measurement. The assumption concerns the joint input blocks, not merely a separable sensor marginal with an arbitrarily entangled reference. At $`\theta=\Theta(1/n)`$ and fixed $`\tau>0`$, such probes have vanishing output distance while the GHZ probe retains a constant gap.

## 4. Exact local-class query complexity

The commuting dissipators factor:

```math
e^{t\mathcal L_\theta}
=\prod_{j=1}^n
\left[(1-r)\mathrm{Id}+r\operatorname{Ad}_{B_j(\theta)}\right],
\qquad r=\frac{1-e^{-2t/n}}2.
```

Sample $`n`$ independent Bernoulli variables and apply each selected reflection once. This is an exact CPTP simulator with at most $`n`$ SELECT calls. A truncated rate-one Poisson trajectory uses $`O(t)`$ bounded calls at fixed error. Consequently the class has an $`O(\min\{t,n\})`$ upper bound for $`t\geq1`$.

The common-angle family proves the matching lower bound. Put

```math
\mu=nr=\Theta(\min\{t,n\}).
```

For $`\mu\geq1`$, choose $`\theta=1/(2\mu)`$. Taylor's theorem, $`|\sin''|\leq1`$, and $`\mathbb E(K/\mu)=1`$ give

```math
F_n(\theta,t/n)
=\mathbb E\sin(K/\mu)
\geq\sin1-\frac{1-r}{2\mu}
\geq\sin1-\frac12>0.34.
```

The SELECT distance is at most $`1/(2\mu)`$, so the ordinary oracle hybrid bound gives $`\Omega(\mu)`$ queries at diamond error $`0.01`$.

If $`\mu<1`$, take $`\theta=1/2`$. The inequality $`\sin x\geq x-x^3/6`$ for $`x\geq0`$, and the binomial moment bound

```math
\mathbb E K^3\leq\mu^3+3\mu^2+\mu\leq5\mu,
```

give $`F_n\geq\mu/6`$. For $`t\geq1`$, $`\mu\geq(1-e^{-2})/2`$, hence this gap exceeds $`0.07`$. Zero queries cannot attain error $`0.01`$. Since $`\min\{t,n\}`$ is bounded in this remaining regime, the same order follows:

```math
Q_{\mathrm{local}}(t,n,0.01)=\Theta(\min\{t,n\}),
\qquad t\geq1.
```

This is a worst-case bounded-query statement for full channel simulation. It holds against arbitrary coherent SELECT algorithms, not only trajectory samplers.

## 5. The long-time limit and the weighted metric

The fixed-rate family does not keep acquiring angular sensitivity at rate $`\sqrt{tn}`$ for $`t\gg n`$. With $`V_\theta=e^{-i\theta Y/2}`$,

```math
e^{t\mathcal L_\theta}
=\operatorname{Ad}_{V_\theta^{\otimes n}}\circ
e^{t\mathcal L_0}\circ
\operatorname{Ad}_{V_\theta^{\dagger\otimes n}}.
```

Thus, at every $`t`$,

```math
\|e^{t\mathcal L_\theta}-e^{t\mathcal L_0}\|_\diamond
\leq\min\{2,\,2n|\theta|,\,2t|\theta|\}.
```

Together with the exact derivative above, the angular sensitivity has order $`\min\{t,n\}`$.

For any chosen $`T\geq n`$, a different family with $`H_j(\theta)=gB_j(\theta)`$, $`g^2=n/T`$, and weights $`1/n`$ has local dephasing time one at $`T`$. Its perturbation is

```math
\eta=2g|\sin(\theta/2)|.
```

The same constant-gap angle $`\theta=1/(2n)`$ now gives $`\eta=\Theta(1/\sqrt{Tn})`$. This proves sharpness of the weighted $`\sqrt{T\log d}`$ metric for arbitrary $`T\geq n`$, using jumps of norm at most one.

The actual dissipative rate has been reduced to $`g^2`$. One may describe it using unit reflections of weights $`g^2/n`$, plus an identity jump of weight $`1-g^2`$; the inactive padding does not restore physical noise activity. The raw reflection SELECT changes by order $`\theta`$, so this example still gives only an $`\Omega(n)`$ raw-query lower bound. It is not a fixed-activity long-time amplification mechanism.

## 6. Retained qubits and a bounded count of pure resets

A related encoded construction makes the weighted dependence on memory and pure-reset count explicit. Suppose at most $`q\geq2`$ qubits are retained, at most $`R\geq0`$ individual pure-qubit resets are allowed, and $`T\geq1`$. Other controls are known and unital. Here $`R`$ is an integer; it is a different resource from the mixed-reset capacity in [the two-qubit protocol](mixed_resets.md).

Use $`n`$ sensor qubits and one logical flag. A known encoding maps

```math
|0\rangle_L\mapsto|+_y\rangle^{\otimes n}|0\rangle_L,
\qquad
|1\rangle_L\mapsto|-_y\rangle^{\otimes n}|1\rangle_L.
```

Starting with sensors in $`|0\rangle^{\otimes n}`$, controlled-NOT gates from the flag followed by $`SH`$ on the sensors implement this encoding in $`O(n)`$ gates. The identity

```math
B_\theta|\pm_y\rangle=e^{\pm i\theta}|\mp_y\rangle
```

means that a jump-parity pattern $`x\in\{0,1\}^n`$ produces a logical phase $`e^{i\theta|x|Z_L}`$. The inverse encoding is a known unitary decoder taking the sensor error sector to $`|x\rangle`$, with that phase on the flag. Every error pattern is retained; no syndrome is selected.

Choose $`B\geq1`$ blocks, each of duration $`T/B`$, and let

```math
M=nB,\qquad g^2=M/T\leq1,\qquad H_j=gB_j,\qquad p_j=1/n.
```

Each sensor has local dephasing time one in each block. Decode after each block. Between blocks, reset the $`n`$ sensors and re-encode. This uses exactly $`n(B-1)`$ individual pure resets. After the last block keep the syndrome register; there is no final uncharged erase.

With $`p=(1-e^{-2})/2`$, the reduced logical coherence is exactly

```math
(1-p+pe^{2i\theta})^M.
```

Starting the flag in $`|+\rangle`$, measure $`-Y_L`$. At $`\theta=1/(2M)`$, its expectation gap is at least $`p\sin1>0.36`$, by the same binomial calculation as before. The weighted perturbation is

```math
\eta=2g|\sin(\theta/2)|
=\Theta\!\left(\frac1{\sqrt{TM}}\right).
```

Here is an explicit choice covering all integer resources and real times:

```math
n=\min\{q-1,\lfloor T\rfloor\},
\qquad
B=\min\left\{1+\lfloor R/n\rfloor,\;\lfloor T/n\rfloor\right\}.
```

Both are positive integers, $`n+1\leq q`$, $`n(B-1)\leq R`$, and

```math
\frac14\min\{T,q+R\}\leq M=nB\leq\min\{T,q+R\}.
```

For the lower estimate, if $`n=\lfloor T\rfloor`$, then $`B=1`$ and $`n\geq T/2`$. Otherwise $`n=q-1`$, and the elementary floor bounds give $`M\geq\frac12\min\{T,R+n\}\geq\frac14\min\{T,R+q\}`$.

The [capacity bound](entropy_capacity.md) gives $`E_{\mathrm{used}}\leq R\log2`$ and $`\log D\leq q\log2`$. Channel stability and the bounded-jump linear-time estimate therefore upper-bound sensitivity by order

```math
\min\{T,\sqrt{T(q+R)}\}.
```

The construction reaches that order at a fixed nonzero output gap in the weighted Hermitian-jump metric.

When $`T\gg q+R`$, it does so by taking $`g^2=M/T\ll1`$. Actual dissipative activity is reduced. For the raw reflection oracle $`B_\theta`$, the change remains of order $`\theta`$, and its hybrid lower bound is $`\Omega(M)`$, not $`\Omega(\sqrt{T(q+R)})`$. The fixed-rate mixed-reset construction and this weighted pure-reset construction must be kept distinct.

## 7. Relation to existing metrology

Dephasing-axis estimation and entanglement-assisted measurement-basis discrimination are established subjects. [Wan and Lasenby](../references/RELATED_WORK.md#wan2022) discuss a changing Hermitian Pauli jump direction. [Kukita, Matsuzaki, and Kondo](../references/RELATED_WORK.md#kukita2021) use collective dephasing and GHZ states with repeated optimized interrogation; their collective jump norm and exposure accounting differ from the independent, total-rate-one family above. [Puchała et al.](../references/RELATED_WORK.md#puchala2021) study multiple-use discrimination of measurement channels, whose retained output must be distinguished from the complete dephasing channel here.

The encoded reset construction is related to informative-noise error correction [Chen et al.](../references/RELATED_WORK.md#chen2024), gauge resets [Liu and Zhou](../references/RELATED_WORK.md#liu2026), and coherent accumulation from mixed probes [Cable, Gu, and Modi](../references/RELATED_WORK.md#cable2016). The calculations above establish the stated sharpness and resource comparisons within these established sensing architectures.
