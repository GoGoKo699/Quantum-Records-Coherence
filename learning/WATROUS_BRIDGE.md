# Watrous to quantum records and coherence

**Single educational anchor:** John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018). Use the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) and its freely accessible pre-publication manuscript. The section and theorem numbers below were checked against that manuscript on 24 October 2026. It is a reading source, not a file redistributed by this repository.

This bridge supplies a selective route into the [30 milestones](MILESTONES.md), not an assignment to read the whole book. [The project primer](README.md) introduces the physical question. The complete arguments remain in [science/](../science/README.md). Other research citations provide attribution, not additional educational anchors.

## Targeted source route

| Source location | Use in this project | Project destination |
|---|---|---|
| Sections 1.1.2–1.1.3 and 1.2.2, as needed | Tensor products, positive operators, trace norms, probability | [Operational model](../science/model.md) |
| Sections 2.1.2–2.1.3 | States, reduced states and purification | [Selected records and positive completion](../science/model.md) |
| Sections 2.2.1–2.2.2 and 2.3.1–2.3.2 | Channels, isometries and measurements | [Decoder reduction](../science/model.md) |
| Section 3.1.1 | Binary state discrimination | [Two separate conditional errors](../science/model.md) |
| Sections 3.2.1–3.2.3 | Fidelity, positive-block characterization and monotonicity | [Visibility envelope](../science/model.md) |
| Sections 5.1.1–5.1.2 | Classical entropy and relative entropy | [Event budget](../science/sharp-bound.md) |
| Sections 5.2.1–5.2.3 | Quantum entropy, subadditivity and data processing | [Correlation budget](../science/model.md) |

Particularly direct pointers are Definition 3.11 (fidelity), Theorem 3.17 (positive-block characterization), Theorem 3.27 (fidelity monotonicity), Theorem 5.13 (classical relative-entropy monotonicity), and Theorem 5.35 (quantum relative-entropy monotonicity). The book's generic positive-block result is an antecedent of the visibility envelope, not a new theorem of this project.

## Convention translation

Watrous writes vectors and adjoints as $u$ and $u^*$; here the corresponding notation is $|u\rangle$ and $\langle u|$. His $uu^*$ is our $|u\rangle\langle u|$. A classical probability vector is represented by a diagonal density matrix when embedded in the quantum model.

Watrous's $F(\rho,\sigma)$ is **unsquared fidelity**:

$$
F_{\mathrm W}(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1.
$$

This is the quantity denoted $V$ in the source comparison. On diagonal states it equals our classical affinity $B(P,Q)=\sum_y\sqrt{P(y)Q(y)}$. It is not automatically the actual visibility $v=|\operatorname{Tr}A|$ of a given joint state. The compatible positive completion can attain it; dephasing the system can instead make visibility zero without changing the conditional record states.

The book's default logarithm has base two, and its entropies are in bits. Here every entropy and relative-entropy budget is in **nats**:

$$
S_{\mathrm{nats}}=(\ln2)H_{\mathrm W},\qquad
D_{\mathrm{nats}}=(\ln2)D_{\mathrm W},\qquad
C_{\mathrm{nats}}=(\ln2)C_{\mathrm{bits}}.
$$

The source's entropy symbol $H$ becomes $S$ for quantum entropy here; classical entropy remains $H$ or $h$. Changing units in both numerator and denominator leaves $C/J_\varepsilon$ invariant. Changing only $C$ would change the sharp coefficient incorrectly. Trace distance in the comparisons is half the trace norm; relative entropy is a different quantity despite uses of the letter $D$ in different sources.

## The additional steps supplied by this repository

**A visibility task, not just a distance between states.** Start from the balanced system–record block state and a phase measurement on the system. [The model](../science/model.md) explains why its cross-block trace is the measured contrast, and proves the local-decoder reduction. It keeps both conditional error bounds, rather than substituting an average-error condition.

**A budget on the actual conditional record state.** For each branch, form the product of that branch's own marginals. Its relative entropy from the joint state is total correlation. Theorem 5.35 allows local decoding to reduce, not increase, this budget. Correlation of the unconditional mixture is not the quantity being bounded.

**A rare-event calculation.** [The converse](../science/sharp-bound.md) supplies the binary event reduction, the product-tail estimate and the three-region partition. The refinement $u(C,s)=(C+o(1))/s$ retains the leading coefficient that a fixed additive entropy constant would lose. These are project derivations, not results attributed to a textbook section.

**A witness under the same budget.** [The matching construction](../science/constructions.md) calibrates a rare common flip, evaluates its entropy and affinity, and gives a coherent-control circuit. [The pairwise construction](../science/pairwise-independence.md) adds sampling without replacement to cancel every conditional pair covariance while controlling global correlation. The hypergeometric certificate is supplied locally; it is not assigned as an additional textbook prerequisite.

**The complete physical conclusion.** [Scope](../science/scope.md) joins the two directions and identifies what changes if all purifiers are included in the constrained environment. [Related work](../references/related-work.md) separates inherited machinery from the sharp law and constructions. [Verification](../verification/README.md) distinguishes numerical consistency from proof and priority.

Return to the [learning route](README.md) or the [milestone map](MILESTONES.md).
