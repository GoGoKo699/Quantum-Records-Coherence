"""Check the perfectly correlated benchmark in references/related-work.md.

Standard library only. Finite checks do not establish asymptotics or priority.
Run: python verification/check_common_error.py
"""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path
import sys


def entropy(p: float) -> float:
    if not 0 <= p <= 1:
        raise ValueError("Probability must be in [0,1].")
    if p in (0.0, 1.0):
        return 0.0
    return -p * math.log(p) - (1 - p) * math.log1p(-p)


def budget_error(n: int, budget: float, eps: float) -> float:
    """Largest common-error weight allowed by the diagonal-record budget."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 2:
        raise ValueError("Require integer n >= 2.")
    if not math.isfinite(budget) or budget < 0 or not 0 < eps < 0.5:
        raise ValueError("Require a finite nonnegative budget and 0 < eps < 1/2.")
    if (n - 1) * entropy(eps) <= budget:
        return eps
    lo, hi = 0.0, eps
    for _ in range(160):
        mid = (lo + hi) / 2
        if (n - 1) * entropy(mid) <= budget:
            lo = mid
        else:
            hi = mid
    return lo


def run() -> dict:
    direct_cases = 0
    max_residual = 0.0
    for n in (2, 3, 5, 8):
        for lam in (0.01, 0.1, 0.2):
            dim = 1 << n
            p0 = [0.0] * dim
            p0[0], p0[-1] = 1 - lam, lam
            p1 = list(reversed(p0))
            marginals = [sum(p0[z] for z in range(dim) if (z >> i) & 1)
                         for i in range(n)]
            q0 = [math.prod(marginals[i] if (z >> i) & 1 else 1 - marginals[i]
                            for i in range(n)) for z in range(dim)]
            total_correlation = sum(p * math.log(p / q) for p, q in zip(p0, q0) if p)
            affinity = sum(math.sqrt(p * q) for p, q in zip(p0, p1))
            residual = abs(total_correlation - (n - 1) * entropy(lam))
            max_residual = max(max_residual, residual)
            assert residual < 2e-14
            assert abs(affinity - 2 * math.sqrt(lam * (1 - lam))) < 2e-14
            assert all(abs(p - lam) < 2e-14 for p in marginals)
            joint = sum(p0[z] for z in range(dim) if z & 1 and z & 2)
            assert abs(joint - marginals[0] * marginals[1] - lam * (1 - lam)) < 2e-14
            direct_cases += 1
    eps, budget = 0.2, 0.1
    j_eps = (1 - 2 * eps) * math.log((1 - eps) / eps)
    coefficient = 2 * math.sqrt(budget / j_eps)
    rows = []
    for n in (100, 1000, 10000, 100000, 1000000):
        lam = budget_error(n, budget, eps)
        tc = (n - 1) * entropy(lam)
        visibility = 2 * math.sqrt(lam * (1 - lam))
        assert 0 < lam <= eps and tc <= budget + 1e-14
        assert abs(tc - budget) < 1e-13
        rows.append({"N": n, "common_error": lam, "total_correlation": tc,
                     "diagonal_completion_visibility": visibility,
                     "sqrt_N_visibility": math.sqrt(n) * visibility,
                     "ratio_to_sharp_asymptotic_scale": math.sqrt(n) * visibility / coefficient,
                     "N_logN_error_over_C": n * math.log(n) * lam / budget})
    return {"direct_distribution_cases": direct_cases, "budget_inversion_cases": len(rows),
            "largest_entropy_identity_residual": max_residual,
            "python": sys.version.split()[0],
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "epsilon": eps, "budget_nats": budget,
            "sharp_asymptotic_coefficient": coefficient, "comparison": rows,
            "scope": "Finite checks of our common-error budget calculation; no source-access or priority certification."}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, allow_nan=False))
