# Related work and attribution

This project studies how known interventions change the query complexity of simulating unknown Hermitian noise. The central resource is the entropy-reduction capacity of a control channel,

```math
\kappa(\mathcal C)=\max_\rho\{S(\rho)-S(\mathcal C(\rho))\},
\qquad E_{\mathrm{used}}=\sum_k\kappa(\mathcal C_k)\leq E.
```

Entropy uses natural logarithms. The dimension $`D`$ includes all retained quantum and classical memory; the bath is unmonitored. The budget $`E`$ constrains the **target protocol's controls**. It does not restrict the simulator's learning ancillas, measurements, resets, or classical computation.

The [channel stability theorem](../science/channel_stability.md) compares two time-dependent Hermitian jump tuples, with common Hamiltonian, common weights, and common parameter-independent CPTP controls at the same times:

```math
\|\Phi_A-\Phi_B\|_\diamond
\le
\left[\int_0^T\sum_j p_j(s)\|A_j(s)-B_j(s)\|_{\mathrm{op}}^2\,ds\right]^{1/2}
\left(1+\sqrt{4\ln D+2E}\right).
```

The [query theorem](../science/query_complexity.md) specializes to one rate-one unknown reflection on a fixed two-qubit target. At fixed small diamond error and total noise time $`T\ge1`$, its worst-case query complexity is

```math
Q(T,E)=\Theta\!\left(\min\{T,\sqrt{T(1+E)}\}\right).
```

These are finite-distance channel and oracle-query statements. Their scope should be distinguished from local quantum Fisher information, monitored trajectory currents, or gate complexity as the target dimension grows. The following source comparisons identify which ingredients are established and which additional statement is developed here. Bibliographic entries are available in [references.bib](references.bib).

## Attribution at a glance

| Ingredient or neighboring result | Main sources | Role in this project |
|---|---|---|
| Minimum entropy gain and channel capacity | [Alicki](#alicki2004), [Faist–Berta–Brandão](#faist2019) | The quantity $`\kappa`$ and its basic resource properties are prior. |
| Relative-entropy contraction and quantum Pinsker | [Lindblad](#lindblad1975), [Watrous](#watrous2018) | Standard tools in the entropy estimate. |
| Noncommutative uniform convexity | [Ricard–Xu](#ricard2016) | A standard alternative route to the dissipation estimate. |
| Learning an unknown unitary in diamond distance | [Haah–Kothari–O'Donnell–Tang](#hkot2023) | The learning subroutine in the query upper bound. |
| General Lindblad simulation | [Wang–Ye](#wang2026), [Borras–Marvian](#borras2026) | General access models and linear-time simulation baselines. |
| Adaptive sensing with informative noise | [Wan–Lasenby](#wan2022), [Das–Górecki–Demkowicz-Dobrzański](#das2025), [Chen et al.](#chen2024) | Established sensitivity bounds and the noise-orientation QEC mechanism. |
| Gauge resets and mixed gauge states | [Liu–Zhou](#liu2026) | Established recovery architecture and polarization-dependent logical signals. |
| Weak-purity and dephasing-axis examples | [Cable–Gu–Modi](#cable2016), [Kukita–Matsuzaki–Kondo](#kukita2021) | Precedents that delimit the claims about the saturation examples. |
| Feedback information and precision | [Honma–Vu](#honma2026) | A distinct information-dependent trajectory bound with different hypotheses. |

## Entropy capacity and standard proof tools

<a id="alicki2004"></a>
### Alicki (2004): minimum entropy gain

Robert Alicki, **“Isotropic quantum spin channels and additivity questions,”** arXiv:quant-ph/0402080v1 (2004). [Primary full text](https://arxiv.org/pdf/quant-ph/0402080).

Section 4, Theorem 3, equations (31)–(35), defines minimum entropy gain $`G(\mathcal C)=\inf_\rho[S(\mathcal C(\rho))-S(\rho)]`$ and proves its additivity under tensor products. For a dimension-preserving channel it lies between $`-\ln D`$ and zero; unital channels have zero minimum entropy gain.

Thus this project's $`\kappa=-G`$ is an established channel quantity. Tensoring with an identity channel leaves it unchanged. The underlying mutual-information data-processing argument also directly proves that a correlated reference cannot increase the entropy decrease caused by a local control. The [capacity note](../science/entropy_capacity.md) uses these properties to account for controls and mixed resets. The contribution sought here concerns the resulting channel-stability and query laws, rather than a new definition of channel entropy capacity.

<a id="faist2019"></a>
### Faist–Berta–Brandão (2019): thermodynamic capacity

Philippe Faist, Mario Berta, Fernando Brandão, **“Thermodynamic Capacity of Quantum Processes,”** *Physical Review Letters* **122**, 200601 (2019). [Published article](https://doi.org/10.1103/PhysRevLett.122.200601); [primary preprint](https://arxiv.org/pdf/1807.05610).

Equation (3) defines the maximum free-energy increase of a channel. The discussion on printed page 4 identifies the trivial-Hamiltonian specialization with minus minimum entropy gain. The operational result concerns asymptotic universal channel implementation and work conversion, including diamond approximation.

This is a resource-theory precedent for $`\kappa`$. The present model defines $`E`$ informationally from target control channels; it does not assign a heat or work cost to a physical implementation. Such an interpretation requires additional Hamiltonians, reservoirs, and implementation assumptions. Faist et al.'s implementation theorem does not itself state a noise-discrimination or oracle-query bound.

<a id="lindblad1975"></a>
### Lindblad (1975): relative-entropy data processing

Göran Lindblad, **“Completely positive maps and entropy inequalities,”** *Communications in Mathematical Physics* **40**, 147–151 (1975). [Primary journal record](https://doi.org/10.1007/BF01609396).

The paper establishes that quantum relative entropy decreases under a trace-preserving completely positive map. This standard theorem implies mutual-information data processing, which underlies reference invariance and additivity of entropy-reduction capacity. The entropy estimate in this project uses the same contraction principle; it is not attributed to the later martingale-convexity literature.

<a id="watrous2018"></a>
### Watrous (2018): channel distance, entropy, and Pinsker

John Watrous, **The Theory of Quantum Information**, Cambridge University Press (2018). [Author's book page](https://cs.uwaterloo.ca/~watrous/TQI/); [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Chapter 5](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf).

Section 3.3 treats channel discrimination and the completely bounded trace norm. Theorem 5.35 gives relative-entropy data processing, and Theorem 5.38 gives quantum Pinsker. The book uses base-two relative entropy, so its Pinsker coefficient is $`1/(2\ln2)`$. With natural-log relative entropy the coefficient is $`1/2`$, as used in [channel stability](../science/channel_stability.md). These are standard finite-dimensional tools.

<a id="ricard2016"></a>
### Ricard–Xu (2016): noncommutative convexity

Éric Ricard, Quanhua Xu, **“A noncommutative martingale convexity inequality,”** *Annals of Probability* **44**(2), 867–882 (2016), DOI [10.1214/14-AOP990](https://doi.org/10.1214/14-AOP990). [Primary full text, arXiv:1405.0431v4](https://arxiv.org/pdf/1405.0431v4).

Theorem 2 restates the sharp Ball–Carlen–Lieb uniform-convexity inequality for noncommutative $`L_q`$ spaces. Theorem 1 and Corollary 3 give conditional-expectation and martingale consequences. The original matrix inequality is due to Keith Ball, Eric A. Carlen, and Elliott H. Lieb, *Inventiones Mathematicae* **115**, 463–482 (1994), [DOI](https://doi.org/10.1007/BF01231769).

Applied to a unitary orbit, this standard convexity estimate yields dissipation of $`\|\rho\|_q^2`$ under Hermitian noise. Choosing $`q-1`$ of order $`1/\ln D`$ gives an alternative route to logarithmic dimension dependence; its entropy limit recovers the relevant entropy-production estimate. That deduction still requires the two-channel Duhamel argument and control accounting. Ricard–Xu does not state the present two-channel diamond bound or the sum-of-capacities query theorem.

<a id="szehr2013"></a>
### Szehr–Wolf (2013): perturbation bounds controlled by mixing

Oleg Szehr, Michael M. Wolf, **“Perturbation Bounds for Quantum Markov Processes and their Fixed Points,”** *Journal of Mathematical Physics* **54**(3) (2013), [DOI](https://doi.org/10.1063/1.4795112). [Primary full text, arXiv:1210.1171v2](https://arxiv.org/html/1210.1171v2).

The paper relates fixed-point sensitivity to spectral and mixing properties and bounds finite-time perturbations for processes converging to a unique stationary state. These assumptions provide useful long-time stability in mixing models. The present estimate instead uses a jump-tuple operator-norm distance and an entropy budget; it permits changing fixed-point algebras and requires no gap, mixing rate, or unique stationary state. The two kinds of control address different regimes.

## Learning and simulation

<a id="hkot2023"></a>
### Haah–Kothari–O'Donnell–Tang (2023): query-optimal unitary learning

Jeongwan Haah, Robin Kothari, Ryan O'Donnell, Ewin Tang, **“Query-optimal estimation of unitary channels in diamond distance,”** *64th IEEE Symposium on Foundations of Computer Science*, 363–390 (2023), [DOI](https://doi.org/10.1109/FOCS57990.2023.00028). The theorem comparison uses [arXiv:2302.14066v2](https://arxiv.org/html/2302.14066v2), revised 29 July 2024.

Theorem 1.1 outputs a classical unitary description with expected squared diamond error at most $`\varepsilon^2`$, using $`O(d^2/\varepsilon)`$ applications and one $`d`$-dimensional qudit. Its lower bound remains valid with inverse and controlled queries.

This project uses that existing learner. Ordinary controlled access allows learning $`\operatorname{diag}(I,U)`$ and fixing the otherwise unobservable global phase using the known identity block. A Hermitian reflection representative can then be recovered for the stability estimate. The additional step is translating learning accuracy into error for an entire controlled dissipative target. The resulting fixed-dimension query theorem does not remove the dimension-dependent cost of tomography or establish efficient simulation as the number of target qubits grows.

<a id="wang2026"></a>
### Wang–Ye (2026): general query-optimal Lindblad simulation

Chunhao Wang, Christopher Ye, **“Query-optimal quantum simulation of Lindblad evolution,”** [arXiv:2609.17490v2](https://arxiv.org/html/2609.17490v2), 25 September 2026.

Theorem 1 provides a general Lindblad simulation algorithm with additive dependence on the evolution-time and precision terms. Its access model uses block encodings of Hamiltonian and jump operators, including controlled access and adjoints; the output is a channel approximated in diamond norm. The paper also treats time dependence.

This is a direct general simulation comparator. The present problem fixes an unknown reflection oracle and asks how known target interventions with budget $`E`$ change the worst-case cost at fixed target dimension. A general worst-case time lower bound does not settle that restricted resource-dependent classification.

<a id="borras2026"></a>
### Borras–Marvian (2026): quantum-trajectory algorithms

Evan Borras, Milad Marvian, **“Quantum simulation algorithms based on quantum trajectories,”** *Quantum* **10**, 2063 (2026), [DOI and published article](https://quantum-journal.org/papers/q-2026-04-13-2063/). [Published full text](https://quantum-journal.org/papers/q-2026-04-13-2063/pdf/); arXiv:2509.10425v2.

Section 4 treats constant total jump rate, $`\sum_jL_j^\dagger L_j=\Gamma I`$, and gives simulation costs linear in evolution time, with an additional precision term. Theorem 6 and Corollary 6.1 discuss a general linear-time lower bound, including a single unitary jump of the form $`e^{iH}`$.

A generic unitary jump need not be a Hermitian involution. That distinction matters: an uncontrolled reflection dissipator can be simulated using the parity of a Poisson count. The present fixed-dimension lower bound comes from the intervening target controls and their entropy capacity, even with only one unknown reflection. Quantum trajectories also provide the linear-time upper bound that caps the classification.

## Informative-noise metrology and error correction

<a id="wan2022"></a>
### Wan–Lasenby (2022): parameter-dependent noise directions

Kianna Wan, Robert Lasenby, **“Bounds on adaptive quantum metrology under Markovian noise,”** *Physical Review Research* **4**, 033092 (2022). [Published article](https://doi.org/10.1103/PhysRevResearch.4.033092); [primary full text, arXiv:2108.11390v3](https://arxiv.org/pdf/2108.11390v3).

Appendix D explicitly distinguishes changing a noise direction from changing its scalar strength. Equation (D5) uses a rotating Hermitian dephasing operator and exhibits an unbounded instantaneous QFI rate over suitable state/SLD configurations. Equation (D8) gives a finite rate bound for scalar rescalings of fixed jump operators.

Consequently, informative noise orientation and the failure of a uniform instantaneous-QFI estimate for it are established. This project's bound concerns integrated finite-distance distinguishability with finite retained dimension and an entropy budget. An instantaneous QFI-rate statement does not imply or refute that bound.

<a id="das2025"></a>
### Das–Górecki–Demkowicz-Dobrzański (2025): adaptive time-scaling bounds

Arpan Das, Wojciech Górecki, Rafał Demkowicz-Dobrzański, **“Universal time scalings of sensitivity in Markovian quantum metrology,”** *Physical Review A* **111**, L020403 (2025). [Published article](https://doi.org/10.1103/PhysRevA.111.L020403); [arXiv:2404.03954v2](https://arxiv.org/html/2404.03954v2).

Equation (2) bounds the derivative of quantum Fisher information through a Kraus-gauge optimization involving an additive term and a term proportional to the square root of QFI. Both the Hamiltonian and jumps may depend on the parameter. The model explicitly permits arbitrarily large ancillary systems and arbitrarily fast, strong controls; the results classify linear and quadratic short- and long-time regimes.

These bounds establish broad adaptive-metrology limits. The present finite-separation converse charges retained dimension and the entropy-reduction capacities of common controls. It should not be described as a stronger QFI theorem: trace-distance Lipschitz continuity alone does not yield a QFI bound by squaring its coefficient.

<a id="chen2024"></a>
### Chen et al. (2024): the pure-reset informative-noise mechanism

Hongzhen Chen, Yu Chen, Jing Liu, Zibo Miao, Haidong Yuan, **“Quantum Metrology Enhanced by Leveraging Informative Noise with Error Correction,”** *Physical Review Letters* **133**, 190801 (2024). [Published article](https://doi.org/10.1103/PhysRevLett.133.190801); [author-hosted published Letter](https://hzchen.me/files/papers/Chen2024prl-preprint.pdf).

Theorem 1 characterizes Heisenberg scaling under sufficiently fast QEC using an effective generator containing both Hamiltonian and jump derivatives. For $`H=B(\cos\theta X+\sin\theta Z)`$ and $`L=\sqrt\gamma(\cos\theta X+\sin\theta Z)`$, their corrected protocol has QFI $`4(B^2+\gamma^2)t^2+4\gamma t`$. At $`B=0`$ it realizes the informative-noise signal and two-qubit code used in this project's pure-reset endpoint.

That mechanism is therefore prior. The present [mixed-reset construction](../science/mixed_resets.md) supplies an exact finite-cycle saturation example for a universal capacity-constrained converse. Chen et al. do not impose that entropy budget.

**Version distinction:** arXiv:2003.13010v1, titled “Fluctuation-enhanced quantum metrology,” contains an earlier code and a different sensitivity expression. The pure-noise quadratic term above is attributed to the published 2024 Letter.

<a id="liu2026"></a>
### Liu–Zhou (2026): subsystem recovery and mixed gauge states

Qiushi Liu, Sisi Zhou, **“Subsystem Quantum Error Correction for Noisy Quantum Metrology,”** [arXiv:2606.19628v1](https://arxiv.org/html/2606.19628v1), 17 June 2026.

The paper studies unitary signal encoding with fixed Pauli noise. Theorem 2 supplies syndrome-free subsystem codes with at most one noiseless ancilla under its algebraic condition. The recovery architecture includes CNOT, gauge reset, and CNOT operations; gauge reset is generally necessary for coherent signal accumulation.

Appendix A, Lemma 3 and equation (22), permits an arbitrary mixed gauge state $`\rho_G`$. Its effective logical Hamiltonian contains coefficients $`\langle H_{G,k}\rangle_{\rho_G}`$, so polarization-dependent logical signals are also already explicit. The recovery resets the gauge to that state.

This project credits both the reset architecture and the mixed-gauge signal mechanism. The additional claim is a converse expressed in the sum of control entropy capacities, together with an exact finite-cycle example and the resulting controlled-reflection query law.

## Purity, memory, and basis-discrimination examples

<a id="cable2016"></a>
### Cable–Gu–Modi (2016): metrology with weak polarization

Hugo Cable, Mile Gu, Kavan Modi, **“Power of One Bit of Quantum Information in Quantum Metrology,”** *Physical Review A* **93**, 040304(R) (2016). [Published article](https://doi.org/10.1103/PhysRevA.93.040304); [primary preprint](https://arxiv.org/abs/1504.02460).

Their unitary-encoding protocol combines pure, partially polarized, and maximally mixed qubits. Equation (11) contains a coherent contribution quadratic in the number of weakly polarized qubits times their polarization; the visibility includes a power of $`\cos\omega+i\epsilon\sin\omega`$.

Thus weak polarization can accumulate a coherent metrological signal in prior work. A qubit's small-polarization entropy deficit is quadratic in its polarization, making this an especially relevant antecedent to the resource scaling of mixed resets. The current construction places that scaling in a single-reflection dissipative model and matches a converse over all target controls with the same capacity budget.

<a id="kukita2021"></a>
### Kukita–Matsuzaki–Kondo (2021): collective dephasing-axis estimation

Shingo Kukita, Yuichiro Matsuzaki, Yasushi Kondo, **“Heisenberg-limited quantum metrology using collective dephasing,”** *Physical Review Applied* **16**, 064026 (2021). [Published article](https://doi.org/10.1103/PhysRevApplied.16.064026); [primary full text](https://arxiv.org/pdf/2103.11612).

This work estimates a relative polar angle of a collective dephasing direction using GHZ probes. The signal jump is a sum of single-spin Pauli operators; the model also allows independent noise and a Hamiltonian. It optimizes repeated interrogation with an interrogation time of order the inverse squared number of spins, treating preparation and readout time as negligible.

The [local-noise example](../science/memory_and_local_noise.md) instead uses independent local jumps with total rate normalized to one, and a single-use finite-distance calculation. The different jump structure, rate normalization, and time accounting must be retained when comparing sensitivity. Enhanced dephasing-axis estimation itself is prior.

<a id="puchala2021"></a>
### Puchała et al. (2021): repeated discrimination of projective measurements

Zbigniew Puchała, Łukasz Pawela, Aleksandra Krawiec, Ryszard Kukulski, Michał Oszmaniec, **“Multiple-shot and unambiguous discrimination of von Neumann measurements,”** *Quantum* **5**, 425 (2021). [Published article](https://quantum-journal.org/papers/q-2021-04-06-425/); [arXiv:1810.05122v4](https://arxiv.org/html/1810.05122v4).

Theorem 1 and Corollary 1 characterize repeated discrimination through an optimized spectral arc and show the optimality of parallel strategies. This is a direct precedent for entanglement-enhanced basis discrimination.

Its measurement channels output classical outcome labels. An unconditioned Lüders dephasing channel retains a quantum output in a parameter-dependent basis. The distinction prevents transferring a measurement-channel result without checking the output model. The local-noise calculation here works directly with the unmonitored quantum output.

<a id="das2026measurement"></a>
### Das et al. (2026): detector information and output conventions

Aritra Das, Simon K. Yung, Lorcán O. Conlon, Özlem Erkılıç, Angus Walsh, Yong-Su Kim, Ping K. Lam, Syed M. Assad, Jie Zhao, **“Precision bounds for characterising quantum measurements,”** *Nature Communications* (2026), [DOI](https://doi.org/10.1038/s41467-026-68529-7). The comparison uses [arXiv:2512.20091v1](https://arxiv.org/html/2512.20091v1).

The paper develops detector quantum Fisher information for estimating measurement parameters. Supplement IX addresses nonadditivity and possible quadratic scaling under entangled probes; Supplement X explicitly distinguishes measurements with classical outputs from processes that also retain quantum outputs.

It supplies another predecessor for enhanced measurement-parameter sensitivity and reinforces the need to specify which outputs are accessible. It does not impose a total retained-dimension or control-capacity budget for an unmonitored Hermitian-noise protocol.

## Feedback information and trajectory precision

<a id="honma2026"></a>
### Honma–Vu (2026): thermodynamic uncertainty with quantum feedback

Ryotaro Honma, Tan Van Vu, **“Thermodynamic Uncertainty Relation with Quantum Feedback,”** *Physical Review Letters* **137**, 160406 (16 October 2026), [DOI](https://doi.org/10.1103/6d8l-94pv). [Full Letter and Supplement, arXiv:2602.22651v1](https://arxiv.org/html/2602.22651v1).

Equation (15) bounds the relative variance of an antisymmetric monitored jump current. Its denominator is $`\Sigma=\Delta S_{\mathrm{sys}}+\Delta S_{\mathrm{env}}-\int dI`$, where $`dI`$ is the change in system-memory mutual information across feedback. The setup uses local-detailed-balance pairs of jumps and unital jump-conditioned feedback. It allows arbitrary initial states and durations; stationarity is not a distinguishing requirement.

Supplement equation (S73) uses scalar jump perturbations, leaving Hamiltonian and feedback fixed. The information term is trajectory- and feedback-dependent, whereas this project's $`\kappa(\mathcal C)`$ is the maximum entropy decrease of a control channel over all inputs. The present theorem concerns arbitrary Hermitian jump-direction changes and full unmonitored-channel diamond distance. These differences in perturbation, output, and resource definition prevent identifying the two bounds.

## Scope of the contribution

The project builds on established entropy inequalities, channel capacity, unitary learning, and informative-noise correction. Its central mathematical statement is the global two-channel bound with explicit retained dimension and control entropy capacity. Its central algorithmic consequence is the matching worst-case query classification for a fixed two-qubit target with a single unknown reflection.

The examples establish saturation within that stated contract. They do not claim the first use of GHZ probes for dephasing-axis sensing, a new error-correction architecture, a new role for weak polarization, or a general QFI bound. The informational capacity definition also stands independently of any thermodynamic implementation.
