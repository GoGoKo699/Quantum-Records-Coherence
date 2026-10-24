"""Finite checks for the records/coherence theorems; not a substitute for proofs.
Run from the repository root: python verification/check_records.py
"""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import brentq, minimize_scalar
from scipy.special import gammaln, logsumexp, xlogy
from scipy.stats import binom, hypergeom


def h(p: float) -> float:
    if not 0 <= p <= 1:
        raise ValueError("Probability must be in [0,1].")
    return float(-xlogy(p, p) - xlogy(1-p, 1-p))


def kl(p: float, q: float) -> float:
    if not 0 < q < 1:
        raise ValueError("Reference probability must be in (0,1).")
    return float(xlogy(p, p/q) + xlogy(1-p, (1-p)/(1-q)))


def tail_cap(c: float, s: float) -> float:
    """Largest p >= exp(-s) with d(p || exp(-s)) <= c."""
    if c < 0 or s <= 0:
        raise ValueError("Require c >= 0 and s > 0.")
    if c >= s:
        return 1.0
    q = math.exp(-s)
    if c == 0:
        return q
    log1mq = math.log(-math.expm1(-s))
    return brentq(lambda p: p*s-h(p)-(1-p)*log1mq-c,
                  q, 1.0, xtol=5e-324, rtol=1e-14)


def upper(n: int, eps: float, c: float) -> float:
    if n < 1 or not 0 < eps < .5 or c < 0:
        raise ValueError("Require n >= 1, 0 < eps < 1/2, c >= 0.")
    single = 2*math.sqrt(eps*(1-eps))
    if c == 0:
        return single**n
    def bound(t: float) -> float:
        return 2*math.sqrt(tail_cap(c, n*kl(t, 1-eps))) + tail_cap(c, n*kl(t, eps))
    opt = minimize_scalar(bound, bounds=(eps+(.5-eps)*1e-5, .5-(.5-eps)*1e-5), method="bounded")
    # Any admissible t is an upper bound; this search need not find its minimum.
    return min(single, bound(float(opt.x)))


def normalized(logw: np.ndarray) -> np.ndarray:
    return np.exp(logw-logsumexp(logw))


def mixture(r: np.ndarray, t: float) -> np.ndarray:
    return (1-t)*r+t*r[::-1]


def stats(w: np.ndarray) -> dict[str, float]:
    n = len(w)-1
    k = np.arange(n+1)
    p = float(w@k/n)
    positive = w > 0
    tc = float(np.sum(w[positive]*(np.log(w[positive])-binom.logpmf(k[positive], n, p))))
    covariance = float(w@(k*(k-1))/(n*(n-1))-p*p) if n > 1 else 0.0
    return {"error": p, "total_correlation": tc, "pair_covariance": covariance,
            "visibility": float(np.sqrt(w)@np.sqrt(w[::-1]))}


def sharp(n: int, eps: float, c: float) -> tuple[np.ndarray, float, float]:
    if n < 1 or not 0 < eps < .5 or not 0 <= c < n*h(eps):
        raise ValueError("Require n >= 1, 0 < eps < 1/2 and 0 <= c < n*h(eps).")
    a_of_t = lambda t: (eps-t)/(1-2*t)
    t = brentq(lambda t: n*(h(eps)-h(a_of_t(t)))-c, 0, eps,
               xtol=5e-324, rtol=1e-14) if c else 0.0
    a = a_of_t(t)
    r = normalized(binom.logpmf(np.arange(n+1), n, a))
    return mixture(r, t), t, a


def pairwise(n: int, eps: float, ell: int) -> tuple[np.ndarray, float, float]:
    if n < 2 or ell < 2 or not 0 < eps < .5:
        raise ValueError("Require n >= 2, integer ell >= 2 and 0 < eps < 1/2.")
    m_total = ell*n
    a_star = (1-math.sqrt((1-2*eps)**2+4*eps*(1-eps)/m_total))/2
    m = math.floor(m_total*a_star)
    if m == 0:
        raise ValueError("Increase n: nonzero population needed.")
    a = m/m_total
    p = (1-math.sqrt(1-4*m_total*a*(1-a)/(m_total-1)))/2
    t = (p-a)/(1-2*a)
    r = normalized(hypergeom.logpmf(np.arange(n+1), m_total, m, n))
    i = np.arange(n, dtype=float)
    certificate = float(np.sum(i/((m_total-1)*(m_total-i)))+n*(h(p)-h(a)))
    return mixture(r, t), t, certificate


def full_prob(w: np.ndarray) -> np.ndarray:
    n = len(w)-1
    k = np.array([z.bit_count() for z in range(2**n)])
    comb = np.exp(gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1))
    return w[k]/comb


def entropy(rho: np.ndarray) -> float:
    vals = np.maximum(np.linalg.eigvalsh(rho).real, 0)
    return float(-np.sum(xlogy(vals, vals)))


def marginal(rho: np.ndarray, n: int, keep: int) -> np.ndarray:
    out = rho.reshape([2]*(2*n))
    live = n
    for j in reversed(range(n)):
        if j != keep:
            out = np.trace(out, axis1=j, axis2=j+live)
            live -= 1
    return out


def run() -> dict:
    checks = 0
    for eps in (.1, .2, .35, .45):
        for n in (2, 5, 20, 100, 1000):
            for c in (.001, .03, .2):
                w, t, a = sharp(n, eps, c)
                z = stats(w)
                assert abs(w.sum()-1) < 1e-12
                assert abs(z["error"]-eps) < 2e-11
                assert c-h(t)-2e-9 <= z["total_correlation"] <= c+2e-9
                lower = 2*math.sqrt(t*(1-t))
                assert lower-1e-12 <= z["visibility"] <= lower+(1-2*t)*(2*math.sqrt(a*(1-a)))**n+1e-11
                assert z["visibility"] <= upper(n, eps, c)+1e-10
                checks += 1
            w, _, _ = sharp(n, eps, 0)
            assert abs(stats(w)["visibility"]-upper(n, eps, 0)) < 2e-12
            checks += 1
    max_pair_residual = 0.0
    for eps in (.1, .2, .35):
        for n in (20, 100, 1000):
            for ell in (2, 6, 20):
                w, t, cert = pairwise(n, eps, ell)
                z = stats(w)
                assert z["error"] <= eps+1e-12
                assert abs(z["pair_covariance"]) < 1e-10
                assert z["total_correlation"] <= cert+1e-9
                assert z["visibility"] >= 2*math.sqrt(t*(1-t))-1e-12
                assert z["visibility"] <= upper(n, eps, cert)+1e-10
                max_pair_residual = max(max_pair_residual, abs(z["pair_covariance"]))
                checks += 1
    # Explicit isometric purification: R is additional to the N records.
    n, d = 3, 8
    w, _, _ = sharp(n, .2, .1)
    p0 = full_prob(w)
    p1 = p0[::-1]
    v = np.zeros((2, d, d, 2))
    for x, p in enumerate((p0, p1)):
        for z in range(d):
            v[x, z, z, x] = math.sqrt(p[z])
    v = v.reshape(2*d*d, 2)
    assert np.allclose(v.T@v, np.eye(2), atol=1e-12)
    psi = (v@np.ones(2)/math.sqrt(2)).reshape(2, d, d)
    rho = np.einsum('xzr,ywr->xzyw', psi, psi).reshape(2*d, 2*d)
    target = .5*np.block([[np.diag(p0), np.diag(np.sqrt(p0*p1))],
                          [np.diag(np.sqrt(p0*p1)), np.diag(p1)]])
    assert np.max(np.abs(rho-target)) < 1e-12
    assert np.linalg.eigvalsh(rho).min() >= -1e-12
    assert abs(2*np.trace(rho[:d,d:]).real-stats(w)["visibility"]) < 1e-12
    checks += 1
    # Linear-gate star circuit: S, F, N records E and N purifiers R.
    _, t, a = sharp(n, .2, .1)
    state = np.zeros(2**(2*n+2))
    state[0] = 1
    indices = np.arange(len(state))
    def one(gate: np.ndarray, bit: int) -> None:
        zero = indices[((indices >> bit) & 1) == 0]
        pair = zero | (1 << bit)
        vals = gate@np.stack((state[zero], state[pair]))
        state[zero], state[pair] = vals[0], vals[1]
    def cnot(control: int, target: int) -> None:
        perm = indices ^ (((indices >> control) & 1) << target)
        state[:] = state[perm]
    def ry_probability(p: float) -> np.ndarray:
        return np.array([[math.sqrt(1-p), -math.sqrt(p)],
                         [math.sqrt(p), math.sqrt(1-p)]])
    one(np.array([[1,1],[1,-1]])/math.sqrt(2), 2*n+1)
    one(ry_probability(t), 2*n)
    for i in range(n):
        one(ry_probability(a), n+i)
        cnot(n+i, i)
    cnot(2*n+1, 2*n)
    for i in range(n):
        cnot(2*n, n+i)
    psi = state.reshape(2,2,d,d)
    rho = np.einsum('xfzr,yfwr->xzyw', psi, psi).reshape(2*d,2*d)
    assert np.max(np.abs(2*rho[:d,:d]-np.diag(p0))) < 1e-12
    assert np.max(np.abs(2*rho[d:,d:]-np.diag(p1))) < 1e-12
    assert abs(2*np.trace(rho[:d,d:]).real-2*math.sqrt(t*(1-t))) < 1e-12
    checks += 1
    # Generic, noncommuting conditional states: measured TC and coherence bounds.
    rng = np.random.default_rng(2402026)
    for n in (2, 3):
        d = 2**n
        for _ in range(20):
            g = rng.normal(size=(2*d, 2*d))+1j*rng.normal(size=(2*d, 2*d))
            rho = g@g.conj().T
            factors = np.repeat([1/math.sqrt(2*np.trace(rho[:d,:d]).real),
                                 1/math.sqrt(2*np.trace(rho[d:,d:]).real)], d)
            rho = factors[:,None]*rho*factors[None,:]
            probs = []
            for x in range(2):
                conditional = 2*rho[x*d:(x+1)*d,x*d:(x+1)*d]
                p = np.diag(conditional).real
                probs.append(p)
                tq = sum(entropy(marginal(conditional,n,i)) for i in range(n))-entropy(conditional)
                bits = np.array([[(z>>i)&1 for z in range(d)] for i in range(n)])
                tc = sum(h(float(row@p)) for row in bits)+float(np.sum(xlogy(p,p)))
                assert tc <= tq+1e-11
            assert 2*abs(np.trace(rho[:d,d:])) <= np.sqrt(probs[0])@np.sqrt(probs[1])+1e-12
            checks += 1
    eps, c = .2, .1
    coefficient = 2*math.sqrt(c/((1-2*eps)*math.log((1-eps)/eps)))
    convergence = []
    for n in (100, 1000, 10000, 100000):
        w, t, _ = sharp(n, eps, c)
        z = stats(w)
        convergence.append({"N": n, **z, "sqrt_N_visibility": math.sqrt(n)*z["visibility"]})
    assert abs(convergence[-1]["sqrt_N_visibility"]/coefficient-1) < 1e-4
    pw, _, certificate = pairwise(10000, eps, 6)
    return {"checks_passed": checks, "seed": 2402026,
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "numpy": np.__version__, "scipy": scipy.__version__,
            "sharp_coefficient_eps_0_2_C_0_1": coefficient,
            "sharp_convergence": convergence,
            "pairwise_N_10000_ell_6": {**stats(pw), "correlation_certificate": certificate},
            "largest_pair_covariance_residual": max_pair_residual,
            "scope": "Finite algebra, distribution and quantum-state checks; asymptotic proofs are in science/."}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, allow_nan=False))
