---
blueprint:
  documentId: KTA-OPS-001
  documentType: release-and-operational-readiness
  schemaVersion: 1.0.0
  templateVersion: 3.0.0
  status: draft
  owner: Jeremy Longshore
  authors: ["Intent Solutions / Codex"]
  reviewers: []
  approvers: []
  generatedAt: 2026-09-10
  updatedAt: 2026-09-10
  classification: internal-draft
  sourceRefs: [KTA-BRIEF-001, KTA-PRD-001, KTA-ADR-001, KTA-ARCH-001, KTA-PRIV-001, KTA-AC-001, KTA-TEST-001, KTA-PLAY-001, KTA-RISK-001, SR-103, SR-111, SR-114]
  assumptions: [A-101, A-103, A-104]
  unknowns: [U-101, U-104, U-105, U-107, U-108]
  relatedArtifacts: [KTA-AUDT-001, KTA-PROGRAM-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure release and operational readiness

> Commands below are target contracts unless the current baseline says otherwise. Local app and teaser repositories plus an unsigned AppImage exist. No configured public repository remote, demonstrated hosted CI, signing key, staging environment, public release, support rotation, working parent destination, or marketplace submission exists.

## Current local baseline

| Surface | Current implementation | Evidence boundary |
|---|---|---|
| Standalone | Electron, Vite, TypeScript, Canvas 2D, Web Audio at local commit `2d4c8fab59fa264691571c16e8d579520dbf82b1` | bounded two-minute prototype, not a finished curriculum or paid release |
| Package | 125,236,660-byte AppImage with SHA-256 `5e2b8deee88852961fc6c24ce32f997dfd0f881d32bd9384bc80b10a3c69320c` | unsigned development artifact with retained startup smoke, not production distribution |
| Teaser | QML and JavaScript Beacon Nine mission at local commit `97cdb6b60a90d9b656a6149c57a7fb63bc2fc2b5` | bounded local teaser, not a marketplace or acquisition funnel |
| Public continuation | `https://oma.intentsolutions.io/omaquest` | returned HTTP 404 during KTA-ASTRA-001 review |

The historical Tauri, React, Phaser, Rust, and SQLite architecture remains a proposed alternative and target decomposition, not current implementation. Electron is the baseline for the next stabilization slice. Any later rewrite requires measured benefit and an explicit replacement decision.

## Release surfaces

| Surface | Channel | Independent rollback | Approval |
|---|---|---:|---|
| Standalone app source | public Git repository | yes | merge review |
| Linux app artifact | GitHub Release or approved distribution | yes | fresh release approval tied to candidate SHA |
| Updater metadata | authenticated static endpoint or approved service | yes | fresh production approval |
| Paid entitlement service/checkout | parent-facing web property and vendor | yes | legal, privacy, business, and production approval |
| Omarchy companion source | separate public Git repository | yes | merge review |
| Omarchy marketplace listing | official submission process | yes through update/removal process | fresh submission approval |
| Portfolio page | `oma.intentsolutions.io` | yes | content review |
| Legal and safety pages | controlled public site with version history | yes | legal/privacy approval |
| Parent stay-in-touch and consent service | shared production VPS only after capacity/readiness gate | yes | privacy, platform, and production approval |
| Parent relationship records | Twenty CRM plus approved consent ledger | yes through export/reconciliation | privacy and operator access approval |

## Environment model

| Environment | Purpose | Data | External effects |
|---|---|---|---|
| Local preview | fast UI/game development | synthetic only | none |
| Local native | current Electron package, storage, audio, and input stabilization; optional Tauri comparison only if separately approved | synthetic only | blocked or fixture endpoints |
| CI | deterministic gates and builds | synthetic only | no release mutation on pull request |
| Omarchy rig | install, plugin, focus, performance, failure paths | synthetic profiles and test entitlements | isolated network capture |
| Closed pilot | approved family evaluation | local participant data under protocol | signed prerelease, parent support only |
| Production | public free/paid use | local learner data; parent commerce data in approved services | signed releases and documented endpoints |

`team-server` is a development and internal systems host, not a production alternative. The dedicated Buzz host is not general application capacity. The shared `intentsolutions` VPS is the proposed online-service target because it already owns customer-facing ingress and Twenty. A 2026-09-10 read-only snapshot showed current headroom, but deployment remains blocked on the service-specific limits, load, backup, restore, monitoring, and rollback gate.

## Work packages and gates

| ID | Work package | Inputs | Exit evidence | Depends on |
|---|---|---|---|---|
| TASK-101 | Decide name, entity, license, jurisdictions, and product owner roles | brief, legal screen | recorded decisions and approved labels | none |
| TASK-102 | Conduct parent discovery and child paper co-design | research protocol | de-identified findings and gate decision | TASK-101, privacy review |
| TASK-103 | Appoint learning/accessibility reviewers and draft skill graph | PRD and UX spec | reviewed curriculum v0 and test probes | TASK-101 |
| TASK-104 | Scaffold only the disposable gameplay and native-runtime proof environments | ADR and architecture | reproducible greyboxes, native benchmark, and bounded proof gates | TASK-101 |
| TASK-105 | Define the minimum deterministic domain fixtures needed by the proofs | curriculum v0 | unit/property/contract evidence for proof scope | TASK-103, TASK-104 |
| TASK-106 | Compare three gameplay greyboxes and run a separate native-runtime spike | domain and UX | blinded gameplay findings plus native input, focus, accessibility, and performance evidence | TASK-102, TASK-105 |
| TASK-107 | Decide whether to authorize a durable slice, then execute Stage B only after approval | signed proof evidence and owner decision | slice candidate, playtest report, and disposition | TASK-106 |
| TASK-108 | Implement storage, recovery, privacy controls, and support export | architecture and annex | migration/failure/network evidence | TASK-104, TASK-105 |
| TASK-109 | Produce free-world content and owned assets | approved slice and provenance process | content graph, rights manifest, creative review | TASK-107 |
| TASK-110 | Build companion from current widget template | stable local summary contract | template gates and Buzz evidence | TASK-108 |
| TASK-111 | Establish package, signing, SBOM, update, rollback, and clean rig | release design | signed candidate rehearsal | TASK-104, TASK-108 |
| TASK-112 | Run closed free-world pilot | signed prerelease and protocol | retention, learning, reliability, support evidence | TASK-109, TASK-111 |
| TASK-113 | Dress repos, freeze the free v1.0 candidate, and run its full applicable lane | complete free world, companion, release system | free candidate evidence packet | TASK-109, TASK-110, TASK-111, TASK-112 |
| TASK-114 | Publish free v1.0 only after exact-candidate approval | approved free packet | release URLs, marketplace receipt, rollback verification | TASK-113 |
| TASK-115 | Observe free release and research parent demand | v1.0 operations and parent cohort | retention, learning, support, reliability, and price evidence | TASK-114 |
| TASK-116 | Decide merchant, price, terms, refund, recovery, update promise, and entitlement | parent evidence and legal review | commerce ADR and approved public policies | TASK-101, TASK-115 |
| TASK-117 | Implement and test paid Family v1.1 features | approved commerce decision | entitlement, family-profile, outage, refund, and recovery evidence | TASK-116 |
| TASK-118 | Freeze and publish Family v1.1 only after a new exact-candidate approval | paid candidate evidence packet | paid release receipt and rollback verification | TASK-117 |

The executable task authority is Beads epic `bd_000-projects-v41u`. Its phase epics and dependency-linked children are cataloged in KTA-PROGRAM-001. This table remains the human release summary; it must not be used as a substitute for Beads state, dependency edges, annotations, or closure evidence.

Each executable repository must run the `audit-tests` diagnostic after scaffold, hand any P0/P1 gaps to `implement-tests`, review its staged changes, and pass a second audit before the applicable foundation or release gate. The app sequence is `bd_000-projects-v41u.4.8` through `.4.10`; the parent service uses `.3.7` and `.3.8` before `.3.6`; the companion uses `.8.6` and `.8.7` before `.8.4`.

## Proposed command contract

The scaffold should expose stable top-level commands regardless of underlying tools:

| Command | Contract |
|---|---|
| `pnpm dev` | start web preview with synthetic local adapters |
| `pnpm dev:desktop` | start native app in development mode |
| `pnpm check` | format, lint, type, schemas, links, policy, and secrets |
| `pnpm test:unit` | TypeScript and Rust unit tests |
| `pnpm test:property` | generated/model tests with reproducible seeds |
| `pnpm test:component` | UI and scene component tests |
| `pnpm test:e2e:web` | Playwright browser path |
| `pnpm test:e2e:desktop` | real Tauri desktop path |
| `pnpm test:content` | curriculum graph, reading level, and provenance |
| `pnpm test:security` | permissions, dependencies, network policy, redaction, and supply chain |
| `pnpm test:performance` | key latency, frame, startup, memory, and idle budgets |
| `pnpm test:release` | fail-closed aggregate for an exact clean revision |
| `pnpm build` | reproducible unsigned development artifact |
| `pnpm release:prepare` | produce checksums, SBOM, notes, evidence, and unsigned/signed handoff without publishing |
| `pnpm evidence:verify` | ensure every receipt belongs to candidate revision and environment |

No `publish` or production update command should be hidden inside the ordinary test command. External mutation must be an explicit, logged operation after fresh approval.

## Candidate evidence packet

Adapt the strongest Contributing Clanker pattern: prepare an immutable packet before asking for approval.

- exact source revision and clean-tree proof
- dependency lockfile and toolchain identities
- app/content/summary/entitlement schema versions
- test commands, environment identities, raw results, limitations, and skipped-test dispositions
- coverage and mutation reports
- child, parent, learning, accessibility, legal, creative, and security review records
- SBOM, dependency and license scans, asset provenance
- binary and package checksums, signatures, and attestations
- screenshots, video/cast, install, update, rollback, remove, and recovery evidence
- privacy network capture and policy-to-runtime comparison
- release notes, known issues, support and vulnerability routes
- rollback artifact and exercised rollback receipt

Changing the source, dependencies, content, signing inputs, updater configuration, or policies after packet generation invalidates affected evidence and requires regeneration.

## Release sequence

The release sequence runs once for free v1.0 and again for Family v1.1. The free release does not wait for production checkout, a live license service, or paid-only acceptance criteria. It does require production-grade privacy, accessibility, persistence, signing, updates, support, and rollback.

1. Freeze a clean candidate and record SHA.
2. Run applicable static, unit, property, component, integration, browser, desktop, Omarchy, privacy, security, performance, and endurance lanes.
3. Build artifacts in the controlled release environment.
4. Generate SBOM, provenance, checksums, and update metadata.
5. Sign artifacts and metadata without exposing private keys.
6. Install the exact artifacts on a reset minimum Omarchy rig.
7. Exercise new install, update from prior supported release, rollback, uninstall, and reinstall.
8. Verify data preservation and deletion paths.
9. Assemble and independently review the evidence packet.
10. Ask for fresh approval naming SHA, version, artifact hashes, release destinations, and known limitations.
11. Publish app artifact, then updater metadata, then site pages and companion listing according to the approved sequence.
12. Verify public hashes, downloads, policy links, install commands, marketplace state, and rollback availability.
13. Record release receipt and begin the observation window.

After free v1.0, collect the defined learning, repeat-use, reliability, support, and parent-demand evidence. Only then approve the paid commercial contract, implement production entitlement, and run a separate paid candidate lane. Later paid content packs use the same entitlement and release boundary without removing access a family already purchased.

## Rollback strategy

- Keep the prior signed artifact and metadata available.
- Back up the local database before any migration.
- Mark migrations as forward-only or backward-compatible explicitly.
- If the app fails but data is compatible, withdraw new updater metadata and republish the prior signed target.
- If data is not backward-readable, block the unsafe downgrade and ship a signed recovery build that restores a supported working state while preserving export and backup. A blocked downgrade or export alone is not successful rollback.
- The companion must tolerate app version mismatch by falling back to launch-only behavior.
- A marketplace listing issue must not prevent direct app use or data access.

## Operational signals

Because automatic child telemetry is excluded, operations rely on:

- public release and download health checks that carry no learner data
- signed updater endpoint availability
- checkout/license provider health for parent workflows
- consented parent support tickets
- parent-previewed redacted diagnostic bundles
- reproducible internal synthetic canaries
- voluntary, separately reviewed pilot surveys

Do not claim a crash-free rate until a lawful, accurate measurement method exists. Synthetic canary success is not user uptime.

## Incident levels

| Level | Definition | Initial action |
|---|---|---|
| P0 | child data disclosure, signature/update compromise, destructive data loss at scale, unsafe content | stop distribution/update, preserve evidence, invoke legal/security owner immediately |
| P1 | app cannot start for supported users, widespread progress corruption, child purchase boundary bypass | withdraw candidate, publish status, restore prior artifact |
| P2 | degraded lesson, accessibility regression, isolated migration/support issue | triage same business day, provide workaround and patch plan |
| P3 | cosmetic, documentation, or non-blocking content issue | normal issue workflow |

## Readiness checklist

### Ownership and policy

- [ ] Named product, engineering, curriculum, accessibility, privacy/legal, security, creative, release, and support owners
- [ ] Approved product name, app ID, repositories, license model, seller, jurisdictions, terms, privacy, child-safety, refund, and support documents
- [ ] No unsupported "COPPA compliant," learning-outcome, or security marketing claim

### Engineering and quality

- [ ] Reproducible local environment and CI with change-scoped lanes
- [ ] Minimum and current Omarchy rigs, hardware/layout matrix, and reset procedure
- [ ] All P0 acceptance evidence tied to exact revision
- [ ] Data migration, deletion, export, update, rollback, and app/plugin mismatch tested
- [ ] No unresolved critical/high security or rights issue

### Product evidence

- [ ] Child co-design, three-gameplay-proof disposition, native-spike disposition, and any separately authorized vertical-slice playtest disposition
- [ ] Learning reviewer accepts curriculum and measurement plan
- [ ] Parent understands progress, privacy, paid boundary, refund, and recovery
- [ ] Free world is complete and permanently usable offline

### Release and support

- [ ] Signing keys, backup, rotation, and revocation custody documented
- [ ] SBOM, checksums, signatures, provenance, and asset rights published as appropriate
- [ ] Support and vulnerability routes monitored
- [ ] Prior signed artifact and rollback procedure verified
- [ ] Fresh exact-candidate approval recorded before each external publish or marketplace mutation

## Current readiness verdict

Ready for a bounded engineering iteration on the existing Electron MVP. Not ready to release, accept payment, publish a marketplace teaser, or claim a complete learning product.

The immediate build contract is input and focus safety, untimed play, corrected contrast, explicit adult navigation, strict access schemas, atomic local writes, packaged native tests, and one finished first chapter. The natural field-manual palette remains the foundation, with darker functional text and controlled ember, teal, and gold signal accents. The free Omarchy teaser is feature-scope locked, but branding, contrast, working parent handoff, and full install-to-remove evidence block release-byte freeze. KTA-ASTRA-001 is the current audit authority for this checkpoint.
