---
blueprint:
  documentId: KTA-PRIV-001
  documentType: security-privacy-legal-annex
  schemaVersion: 1.0.0
  templateVersion: 3.0.0
  status: draft
  owner: Jeremy Longshore
  authors: ["Intent Solutions / Codex"]
  reviewers: []
  approvers: []
  generatedAt: 2026-09-10
  updatedAt: 2026-09-10
  classification: public-draft
  sourceRefs: [KTA-PRD-001, KTA-ARCH-001, SR-107, SR-108, SR-109, SR-110]
  assumptions: [A-101, A-102, A-104]
  unknowns: [U-101, U-104, U-105, U-108]
  relatedArtifacts: [KTA-AC-001, KTA-TEST-001, KTA-RISK-001, KTA-OPS-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure privacy, legal, and child-safety annex

> This is a product and engineering control proposal, not legal advice. "COPPA compliant" must not be published as a marketing claim until qualified review confirms the actual released data flows, notices, consent method, vendors, retention, and deletion behavior.

## Privacy position

The safest first release is local-first and deliberately boring about data. A child creates a device-local avatar profile, plays offline, and produces progress stored only on that device. The parent buys through an external adult flow. The app verifies a signed license that contains no child profile information. No child gameplay telemetry, advertising identifier, IP-linked analytics, crash dump, photo, voice, location, contact, or account identifier is transmitted.

This architecture reduces risk but does not make law or policy work disappear. The website, payment provider, license recovery, support email, update service, downloads, and any consented beta tooling still create data flows that require accurate notices and retention rules.

## HustleStats legal artifact inventory

Observed on 2026-09-10:

| Artifact | Public location | Current content | Reuse decision |
|---|---|---|---|
| Privacy Policy | [hustlestats.io/privacy](https://hustlestats.io/privacy) | COPPA notice, parent and athlete data, automatic data, purposes, sharing, parental rights, security, 30-day deletion, cookies, vendors, transfers, changes, contact | Use as a topic checklist only. Product facts differ materially. |
| Terms of Service | [hustlestats.io/terms](https://hustlestats.io/terms) | adults-only account eligibility, service, accounts, privacy, data license, acceptable use, IP, disclaimers, liability, termination, changes, governing law, contact | Use as a clause inventory only. It does not describe desktop licensing or offline child play. |
| Acceptable Use Policy | none found | Six prohibitions are embedded in Terms section 7 | A standalone AUP is optional for a local single-player app, but repository/community conduct and license restrictions are separate needs. |
| Cookie Policy | none found | Privacy section 8 gives a general cookie statement | App itself should use no cookies. The purchase/download website needs an accurate site-specific disclosure. |
| Data Processing Addendum | none found | No public DPA located | Not needed for direct family sales unless vendor/customer relationships require it; revisit before schools or enterprise buyers. |
| Child Safety Policy | none found | COPPA topics appear in Privacy and Terms | This product needs a plain child-safety and parent-controls statement even if not a separate legal contract. |
| Refund and billing policy | none found | Terms do not state concrete refund or subscription rules | Required before paid launch. |
| Desktop EULA/license terms | none found | Hustle terms cover a hosted service | Required decision for paid binary and content rights. |
| Open-source notices | not part of Hustle legal pages | Unknown from public legal routes | App and companion need license and third-party notice inventories. |

### HustleStats issues that must not be inherited

- The public site's Privacy footer item currently links to `#` even though `/privacy` exists.
- Both legal pages render `Last Updated` from the current date at request time, so the date does not prove when policy text changed.
- The Privacy Policy names categories such as analytics, cookies, GCP, Resend, and payment processors that are not the proposed child-app data flow.
- The Privacy Policy says passwords are "encrypted" while the Terms simply require an account. Password storage terminology and actual implementation must be verified before reuse.
- The governing-law clause says "the state in which HUSTLE operates" rather than naming a jurisdiction.
- The Terms grant an aggregated/anonymized-statistics license. The typing app does not need this if no learning data leaves the device.
- Historical Hustle documents claim legal completeness, but those claims are not substitutes for current counsel or runtime evidence.

## Proposed data inventory

| Data | Source | Location | Leaves device | Purpose | Default retention | Deletion |
|---|---|---|---|---|---|---|
| Generated callsign or optional nickname | learner or parent | SQLite | no | distinguish profiles | profile lifetime | parent/local delete; UI warns not to use a real name |
| Companion summary | app-generated, opt-in | bounded local file | no | generic launch or progress state | profile lifetime or shorter | profile delete and companion uninstall; never include nickname or prompt text |
| Research screening and participant linkage | approved guardian/facilitator | protected research store, never Twenty or product SQLite | no product sync | approved study only | protocol-specific | research custodian deletes primary and backup copies on schedule |
| Coded study events, notes, probes, and consent references | approved study process | protected research store, never Git, Beads, CRM, support, or telemetry | no product sync | approved study questions only | protocol-specific | research custodian plus backup-deletion receipt |
| Avatar and accessibility choices | learner or parent | SQLite | no | presentation and access | profile lifetime | profile delete |
| Skill mastery and session summaries | gameplay | SQLite | no | adapt lessons and show progress | profile lifetime, summary policy configurable | profile delete/reset |
| Bounded attempt evidence | focused lesson input | SQLite | no | local adaptation | compact after proposed 90 days; final rule TBD | profile delete/reset |
| License ID and signed entitlement | parent purchase/recovery | separate local store | license request only, no child link | unlock paid content | license lifetime | local uninstall/delete; vendor records per policy |
| Parent email | external merchant/license service | vendor and controlled service | yes | receipt, recovery, support | vendor/legal schedule | parent request and vendor process |
| Update request | app | release endpoint | yes, includes ordinary network metadata | retrieve signed update metadata | server-log policy TBD | site/operator process |
| Voluntary support bundle | parent | previewed export | only by explicit parent action | diagnose issue | support schedule TBD | support deletion process |
| Stay-in-touch email and optional parent display name | parent-facing site | parent intake API and Twenty CRM | yes, parent service only | selected newsletter or research-recruitment-interest purpose | approved parent-contact schedule | unsubscribe, suppression, deletion-request workflow |
| Consent event | parent verification or withdrawal | append-only product consent ledger | yes, product service only | prove purpose, policy version, source, verification, and withdrawal | legal schedule TBD | correction or deletion process subject to required suppression evidence |
| Campaign context | disclosed page and request metadata | Twenty and consent ledger | optional | understand source of parent interest | shortest approved marketing period | parent request or retention expiry |
| Email delivery state | mail provider and product adapter | bounded delivery/outbox records | yes | verify, retry, unsubscribe, and diagnose delivery | short operational schedule TBD | expiry and provider deletion process |

The product must verify this table against the release candidate. If code behavior differs, the table and policies must change before release.

## Control registry

| ID | Control | Verification |
|---|---|---|
| CTRL-101 | No network-capable dependency may be added to the child gameplay path without architecture and privacy review. | lockfile review, static scan, runtime observation |
| CTRL-102 | Input capture exists only in the focused lesson surface and cannot register a global keyboard hook. | code review and system test |
| CTRL-103 | Logs exclude nicknames, prompt text, raw keystrokes, emails, license tokens, and file contents. | redaction tests and support-bundle inspection |
| CTRL-104 | Parent can export, reset, and delete local profile data without contacting Intent Solutions. | acceptance and recovery tests |
| CTRL-105 | Child mode contains no purchase, advertisement, social, or external-link surface. | route and screenshot inventory |
| CTRL-106 | Entitlement never contains child data and verifies offline with an embedded public key. | schema and cryptographic tests |
| CTRL-107 | Updates are signed, versioned, reversible, and independent of learner records. | release and downgrade tests |
| CTRL-108 | Third-party services have a purpose, data-category, location, retention, deletion, security, and contract entry before use. | vendor register review |
| CTRL-109 | Paid launch is blocked until price, taxes, merchant role, refund, recovery, device, support, and chargeback rules are published. | launch checklist |
| CTRL-110 | Public legal pages use fixed version dates and retain a reviewable change history. | policy repository and release review |
| CTRL-111 | Minor research requires a versioned ethics and safeguarding protocol, guardian consent, child assent and continuing dissent, compensation independent of completion, minimal recording, participant IDs, deletion dates, and no public raw media. | qualified review, study protocol, and evidence audit |
| CTRL-112 | Content and art have source, license, creator, modification, and distribution evidence. | provenance manifest |
| CTRL-113 | Parent-contact purposes use separate unchecked-by-default choices, signed expiring verification, unsubscribe, and suppression. | route, ledger, CRM, and email E2E audit |
| CTRL-114 | Parent API and CRM schemas reject child identity, profile, prompt, keystroke, lesson, mastery, and session fields. | schema contract and planted-field negative test |
| CTRL-115 | CRM and mail credentials remain server-side and operator access uses unique authorized accounts. | bundle scan, deployment review, access review |
| CTRL-116 | Parent relationship records and consent events reconcile after duplicate, timeout, provider outage, retry, unsubscribe, and deletion paths. | deterministic integration and production-canary evidence |
| CTRL-117 | `team-server` and the Buzz production host hold no product parent database or public product API. | deployment inventory and network review |
| CTRL-118 | Research-recruitment interest authorizes contact only. It cannot create a participant, prove guardianship, or authorize child-data collection. | negative service and data-model tests |
| CTRL-119 | A separate research trust zone records controller, custodian, exact fields, linkage, encryption, access, retention, backup deletion, export, incident response, and aggregate release. | approved research data-management plan and deletion drill |
| CTRL-120 | Profile deletion covers the primary database, WAL or journal, app-owned backups, summaries, caches, logs, and temporary files. Parent-created exports are separate copies under parent control. | complete deletion inventory and filesystem evidence |

## Required public documents before launch

| Document | Free offline release | Paid release | School/organization sales |
|---|---:|---:|---:|
| Product-specific Privacy Policy | required | required | required |
| Terms of Use or EULA | required | required | required |
| Child Safety and Parent Controls statement | required | required | required |
| Data inventory and deletion guide | required | required | required |
| Refund and billing policy | not applicable | required | required |
| License recovery and device policy | not applicable | required | required |
| Cookie/site tracking notice | if site behavior requires | if site behavior requires | if site behavior requires |
| Open-source notices and asset credits | required | required | required |
| Security and vulnerability reporting policy | required | required | required |
| DPA and school privacy terms | not planned | not planned | likely required after legal review |

## Legal review questions

1. Which entity is the operator and seller, and what physical and legal contact information must appear?
2. Which US state governs the terms, and which consumer-law rights cannot be waived?
3. Does update checking or license recovery make the product an online service directed to children for the relevant rule analysis?
4. Is the parent-only external checkout and local learner model sufficient for the proposed US launch, and what consent or notice is still required?
5. What changes under the 2025 COPPA amendments apply by the planned release date?
6. What state child-privacy, automatic-renewal, sales-tax, accessibility, and consumer-protection obligations apply?
7. Is a one-time license perpetual for the purchased version, for all updates, or for a stated update window?
8. What refund rights apply to downloaded digital content, and how does a refund revoke or not revoke an offline entitlement?
9. Which product names and comparison language are cleared? "Mavis Beacon" should be treated as historical market context, not a product identity.
10. What licenses govern source code, curriculum, art, audio, fonts, third-party packages, and paid content?

## Child-safety rules

- No social graph, chat, public identity, direct messaging, or external user content.
- No loot boxes, random paid rewards, urgency countdowns, streak loss, variable-ratio purchase loops, or advertisements.
- No diagnosis, intelligence ranking, or claims that measured typing performance predicts school ability.
- No prompt asks a child to type personal facts.
- No voice, photo, camera, location, contact-list, clipboard, or global input permission.
- Parent mode never exposes sibling rankings by default.
- Breaks are encouraged and never reduce access or progress.
- Support interaction is parent-facing.

## Review state

No qualified legal, privacy, child-development, accessibility, or learning review is recorded. No production data flow exists. The proposed controls reduce foreseeable exposure but do not authorize a compliance claim.
