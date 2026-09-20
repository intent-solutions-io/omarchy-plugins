---
blueprint:
  documentId: KTA-TEST-001
  documentType: test-plan
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
  sourceRefs: [KTA-PRD-001, KTA-ADR-001, KTA-ARCH-001, KTA-UX-001, KTA-PRIV-001, KTA-AC-001, SR-103, SR-106, SR-110, SR-111, SR-113, SR-114]
  assumptions: [A-101, A-105]
  unknowns: [U-102, U-103, U-107, U-108]
  relatedArtifacts: [KTA-PLAY-001, KTA-RISK-001, KTA-OPS-001, KTA-AUDT-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure test plan

> This is the required testing environment design, not a test report. There is no app repository or runnable candidate yet. Framework versions and exact commands must be recorded by the scaffold spike.

## Test strategy

The test system must prove four different things:

1. The learning and game rules are correct, deterministic, explainable, and resistant to edge cases.
2. The rendered experience is responsive, accessible, readable, and enjoyable on real hardware.
3. Local data, licensing, installation, updating, and rollback fail safely.
4. The companion follows Omarchy plugin lifecycle and marketplace expectations without expanding the app's trust boundary.

No single coverage percentage proves these outcomes. Coverage is a floor for test adequacy, mutation checks whether assertions detect behavior changes, property tests explore state space, system tests exercise integration, and child playtests evaluate comprehension and motivation.

## Proposed reproducible developer environment

| ID | Surface | Proposed mechanism | Evidence required |
|---|---|---|---|
| ENV-101 | Toolchain | pinned Node LTS, pnpm via Corepack, pinned Rust stable/toolchain file, exact Tauri CLI and lockfiles | version command log and lockfile checksum |
| ENV-102 | Linux build | container or devcontainer for compilers and static tests plus native Arch/Omarchy host for webview tests | image digest and package manifest |
| ENV-103 | Fast web preview | Vite development server with mocked narrow native ports | deterministic fixture and browser URL |
| ENV-104 | Native app | Tauri development and production bundles on named Arch/WebKitGTK versions | binary checksum and package query |
| ENV-105 | Browser matrix | Playwright Chromium, Firefox, and WebKit for portable frontend behavior | pinned Playwright browsers |
| ENV-106 | Desktop E2E | Tauri WebDriver/WebdriverIO on Linux, plus direct process and filesystem observation | session log, screenshot, process/network trace |
| ENV-107 | Omarchy system rig | clean snapshot of minimum and current Omarchy with Buzz and plugin validator | VM/image identity and reset receipt |
| ENV-108 | Hardware matrix | minimum integrated GPU device, primary developer device, high-DPI and multi-monitor device, US and non-US keyboard fixture | hardware and display inventory |

A container cannot prove WebKitGTK, Wayland, audio, global focus, Hyprland, QML, or real keyboard behavior. Those tests must execute on the controlled native rig.

## Quality layers

### Layer 0: Policy and change classification

- Validate generated files, Blueprint metadata, lockfile policy, licenses, secrets, and prohibited paths.
- Classify changed paths into docs, content, frontend, native, plugin, infrastructure, or release.
- Fail closed if a path is unclassified.
- Require exact revision identity before candidate evidence begins.
- Use CODEOWNERS or equivalent review routing for curriculum, privacy, entitlement, release, and signing changes.

### Layer 1: Static analysis

- TypeScript strict typecheck with no unexplained suppressions.
- ESLint and formatting checks.
- Rust formatting, Clippy with warnings treated according to repository policy, unsafe-code inventory, and dependency policy.
- QML lint for the companion.
- JSON Schema validation for content, summary, entitlement, configuration, and evidence records.
- Markdown, link, spelling terminology, forbidden-mark, and consistency checks.
- License, secret, dependency, SBOM, and code scanning.

### Layer 2: Unit tests

- Session state transitions, scoring, coaching, timing adapters, and mastery updates.
- Curriculum eligibility, prerequisite resolution, free/paid boundaries, and reading-level adapters.
- Keyboard normalization across `key`, `code`, Shift, Caps Lock, repeat, composition, dead keys, and layout fixtures.
- Rust storage commands, path checks, entitlement parsing, signature verification, updater policy, and redaction.
- Companion `Model.js` parsing, app presence states, summary bounds, and launch arguments.

### Layer 3: Property, model, and fuzz tests

- Generate learner histories and prove mastery values stay finite and bounded.
- Prove lesson selection terminates and always chooses eligible content or an explicit stop state.
- Prove no paid prerequisite blocks the free completion graph.
- Prove presentation choices do not change curriculum or score.
- Fuzz entitlement, summary, export, migration, and content parsers.
- Model database transactions under interruption and concurrent app starts.
- Mutate high-value rule packages and require a reviewed mutation threshold after baseline measurement.

### Layer 4: Contract and component tests

- React components with semantic queries and user-level events.
- Phaser scenes through a deterministic headless or adapter harness where possible.
- IPC request/response compatibility between frontend and Rust.
- SQLite migrations from every supported schema fixture.
- Summary schema compatibility between current app and supported companion versions.
- Entitlement key rotation and old-key policy.
- Visual component states for loading, empty, error, recovery, free, paid, reduced motion, large type, and narrow display.

### Layer 5: Browser E2E

- New profile to free-world completion using deterministic fixtures.
- Parent dashboard, settings, export, reset, and delete.
- Free and paid route inventory.
- Keyboard-only navigation and focus recovery.
- Automated accessibility scans with `@axe-core/playwright`, plus explicit acknowledgement that manual testing remains required.
- Visual snapshots at supported viewport and scale fixtures.
- Synthetic network block proving the preview works offline.

### Layer 6: Native integration and desktop E2E

- Real Tauri bundle, WebKitGTK, filesystem, SQLite, audio, process, focus, and updater adapters.
- Real key events where automation supports them, supplemented by a hardware protocol.
- App start, close, forced termination, restart, two-instance, full-disk, read-only, corrupt-state, and update-interruption flows.
- Network capture around gameplay, update check, license import/recovery, and support export.
- AppImage or chosen package install, checksum, signature, desktop entry, icon, permissions, and uninstall.

### Layer 7: Omarchy companion system tests

- Current `omarchy plugin validate` behavior on the exact companion revision.
- Template denominator gates, QML lint, coverage, race repetition, mutation, and audit harness.
- Buzz install, enable, render, click, launch, hide, disable, remove, reinstall, shell restart, and app-absent states.
- Process, network, timer, file watcher, memory, and shell-log observation.
- Theme, scale, bar placement, multi-monitor, and keyboard navigation matrix.

### Layer 8: Performance and endurance

- End-to-end key-to-visible-response latency with p50, p95, and p99.
- Frame-time distribution during the most active scene.
- Cold/warm startup, database load, save, export, and delete timing.
- Memory high-water mark and 60-minute soak.
- 1,000 open/play/close cycles in automation where practical.
- Idle CPU, timer, disk write, and network activity.
- Large but allowed profile/history fixture and compaction behavior.

### Layer 9: Security, privacy, and supply chain

- Capability and permission review, CSP, unrestricted command/path search, dependency vulnerabilities, secrets, license compatibility, and asset provenance.
- Runtime network and process observation.
- Log and support-bundle redaction tests.
- Signed update, wrong key, altered artifact, replay, downgrade, and rollback tests.
- SBOM, checksums, source revision, build provenance, and artifact attestation when available.
- Privacy-policy comparison against observed data flows.

### Layer 10: Acceptance and human evaluation

- Child usability and motivation study.
- Parent comprehension, purchase, recovery, export, and deletion study.
- Learning-specialist curriculum review and pre/post probe methodology.
- Accessibility review using keyboard, screen reader where applicable, reduced motion, larger text, contrast, sound-off, and motor-access scenarios.
- Creative and rights review for every shipped asset.

## Test registry

| ID | Test family | Primary trace | Evidence |
|---|---|---|---|
| TEST-101 | process isolation and crash containment | REQ-101; AC-101; RISK-102 | process log and shell health |
| TEST-102 | minimum Omarchy install and play | REQ-102; AC-102; RISK-101 | clean-rig transcript and capture |
| TEST-103 | companion summary and launch | REQ-103; AC-103; RISK-103 | Buzz log and schema fixtures |
| TEST-104 | app without plugin | REQ-104; AC-104 | desktop E2E |
| TEST-105 | app-absent companion and command injection | REQ-105; AC-105 | negative fixtures and process trace |
| TEST-106 | minimal local profile and no-account route | REQ-106; AC-106; RISK-104 | route inventory and DB inspection |
| TEST-107 | multi-profile isolation | REQ-107; AC-107 | property and storage tests |
| TEST-108 | character/curriculum differential | REQ-108; AC-108 | generated state diff |
| TEST-109 | adult-gate route boundary | REQ-109; AC-109; RISK-105 | route graph and manual review |
| TEST-110 | export/reset/delete isolation | REQ-110; AC-110; RISK-106 | before/after DB and file hashes |
| TEST-111 | content ID, graph, and provenance validation | REQ-111; AC-111; RISK-107 | validator report |
| TEST-112 | lesson schema completeness | REQ-112; AC-112 | schema report |
| TEST-113 | accuracy-first mastery cases | REQ-113; AC-113; RISK-108 | golden and generated cases |
| TEST-114 | keyboard-layout semantics | REQ-114; AC-114; RISK-109 | layout matrix |
| TEST-115 | input edge policy | REQ-115; AC-115 | browser and native event logs |
| TEST-116 | free-world graph and completion | REQ-116; AC-116; RISK-110 | graph proof and seeded replay |
| TEST-117 | advanced prerequisites | REQ-117; AC-117 | eligibility cases |
| TEST-118 | adaptive explanation | REQ-118; AC-118 | golden histories and parent review |
| TEST-119 | selector termination and recovery | REQ-119; AC-119 | property test distributions |
| TEST-120 | difficulty parameter boundaries | REQ-124; AC-122 | differential simulations |
| TEST-121 | asset/content rights chain | REQ-125; AC-123; RISK-111 | provenance manifest audit |
| TEST-122 | permanent offline free access | REQ-126; AC-124 | clock and network fixtures |
| TEST-123 | child commerce exclusion | REQ-127; AC-125; RISK-105 | screenshot/route inventory |
| TEST-124 | entitlement cryptographic matrix | REQ-128; AC-126; RISK-112 | unit, fuzz, and integration logs |
| TEST-125 | paid offline continuity | REQ-129; AC-127 | service-outage E2E |
| TEST-126 | learning-data network isolation | REQ-131; AC-129; RISK-104 | packet/process observation |
| TEST-127 | excluded dependency/service scan | REQ-132; AC-130 | static and runtime report |
| TEST-128 | full keyboard navigation | REQ-134; AC-132; RISK-113 | manual and automated record |
| TEST-129 | accessibility configuration | REQ-135; AC-133 | matrix and captures |
| TEST-130 | flash, motion, and timing safety | REQ-136; AC-134 | automated analysis and human review |
| TEST-131 | storage round-trip and atomicity | REQ-137; AC-135; RISK-106 | DB and filesystem receipts |
| TEST-132 | persistence failure matrix | REQ-138; AC-136 | preserved fixtures and logs |
| TEST-133 | release identity and signature | REQ-139; AC-137; RISK-114 | provenance packet |
| TEST-134 | update-request minimization | REQ-140; AC-138 | client/server capture |
| TEST-135 | update rollback and downgrade | REQ-141; AC-139; RISK-115 | installed-version and data hashes |
| TEST-136 | repository governance | REQ-142; AC-140; RISK-116 | repo-dress and consistency reports |
| TEST-137 | parent-intake schema and prohibited-field injection | REQ-143; AC-141 | contract report, request/DB/CRM diff |
| TEST-138 | consent-purpose independence model | REQ-144; AC-142 | generated transition matrix |
| TEST-139 | email verification, replay, unsubscribe, bounce, complaint, and suppression | REQ-145; AC-143 | integration and provider-sandbox receipts |
| TEST-140 | Twenty idempotency, outage, retry, and reconciliation | REQ-146; AC-144 | API fixtures, ledger/CRM reconciliation |
| TEST-141 | offline child and free-world no-login journey | REQ-147; AC-145 | fresh-install native E2E and network capture |
| TEST-142 | parent purchase/recovery and offline entitlement | REQ-148; AC-146 | merchant sandbox, token fixtures, outage E2E |
| TEST-143 | credential and operator-access isolation | REQ-149; AC-147 | source/artifact/log scan and access review |
| TEST-144 | shared-VPS load, resource-limit, health, backup, restore, and rollback | REQ-150; AC-148 | staged load results and dated production rehearsal |
| TEST-145 | static distribution and total-backend-outage play | REQ-151; AC-149 | clean install with blocked network and verified artifacts |

## Change-scoped CI matrix

| Lane | Trigger | Required checks | Typical target |
|---|---|---|---|
| docs | Markdown and documentation config only | format, links, Blueprint consistency, secrets, executable-snippet check | under 3 minutes |
| content | curriculum, story, locale, provenance | docs plus schema, graph, rights, reading level, unit/property, golden simulations | under 10 minutes |
| frontend | React, scene adapters, styles | static, unit/component, browser E2E, axe, visual, performance smoke | under 15 minutes |
| native | Rust, migrations, Tauri config | static, Rust tests, migration matrix, integration, package smoke, security | under 20 minutes |
| plugin | companion QML/JS/manifest | template gates, mutation, audit, Buzz smoke where runner supports | under 15 minutes plus rig queue |
| release | tag or manual signed candidate | every applicable lane plus clean Omarchy system, install/update/rollback, SBOM, signing, attestation, approvals | no time shortcut |

Ambiguous paths trigger the broader lane. Documentation changes that alter commands, manifests, test expectations, legal policies, or release evidence may trigger more than the docs lane.

## Coverage and mutation policy

Start by measuring meaningful baselines rather than copying percentages from the widget template. Proposed release floors after the slice:

- Domain and curriculum: 95 percent statements/functions/lines, 90 percent branches, critical mutation score at least 90 percent.
- Rust security and persistence modules: 90 percent where coverage tooling is reliable, with all threat cases explicitly tested.
- UI components: risk-based coverage plus route and state inventory, not a global vanity target.
- Companion model: inherit the template's 95/95/90/95 floors and mutation gate unless the current template changes.

Any exclusion needs path, rationale, owner, expiry, and compensating test. Generated files and unreachable defensive platform branches may be excluded only after review.

## Entry, suspension, and exit

Entry requires approved requirement versions, candidate revision, content version, clean environment identity, synthetic data, and no unreviewed rights issue. Suspend candidate testing for data loss, shell crash, focus capture, unexpected network/process behavior, invalid signature acceptance, disputed child data flow, or candidate revision change.

Release exit requires all P0 acceptance criteria with evidence, no unresolved critical/high security finding, no disputed asset, current policy review, child and parent pilot disposition, successful install/update/rollback, and owner approval tied to the exact artifact. Skipped tests do not pass.
