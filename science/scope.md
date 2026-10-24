# Physical meaning and scope

## What is established

Under the precise [selected-record model](model.md), the independent endpoint, the fixed-positive-budget asymptotic coefficient, a finite-size upper bound, an attaining star circuit, and an exactly pairwise-independent algebraic family have complete arguments in this repository. Their finite checks are reproducible. This is mathematical analysis with internal checks, not independent peer certification or an experiment.

The message is a robustness boundary: bounded total correlation does not preserve the exponential worst-case suppression obtained from exact conditional independence. The visibility still vanishes as the number of records grows. A positive budget does not allow a fixed nonzero visibility asymptotically under the stated local readability condition.

## Selected records are not necessarily the whole environment

The correlation budget covers $E_1,\ldots,E_N$. The mixed conditional record states are physically realized by an additional unobserved environment. In the general positive completion this includes an $N$-qubit purifier. The explicit star circuit uses a control plus $N$ purifier qubits, or a control plus initially mixed noise records.

Including those purifiers in the constrained fragment partition changes the total correlation. We have **not** proved the same sharp coefficient when the conditional state on an exhaustive $N$-fragment environment must be pure. Neither a measured classical correlation budget nor a selected-fragment quantum budget may be silently relabeled as that stronger constraint.

## Actual coherence versus compatible coherence

Every allowed state obeys the upper bound. The constructions exhibit allowed states attaining it asymptotically. The same conditional record states are also compatible with zero system coherence: dephasing $S$ leaves the records unchanged. Record statistics therefore certify an upper envelope, not a lower guarantee of surviving interference.

There is no environment-assisted eraser or postselection in the reported visibility. Such operations define a different task.

## Assumptions that must remain visible

The local decoder error is bounded separately under both pointer alternatives, with equal prior populations. The total-correlation bound is imposed separately on each conditional state. The asymptotic theorem holds for fixed $0<\varepsilon<1/2$ and fixed $C>0$; it does not supply a uniform crossover theorem as $C$ or $\varepsilon$ varies with $N$. For finite $N$, use the explicit upper bound and the stated construction domains.

At $\varepsilon=0$, a single perfectly readable record forces zero visibility. At $\varepsilon=1/2$, identical records impose no information requirement and visibility one is possible. These endpoints are not obtained by substituting into a singular fixed-interior asymptotic expression.

The star circuit is an existence result with declared couplings and rotation angles. It does not show that generic local environmental dynamics produces the extremal states, or that the required couplings have constant spatial range. The pairwise construction additionally requires correlated initial noise or its explicit purification. There is no claim of sharp optimality within a fixed-Hamiltonian, pure-exhaustive-environment, finite-depth or spatially local subclass.

## Attribution boundary

Independent-product multiplication, relative-entropy data processing, binary Chernoff bounds, entropy identities, and the distinction between pairwise and joint independence are inherited ingredients. The exact extremal coefficient and simultaneous pairwise-independent construction are derived here, but their priority requires the [closest-work comparison](../references/related-work.md). Two material recent full texts could not be retrieved in this pass, so that comparison is not represented as complete.
