from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Finding:
    path: Path
    line: int
    rule: str
    message: str


RULES = [
    ("PY001", re.compile(r"\bshell\s*=\s*True\b"), "subprocess shell=True may enable command injection"),
    ("PY002", re.compile(r"\bos\.system\s*\("), "os.system executes shell commands directly"),
    ("PY003", re.compile(r"\beval\s*\("), "eval executes dynamic Python expressions"),
    ("PY004", re.compile(r"\bexec\s*\("), "exec executes dynamic Python code"),
    ("PY005", re.compile(r"hashlib\.(md5|sha1)\s*\("), "weak hash primitive detected"),
    ("PY006", re.compile(r"yaml\.load\s*\([^\n]*Loader\s*=\s*yaml\.Loader"), "unsafe YAML loader detected"),
    ("PY007", re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*=\s*['\"][^'\"]{6,}['\"]"), "possible hard-coded secret-like value"),
]


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return findings
    for index, line in enumerate(lines, start=1):
        for rule_id, pattern, message in RULES:
            if pattern.search(line):
                findings.append(Finding(path, index, rule_id, message))
    return findings


def iter_python_files(target: Path):
    if target.is_file() and target.suffix == ".py":
        yield target
    elif target.is_dir():
        yield from target.rglob("*.py")


def main() -> None:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("samples")
    findings: list[Finding] = []
    for path in iter_python_files(target):
        findings.extend(scan_file(path))

    if not findings:
        print("No matching risky patterns found.")
        return

    for finding in findings:
        print(f"{finding.path}:{finding.line} [{finding.rule}] {finding.message}")
    print(f"\n{len(findings)} finding(s).")


if __name__ == "__main__":
    main()
