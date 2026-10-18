# Two-qubit Hermitian noise with adjustable mixed resets

A single unknown reflection on two retained qubits gives a sharp finite-distance example for the [controlled channel-stability theorem](channel_stability.md). The dissipative rate stays one. An adjustable replacement state changes the entropy removed by each control, while a logical qubit accumulates information about the reflection axis.

The exact output channel and the estimates below yield constant binary distinguishability at angular separation

```math
\Theta\!\left(\frac{1}{\min\{T,\sqrt{T(1+E)}\}}\right)
```

with total exposure $`T\geq1`$, retained dimension four, and control entropy capacity at most $`E\geq0`$. They also supply the lower-bound witness for the [controlled simulation query theorem](query_complexity.md). The [model conventions](model.md) specify the target-channel contract and oracle access.

## 1. A local-noise implementation

Let $`S`$ be a syndrome qubit and $`L`$ a logical qubit. Define

```math
\begin{aligned}
U_\theta
&=|0\rangle\langle1|_S\otimes e^{i\theta Z_L}
 +|1\rangle\langle0|_S\otimes e^{-i\theta Z_L}\\
&=\cos\theta\,X_S\otimes I_L-\sin\theta\,Y_S\otimes Z_L.
\end{aligned}
```

The two Pauli terms anticommute, so $`U_\theta^\dagger=U_\theta`$ and $`U_\theta^2=I`$. Moreover,

```math
\|U_\theta-U_{\theta'}\|
=2\left|\sin\frac{\theta-\theta'}2\right|
\leq|\theta-\theta'|.
```

The generator is

```math
\mathcal L_\theta=\mathrm{Ad}_{U_\theta}-\mathrm{Id}
=-\frac12[U_\theta,[U_\theta,\cdot]].
```

It has one reflection jump, total rate one, and zero Hamiltonian.

Let $`C`$ be the fixed CNOT with $`L`$ as control and $`S`$ as target. Since $`CX_SC=X_S`$ and $`CY_SC=Y_SZ_L`$,

```math
U_\theta
=C\bigl[(\cos\theta\,X_S-\sin\theta\,Y_S)\otimes I_L\bigr]C.
```

Thus each encoded interval can be implemented by a known CNOT, single-qubit dephasing along the unknown axis on $`S`$, and a known CNOT. The other physical qubit is noiseless during that interval. The replacement described below is performed in the encoded tensor-product basis. This implementation uses a constant number of known gates per interval; it supplies no bath trajectory or measurement record.

## 2. Exact cycle and output

For $`0\leq b\leq1`$, let

```math
\tau_b=\frac{I+bZ}{2},
\qquad
\mathcal R_b(\rho_{SL})=\tau_b\otimes\mathrm{Tr}_S\rho_{SL}.
```

The target consists of $`N`$ intervals of duration $`\Delta>0`$, each followed by $`\mathcal R_b`$:

```math
\mathcal P_{\theta,b,N,\Delta}
=\left(\mathcal R_b\circ e^{\Delta\mathcal L_\theta}\right)^N,
\qquad T=N\Delta.
```

There are exactly $`N`$ charged replacement controls, including the terminal one. For the distinguishability witness, choose the same known input $`\tau_b\otimes|+\rangle\langle+|_L`$ under both hypotheses. This is a witness input to the full-channel problem, not an uncharged target replacement of an arbitrary input.

The involution identity gives

```math
e^{\Delta\mathcal L_\theta}
=(1-p)\mathrm{Id}+p\mathrm{Ad}_{U_\theta},
\qquad p=\frac{1-e^{-2\Delta}}2.
```

On an input $`\tau_b\otimes\rho_L`$, one cycle outputs $`\tau_b\otimes\mathcal F_{\theta,b}(\rho_L)`$, where

```math
\begin{aligned}
\mathcal F_{\theta,b}(\rho)
={}&(1-p)\rho\\
&+\frac{p(1+b)}2 e^{-i\theta Z}\rho e^{i\theta Z}
+\frac{p(1-b)}2 e^{i\theta Z}\rho e^{-i\theta Z}.
\end{aligned}
```

In particular, a logical off-diagonal element is multiplied by

```math
f_b(\theta)=1-p+p\cos(2\theta)-ipb\sin(2\theta).
```

After $`N`$ cycles the logical state is exactly

```math
\rho_L(\theta)
=\frac12
\begin{pmatrix}
1&f_b(\theta)^N\\
\overline{f_b(\theta)}^{\,N}&1
\end{pmatrix},
```

and therefore

```math
\|\rho_L(\theta)-\rho_L(0)\|_1
=|f_b(\theta)^N-1|.
```

The complete retained output is $`\tau_b\otimes\rho_L(\theta)`$, with the same trace-norm gap. Every expression concerns the unconditioned CPTP output.

## 3. Entropy capacity and its actual use

Use natural logarithms and define

```math
h(x)=-x\log x-(1-x)\log(1-x),
\qquad
e(b)=\log2-h\!\left(\frac{1+b}{2}\right).
```

The [entropy-decrease capacity](entropy_capacity.md) of one replacement is exactly

```math
\kappa(\mathcal R_b)=e(b).
```

Indeed,

```math
S(\rho_{SL})-S(\mathcal R_b\rho_{SL})
=S(S|L)_\rho-S(\tau_b)
\leq\log2-S(\tau_b).
```

The product input $`I_S/2\otimes\rho_L`$ attains equality. Adding an untouched reference gives the same maximum. Consequently the target budget is

```math
E_{\mathrm{used}}=Ne(b).
```

Differentiating $`e`$, expanding $`\mathrm{arctanh}b`$, and integrating gives

```math
e(b)=\sum_{k=1}^{\infty}
\frac{b^{2k}}{(2k-1)(2k)}.
```

The endpoint $`b=1`$ follows by continuity. This positive series implies the uniform bounds

```math
\frac{b^2}{2}\leq e(b)\leq(\log2)b^2.
```

The capacity is substantially used on the baseline hypothesis. At $`\theta=0`$, the logical state is unchanged, while an interval sends $`\tau_b`$ to $`\tau_{ab}`$, with $`a=e^{-2\Delta}`$. The entropy actually removed by the following replacement is $`e(b)-e(ab)`$. Termwise comparison of the series gives

```math
(1-a^2)e(b)\leq e(b)-e(ab)\leq e(b).
```

Hence the actual baseline entropy removed over the target is between

```math
(1-e^{-4\Delta})E_{\mathrm{used}}
\quad\text{and}\quad E_{\mathrm{used}}.
```

For intervals of duration at least one, this is at least $`(1-e^{-4})E_{\mathrm{used}}`$. Small $`E_{\mathrm{used}}`$ means weakly polarized replacements; it does not mean few replacement operations. At $`b=0`$, the map is unital and its capacity is exactly zero.

## 4. Uniform finite separation

Set $`p_0=(1-e^{-2})/2`$. First suppose $`p\in[p_0,1/2]`$ and $`Nb^2\geq1`$. Choose

```math
\theta=\frac{1}{2Nb}.
```

Then $`0<2\theta\leq1`$. Write $`f_b=A-iB`$, with $`A>0`$, $`B\geq0`$. Since

```math
A=1-p(1-\cos2\theta)
\geq1-2p\theta^2
\geq1-\frac{p}{2N},
```

Bernoulli's inequality gives

```math
|f_b|^N\geq A^N\geq1-\frac p2\geq\frac34.
```

Also $`\sin2\theta\geq\theta`$, $`B\leq2pb\theta=p/N`$, and $`B/A<1`$. If $`\phi=\arctan(B/A)`$, then

```math
\frac p4
\leq N\phi
\leq\frac{p}{1-p/2}
\leq\frac23<\frac{\pi}{2}.
```

The lower inequality uses $`\arctan x\geq x/2`$ for $`0\leq x\leq1`$. Thus

```math
\begin{aligned}
|f_b(\theta)^N-1|
&\geq|\mathrm{Im}f_b(\theta)^N|\\
&\geq(1-p/2)\sin(p/4)\\
&\geq\frac34\sin(p_0/4)>0.08.
\end{aligned}
```

For $`\Delta=1`$, the sharper displayed expression $`(1-p_0/2)\sin(p_0/4)`$ exceeds $`0.084`$. The uniform $`0.08`$ threshold suffices throughout.

For zero polarization choose instead

```math
b=0,\qquad \theta=\frac{1}{2\sqrt N}.
```

Now $`f_0=1-2p\sin^2\theta`$ is real and positive. Using $`\sin\theta\geq2\theta/\pi`$,

```math
1-f_0(\theta)^N
\geq1-\exp(-2p/\pi^2)
\geq1-\exp(-2p_0/\pi^2)>0.08.
```

This signal is a second-order change of logical dephasing at the baseline. Its finite separation does not require a nonzero first derivative.

The witnesses have simple readout: measure $`X_L`$ in the zero-polarization case and $`Y_L`$ in the positive-polarization case. The latter expectation equals $`-\mathrm{Im}f_b^N`$. With equal priors and the corresponding decision rule, an expectation gap greater than $`0.08`$ gives success probability greater than $`1/2+0.08/4=0.52`$. No repetitions or retained outcome history are implicit.

## 5. Every real exposure time and every supplied budget

For any real $`T\geq1`$, choose

```math
N=\lfloor T\rfloor,\qquad
\Delta=T/N\in[1,2).
```

Then $`T/2\leq N\leq T`$ and $`p\in[p_0,1/2]`$, so all finite bounds above apply. There is no additional remainder interval.

| Supplied capacity bound | Polarization | Used capacity | Separation angle |
|---|---|---|---|
| $`0\leq E<\log2`$ | $`b=0`$ | $`0`$ | $`1/(2\sqrt N)`$ |
| $`\log2\leq E\leq N\log2`$ | $`b^2=E/(N\log2)`$ | $`Ne(b)\leq E`$ | $`1/(2Nb)`$ |
| $`E\geq N\log2`$ | $`b=1`$ | $`N\log2\leq E`$ | $`1/(2N)`$ |

The inverse angle is uniformly of order $`\min\{T,\sqrt{T(1+E)}\}`$, including $`1\leq T<2`$. In the middle regime, $`Nb^2\geq1`$ and $`Nb=\sqrt{NE/\log2}`$.

For a general target in this fixed-dimensional reflection model with operator-norm Lipschitz constant at most one in its angle, the controlled stability theorem and the elementary linear-time bound give

```math
\|\mathcal P_\theta-\mathcal P_{\theta'}\|_\diamond
\leq
\min\!\left\{
2,\;2T|\theta-\theta'|,\;
|\theta-\theta'|\sqrt T
\left[1+\sqrt{4\log4+2E}\right]
\right\}.
```

A fixed nonzero binary advantage therefore requires separation at least a constant times the reciprocal scale achieved above. This is a finite-distance discrimination statement; it is not a quantum-Fisher-information claim or an assertion about arbitrary estimator risk.

In the oracle simulation problem, $`\theta`$ is hidden in the supplied controlled reflection. Its operator distance from the baseline oracle is at most $`|\theta|`$. A $`q`$-query simulator has endpoint output gap at most $`2q|\theta|`$, even with arbitrary workspace and known interleavings. Two diamond approximation errors of $`0.01`$ consume at most $`0.02`$ of the target's $`0.08`$ gap. Thus $`q>0.03/|\theta|`$. The full matching upper and the precise query theorem are given in [query complexity](query_complexity.md).

## 6. Physical resources and related mechanisms

The protocol retains two qubits, prepares a known constant-size input, and uses $`N`$ known replacements and $`O(N)`$ known CNOT gates in the local-noise implementation. No QRAM, bath monitoring, postselection, or adaptive estimate is used. The capacity measures possible entropy removal from the retained system; it is not a work or temperature accounting for the reset apparatus.

Turning informative noise into coherent signal through error correction has a direct predecessor in [Chen et al.](../references/RELATED_WORK.md#chen2024). Gauge-reset architectures are also studied by [Liu and Zhou](../references/RELATED_WORK.md#liu2026), and phase accumulation from weakly polarized probes appears in [Cable, Gu, and Modi](../references/RELATED_WORK.md#cable2016). [Wan and Lasenby](../references/RELATED_WORK.md#wan2022) explicitly discuss parameter-dependent Hermitian dephasing directions. The exact calculation here provides a normalized finite-distance witness for the entropy-capacity theorem using these established metrological mechanisms.
