# Watrous bridge: channels, entropy, and controlled noise

John Watrous's finite-dimensional treatment of quantum information supplies the language for this project: states, channels, untouched references, distinguishability, and entropy. The additional arguments connect that language to continuous noisy evolution, entropy-removing controls, and the number of calls to an unknown unitary. This bridge explains those connections. The linked [science accounts](../science/README.md) contain the complete proofs and their assumptions.

<a id="source-and-version"></a>

## 1. Source and verified locations

The educational anchor is **John Watrous, _The Theory of Quantum Information_, Cambridge University Press, 2018**. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies the April 2018 publication and links the available manuscript. The linked text used here is the author's **standard-layout pre-publication manuscript**; its [front matter](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) identifies the author and has a preface dated January 2018.

The following are printed page numbers in that manuscript, not PDF page indices or a claim about pagination in every commercial format. The chapter links are parts of this one book. This repository links to the author-hosted material; it does not include or redistribute the book PDFs.

| Foundation | Verified location in the author manuscript | Connection to this project |
|---|---|---|
| Operators, decompositions, and norms | [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), §§1.1.2–1.1.3, pp. 8 and 24; spectral theorem, Theorem 1.3, p. 25 | Hermitian reflections, matrix functions, operator and trace norms |
| Composite states and their reductions | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §§2.1.2–2.1.3, pp. 61 and 67 | Reduced states, entangled inputs, and the reference register |
| Channels and their representations | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §§2.2.1–2.2.2, pp. 72 and 77 | CPTP maps, Kraus operators, and the adjoint action on observables |
| State discrimination | [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §3.1.1, p. 125, including Theorem 3.4 | The operational meaning of a finite trace-norm gap |
| Complete channel distance | [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §§3.3.1–3.3.3, pp. 164, 166, and 175; Theorems 3.51–3.52, pp. 176–177 | Diamond distance, an input-sized reference, and channel discrimination |
| Unital channels | [Chapter 4](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf), §4.1.1, p. 202, and §4.2.2, p. 228 | Random-unitary noise and the distinction between unital and general controls |
| Entropy and conditional entropy | [Chapter 5](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), §§5.2.1–5.2.2, pp. 265 and 267; Theorems 5.24–5.25, pp. 270–271 | Entropy ranges, subadditivity, and the effect of an untouched reference |
| Relative entropy | [Chapter 5](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), §5.2.3, p. 276; Theorem 5.35, p. 280, and Theorem 5.38, p. 282 | Data processing and quantum Pinsker |

Two adjoint facts have particularly direct roles. Proposition 2.18 and its following remark, on manuscript p. 76, establish positivity and complete positivity of adjoints. Theorem 2.26, on p. 87, identifies trace preservation with unitality of the adjoint. Together they allow a terminal observable to be propagated backward through arbitrary CPTP controls.

Watrous provides these mathematical foundations. The controlled Lindblad stability bound, the reset witness, and the oracle-query classification are additional results developed in the [canonical project proofs](../science/README.md). Their attribution and imported research dependencies are recorded in [related work](../references/RELATED_WORK.md).

<a id="notation"></a>

## 2. Translate the conventions before using a bound

| Topic | Watrous notation or background convention | Convention here |
|---|---|---|
| Vectors and adjoints | Vectors such as $`u`$, rank-one operators $`uu^*`$, and adjoints $`X^*`$, $`\Phi^*`$ | Dirac notation $`\lvert u\rangle`$, $`\lvert u\rangle\langle u\rvert`$, and daggers $`X^\dagger`$, $`\Phi^\dagger`$ |
| Identity | The identity operator and identity map are distinguished by their spaces | $`I`$ is an operator; $`\operatorname{Id}`$ or $`\mathrm{id}`$ is a map |
| Entropy | $`H(\rho)`$, with base-two logarithms | $`S(\rho)=(\ln2)H(\rho)`$, in nats; a maximally mixed qubit has entropy $`\ln2`$ |
| Relative entropy | Base-two $`D(\rho\Vert\sigma)`$ | Natural-logarithm relative entropy equals the base-two value multiplied by $`\ln2`$ |
| Trace norm | $`\|X\|_1=\operatorname{Tr}\sqrt{X^\dagger X}`$ | The same full norm; no factor $`1/2`$ is absorbed into it |
| Complete channel norm | The book's triple-bar completely bounded trace norm, $`\lVert\!\lVert\!\lVert\Phi\rVert\!\rVert\!\rVert_1`$ | $`\|\Phi\|_\diamond`$, also unhalved; the induced trace norm without a reference is a different quantity |
| Retained system and reference | Tensor-product registers and reduction maps | $`A`$ is the retained target, $`D=\dim A`$; $`R`$ is present as a reference and untouched by the entire target protocol |
| Control resource | Channel and entropy notions provide the ingredients | $`E`$ bounds the sum of target-control capacities $`\kappa(C)`$; it does not constrain the simulator's own probes or resets |
| Time and rates | A channel definition alone does not set a physical rate | $`T`$ is total exposure at the specified normalization; reflection noise has total Poisson rate one |

The operator logarithm is explicitly base two in Chapter 1, manuscript p. 28. Consequently, Theorem 5.38 converts as follows:
```math
D_2(\rho\Vert\sigma)\geq
\frac{1}{2\ln2}\|\rho-\sigma\|_1^2
\quad\Longrightarrow\quad
D_{\mathrm{nat}}(\rho\Vert\sigma)\geq
\frac12\|\rho-\sigma\|_1^2.
```
The project's Hermitian jump matrices $`H_j`$ are unrelated to the book's entropy symbol $`H`$. Its retained dimension $`D`$ is likewise distinct from relative entropy.

For equal-prior state discrimination, Theorem 3.4 gives
```math
p_{\mathrm{succ}}
=\frac12+\frac14\|\rho-\sigma\|_1.
```
Thus a full trace-norm gap $`0.08`$ corresponds to optimal success probability $`0.52`$. A convention using half the trace norm would attach a different numerical distance to the same experiment. The same conversion applies to the diamond-norm channel-discrimination statement in Theorem 3.52.

The reference convention is also a resource convention. A record generated during the target protocol and retained until its output belongs to $`A`$, including a record used only in the final readout. It cannot be relabeled as an untouched reference. A measurement applied after the completed target channel is ordinary final data processing and does not require enlarging the retained dimension used in the theorem. A temporary environment discarded inside a control is represented by that control's CPTP map. The [model](../science/model.md) fixes these boundaries.

<a id="reset-example"></a>

## 3. Worked example: replace one qubit, with or without correlations

Let $`A`$ be a qubit and let
```math
\tau_b=\frac{I+bZ}{2}
=\lambda_0|0\rangle\langle0|+\lambda_1|1\rangle\langle1|,
\qquad
\lambda_0=\frac{1+b}{2},\quad
\lambda_1=\frac{1-b}{2},
\quad 0\leq b\leq1.
```
Replacing the qubit by this known state is the channel
```math
\mathcal R_b(X)=\tau_b\,\operatorname{Tr}X.
```
The channel representations of Chapter 2 make this concrete. Its four Kraus operators can be chosen as
```math
K_{ac}=\sqrt{\lambda_a}\,|a\rangle\langle c|,
\qquad a,c\in\{0,1\}.
```
Direct substitution gives
```math
\sum_{a,c}K_{ac}^\dagger K_{ac}=I,
\qquad
\sum_{a,c}K_{ac}XK_{ac}^\dagger
=\tau_b\,\operatorname{Tr}X.
```
The first identity proves trace preservation; the Kraus form supplies complete positivity. On a state correlated with a reference,
```math
(\mathcal R_b\otimes\mathrm{id}_R)(\rho_{AR})
=\tau_b\otimes\rho_R.
```
The reference marginal is unchanged, while the original correlations are removed.

The actual joint entropy decrease on this input is
```math
S(\rho_{AR})-S(\tau_b\otimes\rho_R)
=S(A\mid R)_\rho-S(\tau_b).
```
Subadditivity bounds $`S(A\mid R)_\rho\leq\ln2`$, and equality is attained on $`(I/2)\otimes\rho_R`$. Therefore the largest decrease, including arbitrary references, is
```math
\kappa(\mathcal R_b)
=\ln2-h\!\left(\frac{1+b}{2}\right),
\qquad
h(x)=-x\ln x-(1-x)\ln(1-x).
```
For example, at $`b=1/2`$ this equals $`\frac34\ln3-\ln2`$ nats.

A Bell input shows why this maximum must be distinguished from what happens on one correlated state. For
```math
|\Omega\rangle
=\frac{|00\rangle+|11\rangle}{\sqrt2},
```
the initial joint entropy is zero, but the output is $`\tau_b\otimes I_R/2`$, with entropy
```math
S(\tau_b)+\ln2.
```
The joint entropy decrease is now negative. The same channel has a positive maximum entropy decrease whenever $`b>0`$. Reference invariance of capacity says that correlations cannot raise that maximum; it does not say that a reference leaves the actual entropy change unchanged.

The backward action is equally explicit:
```math
\mathcal R_b^\dagger(O)=\operatorname{Tr}(\tau_b O)\,I.
```
For the observable $`Z`$,
```math
\mathcal R_b^\dagger(Z^2)
-\bigl(\mathcal R_b^\dagger Z\bigr)^2
=(1-b^2)I\succeq0.
```
This is a small instance of the positive variance contribution used at a control boundary in the stability proof. At $`b=0`$, the reset is unital and has zero capacity, yet it still changes states, correlations, and backward observables.

The [capacity account](../science/entropy_capacity.md#reset-capacity) proves the general subsystem formula. The [two-qubit protocol](../science/mixed_resets.md) adds noisy intervals to this replacement and computes its output exactly. These reset formulas are applications of the book's channel and entropy tools, not theorems attributed to the book.

<a id="from-channels-to-noise"></a>

## 4. From a static channel to a noisy evolution

A channel specifies an input-output transformation. The project also needs a generator that specifies how transformations accumulate with exposure time. For a Hermitian matrix $`H`$, its dissipator is
```math
\mathcal D_H(\rho)
=H\rho H-\frac12\{H^2,\rho\}
=-\frac12[H,[H,\rho]].
```
It satisfies $`\mathcal D_H(I)=0`$, so its evolution is unital. A weighted sum of such dissipators, with an optional common Hamiltonian, gives the generators in the [stability model](../science/channel_stability.md#main-theorem). The generator and its time dependence are additional dynamical structure.

For a reflection $`U=U^\dagger`$, $`U^2=I`$, the evolution has an elementary channel representation:
```math
e^{t(\operatorname{Ad}_U-\operatorname{Id})}
=e^{-t}\sum_{k=0}^{\infty}
\frac{t^k}{k!}\operatorname{Ad}_{U^k}.
```
This is a Poisson mixture of unitary channels. Even jump counts give the identity and odd counts give $`U`$, so
```math
e^{t(\operatorname{Ad}_U-\operatorname{Id})}
=(1-p_t)\operatorname{Id}+p_t\operatorname{Ad}_U,
\qquad
p_t=\frac{1-e^{-2t}}2.
```
An uninterrupted reflection-noise interval can therefore be implemented exactly by a known classical coin and at most one call to $`U`$, for every $`t`$.

Interposed controls prevent a general reduction of the entire target to one parity. Each interval still has its own parity representation, but moving an oracle application through a control generally changes the channel. The [interpretation of the one-reflection case](../science/interpretation.md#one-reflection-without-interventions) makes this distinction explicit.

Zero entropy capacity also permits nontrivial interventions. In the mixed-reset example, maximally mixed syndrome replacements have zero capacity, while $`N`$ equal-duration cycles give a logical coherence factor
```math
f_0(\theta)^N,
\qquad
f_0(\theta)=1-p+p\cos(2\theta).
```
Here $`p=p_\Delta`$ is the odd-jump probability for the common fixed interval duration $`\Delta>0`$. The dependence on $`N\theta^2`$ makes angles of order $`N^{-1/2}`$ visible. Thus the worst-case square-root query behavior at $`E=0`$ is compatible with the one-query uninterrupted channel.

Unitality, complete positivity, and a convex mixture of unitary channels are related but distinct concepts. The explicit Poisson representation establishes the mixed-unitary property for the reflection example; no general equivalence between unital and mixed-unitary channels is assumed.

<a id="entropy-and-variance"></a>

## 5. The additional entropy and variance argument

The central stability proof compares two matched Hermitian jump families $`A_j(s)`$ and $`B_j(s)`$ under the same controls and a common Hamiltonian, if present. The perturbation is measured by
```math
V^2=\int_0^T\sum_jp_j(s)
\|A_j(s)-B_j(s)\|_{\mathrm{op}}^2\,ds.
```
Three connections turn the book's finite-dimensional tools into the complete-channel estimate.

### Entropy production bounds a commutator

For a full-rank state, define
```math
\sigma_H(\rho)
=-\operatorname{Tr}\mathcal D_H(\rho)\ln\rho.
```
Along the unitary curve $`\rho_x=e^{ixH}\rho e^{-ixH}`$, direct expansion gives
```math
D_{\mathrm{nat}}(\rho_x\Vert\rho)
=x^2\sigma_H(\rho)+O(x^3),
\qquad
\|\rho_x-\rho\|_1
=|x|\|[H,\rho]\|_1+o(|x|).
```
The natural-log Pinsker coefficient then implies
```math
\|[H,\rho]\|_1^2\leq2\sigma_H(\rho).
```
Pinsker is the imported book theorem. The unitary-curve expansion and its connection to this dissipator are the extra steps; the [commutator proof](../science/channel_stability.md#unitary-curve) gives all coefficients.

During Hermitian noise, entropy production is nonnegative. Controls can lower entropy and permit more subsequent production. With an untouched reference, the conditional entropy range is
```math
-\ln D\leq S(A\mid R)\leq\ln D.
```
These two bounds follow from the entropy inequalities in Chapter 5. Summing changes through the whole protocol, and using reference invariance of each control's capacity, gives
```math
\Delta S_{\mathrm{noise}}\leq2\ln D+E,
\qquad
\int_0^T\sum_jp_j
\|[H_j,\rho_s]\|_1^2\,ds
\leq4\ln D+2E.
```
Here $`E`$ is a structural bound on the specified controls, not a value obtained by evaluating their entropy decrease only on a favored input. The [control-budget proof](../science/entropy_capacity.md#control-budget) handles this summation.

### A backward observable has a separate variance budget

Let $`\rho_s`$ be the forward state and let $`O_s`$ be a terminal Hermitian observable propagated backward through the remaining evolution and controls. The adjoint facts in Chapter 2 imply $`\|O_s\|_{\mathrm{op}}\leq1`$ when the terminal observable has norm at most one.

For a matched forward and backward evolution,
```math
g(s)=\operatorname{Tr}\rho_s O_s^2
```
has noisy-interval derivative
```math
g'(s)=\sum_jp_j(s)\operatorname{Tr}\rho_s
[H_j(s),O_s]^\dagger[H_j(s),O_s]\geq0.
```
At a control $`C`$, its jump is also nonnegative because the adjoint is unital and completely positive:
```math
C^\dagger(O^2)-\bigl(C^\dagger O\bigr)^2\succeq0.
```
The reset calculation above illustrates this inequality directly. Since $`0\leq g\leq1`$, the integral of the displayed nonnegative noisy derivative is at most one. No factor counting the control boundaries is needed.

This matched variance identity is an additional dynamical calculation. [Section 5 of the stability proof](../science/channel_stability.md#5-a-matched-variance-budget-survives-cptp-controls) derives both the continuous derivative and the control jump.

### Combine the budgets and keep the reference

Interpolate the jumps as
```math
H_j^{(u)}(s)=A_j(s)+u\bigl(B_j(s)-A_j(s)\bigr),
\qquad 0\leq u\leq1.
```
These matrices remain Hermitian even when the endpoints are reflections. Differentiating a final expectation produces two commutator terms. The first uses the forward entropy budget; the second uses the backward variance budget. Weighted Cauchy–Schwarz therefore gives
```math
\|\Phi_A-\Phi_B\|_\diamond
\leq V\left[1+\sqrt{4\ln D+2E}\right].
```
The state and observable must be propagated through the same interpolated protocol for the variance cancellation to hold.

The proof first bounds every final Hermitian expectation, then the full output trace norm, uniformly over initial states and untouched references. Theorem 3.51 identifies this optimization with the diamond norm for a difference of channels and shows that an input-sized reference suffices. The entropy bound depends on $`S(A\mid R)`$, so the size of an untouched reference does not add to $`\ln D`$. The [complete stability proof](../science/channel_stability.md#main-theorem) supplies the interpolation and optimization details.

Pure resets require one further step. Making the input full rank alone is insufficient: a pure replacement immediately restores zero eigenvalues. The proof regularizes every control by mixing it with a small completely depolarizing component, as well as regularizing the input. Entropy concavity ensures that this does not increase its capacity. The bound then passes to the limit for each finite control sequence. This is the purpose of the [singular-state argument](../science/channel_stability.md#singular-states).

<a id="query-connection"></a>

## 6. From channel stability to an oracle algorithm

A stability estimate states how accurately an unknown jump must be approximated. It does not by itself provide a circuit that learns or realizes the approximation.

The access model supplies ordinary controlled-$`U`$ queries. The simulation upper bound imports the unitary learner of **Haah–Kothari–O'Donnell–Tang** through the precise statement and attribution in [query complexity](../science/query_complexity.md#learning-upper-bound) and [related work](../references/RELATED_WORK.md#hkot2023). This is a research dependency of the algorithm; Watrous remains the educational anchor.

The learner is applied to
```math
W=\operatorname{diag}(I_4,U),
```
which is one supplied controlled-$`U`$ call. Channel learning initially determines a unitary only up to global phase. The known identity block supplies a phase reference, after which Hermitian symmetrization and a spectral sign operation give a reflection estimate $`U'`$. The estimate is learned on auxiliary probes while the unknown target input is kept untouched.

At fixed dimension, the imported learner uses order $`1/\eta`$ queries for the needed root-mean-square error scale $`\eta`$. Stability converts this error into error of the complete controlled target, with the required accuracy scale
```math
\eta\asymp\frac{1}{\sqrt{T(1+E)}}.
```
For every learned estimate, the simulator implements the same known target controls with $`U'`$ substituted for $`U`$. Its output is the average over all learning outcomes. Convexity of the diamond norm and the expected-square learning guarantee bound that averaged error. There is no successful branch on which the guarantee is conditioned.

A separate direct sampler caps the total Poisson query count and gives order $`T`$ queries. Combining the two algorithms yields the upper part of
```math
Q_4(T,E,0.01)
=\Theta\!\left(\min\{T,\sqrt{T(1+E)}\}\right),
\qquad T\geq1,\quad E\geq0.
```
The query theorem concerns the worst target in the specified class, with a query bound on every execution. Handling a long list of known controls can still take substantial time.

The lower bound connects state discrimination back to oracle use. The exact mixed-reset protocol gives two target outputs whose full trace-norm gap exceeds $`0.08`$, for a chosen pair $`U_0,U_\theta`$ with operator distance at most $`|\theta|`$. An algorithm using $`q`$ controlled-oracle calls has output gap at most $`2q|\theta|`$, by replacing its calls one at a time and using channel contraction. Diamond error $`0.01`$ under each hypothesis can remove at most $`0.02`$ from the target gap. A nonzero gap therefore forces $`q`$ of order $`1/|\theta|`$.

Chapter 3, §3.3.3, pp. 178–179, provides the channel-network error-addition framework behind such replacements. Choosing the oracle family, obtaining a uniform finite output gap, and arranging every real $`T`$ and every capacity budget are extra arguments in the [query lower proof](../science/query_complexity.md#lower-bound). Matrix entries, arbitrary unknown powers, quantum random-access memory, and postselection are not supplied by the model.

<a id="memory-and-rates"></a>

## 7. Memory and rate normalization in the supporting spin example

The logarithmic dimension factor has a transparent local-spin realization. The [local-noise account](../science/memory_and_local_noise.md) uses $`n`$ independent spin jumps, a known GHZ preparation, and an ordinary product measurement. At normalized total-rate-one exposure $`T=n`$, an axis change of order $`1/n`$ produces a constant output gap. Since $`\ln D=n\ln2`$, this realizes the $`\sqrt{T\ln D}`$ sensitivity scale without intermediate resets.

The normalization is essential. If every one of $`n`$ sites instead has rate one for a physical time $`t_{\mathrm{phys}}`$, the same evolution has total-rate-one exposure $`T=nt_{\mathrm{phys}}`$. The entangled state is part of the retained target; it cannot be hidden in an untouched reference. Its known preparation takes order $`n`$ elementary gates and supplies no unknown-oracle information.

At long exposure the fixed local family saturates: its exact query order is $`\Theta(\min\{T,n\})`$. The construction that realizes the weighted stability scale for $`T\gg n`$ reduces the jump amplitudes. That change is included in $`V`$, and it cannot be interpreted as an unchanged-rate reflection-oracle lower bound. The [weighted metric discussion](../science/memory_and_local_noise.md#5-the-long-time-limit-and-the-weighted-metric) and the retained-qubit/reset construction make this distinction explicit.

