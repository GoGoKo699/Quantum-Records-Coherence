# Reproducible finite checks

From the repository root, run:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_records.py
```

The script prints JSON and makes no network requests. To refresh the checked numerical record:

```bash
python verification/check_records.py > verification/results.json
```

The stored output was produced with Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. Its `source_sha256` identifies the script that generated it. Floating-point values may vary slightly across supported platforms.

## What the 149 check cases cover

The deterministic grid tests normalization, marginal errors, the finite entropy sandwich, the mixture affinity sandwich, the independent endpoint and the finite-size converse. Hypergeometric cases test exact-pairwise formulas to numerical tolerance and the explicit entropy certificate. An explicit purifying isometry is traced to its positive completion. A separate gate-level simulation checks the linear-gate star circuit. Forty random positive quantum states with generally noncommuting conditional states check the visibility-to-affinity and quantum-to-classical total-correlation inequalities. The fixed random seed is 2402026.

The count is parameter/state cases, not 149 independent proofs. Pairwise marginals are certified analytically by exchangeability and the binary covariance identity; the numerical covariance residual is a finite consistency check.

## Representative outputs

For $\varepsilon=0.2$ and $C=0.1$, the asymptotic coefficient is approximately $0.6934683460$. At $N=100000$, the matching distribution gives $\sqrt N\,v\approx0.6934665317$.

At $N=10000$, $\varepsilon=0.2$ and $\ell=6$, the pairwise-independent construction gives visibility approximately $0.0054428834$, total correlation approximately $0.0693432610$, and the explicit upper certificate $0.0772647888$ nats. Its local error is approximately $0.1999877774$. These are floating-point evaluations; the exact independence proof is in [the science](../science/pairwise-independence.md).

## What the checks do not establish

The script does not prove uniform or asymptotic statements, certify historical novelty, establish typical environmental dynamics, or verify GitHub's hosted mathematical rendering. The written proofs establish the stated mathematical claims. Computation uses ordinary floating-point arithmetic, not interval-certified bounds. Extremely small budgets or parameters at machine-precision distance from the endpoints can require higher precision than this reproduction script supplies.
