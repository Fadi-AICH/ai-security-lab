# Code-Agent Security Review Checklist

Use this checklist when reviewing code produced or modified by an AI coding assistant.

## Inputs and trust boundaries

- [ ] Are user-controlled values validated before reaching interpreters, shells, SQL or file paths?
- [ ] Are external documents/web content treated as untrusted data rather than instructions?
- [ ] Are model/tool inputs separated from system-level instructions?

## Secrets and credentials

- [ ] No API keys, passwords or tokens are hard-coded.
- [ ] Secrets are loaded from an appropriate secret store or environment variable.
- [ ] Logs and error messages do not expose secrets.

## Command and code execution

- [ ] Avoid `shell=True` unless there is a documented, constrained reason.
- [ ] Avoid dynamic `eval` / `exec` on untrusted values.
- [ ] Command arguments are passed as structured argument lists where possible.
- [ ] Tool permissions follow least privilege.

## File and path handling

- [ ] Paths are normalized and constrained to expected directories.
- [ ] Uploaded/generated filenames cannot escape the intended directory.
- [ ] Sensitive local files are not automatically exposed to the model/agent.

## Dependencies

- [ ] New packages are necessary and maintained.
- [ ] Versions are pinned where reproducibility matters.
- [ ] Generated package names are checked for typosquatting/hallucination.

## Cryptography and authentication

- [ ] Modern, appropriate primitives are used.
- [ ] No custom cryptography is introduced without a strong reason.
- [ ] Authentication/authorization checks happen server-side.

## Output handling

- [ ] Model-generated code/output is reviewed before execution.
- [ ] Structured outputs are schema-validated.
- [ ] HTML/Markdown/UI output is escaped or sanitized where required.

## Verification

- [ ] Unit/security tests cover the changed security boundary.
- [ ] Static analysis is run.
- [ ] Dependency/security scanning is run where applicable.
- [ ] Human review is required before sensitive tool execution or deployment.
