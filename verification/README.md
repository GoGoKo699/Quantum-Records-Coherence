# Reproduction and review

## Numerical and structural checks

From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_records.py
python verification/check_common_error.py
python verification/check_bavaro_comparison.py
python verification/check_learning_example.py
python verification/check_repository.py
```

These five scripts do not make network requests. The first three print numerical records with script hashes; their stored outputs use Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0 (the common-error script uses only the standard library). Platform-dependent floating-point differences may occur. Refresh an existing record only after checking the reason for any changes:

```bash
python verification/check_records.py > verification/results.json
python verification/check_common_error.py > verification/common_error_results.json
python verification/check_bavaro_comparison.py > verification/bavaro_comparison_results.json
```

| Check | What it establishes in finite cases |
|---|---|
| `check_records.py` — 149 parameter/state cases | Normalization, conditional errors, entropy and affinity sandwiches, independent endpoint, finite converse, pairwise covariance, entropy certificate, positive completion, gate-level star circuit, and 40 random noncommuting quantum-state comparisons. |
| `check_common_error.py` — 17 cases | Twelve explicit two-point distributions and five inverse-budget calculations; entropy, affinity and covariance identities. |
| `check_bavaro_comparison.py` — 58 cases | The source's numerical example, 33 endpoint/inequality cases including six zero-budget regressions at large $N$, four matching-family comparisons and 20 total-correlation splitting cases. |
| `check_learning_example.py` | The primer's two-record distributions, positive completions with visibility 0.64 and zero, unconditional dependence and bit/nat conversion. |
| `check_repository.py` | Exactly 30 ordered milestones, 14/16 phase allocation, required fields, backward dependencies, selected anchor, six bibliography entries and existing local link targets. |

The case counts are not counts of independent proofs. General heading fragments and external URLs are outside the structural script's checks. Personal coaching records and a separate manuscript entrypoint are excluded from the reader route.

At exactly zero correlation, the comparison function evaluates the product expression directly; it does not round-trip an exponentially small affinity through inverse cosine and cosine. The regression cases prevent the resulting artificial machine-precision visibility floor. This is a numerical endpoint safeguard, not a change to the mathematical statement.

## Representative numerical results

For $\varepsilon=0.2$ and $C=0.1$, the sharp asymptotic coefficient is approximately $0.6934683460$. The matching family at $N=100000$ has $\sqrt N\,v\approx0.6934665317$. The exactly pairwise-independent family at $N=10000$, $\ell=6$ has visibility about $0.0054428834$, total correlation $0.0693432610$, error $0.1999877774$, and correlation certificate $0.0772647888$ nats. Exact independence follows from [the proof](../science/pairwise-independence.md), not from a small floating-point covariance.

For the fixed-budget two-point common-error family at $N=100000$, $\sqrt N\,v\approx0.1503791947$. Its comparison ratio uses the asymptotic sharp scale, not a numerically optimized finite-size frontier. The [inverse-entropy argument](../references/related-work.md) proves its extra logarithmic loss.

The Bavaro comparison reproduces the source example's affinity $0.4555946768$, Bures-angle bound $0.5202211031$, and total-correlation bound $0.5942530214$. For the matching family at $N=100000$, using actual angles gives about $0.00226587078$, while the declared-budget relaxation gives $0.58687874372$. The actual visibility is $0.00219293372$. See the [precise comparison and blockwise deduction](../references/bavaro-comparison.md). These calculations neither certify priority nor claim universal finite-bound superiority.

## Actual hosted mathematical rendering

Source delimiters do not establish correct GitHub display. The separate browser check visits this repository's actual hosted pages at an exact commit and saves full-page rendered screenshots, article coordinates and a JSON report:

```bash
python -m pip install -r verification/render-requirements.txt
python -m playwright install --with-deps chromium
python verification/check_hosted_rendering.py --ref FULL_COMMIT_SHA
```

Unlike the numerical scripts, this command requires network access. It reads public pages without authentication or credentials. It covers all 13 Markdown pages: the root README, the three learning pages, six scientific pages, two related-work pages and this verification guide. It checks renderer error messages, missing rendered expressions, leftover dollar delimiters and the displayed milestone count. A missing page, renderer alert or absent mathematical output is a failure, not a passing review.

The [GitHub Actions workflow](../.github/workflows/verify.yml) runs the numerical, structural and hosted checks, retaining output, the exact reviewed source archive, and screenshots as a seven-day workflow artifact. Action implementations and browser-library version are pinned. The browser step is a real hosted-rendering check, not a local Markdown preview. **Its screenshots still require visual inspection** for layout, tables, clipping, notation and unintended emphasis. A green job alone is not a complete visual review, and an access failure must not be represented as a successful rendering check.

Mathematical display blocks use fenced `math` where Markdown escaping would otherwise alter row separators or delimiters. Operator labels use supported upright notation, and literal set braces are written as named delimiters. These are hosting-compatibility choices, not changes to the equations or a universal notation rule for other projects.

## Evidence boundaries

Written proofs establish the mathematical statements. Numerical cases test finite formulas with ordinary floating-point arithmetic, not interval certification. The structural script does not assess scientific correctness. Browser screenshots assess the inspected pages and commit only. None of these checks supplies independent peer review, exhaustive historical priority, a generic local-dynamics realization, or a result for a different environment partition. Very small budgets and endpoint-near parameters may need higher precision than the numerical scripts provide.
