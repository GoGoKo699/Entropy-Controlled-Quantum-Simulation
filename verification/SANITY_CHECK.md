# Repository sanity check

Reviewed on **24 October 2026**, starting from commit [`51f7d4bc586796d9f2de52e2e98770874bec734a`](https://github.com/GoGoKo699/Entropy-Controlled-Quantum-Simulation/tree/51f7d4bc586796d9f2de52e2e98770874bec734a). The scientific statements survived the review without a substantive defect found. The corrections below affect hosted notation and attribution; they do not change a theorem or resource model.

## Scientific review

| Account | Arguments checked |
|---|---|
| [Entropy capacity](../science/entropy_capacity.md) | Unitality, reference invariance, composition, tensor additivity, convexity, and exact replacement capacity. |
| [Channel stability](../science/channel_stability.md) | Pinsker normalization, both commutator estimates, Duhamel interpolation, the reference-independent entropy budget, CPTP control jumps in the backward variance, full diamond-norm completion, and regularization of singular inputs and every control. |
| [Query complexity](../science/query_complexity.md) and [mixed resets](../science/mixed_resets.md) | Bounded Poisson sampling, the imported unitary-learning guarantee, identity-block phase fitting, averaging of fitted channels, exact cycle coherence, all real-time/capacity regimes, finite separation constants, and the adaptive ordinary-oracle hybrid. |
| [Memory and local noise](../science/memory_and_local_noise.md) | GHZ signal and entropy, separable-block fidelity, the local query law, rate normalization, pure-reset decoding, and resource rounding. |

The headline, model, proofs, examples, interpretation, and learning route use the same resource boundaries: fixed target dimension and fixed error for the main query theorem; capacity charged to every target control; unrestricted but query-charged simulator probes; genuinely untouched references; and a supplied matched Hermitian-jump representation for the general channel theorem.

The learning theorem was checked against Haah–Kothari–O'Donnell–Tang, [arXiv:2302.14066v2](https://arxiv.org/html/2302.14066v2), Theorem 1.1 and Proposition 1.6. The relevant expected squared full-diamond error and bounded forward-query guarantees support the stated upper bound.

## Reproduction and finite checks

Executed in Python 3.12.14 with NumPy 2.3.5 and SciPy 1.17.0:

```bash
python3 verification/checks.py --output /tmp/ecqs-audit-results.json
python3 -O verification/checks.py
```

The normal run passed and its parsed JSON exactly matched [expected_results.json](expected_results.json): two controlled protocols, 36 direct two-qubit circuits, 12 positive-budget witnesses, and 12 local-spin points. The maximum circuit residual was below $`1.24\times10^{-15}`$. Optimized execution failed with the intended assertion-protection error.

Additional finite screening checked 2,000 random anchored-unitary fits, noninteger-time witness grids, local-query inequalities, and an independently implemented encoded pure-reset circuit. These checks found no counterexample. They are supplemental screening, not additional committed reproduction commands or substitutes for the written proofs.

## Learning and navigation

The map contains exactly M01–M30, with 10 background/preliminary and 20 narrative/innovation milestones. Every milestone has the required understanding-target fields and backward-pointing declared dependencies. Watrous remains the sole educational anchor; its section and theorem pointers were checked against the author-hosted chapters. The base revision's 286 local file/fragment links had no broken target; the final corrected tree passed all 296 such links. All 20 bibliography keys are unique, and the topic-based science and LLM routes are coherent. No personal coaching records or obsolete manuscript entrypoint are present.

## Hosted mathematics and corrections

Inspected actual GitHub rendering of the README, Watrous bridge, milestone map, and all seven substantive science pages. Representative README, stability, bridge, milestone, and query formulas were also inspected visually. Rendered formula counts agreed with the source after the query-page correction: README 23; bridge 126; milestones 120; model 64; capacity 91; stability 153; mixed resets 116; query complexity 180; memory/local noise 148; interpretation 55.

GitHub reported `Missing \end{cases}` in the query proof's budget-dependent polarization formula. Replacing the two literal less-than signs inside that cases block by the equivalent `\lt` notation repaired it. The repaired branch rendered all 180 query-page formulas, with no pending formula or renderer error; the cases block was inspected visually. Source validity alone would not have caught this hosted defect.

The [related-work account](../references/RELATED_WORK.md) and [bibliography](../references/references.bib) now use Honma–Vu [arXiv:2602.22651v2](https://arxiv.org/html/2602.22651v2), revised 22 October 2026. Its antisymmetric-current, local-detailed-balance, unital-feedback, and scalar-perturbation assumptions preserve the existing comparison. The account also includes Chen–Gao–Wang–Zhou [arXiv:2609.18757v1](https://arxiv.org/html/2609.18757v1) as a general simulation comparator, distinguishing its encoding model and general query optimality from the capacity-dependent classification here.

## Limits

This is a reconstruction of written arguments, finite numerical reproduction and screening, targeted primary-literature checking, and representative hosted visual inspection. It is not machine formalization, independent expert certification, an exhaustive priority search, or a publication prediction. The numerical suite does not implement the unitary learner or certify universal diamond-norm bounds. These limits do not supply an unresolved defect in the inspected contribution.
