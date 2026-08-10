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

## Promote a discovered job to application tracking

A role appearing in `latest-jobs.md` is not automatically an application.

1. Reopen the official vacancy page.
2. Confirm that it is still active.
3. Review eligibility.
4. Decide whether to apply.
5. Add one row to `applications/tracker.csv`.
6. Save the job description only when tailoring or ATS analysis is needed.
7. Create `companies/applications/<company>/` only for a serious application.
8. Use the same Job ID across discovery, tracking, and application-package metadata.

Discovery never updates the tracker; adding a tracker row is a manual decision.
Create a company package only when eligibility has been reviewed, the role is
qualified, the candidate intends to apply, and tailoring is useful. Low-quality
rejected discoveries are not permanently stored: Git history preserves prior
reports, while `latest-jobs.md` remains the single current discovery output.

## Tracker status values

Use only: `Researching`, `Qualified`, `Preparing`, `Ready to Apply`, `Applied`,
`Follow-up Due`, `Recruiter Screen`, `Technical Interview`, `Final Interview`,
`Offer`, `Rejected`, `Withdrawn`, or `Closed`.

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
