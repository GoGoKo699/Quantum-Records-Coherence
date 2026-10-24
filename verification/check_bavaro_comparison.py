"""Check the statement-level Bavaro comparison; no external PDF is redistributed.

Run: python verification/check_bavaro_comparison.py
Dependencies are the same as check_records.py. The block refinement is derived
in references/bavaro-comparison.md, not attributed to the source manuscript.
"""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path
import sys
import numpy as np
import scipy
from scipy.stats import binom
import check_records as core


def angle_from_correlation(c: float) -> float:
    if not math.isfinite(c) or c < 0:
        raise ValueError("Require a finite, nonnegative correlation.")
    # Equivalent to acos(exp(-c/2)), more stable near zero.
    return math.atan2(math.sqrt(-math.expm1(-c)), math.exp(-c/2))


def angle_bound(product_affinity: float, gamma0: float, gamma1: float) -> float:
    if not 0 <= product_affinity <= 1 or min(gamma0, gamma1) < 0:
        raise ValueError("Invalid affinity or angle.")
    angle = max(0.0, math.acos(product_affinity)-gamma0-gamma1)
    return math.cos(angle)


def direct(n: int, eps: float, c: float) -> float:
    if not isinstance(n, int) or isinstance(n, bool) or n < 1 or not 0 < eps < .5:
        raise ValueError("Require integer n >= 1 and 0 < eps < 1/2.")
    r = 2*math.sqrt(eps*(1-eps))
    gamma = angle_from_correlation(c)
    # Preserve the exact independent endpoint instead of a cos(pi/2) rounding floor.
    if c == 0:
        return r**n
    return angle_bound(r**n, gamma, gamma)


def direct_limit(c: float) -> float:
    if not math.isfinite(c) or c < 0:
        raise ValueError("Require a finite nonnegative budget.")
    if c >= math.log(2):
        return 1.0
    return 2*math.exp(-c/2)*math.sqrt(-math.expm1(-c))


def block_refinement(n: int, eps: float, c: float) -> tuple[float, int, int]:
    """Best of our elementary r**k + 2 sqrt(c/floor(n/k)) bounds."""
    direct(n, eps, c)  # validate inputs
    r = 2*math.sqrt(eps*(1-eps))
    candidates = ((min(r, r**k+2*math.sqrt(c/(n//k))), k, n//k)
                  for k in range(1, n+1))
    return min(candidates)


def source_example() -> dict[str, float]:
    p = np.array([.83, .07, .07, .03])
    q = p[::-1]
    proxy = np.array([.81, .09, .09, .01])
    affinity = float(np.sqrt(p)@np.sqrt(q))
    gamma = math.acos(float(np.sqrt(p)@np.sqrt(proxy)))
    tc = float(np.sum(p*np.log(p/proxy)))
    geometric = angle_bound(.36, gamma, gamma)
    entropy_bound = angle_bound(.36, angle_from_correlation(tc), angle_from_correlation(tc))
    assert abs(affinity-.45559) < 1e-5
    assert abs(gamma-.08942) < 1e-5
    assert abs(tc-.01802) < 1e-5
    assert abs(geometric-.52022) < 1e-5
    assert abs(entropy_bound-.59425) < 1e-5
    assert .36 < affinity <= geometric <= entropy_bound
    return {"joint_affinity": affinity, "product_proxy_affinity": .36,
            "branch_Bures_angle": gamma, "branch_total_correlation": tc,
            "Theorem_6_2_bound": geometric, "Corollary_6_3_bound": entropy_bound}


def run() -> dict:
    source = source_example()
    endpoint_checks = 0
    for eps in (.1, .2, .35):
        r = 2*math.sqrt(eps*(1-eps))
        for n in (1, 5, 20):
            assert abs(direct(n, eps, 0)-r**n) < 1e-14
            endpoint_checks += 1
        for n in (1000, 100000):
            assert direct(n, eps, 0) == r**n
            endpoint_checks += 1
        for c in (.001, .1, math.log(2), 1.0):
            assert abs(direct(100000, eps, c)-direct_limit(c)) < 1e-12
            endpoint_checks += 1
    for c in (0., 1e-8, .001, .1, .7, 3.):
        assert angle_from_correlation(c) <= math.sqrt(c)+1e-14
        endpoint_checks += 1
    eps, c = .2, .1
    coefficient = 2*math.sqrt(c/((1-2*eps)*math.log((1-eps)/eps)))
    rows = []
    for n in (100, 1000, 10000, 100000):
        w, _, _ = core.sharp(n, eps, c)
        z = core.stats(w)
        r = 2*math.sqrt(eps*(1-eps))
        proxy = core.normalized(binom.logpmf(np.arange(n+1), n, eps))
        gamma = math.acos(min(1.0, float(np.sqrt(w)@np.sqrt(proxy))))
        geometric = angle_bound(r**n, gamma, gamma)
        entropy_actual = direct(n, eps, max(0.0, z["total_correlation"]))
        uniform = direct(n, eps, c)
        block, k, m = block_refinement(n, eps, c)
        sharp_upper = core.upper(n, eps, c)
        assert z["visibility"] <= geometric+1e-10 <= entropy_actual+2e-10
        assert entropy_actual <= uniform+1e-10
        assert z["visibility"] <= block+1e-10
        assert z["visibility"] <= sharp_upper+1e-10
        rows.append({"N": n, "attained_visibility": z["visibility"],
                     "actual_branch_total_correlation": z["total_correlation"],
                     "actual_branch_Bures_angle": gamma,
                     "Bavaro_with_actual_angles": geometric,
                     "Bavaro_with_actual_total_correlations": entropy_actual,
                     "Bavaro_with_budget_C": uniform,
                     "derived_block_bound": block, "block_size": k, "block_count": m,
                     "our_finite_upper_bound": sharp_upper,
                     "sharp_asymptotic_scale_not_finite_bound": coefficient/math.sqrt(n)})
    # Consistency of the total-correlation splitting inequality on explicit laws.
    rng = np.random.default_rng(24102026)
    splitting_checks = 0
    for _ in range(20):
        p = rng.dirichlet(np.ones(16)).reshape(2,2,2,2)
        ent = lambda a: -float(np.sum(a*np.log(a)))
        marg = [p.sum(axis=tuple(j for j in range(4) if j != i)) for i in range(4)]
        b0, b1 = p.sum(axis=(2,3)), p.sum(axis=(0,1))
        total = sum(ent(a) for a in marg)-ent(p)
        t0 = ent(marg[0])+ent(marg[1])-ent(b0)
        t1 = ent(marg[2])+ent(marg[3])-ent(b1)
        assert t0+t1 <= total+1e-12
        splitting_checks += 1
    return {"source_example_cases": 1, "endpoint_inequality_cases": endpoint_checks,
            "matching_family_cases": len(rows), "correlation_splitting_cases": splitting_checks,
            "source_pdf_sha256": "50aaff14f11a81da5ee7557d3ff86e446d8075b69717daf220ad75ff814410f9",
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "core_source_sha256": hashlib.sha256(Path(core.__file__).read_bytes()).hexdigest(),
            "python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__,
            "Bavaro_Remark_6_4": source, "epsilon": eps, "budget_nats": c,
            "direct_fixed_budget_limit": direct_limit(c),
            "sharp_asymptotic_coefficient": coefficient, "comparison": rows,
            "scope": "Finite internal checks; the block refinement is derived here. No exhaustive priority or finite-optimality certification."}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, allow_nan=False))
