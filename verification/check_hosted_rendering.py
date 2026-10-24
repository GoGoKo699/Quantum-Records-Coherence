"""Inspect GitHub's actual Markdown rendering of this repository at a commit.

Requires Playwright and Chromium. Saves screenshots for human/model inspection;
automated success alone is not a visual layout review. No credentials are used.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from playwright.sync_api import sync_playwright

PAGES = ['README.md', 'learning/README.md', 'learning/WATROUS_BRIDGE.md',
         'learning/MILESTONES.md', 'science/sharp-bound.md',
         'science/pairwise-independence.md', 'references/bavaro-comparison.md',
         'science/model.md', 'science/constructions.md', 'science/scope.md',
         'science/README.md', 'references/related-work.md', 'verification/README.md']
SCAN = r'''element => {
  const roots = [element], nodes = [];
  for (let i = 0; i < roots.length; i++) {
    for (const node of roots[i].querySelectorAll('*')) {
      nodes.push(node);
      if (node.shadowRoot) roots.push(node.shadowRoot);
    }
  }
  const count = selector => nodes.filter(n => n.matches(selector)).length;
  return {mathHosts: count('math-renderer'),
          renderedMath: count('mjx-container, math, .katex'),
          mathErrors: nodes.filter(n => n.matches('mjx-merror, .katex-error, .MathJax_Error, [data-mjx-error]'))
                           .map(n => n.textContent),
          headings: [...element.querySelectorAll('h1,h2,h3')].map(n => n.textContent),
          text: element.innerText};
}'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--ref', required=True)
    parser.add_argument('--output', default='artifacts/hosted')
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9a-f]{40}', args.ref):
        raise SystemExit('Use an exact 40-character commit SHA.')
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    rows = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={'width': 1440, 'height': 1100}, device_scale_factor=1)
        for path in PAGES:
            slug = path.replace('/', '__').replace('.md', '')
            url = f'https://github.com/GoGoKo699/Quantum-Records-Coherence/blob/{args.ref}/{path}'
            row = {'path': path, 'url': url, 'ok': False}
            try:
                response = page.goto(url, wait_until='domcontentloaded', timeout=60000)
                row['http_status'] = response.status if response else None
                if not response or response.status != 200:
                    raise RuntimeError('Hosted page did not return HTTP 200.')
                article = page.locator('article.markdown-body').first
                if article.count() == 0:
                    article = page.locator('.markdown-body').first
                article.wait_for(state='visible', timeout=30000)
                page.wait_for_timeout(5000)
                # Scroll through the article so lazy math renderers are activated.
                height = int(page.evaluate('document.documentElement.scrollHeight'))
                for y in range(0, height, 850):
                    page.evaluate('(y) => window.scrollTo(0,y)', y)
                    page.wait_for_timeout(150)
                page.wait_for_timeout(2500)
                info = article.evaluate(SCAN)
                text = info.pop('text')
                (output / f'{slug}.txt').write_text(text)
                row.update(info)
                page.evaluate('window.scrollTo(0, 0)')
                page.wait_for_timeout(750)
                row['article_box'] = article.bounding_box()
                page.screenshot(path=str(output / f'{slug}.png'), full_page=True, timeout=30000)
                row['screenshot'] = f'{slug}.png'
                error_patterns = (r'macros are not allowed', r'(?m)^Missing[^\n]*delimiter[^\n]*$',
                                  r'(?m)^Missing[^\n]*\\end[^\n]*$', r'Undefined control sequence',
                                  r'ParseError', r'KaTeX parse error')
                row['text_errors'] = [pattern for pattern in error_patterns
                                      if re.search(pattern, text, flags=re.I)]
                if info['mathErrors'] or row['text_errors']:
                    raise RuntimeError('A mathematical rendering error is present.')
                if info['renderedMath'] < info['mathHosts']:
                    raise RuntimeError('At least one math host has no rendered expression.')
                if '$' in text:
                    raise RuntimeError('Literal dollar delimiters remain in the displayed article.')
                if path not in ('learning/MILESTONES.md', 'science/README.md') and info['renderedMath'] == 0:
                    raise RuntimeError('No rendered mathematical nodes detected; inspect screenshot.')
                if path == 'learning/MILESTONES.md':
                    milestones = [h for h in info['headings'] if re.match(r'M\d\d\b', h)]
                    if len(milestones) != 30:
                        raise RuntimeError('Rendered page does not contain 30 milestone headings.')
                row['ok'] = True
            except Exception as error:
                row['error'] = str(error)
                page.screenshot(path=str(output / f'{slug}-failure.png'))
            rows.append(row)
        browser.close()
    report = {'repository': 'GoGoKo699/Quantum-Records-Coherence', 'ref': args.ref,
              'all_passed': all(r['ok'] for r in rows), 'pages': rows,
              'scope': 'Actual GitHub pages; screenshots still require visual review.'}
    (output / 'report.json').write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    if not report['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
