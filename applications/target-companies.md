# Target Companies

## Purpose

This is the canonical preferred-company source for the job-discovery agent. It
supports monitoring order only; a company entry never proves that a particular
vacancy is open, technically suitable, ethically suitable, or eligible from
Bangladesh. Verify those facts on the original vacancy page.

## Eligibility definitions

| Classification | Meaning |
| --- | --- |
| Confirmed eligible | The vacancy or employer explicitly supports the candidate's location or a viable work route. |
| Probably eligible | Evidence supports a route, but a vacancy-specific detail remains to be confirmed. |
| Needs verification | No explicit Bangladesh, contractor, sponsorship, or relocation evidence is available for the vacancy. |
| Not eligible | The vacancy explicitly excludes the candidate's location or work route. |

“Remote” does not mean worldwide. Do not infer Bangladesh eligibility from a
distributed workforce, sponsorship from an international employer, relocation
from an office location, or contractor eligibility from flexible-work language.

## Priority definitions

| Priority | Meaning |
| --- | --- |
| A1 | Strong technical fit with a plausible global or Bangladesh-remote route |
| A2 | Strong company fit, but hiring eligibility must be verified per vacancy |
| B | Primary route is visa-sponsored relocation |
| C | Strategic watchlist or weaker immediate route |
| Paused | Do not actively monitor |
| Archived | No longer relevant |

Ethical review means reviewing the exact product, team, customers, and duties
before applying. Exclude roles that directly support the sectors or activities
listed in `config/job-search.yml`.

## Canonical company list

| Company | Priority | Status | Domain | Target route | Role tracks | Careers URL | ATS | ATS identifier | Eligibility | Ethical review | Check frequency | Last verified | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Canonical | A1 | Active | Linux, cloud, Kubernetes | Global remote | Senior backend; platform; architect | https://canonical.com/careers | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | Prefer Java-adjacent roles; exclude unsupported Linux, Python, Go, or region-restricted roles. |
| LaunchGood | A1 | Active | Crowdfunding and social impact | Global remote | Backend; platform; lead | https://launchgood.com/v4/careers | Unknown | Unknown | Needs verification | Yes | Weekly | 2026-07-26 | Review payment-processing and campaign-compliance scope. |
| Yaqeen Institute | A1 | Monitor | Education and digital products | Vacancy-specific | Backend; platform; architect | https://yaqeeninstitute.org/careers | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | Some roles may be geographically restricted. |
| Muslim Pro / Bitsmedia | A1 | Active | Muslim digital products | Bangladesh remote | Backend; platform; lead | https://career.muslimpro.com | Unknown | Unknown | Probably eligible | Yes | Weekly | 2026-07-26 | Bangladesh presence does not establish eligibility for every vacancy; review fintech scope. |
| Tarteel AI | A1 | Monitor | Speech AI and education | Vacancy-specific | Backend; platform; architect | https://tarteel.ai | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | Confirm hiring geography and role requirements. |
| Temporal.io | A1 | Active | Workflow orchestration | Global remote | Senior backend; platform | https://temporal.io/careers | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | Strong Java and distributed-systems fit; confirm each vacancy's hiring locations. |
| Rocket.Chat | A1 | Monitor | Open-source communications | Global remote | Backend; platform; lead | https://www.rocket.chat/careers | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | Mixed technology stack; confirm Java relevance. |
| HOT (Humanitarian OpenStreetMap Team) | A1 | Monitor | Humanitarian mapping | Global remote | Backend; platform | https://www.hotosm.org/jobs/ | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | Mission-aligned; monitor for relevant engineering roles. |
| UNICEF Innovation | A1 | Monitor | Humanitarian technology | Vacancy-specific | Backend; architect | https://www.unicef.org/careers | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | Confirm employing entity, vacancy location, and work authorization. |
| GitLab | A2 | Active | DevOps platform | International contractor | Backend; platform; lead | https://about.gitlab.com/jobs/ | Greenhouse | Unknown | Needs verification | No | Weekly | 2026-07-26 | All-remote does not mean every country can be employed. |
| Grafana Labs | A2 | Active | Observability | Vacancy-specific | Backend; platform | https://grafana.com/about/careers/ | Greenhouse | Unknown | Needs verification | No | Weekly | 2026-07-26 | Prefer Java-adjacent roles; many backend roles are Go-first. |
| Elastic | A2 | Active | Search and data platform | Vacancy-specific | Backend; platform; architect | https://www.elastic.co/careers | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | Check location and language requirements per role. |
| Camunda | A2 | Active | Process automation | Global remote | Senior backend; architect | https://camunda.com/career/ | Ashby | Unknown | Needs verification | No | Weekly | 2026-07-26 | Confirm that the specific vacancy explicitly permits Bangladesh. |
| Conduktor | A2 | Monitor | Kafka and data streaming | Visa-sponsored relocation | Backend; platform | https://www.conduktor.io/careers | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | European-route target; confirm vacancy geography. |
| Sourcegraph | A2 | Monitor | Code intelligence | Global remote | Backend; platform | https://sourcegraph.com/jobs | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | Confirm legal employing locations and Java relevance. |
| Mattermost | A2 | Monitor | Secure collaboration | Global remote | Backend; platform; security | https://mattermost.com/careers/ | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | Mixed Go and React stack; target only compatible roles. |
| Automattic | A2 | Monitor | Web platform | Global remote | Backend; platform | https://automattic.com/work-with-us/ | Unknown | Unknown | Needs verification | No | Weekly | 2026-07-26 | PHP-heavy; monitor only Java-adjacent engineering roles. |
| JetBrains | B | Active | Developer tools | Visa-sponsored relocation | Backend; platform; architect | https://www.jetbrains.com/careers/ | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Apply only where the vacancy explicitly offers relocation or sponsorship. |
| Alef Education | B | Active | Education technology | Visa-sponsored relocation | Backend; architect | https://www.alefeducation.com/careers/ | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | UAE roles require vacancy-level sponsorship confirmation. |
| Tarabut | B | Active | Open banking APIs | Visa-sponsored relocation | Backend; platform | https://www.tarabut.com/careers | Unknown | Unknown | Needs verification | Yes | Biweekly | 2026-07-26 | Review product scope and financial-services responsibilities. |
| Tamara | B | Ethical review required | Fintech | Visa-sponsored relocation | Backend; distributed systems | https://tamara.co/careers | Greenhouse | Unknown | Needs verification | Yes | Biweekly | 2026-07-26 | Apply only after role-level review; exclude prohibited lending or credit work. |
| Wahed Invest | B | Ethical review required | Investment platform | Visa-sponsored relocation | Backend; data | https://wahed.com/careers | Unknown | Unknown | Needs verification | Yes | Biweekly | 2026-07-26 | Confirm fund and product scope before applying. |
| Salam Booking | B | Monitor | Travel technology | Visa-sponsored relocation | Backend; platform | https://salambooking.com | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm current hiring route. |
| HalalTrip | B | Monitor | Travel technology | Visa-sponsored relocation | Backend; platform | https://www.halaltrip.com | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm current hiring route. |
| Hala | B | Ethical review required | SME fintech | Visa-sponsored relocation | Backend; platform | Unknown | Unknown | Unknown | Needs verification | Yes | Biweekly | 2026-07-26 | Verify financial product mechanics and team scope. |
| Noon Academy | B | Monitor | Education technology | Vacancy-specific | Backend; platform | https://www.noonacademy.com/careers | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm work location and sponsorship for each role. |
| Classera | B | Ethical review required | Education technology | Vacancy-specific | Backend; platform | https://www.classera.com/careers | Unknown | Unknown | Needs verification | Yes | Biweekly | 2026-07-26 | Review payment and marketplace product responsibilities. |
| GovTech Singapore | B | Monitor | Public digital services | Visa-sponsored relocation | Backend; architect | https://www.tech.gov.sg/careers | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Sponsorship and foreign eligibility are vacancy-specific. |
| Synapxe | B | Monitor | Public health technology | Visa-sponsored relocation | Backend; platform | https://www.synapxe.sg/careers | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Sponsorship and foreign eligibility are vacancy-specific. |
| NCS | B | Monitor | Public and enterprise technology | Visa-sponsored relocation | Backend; platform | https://www.ncs.co/en-sg/careers/ | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Country and vacancy-specific eligibility. |
| Altibbi | B | Monitor | Telehealth | Visa-sponsored relocation | Backend; platform | https://altibbi.com | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm current careers route and sponsoring entity. |
| Okadoc | B | Monitor | Health technology | Visa-sponsored relocation | Backend; platform | https://www.okadoc.com | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm current careers route and sponsoring entity. |
| Lean Business Services | B | Monitor | Health technology | Visa-sponsored relocation | Backend; platform | https://lean.sa/careers | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm sponsorship for each vacancy. |
| Elm | B | Monitor | Public digital services | Visa-sponsored relocation | Backend; architect | https://elm.sa/en/careers | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm sponsorship for each vacancy. |
| Takamol Holding | B | Monitor | Public platforms | Visa-sponsored relocation | Backend; platform | https://takamolholding.com/careers | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm sponsorship for each vacancy. |
| Thiqah | B | Monitor | Government and enterprise services | Visa-sponsored relocation | Backend; platform | https://thiqah.sa | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm sponsorship for each vacancy. |
| Unifonic | B | Monitor | Communications APIs | Visa-sponsored relocation | Backend; platform | https://www.unifonic.com/careers | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm sponsorship and product team. |
| SITE | B | Ethical review required | Digital government | Visa-sponsored relocation | Backend; platform | https://site.sa | Unknown | Unknown | Needs verification | Yes | Biweekly | 2026-07-26 | Review government, security, and surveillance adjacency. |
| CNTXT | B | Monitor | Cloud services | Visa-sponsored relocation | Backend; platform | https://www.cntxt.com/careers | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm sponsorship and role fit. |
| Presight | B | Ethical review required | AI and analytics | Visa-sponsored relocation | Backend; platform | https://presight.ai/careers | Unknown | Unknown | Needs verification | Yes | Biweekly | 2026-07-26 | Review surveillance, government, and defence-adjacent scope. |
| Aerodyne Group | B | Monitor | Drone and digital services | Visa-sponsored relocation | Backend; platform | https://aerodyne.group/careers | Unknown | Unknown | Needs verification | Yes | Biweekly | 2026-07-26 | Review drone and customer-use scope. |
| RunCloud | B | Monitor | Developer tools | Visa-sponsored relocation | Backend; platform | https://runcloud.io/careers | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm location and work authorization. |
| Mekari | B | Monitor | Enterprise SaaS | Visa-sponsored relocation | Backend; platform | https://mekari.com/career/ | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Confirm location and work authorization. |
| Picus Security | C | Monitor | Security platform | Visa-sponsored relocation | Backend; platform | https://www.picussecurity.com/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and role fit. |
| Halodoc | B | Monitor | Health technology | Local or regional only | Backend; platform | https://www.halodoc.com/careers | Unknown | Unknown | Needs verification | No | Biweekly | 2026-07-26 | Local or regional hiring may be the primary route. |
| Alodokter | C | Monitor | Health technology | Local or regional only | Backend; platform | https://www.alodokter.com/career | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Local or regional hiring may be the primary route. |
| Ruangguru | C | Monitor | Education technology | Local or regional only | Backend; platform | https://career.ruangguru.com | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Local or regional hiring may be the primary route. |
| Red Hat | C | Monitor | Enterprise software | Visa-sponsored relocation | Backend; platform | https://www.redhat.com/en/jobs | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Monitor compatible Java roles and explicit work routes. |
| Sonar | C | Monitor | Code quality | Visa-sponsored relocation | Backend; platform | https://www.sonarsource.com/company/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and hiring route. |
| HERE Technologies | C | Monitor | Mapping technology | Visa-sponsored relocation | Backend; platform | https://www.here.com/careers | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and product scope. |
| TomTom | C | Monitor | Mapping technology | Visa-sponsored relocation | Backend; platform | https://www.tomtom.com/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and product scope. |
| Esri | C | Monitor | Geospatial software | Visa-sponsored relocation | Backend; platform | https://www.esri.com/en-us/about/careers/overview | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and product scope. |
| Carto | C | Monitor | Spatial data | Visa-sponsored relocation | Backend; platform | https://carto.com/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and product scope. |
| Redis | C | Monitor | Data platform | Vacancy-specific | Backend; platform | https://redis.io/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and role fit. |
| MongoDB | C | Monitor | Data platform | Visa-sponsored relocation | Backend; platform | https://www.mongodb.com/careers | Greenhouse | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and role fit. |
| Confluent | C | Monitor | Data streaming | Visa-sponsored relocation | Backend; platform | https://www.confluent.io/careers/ | Greenhouse | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and role fit. |
| JFrog | C | Monitor | DevOps platform | Visa-sponsored relocation | Backend; platform | https://jfrog.com/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and role fit. |
| Snyk | C | Monitor | Security platform | Visa-sponsored relocation | Backend; platform | https://snyk.io/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and role fit. |
| Sentry | C | Monitor | Developer tools | Vacancy-specific | Backend; platform | https://sentry.io/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and role fit. |
| Postman | C | Monitor | API platform | Visa-sponsored relocation | Backend; platform | https://www.postman.com/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and role fit. |
| Docker | C | Monitor | Container platform | Visa-sponsored relocation | Backend; platform | https://www.docker.com/career-openings/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Core engineering may require infrastructure evidence beyond the verified profile. |
| SUSE | C | Monitor | Linux and cloud | Visa-sponsored relocation | Backend; platform | https://www.suse.com/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm stack and geography. |
| Cloudflare | C | Monitor | Internet infrastructure | Visa-sponsored relocation | Backend; platform | https://www.cloudflare.com/careers/jobs/ | Greenhouse | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Systems roles may exceed verified infrastructure evidence; review customer scope. |
| Akamai | C | Monitor | Internet infrastructure | Visa-sponsored relocation | Backend; platform | https://www.akamai.com/careers | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm stack and geography. |
| Cockroach Labs | C | Monitor | Distributed database | Visa-sponsored relocation | Backend; platform | https://www.cockroachlabs.com/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Database-internals roles may exceed verified evidence. |
| Neo4j | C | Monitor | Graph database | Visa-sponsored relocation | Backend; platform | https://neo4j.com/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Database-engine roles may exceed verified evidence. |
| Celonis | C | Monitor | Process intelligence | Visa-sponsored relocation | Backend; platform | https://www.celonis.com/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm stack and geography. |
| Acronis | C | Monitor | Cybersecurity | Visa-sponsored relocation | Backend; platform | https://careers.acronis.com/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm stack and geography. |
| Atlassian | C | Monitor | Developer tools | Visa-sponsored relocation | Backend; platform | https://www.atlassian.com/company/careers | Greenhouse | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm employing location and work route. |
| Contentful | C | Monitor | Content platform | Visa-sponsored relocation | Backend; platform | https://www.contentful.com/careers/ | Greenhouse | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and role fit. |
| Nokia | C | Ethical review required | Telecommunications | Visa-sponsored relocation | Backend; platform | https://www.nokia.com/about-us/careers/ | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review security, government, and lawful-interception scope. |
| Ericsson | C | Ethical review required | Telecommunications | Visa-sponsored relocation | Backend; platform | https://www.ericsson.com/en/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review security, government, and lawful-interception scope. |
| Siemens Digital Industries Software | C | Monitor | Industrial software | Visa-sponsored relocation | Backend; platform | https://jobs.siemens.com/careers | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm product area and work route. |
| Bosch Digital | C | Monitor | Industrial software | Visa-sponsored relocation | Backend; platform | https://www.bosch.com/careers/ | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm product area and work route. |
| ViTrox | C | Monitor | Industrial technology | Visa-sponsored relocation | Backend; platform | https://www.vitrox.com/careers | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm role relevance and work route. |
| Property Finder | C | Ethical review required | Property marketplace | Visa-sponsored relocation | Backend; platform | https://www.propertyfinder.ae/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review marketplace and advertising responsibilities. |
| Bayut | C | Ethical review required | Property marketplace | Visa-sponsored relocation | Backend; platform | https://www.bayut.com/careers/ | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review marketplace and advertising responsibilities. |
| Privy | C | Monitor | Digital identity | Visa-sponsored relocation | Backend; platform | https://privy.id/career | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and role fit. |
| Careem | C | Ethical review required | Super-app | Visa-sponsored relocation | Backend; platform | https://www.careem.com/careers/ | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review financial-services and product scope. |
| Tabby | C | Ethical review required | Fintech | Visa-sponsored relocation | Backend; platform | https://tabby.ai/careers | Greenhouse | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Exclude prohibited lending or credit work. |
| Foodics | C | Ethical review required | Merchant platform | Visa-sponsored relocation | Backend; platform | https://www.foodics.com/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review merchant product responsibilities. |
| Mozn | C | Ethical review required | AI and security | Visa-sponsored relocation | Backend; platform | https://mozn.sa/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review security and government customer scope. |
| GoTo / Gojek | C | Ethical review required | Super-app | Visa-sponsored relocation | Backend; platform | https://www.gotocompany.com/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review financial-services and product scope. |
| Grab | C | Ethical review required | Super-app | Visa-sponsored relocation | Backend; platform | https://www.grab.careers/ | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review financial-services and product scope. |
| Xendit | C | Ethical review required | Payment infrastructure | Visa-sponsored relocation | Backend; platform | https://www.xendit.co/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Confirm team scope before applying. |
| Lalamove | C | Monitor | Logistics technology | Visa-sponsored relocation | Backend; platform | https://www.lalamove.com/en/careers | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Confirm geography and work route. |
| G42 / Core42 | C | Ethical review required | AI and cloud | Visa-sponsored relocation | Backend; platform | https://www.g42.ai/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review government, surveillance, and defence-adjacent scope. |
| Rohde & Schwarz | C | Ethical review required | Communications technology | Visa-sponsored relocation | Backend; platform | https://www.rohde-schwarz.com/career/ | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review defence and surveillance adjacency. |
| Amazon | C | Ethical review required | Cloud and commerce | Visa-sponsored relocation | Backend; platform | https://www.amazon.jobs/ | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review business unit, customers, and role scope. |
| Google | C | Ethical review required | Technology platform | Visa-sponsored relocation | Backend; platform | https://www.google.com/about/careers/ | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review business unit, customers, and role scope. |
| Microsoft | C | Ethical review required | Technology platform | Visa-sponsored relocation | Backend; platform | https://jobs.careers.microsoft.com/ | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review business unit, customers, and role scope. |
| Oracle | C | Ethical review required | Enterprise software | Visa-sponsored relocation | Backend; platform | https://www.oracle.com/careers/ | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review business unit, customers, and role scope. |
| SAP | C | Ethical review required | Enterprise software | Visa-sponsored relocation | Backend; platform | https://www.sap.com/about/careers.html | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review business unit, customers, and role scope. |
| IBM | C | Ethical review required | Enterprise software | Visa-sponsored relocation | Backend; platform | https://www.ibm.com/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review business unit, customers, and role scope. |
| Vercel | C | Monitor | Developer platform | Vacancy-specific | Backend; platform | https://vercel.com/careers | Unknown | Unknown | Needs verification | No | Monthly | 2026-07-26 | Platform roles may exceed verified infrastructure evidence. |
| Salla | C | Ethical review required | Merchant platform | Visa-sponsored relocation | Backend; platform | https://salla.com/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review merchant product responsibilities. |
| Zid | C | Ethical review required | Merchant platform | Visa-sponsored relocation | Backend; platform | https://zid.sa/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review merchant product responsibilities. |
| StoreHub | C | Ethical review required | Merchant platform | Visa-sponsored relocation | Backend; platform | https://www.storehub.com/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review merchant product responsibilities. |
| Dubizzle Group | C | Ethical review required | Marketplace | Visa-sponsored relocation | Backend; platform | https://www.dubizzlegroup.com/careers | Unknown | Unknown | Needs verification | Yes | Monthly | 2026-07-26 | Review marketplace and advertising responsibilities. |
| Quran.com / Quran Foundation | C | Monitor | Education and digital infrastructure | Unverified | Backend; platform | https://quran.foundation | Unknown | Unknown | Needs verification | No | Manual only | 2026-07-26 | Hiring route is unverified. |
| Muslim Central | C | Monitor | Educational media | Unverified | Backend; platform | https://muslimcentral.com | Unknown | Unknown | Needs verification | No | Manual only | 2026-07-26 | Hiring route is unverified. |
| Islamic Network | C | Monitor | Islamic APIs | Unverified | Backend; platform | https://www.islamicnetwork.com | Unknown | Unknown | Needs verification | No | Manual only | 2026-07-26 | Hiring route is unverified. |
