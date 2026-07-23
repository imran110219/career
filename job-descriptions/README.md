# Job Descriptions

Save a job description as Markdown or plain text, then compare it to a tailored Markdown resume:

```bash
python3 scripts/analyze_ats.py \
  resumes/senior-backend/resume.md \
  job-descriptions/acme-senior-backend.md \
  --output reports/acme-senior-backend-ats.md \
  --json-output reports/acme-senior-backend-ats.json
```

Use this optional metadata block at the top when useful:

```md
---
company: Acme
role: Senior Backend Engineer
source_url: https://example.com/jobs/123
date_saved: 2026-07-23
---
```

Paste the full role description below the metadata. The analyzer recognizes common backend, data, platform, security, and delivery terms, reports exactly what it found, and scores transparent categories. It does not simulate a proprietary ATS or recommend unsupported claims.

Reports are ignored by Git by default. Keep a job description here when it is public-safe; otherwise store it locally under the relevant ignored company application folder.
