# Learning route: how many records suppress interference?

A qubit can leave the same binary information in many environmental fragments. One observer reads one fragment, another reads a different fragment, and both usually infer the same pointer alternative. The question is not simply whether the fragments carry information. It is how much interference can remain when their errors are allowed to be dependent.

Use [Watrous (2018)](WATROUS_BRIDGE.md) as the one educational anchor. Follow the [30 project-defined milestones](MILESTONES.md): M01–M14 build the background and model; M15–M30 assemble the proof, witnesses and physical conclusion. The map applies to any reader. Its dependencies describe the science, not an individual's study history.

## One record, one measurement, one contrast

A density matrix records the probabilities and coherences of a quantum state. A reduced density matrix describes a subsystem when the other registers are not measured. In the balanced pointer basis, write the system and selected records as

$$
\rho_{SE}=\frac12\begin{pmatrix}\rho_E^0&A\\A^\dagger&\rho_E^1\end{pmatrix}.
$$

The diagonal blocks are the record states conditioned on the two pointer alternatives. The cross block $A$ carries coherence between them. Tracing the records and scanning the system's relative phase produces

$$
p_+(\theta)=\frac{1+\operatorname{Re}(e^{i\theta}\operatorname{Tr}A)}2,
\qquad v=|\operatorname{Tr}A|.
$$

The contrast $v$ belongs to this joint state. The record states alone constrain it from above but generally do not determine it. [The operational model](../science/model.md) contains the exact assumptions and proof.

A local decoder is a two-outcome quantum measurement on one fragment. Its chance of reporting one when the alternative is zero must be at most $\varepsilon$, and its chance of reporting zero when the alternative is one must separately be at most $\varepsilon$. This is more than a statement about their average.

## A complete two-record example

Take $\varepsilon=1/5$. In outcome order $00,01,10,11$, independent conditional records have

$$
P_0=(16,4,4,1)/25,\qquad P_1=(1,4,4,16)/25.
$$

Each fragment has error $1/5$ under each alternative. Their classical affinity is the sum of the four square-root products,

$$
B(P_0,P_1)=16/25=0.64.
$$

For each string $y$, let $|\chi_y\rangle=\sqrt{P_0(y)}|0\rangle+\sqrt{P_1(y)}|1\rangle$. The positive joint state

$$
\rho_{SE}=\frac12\sum_y|\chi_y\rangle\langle\chi_y|\otimes|y\rangle\langle y|
$$

has exactly these conditional records and visibility $0.64$. Dephasing only the system removes its cross block and makes visibility zero, while leaving both record distributions unchanged. Thus the same records allow different actual contrasts. This construction, rather than an inference from record probabilities alone, supplies attainability.

Conditioned on either alternative the records are independent. Without conditioning, their equally weighted mixture is $(17,8,8,17)/50$, which is not a product of its uniform one-bit marginals. Shared information about the pointer must not be mistaken for conditional dependence among the records. [The example check](../verification/check_learning_example.py) verifies these identities and both quantum completions.

## What the correlation budget measures

For each conditional state separately,

$$
T_x=D\!\left(\rho_E^x\,\middle\|\,\bigotimes_i\rho_{E_i}^x\right)
=\sum_iS(\rho_{E_i}^x)-S(\rho_E^x)\le C.
$$

Here $S$ is entropy in nats and $D$ is relative entropy. The reference state uses the same branch's marginals, not an independent model chosen after seeing the answer. Zero total correlation forces a product state. Small positive total correlation is not the same as pairwise independence, and pairwise independence does not imply zero total correlation.

Only the selected fragments are in this budget. The attaining quantum preparations may use an additional control or purifier outside those fragments. The [scope statement](../science/scope.md) explains why including those registers changes the problem.

## How the two sides of the result meet

The upper-bound proof first decodes quantum records into bits without increasing their total correlation. A product law predicts exponentially rare patterns that resemble the opposite branch. Relative entropy limits how much probability the actual law can move into those patterns. Splitting the outcome space into the two branch-typical regions and a middle region gives a sharp bound on affinity.

The attaining family inserts a rare coherent common flip into independently noisy records. A probability of order $1/N$ costs only a fixed total correlation, but contributes to visibility through its square root. The [converse](../science/sharp-bound.md) and [construction](../science/constructions.md) agree on

$$
\lim_{N\to\infty}\sqrt N\,v_{\max}=2\sqrt{C/J_\varepsilon},
\qquad J_\varepsilon=(1-2\varepsilon)\ln\frac{1-\varepsilon}{\varepsilon},
$$

for fixed $C>0$ and fixed $0<\varepsilon<1/2$. At exactly $C=0$, the envelope is instead $[2\sqrt{\varepsilon(1-\varepsilon)}]^N$. These are different limiting regimes, not a finite discontinuity assertion. The algebraic envelope still tends to zero.

The [pairwise-independent family](../science/pairwise-independence.md) is a separate witness: negative sampling correlations cancel the common-flip pair correlations. Its order is sharp, but an optimal coefficient under the extra pairwise restriction is not claimed.

## Where to go next

The [milestone map](MILESTONES.md) gives the conceptual route; the [Watrous bridge](WATROUS_BRIDGE.md) identifies the source sections and notation changes. A specialist can go directly to the [claim-to-proof map](../science/README.md). The [prior-work comparison](../references/bavaro-comparison.md) explains why the contribution is the sharp law and witnesses, not the generic visibility envelope or the existence of correlation corrections.
