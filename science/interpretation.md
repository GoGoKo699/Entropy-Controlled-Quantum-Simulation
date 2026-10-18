# Entropy, control, and simulation cost

The central result identifies a resource of the **target evolution** that changes its simulation-query cost. A two-qubit target with one unknown reflection can require between square-root and linear query growth, depending on how much entropy its known controls can remove. The [model](model.md) fixes the oracle, rate, channel-error, and control conventions; the [query theorem](query_complexity.md) proves the classification.

## Entropy provides finite room for sensitivity

Hermitian Lindblad noise is unital. During each noisy interval it can increase the entropy of the retained system together with an untouched reference. For retained dimension $`D`$, the conditional entropy relative to that reference lies between $`-\log D`$ and $`\log D`$.

If common controls intervene, their total entropy-decrease capacity supplies additional room for noise to produce entropy. The sum of the entropy gains during all noisy intervals obeys

```math
\Delta S_{\mathrm{noise}}\le2\log D+E.
```

The [stability proof](channel_stability.md) connects that budget to sensitivity through a commutator inequality. A second forward-state/backward-observable identity supplies a bounded variance integral. Both estimates survive arbitrary common CPTP controls, giving

```math
\|\Phi_A-\Phi_B\|_\diamond
\le V[1+\sqrt{4\log D+2E}].
```

At a fixed jump distance per unit time, $`V`$ grows as $`\sqrt T`$. Retained memory contributes through $`\log D`$, and controls contribute through the entropy they can remove. Common coherent driving contributes neither entropy decrease nor an additional variance term, so a strong known Hamiltonian does not invalidate the bound.

## Adjustable reset purity gives the crossover

The saturating construction uses one syndrome qubit and one logical qubit. Its unknown reflection is

```math
U_\theta=\cos\theta\,X_S-\sin\theta\,Y_SZ_L.
```

A fixed CNOT turns this into local Pauli-axis noise with a noiseless ancillary qubit. After each noise interval, the controller replaces the syndrome by $`\tau_b=(I+bZ)/2`$, with $`0\le b\le1`$. This operation has capacity

```math
e(b)=\log2-h((1+b)/2)=\Theta(b^2).
```

Here $`h(x)=-x\log x-(1-x)\log(1-x)`$ is binary entropy. For $`T\ge1`$, take $`N=\lfloor T\rfloor`$ intervals of duration $`\Delta=T/N\in[1,2)`$ and define the odd-jump probability $`p=(1-e^{-2\Delta})/2`$. Then $`N=\Theta(T)`$, and the exact logical coherence multiplier is

```math
f_b(\theta)^N,
\qquad f_b(\theta)=1-p+p\cos(2\theta)-ipb\sin(2\theta).
```

For a small angle, the phase per interval is proportional to $`b\theta`$, while loss of coherence begins at order $`\theta^2`$. The accumulated phase therefore has scale $`Nb\theta`$. The used capacity is $`E_{\mathrm{used}}=Ne(b)=\Theta(Nb^2)`$, so the phase scale is $`\sqrt{NE_{\mathrm{used}}}\,\theta`$. In the intermediate-budget regime, the construction chooses $`E_{\mathrm{used}}=\Theta(E)`$. The finite proof in [the construction](mixed_resets.md) controls both phase and visibility, rather than relying on this expansion as an asymptotic substitute.

At zero polarization, the coherent phase vanishes. The real multiplier becomes $`1-2p\sin^2\theta`$, and repeated intervals still create a constant logical dephasing signal at angle of order $`1/\sqrt N`$. At full polarization, each reset costs $`\log2`$, and a constant phase is visible at angle of order $`1/N`$. Partially polarized replacements connect these endpoints continuously.

At the zero-angle baseline, the total entropy actually removed by the replacements is at least $`(1-e^{-4\Delta})E_{\mathrm{used}}`$. Whenever $`b>0`$, the baseline therefore uses a constant fraction of the controls' summed entropy capacity. The supplied allowance $`E`$ may be larger than $`E_{\mathrm{used}}`$, especially after the linear-time regime has saturated.

## Why distinguishability imposes query cost

The two oracle hypotheses obey $`\|U_\theta-U_0\|_{\mathrm{op}}\le|\theta|`$. Any algorithm with $`q`$ ordinary queries can change its output by at most $`2q|\theta|`$ in trace norm between these hypotheses, even with arbitrary auxiliary memory and measurements.

The prescribed target channel can create a gap greater than $`0.08`$ on a known input. A simulator with diamond error $`0.01`$ at each endpoint must preserve more than $`0.06`$ of that gap. Consequently its query count is bounded below by a constant times the inverse angle. This produces the lower half of

```math
Q_4(T,E,0.01)=\Theta\!\left(\min\{T,\sqrt{T(1+E)}\}\right).
```

For the upper half, an algorithm can learn the constant-dimensional reflection, then implement the known fitted target. The stability theorem specifies exactly how accurate that estimate needs to be. The [optimal unitary-learning theorem](../references/RELATED_WORK.md#hkot2023) has inverse-error query cost, so an estimate accurate to order $`1/\sqrt{T(1+E)}`$ gives the required simulation upper. A direct Poisson trajectory supplies the linear cap.

The lower bound is therefore against arbitrary oracle algorithms, and the upper is an actual channel implementation. Their combination is stronger than a statement about a particular recovery circuit or a formal low-degree expression for a superoperator.

## One reflection without interventions

With no interventions, every jump word reduces to its parity because $`U^2=I`$. Exactly,

```math
e^{T(\mathrm{Ad}_U-\mathrm{id})}
=\frac{1+e^{-2T}}2\,\mathrm{id}
+\frac{1-e^{-2T}}2\,\mathrm{Ad}_U.
```

Sampling one classical Bernoulli variable and applying $`U`$ on the odd branch implements this channel with at most one query, for every $`T`$. Interleaved known controls can prevent that global parity cancellation. The zero-capacity class still permits many unital controls, including the maximally mixed syndrome replacement used in the lower bound. Thus the square-root lower at $`E=0`$ describes a controlled class that already contains more targets than the uninterrupted single-reflection semigroup.

## Target capacity and simulator resources

The distinction between the target and its simulator is essential. The budget $`E`$ constrains the prescribed maps $`C_k`$ inside the target descriptor. A learning-based simulator may consume fresh probes, reset its workspace, and perform classical estimation. These resources are allowed, and every unknown-oracle call made during learning is counted.

At fixed dimension the query upper is small enough to match the lower, but known-gate cost can still scale with the number of target intervals. In larger dimensions, learning whole unitary matrices has a dimension cost. The theorem does not identify query complexity with end-to-end runtime.

Initial probe preparation in a lower-bound witness serves a different role: the simulator is required to work on every input, so it must also work on that particular known state. No operation replaces an arbitrary target input for free. All initial or terminal controls that are actually included in a target descriptor count toward its capacity budget.

## Capacity, reset count, and retained memory

The maximum entropy decrease is an informational property of a channel. It gives a direct accounting rule for several control resources, but those resources need not coincide.

| Resource description | How it enters the theorem |
|---|---|
| $`q`$ retained qubits | $`\log D=q\log2`$ |
| $`R`$ pure-qubit replacements | Capacity at most $`R\log2`$ |
| Replacements by mixed states | Each contributes its entropy deficit from the maximally mixed state |
| Retained measurement record | Its register contributes to $`D`$, including when it is used only at final readout |
| A discarded record or temporary environment inside a control | Its effect is represented by that CPTP map and bounded by its capacity |

The two-qubit interpolation uses order-$`T`$ replacement operations even when their summed capacity is small. A theorem about the number of pure resets is therefore a distinct statement. The [memory and local-noise account](memory_and_local_noise.md) supplies such a supporting tradeoff in the weighted Hermitian-jump metric, with the active-rate normalization stated explicitly.

Keeping a long classical history can increase retained dimension even if the number of quantum probe qubits stays small. A record generated during the protocol belongs to this retained memory even if no later control consults it; it cannot be treated as an untouched reference. Access to a bath jump label also changes the sensing model. The present theorem applies to the final unconditioned channel without bath monitoring.

## Relation to metrology and thermodynamics

The noisy-axis error-correction mechanism has a close predecessor in [Chen and colleagues](../references/RELATED_WORK.md#chen2024). [Subsystem recovery](../references/RELATED_WORK.md#liu2026) already includes gauge resets and mixed gauge states, and [weakly polarized probe metrology](../references/RELATED_WORK.md#cable2016) contains the corresponding coherent-accumulation mechanism in a unitary-encoding setting. Their role here is to supply physically transparent saturation mechanisms. The combined result is the full-channel converse with explicit entropy accounting and its matched simulation-query law.

The operational sensing conclusion concerns **finite binary separation**. A small first derivative of trace distance, or a trace-distance Lipschitz bound, cannot in general be squared into an SLD quantum-Fisher-information upper bound near singular states. The exact witness and the query lower avoid that inference.

The capacity $`\kappa`$ also has an established relation to [thermodynamic capacity for trivial Hamiltonians](../references/RELATED_WORK.md#faist2019). A physical heat or work cost would require an additional reservoir and implementation model. The present results use only the informational entropy capacity defined in the target descriptor.

## What the bound explains

A finite retained system has limited room for noise-generated entropy. Entropy-removing controls can repeatedly restore that room, and partially mixed resets make the amount adjustable. The same resource that permits stronger discrimination of nearby noise operators also forces a simulator to spend more oracle queries reproducing the target channel. The entropy/variance proof and exact construction identify this relationship quantitatively under a common, fully specified access and output model.
