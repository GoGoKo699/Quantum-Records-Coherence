# Thirty milestones for quantum records and coherence

The single educational anchor is [Watrous (2018)](WATROUS_BRIDGE.md). Section numbers below refer to the author's pre-publication manuscript; the bridge explains notation and units. Local proof links are authoritative for the project's results, not claims that Watrous proves them.

**Allocation:** 14 background/preliminaries milestones build the operational and information-theoretic model. Then 16 narrative/innovation milestones connect local proof mechanisms to the complete extremal law, physical realizations and attribution. This allocation reflects the quantum-to-classical interface and the two different witnesses. Each phase proceeds from local objects to a global synthesis. The map is learner-independent and is not a catalogue of every technical lemma.

## Phase I — Background and preliminaries (M01–M14)

<a id="m01"></a>
### M01 — Alternatives and registers

**Question:** What distinguishes the pointer alternative from its records?
**Target:** Identify the system qubit, the selected fragments, and the classical branch label without treating the label as an extra coherent conditioning register.
**Dependencies:** None.
**Story role and connection:** Establish the local physical objects before combining them into a joint state.
**Sources:** Watrous §§2.1.1–2.1.2; [model](../science/model.md).

<a id="m02"></a>
### M02 — Joint states and partial traces

**Question:** What information remains when some registers are ignored?
**Target:** Distinguish a joint density operator, its system marginal, and branch-conditioned record marginals; explain why discarding access is not a coherent reversal.
**Dependencies:** M01.
**Story role and connection:** Connect local registers to the state of the composite experiment.
**Sources:** Watrous §2.1.3; [model](../science/model.md), [scope](../science/scope.md).

<a id="m03"></a>
### M03 — Actual fringe visibility

**Question:** Which part of the joint state determines the observed fringe?
**Target:** Explain the cross block and why its trace determines phase-scan contrast, rather than inferring contrast from the diagonal record states alone.
**Dependencies:** M02.
**Story role and connection:** Tie a matrix entry to the physical observable being bounded.
**Sources:** Watrous §§2.1.2, 2.3; [primer](README.md), [model](../science/model.md).

<a id="m04"></a>
### M04 — Two conditional decoding errors

**Question:** What does one locally readable fragment promise?
**Target:** Express the two POVM error constraints separately and identify the measurement and branch in each probability.
**Dependencies:** M01, M02.
**Story role and connection:** Translate the physical record into an operational statistical promise.
**Sources:** Watrous §§2.3.1–2.3.2; [model](../science/model.md).

<a id="m05"></a>
### M05 — Distinguishability is not the whole error promise

**Question:** How is decoder accuracy related to trace distance?
**Target:** Derive the implied local trace-distance threshold and distinguish it from the stronger separate-error assumption; an average success guarantee does not by itself establish both conditional bounds.
**Dependencies:** M04.
**Story role and connection:** Connect measurement evidence to a state-distance comparison while preserving assumptions.
**Sources:** Watrous §3.1.1; [Bavaro correspondence](../references/bavaro-comparison.md).

<a id="m06"></a>
### M06 — Fidelity and classical affinity

**Question:** Which notion of overlap enters the visibility envelope?
**Target:** Recognize unsquared fidelity and its diagonal-state affinity formula, and distinguish either from squared fidelity and from actual visibility.
**Dependencies:** M02, M03.
**Story role and connection:** Introduce the common overlap quantity across quantum and classical descriptions.
**Sources:** Watrous §3.2.1, Definition 3.11; [bridge](WATROUS_BRIDGE.md), [model](../science/model.md).

<a id="m07"></a>
### M07 — Channels and direction of data processing

**Question:** What can decoding or discarding information do to distinguishability?
**Target:** Explain why a common channel can increase fidelity while it cannot increase relative entropy; do not reverse the direction when deriving an upper bound.
**Dependencies:** M04, M06.
**Story role and connection:** Prepare the quantum-to-classical comparison through a physical measurement channel.
**Sources:** Watrous §§2.2.1–2.2.2, Theorems 3.27 and 5.35; [model](../science/model.md).

<a id="m08"></a>
### M08 — Purification and the selected subsystem

**Question:** Can mixed record states arise from a unitary preparation?
**Target:** Identify an auxiliary purifier and explain why tracing it gives mixed records without making it part of the selected-fragment correlation budget.
**Dependencies:** M02, M07.
**Story role and connection:** Connect abstract density operators to a realization and its resource boundary.
**Sources:** Watrous §2.1.3; [positive completion](../science/model.md), [scope](../science/scope.md).

<a id="m09"></a>
### M09 — Independence after conditioning

**Question:** Why can records of the same bit be correlated even with zero conditional correlation?
**Target:** Separate independence within each branch from dependence in their unconditional mixture, and pairwise independence from full factorization.
**Dependencies:** M01, M04.
**Story role and connection:** Identify exactly which correlations the theorem constrains.
**Sources:** Watrous §§1.2.2, 5.1; [two-record example](README.md), [model](../science/model.md).

<a id="m10"></a>
### M10 — Entropy and its units

**Question:** What does an entropy budget count?
**Target:** Interpret classical and quantum entropy, use the binary entropy function, and consistently convert bits to nats.
**Dependencies:** M02, M09.
**Story role and connection:** Supply the scale needed to compare record dependence quantitatively.
**Sources:** Watrous §§5.1.1, 5.2.1; [unit conversion](WATROUS_BRIDGE.md).

<a id="m11"></a>
### M11 — Relative entropy and rare support

**Question:** What is the cost of assigning mass where a reference law assigns little or none?
**Target:** Understand the direction and support condition of relative entropy and why a finite budget prohibits positive mass on a zero-probability reference event.
**Dependencies:** M10.
**Story role and connection:** Connect information cost to the rare events used by the converse.
**Sources:** Watrous §§5.1.1–5.1.2; [event lemma](../science/sharp-bound.md).

<a id="m12"></a>
### M12 — Total correlation

**Question:** How is global conditional dependence measured?
**Target:** Relate divergence from the product of a state's own marginals to the entropy difference; distinguish a bound on each branch from an averaged budget or a bound on pairs.
**Dependencies:** M09, M10, M11.
**Story role and connection:** Assemble the scalar constraint controlling all the selected records.
**Sources:** Watrous §§5.2.1–5.2.3; [model](../science/model.md).

<a id="m13"></a>
### M13 — Event reduction and product tails

**Question:** Why is an indicator or a sum of decoded bits useful?
**Target:** Explain coarse-graining to an event and how product structure bounds the exponential moment of a sum; separate this property of a reference law from independence of the actual law.
**Dependencies:** M07, M11, M12.
**Story role and connection:** Prepare a tractable global statistic without assuming away correlations.
**Sources:** Watrous §1.2.2, Theorem 5.13; [local tail derivation](../science/sharp-bound.md).

<a id="m14"></a>
### M14 — The complete operational contract

**Question:** Over which experiments is the maximum visibility taken?
**Target:** Combine equal priors, separate conditional errors, selected-fragment branch budgets, finite dimensions, and actual unconditioned visibility into one model. Identify additional purifiers and excluded recovery operations.
**Dependencies:** M03, M05, M08, M12, M13.
**Story role and connection:** Conclude the background phase with the entire problem rather than one more isolated definition.
**Sources:** Watrous Chapters 2, 3 and 5 via the [bridge](WATROUS_BRIDGE.md); [model](../science/model.md), [scope](../science/scope.md).

## Phase II — Narrative and innovation (M15–M30)

<a id="m15"></a>
### M15 — Decoding preserves the required upper-bound direction

**Question:** Why does a classical inequality constrain arbitrary quantum records?
**Target:** Follow the product measurement, relative-entropy contraction and outcome-wise positive-block inequality to obtain the affinity upper bound without assuming commuting input states.
**Dependencies:** M06, M07, M12, M14.
**Story role and connection:** Start the result from the local quantum-to-classical interface.
**Sources:** Watrous Theorems 3.27 and 5.35; [reduction](../science/model.md).

<a id="m16"></a>
### M16 — A positive completion attains classical affinity

**Question:** Is the classical relaxation only an upper bound?
**Target:** Verify the normalized positive completion and its purifying isometry, identifying why every admissible classical pair has a compatible quantum state with the same budget and attained affinity.
**Dependencies:** M08, M15.
**Story role and connection:** Match the classical optimization to the declared quantum experiment.
**Sources:** Watrous §§2.1.3, 3.2.2; [completion](../science/model.md).

<a id="m17"></a>
### M17 — The independent endpoint

**Question:** What happens when the correlation budget is exactly zero?
**Target:** Connect zero divergence, factorization, one-bit overlap and a product saturator to the exact exponential envelope; recognize this endpoint as inherited structure.
**Dependencies:** M06, M11, M12, M16.
**Story role and connection:** Establish the benchmark against which robustness is assessed.
**Sources:** Watrous §3.2.1; [independent endpoint](../science/sharp-bound.md), [attribution](../references/related-work.md).

<a id="m18"></a>
### M18 — The sharp event-budget inversion

**Question:** How much rare-event probability can a fixed relative-entropy budget buy?
**Target:** Explain the binary reduction and the refinement from a constant-loss bound to $u(C,s)=(C+o(1))/s$ at fixed positive budget.
**Dependencies:** M11, M13, M15.
**Story role and connection:** Isolate the local estimate that preserves the final leading coefficient.
**Sources:** Watrous Theorem 5.13; [rare-event lemma](../science/sharp-bound.md).

<a id="m19"></a>
### M19 — Correct and wrong-branch tail exponents

**Question:** Why are two different binary divergences needed?
**Target:** Derive the product-reference tail estimates and distinguish the near-branch exponent from the wrong-branch exponent tending to $J_\varepsilon$; account for heterogeneous marginals.
**Dependencies:** M13, M18.
**Story role and connection:** Turn local accuracy into a geometric separation of whole record strings.
**Sources:** Watrous §1.2.2; [Chernoff calculation](../science/sharp-bound.md).

<a id="m20"></a>
### M20 — The three-region affinity bound

**Question:** Why not use one global distance from a product state?
**Target:** Partition strings into two branch-typical regions and a middle region, and apply Cauchy–Schwarz with the correct branch probabilities on each part.
**Dependencies:** M18, M19.
**Story role and connection:** Assemble the local tail controls into a finite-size converse.
**Sources:** Watrous §1.1 for inner-product inequalities; [three-region proof](../science/sharp-bound.md).

<a id="m21"></a>
### M21 — Uniform converse and its asymptotic domain

**Question:** How does the finite inequality produce the exact leading upper coefficient?
**Target:** Choose a shrinking threshold gap, show the middle term is lower order, and justify taking the supremum. Keep $C$ and $\varepsilon$ fixed and distinguish the limit from a finite-size equality.
**Dependencies:** M17, M20.
**Story role and connection:** Complete the upper half of the extremal law for the full admissible class.
**Sources:** Watrous §1.2.1 as analytical background; [asymptotic converse](../science/sharp-bound.md).

<a id="m22"></a>
### M22 — Calibrating a rare common flip

**Question:** How can common errors be added without worsening local accuracy?
**Target:** Explain the mixture of complemented product laws and the adjustment $a=(\varepsilon-t)/(1-2t)$ that keeps both local error probabilities equal to $\varepsilon$.
**Dependencies:** M09, M14, M17.
**Story role and connection:** Begin the lower witness with a single controllable mechanism.
**Sources:** Watrous §§1.2.2, 5.1; [matching family](../science/constructions.md).

<a id="m23"></a>
### M23 — Paying for the common flip

**Question:** Does the attaining family really meet the same budget?
**Target:** Use mixture-entropy bounds to obtain the finite entropy sandwich, then explain why its calibrated flip probability scales as $C/(NJ_\varepsilon)$.
**Dependencies:** M10, M12, M22.
**Story role and connection:** Charge the proposed mechanism before attributing an advantage to it.
**Sources:** Watrous §§5.1–5.2; [entropy calculation](../science/constructions.md).

<a id="m24"></a>
### M24 — Matching the upper coefficient

**Question:** Why does a rare event of weight $1/N$ give visibility of order $1/\sqrt N$?
**Target:** Read the affinity sandwich, identify the exponentially small remainder, and combine it with the calibrated entropy cost and converse under identical assumptions.
**Dependencies:** M16, M21, M23.
**Story role and connection:** Join the two proof directions into the sharp extremal law.
**Sources:** Watrous §3.2 for overlap background; [matching proof](../science/constructions.md), [converse](../science/sharp-bound.md).

<a id="m25"></a>
### M25 — Coherent control and circuit resources

**Question:** What quantum preparation realizes the algebraic witness?
**Target:** Trace the star circuit, explain why a coherent flag differs from a classical random flag, and count selected records, extra registers, rotations and CNOTs without assuming spatial locality.
**Dependencies:** M03, M08, M22, M24.
**Story role and connection:** Translate the statistical witness into actual unconditioned visibility.
**Sources:** Watrous §§2.1.3, 2.2; [star circuit](../science/constructions.md), [scope](../science/scope.md).

<a id="m26"></a>
### M26 — Exact cancellation of pair correlations

**Question:** Can every conditional pair be independent while the records remain globally dependent?
**Target:** Combine negative covariance from sampling without replacement with positive common-flip covariance; explain why zero covariance establishes independence for binary pairs, not arbitrary variables.
**Dependencies:** M09, M22, M23.
**Story role and connection:** Construct the second witness without confusing pairwise and joint constraints.
**Sources:** Watrous §1.2.2; [hypergeometric construction](../science/pairwise-independence.md).

<a id="m27"></a>
### M27 — A global budget for the pairwise witness

**Question:** Can the exact pairwise property coexist with any fixed positive correlation budget?
**Target:** Follow the chain-rule certificate and the choice of population ratio; combine the eventual budget and readability guarantees with algebraic visibility. Do not claim the best pairwise-restricted coefficient.
**Dependencies:** M11, M12, M24, M26.
**Story role and connection:** Upgrade pair cancellation to a complete admissible asymptotic family.
**Sources:** Watrous §5.1; [certificate and limit](../science/pairwise-independence.md).

<a id="m28"></a>
### M28 — Distinguishing the contribution from antecedents

**Question:** Which parts are inherited, and what changes quantitatively?
**Target:** Separate the standard visibility envelope and product law, the same-budget Bures-angle bound, its blockwise reuse, and the sharp law here. Explain the logarithmic loss of the two-point common-error benchmark without confusing history observables with qubit visibility.
**Dependencies:** M17, M21, M24, M27.
**Story role and connection:** Place both witnesses in their actual scientific context.
**Sources:** Watrous §3.2; [related work](../references/related-work.md), [Bavaro comparison](../references/bavaro-comparison.md).

<a id="m29"></a>
### M29 — What verification establishes

**Question:** How should an exact proof and a finite calculation support one another?
**Target:** Map each numerical check to its formula, distinguish construction feasibility from universal optimality, and separate asymptotic convergence, floating-point residuals and historical-priority evidence.
**Dependencies:** M24, M25, M27, M28.
**Story role and connection:** Connect the complete mathematical story to inspectable evidence.
**Sources:** Watrous Chapters 3 and 5 for the tested identities; [verification](../verification/README.md), [claim map](../science/README.md).

<a id="m30"></a>
### M30 — The complete physical statement

**Question:** What has the project established about redundant records and surviving interference?
**Target:** Explain the exponential independent endpoint, sharp algebraic fixed-positive-budget envelope, two realizations, and pairwise counterexample together. Preserve the selected-record/purifier boundary, fixed-parameter limit, absence of postselection, and distinction between a worst-case envelope and typical environmental dynamics.
**Dependencies:** M14, M24, M25, M27, M28, M29.
**Story role and connection:** Conclude with the contribution, resources, meaning and limitations as one coherent account.
**Sources:** Watrous foundations through the [bridge](WATROUS_BRIDGE.md); [scientific synthesis](../science/scope.md), [principal result](../README.md).

Return to the [learning route](README.md) or the [specialist route](../science/README.md).
