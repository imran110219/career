# Cloud and DevOps Preparation

Cloud and DevOps support the target roles. They should not replace the Lead Backend, Senior Backend, or Software Architect positioning.

## Focus Areas

| Area | Practical interview focus |
| --- | --- |
| Containers | Docker, Docker Compose, image hygiene, multi-stage builds. |
| Kubernetes | Deployments, services, config, secrets, probes, resource requests, secure configuration. |
| Helm | Values, releases, rollback concept, environment differences. |
| CI/CD | GitHub Actions, Jenkins, build/test/security stages, release gates, rollback. |
| AWS fundamentals | IAM, EC2, RDS, ElastiCache, S3, load balancing, Auto Scaling, CloudWatch, ECS, EKS basics, Secrets Manager. |
| IaC | Terraform fundamentals, state, modules, environment separation, security checks. |
| Observability | Logs, metrics, traces, OpenTelemetry, Prometheus, Grafana, alerting, runbooks. |
| Reliability | Deployment strategy, rollback, disaster recovery, backup/restore, incident follow-up. |

## High-Priority DevSecOps Topics

- Secure CI/CD.
- SAST fundamentals.
- Dependency scanning.
- Container scanning with Trivy.
- Secret management.
- Terraform fundamentals and Terraform security checks.
- Threat modelling and OWASP.
- SBOM and supply-chain security fundamentals.
- IAM and audit logging.
- Observability with OpenTelemetry, Prometheus and Grafana.
- Secure Kubernetes configuration.

## Experience-Based Questions

- What CI/CD stages would you require before deploying a Spring Boot service?
- How would you roll back a failed backend deployment?
- How would you design observability for a high-risk election workflow?
- What AWS services would you use for a Spring Boot API backed by PostgreSQL and Redis?
- What Kubernetes responsibilities are résumé-safe based on current evidence?
- How would you prevent secrets from leaking through logs, CI, or containers?

## Practice Tasks

- Document a CI/CD pipeline design for a backend service with test and security gates.
- Build a small lab with Docker Compose, PostgreSQL, Redis, and health checks.
- Add an observability plan with metrics, logs, traces, dashboards, and alerts.
- Record lab or professional evidence in [EVIDENCE_LOG.md](../EVIDENCE_LOG.md).

## Evidence Notes

Docker, CI/CD, GitHub Actions, Jenkins, Nginx configuration, Locust load testing, and Kubernetes deployment support are recorded. Cloud-platform ownership, Terraform, observability ownership, and advanced Kubernetes administration remain evidence gaps.
