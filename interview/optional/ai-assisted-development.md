# AI-Assisted Development

AI-assisted development is a supporting engineering capability. Do not describe it as professional experience until a specific tool, workflow, safeguard and outcome are recorded in [../EVIDENCE_LOG.md](../EVIDENCE_LOG.md).

## Practical Topics

| Topic | Interview focus |
| --- | --- |
| Code generation | Use for drafts, alternatives and boilerplate, followed by human review. |
| Reviewing AI-generated code | Verify APIs, dependencies, error handling, security, tests and maintainability. |
| Test generation | Generate test ideas, edge cases and fixtures; execute and inspect results. |
| Refactoring assistance | Use for mechanical refactors with diff review and regression tests. |
| Documentation generation | Draft README/API docs, then verify against source. |
| SQL review | Ask for index and query-plan hypotheses, then validate with `EXPLAIN ANALYZE`. |
| Architecture brainstorming | Explore options and trade-offs; decisions need evidence and review. |
| Threat-model brainstorming | Generate abuse cases; security owner still validates controls. |
| Log analysis | Summarize logs only when data sensitivity permits. |
| Prompt quality | Provide context, constraints, expected output and verification criteria. |

## Safeguards

- Do not paste secrets, private contact data, credentials, logs with sensitive data or confidential architecture.
- Check for hallucinated APIs, unsupported dependencies and fake configuration.
- Require tests, static checks and human code review before merge.
- Keep prompts and outputs reproducible when used for meaningful engineering work.
- Record measurable usefulness only when it can be verified.

## Evidence Needed Before Resume Use

- Tool used.
- Engineering workflow.
- Human review process.
- Quality or productivity outcome.
- Security/privacy safeguards.
- Link to project, PR, lab or documentation.
