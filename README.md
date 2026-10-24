# Quantum Records and Coherence

How much interference can remain when many environmental fragments each record the same binary alternative, but those records are not exactly independent?

## Principal result

A balanced qubit is correlated with $N$ selected record fragments. Each fragment has a local binary decoder whose error is at most $\varepsilon$ **for each alternative**, with $0<\varepsilon<1/2$. In each conditional record state, the quantum total correlation among these $N$ fragments is at most $C$ nats. Visibility means the qubit's actual, unconditioned fringe visibility, not coherence recovered by erasing or postselecting records.

For every fixed $C>0$ and fixed $\varepsilon$,

$$
\lim_{N\to\infty}\sqrt{N}\,v_{\max}(N,\varepsilon,C)
=2\sqrt{\frac{C}{(1-2\varepsilon)\ln[(1-\varepsilon)/\varepsilon]}}.
$$

At exactly $C=0$,

$$
v_{\max}(N,\varepsilon,0)=[2\sqrt{\varepsilon(1-\varepsilon)}]^N.
$$

The result is a worst-case, attainable envelope: allowing any fixed positive total-correlation budget changes exponential suppression to algebraic suppression. It does **not** say that every correlated environment retains that visibility.

A second construction has exactly independent conditional **pairs** of records, a bounded total-correlation budget, and visibility of order $N^{-1/2}$. Thus pairwise independence does not restore the exponential envelope. The general distinction between pairwise and full independence is prior work; the quantitative simultaneous construction is the contribution investigated here.

## Scientific reading route

| Question | Authoritative account |
|---|---|
| What is constrained, and how does a quantum record reduce to a classical distribution? | [Operational model](science/model.md) |
| Where is the finite-size converse and exact asymptotic coefficient proved? | [Sharp upper bound](science/sharp-bound.md) |
| What attains the coefficient, and what does the circuit cost? | [Matching constructions](science/constructions.md) |
| Can every conditional pair be independent? | [Pairwise-independent records](science/pairwise-independence.md) |
| What does the theorem not imply? | [Physical scope](science/scope.md) |
| Which ingredients and comparisons come from prior work? | [Related work and review limits](references/related-work.md) |
| How are the formulas and quantum realizations checked? | [Verification](verification/README.md) |

The complete proof route starts at [science/README.md](science/README.md). The reproducible script checks 149 finite parameter/state cases, including a gate-level star-circuit calculation. These checks support the formulas; the asymptotic statements rest on the written proofs.

**Scope that matters:** the attaining quantum realizations allow an additional unobserved environment/purifier. The budget covers correlations among the selected record fragments, not correlations with that additional environment. Attainability with a pure conditional state of an exhaustive $N$-fragment environment is not established. The two closest 2026 full-text comparisons remain unresolved because only their primary-source abstracts/descriptions were retrievable; no priority certification is claimed.

## Reproduction

```bash
python -m pip install -r verification/requirements.txt
python verification/check_records.py
```

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
