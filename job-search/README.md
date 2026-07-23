# Job Search Workspace

This directory contains manually generated job-discovery reports.

## Files

- `AGENT.md` — stable instructions for the job-discovery agent
- `latest-jobs.md` — latest generated and validated job report

Search positioning, scoring, markets, and filtering are configured in:

`../config/job-search.yml`

Application progress is tracked in:

`../applications/tracker.csv`

Preferred companies may be maintained in:

`../applications/target-companies.md`

## Run with Codex

Use:

```text
Read `job-search/AGENT.md` and `config/job-search.yml`.

Search the public web for currently open jobs matching the configured profile. Validate original vacancy pages, revalidate existing report entries, score and classify eligible roles, remove expired and duplicate jobs, and replace `job-search/latest-jobs.md`.

Do not modify resumes, configuration, evidence files, or `applications/tracker.csv`. Do not automatically apply.
```

## Important

The report is research support, not proof of eligibility.

Always verify:

- vacancy status
- remote scope
- visa sponsorship
- relocation support
- work-authorization requirements

before applying.
