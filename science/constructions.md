# Matching constructions

Use the notation and model in [Sharp upper bound](sharp-bound.md) and [Operational model](model.md).

## 1. A rare common error

For fixed $C>0$ and sufficiently large $N$, choose the unique $t_N\in(0,\varepsilon)$ satisfying

```math
N[h(\varepsilon)-h(a_N)]=C,\qquad
 a_N=\frac{\varepsilon-t_N}{1-2t_N}.
```

Existence and uniqueness follow because $a_N$ decreases continuously from $\varepsilon$ to zero as $t_N$ increases from zero to $\varepsilon$, and $h$ is strictly increasing on $(0,1/2)$. The finite condition is $C<Nh(\varepsilon)$.

Define

```math
R_0=\mathrm{Bern}(a_N)^{\otimes N},\qquad
R_1=\mathrm{Bern}(1-a_N)^{\otimes N},
```

```math
P_0=(1-t_N)R_0+t_NR_1,\qquad
P_1=t_NR_0+(1-t_N)R_1.
```

Every marginal error is exactly $a_N+t_N(1-2a_N)=\varepsilon$. Entropy of a mixture lies between its average component entropy and that quantity plus the mixing entropy. Since $H(R_0)=H(R_1)=Nh(a_N)$,

```math
C-h(t_N)\le D(P_x\|\textstyle\bigotimes_iP_{x,i})\le C.
```

The construction therefore meets the budget for every $N$ in its stated domain, not merely asymptotically.

## 2. Affinity and the coefficient

For nonnegative $r,s$ and $0\le t\le1/2$,

```math
\sqrt{[(1-t)r+ts][tr+(1-t)s]}
=\sqrt{t(1-t)(r+s)^2+(1-2t)^2rs}.
```

Bounding the square root below by the first term and above by the sum of square roots yields

```math
2\sqrt{t_N(1-t_N)}\le B(P_0,P_1)
\le2\sqrt{t_N(1-t_N)}+(1-2t_N)[2\sqrt{a_N(1-a_N)}]^N.
```

The second term is exponentially small. Taylor expansion at $t=0$ gives

```math
h(\varepsilon)-h\!\left(\frac{\varepsilon-t}{1-2t}\right)
=J_\varepsilon t+O(t^2).
```

Thus $Nt_N\to C/J_\varepsilon$, and both bounds have leading term $2\sqrt{C/(NJ_\varepsilon)}$. Together with the converse,

```math
\lim_{N\to\infty}\sqrt N\,v_{\max}(N,\varepsilon,C)
=2\sqrt{C/J_\varepsilon}.
```

The [positive completion](model.md) attains the full classical affinity exactly. The following simpler circuit attains the same leading coefficient.

## 3. An explicit star circuit

Take one extra control qubit $F$ and $N$ initially independent noisy record qubits $E_i$ with diagonal state $\mathrm{diag}(1-a_N,a_N)$. Prepare

```math
|f\rangle_F=\sqrt{1-t_N}|0\rangle+\sqrt{t_N}|1\rangle,
\qquad |+\rangle_S=(|0\rangle+|1\rangle)/\sqrt2.
```

Apply a CNOT from $S$ to $F$, followed by a CNOT from $F$ to every $E_i$. Conditioned on the system alternative, $F$ has opposite weights. Tracing out $F$ gives exactly the two displayed record laws: a common bit $F$ flips all the independently noisy records.

The system visibility after the first CNOT is

```math
\langle f|X|f\rangle=2\sqrt{t_N(1-t_N)}.
```

All later gates act only on the environment, so they leave the reduced state of $S$ unchanged. This is the visibility at the end, not a visibility restored by erasure or selection. The initial state of $F$ is a coherent superposition: replacing it by its diagonal mixture preserves the record probabilities but gives zero system visibility. Classical common noise alone is not being claimed to create coherence.

To make the entire preparation pure and unitary, purify each noisy $E_i$ with another qubit $R_i$, initially in

```math
\sqrt{1-a_N}|0\rangle_{E_i}|0\rangle_{R_i}
+\sqrt{a_N}|1\rangle_{E_i}|1\rangle_{R_i}.
```

Starting from zero states, apart from preparation of $|+\rangle_S$, the circuit uses $N+1$ single-qubit rotations and $2N+1$ CNOTs. It has $N$ selected records and $N+1$ additional environment qubits ($F,R_1,\ldots,R_N$). A sequential implementation has $O(N)$ gate count and depth when these couplings and arbitrary-angle rotations are available. This is not a finite-gate-set synthesis or geometric-locality claim. No postselection, reset, uncomputed work register or free data-loading oracle is invoked.

The extra environment is load-bearing: only correlations among the $E_i$ are constrained by $C$. Reclassifying the control and purifiers as part of an exhaustive set of constrained fragments changes the problem. The circuit also does not imply that increasing record number in a fixed natural Hamiltonian tunes $t_N$ automatically.

## 4. Mechanism

Under an independent product reference, a record pattern typical of the opposite alternative costs an exponential probability factor with exponent $NJ_\varepsilon$. Giving such patterns weight $t_N=\Theta(1/N)$ therefore costs only $\Theta(1)$ relative entropy. Visibility is sensitive to square roots of these weights, producing $\Theta(N^{-1/2})$ interference. The three-region proof shows that no other admissible mechanism can improve the leading coefficient in the declared model.
