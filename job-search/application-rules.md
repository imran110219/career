# Application Rules

## Research and Matching

1. Read `AGENTS.md`, `job-search/candidate-profile.md`, `job-search/job-preferences.md`, and the relevant canonical resume and evidence files before tailoring.
2. Prefer official vacancy pages or the original employer/recruiter posting over aggregators.
3. Record publication date, last verification date, active/closed status, location, work mode, salary, sponsorship or relocation terms, and application URL.
4. Rank opportunities using role fit, verified technical match, seniority, relocation or remote eligibility, salary transparency, and posting recency.
5. Do not treat search keywords as evidence of candidate experience.

## Evidence and Writing

- Never invent employers, dates, technologies, certifications, responsibilities, metrics, salary, work authorization, or application outcomes.
- Use the canonical resume and achievement inventory as the source of truth.
- Mark candidate-provided but unverified details as `needs-review` until confirmed.
- Preserve personal ownership boundaries and distinguish reported team/platform outcomes from measured individual outcomes.
- Tailor only from verified facts; omit unsupported job-description keywords.
- Use the role-specific resume track that best matches the posting: `senior-backend`, `lead-backend`, `staff-backend`, or `software-architect`.

## Application Preparation

- Generate a tailored resume and cover letter only after the role is confirmed active and eligible.
- Prepare customized application answers from verified experience and label any answer requiring user confirmation.
- Do not disclose private contact data, confidential employer details, references, salary expectations, or identity documents without explicit user direction.
- Do not upload files, send messages, or enter sensitive information into LinkedIn or an employer site without explicit approval for that specific destination and action.

## Approval Gate

- Searching, reading postings, scoring fit, and drafting materials are allowed without additional approval.
- Adding a role to the tracker is allowed when it is clearly a research record and does not claim an application was submitted.
- Before submitting any application, ask the user to approve the exact company, role, location, resume version, cover letter, and final answers.
- Never click the final Apply/Submit button automatically.
- After submission, record the date, exact URL, resume version, status, and any confirmation identifier only if the user authorized submission and the site confirms it.

## Tracker Fields

Maintain `applications/tracker.csv` with:

- Company
- Position
- Role track
- Location and work mode
- Salary range
- Job URL and source
- Date found and last verified
- Fit score and priority
- Visa/relocation eligibility
- Resume version
- Status
- Application date
- Next action and follow-up date
- Notes and outcome reason

Use statuses from the existing job-search workflow, including `Researching`, `Qualified`, `Preparing`, `Ready to Apply`, `Applied`, `Follow-up Due`, `Rejected`, `Withdrawn`, and `Closed`.
