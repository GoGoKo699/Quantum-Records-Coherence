"""Check the teaching example and bit/nat conversion; not an asymptotic proof."""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path
import numpy as np


def run() -> dict:
    p = np.array([16, 4, 4, 1], dtype=float) / 25
    q = p[::-1]
    bits = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
    assert np.allclose(bits @ p, [.2, .2])
    assert np.allclose((1 - bits) @ q, [.2, .2])
    assert np.allclose(p, np.kron([.8, .2], [.8, .2]))
    b = float(np.sqrt(p) @ np.sqrt(q))
    assert math.isclose(b, .64, abs_tol=1e-14)
    cross = np.diag(np.sqrt(p * q))
    rho = .5 * np.block([[np.diag(p), cross], [cross, np.diag(q)]])
    dephased = .5 * np.block([[np.diag(p), np.zeros((4, 4))],
                              [np.zeros((4, 4)), np.diag(q)]])
    for state in [rho, dephased]:
        assert abs(np.trace(state) - 1) < 1e-14
        assert np.linalg.eigvalsh(state).min() >= -1e-14
        assert np.allclose(2 * state[:4, :4], np.diag(p))
        assert np.allclose(2 * state[4:, 4:], np.diag(q))
    v = float(2 * np.trace(rho[:4, 4:]))
    vd = float(2 * np.trace(dephased[:4, 4:]))
    assert math.isclose(v, .64, abs_tol=1e-14) and vd == 0
    average = (p + q) / 2
    assert np.allclose(average, np.array([17, 8, 8, 17]) / 50)
    assert np.allclose(bits @ average, [.5, .5])
    assert not np.allclose(average, np.full(4, .25))
    d_nats = float(np.sum(p * np.log(p / q)))
    d_bits = float(np.sum(p * np.log2(p / q)))
    assert math.isclose(d_nats, math.log(2) * d_bits, rel_tol=1e-14)
    c_nats = .1
    c_bits = c_nats / math.log(2)
    j_nats = .6 * math.log(4)
    j_bits = .6 * math.log2(4)
    assert math.isclose(c_nats / j_nats, c_bits / j_bits, rel_tol=1e-14)
    return {"example": "N=2, epsilon=1/5, conditional product laws",
            "affinity": b, "completion_visibility": v, "dephased_visibility": vd,
            "unconditional_distribution": average.tolist(),
            "bit_nat_conversion_checked": True,
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope": "Finite learning example and convention check only."}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, allow_nan=False))
