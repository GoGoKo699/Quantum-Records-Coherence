# Comparison with Bavaro's fragmented-record bounds

## Source and inspected scope

Peter James Bavaro, **The Accessible Quantum Past: Record Information, Coherence Bounds, and Echo Tests**, manuscript dated 7 September 2026. This is the title printed in the supplied 33-page file `Past_Selection_Filtration_version_9_0_2.pdf`. The associated [Zenodo record](https://doi.org/10.5281/zenodo.22647510) was previously catalogued under *The Accessible Quantum Past: Record Filtrations, Expected Lifts, and Visibility Bounds*. Keep the printed title, catalogue title and version labels distinct.

The supplied file has 670609 bytes, MD5 `06bfc9d1e4f7d7201404150e2e51da2d` (matching the previously retrieved record checksum), and SHA256 `50aaff14f11a81da5ee7557d3ff86e446d8075b69717daf220ad75ff814410f9`. The comparison uses that exact file, not an inferred later revision. The source PDF is not redistributed here.

Review date: 24 October 2026. Sections 4–6 and their proofs are the directly relevant material; the full text was also checked for a competing extremal law or pairwise-independent family. The equations and example on printed pages 13–14 were inspected in rendered page images. The other sections concern accessible algebras, three-alternative completion, calibrated echo models and further physical postulates. Their distinct results are not claimed as contributions of this project.

## Common ingredients and exact correspondence

| Source location | Relationship to this project |
|---|---|
| Lemma 4.1, p. 8, Eq. (12) | Uses the same balanced block-state observable, actual visibility equal to the absolute trace of the cross block, and proves the compatible root-fidelity envelope. This is inherited background, not a different visibility task. |
| Remark 4.3, p. 8 | Already distinguishes actual coherence from the envelope and notes invariance of actual coherence under a record-only channel. |
| Theorem 5.3 and Corollary 5.5, pp. 9–10 | Product fidelity factorization, sharp distinguishability threshold and symmetric commuting saturators include the independent endpoint used here. |
| Theorem 6.2, p. 13, Eqs. (25)–(26) | Gives a finite-size correction in terms of the Bures angles between each branch state and its own product of marginals. |
| Corollary 6.3, p. 13 | Explicitly converts that correction to **the same branchwise relative-entropy total correlation** used here. The distinction is not a different definition of the budget. |
| Remark 6.4, p. 14 | Supplies a two-fragment numerical example, reproduced below. It is not a growing-family sharpness construction. |

Our separate conditional decoder-error bounds imply local trace distance at least $\delta=1-2\varepsilon$: the decoder's outcome-zero effect has expectation at least $1-\varepsilon$ under branch zero and at most $\varepsilon$ under branch one. Thus every admissible state here satisfies the source's threshold hypothesis, with $R_\delta=N$. The source does not require our stronger separate-error condition. Its upper bounds therefore genuinely apply to our class; the difference in assumptions does not remove this overlap.

## Direct specialization to a fixed budget

Let $V$ denote root fidelity (not its square), put $r=2\sqrt{\varepsilon(1-\varepsilon)}$, and define

```math
g(T)=\arccos(e^{-T/2}),\qquad [z]_+=\max\lbrace z,0\rbrace.
```

Applying Theorem 6.2 and Corollary 6.3 with $T_0,T_1\le C$ gives the valid bound

```math
v\le V\le U_{\rm B}(N,\varepsilon,C)
:=\cos\!\left([\arccos(r^N)-2g(C)]_+\right).
```

This is our specialization of the source's inequalities. For every fixed $C>0$ and $0<\varepsilon<1/2$, direct evaluation gives

```math
\lim_{N\to\infty}U_{\rm B}(N,\varepsilon,C)=
\begin{cases}
2e^{-C/2}\sqrt{1-e^{-C}},&0<C<\ln2,\\
1,&C\ge\ln2.
\end{cases}
```

The elementary one-fragment cap $r$ can be imposed as well; the minimum still has a positive limit. At $C=0$, keep $U_{\rm B}=r^N$ rather than treating floating-point roundoff at $\cos(\pi/2)$ as residual visibility. The nonzero limit is a limitation of this **direct bound**, not a claim that nonzero asymptotic visibility is attainable.

In contrast, our [converse and matching construction](../science/sharp-bound.md) prove, for the declared class,

```math
\lim_{N\to\infty}\sqrt N\,v_{\max}(N,\varepsilon,C)
=2\sqrt{C/J_\varepsilon},\qquad
J_\varepsilon=(1-2\varepsilon)\ln\frac{1-\varepsilon}{\varepsilon}.
```

The improvement uses the distribution of rare-event probability under the relative-entropy budget. Replacing that budget by one global Bures angle loses the large-deviation information used by the three-region argument.

## A stronger reuse of the source: block refinement

It would be too strong to say that the source's inequalities cannot yield any vanishing bound. The following deduction combines them with the standard total-correlation decomposition. It is derived here, not stated as a theorem in Bavaro's manuscript, and is not claimed to be the best possible consequence of that framework.

Partition the records into $m=\lfloor N/k\rfloor$ disjoint blocks of size $k$, plus any remainder. For either branch, subadditivity across the block partition gives

```math
\sum_{j=1}^m T_x(E_{B_j})\le T_x(E)\le C.
```

Indeed, the difference is the total correlation between the blocks and remainder plus the internal total correlation of the remainder; both are nonnegative. Adding the two branch inequalities yields some block $B_j$ with

```math
T_0(E_{B_j})+T_1(E_{B_j})\le2C/m.
```

Fidelity data processing bounds the full-record envelope by this block's envelope. Also $g(T)\le\sqrt T$: for $z=g(T)$, $T=-2\ln\cos z\ge z^2$, since $\tan z\ge z$ on $[0,\pi/2)$. Applying Corollary 6.3 on the block therefore gives an angle correction at most $2\sqrt{C/m}$. Cosine is 1-Lipschitz, including the clipped case, so

```math
v\le\min\left\lbrace r,\quad r^k+2\sqrt{\frac{C}{\lfloor N/k\rfloor}}\right\rbrace,\qquad 1\le k\le N.
```

For fixed $r\in(0,1)$ choose $k=\lceil\ln N/(-2\ln r)\rceil$, which is at most $N$ eventually. Then $r^k\le N^{-1/2}$ and the second term is $O(\sqrt{C\ln N/N})$. This establishes a weaker vanishing guarantee from the prior inequalities with an additional block argument. It does not supply the sharp coefficient or the matching $N^{-1/2}$ extremal law. The comparison is therefore more precise than simply contrasting a constant bound with a vanishing one.

## State-specific angles remain useful

Theorem 6.2 can be substantially stronger than its total-correlation relaxation when the actual angles are known. Our comparison is about what follows **uniformly from the given budgets**, not a universal ordering of every state-specific finite bound.

For the main matching family at $\varepsilon=0.2$, $C=0.1$, $N=100000$, the actual branch total correlation is approximately $0.0999824097$ nats, while its Bures angle to its own product proxy is only $0.00113293636$. The actual-angle bound is approximately $0.00226587078$, close to the attained visibility $0.00219293372$. It is even tighter here than our implemented finite-size converse, approximately $0.00252486372$. By contrast, replacing the angles by the declared total-correlation budget gives approximately $0.58687874372$.

Thus the source's geometric bound is correct, complementary and sometimes numerically strong. Its stated total-correlation specialization does not itself provide the fixed-budget sharp asymptotic result. The additional information required to evaluate the actual angles must not be silently treated as supplied by $T_x\le C$.

## Reproduction and contribution boundary

The [comparison script](../verification/check_bavaro_comparison.py) reproduces Remark 6.4: joint affinity $0.4555946768$, product proxy $0.36$, Bures-angle bound $0.5202211031$, and total-correlation bound $0.5942530214$. It also checks the direct-limit formula, the block budget decomposition on finite classical laws, and the three bounds on the main matching family. [Stored output](../verification/bavaro_comparison_results.json) identifies both script hashes and the source PDF. Floating-point checks corroborate the displayed finite calculations; the asymptotic comparison rests on the arguments above.

The inspected manuscript does not state the sharp coefficient for fixed positive $C$, a construction attaining that coefficient under the same budget, or the growing exactly conditionally pairwise-independent family with arbitrarily small fixed positive total correlation and algebraic visibility. Those are the distinctions supported by this comparison. The generic visibility envelope, product law and existence of correlation-budget corrections must be credited to prior work.

This resolves the identified full-text comparison for the supplied version. It is not an exhaustive historical-priority certificate, a claim of independent expert review, or a claim that no further deduction from earlier information-theoretic tools is possible. The selected-record/purifier boundary and all other [physical qualifications](../science/scope.md) remain unchanged.
