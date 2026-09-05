import tempfile
import unittest
from pathlib import Path

from scanner.scan import scan_file


class ScannerTests(unittest.TestCase):
    def test_flags_shell_true(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.py"
            path.write_text("import subprocess\nsubprocess.run('echo hi', shell=True)\n", encoding="utf-8")
            rules = {finding.rule for finding in scan_file(path)}
            self.assertIn("PY001", rules)

    def test_clean_snippet(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.py"
            path.write_text("print('hello')\n", encoding="utf-8")
            self.assertEqual(scan_file(path), [])


if __name__ == "__main__":
    unittest.main()
