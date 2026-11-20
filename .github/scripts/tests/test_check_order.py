"""Inline README/diff fixtures plus real-git driver tests; no network required."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'check_order.py'
spec = importlib.util.spec_from_file_location('check_order', SCRIPT)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
YEAR = 'Fundamentals & Getting Started'
ALPHA = 'Related Awesome Lists'


def entry(title, year='2026', url=None):
    return f'- [{title}]({url or "https://example.com/" + title.replace(" ", "_")}) - Description.' + (f' ({year})' if year else '')


def readme(*entries, section=YEAR):
    return '## ' + section + '\n\n' + '\n'.join(entries) + '\n'


def patch(old, new):
    # Use git's actual diff format, not a parser-shaped approximation.
    import difflib
    lines = list(difflib.unified_diff(old.splitlines(), new.splitlines(),
                                    fromfile='a/README.md', tofile='b/README.md', n=0, lineterm=''))
    return 'diff --git a/README.md b/README.md\n' + '\n'.join(lines) + '\n' if lines else ''


class Keys(unittest.TestCase):
    def test_articles_preserved(self):
        self.assertEqual(c.title_key('The Meta-Agent'), ('the', 'meta', 'agent'))
        self.assertEqual(c.title_key('An Agent'), ('an', 'agent'))
        self.assertEqual(c.title_key('A Self'), ('a', 'self'))
        self.assertLess(c.title_key('A Self'), c.title_key('Huxley'))

    def test_punctuation_dashes_slashes(self):
        self.assertEqual(c.title_key('Tree-search / AI—R&D'), ('tree', 'search', 'ai', 'rd'))
        self.assertEqual(c.title_key('Tree search'), c.title_key('Tree-search'))
        self.assertNotEqual(c.title_key('Treesearch'), c.title_key('Tree-search'))

    def test_nfkc_lower(self):
        self.assertEqual(c.title_key('ＡＩＤＥ²'), ('aide2',))

    def test_apostrophe(self):
        self.assertEqual(c.title_key("Don't"), c.title_key('Dont'))

    def test_text_numbers_and_accents(self):
        self.assertLess(c.title_key('Agent 10'), c.title_key('Agent 2'))
        self.assertLess(c.title_key('Godel'), c.title_key('Gödel'))
        self.assertLess(c.title_key('Tree'), c.title_key('Tree search'))

    def test_exact_tiebreakers(self):
        r = c.audit(readme(entry('Dont'), entry("Don't")))
        self.assertEqual(r['adjacent_descents'], 1)
        r = c.audit(readme(entry('Alpha', url='https://e/z'), entry('Alpha', url='https://e/A')))
        self.assertEqual(r['displaced_entries'], 2)


class Parsing(unittest.TestCase):
    def test_final_annotation_only(self):
        r = c.audit(readme(entry('ICLR 2026 Title', '2025', 'https://e/2024')))
        self.assertEqual(next(iter(r['groups'].values()))[0]['year'], 2025)
        self.assertFalse(r['errors'])

    def test_missing_ambiguous_and_nonstandalone_years(self):
        for year in ('', '2025 and 2026', 'X2026', '20260', '1899', '2100'):
            with self.subTest(year=year):
                self.assertTrue(c.audit(readme(entry('Title 2026', year)))['errors'])
        self.assertTrue(c.audit(readme(entry('Title') + ' More prose.'))['errors'])

    def test_trailing_period(self):
        self.assertFalse(c.audit(readme(entry('A') + '.'))['errors'])

    def test_year_vs_alpha(self):
        text = readme(entry('Zeta', '2026'), entry('Alpha', '2025'))
        self.assertEqual(c.audit(text)['adjacent_descents'], 0)
        text = readme(entry('Zeta', '2026'), entry('Alpha', '2025'), section=ALPHA)
        self.assertEqual(c.audit(text)['adjacent_descents'], 1)
        self.assertFalse(c.audit(readme(entry('Tool', ''), section=ALPHA))['errors'])

    def test_mixed_explicit_allowlist(self):
        c.MIXED[('Fixture',)] = {'https://e/tool'}
        try:
            r = c.audit(readme(entry('Zeta'), entry('Alpha', '', 'https://e/tool'), section='Fixture'))
            self.assertFalse(r['errors'])
            self.assertEqual(r['adjacent_descents'], 0)
            self.assertTrue(c.audit(readme(entry('Tool', ''), section='Fixture'))['errors'])
            self.assertTrue(c.audit(readme(entry('Tool', '2025 2026', 'https://e/tool'), section='Fixture'))['errors'])
        finally:
            c.MIXED.clear()

    def test_parent_child_independent(self):
        text = readme(entry('Zeta')) + '\n### Unknown\n' + entry('Alpha')
        r = c.audit(text)
        self.assertEqual(r['entries'], 1)
        self.assertEqual(len(r['errors']), 1)
        self.assertEqual(r['adjacent_descents'], 0)

    def test_unsupported_syntax(self):
        lines = ['* [A](https://e/a) - Description. (2026)',
                 '- [[A]](https://e/a) - Description. (2026)',
                 '- [A](https://e/a)', '- [A][reference]', '- [Unclosed',
                 '- [A](https://e/(a)) - Description. (2026)',
                 '- [**A**](https://e/a) - Description. (2026)',
                 entry('A') + '\n  continuation',
                 entry('!!!', url='https://e/a')]
        for line in lines:
            with self.subTest(line=line):
                self.assertTrue(c.audit(readme(line))['errors'])

    def test_ignore_contents_prose_and_fences(self):
        text = ('## Contents\n- [Scope](#scope)\nText [link](https://e/a).\n'
                '- Explanatory bullet.\n- ![Map](https://e/image.png)\n~~~markdown\n' + entry('Ignored') + '\n```\n~~~\n')
        r = c.audit(text)
        self.assertEqual((r['entries'], r['errors']), (0, []))
        self.assertTrue(c.audit('```\n' + entry('Hidden'))['errors'])

    def test_duplicate_occurrences_stable(self):
        r = c.audit(readme(entry('A'), entry('A')))
        self.assertEqual(r['entries'], 2)
        self.assertEqual(r['displaced_entries'], 0)
        self.assertEqual(len(r['duplicates'][0]['occurrences']), 2)


class DiffAndScope(unittest.TestCase):
    def test_hunk_context_deletion_and_no_newline(self):
        fixture = ('diff --git a/README.md b/README.md\nindex abc..def 100644\n'
                   '--- a/README.md\n+++ b/README.md\n@@ -2,2 +2,2 @@\n context\n-old\n+new\n'
                   '\\ No newline at end of file\n@@ -7,0 +8 @@\n+insert\n')
        self.assertEqual(c.parse_diff(fixture), {3, 8})
        self.assertEqual(c.parse_diff(''), set())

    def test_damaged_diff(self):
        good = patch('old\n', 'new\n')
        for bad in ('garbage', good.replace('+1 @@', '+1,2 @@'),
                    good.replace('@@ -1', '@ -1'), good + '?bad\n',
                    good.replace('--- a/README.md', '--- /dev/null'),
                    good + '@@ -1 +1 @@\n-a\n+b\n'):
            with self.subTest(bad=bad):
                with self.assertRaises(c.Undetermined):
                    c.parse_diff(bad)

    def test_movement_and_baseline_pairs(self):
        base = readme(entry('B'), entry('A'), entry('C'))
        new = readme(entry('C'), entry('B'), entry('A'))
        b, n, delta = c.compare(base, new, patch(base, new))
        self.assertEqual(b['findings'][0]['scope'], ['BASELINE'])
        old_edge = next(f for f in n['findings'] if f['entry']['title'] == 'B')
        self.assertIn('BASELINE', old_edge['scope'])
        self.assertIn('PR-related', old_edge['scope'])
        self.assertEqual(len(delta['new_pairs']), 1)
        self.assertTrue(all('current_neighbors' in f and 'canonical_neighbors' in f for f in n['findings']))

    def test_cross_section_and_heading_changes(self):
        base = readme(entry('A'), section=ALPHA)
        new = readme(entry('A'))
        _, n, _ = c.compare(base, new, patch(base, new))
        self.assertTrue(n['groups'][(YEAR,)][0]['touched'])
        # Heading-only edit must touch an unchanged resource line.
        self.assertNotIn(3, c.parse_diff(patch(base, new)))

    def test_duplicates_do_not_overwrite_url_attribution(self):
        base = readme(entry('A'), section=ALPHA) + readme(entry('A'))
        _, n, _ = c.compare(base, base, '')
        self.assertEqual(n['entries'], 2)
        self.assertTrue(all(not e['touched'] for es in n['groups'].values() for e in es))

    def test_exit_codes(self):
        clean = c.audit(readme(entry('A')))
        bad = c.audit(readme(entry('B'), entry('A')))
        unknown = c.audit(readme(entry('A', '')))
        self.assertEqual(c.exit_code([bad], True), 0)
        self.assertEqual(c.exit_code([bad], False), 1)
        self.assertEqual(c.exit_code([unknown], True), 2)
        self.assertEqual(c.exit_code([clean], False), 0)

    def test_undetermined_cli_and_resolved_pairs(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'README.md'
            path.write_text(readme(entry('A', '')))
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(c.main(['--readme', str(path), '--report-only']), 2)
            self.assertIn('UNDETERMINED', out.getvalue())
        before = readme(entry('B'), entry('A'))
        after = readme(entry('A'), entry('B'))
        _, _, delta = c.compare(before, after, patch(before, after))
        self.assertEqual(len(delta['resolved_pairs']), 1)
        self.assertEqual(delta['new_pairs'], [])

    def test_safe_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'summary'
            with contextlib.redirect_stdout(io.StringIO()) as stdout:
                c.emit({'title': '<script>```\n::error::unsafe'}, path)
            self.assertNotIn('<script>', path.read_text())
            self.assertNotIn('\n::error::', stdout.getvalue())
            self.assertIn('&lt;script&gt;', path.read_text())


class GitDriver(unittest.TestCase):
    def test_real_merge_and_failures(self):
        with tempfile.TemporaryDirectory() as tmp:
            def git(*args):
                return subprocess.check_output(['git', '-C', tmp, *args], stderr=subprocess.STDOUT, text=True).strip()
            git('init', '-b', 'main')
            git('config', 'user.name', 'Fixture')
            git('config', 'user.email', 'fixture@example.com')
            path = Path(tmp) / 'README.md'
            path.write_text(readme(entry('A')))
            git('add', '.'); git('commit', '-m', 'base')
            base = git('rev-parse', 'HEAD')
            git('checkout', '-b', 'feature')
            path.write_text(readme(entry('B'), entry('A')))
            git('add', '.'); git('commit', '-m', 'head')
            head = git('rev-parse', 'HEAD')
            git('checkout', 'main'); git('merge', '--no-ff', 'feature', '-m', 'candidate')
            b, n, delta = c.run(tmp, base, head, 'HEAD')
            self.assertEqual(n['adjacent_descents'], 1)
            self.assertEqual(b['adjacent_descents'], 0)
            self.assertTrue(delta['readme_changed'])
            for bs, hs, rev in [(base, base, 'HEAD'), (base, head, head),
                                ('--bad', head, 'HEAD'), (base, head, 'missing')]:
                with self.subTest(bs=bs, hs=hs, rev=rev), self.assertRaises(c.Undetermined):
                    c.run(tmp, bs, hs, rev)
            args = ['--repo', tmp, '--base', base, '--head', head, '--report-only']
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(c.main(args), 0)
            self.assertIn('PR-related', out.getvalue())
            path.unlink()
            git('add', '.'); git('commit', '--amend', '--no-edit')
            with self.assertRaises(c.Undetermined):
                c.run(tmp, base, head, 'HEAD')

    def test_no_readme_change_audits_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            def git(*args):
                return subprocess.check_output(['git', '-C', tmp, *args], stderr=subprocess.STDOUT, text=True).strip()
            git('init', '-b', 'main'); git('config', 'user.name', 'Fixture'); git('config', 'user.email', 'f@example.com')
            (Path(tmp) / 'README.md').write_text(readme(entry('B'), entry('A')))
            git('add', '.'); git('commit', '-m', 'base'); base = git('rev-parse', 'HEAD')
            git('checkout', '-b', 'feature')
            (Path(tmp) / 'other').write_text('fixture')
            git('add', '.'); git('commit', '-m', 'head'); head = git('rev-parse', 'HEAD')
            git('checkout', 'main'); git('merge', '--no-ff', 'feature', '-m', 'candidate')
            b, n, delta = c.run(tmp, base, head, 'HEAD')
            self.assertFalse(delta['readme_changed'])
            self.assertEqual(n['findings'][0]['scope'], ['BASELINE'])
            self.assertEqual(c.exit_code([b, n], False), 1)


if __name__ == '__main__':
    unittest.main()
