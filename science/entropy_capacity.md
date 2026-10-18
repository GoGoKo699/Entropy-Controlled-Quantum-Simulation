# Entropy-decrease capacity of a control

The capacity used in the [controlled-noise model](model.md) measures how much a specified control can decrease the entropy of the retained system. It is the negative of minimum entropy gain, an established channel quantity; see [Alicki's entropy-gain results](../references/RELATED_WORK.md#alicki2004). This file proves the properties needed for [channel stability](channel_stability.md) and fixes the accounting for references, resets, and classical records.

All spaces are finite dimensional. All logarithms are natural, so entropy is measured in nats. A channel is completely positive and trace preserving (CPTP). Write

```math
S(\rho)=-\mathrm{Tr}\rho\log\rho,
\qquad
I(A:R)_\rho=S(\rho_A)+S(\rho_R)-S(\rho_{AR}).
```

The convention is $`0\log0=0`$.

<a id="definition"></a>

## 1. Definition and elementary bounds

Let $`\mathcal C`$ be a channel on a retained system $`A`$ of dimension $`D`$, with equal input and output dimensions. Define

```math
\boxed{
\kappa(\mathcal C)
=\max_{\rho_A}
\left\{S(\rho_A)-S(\mathcal C(\rho_A))\right\}.
}
```

The maximum exists because the state space is compact and finite-dimensional entropy is continuous. For every channel,

```math
0\leq\kappa(\mathcal C)\leq\log D.
```

The upper bound follows from $`S(\rho_A)\leq\log D`$ and nonnegativity of output entropy. For the lower bound, use the maximally mixed input:

```math
\kappa(\mathcal C)
\geq \log D-S\!\left(\mathcal C(I_D/D)\right)
\geq0.
```

### Zero capacity is equivalent to unitality

If $`\mathcal C`$ is unital, then $`\mathcal C(I_D/D)=I_D/D`$. Data processing of relative entropy gives

```math
D\!\left(\mathcal C(\rho)\middle\|I_D/D\right)
\leq
D\!\left(\rho\middle\|I_D/D\right).
```

Using $`D(\rho\|I_D/D)=\log D-S(\rho)`$ yields $`S(\mathcal C(\rho))\geq S(\rho)`$ for every input. Thus $`\kappa(\mathcal C)=0`$.

Conversely, if $`\mathcal C`$ is not unital, its output on $`I_D/D`$ is not maximally mixed. The maximally mixed state uniquely maximizes entropy, so

```math
\log D-S\!\left(\mathcal C(I_D/D)\right)>0.
```

Therefore

```math
\boxed{\kappa(\mathcal C)=0
\quad\Longleftrightarrow\quad
\mathcal C\text{ is unital}.}
```

In particular, unitary controls, mixtures of unitary controls, and nonselective projective measurements have zero capacity. The relative-entropy data-processing theorem and entropy conventions are recorded under [Lindblad](../references/RELATED_WORK.md#lindblad1975) and [Watrous](../references/RELATED_WORK.md#watrous2018).

<a id="reference-invariance"></a>

## 2. An untouched reference does not increase capacity

Let $`R`$ be an arbitrary finite-dimensional reference. A local channel on $`A`$ leaves the $`R`$ marginal unchanged. For a joint input $`\rho_{AR}`$, write $`\rho'_{AR}=(\mathcal C\otimes\mathrm{Id}_R)(\rho_{AR})`$. Then

```math
\begin{aligned}
S(\rho_{AR})-S(\rho'_{AR})
={}&S(\rho_A)-S(\mathcal C(\rho_A))\\
&-\left[I(A:R)_\rho-I(A:R)_{\rho'}\right].
\end{aligned}
```

Mutual information cannot increase under a channel on $`A`$. Consequently,

```math
\boxed{
S(\rho_{AR})-S\!\left(
(\mathcal C\otimes\mathrm{Id}_R)(\rho_{AR})
\right)
\leq\kappa(\mathcal C).
}
```

Product states $`\rho_A\otimes\rho_R`$, with $`\rho_A`$ maximizing the definition, achieve equality in the optimization over joint inputs. Thus

```math
\kappa(\mathcal C\otimes\mathrm{Id}_R)
=\kappa(\mathcal C).
```

No reference optimization is hidden in the definition of $`\kappa`$. This invariance is what permits the same control budget in an arbitrary-input diamond-norm theorem.

## 3. Composition, products, and mixtures

### Composition

For channels $`\mathcal B,\mathcal C`$ on the same retained system,

```math
\begin{aligned}
S(\rho)-S(\mathcal C\mathcal B(\rho))
={}&S(\rho)-S(\mathcal B(\rho))\\
&+S(\mathcal B(\rho))-S(\mathcal C\mathcal B(\rho))\\
\leq{}&\kappa(\mathcal B)+\kappa(\mathcal C).
\end{aligned}
```

Maximizing over the input proves

```math
\boxed{
\kappa(\mathcal C\circ\mathcal B)
\leq\kappa(\mathcal C)+\kappa(\mathcal B).
}
```

### Tensor products

Let $`\mathcal B`$ act on $`B`$ and $`\mathcal C`$ on $`A`$. For a joint input, the difference of joint entropies can be written as the sum of the two marginal entropy decreases minus the decrease of mutual information. Data processing therefore gives

```math
\kappa(\mathcal C\otimes\mathcal B)
\leq\kappa(\mathcal C)+\kappa(\mathcal B).
```

Independent inputs maximizing the two capacities give the reverse inequality. Hence

```math
\boxed{
\kappa(\mathcal C\otimes\mathcal B)
=\kappa(\mathcal C)+\kappa(\mathcal B).
}
```

This is the additivity of negative minimum entropy gain, with the sign convention used here.

### Convex mixtures

For probabilities $`a_\ell`$, entropy concavity gives

```math
S\!\left(\sum_\ell a_\ell\mathcal C_\ell(\rho)\right)
\geq
\sum_\ell a_\ell S(\mathcal C_\ell(\rho)).
```

It follows that

```math
\boxed{
\kappa\!\left(\sum_\ell a_\ell\mathcal C_\ell\right)
\leq\sum_\ell a_\ell\kappa(\mathcal C_\ell).
}
```

In particular, let $`\mathcal D_D(\rho)=I_D\mathrm{Tr}(\rho)/D`$ denote complete depolarization. Since $`\mathcal D_D`$ is unital,

```math
\kappa\!\left((1-\epsilon)\mathcal C+\epsilon\mathcal D_D\right)
\leq(1-\epsilon)\kappa(\mathcal C).
```

This inequality ensures that the full-rank regularization in the [stability proof](channel_stability.md#singular-states) does not increase the budget.

### Change of basis

Precomposition or postcomposition by a unitary channel leaves $`\kappa`$ unchanged. Output entropy is unchanged by the latter operation, and unitary conjugation gives a bijection of input states for the former. Reset capacity is therefore independent of the known encoding basis in which the reset is performed.

<a id="reset-capacity"></a>

## 4. Exact capacity of a replacement

Suppose the retained system is $`A\otimes B`$, with $`\dim A=a`$. Replacing $`A`$ with a fixed state $`\tau_A`$ while keeping $`B`$ is the channel

```math
\mathcal R_\tau(\rho_{AB})
=\tau_A\otimes\rho_B.
```

For an arbitrary input,

```math
\begin{aligned}
S(\rho_{AB})-S(\mathcal R_\tau(\rho_{AB}))
&=S(A\mid B)_\rho-S(\tau_A)\\
&\leq\log a-S(\tau_A).
\end{aligned}
```

Equality holds on $`(I_A/a)\otimes\rho_B`$. Therefore

```math
\boxed{
\kappa(\mathcal R_\tau)=\log a-S(\tau_A).
}
```

By reference invariance this formula already allows correlations with any untouched external reference.

For a qubit replacement

```math
\tau_b=\frac{I+bZ}{2},
\qquad 0\leq b\leq1,
```

define the binary entropy with natural logarithms by

```math
h(x)=-x\log x-(1-x)\log(1-x).
```

The exact capacity is

```math
\begin{aligned}
e(b)
&=\log2-h\!\left(\frac{1+b}{2}\right)\\
&=\frac12\left[(1+b)\log(1+b)+(1-b)\log(1-b)\right].
\end{aligned}
```

For $`|b|<1`$, differentiating gives $`e'(b)=\mathrm{artanh}b`$. Integrating its power series and using $`e(0)=0`$ yields

```math
e(b)
=\sum_{k=1}^{\infty}\frac{b^{2k}}{(2k-1)(2k)}.
```

The identity extends to $`b=1`$ by continuity and monotone convergence. All coefficients are positive, the first is $`1/2`$, and their sum is $`e(1)=\log2`$. Since $`b^{2k}\leq b^2`$ on $`[0,1]`$,

```math
\boxed{
\frac{b^2}{2}\leq e(b)\leq(\log2)b^2.
}
```

Thus a pure-qubit reset costs $`\log2`$, whereas replacement by $`I/2`$ has capacity zero. For $`0<b\ll1`$, capacity is quadratic in the polarization, $`e(b)=b^2/2+O(b^4)`$. The [mixed-reset construction](mixed_resets.md) uses this exact dependence.

## 5. An implementation bound from a discarded environment

Suppose a known control is realized by coupling the retained system to an initially independent environment $`F`$ of dimension $`f`$ in state $`\tau_F`$, applying a joint unitary, and discarding $`F`$. If $`\omega_{AF}`$ is the state after that unitary, then

```math
S(\omega_{AF})=S(\rho_A)+S(\tau_F).
```

Consequently,

```math
\begin{aligned}
S(\rho_A)-S(\omega_A)
&=S(F\mid A)_\omega-S(\tau_F)\\
&\leq\log f-S(\tau_F).
\end{aligned}
```

Maximizing the input gives

```math
\boxed{
\kappa(\mathcal C)\leq\log f-S(\tau_F).
}
```

This supplies a usable bound when the controller's channel is specified through an environment implementation. It bounds entropy decrease of the retained system. The results here impose no temperature or energy model and make no assertion about a work cost. The separate relation of entropy decrease to process thermodynamic capacity is discussed in the [related work](../references/RELATED_WORK.md#faist2019).

<a id="control-budget"></a>

## 6. Budget of a specified control sequence

For a target with controls $`\mathcal C_0,\ldots,\mathcal C_r`$, including any initial and terminal controls, define

```math
E_{\mathrm{used}}
=\sum_{k=0}^{r}\kappa(\mathcal C_k).
```

The model promises $`E_{\mathrm{used}}\leq E`$. This is the capacity of the specified controls at their specified positions. It is not a minimization over all decompositions of the eventual target channel. Composition subadditivity explains why replacing adjacent controls by their composition can give a smaller upper bound.

Since every summand is nonnegative, $`E_{\mathrm{used}}=0`$ holds exactly when every specified control is unital.

If the retained space consists of $`q`$ qubits, then $`\log D=q\log2`$. If the controls contain at most $`R`$ individual pure-qubit resets and all other operations are unital, the preceding properties imply

```math
E_{\mathrm{used}}\leq R\log2.
```

Replacement count and entropy capacity are distinct. A sequence can use many replacements by weakly polarized states while having small total capacity. Conversely, any classical measurement record retained between sensing intervals occupies part of the retained space. Conditional feedback is represented as a common channel on that space. If the record is forgotten, the corresponding discard or replacement is included among the controls. A final readout is covered by data processing of the final channel distance.

The [stability theorem](channel_stability.md#main-theorem) uses $`E_{\mathrm{used}}`$ to bound how much entropy production can occur during the noisy intervals. The [query theorem](query_complexity.md#query-theorem) classifies targets by an upper bound $`E`$ on this quantity.
