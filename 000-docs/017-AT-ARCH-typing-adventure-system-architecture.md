---
blueprint:
  documentId: KTA-ARCH-001
  documentType: architecture-description
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
  sourceRefs: [KTA-PRD-001, KTA-ADR-001, SR-103, SR-104, SR-105, SR-106, SR-113, SR-115, SR-116]
  assumptions: [A-101, A-105]
  unknowns: [U-101, U-104, U-107, U-108]
  relatedArtifacts: [KTA-UX-001, KTA-PRIV-001, KTA-AC-001, KTA-TEST-001, KTA-RISK-001, KTA-OPS-001, KTA-AUDT-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure system architecture

> Proposed target architecture. Paths, package names, versions, commands, services, and performance results do not exist until the application repository is scaffolded and verified.

## System context

```text
                           parent only
             +------------------+-------------------+
             | stay-in-touch / external checkout   |
             | verification / license recovery      |
             +-----------+--------------------------+
                         | server-side only
             +-----------v--------------------------+
             | parent service, consent ledger,      |
             | Twenty adapter, mail adapter          |
             +-----------+--------------------------+
                         | signed entitlement only
+----------------+      +-------v-------------------------+
| Omarchy bar    | open | standalone typing app process  |
| companion      +----->| Tauri host + web frontend      |
| QML plugin     |<-----+ local summary contract         |
+----------------+      +-------+------------+------------+
                                |            |
                           transactions    content load
                                |            |
                       +--------v---+   +----v-------------+
                       | local SQLite|   | bundled curriculum|
                       | and backups |   | and owned assets  |
                       +------------+   +------------------+

No child gameplay or profile data crosses the network boundary.
```

The desktop app is distributed, not hosted as a continuously running game service. Static signed artifacts, checksums, and updater metadata may use GitHub Releases or an approved static origin. Only parent relationship, consent, checkout, recovery, and entitlement issuance need online runtime services.

## Repository strategy

The application should use its own public repository because it has a different runtime, release cadence, build chain, threat model, artifact set, and commercial entitlement boundary from an Omarchy plugin. The companion plugin should use its own small public repository derived from `omarchy-widget-template`. The umbrella repository links both and owns portfolio-level documentation.

Proposed repositories:

```text
typing-adventure-app/             # final name pending
├── apps/
│   ├── desktop/                  # React shell and Tauri host
│   └── web-preview/              # development and playtest-only preview
├── packages/
│   ├── domain/                   # sessions, mastery, scoring, deterministic state
│   ├── curriculum/               # schemas, graph validation, content loader
│   ├── input/                    # keyboard normalization and focus policy
│   ├── game-scenes/              # Phaser adapters and scenes
│   ├── ui/                       # accessible shared UI and design tokens
│   └── test-fixtures/            # synthetic profiles, clocks, seeds, entitlement fixtures
├── content/
│   ├── curriculum/               # lessons and skill graph
│   ├── story/                    # missions and dialog
│   ├── locale/                   # approved strings
│   └── provenance/               # rights and source records
├── src-tauri/
│   ├── src/                      # commands, storage, entitlement, updater adapters
│   ├── migrations/               # SQLite migrations
│   ├── capabilities/             # least-privilege Tauri permissions
│   └── tauri.conf.json
├── tests/
│   ├── contract/                 # schemas and IPC contracts
│   ├── integration/              # storage, migrations, entitlement
│   ├── e2e-web/                  # Playwright fast path
│   ├── e2e-desktop/              # WebDriver real app
│   ├── system-omarchy/           # clean VM install, update, rollback
│   ├── performance/              # input and frame budgets
│   └── security/                 # network, permissions, supply chain
├── tools/                        # validators and evidence packager
├── 000-docs/                     # product, runbooks, decisions, releases
└── .github/workflows/            # scoped CI and release candidates

typing-adventure-omarchy/         # final name pending
├── BarWidget.qml
├── Panel.qml
├── Model.js
├── manifest.json
├── tests/
├── e2e/
└── 000-docs/
```

## Component registry

| ID | Component | Responsibility | Prohibited responsibility |
|---|---|---|---|
| CMP-101 | App shell | Window, navigation, parent-mode boundary, accessibility settings | Curriculum decisions or raw SQL |
| CMP-102 | Game scene adapter | Render scenes, audio, animation, semantic input actions | Mastery truth or entitlement decisions |
| CMP-103 | Input normalizer | Convert `key`, `code`, modifiers, repeat, composition, and focus into explicit events | Guess unsupported layouts silently |
| CMP-104 | Session engine | Deterministic prompt, response, coaching, score, and session transitions | DOM, clock, filesystem, network |
| CMP-105 | Mastery engine | Update explainable per-skill estimates and select eligible practice | Hide thresholds or use remote models |
| CMP-106 | Curriculum registry | Validate prerequisites, entitlements, prompts, content references, and versions | Execute content as code |
| CMP-107 | Profile service | Create, export, reset, and delete local learner records | Collect online identifiers from children |
| CMP-108 | Storage adapter | Own SQLite transactions, migrations, backup, recovery, and file permissions | Send telemetry or accept arbitrary paths |
| CMP-109 | Entitlement verifier | Verify signed license artifacts and expose edition capabilities | Process cards or inspect learner data |
| CMP-110 | Update adapter | Check signed metadata, download with parent/neutral consent, verify, stage, and rollback | Auto-run unsigned packages |
| CMP-111 | Local summary contract | Produce a minimal, versioned non-sensitive summary for the companion | Expose per-key errors, names, or session logs by default |
| CMP-112 | Companion plugin | Launch/resume, show daily completion state, open help | Own the learning game, checkout, or updater |
| CMP-113 | Parent intake API | Validate, rate limit, deduplicate, and record parent-purpose requests | Accept child data, expose vendor credentials, or act as a game API |
| CMP-114 | Consent ledger | Retain append-only purpose, policy, source, verification, unsubscribe, deletion, and reconciliation events | Store learner profiles, game events, or payment card data |
| CMP-115 | Twenty adapter | Upsert approved parent relationship fields through a supported server-side API | Write directly to Twenty's internal database or send learning data |
| CMP-116 | Mail adapter | Send verification, confirmation, unsubscribe, recovery, and owner digest messages | Enroll an unverified address or include child progress |

## Data model

The exact schema is deferred, but normative entities are known:

| Entity | Key fields | Sensitivity | Retention |
|---|---|---|---|
| LearnerProfile | local UUID, nickname/callsign, avatar settings, accessibility settings | child-related local data | until parent/local user deletes |
| SkillDefinition | skill ID, prerequisites, key semantics, mastery rules | public product content | version lifetime |
| LessonDefinition | lesson ID, skill links, prompts, story links, entitlement | public product content | version lifetime |
| Session | profile ID, content version, timestamps, seed, outcome summary | child-related local data | configurable local history; default proposed 12 months |
| AttemptEvent | session ID, target, normalized input class, correctness, latency bucket | sensitive learning data | shortest period needed for local adaptation; raw events should be compacted |
| MasteryState | profile ID, skill ID, estimate, evidence count, last practiced | child-related local data | until profile deletion |
| Entitlement | license ID, product, edition, issue/expiry/update fields, signature | parent commercial data, no child data | license lifetime plus documented recovery window |
| AppSettings | theme, audio, motion, layout, update preference | local device data | until reset/uninstall |

Online parent data is a separate model and database trust zone:

| Entity | Proposed fields | Prohibited fields | Authority and retention |
|---|---|---|---|
| ParentContact | CRM UUID, normalized parent email, optional parent display name, lifecycle stage, created/updated time | child name, child age, profile ID, prompt, keystroke, lesson, mastery, session | Twenty relationship record; approved parent-retention policy |
| ConsentEvent | event UUID, contact UUID, purpose, action, policy version, source, occurred time, verification method, disclosed campaign context | child or gameplay data, free-form research transcript | authoritative append-only permission ledger; legal schedule and suppression needs |
| EmailDelivery | message purpose, provider message ID, state, attempts, last error class, time | message body copies, child information | shortest operational period needed for retry and proof |
| Suppression | contact UUID or normalized-address key, purpose, unsubscribe/bounce/complaint reason, time | learner link | retained long enough to prevent unlawful or unwanted re-enrollment |
| LicenseAccount | parent identity reference, merchant customer reference, license IDs, recovery state | payment card, child profile, mastery | paid phase only; merchant and product policy |

The service must not write directly to Twenty's PostgreSQL database. It uses an authenticated server-side API adapter. Consent and suppression events are authoritative; Twenty is a verified-parent relationship projection; mail is a delivery projection. One transaction appends an event and its outbox work. At-least-once projectors use unique idempotency keys and durable cursors, support replay and rebuild, and converge within a measured bound. No send occurs unless the current authoritative consent projection permits it.

Raw key logs are dangerous. The system must store only learning events required by the active prompt and must never behave as a global keylogger. Input capture is active only in the focused lesson surface. Password-like free-form fields are not part of child play.

## Critical flows

### Child begins a session

1. App shell opens with no network requirement.
2. Child selects a local avatar profile.
3. Profile service loads mastery and accessibility settings through the storage adapter.
4. Curriculum registry selects only lessons whose prerequisites and entitlement are satisfied.
5. Session engine receives an explicit seed, content version, and monotonic clock adapter.
6. Game scene renders a semantic prompt and exposes the same prompt to accessible DOM or text structure.
7. A normative focus state machine accepts only eligible focused input, defers composition, excludes paste or automation from mastery without punishing the learner, and emits a typed domain event.
8. Session engine scores correctness before speed and returns coaching plus next state.
9. Immediate visible feedback updates in memory. A bounded persistence batch appends journal events and advances session and mastery projections in one SQLite transaction with an expected aggregate version.
10. On completion, the app verifies the projection against the journal sequence and shows a calm result.

### Parent unlocks paid content

1. Parent enters parent mode and chooses an external purchase or license-recovery link.
2. The browser checkout handles identity and payment outside the child flow.
3. License service or support returns a signed entitlement artifact to the parent.
4. App imports the artifact through a bounded parser.
5. Entitlement verifier validates signature, product, edition, and policy fields using an embedded public key.
6. Storage saves the entitlement separately from learner records.
7. Curriculum registry exposes additional owned content without contacting the service for each session.

### Companion launches app

1. Companion checks a fixed executable or desktop-entry contract without constructing arbitrary shell commands.
2. If absent, it presents documented installation help.
3. If present, it requests launch or focus with a fixed argument such as `--resume`.
4. It reads only a size-bounded, versioned summary written atomically by the app.
5. It stops all timers and file watchers when hidden or unloaded.

### Parent joins the early-access or Friday-letter list

1. A parent-facing page states the sender, specific purpose, data fields, policy version, and unsubscribe route.
2. Browser submits a size-bounded request to the parent intake API. No administrative or CRM token is present in client code.
3. API validates email and purpose, applies bot and rate controls, deduplicates idempotently, and transactionally appends a pending consent event plus outbox work.
4. Mail projection sends a purpose-specific possession-verification link with bounded expiry and replay protection. Unverified addresses are not projected into Twenty.
5. Verification appends an accepted event plus outbox work and activates only the selected contact purpose. Research-recruitment interest is not study consent.
6. Twenty projection creates or updates the approved verified-parent relationship fields.
7. An unsubscribe appends a withdrawn event and suppression state before mail or Twenty projection. The most restrictive authoritative state wins.
8. Projectors retry at least once, retain cursors, and support replay or rebuild after every crash boundary. Jeremy notification failure cannot lose the authoritative event.

### Authentication and authorization matrix

| Surface | Mechanism | Proves | Does not prove |
|---|---|---|---|
| Child game | no login; local profile | selected local play context | legal identity, age, guardianship |
| Local parent mode | documented adult navigation gate | deliberate transition out of ordinary child play | verified adult identity |
| Newsletter or research-recruitment interest | signed, expiring email verification link | control of email at verification time and chosen contact purpose | guardianship, study consent, child assent, enrollment, or entitlement ownership |
| Paid checkout and recovery | merchant or approved parent identity flow | merchant-defined parent/customer transaction or email control | any learner identity |
| Installed paid app | signed offline entitlement | approved license claims signed by issuer | parent's password or payment credential |
| Operators | unique estate and vendor accounts, least privilege, approved secret custody | authorized operator identity to the supported system | authority to bypass candidate or publication approval |

## Trust boundaries

| Boundary | Threat | Control |
|---|---|---|
| Web frontend to Rust IPC | compromised renderer calls powerful commands | narrow commands, typed payloads, allowlisted paths, Tauri capabilities, CSP |
| Content to engine | malformed or malicious content changes behavior | JSON Schema, size limits, unique IDs, graph validation, no expressions, signed bundled release |
| Keyboard to app | layout ambiguity, repeat, composition, focus leakage | event policy, layout fixture, focused capture only, pause on blur, no global listener |
| Local files to storage | corruption, symlink/path swap, unsafe migration | app-owned directory, descriptor-safe operations where available, transactions, backup, bounded parsing |
| Entitlement import | forged or oversized token | signature, size limit, schema, algorithm allowlist, key rotation policy |
| Updater to installed app | supply-chain replacement or downgrade | TLS plus signed metadata/artifact, exact target, version policy, staged rollback |
| App to child | pressure, shame, hidden collection | child-safety design rules, playtest review, no ads/social/purchases/telemetry |
| Plugin to shell | crash, focus capture, background work | thin QML, pure model, current plugin gates, lifecycle system tests |
| Browser to parent API | bots, oversized input, replay, client-secret theft | TLS, size and purpose allowlists, rate limit, idempotency, no client credential |
| Parent API to Twenty/mail | vendor outage, token compromise, duplicate or lost record | server-only credentials, least privilege, bounded retry, consent ledger, reconciliation, redacted logs |
| Parent database to learner database | accidental correlation or child-data ingestion | separate schemas, identifiers, services, tests, and prohibited-field gate; no join key |

## Deployment placement and current headroom

| Surface | Placement | Decision |
|---|---|---|
| Development and internal build work | `team-server` | allowed for development only; 2026-09-10 root disk was 97 percent used with 13 GB free, so it is explicitly rejected for new public production hosting |
| Game binary, content, checksums, SBOM, updater metadata | GitHub Releases or approved static distribution | recommended; no persistent game server required |
| Parent intake, consent ledger, Twenty/mail adapters | shared production VPS `intentsolutions` behind existing ingress | recommended only after readiness gate; snapshot showed 8 CPU, 23 GiB RAM with about 16 GiB available, 147 GB disk available, and 47 containers |
| Twenty CRM | existing shared production service | rebuildable projection for approved verified-parent relationship fields through a supported API; never contact-permission authority |
| Buzz production host | dedicated Buzz workload | rejected for this product |
| Omarchy test rig or Buzz-assisted validation | non-production test evidence | allowed for testing, never the parent-data production store |

The capacity snapshot is not a reservation or load test. Deployment requires declared CPU and memory limits, request and queue budgets, backup-size estimate, restore proof, health checks, alerting, secret rotation, a rollback rehearsal, and a trigger for moving the service if sustained use or blast radius becomes unacceptable.

## Build and dependency graph

```text
schemas and design tokens
        |
        +--> domain and curriculum packages
        |          |
        |          +--> input and game scene adapters
        |                       |
        |                       +--> React application
        |                                  |
        +--> Rust storage/entitlement ------+--> Tauri bundle
                                                   |
                                     signed artifact + updater metadata

local summary schema --> companion Model.js --> QML widget --> marketplace candidate
```

The domain, curriculum, and schema packages must build and test before the UI. The Tauri bundle depends on the compiled frontend. The companion depends only on the stable summary schema and app launch contract, never app source internals.

## Failure behavior

| Failure | Required behavior |
|---|---|
| Webview loses focus during prompt | Pause timing, reject subsequent keystrokes until explicit resume, persist safe checkpoint |
| Unsupported keyboard layout | Explain limitation and allow safe layout selection; never grade physical position as character without disclosure |
| Database migration fails | Preserve original database, log locally without learner text, open recovery flow, do not create a blank replacement silently |
| Disk becomes full | Keep last committed state, explain locally, allow export/delete, avoid repeated writes |
| Entitlement service unavailable | Existing valid local entitlement continues; free content always works |
| Entitlement import invalid | Reject without changing current access; provide parent-facing recovery instructions |
| Update signature invalid | Abort, retain current version, record local diagnostic, provide support link |
| New version cannot read current data | Block install before mutation or require verified migration and backup |
| Plugin cannot find app | Show install/help state without shell error or recurring process |
| Optional art/audio missing | Use approved fallback and fail release validation; do not crash learner session |

## Observability without surveillance

Production defaults to local operational logs with no prompt text, nickname, raw keystrokes, or learner identifiers. Logs rotate by size and age. A parent may export a redacted support bundle after previewing its contents. Remote crash reporting and analytics are excluded until a separate privacy decision, consent design, vendor contract, retention policy, and child-safety review are approved.

## Architecture fitness functions

- Domain tests run without React, Phaser, Tauri, filesystem, real clock, or network.
- A complete seeded session replays byte-identically for the same engine and content versions.
- No Tauri command accepts an unrestricted path or arbitrary shell command.
- Network tests observe no outbound gameplay traffic.
- Curriculum graph validation proves no paid prerequisite blocks the free-world completion path.
- Free and paid builds use one code path plus entitlement fixtures, not forked logic.
- Companion absence never affects app behavior, and app absence never destabilizes the shell.
- Documentation-only changes do not trigger full desktop system tests unless they modify executable examples, manifests, workflow logic, or release evidence.
