# Stability of Hermitian noise under common controls

This file proves a complete-channel perturbation bound for Hermitian Lindblad jumps, including arbitrary untouched references, a common time-dependent Hamiltonian, and known CPTP controls between noisy intervals. The control resource is the [entropy-decrease capacity](entropy_capacity.md); the oracle consequence is proved in [query complexity](query_complexity.md).

The proof uses relative-entropy data processing and quantum Pinsker, whose natural-logarithm conventions are documented under [Watrous](../references/RELATED_WORK.md#watrous2018) and [Lindblad](../references/RELATED_WORK.md#lindblad1975). Every factor needed in the commutator, entropy, and variance estimates is derived below.

<a id="main-theorem"></a>

## 1. Statement

Let the retained system $`A`$ have dimension $`D`$. It includes every quantum register and every classical record retained during interrogation, as specified in the [model](model.md). A separate finite-dimensional reference $`R`$ is untouched.

On the noisy intervals, consider two time-dependent generators

```math
\begin{aligned}
\mathcal L_A(s)(X)
&=-i[K(s),X]
-\frac12\sum_{j=1}^{m}p_j(s)[A_j(s),[A_j(s),X]],\\
\mathcal L_B(s)(X)
&=-i[K(s),X]
-\frac12\sum_{j=1}^{m}p_j(s)[B_j(s),[B_j(s),X]].
\end{aligned}
```

The matrices $`A_j(s),B_j(s),K(s)`$ are Hermitian. The common weights satisfy $`p_j(s)\geq0`$ and $`\sum_jp_j(s)=1`$. Bounded, piecewise continuous matrices and weights, with a finite number of jumps and a finite number of control boundaries, are sufficient.

The two protocols have the same control times and the same parameter-independent CPTP maps $`\mathcal C_0,\ldots,\mathcal C_r`$, including any initial or terminal control. Put

```math
\begin{aligned}
E_{\mathrm{used}}
&=\sum_{k=0}^{r}\kappa(\mathcal C_k)\leq E,\\
V^2
&=\int_0^T\sum_jp_j(s)
\|A_j(s)-B_j(s)\|_{\mathrm{op}}^2\,ds.
\end{aligned}
```

Let $`\Phi_A,\Phi_B`$ be the resulting complete, unconditioned channels on the retained system.

**Theorem.**

```math
\boxed{
\|\Phi_A-\Phi_B\|_\diamond
\leq
V\left[1+\sqrt{4\log D+2E}\right].
}
```

The diamond norm is the unhalved norm. The trivial upper bound two is always available. The estimate requires no spectral gap, rapid mixing, locality, common fixed-point algebra, commutativity, or involution property. Although finite-dimensional generators are assumed bounded on the time interval, the displayed constant does not depend on a bound for the common base-jump norms or the common Hamiltonian.

For constant jumps and no intermediate controls, write

```math
\eta^2=\sum_jp_j\|A_j-B_j\|_{\mathrm{op}}^2.
```

Then the theorem specializes to

```math
\boxed{
\|e^{T\mathcal L_A}-e^{T\mathcal L_B}\|_\diamond
\leq\eta\sqrt T\left(1+2\sqrt{\log D}\right),
}
```

where a common constant Hamiltonian may be included in the two generators.

<a id="unitary-curve"></a>

## 2. Entropy production controls a state commutator

For a Hermitian matrix $`H`$, define

```math
\mathcal D_H(X)
=-\frac12[H,[H,X]]
=HXH-\frac12\{H^2,X\}.
```

For a full-rank state $`\rho`$, define the entropy-production rate

```math
\sigma_H(\rho)
=-\operatorname{Tr}\mathcal D_H(\rho)\log\rho.
```

### 2.1 Quantum Pinsker with natural logarithms

For states $`\alpha,\beta`$, natural-logarithm relative entropy satisfies

```math
D(\alpha\|\beta)
\geq\frac12\|\alpha-\beta\|_1^2.
```

Here is the coefficient calculation. Measure the projector onto the positive part of $`\alpha-\beta`$, and let the two “positive” probabilities be $`p,q`$. Because $`\operatorname{Tr}(\alpha-\beta)=0`$,

```math
p-q=\frac12\|\alpha-\beta\|_1.
```

Relative-entropy data processing bounds the quantum relative entropy below by binary relative entropy

```math
d(p\|q)
=p\log\frac pq+(1-p)\log\frac{1-p}{1-q}.
```

For fixed $`0<q<1`$, the function
$`d(p\|q)-2(p-q)^2`$ has value and first derivative zero at $`p=q`$, and second derivative

```math
\frac1{p(1-p)}-4\geq0.
```

It is therefore nonnegative. Boundary cases follow by continuity or infinite relative entropy. Thus $`d(p\|q)\geq2(p-q)^2`$, proving the stated quantum coefficient. In base-two entropy the coefficient is $`1/(2\log2)`$ instead; the natural-logarithm convention is used throughout this project.

### 2.2 Expand the unitary curve

Let

```math
\rho_x=e^{ixH}\rho e^{-ixH}.
```

Its expansion is

```math
\rho_x
=\rho+ix[H,\rho]
-\frac{x^2}{2}[H,[H,\rho]]
+O(x^3).
```

Unitary conjugation preserves entropy, so

```math
D(\rho_x\|\rho)
=\operatorname{Tr}\rho\log\rho
-\operatorname{Tr}\rho_x\log\rho.
```

The linear term vanishes:

```math
\operatorname{Tr}[H,\rho]\log\rho
=\operatorname{Tr}H[\rho,\log\rho]=0.
```

The quadratic coefficient is

```math
\frac12\operatorname{Tr}[H,[H,\rho]]\log\rho
=\sigma_H(\rho).
```

Consequently,

```math
D(\rho_x\|\rho)
=x^2\sigma_H(\rho)+O(x^3).
```

Also, continuity of the trace norm gives

```math
\frac{\|\rho_x-\rho\|_1}{|x|}
\longrightarrow
\|[H,\rho]\|_1.
```

Apply quantum Pinsker, divide by $`x^2`$, and let $`x\to0`$. This proves the lemma

```math
\boxed{
\|[H,\rho]\|_1^2\leq2\sigma_H(\rho).
}
```

The same proof applies on a system and reference, with $`H`$ replaced by $`H\otimes I_R`$. Singular states are treated by the regularization in Section 7.

### 2.3 Entropy derivative during a noisy interval

For a full-rank differentiable state, trace preservation gives

```math
\frac{d}{ds}S(\rho_s)
=-\operatorname{Tr}\dot\rho_s\log\rho_s.
```

The common Hamiltonian contributes zero, because

```math
\operatorname{Tr}[K,\rho_s]\log\rho_s
=\operatorname{Tr}K[\rho_s,\log\rho_s]=0.
```

For Hermitian jumps $`H_j(s)`$,

```math
\frac{d}{ds}S(\rho_s)
=\sum_jp_j(s)\sigma_{H_j(s)}(\rho_s)\geq0.
```

Integrating the commutator lemma over all noisy intervals therefore yields

```math
\int_0^T\sum_jp_j(s)
\|[H_j(s),\rho_s]\|_1^2\,ds
\leq2\Delta S_{\mathrm{noise}},
```

where $`\Delta S_{\mathrm{noise}}`$ is the sum of entropy increases during those intervals. Instantaneous controls are excluded from this integral and accounted for separately.

<a id="weighted-cauchy-schwarz"></a>

## 3. The two commutator estimates

Let $`O,H,F`$ be Hermitian, $`\|O\|_{\mathrm{op}}\leq1`$, and let $`\rho`$ be a state.

### 3.1 The term involving the forward state

Cyclicity of the trace gives

```math
\operatorname{Tr}O[F,[H,\rho]]
=\operatorname{Tr}[O,F][H,\rho].
```

The trace/operator Hölder inequality and the elementary commutator bound give

```math
\begin{aligned}
\frac12\left|
\operatorname{Tr}O[F,[H,\rho]]
\right|
&\leq
\frac12\|[O,F]\|_{\mathrm{op}}
\|[H,\rho]\|_1\\
&\leq
\|F\|_{\mathrm{op}}\|[H,\rho]\|_1.
\end{aligned}
```

### 3.2 The term involving the backward observable

Put $`C=[O,H]`$. It is anti-Hermitian, so
$`CC^\dagger=C^\dagger C`$. Cyclicity now gives

```math
\operatorname{Tr}O[H,[F,\rho]]
=\operatorname{Tr}\rho[C,F].
```

The state-weighted inner product

```math
\langle X,Y\rangle_\rho
=\operatorname{Tr}\rho X^\dagger Y
```

obeys Cauchy–Schwarz. This follows from the Hilbert–Schmidt inner product of $`X\rho^{1/2}`$ and $`Y\rho^{1/2}`$, and remains valid when it is only semidefinite. Applying it twice,

```math
\begin{aligned}
|\operatorname{Tr}\rho CF|
&\leq
\sqrt{\operatorname{Tr}\rho CC^\dagger}
\sqrt{\operatorname{Tr}\rho F^2},\\
|\operatorname{Tr}\rho FC|
&\leq
\sqrt{\operatorname{Tr}\rho C^\dagger C}
\sqrt{\operatorname{Tr}\rho F^2}.
\end{aligned}
```

The two commutator orders agree because $`C`$ is anti-Hermitian. Taking half their sum and using $`\operatorname{Tr}\rho F^2\leq\|F\|_{\mathrm{op}}^2`$ proves

```math
\boxed{
\frac12\left|
\operatorname{Tr}O[H,[F,\rho]]
\right|
\leq
\|F\|_{\mathrm{op}}
\sqrt{
\operatorname{Tr}\rho[H,O]^\dagger[H,O]
}.
}
```

### 3.3 Sum over time and jumps

For nonnegative functions $`a_j(s),b_j(s)`$,

```math
\begin{aligned}
\int_0^T\sum_jp_j(s)a_j(s)b_j(s)\,ds
\leq{}&
\left(\int_0^T\sum_jp_j(s)a_j(s)^2\,ds\right)^{1/2}\\
&\times
\left(\int_0^T\sum_jp_j(s)b_j(s)^2\,ds\right)^{1/2}.
\end{aligned}
```

This is ordinary Cauchy–Schwarz for the measure $`p_j(s)\,ds`$ on time and jump index. Both estimates below use $`a_j(s)=\|A_j(s)-B_j(s)\|_{\mathrm{op}}`$, whose squared integral is $`V^2`$.

## 4. Interpolation and the entropy budget

Define

```math
F_j(s)=B_j(s)-A_j(s),
\qquad
H_j(u,s)=A_j(s)+uF_j(s),
\qquad 0\leq u\leq1.
```

Let $`\mathcal L_u(s)`$ use these Hermitian jumps and the same common Hamiltonian. Every intermediate noisy propagator is CPTP and unital. In particular, reflection endpoints may be interpolated through Hermitian matrices that are not reflections. This is an analytic path; no implementation of its intermediate generators is assumed.

Fix $`u`$, an arbitrary joint input $`\rho_{\mathrm{in}}`$, and a terminal Hermitian observable $`O`$ with norm at most one. Let $`\rho_s`$ be the forward joint state in the complete interpolated protocol. Let $`O_s`$ be the observable propagated backward through every future interval and control using the actual adjoint maps. Future maps are CPTP, so their adjoints are unital completely positive and

```math
\|O_s\|_{\mathrm{op}}\leq1.
```

All operators on the retained system below implicitly tensor with the identity on the reference.

Differentiating the finite product of propagators and controls, using Duhamel's formula inside each noisy interval, gives

```math
\frac{d}{du}\operatorname{Tr}O\,
(\Phi_u\otimes\operatorname{Id}_R)(\rho_{\mathrm{in}})
=
\sum_{\mathrm{intervals}}\int
\operatorname{Tr}O_s\,\dot{\mathcal L}_u(s)(\rho_s)\,ds,
```

with

```math
\dot{\mathcal L}_u(s)(X)
=-\frac12\sum_jp_j(s)
\left(
[F_j(s),[H_j(u,s),X]]
+[H_j(u,s),[F_j(s),X]]
\right).
```

The common Hamiltonian, weights, and controls have zero derivative with respect to $`u`$.

Let $`\rho_{k,-}`$ and $`\rho_{k,+}`$ denote the joint states immediately before and after control $`\mathcal C_k`$. Entropy changes telescope across the whole protocol:

```math
\Delta S_{\mathrm{noise}}
=
S(\rho_{\mathrm{out}})-S(\rho_{\mathrm{in}})
-\sum_{k=0}^{r}
\left[S(\rho_{k,+})-S(\rho_{k,-})\right].
```

The reference marginal never changes. Subadditivity and the Araki–Lieb inequality give

```math
-\log D\leq S(A\mid R)\leq\log D.
```

Hence $`S(\rho_{\mathrm{out}})-S(\rho_{\mathrm{in}})\leq2\log D`$. By [reference invariance of capacity](entropy_capacity.md#reference-invariance), each negative control entropy change is at most $`\kappa(\mathcal C_k)`$. Therefore

```math
0\leq\Delta S_{\mathrm{noise}}
\leq2\log D+E.
```

Section 2 and the first estimate of Section 3 now imply that the integrated forward-state term in the Duhamel derivative is at most

```math
\begin{aligned}
&\int_0^T\sum_jp_j(s)
\|F_j(s)\|_{\mathrm{op}}
\|[H_j(u,s),\rho_s]\|_1\,ds\\
&\hspace{1cm}\leq
V\sqrt{2\Delta S_{\mathrm{noise}}}
\leq V\sqrt{4\log D+2E}.
\end{aligned}
```

No factor equal to the number of controls appears.

## 5. A matched variance budget survives CPTP controls

On an open noisy interval, the forward state and backward observable obey

```math
\dot\rho_s=\mathcal L_u(s)(\rho_s),
\qquad
\dot O_s=-\mathcal L_u(s)^\dagger(O_s).
```

Define

```math
g(s)=\operatorname{Tr}\rho_sO_s^2.
```

Differentiating both factors gives

```math
g'(s)
=\operatorname{Tr}\rho_s
\left[
\mathcal L_u^\dagger(O_s^2)
-\mathcal L_u^\dagger(O_s)O_s
-O_s\mathcal L_u^\dagger(O_s)
\right].
```

The Hamiltonian part of $`\mathcal L_u^\dagger`$ is $`i[K,\cdot]`$ and contributes zero by the Leibniz rule. For each Hermitian dissipator, expansion gives

```math
\begin{aligned}
&\mathcal D_H(O^2)-\mathcal D_H(O)O-O\mathcal D_H(O)\\
&\quad=
HO^2H-HOHO-OHOH+OH^2O\\
&\quad=[H,O]^\dagger[H,O].
\end{aligned}
```

Thus, during a noisy interval,

```math
g'(s)
=
\operatorname{Tr}\rho_s
\sum_jp_j(s)
[H_j(u,s),O_s]^\dagger[H_j(u,s),O_s]
\geq0.
```

### The jump at a control boundary

At a control $`\mathcal C`$,

```math
\rho_+=(\mathcal C\otimes\operatorname{Id}_R)(\rho_-),
\qquad
O_-=(\mathcal C^\dagger\otimes\operatorname{Id}_R)(O_+).
```

Writing $`\Psi=\mathcal C^\dagger\otimes\operatorname{Id}_R`$,

```math
g_+-g_-
=
\operatorname{Tr}\rho_-
\left[\Psi(O_+^2)-\Psi(O_+)^2\right]\geq0.
```

For completeness, the operator inequality follows from complete positivity and unitality of $`\Psi`$. Apply its two-by-two matrix amplification to the positive block matrix

```math
\begin{pmatrix}
O_+^2&O_+\\
O_+&I
\end{pmatrix}\geq0.
```

The image has lower-right block $`I`$. Its Schur complement is $`\Psi(O_+^2)-\Psi(O_+)^2\geq0`$. This is the Kadison–Schwarz inequality in the form required here.

The variance changes therefore telescope with nonnegative contributions both in noisy intervals and at all controls, including initial and terminal controls. Since

```math
0\leq g_{\mathrm{in}},
\qquad
g_{\mathrm{out}}
=\operatorname{Tr}\rho_{\mathrm{out}}O^2\leq1,
```

the integrated noisy contribution satisfies

```math
\boxed{
\int_0^T\sum_jp_j(s)
\operatorname{Tr}\rho_s
[H_j(u,s),O_s]^\dagger[H_j(u,s),O_s]\,ds
\leq1.
}
```

Use the second estimate and weighted Cauchy–Schwarz from Section 3. The integrated backward-observable term in the Duhamel derivative is at most $`V`$.

## 6. Finish the channel bound

Combining Sections 4 and 5 gives, for each interpolation value, joint input, and terminal witness,

```math
\left|
\frac{d}{du}\operatorname{Tr}O\,
(\Phi_u\otimes\operatorname{Id}_R)(\rho_{\mathrm{in}})
\right|
\leq
V\left[1+\sqrt{4\log D+2E}\right].
```

Integrate over $`u\in[0,1]`$ and optimize the final Hermitian witness. Since the difference of output states is Hermitian, trace-norm duality gives

```math
\left\|
((\Phi_A-\Phi_B)\otimes\operatorname{Id}_R)(\rho_{\mathrm{in}})
\right\|_1
\leq
V\left[1+\sqrt{4\log D+2E}\right].
```

### Why optimization over states gives the full diamond norm

There is no additional factor of two in this step. Here is a direct argument. Let $`\Lambda`$ be a Hermiticity-preserving map, and suppose the displayed bound holds on all joint states with arbitrary finite references.

For an arbitrary operator $`X`$ with $`\|X\|_1=1`$, introduce an additional reference qubit and form the Hermitian block matrix

```math
Y=\frac12
\begin{pmatrix}
0&X\\
X^\dagger&0
\end{pmatrix}.
```

Then $`\|Y\|_1=1`$, and Hermiticity preservation implies

```math
\|(\Lambda\otimes\operatorname{Id})(Y)\|_1
=\|(\Lambda\otimes\operatorname{Id})(X)\|_1.
```

Decompose $`Y=Y_+-Y_-`$. The positive traces sum to one. A bound on normalized positive inputs therefore bounds the image of $`Y`$ by the triangle inequality with the same constant. Thus a state bound controls the definition of the diamond norm over all trace-norm-one operators.

Moreover, convexity reduces state optimization to pure states. Every pure state on $`A\otimes R`$ has Schmidt rank at most $`D`$, so a reference of dimension $`D`$ suffices after an isometry on the reference. The map $`\Phi_A-\Phi_B`$ is Hermiticity preserving, so the argument applies. These standard diamond-norm facts are also discussed in [Watrous](../references/RELATED_WORK.md#watrous2018).

<a id="singular-states"></a>

## 7. Singular inputs and pure resets

The entropy expansions above assumed full rank. Regularizing only the initial state would be insufficient because a later pure reset can create a singular state.

Fix a finite reference dimension $`d_R`$. For $`0<\epsilon<1`$, replace the input by

```math
\rho_{\mathrm{in}}^{(\epsilon)}
=(1-\epsilon)\rho_{\mathrm{in}}
+\epsilon\,\frac{I_{A\otimes R}}{Dd_R},
```

and replace every control by

```math
\mathcal C_k^{(\epsilon)}
=(1-\epsilon)\mathcal C_k+\epsilon\mathcal D_D.
```

The reference marginal $`\rho_R^{(\epsilon)}`$ is full rank and remains fixed. At any regularized control,

```math
(\mathcal C_k^{(\epsilon)}\otimes\operatorname{Id}_R)(\rho)
\geq
\epsilon\,\frac{I_A}{D}\otimes\rho_R^{(\epsilon)}
>0.
```

Noisy interval propagators, including the common Hamiltonian, are unital on $`A`$ and leave this positive product floor invariant. Hence every state entering the entropy differentiation is full rank.

By [convexity of capacity](entropy_capacity.md),

```math
\sum_k\kappa(\mathcal C_k^{(\epsilon)})
\leq(1-\epsilon)\sum_k\kappa(\mathcal C_k)
\leq E.
```

The established bound is therefore uniform in $`\epsilon`$. Each control changes in diamond norm by at most $`2\epsilon`$. Since the sequence is finite, telescoping and CPTP contractivity show that its regularized channel converges in diamond norm to the original channel. The input mixture also converges in trace norm. Taking $`\epsilon\to0`$ proves the theorem for the original controls and arbitrary, possibly singular, inputs.

## 8. State-dependent form and elementary caps

### A specified initial state

For an input $`\rho_{AR}`$, the entropy argument can use the stronger estimate

```math
\Delta S_{\mathrm{noise}}
\leq \log D-S(A\mid R)_\rho+E.
```

The same proof then gives

```math
\left\|
((\Phi_A-\Phi_B)\otimes\operatorname{Id}_R)(\rho)
\right\|_1
\leq
V\left[
1+\sqrt{2\bigl(\log D-S(A\mid R)_\rho+E\bigr)}
\right].
```

Without a reference, replace conditional entropy by the input entropy. The diamond-norm theorem uses the worst allowed conditional entropy $`-\log D`$.

### Reflection endpoints

If every endpoint jump is a Hermitian unitary involution, then

```math
\mathcal D_A=\operatorname{Ad}_A-\operatorname{Id}.
```

For any unitaries $`A,B`$,

```math
\operatorname{Ad}_A(X)-\operatorname{Ad}_B(X)
=(A-B)XA^\dagger+BX(A^\dagger-B^\dagger).
```

The multiplication bounds hold with any reference, giving

```math
\|\operatorname{Ad}_A-\operatorname{Ad}_B\|_\diamond
\leq2\|A-B\|_{\mathrm{op}}.
```

Duhamel's formula on each interval and contractivity through the common controls imply

```math
\|\Phi_A-\Phi_B\|_\diamond
\leq
2\int_0^T\sum_jp_j(s)
\|A_j(s)-B_j(s)\|_{\mathrm{op}}\,ds.
```

### General norm-at-most-one Hermitian endpoints

If $`\|A\|_{\mathrm{op}},\|B\|_{\mathrm{op}}\leq1`$, the difference of the terms $`AXA`$ and $`BXB`$ has diamond norm at most $`2\|A-B\|_{\mathrm{op}}`$. The difference of the anticommutator terms has norm at most

```math
\|A^2-B^2\|_{\mathrm{op}}
\leq2\|A-B\|_{\mathrm{op}}.
```

Thus

```math
\|\mathcal D_A-\mathcal D_B\|_\diamond
\leq4\|A-B\|_{\mathrm{op}},
```

and the preceding integral bound holds with factor four. These bounds can be combined with the theorem and the trivial upper bound two.

## 9. Consequences used in the query theorem

For a single static reflection $`U`$ and a fitted reflection $`U'`$, under the same specified controls,

```math
\boxed{
\|\Phi_U-\Phi_{U'}\|_\diamond
\leq
\sqrt T\,\|U-U'\|_{\mathrm{op}}
\left[1+\sqrt{4\log D+2E}\right].
}
```

This is the stability estimate used by the [learning upper bound](query_complexity.md#learning-upper-bound).

For $`q`$ retained qubits and controls consisting of unital operations and at most $`R`$ individual pure-qubit resets,

```math
\|\Phi_A-\Phi_B\|_\diamond
\leq
V\left[1+\sqrt{(4q+2R)\log2}\right].
```

The [mixed-reset example](mixed_resets.md) gives a matching fixed-dimensional dependence on the control capacity at normalized rate one. The [local-noise examples](memory_and_local_noise.md) explain the role of retained dimension and the normalization of a separate pure-reset-count construction.

The theorem is a finite-distance statement about complete channels. It does not identify trace-norm derivatives with quantum Fisher information at rank-changing states. The source-by-source comparison with entropy-gain, convexity, and adaptive-metrology results is in [related work](../references/RELATED_WORK.md).
