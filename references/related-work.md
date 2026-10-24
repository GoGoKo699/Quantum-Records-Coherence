# Related work, attribution and review limits

Scientific review date: 24 October 2026. Distinguish inspected primary statements, calculations supplied here, and limits of the comparison. An independently reconstructed proof does not establish historical priority. Structured source metadata is in [the bibliography](references.bib).

## Foundations and imported ingredients

**W. H. Zurek, “Quantum Darwinism,” Nature Physics 5, 181–188 (2009).** [Publisher](https://doi.org/10.1038/nphys1202); [arXiv:0903.5082](https://arxiv.org/abs/0903.5082). This is the foundational setting of redundant environmental records. The present project asks a worst-case quantitative robustness question; it does not claim to introduce redundancy or objectivity.

**M. Zwolak, C. J. Riedel and W. H. Zurek, “Amplification, Decoherence and the Acquisition of Information by Spin Environments,” Scientific Reports 6, 25277 (2016).** [Article](https://doi.org/10.1038/srep25277). The inspected abstract relates amplification in spin environments to quantum Chernoff information. We do not claim novelty for exponential amplification/distinguishability under independent record structure.

**J. Watrous, The Theory of Quantum Information (Cambridge University Press, 2018).** [Author's book page](https://cs.uwaterloo.ca/~watrous/TQI/). Chapters 2, 3 and 5 supply the background for states, measurements, distance/fidelity and entropy/data processing. This is the single selected educational anchor; the [source-to-project bridge](../learning/WATROUS_BRIDGE.md) identifies the relevant sections, conventions and locally supplied derivations. No source files from the book are redistributed.

The proof pages explicitly derive the binary event bound, product Chernoff estimate and hypergeometric correlation certificate, so those steps can be checked without treating this bibliography as a substitute proof.

## Pairwise versus global independence: established prior work

**A. Feller, B. Roussel, I. Frerot and P. Degiovanni, “Comment on ‘Strong Quantum Darwinism and Strong Independence are Equivalent to Spectrum Broadcast Structure’” (2021), arXiv:2101.09186v1.** [Primary PDF](https://arxiv.org/pdf/2101.09186); [abstract](https://arxiv.org/abs/2101.09186).

The two-page text was inspected. Its explicit classical counterexample has a qubit system and three qutrit fragments. Conditional pairwise independence does not imply full factorization; the corrected formulation uses multipartite conditional independence. Consequently the generic pairwise-independence warning is not new here. Our distinct investigated statement is the simultaneous growing-$N$ construction with imperfect local readability, any prescribed positive fixed total-correlation budget, and attainable $N^{-1/2}$ visibility. The source's PDF screenshot request failed; the mathematical comparison above uses its parsed equations and text, not a claimed visual inspection.

## Strasberg: statement-level comparison

**P. Strasberg, “Redundant Records of the Past: Unifying Quantum Darwinism and Decoherent Histories,” arXiv:2610.09845v1 (7 October 2026).** [Primary text](https://arxiv.org/abs/2610.09845v1). Sections III.1.2, IV.1 and Appendix A were inspected in indexed primary full text; no figure inspection is claimed.

| Source location | Relationship to this project |
|---|---|
| Equations (14)–(15) | Independent-record affinity multiplication is inherited. |
| Equations (31)–(34) | Affinity controls a history probability-sum defect, not the present qubit visibility. |
| Theorem IV.1 and Appendix A | A supplied decay function $g(n)$ yields an information deficit of order $g(n)\lvert\ln g(n)\rvert$. |
| Equations (35)–(37) | A perfectly correlated example motivates the budget calculation below. |

Those statements do not derive the fixed-total-correlation coefficient established here. The specific comparison is resolved, not global priority.

### Our correlation-budget calculation for the common-error family

This is a calculation in the [present model](../science/model.md), not a theorem attributed to the source. Let $N\ge2$ and $0<\lambda\le\varepsilon<1/2$. Consider

$$
P_0=(1-\lambda)\delta_{0^N}+\lambda\delta_{1^N},\qquad
P_1=\lambda\delta_{0^N}+(1-\lambda)\delta_{1^N}.
$$

Each local conditional decoding error is $\lambda$. The joint entropy is $h(\lambda)$ and each marginal entropy is $h(\lambda)$, where $h$ is binary entropy in nats. Thus the classical total correlation, and the quantum total correlation of the diagonal completion, equal

$$
T_x=(N-1)h(\lambda).
$$

The two shared outcomes give

$$
B(P_0,P_1)=2\sqrt{\lambda(1-\lambda)}.
$$

The model's positive completion attains this affinity as actual visibility. This completion is a different state construction from a history-based example: equality of record statistics does not identify their physical observables. Also, a *pure* GHZ-type conditional state with these weights has entropy zero and one-fragment entropy $h(\lambda)$, hence total correlation $Nh(\lambda)$. Measured, diagonal and pure-state budgets must not be interchanged.

At fixed nonzero $\lambda$, the correlation cost is extensive, so such a sequence is outside the fixed-$C$ model. Within the diagonal family, visibility increases with $\lambda$ below $1/2$. For fixed $C>0$ and sufficiently large $N$, its maximum therefore occurs at the unique solution

$$
(N-1)h(\lambda_N)=C.
$$

Using $h(z)=z\ln(1/z)+z+O(z^2)$ as $z\downarrow0$ gives

$$
\lambda_N=\frac{C}{N\ln N}[1+o(1)],\qquad
v_{\mathrm{common}}=2\sqrt{\frac{C}{N\ln N}}[1+o(1)].
$$

For a direct asymptotic justification, evaluate $(N-1)h(z)$ at $z=(1\pm\delta)C/(N\ln N)$ for fixed $0<\delta<1$. The two values tend to $(1\pm\delta)C$; monotonicity brackets the root, and then $\delta\downarrow0$ proves the limit. The readability bound holds eventually because $\lambda_N\to0$.

Relative to the [sharp fixed-budget scale](../science/sharp-bound.md), with $J_\varepsilon=(1-2\varepsilon)\ln[(1-\varepsilon)/\varepsilon]$,

$$
\frac{v_{\mathrm{common}}}{2\sqrt{C/(NJ_\varepsilon)}}
=\sqrt{\frac{J_\varepsilon}{\ln N}}[1+o(1)]\longrightarrow0.
$$

Thus this two-point family does not provide the sharp matching witness. The [independently noisy common-flip construction](../science/constructions.md) has a genuinely different correlation cost. Moreover, the two-point family's conditional pair covariance is $\lambda(1-\lambda)>0$, so it is not the [exactly pairwise-independent construction](../science/pairwise-independence.md). These are comparisons of the declared families, not a claim that all other correlated mechanisms have been classified.

The [companion check](../verification/check_common_error.py) tests these finite entropy and affinity identities and the budget inversion. Its [stored output](../verification/common_error_results.json) supports the formulas, not historical priority or their asymptotic proof.

## Bavaro: full-text comparison

**P. J. Bavaro, “The Accessible Quantum Past: Record Information, Coherence Bounds, and Echo Tests,” manuscript dated 7 September 2026.** [Associated Zenodo record](https://doi.org/10.5281/zenodo.22647510). This is the title printed in the supplied 33-page `Past_Selection_Filtration_version_9_0_2.pdf`, whose MD5 `06bfc9d1e4f7d7201404150e2e51da2d` matches the previously retrieved record checksum. The catalogue's earlier title (“Record Filtrations, Expected Lifts, and Visibility Bounds”), record label v5 and manuscript v9.0 label are not silently substituted for the printed title. The [dedicated comparison](bavaro-comparison.md) records the exact file provenance and inspected scope.

Lemma 4.1 supplies the same actual-visibility/fidelity-envelope distinction. Theorem 5.3 and Corollary 5.5 include the product endpoint. Most importantly, **Corollary 6.3 already uses the same branch total correlation** as this project, by relaxing Theorem 6.2's Bures-angle correction. Generic correlation-budget visibility bounds are therefore prior work.

The direct fixed-budget specialization has a nonzero large-$N$ upper-bound limit. A stronger blockwise reuse, derived in the comparison, yields $O(\sqrt{\ln N/N})$ for fixed positive budget; no claim is made that earlier tools cannot imply decay. The source's state-specific angle bound can also be tight when additional angle information is available. The distinction supported here is the sharp fixed-budget $N^{-1/2}$ law and coefficient with matching attainability, and the simultaneous pairwise-independent bounded-correlation family. These are not stated in the inspected manuscript.

The [comparison script](../verification/check_bavaro_comparison.py) reproduces the source's Remark 6.4, checks the budget specialization and block deduction, and contrasts actual-angle and budget-only bounds. The full-text access gap for this identified source is resolved. This statement-level comparison is not an exhaustive historical-priority certificate or independent expert validation.
