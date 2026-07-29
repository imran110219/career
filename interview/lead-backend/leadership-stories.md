# Leadership Stories

Use STAR: Situation, Task, Action, Result, Lesson. Replace `Evidence needed` only when the detail is verified and public-safe.

## Story Backlog

| Story | Candidate source | Status |
| --- | --- | --- |
| Leading a difficult delivery | Election Management System candidate-management or reporting services | Practising |
| Mentoring developers | Backend team guidance, code reviews, design discussions | Practising |
| Resolving architecture disagreement | Service boundary, reporting, integration or API contract decision | Needs evidence review |
| Improving code-review quality | Continuous code-quality and dependency-security remediation | Practising |
| Managing a production incident | Distributed integration or deployment troubleshooting | Practising |
| Communicating technical risk | Sensitive workflow, access control, deployment or deadline risk | Practising |
| Choosing simplicity | Modular design versus unnecessary microservices | Needs evidence review |
| Coordinating modules or teams | SMS, payment, identity, master-data, frontend or reporting coordination | Practising |
| Handling technical debt | Validation, logging, runbooks, query or deployment improvements | Needs evidence review |
| Recovering a delayed project | Election or exam workflow delivery | Evidence needed |

## STAR Template

```markdown
### Story Title

- Situation:
- Task:
- Personal action:
- Team action:
- Result:
- Lesson:
- Evidence level:
- Disclosure limit:
```

## Seed Prompts From Existing Notes

### Mentoring Developers — From Business Context to Independent Delivery

**Use for:** “How do you mentor junior developers?”, “How do you help someone who is blocked?” or “How do you build engineering capability?”

- Situation: I worked with developers who were early in their careers and needed support moving from programming fundamentals to delivering production features. At the beginning of a project, they could struggle to turn business requirements into a clear implementation plan.
- Task: I needed to help them build both technical foundations and the engineering habits needed to contribute effectively: understanding business logic, identifying implementation priorities, breaking work into steps, and asking useful questions before coding.
- Personal action: I trained them progressively from basic to more advanced programming concepts and supported their growth as engineers, not only their assigned tickets. When someone was unsure how to start, I discussed the business rule and the expected workflow first, then helped them divide the feature into smaller implementation steps. For example, when a junior developer was designing an API, I explained that completing the success path was not enough. I guided them to return a consistent response body, handle expected errors and exceptions, use messages that users could understand, and add purposeful logging so that support and developers could diagnose failures. Where a concrete example was useful, I walked through a similar feature I had implemented and explained the decisions behind it. During project discussions, I made time to explain the business logic, technical approach, and priority order so that developers understood why the work mattered, not just what code to write. I reinforced this through implementation guidance and code-review feedback.
- Team action: Junior developers applied the guidance to their assigned work, raised questions during discussions and reviews, and iterated on their implementations.
- Result: The immediate result was that developers had a clearer starting point for implementation and stronger context for making day-to-day decisions. Do not claim a numerical productivity, retention, or promotion outcome unless you can verify it.
- Lesson: Effective mentoring is not giving the solution immediately. I start with the business outcome and constraints, then use examples and smaller steps to help the developer reach a solution they can own next time.
- Evidence level: Professional evidence; measurable outcome needs verification.
- Disclosure limit: Keep examples at feature or workflow level; do not identify individual developers or disclose client-confidential business rules.

**60-second spoken version:**

> I have mentored developers who were early in their careers and were sometimes unsure how to begin implementing a feature. My approach was to start with the business logic: what problem the feature solves, the workflow, and the implementation priorities. Then I helped them break the work into smaller steps. For example, when a junior developer designed an API, I explained that a successful response alone is not sufficient in production. I guided them to use a consistent response body, clear user-facing error messages, appropriate exception handling, and useful logging for diagnosis. I used similar existing features as examples and reinforced the reasoning in design discussions and code reviews. The result was clearer direction for the developer and a more production-ready API design. The lesson is that mentoring works best when you teach the reasoning process, not just the final code.

**Before marking interview-ready, verify:**

- The API or feature context, described without confidential details.
- Whether the guidance happened in a design discussion, code review, or pairing session.
- The observable improvement: revised the API successfully, applied the same pattern later, or needed less implementation support.

### Improving Code Quality — Continuous SonarQube and Trivy Remediation

**Use for:** “How do you improve code quality?”, “What do you look for in reviews?” or “How do you handle dependency vulnerabilities?”

- Situation: In ongoing backend delivery, code-quality issues and vulnerable or obsolete dependencies can accumulate if they are left until a major release or treated as someone else's problem.
- Task: I needed to help keep the codebase maintainable and reduce avoidable dependency risk while continuing feature delivery.
- Personal action: I used SonarQube findings to identify code issues, prioritized items that were meaningful for correctness, maintainability, or delivery risk, and worked with the team to resolve them continuously. I also used Trivy to identify dependency vulnerabilities. When a library was obsolete or had a relevant vulnerability, I guided the update process and ensured the impact on the application was considered rather than upgrading blindly. In code reviews, I reinforced the same expectations: clear error handling, useful logging, maintainable structure, and dependency hygiene.
- Team action: Developers addressed assigned findings and validated their changes; the team incorporated the checks into normal delivery work.
- Result: The team continuously reduced identified code issues and addressed dependency concerns as part of ongoing development. Do not claim zero vulnerabilities, a particular SonarQube rating, or a measured defect reduction unless verified.
- Lesson: Quality works best as a steady engineering practice. Automated findings create visibility, but technical judgment is needed to prioritize what matters, make safe upgrades, and prevent the same issue from recurring.
- Evidence level: Professional evidence; tool configuration, scan cadence, and measurable outcomes need verification.
- Disclosure limit: Do not disclose scan reports, vulnerability identifiers, repository details, security configuration, or internal quality thresholds.

**60-second spoken version:**

> I treat code quality and dependency security as continuous delivery work, not a cleanup activity at the end. We used SonarQube to identify code issues, and I helped prioritize and resolve findings that affected maintainability, correctness, or delivery risk. We also used Trivy to identify dependency vulnerabilities. When a library was obsolete or had a relevant vulnerability, I guided the update carefully and considered its impact on the application before merging it. I reinforced the same standards in code review—error handling, logging, readable structure, and dependency hygiene. The result was a more consistent process for addressing identified issues while features continued to move forward. My main lesson is that tools provide visibility, but leadership is needed to prioritize, validate, and make quality part of normal delivery.

**Before marking interview-ready, verify:**

- Whether SonarQube and Trivy ran in CI, locally, or on a scheduled basis.
- One anonymized example of a code issue or dependency update you handled.
- The testing or validation completed after a dependency upgrade.
- Any safe quality outcome, such as a resolved critical issue or a release gate.

### Leading a Difficult Delivery — Client-Driven Election Reports

**Use for:** “Tell me about a difficult delivery,” “How do you lead cross-functional work?” or “How do you manage delivery risk?”

- Situation: I led delivery for official election reports whose layouts had to reflect detailed client requirements drawn from laws and rule books. Those source documents contained many tabular report formats. The client wanted the system output to match them, but an exact reproduction was not always technically practical or usable in the PDF-reporting platform.
- Task: My responsibility was to provide the report-data APIs and lead the developers designing the report layouts. I had to protect the correctness of the official data while helping the client make practical decisions when a requested tabular format could not be reproduced exactly.
- Personal action: I first clarified what each report needed to communicate and separated that from purely visual formatting requests. I designed the APIs to provide the required report data in a reliable, reusable form. I then guided the report-layout work against the client's requirements, identified early where a rule-book table could not be rendered exactly, and explained the technical and usability consequences in plain language. Rather than silently approximating the request, I discussed alternatives with the client—for example, preserving required fields, ordering, totals, and legal meaning while adapting the presentation to a practical report layout. I incorporated the agreed decision into the design and kept the team aligned through planning, implementation guidance, and code review.
- Team action: Developers implemented the approved layouts, while the reporting/PDF platform rendered the documents. The wider team validated the report data and delivery flow with relevant stakeholders.
- Result: We delivered report capabilities based on agreed, feasible layouts while preserving the required information and legal intent. The credible outcome is alignment on an implementable design and fewer late surprises; add a specific acceptance, release, or rework outcome only if you can verify it.
- Lesson: When a client requirement comes from a formal rule book, “matching the form” and “preserving the meaning” are different requirements. A lead developer should surface that distinction early, make the trade-offs visible, and obtain agreement before the team invests in an unworkable layout.
- Evidence level: Professional evidence; specific outcome details need verification.
- Disclosure limit: Use “election-management platform,” “formal rules,” and “official reports”; do not name the client, disclose rule-book contents, internal platform names, or sensitive report data.

**60-second spoken version:**

> I led delivery for official reports in a sensitive election-management platform. The client’s requirements came from formal laws and rule books, which included many detailed tabular formats. They wanted the report output to match those formats, but an exact visual copy was not always feasible in the reporting platform. My role was to provide the report-data APIs and lead the developers designing the layouts. I clarified which fields and legal meaning had to be preserved, identified layout constraints early, and discussed practical alternatives with the client instead of allowing the team to guess. Once we agreed on a workable design, I guided implementation and reviewed the work for data correctness and maintainability. We delivered reports that preserved the required information while using a feasible layout. The lesson was that, in regulated work, the lead must make the distinction between legal intent and visual form clear early, then document and align on the trade-off.

**Before claiming this as interview-ready, verify:**

- One representative report and the exact layout constraint, stated without exposing confidential content.
- Which alternative the client accepted and how that approval was recorded.
- Whether client review led to one or more revisions before acceptance.
- A safe, observable outcome: release completion, stakeholder sign-off, manual step removed, or rework avoided.

### Production Incident

**Use for:** “Tell me about a production incident,” “How do you troubleshoot integrations?” or “How do you work with DevOps during an outage?”

- Situation: In the candidate-management registration workflow, the backend called an external National ID (NID) service. Registration could not proceed because the application server was unable to reach that external service.
- Task: I needed to determine whether the failure was caused by our application, the external API, or network/service reachability, then engage the team that could resolve the actual issue without making an unsupported code change.
- Personal action: I investigated the registration failure from the backend side and checked the connectivity path from our server to the NID service. This showed that the external service was unreachable from our environment. I communicated the finding and impact to the relevant people, then coordinated with DevOps for the environment-level fix. I kept the diagnosis specific: the evidence pointed to reachability, not an application-level candidate-management defect.
- Team action: DevOps corrected the connectivity/environment issue. The backend and relevant delivery teams then validated that the registration flow could reach the external NID service again.
- Result: The team restored access to the external NID service so the registration integration could proceed. Do not claim downtime, affected-user count, root cause, or prevention measures until those details are verified.
- Lesson: For distributed integrations, I narrow the fault domain before changing code. Confirming whether the request leaves our environment and can reach the dependency helps the team route the incident quickly to the correct owner.
- Evidence level: Professional evidence; incident timing and measurable outcome need verification.
- Disclosure limit: Say “external identity-verification service” in public interviews if naming NID is not approved. Do not disclose endpoints, network configuration, credentials, IP addresses, or internal incident details.

**60-second spoken version:**

> In a candidate-registration workflow, our backend depended on an external identity-verification service. Registration began failing because the service could not be reached from our application environment. I first investigated from the backend side to separate an application bug from an integration or network issue. The connectivity checks showed that the dependency was unreachable from our server, so I communicated the diagnosis and coordinated with DevOps rather than changing application code without evidence. DevOps fixed the environment-level connectivity issue, and we validated that the registration flow could reach the external service again. The key lesson was to narrow the fault domain early; in distributed systems, the fastest resolution often comes from proving where the request stops and involving the right owner.

**Before marking interview-ready, verify:**

- How the issue was detected: user report, failed request, log, monitoring alert, or QA escalation.
- The safe description of the connectivity check and who was informed.
- Whether there was a fallback, retry, or user-facing error message while the service was unavailable.
- The final confirmation method and any prevention action, such as a health check or runbook.

### Slow Database Query

**Use for:** “Tell me about a performance problem,” “How do you optimize a slow API?” or “How do you decide whether to cache?”

- Situation: In an exam-management system, search and filter workflows, along with APIs that used multiple database joins, were affecting response time. Some data was read frequently but changed infrequently, making repeated database reads unnecessary for those cases.
- Task: I needed to improve backend response time without treating caching as a substitute for a sound database design or serving stale data where fresh data was required.
- Personal action: I reviewed the search and filter access patterns, then added indexes where they supported the actual query paths. I optimized queries involving multiple joins to reduce unnecessary database work. For read-heavy, low-write data, I implemented Redis caching so frequently requested values could be served without repeatedly querying the database. I kept the approach selective: data that was updated often was not an automatic caching candidate. The DevOps team used Percona monitoring to observe query efficiency; I used the resulting operational feedback alongside application-level investigation to guide the performance work.
- Team action: The delivery team supported implementation and validation, while DevOps provided database-query observability through Percona.
- Result: The system achieved a reported 30% reduction in response time through Redis caching and backend performance improvements. The exact baseline, measurement window, cache-expiry strategy, and individual contribution of each change still need verification.
- Lesson: I start with the query and access pattern. Indexing and query design address the root database cost; caching is valuable when the data is read often, changes rarely, and its freshness requirements are clear.
- Evidence level: Professional evidence; 30% result is recorded as verified/public-safe, while the measurement method needs capture.
- Disclosure limit: Describe this as an exam-management system; do not disclose database schema, internal query text, monitoring credentials, or confidential usage data.

**60-second spoken version:**

> In an exam-management system, some search and filter operations and APIs with multiple joins were slower than we wanted. I first looked at the access patterns, then added indexes where they matched the real search paths and optimized the queries to avoid unnecessary work across joins. I also introduced Redis caching for data that was read frequently but changed infrequently; I did not apply caching to data that needed frequent updates. DevOps used Percona to observe query efficiency, which supported our investigation and validation. Together, the backend improvements and Redis caching produced a reported 30% reduction in response time. The key lesson was to fix database access first and use caching selectively based on data freshness and read/write behavior.

**Before marking interview-ready, verify:**

- One endpoint, report, search, or filter workflow that was visibly slow.
- The response-time baseline and measurement window behind the reported 30% result.
- One actual index or query change, explained at a public-safe level.
- Cache invalidation or expiry behavior for the Redis data.

### Access-Control Issue

Candidate context: Keycloak-backed role controls and validation.

- Situation: unwanted-data-change or wrong-data-view risk.
- Task: Evidence needed.
- Personal action: authorization and validation changes.
- Result: state controls added unless a quantified risk reduction is verified.
