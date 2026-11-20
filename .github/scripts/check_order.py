#!/usr/bin/env python3
"""Mechanical README ordering, using only the trusted base policy (stdlib only).

Supported resources are single-line, plain Markdown links. Unsupported resource
syntax is UNDETERMINED, never a clean result. No candidate code is executed.
"""
import argparse
from collections import Counter, defaultdict
import html
import json
from pathlib import Path
import re
import subprocess
import sys
import unicodedata

ALPHA = {
 ('Harness-level RSI', 'Extensible Harness Substrates'),
 ('Frameworks & Tools', 'Self-Modifying / Self-Evolving Systems'),
 ('Frameworks & Tools', 'Harness / Memory / Skill Evolution'),
 ('Frameworks & Tools', 'Automated Search / AI R&D'),
 ('Related Awesome Lists',),
}
YEAR = {
 ('Fundamentals & Getting Started',),
 *(('Model-level RSI', s) for s in ['Self-Training & Self-Reward','Synthetic Data & Self-Distillation','Self-Play & Iterative Fine-tuning','Self-Taught Reasoning']),
 *(('Harness-level RSI', s) for s in ['Prompt & Program Optimization','Context & Memory Evolution','Harness & Scaffold Evolution','Self-Verification & Self-Correction — Enabling Foundations','Self-Evolving Agent Frameworks']),
 *(('Multi-Agent Self-Improvement', s) for s in ['Co-Evolution','Inference-time Debate']),
 *(('Coding / Software-Engineering Self-Improvement', s) for s in ['Self-Modifying Coding Agents','Iterative Repair & Training']),
 *((s,) for s in ['Automated AI R&D','Embodied & Physical Self-Improvement','Evolutionary & Open-Ended RSI','Safety, Alignment & Theory','Introspection & Self-Modeling','Blog Posts & Discussions','Talks & Videos']),
 ('Safety, Alignment & Theory','Supporting Safety Foundations'),
 *(('Benchmarks & Evaluations',s) for s in ['Direct RSI & Self-Improvement Evaluations','Frontier Lab Self-Improvement & AI R&D Evaluation Frameworks','AI R&D Capability Proxies','Agent Capability Proxies']),
}
# Future mixed sections must be explicitly registered, with approved undated URLs.
MIXED = {}  # {('Parent','Leaf'): {'https://canonical/tool'}}
def title_key(title):
 s = unicodedata.normalize('NFKC',title).lower()
 s = ''.join(' ' if c.isspace() or c=='/' or unicodedata.category(c)=='Pd' else c for c in s)
 return tuple(w for token in s.split() if (w := ''.join(c for c in token if unicodedata.category(c)[0] in 'LN')))


class Undetermined(ValueError):
    """Input cannot be safely interpreted under this policy."""


def parse(text):
    groups = defaultdict(list)
    headings = defaultdict(set)
    stack = []
    fence = None
    errors = []
    previous_entry = False
    for line, raw in enumerate(text.splitlines(), 1):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", raw)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]))
            previous_entry = False
            continue
        heading = re.fullmatch(r"(#{1,6}) (.+)", raw)
        if heading:
            depth = len(heading[1])
            stack = [v for v in stack if v[0] < depth]
            if depth > 1:
                stack.append((depth, heading[2], line))
            previous_entry = False
            continue
        section = tuple(v[1] for v in stack)
        # Indented continuation of a resource is outside the single-line grammar.
        if previous_entry and raw[:1].isspace() and raw.strip():
            errors.append((line, "unsupported resource continuation"))
        previous_entry = False
        # Internal Contents links and ordinary explanatory bullets are not resources.
        if re.fullmatch(r"\s*[-*+] \[[^\[\]]+\]\(#[^ )]+\)", raw):
            continue
        if re.match(r"\s*[-*+] !\[", raw):
            continue
        resource = re.match(r"\s*(?:[-*+]|[0-9]+[.)])\s+", raw)
        if not resource or not re.search(r"https?://|\[|<[^>]+>", raw):
            continue
        match = re.fullmatch(r"- \[([^\[\]\\`*_<>]+)\]\((https?://[^\s()<>]+)\) - (\S.*)", raw)
        if not match:
            errors.append((line, "unsupported resource syntax"))
            continue
        title, url, desc = match.groups()
        previous_entry = True
        if section not in ALPHA | YEAR | MIXED.keys():
            errors.append((line, "unregistered section: " + repr(section)))
            continue
        annotation = re.search(r"\(([^()]*)\)\.?\s*$", desc)
        years = re.findall(r"(?<!\w)(?:19|20)[0-9]{2}(?!\w)", annotation[1]) if annotation else []
        year = int(years[0]) if len(years) == 1 else None
        if section in YEAR and year is None:
            errors.append((line, "missing or ambiguous final publication year"))
            continue
        if section in MIXED and year is None:
            # A malformed/ambiguous dated annotation is not an undated tool.
            if years or url not in MIXED[section]:
                errors.append((line, "unregistered undated or ambiguous Mixed resource"))
                continue
        key = title_key(title)
        if not key:
            errors.append((line, "empty title key"))
            continue
        prefix = () if section in ALPHA else ((0, -year) if year is not None else (1, 0))
        groups[section].append(dict(line=line, title=title, url=url, year=year,
                                    key=prefix + (key, title, url)))
        headings[section].update(v[2] for v in stack)
    if fence:
        errors.append((len(text.splitlines()), "unclosed code fence"))
    return groups, errors, headings


def parse_diff(patch):
    """Validate unified hunk counts/coordinates; return candidate added lines."""
    if not patch:
        return set()
    lines = patch.splitlines()
    if len(lines) < 3 or lines[0] != "diff --git a/README.md b/README.md":
        raise Undetermined("invalid README diff header")
    i = 1
    if i < len(lines) and re.fullmatch(r"index [0-9a-f]+\.\.[0-9a-f]+(?: [0-7]{6})?", lines[i]):
        i += 1
    if lines[i:i+2] != ["--- a/README.md", "+++ b/README.md"]:
        raise Undetermined("unsupported README diff metadata")
    i += 2
    added = set()
    last_old = last_new = -1
    hunks = 0
    while i < len(lines):
        h = re.fullmatch(r"@@ -([0-9]+)(?:,([0-9]+))? \+([0-9]+)(?:,([0-9]+))? @@.*", lines[i])
        if not h:
            raise Undetermined("invalid diff hunk header")
        old, oc, new, nc = int(h[1]), int(h[2] or 1), int(h[3]), int(h[4] or 1)
        # Zero-count hunks name the line BEFORE the insertion/deletion.
        old_start, new_start = old if oc else old + 1, new if nc else new + 1
        if (oc and old == 0) or (nc and new == 0) or old_start < last_old or new_start < last_new:
            raise Undetermined("overlapping or invalid diff coordinates")
        i += 1
        used_old = used_new = 0
        body = 0
        while i < len(lines) and not lines[i].startswith("@@"):
            raw = lines[i]
            if raw == "\\ No newline at end of file":
                if not body:
                    raise Undetermined("orphan newline marker")
                i += 1
                continue
            if not raw or raw[0] not in "+- ":
                raise Undetermined("invalid diff body")
            if raw[0] == "+":
                added.add(new + used_new)
            used_old += raw[0] in "- "
            used_new += raw[0] in "+ "
            body += 1
            i += 1
        if (used_old, used_new) != (oc, nc) or not body:
            raise Undetermined("diff hunk count mismatch")
        last_old, last_new = old_start + oc, new_start + nc
        hunks += 1
    if not hunks:
        raise Undetermined("diff contains no hunks")
    return added


def identity(section, entry):
    return (section, entry['title'], entry['url'], entry['key'])


def audit(text):
    groups, errors, headings = parse(text)
    findings, pairs, duplicates = [], set(), []
    urls = defaultdict(list)
    for section, entries in groups.items():
        expected = sorted(entries, key=lambda e: e['key'])
        ranks = {e['line']: i for i, e in enumerate(expected)}
        def neighbor(items, index):
            return items[index] if 0 <= index < len(items) else None
        for i, entry in enumerate(entries):
            urls[entry['url']].append(dict(section=section, entry=entry))
            j = ranks[entry['line']]
            descent = i + 1 < len(entries) and entry['key'] > entries[i+1]['key']
            pair = (identity(section, entry), identity(section, entries[i+1])) if descent else None
            if pair:
                pairs.add(pair)
            if descent or i != j:
                findings.append(dict(section=section, entry=entry,
                    adjacent_descent=descent, pair=pair, displaced=i != j,
                    actual_rank=i+1, expected_rank=j+1,
                    current_neighbors=[neighbor(entries, i-1), neighbor(entries, i+1)],
                    canonical_neighbors=[neighbor(expected, j-1), neighbor(expected, j+1)]))
    duplicates = [dict(url=url, occurrences=items) for url, items in urls.items() if len(items) > 1]
    return dict(entries=sum(map(len, groups.values())), sections=len(groups),
                errors=errors, adjacent_descents=sum(f['adjacent_descent'] for f in findings),
                displaced_entries=sum(f['displaced'] for f in findings), findings=findings,
                duplicates=duplicates, groups=groups, headings=headings, pairs=pairs)


def compare(base_text, candidate_text, patch):
    added = parse_diff(patch)
    base, candidate = audit(base_text), audit(candidate_text)
    base_urls = defaultdict(list)
    for section, entries in base['groups'].items():
        for entry in entries:
            base_urls[entry['url']].append(section)
    touched_sections = set()
    for section, entries in candidate['groups'].items():
        for entry in entries:
            entry['touched'] = (entry['line'] in added
                or bool(candidate['headings'][section] & added)
                or (entry['url'] in base_urls and section not in base_urls[entry['url']]))
            if entry['touched']:
                touched_sections.add(section)
    # Deleted resources can change the adjacency of remaining entries.
    for section in set(base['groups']) | set(candidate['groups']):
        before = Counter((e['title'], e['url'], e['key']) for e in base['groups'].get(section, []))
        after = Counter((e['title'], e['url'], e['key']) for e in candidate['groups'].get(section, []))
        if before != after:
            touched_sections.add(section)
    base_positions = {identity(f['section'], f['entry']) for f in base['findings'] if f['displaced']}
    for finding in base['findings']:
        finding['scope'] = ['BASELINE']
    for finding in candidate['findings']:
        # A row can have two findings; classify them independently so an old
        # adjacent edge never hides a newly displaced position (or vice versa).
        scopes = {}
        for kind, present, existing in (
            ('adjacent', finding['adjacent_descent'], finding['pair'] in base['pairs']),
            ('position', finding['displaced'], identity(finding['section'], finding['entry']) in base_positions),
        ):
            if not present:
                continue
            scope = ['BASELINE'] if existing else []
            if finding['section'] in touched_sections:
                scope.append('PR-related')
            scopes[kind] = scope or ['CANDIDATE']
        finding['scope_by_finding'] = scopes
        finding['scope'] = sorted({s for values in scopes.values() for s in values})
    return base, candidate, dict(readme_changed=bool(patch),
        new_pairs=sorted(candidate['pairs'] - base['pairs']),
        resolved_pairs=sorted(base['pairs'] - candidate['pairs']))


def public(result):
    return {k: v for k, v in result.items() if k not in ('groups', 'headings', 'pairs')}


def git(repo, *args):
    result = subprocess.run(['git', '-C', str(repo), *args], capture_output=True, text=True,
                            encoding='utf-8', errors='strict', timeout=60)
    if result.returncode:
        raise Undetermined('git failed: ' + result.stderr.strip())
    return result.stdout


def run(repo, base, head, candidate):
    if not all(re.fullmatch(r'[0-9a-fA-F]{40}', sha) for sha in (base, head)):
        raise Undetermined('base/head must be full SHA hex strings')
    # Resolve a revision to an object id before using it in any later git call.
    resolved = git(repo, 'rev-parse', '--verify', '--end-of-options', candidate + '^{commit}').strip()
    parents = git(repo, 'show', '-s', '--format=%P', resolved).split()
    if parents != [base.lower(), head.lower()]:
        raise Undetermined('candidate merge parents do not match event base/head')
    base_text = git(repo, 'show', base + ':README.md')
    candidate_text = git(repo, 'show', resolved + ':README.md')
    patch = git(repo, 'diff', '--no-ext-diff', '--no-textconv', '--no-renames',
                '--unified=0', base, resolved, '--', 'README.md')
    return compare(base_text, candidate_text, patch)


def exit_code(results, report_only):
    if any(r['errors'] for r in results):
        return 2
    if not report_only and any(r['findings'] for r in results[-1:]):
        return 1
    return 0


def emit(report, summary):
    payload = json.dumps(report, ensure_ascii=True, indent=2)
    # JSON escapes embedded CR/LF; prefix prevents workflow-command interpretation.
    print('ORDER_REPORT ' + payload)
    if summary:
        with open(summary, 'a', encoding='utf-8') as stream:
            stream.write('<h2>README ordering</h2><pre>' + html.escape(payload) + '</pre>\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', default='.')
    parser.add_argument('--base')
    parser.add_argument('--head')
    parser.add_argument('--candidate', default='HEAD')
    parser.add_argument('--readme', help='standalone full-tree audit, without PR attribution')
    parser.add_argument('--report-only', action='store_true')
    parser.add_argument('--summary')
    args = parser.parse_args(argv)
    try:
        if unicodedata.unidata_version != '16.0.0':
            raise Undetermined('expected Unicode 16.0.0; review fixtures before upgrading')
        if args.readme:
            candidate = audit(Path(args.readme).read_text(encoding='utf-8'))
            for finding in candidate['findings']:
                finding['scope'] = ['CANDIDATE']
            results = [candidate]
            report = dict(candidate=public(candidate))
        else:
            if not args.base or not args.head:
                raise Undetermined('--base and --head are required for PR mode')
            base, candidate, attribution = run(args.repo, args.base, args.head, args.candidate)
            results = [base, candidate]
            report = dict(base=public(base), candidate=public(candidate), attribution=attribution)
            if not attribution['readme_changed']:
                report['message'] = 'No ordering-related README changes'
        code = exit_code(results, args.report_only)
        report.update(status='UNDETERMINED' if code == 2 else 'REPORT',
                      report_only=args.report_only, python=sys.version.split()[0],
                      unicode=unicodedata.unidata_version)
        emit(report, args.summary)
        return code
    except (Undetermined, OSError, UnicodeError, subprocess.SubprocessError) as error:
        emit(dict(status='UNDETERMINED', error=str(error)), args.summary)
        return 2


if __name__ == '__main__':
    sys.exit(main())
