# Model and principal results

An unknown noise operator can be queried as a unitary, while the evolution it generates is an open-system channel. Simulating that channel means reproducing its action on every input, including an input entangled with an inaccessible reference. This project asks how known operations performed during the target evolution change the number of unknown-unitary queries required.

The control resource is the amount of entropy a prescribed operation can remove from the retained system. At fixed target dimension, that resource determines a sharp crossover from square-root to linear query cost. The [entropy-capacity account](entropy_capacity.md), [stability theorem](channel_stability.md), [exact two-qubit construction](mixed_resets.md), and [query proof](query_complexity.md) supply the definitions and proofs behind the statements below.

## Channels, entropy, and distance

A quantum channel is a completely positive trace-preserving (CPTP) linear map. On a retained system of dimension $`D`$, a state is a positive matrix $`\rho`$ of trace one. Its von Neumann entropy is

```math
S(\rho)=-\mathrm{Tr}(\rho\log\rho),
```

with natural logarithms and the convention $`0\log0=0`$. Thus the entropy of a maximally mixed qubit is $`\log2`$.

The operator norm is denoted by $`\|\cdot\|_{\mathrm{op}}`$, the trace norm by $`\|\cdot\|_1`$, and the diamond norm by $`\|\cdot\|_\diamond`$. For a difference of channels with input dimension $`D`$,

```math
\|\Phi-\Psi\|_\diamond
=\max_{\rho_{SR}}
\|((\Phi-\Psi)\otimes\mathrm{id}_R)(\rho_{SR})\|_1,
\qquad \dim R=D.
```

The reference is untouched by both channels. A larger reference cannot increase this maximum. We use the full trace norm: equal-prior discrimination of states has optimal success probability $`1/2+\|\rho-\sigma\|_1/4`$. These conventions matter for the finite constants in the lower bound.

## A controlled reflection target

A Hermitian reflection satisfies

```math
U=U^\dagger,\qquad U^2=I.
```

It generates the rate-one dissipator

```math
\mathcal L_U(\rho)=U\rho U-\rho,
\qquad \mathcal E_{U,t}=e^{t\mathcal L_U}.
```

Rate one refers to the Poisson jump rate in this representation. Along a single off-diagonal block between the two eigenspaces of $`U`$, coherence decays as $`e^{-2t}`$.

A target descriptor consists of finitely many nonnegative durations $`t_1,\ldots,t_r`$ and known CPTP controls $`C_0,\ldots,C_r`$. Its full channel is

```math
\Phi_U
=C_r\circ\mathcal E_{U,t_r}\circ C_{r-1}
\circ\cdots\circ C_1\circ\mathcal E_{U,t_1}\circ C_0,
\qquad T=\sum_{k=1}^{r}t_k.
```

Every control is independent of the unknown oracle. Identity controls are allowed. Initial and terminal controls are included in the descriptor and in the resource budget. The prescribed control sequence is known to the simulator.

For any dimension-preserving channel, define its maximum entropy decrease by

```math
\kappa(C)=\max_\rho\{S(\rho)-S(C\rho)\},
\qquad E_{\mathrm{used}}=\sum_{k=0}^{r}\kappa(C_k).
```

This is the negative of established minimum entropy gain; see [Alicki](../references/RELATED_WORK.md#alicki2004). The promise on an instance is $`E_{\mathrm{used}}\le E`$. The maximum is attained in finite dimension. The budget refers to the specified sequence of controls, including their placement between noisy intervals.

The [capacity proof](entropy_capacity.md) establishes the useful special cases:

| Control on the retained system | Capacity |
|---|---:|
| Unitary conjugation | $`0`$ |
| Any unital channel | $`0`$ |
| Replacement of an $`a`$-dimensional subsystem by $`\tau`$ | $`\log a-S(\tau)`$ |
| Pure-qubit replacement | $`\log2`$ |
| Qubit replacement by $`I/2`$ | $`0`$ |

For channels with equal finite input and output dimension, zero capacity is equivalent to unitality. Since every capacity is nonnegative, $`E=0`$ means that all specified controls are unital. It still permits repeated interventions.

## Oracle access and the simulator

The supplied oracle is ordinary controlled-$`U`$,

```math
\mathrm{c}U=|0\rangle\langle0|\otimes I
+|1\rangle\langle1|\otimes U.
```

Each application counts as one query. Fixing its control to one supplies an uncontrolled application. Because $`U^\dagger=U`$ and $`U^2=I`$, inverse access uses the same oracle, and known integer powers reduce to the identity or one ordinary query. The oracle is available on auxiliary learning probes as well as on the target input.

The simulator may use arbitrary known operations, auxiliary quantum memory, measurements, resets, and classical processing. All its unknown-oracle calls count. It must implement an unconditioned CPTP channel $`\widehat\Phi_U`$ satisfying

```math
\|\widehat\Phi_U-\Phi_U\|_\diamond\le0.01
```

for every allowed unknown reflection. Random learning outcomes are averaged in the implemented channel. The guarantee does not condition on a successful measurement branch.

Only unknown-oracle queries are counted. The number of control boundaries, the classical work needed to handle their descriptions, and synthesis of known fitted channels can still contribute substantially to runtime. The target capacity budget does not restrict the simulator's own learning memory or reset use.

Formally, for each target descriptor, minimize the maximum number of queries over algorithms satisfying the uniform-in-$`U`$ error requirement. Then take the supremum over descriptors with total duration $`T`$ and capacity at most $`E`$. This defines $`Q_D(T,E,0.01)`$.

## Theorem Q: fixed-dimensional query classification

For a two-qubit retained target, uniformly for all real $`T\ge1`$ and $`E\ge0`$,

```math
Q_4(T,E,0.01)
=\Theta\!\left(\min\{T,\sqrt{T(1+E)}\}\right).
```

The implied constants are independent of $`T`$, $`E`$, and the number of specified control boundaries. The [query-complexity proof](query_complexity.md) gives both a bounded-query upper and an ordinary-oracle hybrid lower. The [mixed-reset construction](mixed_resets.md) treats zero, intermediate, and large budgets, including noninteger $`T`$, by exact finite channel formulas.

| Capacity regime | Query order | Saturating control |
|---|---:|---|
| Bounded $`E`$, including zero | $`\sqrt T`$ | Maximally mixed syndrome replacement |
| $`1\ll E\ll T`$ | $`\sqrt{TE}`$ | Partially polarized syndrome replacement |
| $`E=\Omega(T)`$ | $`T`$ | Pure syndrome replacement |

This is a worst-case theorem for the stated class at fixed error. The exact one-reflection channel without interventions has the much simpler parity sampler explained in [the interpretation](interpretation.md#one-reflection-without-interventions). The target controls are part of what is being simulated.

## Theorem S: Hermitian-noise stability with controls

The more general stability result permits matched time-dependent Hermitian jumps $`A_j(s),B_j(s)`$, common nonnegative weights $`p_j(s)`$ summing to one, and a common Hamiltonian $`K(s)`$. Between the same control boundaries, the first generator is

```math
\mathcal L_A(s)(\rho)
=-i[K(s),\rho]
-\frac12\sum_jp_j(s)[A_j(s),[A_j(s),\rho]],
```

and the second replaces $`A_j`$ by $`B_j`$. Bounded, piecewise continuous finite-dimensional coefficients and finitely many controls suffice. Define the integrated jump distance

```math
V^2=\int_0^T\sum_jp_j(s)
\|A_j(s)-B_j(s)\|_{\mathrm{op}}^2\,ds.
```

With the same known CPTP controls under both hypotheses,

```math
\|\Phi_A-\Phi_B\|_\diamond
\le V\left[1+\sqrt{4\log D+2E}\right].
```

The theorem is representation-explicit: it compares the supplied matched jump families, rather than minimizing over all Lindblad representations. It requires no spectral gap or mixing assumption. The constant does not depend on a common upper bound for the base-jump norms; bounded endpoint norms supply an additional elementary linear-time cap.

The retained dimension $`D`$ includes all retained quantum and classical registers, including records used only at the final readout. Newly generated records count in $`D`$ even when they never affect later controls. The allowed untouched reference is a separate register on which the entire protocol acts as the identity; records generated by the protocol are not such a reference. A temporary ancillary environment discarded inside a control is represented by that CPTP map and its capacity. The noise bath and its trajectory labels are inaccessible.

## Finite discrimination and memory

For norm-at-most-one Hermitian jumps satisfying a unit Lipschitz condition in the weighted jump metric, Theorem S and the linear-time cap imply that a fixed nonzero output trace-norm gap requires a parameter separation of order at least

```math
\frac1{\min\{T,\sqrt{T(1+E)}\}}
```

at fixed $`D=4`$. The same two-qubit construction attains this order. The threshold used in the proofs is a trace-norm gap greater than $`0.08`$, corresponding to a fixed nonzero binary advantage. No conversion from this trace-distance statement to an SLD quantum-Fisher-information upper bound is assumed.

The [supporting memory account](memory_and_local_noise.md) gives a local GHZ realization of the dimension dependence and a retained-qubit/pure-reset tradeoff in the weighted bounded-Hermitian metric. Its rate normalization is part of its statement. These examples explain how retained memory and entropy-removing controls enter the general theorem.

## Proof and evidence route

| Result | Authoritative account |
|---|---|
| Capacity and reference accounting | [Entropy capacity](entropy_capacity.md) |
| Complete channel stability, including singular resets | [Entropy and variance proof](channel_stability.md) |
| Exact physical saturation in every budget regime | [Two-qubit mixed resets](mixed_resets.md) |
| Learning upper, Poisson cap, and oracle hybrid lower | [Query complexity](query_complexity.md) |
| Dimension dependence and local noise | [Memory and local dephasing](memory_and_local_noise.md) |
| Physical meaning and resource boundaries | [Interpretation](interpretation.md) |
| Imported results and closest prior models | [Related work](../references/RELATED_WORK.md) |
| Reproducible finite identities and residuals | [Verification](../verification/README.md) |
