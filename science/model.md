# Operational model and proposed frontier

Consider a binary classical label X with equally likely values and conditional environment states P_0 and P_1 on N record registers. In a classical diagonal realization, each register admits a decision rule with error at most ε, 0 < ε < 1/2, for each conditional label. Define total conditional correlation by D(P_x || ⊗_i P_{x,i}) ≤ C (for both x). The quantum version must specify the measurement channels and whether the budget applies to the original quantum record state or to the measured classical distribution.

For pure conditional environment vectors |E_0⟩ and |E_1⟩, system interference is proportional to |⟨E_0|E_1⟩|. A diagonal classical construction can be purified with overlap equal to the Bhattacharyya affinity B(P_0,P_1)=Σ_z √(P_0(z)P_1(z)). General mixed states require an explicit operational definition of recoverable visibility and a proof that the classical bound lifts.

**Candidate asymptotic formula (not yet certified):** for fixed ε and C>0, B_max ∼ 2√C / √[N(1−2ε) log((1−ε)/ε)]. At C=0 the independent-record benchmark is [2√(ε(1−ε))]^N. The limiting statements must clarify whether C is a bound for each conditional state or an average, and whether record errors are symmetric or only bounded.

The headline is currently a research conjecture pending full upper-bound proof, construction, endpoint checks and literature review. It is not a theorem merely because finite numerical examples fit it.
