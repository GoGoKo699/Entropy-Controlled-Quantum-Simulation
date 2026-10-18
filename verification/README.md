# Finite numerical verification

The [check script](checks.py) verifies finite matrix identities, selected inequalities, and explicit witness formulas. It uses a fixed random seed and small dense matrices. It is independent of the analytical proofs in [science](../science/README.md): numerical agreement does not prove the all-dimension stability theorem, asymptotic query bounds, or the uniform parameter estimates.

## Run

From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 verification/checks.py
```

A successful run prints PASS, the numbers of checked parameter points, and the largest two-qubit circuit residual. Any failed assertion exits unsuccessfully. Run Python normally, without its optimization flag; the script explicitly rejects optimized execution because assertions carry the numerical checks.

The script writes no files by default. To save its full numerical report:

```bash
python3 verification/checks.py --output /tmp/ecqs-results.json
```

The optional output path is chosen by the caller. The committed [expected results](expected_results.json) are a reference numerical record, not a file that a normal run overwrites.

The reference environment is Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. The two numerical packages are pinned in [requirements](../requirements.txt).

## What is checked

| Calculation | Finite instances | Independent comparison |
|---|---|---|
| Controlled forward/backward identities | Two nonunital replacements, each between two noise intervals on one qubit with an untouched qubit reference | Duhamel integral versus a matrix-exponential Fréchet derivative; integrated carré-du-champ plus the control jump versus the endpoint variance difference |
| Entropy and commutator estimates | The same two controlled protocols with full-rank joint inputs, three Hermitian jumps, and a common Hamiltonian | Integrated entropy production versus the exact entropy changes; Pinsker commutator bound; control capacity and total entropy budget |
| Two-qubit mixed-reset circuit | 36 combinations of polarization, cycle count, and angle, including zero and pure polarization | Direct density-matrix evolution and replacement versus the exact logical coherence $`f_b(\theta)^N`$; reflection identities and fixed CNOT conjugation |
| Positive-budget finite witnesses | 12 parameter points, with cycle counts from 1 to 1000 | Constant trace-norm gap; bounds on $`e(b)`$; actual baseline entropy removed compared with the advertised capacity |
| Local GHZ witnesses | 1–6 spins at local times 0.3 and 1 | Explicit mixtures over every jump-parity subset versus the binomial readout formula and the entropy $`n h(r)`$ |

The common pseudorandom seed is 41018. It fixes the Hermitian matrices, full-rank input, and observable in the controlled-identity checks. The continuous integrals use 80-point Gauss–Legendre quadrature. The local GHZ checks enumerate all subsets only for the listed small systems.

The mixed-reset gap stored under the JSON field name "trace_distance" is the **unhalved trace norm** $`\|\rho_\theta-\rho_0\|_1=|f_b(\theta)^N-1|`$, consistent with the scientific notes. It is not half that value.

## Tolerances and reference values

Integral identities and the associated combined inequalities use tolerance $`10^{-8}`$. Direct matrix identities, output comparisons, and the GHZ formulas use $`10^{-10}`$; some elementary capacity bounds use $`10^{-12}`$. Positivity and entropy inequalities allow only the stated small numerical tolerance.

The reference file records residuals much smaller than those thresholds:

| Reference residual | Recorded value |
|---|---:|
| Maximum Duhamel identity error | $`1.4\times10^{-17}`$ |
| Maximum controlled variance identity error | $`2.3\times10^{-16}`$ |
| Maximum integrated entropy identity error | $`8.9\times10^{-16}`$ |
| Maximum two-qubit circuit matrix error | $`1.3\times10^{-15}`$ |
| Maximum local-spin readout error | $`4.5\times10^{-16}`$ |
| Maximum local-spin entropy error | $`3.6\times10^{-15}`$ |

Values displayed here are rounded upward from the recorded results. Floating-point residuals can change across BLAS/LAPACK versions and machines. The scientific assertions and their tolerances determine success; byte-for-byte equality with the reference JSON is not required.

## What is established analytically instead

The [channel-stability proof](../science/channel_stability.md) establishes the uniform statement, including arbitrary references, arbitrary finite sequences of common CPTP controls, and singular-state regularization. The finite checks sample full-rank states; they do not replace the singular-state argument or optimize a diamond norm.

The [mixed-reset derivation](../science/mixed_resets.md) proves all exposure-time and budget regimes, including noninteger time and zero budget. The finite grid checks unit-duration intervals and selected parameters.

The [memory and local-noise derivation](../science/memory_and_local_noise.md) proves the exact query law, the separable-probe estimate, the all-size entropy identity, and the weighted retained-qubit/pure-reset construction. The finite GHZ grid does not certify these universal statements.

The [query-complexity proof](../science/query_complexity.md) supplies the learning upper bound, phase fit, Poisson truncation, and hybrid lower bound. This script does not implement unitary tomography, search for an optimal simulator, or verify originality relative to prior work.
