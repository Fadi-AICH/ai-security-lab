import hashlib
import os
import subprocess

# Safe training fixture: intentionally insecure patterns for scanner validation.
API_KEY = "example-not-a-real-secret"


def run_user_command(command: str) -> None:
    subprocess.run(command, shell=True)


def legacy_hash(value: bytes) -> str:
    return hashlib.md5(value).hexdigest()


def parse_dynamic(expression: str):
    return eval(expression)


def direct_shell(command: str) -> int:
    return os.system(command)
