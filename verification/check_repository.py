"""Validate local reading links, milestone dependencies and source conventions."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def run() -> dict:
    milestone_text = (ROOT / 'learning/MILESTONES.md').read_text()
    parts = re.split(r'^### (M\d\d) — (.+)$', milestone_text, flags=re.M)
    ids = parts[1::3]
    assert ids == [f'M{i:02}' for i in range(1, 31)], 'Expected exactly M01–M30.'
    phase_two = milestone_text.index('## Phase II')
    assert milestone_text[:phase_two].count('\n### M') == 14
    assert milestone_text[phase_two:].count('\n### M') == 16
    for ident, body in zip(parts[1::3], parts[3::3]):
        for field in ['Question', 'Target', 'Dependencies', 'Story role and connection', 'Sources']:
            assert f'**{field}:**' in body, (ident, field)
        dependencies = re.search(r'\*\*Dependencies:\*\* (.+)', body)[1]
        for dependency in re.findall(r'M\d\d', dependencies):
            assert int(dependency[1:]) < int(ident[1:]), (ident, dependency)
        assert f'id="{ident.lower()}"' in milestone_text
    bridge = (ROOT / 'learning/WATROUS_BRIDGE.md').read_text()
    assert 'Single educational anchor' in bridge and 'Watrous' in bridge
    assert 'unsquared fidelity' in bridge and 'nats' in bridge and 'bits' in bridge
    checked_links = 0
    markdown_files = sorted(ROOT.rglob('*.md'))
    for path in markdown_files:
        text = path.read_text()
        assert len(re.findall(r'^\$\$$', text, flags=re.M)) % 2 == 0, path
        assert text.count('```') % 2 == 0, path
        for target in re.findall(r'\]\(([^)]+)\)', text):
            url = urlsplit(target)
            if url.scheme or target.startswith('//'):
                continue
            dest = (path.parent / unquote(url.path)).resolve() if url.path else path
            assert dest.is_relative_to(ROOT) and dest.exists(), (path, target)
            # Check explicit milestone fragments. Other heading slugs need the host renderer.
            if re.fullmatch(r'm\d\d', url.fragment):
                assert f'id="{url.fragment}"' in dest.read_text(), (path, target)
            checked_links += 1
    guide = (ROOT / 'llms.txt').read_text()
    assert 'No educational anchor has been selected' not in guide
    assert 'learning/MILESTONES.md' in guide and 'learning/WATROUS_BRIDGE.md' in guide
    assert not (ROOT / 'manuscript/main.md').exists()
    assert not list(ROOT.rglob('COACHING.md'))
    bibliography = (ROOT / 'references/references.bib').read_text()
    keys = re.findall(r'@\w+\{([^,]+),', bibliography)
    assert len(keys) == len(set(keys)) == 6
    assert 'Watrous2018' in keys
    return {'milestones': len(ids), 'background': 14, 'narrative': 16,
            'markdown_files': len(markdown_files), 'local_link_targets': checked_links,
            'bibliography_entries': len(keys), 'anchor': 'Watrous (2018)',
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope': 'Source structure and local paths; not external links, general heading slugs or hosted rendering.'}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
