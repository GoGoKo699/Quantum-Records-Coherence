# Operational model

## System, records and visibility

Let $S$ be a qubit with a fixed pointer basis, and let $E=E_1\cdots E_N$ be the **selected** record fragments. All Hilbert spaces are finite-dimensional; the bound does not depend on their dimensions. Consider any positive, trace-one state

```math
\rho_{SE}=\frac12
\begin{pmatrix}
\rho_E^0&A\\
A^\dagger&\rho_E^1
\end{pmatrix},
\qquad \mathrm{Tr}\rho_E^x=1.
```

The alternatives have equal prior probabilities. The actual normalized fringe visibility measured on $S$ is

```math
v=2|\langle0|\rho_S|1\rangle|=|\mathrm{Tr}A|.
```

No environment-assisted recovery, outcome conditioning or postselection is included in this definition. The total state may be mixed. A purification may occupy an additional register $R$ outside the selected fragments.

## Local readability and correlation budget

Each $E_i$ has a fixed two-outcome POVM $\lbrace M_i^0,M_i^1\rbrace$ satisfying

```math
\mathrm{Tr}(M_i^1\rho_{E_i}^0)\le\varepsilon,
\qquad
\mathrm{Tr}(M_i^0\rho_{E_i}^1)\le\varepsilon.
```

This is a bound on **both conditional errors**, not merely their average. Decoders can differ between fragments, and no permutation symmetry is assumed in the converse.

For each $x\in\lbrace 0,1\rbrace$ impose

```math
T_x=D\!\left(\rho_E^x\,\middle\|\,\bigotimes_{i=1}^N\rho_{E_i}^x\right)
=\sum_{i=1}^N S(\rho_{E_i}^x)-S(\rho_E^x)\le C.
```

All logarithms are natural; entropies and correlation budgets are in nats. This is correlation conditioned on the classical pointer alternative. It is not an unspecified conditional mutual information with a coherent conditioning system. The budget excludes correlations with $S$ and with an additional purifier.

Define $v_{\max}(N,\varepsilon,C)$ as the supremum of $v$ over this class. No spatial locality, preparation-time, native gate-set or purity constraint is imposed on that supremum.

## Quantum-to-classical reduction

Apply all the local decoders and write their joint output as $Y\in\lbrace 0,1\rbrace^N$. The conditional laws $P_x$ obey

```math
P_0(Y_i=1)\le\varepsilon,\qquad P_1(Y_i=0)\le\varepsilon.
```

The same product measurement maps $\bigotimes_i\rho_{E_i}^x$ to $\bigotimes_iP_{x,i}$. Quantum relative-entropy data processing therefore gives

```math
D(P_x\|Q_x)\le T_x\le C,
\qquad Q_x=\bigotimes_iP_{x,i}.
```

The post-measurement state has, for each outcome $y$, a positive qubit block proportional to

```math
\begin{pmatrix}P_0(y)&a_y\\a_y^\ast&P_1(y)\end{pmatrix}.
```

Positivity gives $|a_y|\le\sqrt{P_0(y)P_1(y)}$. Since the measurement is trace-preserving, $\sum_y a_y=\mathrm{Tr}A$. Hence

```math
v\le B(P_0,P_1):=\sum_y\sqrt{P_0(y)P_1(y)}.
```

This proves the reduction directly for actual visibility; it does not assume that visibility equals a fidelity envelope for an arbitrary given state. The standard quantum-information ingredients are documented in [Watrous, Chapters 2, 3 and 5](../references/related-work.md).

## Positive completion and exact classical attainability

Conversely, for any two classical laws define the unnormalized vectors

```math
|\chi_y\rangle=\sqrt{P_0(y)}|0\rangle+\sqrt{P_1(y)}|1\rangle
```

and the state

```math
\rho_{SE}=\frac12\sum_y|\chi_y\rangle\langle\chi_y|\otimes|y\rangle\langle y|.
```

It is positive and trace one, its conditional record states are diagonal with laws $P_x$, its quantum total correlations equal the classical total correlations, and its visibility is exactly $B(P_0,P_1)$. Thus the quantum and classical suprema in this declared model coincide, and qubit record registers suffice to attain the classical constructions.

An explicit isometry is

```math
|x\rangle_S\longmapsto |x\rangle_S\sum_y\sqrt{P_x(y)}|y\rangle_E|y\rangle_R.
```

The two images are orthonormal because the system labels are orthogonal. It extends to a unitary with initially pure environment registers. Tracing $R$ gives the displayed positive completion. This realization uses $N$ additional purifier qubits; its general state-preparation gate cost is not bounded here. A simpler linear-gate realization attains the sharp *leading coefficient* in [Matching constructions](constructions.md).
