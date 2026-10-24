# Scientific account

The central distinction is between many locally readable records and many *conditionally independent* records. A rare common error can have small total-correlation cost while preserving substantially more interference than independent errors do.

Read [the model](model.md), [the converse](sharp-bound.md), [the matching realization](constructions.md), and [the pairwise-independent construction](pairwise-independence.md), then [the physical scope](scope.md).

## Claim-to-proof map

| Claim | Proof location | Finite check |
|---|---|---|
| Quantum visibility is bounded by decoded Bhattacharyya affinity; decoding cannot increase total correlation | Model, quantum-to-classical reduction | Random noncommuting conditional states |
| Every classical record pair has a quantum realization with the same correlation and affinity | Model, positive completion | Explicit isometry and partial trace |
| Exact independent-record envelope | Sharp upper bound, independent endpoint | Product distributions |
| Fixed-positive-budget sharp coefficient | Sharp upper bound, three-region argument; matching constructions | Convergence through $N=100000$ |
| Linear-gate star circuit attains the leading coefficient | Matching constructions, physical circuit | Direct rotation/CNOT state simulation |
| Exact conditional pairwise independence and algebraic visibility under any positive fixed budget | Pairwise-independent records | Hypergeometric moments and entropy certificate |

The proofs are reconstructed here in full. Numerical checks are not independent expert review. The [related-work account](../references/related-work.md) and [Bavaro comparison](../references/bavaro-comparison.md) separate inherited envelopes and correlation bounds from the sharp fixed-budget result and its witnesses.
