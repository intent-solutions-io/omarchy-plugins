---
blueprint:
  documentId: KTA-AUDT-001
  documentType: appaudit-devops-playbook
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
  sourceRefs: [KTA-BRIEF-001, KTA-PRD-001, KTA-ADR-001, KTA-ARCH-001, KTA-UX-001, KTA-PRIV-001, KTA-AC-001, KTA-TEST-001, KTA-PLAY-001, KTA-RISK-001, KTA-OPS-001, SR-102, SR-103, SR-104, SR-105, SR-106, SR-107, SR-108, SR-109, SR-110, SR-111, SR-113, SR-114]
  assumptions: [A-101, A-102, A-103, A-104, A-105]
  unknowns: [U-101, U-102, U-103, U-104, U-105, U-106, U-107, U-108]
  relatedArtifacts: [KTA-BRIEF-001, KTA-PRD-001, KTA-ADR-001, KTA-ARCH-001, KTA-UX-001, KTA-PRIV-001, KTA-AC-001, KTA-TEST-001, KTA-PLAY-001, KTA-RISK-001, KTA-OPS-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy Kids Typing Adventure: Operator-Grade System Analysis

*Generated: 2026-09-10*

*Version: pre-build proposal on `docs/typing-adventure-blueprint`, based on umbrella commit `e875984`; no application commit exists*

---

## 1. This System in 5 Minutes

The proposed product is a child-centered typing adventure for Omarchy. It is intended to recover the durable value of classic typing tutors, structured skill introduction, visible keyboard and finger guidance, immediate correction, progressive practice, and parent-readable progress, while replacing the worksheet feeling with an original game in which typing directly controls meaningful actions. The working label in this document is not a public product name. `OmaType` is already used by an existing Omarchy marketplace entry, and Mavis Beacon is third-party historical market context, not a name or asset source.

This should not be built as one large Omarchy plugin. Omarchy plugins run QML and JavaScript within the long-lived shell context and are well suited to bounded widgets and overlays. A full learning game adds many scenes, audio, content, learner profiles, durable storage, accessibility state, paid entitlement, packaging, updating, rollback, and longer resource use. The recommended system has a standalone application process for the complete free and paid product and a separate free companion plugin for launch, resume, a daily completion cue, and marketplace discovery. The app works without the plugin. The plugin works safely when the app is absent.

The recommended technical direction is a Tauri 2 desktop shell, React and TypeScript for application UI, Phaser for bounded game scenes, pure TypeScript packages for curriculum and mastery rules, Rust-owned SQLite for local state, and a signed offline entitlement imported through a parent-only external purchase flow. This remains an option, not a selection. Three disposable gameplay proofs determine whether typing creates meaningful play, while a separate native-runtime spike tests WebKitGTK input latency, keyboard-layout behavior, Wayland focus, audio, graphics, packaging, and accessibility on actual Omarchy devices. Only a later decision may authorize a durable slice.

The safety and privacy thesis is local-first. A child does not create an online account. Gameplay and learning history stay on the device. The app does not include ads, chat, leaderboards, public profiles, third-party analytics, global key capture, automatic crash upload, or child-facing purchases. A parent can inspect, export, reset, and delete each local profile. Paid access is represented by a signed license artifact containing no learner data. Update and license services are separate adult or neutral infrastructure surfaces whose actual data handling must be documented.

The current system is a plan, not an app. There is no product repository, executable, curriculum, approved name, paid model, signed artifact, or child study. The available widget template is mature for the companion: its local test, race, mutation, audit, and vendored-gate lanes passed during this review at commit `19f1e64`. It is not an app template and is missing several production-repository capabilities. The largest risk is building polished content before proving that children find the typing loop enjoyable and that a qualified reviewer accepts the learning sequence. The correct next move is governed discovery, three disposable gameplay proofs, and a separate native-runtime spike. A durable slice requires a later evidence-backed decision. Paid Family work begins after evidence from the complete free release, not before it.

## 2. Executive Summary

### What It Does

The product teaches touch typing through short narrative missions. A lesson introduces one small skill, untimed practice establishes the motion, and a mission recombines the skill under bounded pressure. Accuracy controls progress before speed. Incorrect input receives specific coaching and no shame, public ranking, or permanent loss. A normal session targets a satisfying stop within 10 to 20 minutes. The free edition contains one complete world and a coherent beginner curriculum through lowercase and uppercase letters, space, Enter, Shift, numerals, and essential sentence punctuation, essential correction, basic local adaptation, accessibility, parent-readable progress, export, reset, and deletion. A proposed paid family edition adds multiple profiles, additional original worlds, deeper local adaptation, advanced punctuation and symbols, sustained fluency, code-like patterns, and an Omarchy shortcut academy.

The buyer and primary operator for commerce is the parent or guardian. The learner is the primary gameplay user. These are different surfaces with different safety rules. Child mode cannot reach pricing, checkout, legal changes, entitlement import, external links, or destructive profile controls. Parent mode can understand the data model, accessibility options, skill progress, purchase promise, refund, recovery, export, reset, and deletion. The system does not pretend that a simple arithmetic question or hidden button proves adult identity. The adult gate must be described honestly and reviewed against the actual risk.

The application architecture separates deterministic learning rules from presentation. Curriculum definitions, prompt selection, response classification, mastery, scoring, and session state live in pure packages with injected clock and random sources. React owns ordinary navigation and accessible parent screens. Phaser owns only scenes and presentation adapters. Rust owns native permissions, storage, entitlement verification, update policy, and safe file boundaries. This separation permits fast browser testing, deterministic replay, native integration testing, and a future platform change without rewriting learning truth.

The current health score is **24/100**. That low number describes pre-build readiness, not product quality. Strategic framing, architecture, acceptance, privacy posture, risk, tests, and release controls now have written drafts. Implementation, product evidence, ownership, legal approval, learning validation, infrastructure, release credentials, and operational history remain absent. There are zero confirmed production incidents because there is no production system, not because reliability is proven.

### Operational Status

| Environment | Status | Uptime Target | Release Cadence | Last Deploy |
|---|---|---|---|---|
| Production app | not created | not defined | not defined | never |
| Paid checkout/license | not created for this product | not defined | not defined | never |
| Closed pilot | not created | study-window availability only | milestone based | never |
| Staging/native rig | proposed | available during scheduled validation | per candidate | never |
| Local app development | not created | not applicable | continuous | never |
| Companion plugin | not created | dependent only on local shell/app | with compatible app contracts | never |
| Widget template | available at `19f1e64` | not a service | template releases | no tag observed in this audit |

### Technology Stack

| Category | Technology | Version | Purpose | State |
|---|---|---|---|---|
| Desktop shell | Tauri | 2.x, exact pin unknown | native process, IPC, packaging, update boundary | proposed |
| Native core | Rust | pinned stable, exact version unknown | storage, entitlement, updater, permissions | proposed |
| App UI | React and TypeScript | exact pins unknown | navigation, lessons, parent screens, accessible DOM | proposed |
| Game scenes | Phaser | exact pin unknown | bounded 2D scenes, input, audio, WebGL/Canvas | proposed |
| Build/dev | Vite and pnpm | exact pins unknown | preview, package graph, builds | proposed |
| Local data | SQLite | system/library version unknown | profiles, mastery, sessions, migrations | proposed |
| Browser E2E | Playwright | exact pin unknown | portable UI, accessibility, visual tests | proposed |
| Native E2E | Tauri WebDriver with WebdriverIO or direct driver | exact pin unknown | real application integration on Linux | proposed |
| Property tests | fast-check or reviewed equivalent | unknown | generated curriculum and mastery histories | proposed |
| Companion | QML, JavaScript, Quickshell | Omarchy baseline unknown | launch and bounded local summary | proposed |
| Plugin quality | widget-template gate lane and audit harness | template audit at `19f1e64`, audit harness 1.4.0 | plugin static, unit, mutation, audit, render preparation | verified only on template |
| Release security | checksums, signing, SBOM, GitHub attestation where available | unknown | candidate integrity and provenance | proposed |

Versions are intentionally unresolved because copying current latest versions into planning prose produces false precision. The scaffold spike must pin exact versions, record their support windows, and prove them together on the named Omarchy baseline.

## 3. Architecture

### Stack in Detail

| Layer | Technology | Why This | Cost and constraint |
|---|---|---|---|
| Process boundary | Tauri application | protects the shell from a long-running game and provides native packaging | adds Rust, WebKitGTK, native CI, and updater complexity |
| Ordinary UI | React semantic DOM | strong fit for profile, settings, progress, recovery, and accessible controls | canvas and DOM focus must be coordinated carefully |
| 2D game presentation | Phaser | established scene, audio, input, and rendering system without building an engine | accessibility representation must exist outside the canvas; Phaser must not own learning logic |
| Learning domain | pure TypeScript | same deterministic logic runs in unit tests, browser preview, and app | explicit adapters are required for every external effect |
| Native boundary | Rust commands with narrow Tauri capabilities | compile-time safety and a controlled filesystem/crypto/update surface | unsafe assumptions can still exist and need threat-driven tests |
| Persistence | SQLite transactions and migrations | suitable for multiple profiles, queries, exports, backups, and recovery | requires schema evolution discipline and native failure tests |
| Content | versioned JSON or equivalent data validated by schemas | editors and reviewers can inspect content without executable code | schema does not prove instructional quality or rights |
| Entitlement | signed local document | paid use survives outages and contains no child profile | private-key custody, recovery, refund, transfer, and revocation remain operations work |
| Integration | QML companion with minimal summary file | uses the proven Omarchy widget pattern while keeping failure domains separate | separate repo and compatibility contract |

Tauri is not accepted merely because it is lighter than Electron. The current official prerequisites list Arch packages including WebKitGTK 4.1 and other native libraries. Tauri's official testing overview supports a mock runtime and WebDriver-based E2E on Linux, but mock tests do not execute the native webview. The architecture therefore requires both a fast browser lane and a real Omarchy lane. A stack spike is failed if real input, focus, frame, packaging, or accessibility behavior does not meet the targets.

Phaser is selected provisionally over a custom canvas layer because it supplies mature scene and rendering foundations while retaining TypeScript. It is selected over Godot for the first slice because the product includes substantial non-game UI and benefits from a single testable web frontend. If the game scenes become the majority of complexity or the webview fails, Godot should be reconsidered before content expansion, not after a sunk-cost full build.

### System Diagram

```text
TRUST ZONE: CHILD AND LOCAL DEVICE

 +-------------------+       +--------------------------------------+
 | Omarchy companion | open  | standalone app                      |
 | QML + pure JS      +------>|                                      |
 |                    |       | +---------------+  +---------------+ |
 | reads summary only |<------+ | React UI      |  | Phaser scenes | |
 +-------------------+       | +-------+-------+  +-------+-------+ |
                              |         |                  |         |
                              |         +--------+---------+         |
                              |                  | domain events     |
                              |     +------------v--------------+    |
                              |     | session + mastery engines |    |
                              |     +------+---------------+----+    |
                              |            |               |         |
                              | +----------v---+   +-------v-------+ |
                              | | curriculum  |   | Tauri commands| |
                              | | and assets  |   | Rust boundary | |
                              | +--------------+   +---+--------+--+ |
                              +---------------------|--------|------+
                                                    |        |
                                              +-----v--+ +---v--------+
                                              | SQLite | | entitlement|
                                              | backup | | and updater|
                                              +--------+ +---+--------+
                                                               |
====================== NETWORK AND ADULT BOUNDARY ==============|====
                                                               |
                      +------------------+    +-----------------v--+
                      | parent checkout  |    | signed release and |
                      | and recovery     |    | update endpoint    |
                      +------------------+    +--------------------+

No learner profile, prompt history, mastery state, or raw key input is sent
across the boundary in the proposed first release.
```

### The Critical Path

The most important path is one focused keystroke becoming correct instructional feedback and durable progress.

1. The learner opens a local profile. The profile service reads settings and mastery in one bounded storage transaction. Failure point: a corrupt or future schema. Required response: preserve the original database, offer an explicit recovery state, and never silently replace progress with a new blank profile.
2. The curriculum registry resolves eligible lessons using the exact content version and entitlement capabilities. Failure point: a missing prerequisite or a paid node in the free path. Required response: release-time graph validation blocks the content; runtime uses an explicit safe state rather than inventing a lesson.
3. The session engine receives a deterministic seed and injected monotonic clock. It selects a prompt whose characters and reading level are legal for the active lesson. Failure point: prompt includes an untaught or unsupported character. Required response: schema and property tests block release.
4. React and the scene adapter render the same semantic prompt. The canvas may animate the world, but an accessible DOM representation owns instructions, status, and navigation. Failure point: canvas state diverges from semantic state. Required response: contract and differential tests fail.
5. The focused input normalizer receives a `keydown`, composition, or input event. It distinguishes the character generated from the physical key position, records active layout assumptions, handles repeat and modifier state, and rejects paste or synthetic mastery credit. Failure point: focus leaves the app, the webview maps a non-US layout differently, or system shortcuts intercept the event. Required response: pause timing, preserve the session, and require explicit resume.
6. The normalizer emits a small domain event. It does not send the raw event object, read global input, or record unrelated keys. Failure point: frontend compromise invokes a broad native command. Required response: Tauri capabilities and typed Rust validation deny the call.
7. The session engine compares the normalized response with the target, calculates correctness before speed, and emits coaching plus a next state. Failure point: a held key earns repeated credit or a timer creates negative/NaN metrics. Required response: pure property invariants keep values finite and credit bounded.
8. The scene adapter renders a response within the proposed 50 ms p95 target. Failure point: WebKitGTK frame delay or garbage collection. Required response: measured trace identifies the layer; cosmetic work is removed before learning logic is weakened.
9. The storage adapter records only the evidence needed for local adaptation. It uses a transaction and excludes nickname, prompt prose, raw global input, and secrets from logs. Failure point: disk full or process kill during commit. Required response: the previous transaction remains valid and recovery guidance appears.
10. At session end, the mastery engine updates explainable skill state and the app writes an atomic bounded summary for the companion. Failure point: a partial summary or incompatible companion. Required response: companion retains last-good or shows launch-only state.

### Dependency Graph and Build Order

```text
policy decisions and names
    |
    +--> curriculum model and content schema
    |        |
    |        +--> pure domain engine and fixtures
    |                 |
    |                 +--> React lesson UI
    |                 +--> Phaser scene adapters
    |                 +--> simulation and mastery tests
    |
    +--> local data and privacy model
    |        |
    |        +--> SQLite schema and Rust storage
    |        +--> export/delete/recovery
    |
    +--> commerce decision
             |
             +--> signed entitlement and parent flow

gameplay greyboxes + native spike --> owner decision --> durable vertical slice --> child/parent evidence
                                              |
                                              +--> free world and assets
                                              +--> app release pipeline
                                              +--> stable summary contract
                                                        |
                                                        +--> companion plugin
```

The app should not wait for paid commerce to build the free slice. Commerce should not be implemented until parent research, legal terms, seller/tax responsibility, price, recovery, and refund policy are decided. The companion should not begin until the app has a stable launch and summary contract. Creative production at scale should not begin until the slice passes child interest and learning gates.

### Availability and Failure Domains

The app's learning path depends only on installed code, bundled content, and local storage. Checkout can fail without affecting free or already entitled play. The updater can fail without affecting the installed version. The companion can fail without affecting the app. The marketplace can be unavailable without removing direct application access. This decomposition is a deliberate availability feature.

SQLite is the single local progress store and therefore the most important durability boundary. It needs transaction integrity, schema backups, migration fixtures, export, deletion, full-disk behavior, read-only behavior, and downgrade policy. A cloud backup would add a different and more serious privacy system; it is intentionally not part of the first release.

## 4. Design Decisions and Tradeoffs

### Decision Log

#### Application over plugin-only

- Chosen: standalone app plus companion plugin
- Over: plugin-only game
- Because: resource containment, packaging, persistence, updates, testing, accessibility, and commerce need an independent process and lifecycle
- Cost: two repositories and a compatibility contract
- Revisit when: Omarchy adds an external-app contract or the companion has no discovery value

#### Tauri over Electron

- Chosen: system webview with Rust host
- Over: bundled Chromium runtime
- Because: lower expected footprint and a narrower native surface fit Omarchy better
- Cost: WebKitGTK variability and broader Linux prerequisites
- Revisit when: the measured support burden exceeds the resource savings or uniform Chromium behavior becomes essential

#### Tauri/React over pure QML

- Chosen: web UI plus native shell
- Over: Qt/QML for the complete app
- Because: accessible form-heavy screens, content tooling, browser preview, visual tests, and cross-platform option are central
- Cost: visual integration with Omarchy is adapter-driven rather than native QML throughout
- Revisit when: the slice fails native input/performance targets or the product is permanently Omarchy-only and QML tooling improves the total test cost

#### Phaser over a game engine written from scratch

- Chosen: established 2D scene runtime
- Over: hand-built loop and renderer
- Because: focus should remain on learning mechanics and content rather than collision, audio, scene, and render infrastructure
- Cost: dependency size and canvas accessibility work
- Revisit when: the slice needs only simple DOM animation or Phaser becomes the dominant complexity

#### Pure domain packages over UI-owned rules

- Chosen: deterministic framework-free TypeScript
- Over: rules in React hooks or Phaser scenes
- Because: reproducibility, property tests, simulation, and portability are product requirements
- Cost: adapters and event contracts add files and concepts
- Revisit when: never for separation itself; specific hot paths may move to Rust with differential evidence

#### SQLite over localStorage or remote database

- Chosen: Rust-owned local SQLite
- Over: browser storage, loose JSON, cloud storage
- Because: durability, multiple profiles, migrations, exports, recovery, and queries
- Cost: native tests and schema operations
- Revisit when: the slice proves a smaller model or approved sync becomes necessary

#### Offline signed license over continuous login

- Chosen: parent-acquired, locally verified entitlement
- Over: child account, always-online subscription validation
- Because: privacy, resilience, and a one-time family promise
- Cost: revocation and device enforcement are weaker; recovery and key custody are operational responsibilities
- Revisit when: business model changes after research, with owned access and child safety preserved

#### One complete free world over timed trial

- Chosen: durable free learning value
- Over: expiring trial or heavily gated demo
- Because: trust and child usefulness should precede purchase pressure
- Cost: more content must be produced before revenue
- Revisit when: scope needs narrowing, but not by paywalling safety, access, or core remediation

#### Local-only learning data over telemetry

- Chosen: no remote gameplay analytics in the initial release
- Over: automatic event analytics and crash uploads
- Because: child privacy, trust, and operational simplicity outweigh early funnel precision
- Cost: product decisions rely on smaller consented research and parent-reported support
- Revisit when: a separate data purpose, consent method, vendor, retention, deletion, and legal review are approved

#### Change-scoped CI over every-test-on-every-doc-change

- Chosen: fail-closed path classification with a complete release lane
- Over: full native matrix for all changes or weak universal smoke test
- Because: contributors need proportionate feedback while releases need comprehensive evidence
- Cost: the classifier needs tests and governance
- Revisit when: repository scale requires an explicit build graph

### What Was Deliberately Not Built

No code is built in this phase. More importantly, the target scope deliberately excludes cloud learner accounts, cloud saves, social features, leaderboards, chat, ads, behavioral tracking, automatic crash upload, runtime AI, voice capture, photo capture, global keyboard monitoring, school rostering, and child-facing commerce. These omissions are not a backlog accident. They protect the core proposition and prevent an early product from becoming a surveillance or platform project.

Mobile, macOS, Windows, and browser production delivery are also excluded from the first release. The architecture preserves portability, but each platform adds signing, packaging, keyboard, accessibility, store, legal, and test obligations. Cross-platform claims begin only after the Omarchy product proves interest and learning value.

The exact story, public name, pricing, merchant, update window, device count, refund terms, and curriculum sequence were not invented. They require evidence or authority the current workspace does not contain. The Blueprint uses unknown IDs rather than hiding these gaps in polished prose.

### Assumptions the Architecture Rests On

- Ages 9 to 11 and 12 to 14 are separate candidate cohorts, not one selected market. Cohort findings change reading load, consent, interaction, art, support, and positioning.
- Linux on current Omarchy is the first platform. The product might later broaden, but first-release quality is not diluted by untested portability claims.
- Parents prefer a one-time family purchase. This remains a hypothesis until price research.
- Local-only progress is acceptable for initial buyers. If device sync is essential, privacy and architecture must be reopened.
- Tauri plus WebKitGTK can meet input, frame, focus, audio, and packaging targets. This is the main technical hypothesis for the slice.
- An independent learning reviewer can accept an accuracy-first mastery model and proposed lesson graph.
- Intent Solutions can maintain signing keys, releases, policy pages, support, and vulnerability intake for a paid product.

Each assumption has a defined revisit point in the brief or risk register. An assumption is not transformed into fact by repeating it in multiple documents.

## 5. Directory Structure

### Target App Layout

```text
typing-adventure-app/
├── apps/
│   ├── desktop/                   # React route shell and Tauri frontend
│   └── web-preview/               # development and supervised study preview
├── packages/
│   ├── domain/                    # deterministic session and mastery logic
│   ├── curriculum/                # schemas, graph, selection, content API
│   ├── input/                     # keyboard normalization and focus rules
│   ├── game-scenes/               # Phaser scenes and semantic adapters
│   ├── ui/                        # accessible components and design tokens
│   └── test-fixtures/             # seeds, clocks, profiles, corrupt data, licenses
├── content/
│   ├── curriculum/                # skills, lessons, prompts
│   ├── story/                     # missions, characters, dialog
│   ├── locale/                    # learner and parent strings
│   └── provenance/                # asset and content rights records
├── src-tauri/
│   ├── src/                       # narrow native commands and adapters
│   ├── migrations/                # ordered SQLite migrations
│   ├── capabilities/              # explicit Tauri permissions
│   └── tauri.conf.json            # bundle, CSP, updater, identifiers
├── tests/
│   ├── contract/
│   ├── integration/
│   ├── e2e-web/
│   ├── e2e-desktop/
│   ├── system-omarchy/
│   ├── performance/
│   └── security/
├── tools/                         # content, evidence, SBOM, and release tooling
├── 000-docs/                      # doc-filing-compliant operational corpus
├── .github/                       # owners, issues, CI, release workflows
├── AGENTS.md                      # Beads and agent operating rules
├── CLAUDE.md                      # compatible AI project guidance if needed
├── SECURITY.md
├── SUPPORT.md
├── CONTRIBUTING.md
├── LICENSE
├── package.json
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
└── rust-toolchain.toml
```

### Target Companion Layout

```text
typing-adventure-omarchy/
├── BarWidget.qml                  # bar button and app state cue
├── Panel.qml                      # small launch/help/progress surface
├── Model.js                       # pure summary parsing and launch state
├── manifest.json                  # marketplace identity and bar entry point
├── contracts/
│   ├── local-summary.md           # app/plugin compatibility contract
│   └── marketplace.md             # claim evidence ledger
├── tests/                         # model, contract, a11y, gates, journeys
├── e2e/                           # Buzz journey
├── scripts/gates/                 # vendored, manifest-bound canonical lane
├── scripts/                       # rig, render, approval, freshness
├── assets/                        # original listing and icon assets
├── 000-docs/                      # only useful plugin-specific records
└── repository governance files
```

### Load-Bearing Files

These do not exist yet in the app repo, but their contracts should be treated as load-bearing:

| Path | Role | Failure consequence |
|---|---|---|
| `packages/domain/src/session.ts` | normative state transition | incorrect teaching, scoring, or unreproducible sessions |
| `packages/domain/src/mastery.ts` | progression and adaptation | children advance too early, get trapped, or receive unexplained practice |
| `packages/input/src/normalize.ts` | key/layout/focus semantics | false errors, shortcut conflict, layout exclusion, leaked input |
| `packages/curriculum/schema/*.json` | content contract | dead paths, untaught keys, rights or entitlement drift |
| `src-tauri/src/storage.rs` | transaction and data boundary | progress loss, retention failure, unsafe paths |
| `src-tauri/src/entitlement.rs` | paid access verification | forged unlock, lost access, child data mixed with commerce |
| `src-tauri/tauri.conf.json` | permissions, CSP, updater, application ID | broad authority or broken distribution |
| `src-tauri/migrations/` | schema evolution | irreversible data loss or incompatible rollback |
| `content/provenance/manifest.*` | rights chain | takedown or inability to distribute commercial assets |
| `.github/workflows/release.yml` | build/sign/provenance sequence | altered or untraceable release artifacts |
| `tools/evidence-verify.*` | candidate evidence identity | green evidence attached to the wrong revision |
| companion `manifest.json` and `Model.js` | marketplace identity and local contract | shell load failure or private data exposure |

### Repo-Dress Audit of the Widget Template

Target: `/home/jeremy/000-projects/omarchy-widget-template`, remote `jeremylongshore/omarchy-widget-template`, branch `main`, commit `19f1e64`, clean after tests, MIT license, no release tag observed.

The 27-item repo-dress checklist classifies as:

| Classification | Count | Detail |
|---|---:|---|
| Present | 18 | 10 root governance files, all 6 GitHub-layer files, Dependabot, CI capability through `test.yml` plus `gates.yml` |
| Project-specific alternative or not applicable | 6 | enterprise planning set is excessive for a small template; contracts and test documentation provide narrower useful context |
| Missing | 3 | `AGENTS.md`, `CLAUDE.md`, release automation |

Material template findings:

1. `CHANGELOG.md` tells users to run `scripts/gen-changelog.py`, but only `scripts/gen-changelog.sh` exists. The script's own usage is correct. This is a documentation drift defect.
2. Package and manifest versions are `0.1.0`, while the placeholder changelog section is `1.0.0 - unreleased`. A template may intentionally stage a target version, but the current text reads as inconsistent.
3. There is no release workflow. That may be reasonable for a template that is copied rather than distributed as a binary, but instantiated production plugins need a defined release and evidence lane.
4. `AGENTS.md` and `CLAUDE.md` are absent. The app repo should include agent and Beads rules. The installable companion tree must still satisfy gate C44, which excludes agent instructions from the plugin payload.
5. The README names `test.yml` as the CI artifact but does not summarize the separate gate and review workflows in its file table.
6. `SECURITY.md` promises acknowledgement "within a few days," while `SUPPORT.md` correctly disclaims guaranteed response. A paid app needs explicit owned response targets; a personal template can retain a lower promise if it is internally consistent.
7. OSV and Markdown lint were unmeasured in the audit environment because their tools were absent. Audit-harness correctly reported advisories rather than passes.
8. A Buzz or real-shell render was not run in this audit. Static and Node evidence must not be described as native render proof.

The template remains a strong seed for the companion because it encodes bounded QML text, no arbitrary shell construction, no unavailable runtime dependencies, manifest-bound vendored gates, change scope, coverage, mutation, race repetition, lifecycle scripts, and exact render receipts. It should not be forked as the app repository because its directory and CI assumptions are intentionally QML-plugin-specific.

## 6. Getting Started

### Prerequisites

This table describes the proposed first-week environment. Exact pins must replace every `unknown` before implementation is considered reproducible.

| Tool | Version | Install source | Verify |
|---|---|---|---|
| Git | supported current | Arch package | `git --version` |
| Node.js | pinned LTS, unknown | approved version manager or package | `node --version` |
| pnpm | pinned through Corepack | project package manager field | `pnpm --version` |
| Rust | pinned stable, unknown | rustup/toolchain file | `rustc --version` and `cargo --version` |
| Tauri CLI | lockfile pin, unknown | workspace dependency | `pnpm tauri --version` |
| WebKitGTK 4.1 | supported Arch package | `pacman` on dev/rig image | package query and native smoke |
| SQLite tooling | compatible version | Arch package and Rust dependency | `sqlite3 --version` where used |
| Playwright browsers | matching package version | Playwright installer in CI image | `pnpm playwright --version` |
| jq, shellcheck, gitleaks, lychee, markdownlint, OSV scanner | pinned/recorded | dev image | individual version commands |
| Omarchy and plugin validator | minimum and current named builds | resettable rig | Omarchy version and validate command |
| Buzz rig access | controlled maintainer environment | internal setup | non-secret health check |

Tauri's official Arch prerequisites must be translated into an idempotent development setup and CI image. Do not run an unreviewed curl-to-shell installer in automation. Capture package names and versions from the environment actually used.

### Zero to Running, Proposed Contract

1. Clone the future app repository and enter it.
2. Run `corepack enable` if the approved setup requires it.
3. Run `pnpm install --frozen-lockfile`. Expect no lockfile mutation.
4. Run `pnpm env:doctor`. Expect a structured report naming Node, Rust, WebKitGTK, graphics session, audio, keyboard layout, and missing optional rig tools.
5. Run `pnpm check`. Expect static and schema gates without network or native UI.
6. Run `pnpm test:unit`. Expect domain and Rust results with reproducible seeds.
7. Run `pnpm dev`. Open the printed loopback URL and use only synthetic native adapters.
8. Run `pnpm dev:desktop`. Expect a separate native window and an isolated test profile directory.
9. Run `pnpm test:e2e:web` for the fast user path.
10. On a compatible native machine, run `pnpm test:e2e:desktop`.

These commands are not implemented. The first scaffold pull request is responsible for making them true and documenting actual output.

### Common Setup Problems

| Symptom | Likely cause | Fix contract |
|---|---|---|
| Tauri build cannot find GTK/WebKit | missing or mismatched Arch development package | run doctor, install the documented package set, record package versions |
| Blank or visually corrupt native window | WebKitGTK/GPU/Wayland issue | capture logs and device identity, test software render only as diagnosis, compare supported matrix |
| Browser preview works but desktop E2E fails | mocked API differs from Tauri command or focus behavior | contract-test both adapters and reproduce on native rig |
| Keys grade incorrectly | layout, composition, repeat, or `key` versus `code` policy mismatch | capture sanitized event classification in developer mode, add fixture, never store unrelated raw input |
| System shortcut steals a lesson key | Hyprland binding conflict | pause safely, revise lesson/control mapping, document supported practice mode |
| Tests pass locally but fail in CI | unpinned tool/browser/font/locale/clock | compare doctor reports and lock environment inputs |
| Profile appears empty after upgrade | migration or path mismatch | stop writes, preserve DB, run recovery inspection, do not create a replacement automatically |
| Plugin shows app missing | desktop entry/path contract drift | check fixed contract version, fall back to documented install help |

## 7. Operations

### Command Map

| Task | Proposed command | Notes |
|---|---|---|
| Run web preview | `pnpm dev` | synthetic adapters, no real child data |
| Run desktop app | `pnpm dev:desktop` | isolated dev profile |
| Static checks | `pnpm check` | includes docs/content/policy classification |
| Unit tests | `pnpm test:unit` | TypeScript and Rust |
| Property tests | `pnpm test:property` | logs replay seeds |
| Component tests | `pnpm test:component` | React and scene adapters |
| Browser E2E | `pnpm test:e2e:web` | Playwright and axe |
| Desktop E2E | `pnpm test:e2e:desktop` | real Tauri app on Linux |
| Content validation | `pnpm test:content` | graph, reading level, rights |
| Performance | `pnpm test:performance` | hardware identity required |
| Security | `pnpm test:security` | dependencies, permissions, runtime, redaction |
| Build candidate | `pnpm build` | does not publish |
| Prepare release | `pnpm release:prepare` | evidence, SBOM, checksums, signing handoff |
| Verify evidence | `pnpm evidence:verify` | exact revision and artifact identity |
| Full candidate lane | `pnpm test:release` | all applicable tests, no time shortcut |
| Companion portable checks | `npm test && scripts/run-plugin-gates.sh .` | after companion exists |
| Companion rig | `scripts/rig-verify.sh` and render/Buzz scripts | maintainer-controlled native proof |

### Deployment

There is no server deployment for child gameplay. Deployment means publishing a signed desktop artifact, compatible updater metadata, optional parent commerce services, a companion repository/listing, and accurate policy/site pages.

Pre-flight begins by freezing an exact clean revision. The release manager records the app version, content version, database schema, entitlement schema, summary contract, prior supported version, toolchains, and target matrix. All P0 acceptance evidence must resolve to this candidate. If source or content changes, affected evidence is invalidated.

The build runs in a controlled environment with least-privilege GitHub permissions or an equivalent builder. It produces the app packages, checksums, SBOM, provenance, update metadata, and a complete evidence packet. Signing private keys do not enter source control, logs, artifacts, pull-request workflows, or ordinary development environments. App artifacts and updater metadata have separate verification where the framework requires it.

The candidate is installed on a reset minimum Omarchy rig. The operator exercises first install, free play, entitlement import with a test key, paid play, close/restart, update from the prior version, migration, rollback, deletion, uninstall, reinstall, companion install, companion removal, and app/plugin mismatch. Network and process traces confirm the privacy and lifecycle claims. A human reviews the visible experience and evidence limitations.

Publishing remains a separate action. Following the Contributing Clanker authority pattern, a preparation command may assemble everything but cannot create a public release, change update metadata, submit to the marketplace, enable checkout, or publish legal text. Fresh approval names the exact revision, version, artifact hashes, destinations, known limitations, and rollback.

Verification after publish checks that public bytes match approved hashes, signatures verify, download and update links work, policy links resolve, release notes are correct, direct app installation works, and the marketplace listing points to the intended repository. The release receipt records URLs and timestamps. Rollback is rehearsed before the observation window ends.

### Monitoring and Alerting

There is no plan for automatic learner telemetry. The supported monitoring model is deliberately split:

- Public synthetic health: download, updater metadata, checkout, and license recovery endpoints.
- Internal synthetic canary: install and launch a fresh profile on a controlled Omarchy rig.
- Repository health: CI, dependency alerts, vulnerability reports, release signatures, and issue backlog.
- Parent support: voluntary ticket and a parent-previewed redacted diagnostic bundle.
- Research: consented, time-bounded pilot evidence under a separate protocol.

SLIs for public infrastructure may include endpoint availability, signed-metadata freshness, checkout success, license delivery delay, and support response. They must not include child identity or learning events. App crash-free rate cannot be claimed until a lawful and accurate collection method exists. A successful synthetic canary is not user uptime.

On-call is not established. Before paid release, name primary and backup owners for signing/update compromise, checkout/license outage, child privacy, data loss, and vulnerability disclosure. A product sold to families cannot rely on a generic "we will look when available" promise without stating support boundaries clearly.

### Incident Response

| Severity | Definition | Target initial response | Playbook |
|---|---|---|---|
| P0 | child data disclosure, malicious or wrongly signed update, broad destructive data loss, unsafe content | immediate upon awareness | stop distribution and update, preserve evidence, revoke or rotate according to plan, engage privacy/security/legal owners |
| P1 | supported app cannot launch broadly, migration corruption, child reaches commerce, entitlement outage removes paid access | within one hour during supported coverage | withdraw candidate, restore prior metadata/artifact, publish parent-facing status, recover data |
| P2 | material feature, accessibility, lesson, or isolated recovery failure | same business day | triage, workaround, patch candidate, regression evidence |
| P3 | cosmetic, documentation, or low-impact content defect | normal backlog | issue, owner, next release disposition |

The first responder does not modify production blindly. They identify the release and hashes, stop the narrow failing surface, preserve relevant logs without expanding child-data collection, and use the rehearsed rollback. Every P0/P1 gets a post-incident record with impact, timeline, root cause, contributing conditions, corrective controls, evidence, and policy notification decision.

## 8. Things That Will Bite You

### 8.1 `key` and `code` are not interchangeable

- Symptom: the screen asks for one character but a learner on another layout is graded against a physical US position.
- Cause: `KeyboardEvent.code` describes physical position while `key` represents the generated character with layout and modifiers. Composition and dead keys add another state.
- Fix: make the expected semantic explicit per lesson, declare supported layouts, test real fixtures, and wait for composition completion.
- Prevention: centralize input normalization and prohibit direct grading inside UI components or scenes.

### 8.2 Omarchy shortcuts can intercept the lesson

- Symptom: typing a combination changes workspace, closes a window, or never reaches the app.
- Cause: compositor/system bindings have higher authority than the webview, and an Omarchy shortcut curriculum deliberately teaches some of those combinations.
- Fix: keep ordinary touch-typing prompts away from global combinations, pause on focus loss, and use a controlled shortcut-practice sandbox with current bindings.
- Prevention: maintain a versioned binding compatibility matrix and do not infer completion by globally watching the desktop.

### 8.3 Browser tests can create false native confidence

- Symptom: Playwright is green while the Tauri app has focus, font, audio, file, or WebKitGTK bugs.
- Cause: the browser preview uses mocks and a different host/runtime.
- Fix: reproduce in real Tauri E2E and the Omarchy rig; add a contract case at the narrowest layer.
- Prevention: treat browser E2E as fast feedback and native E2E as separate release evidence.

### 8.4 Canvas accessibility is not automatic

- Symptom: a sighted mouse user can play, but a keyboard or assistive user cannot understand state or leave the scene.
- Cause: visual scene objects have no semantic accessibility tree by default.
- Fix: mirror instructional state and controls through semantic UI, preserve focus, support reduced motion and untimed paths, and test manually.
- Prevention: make accessibility state part of the scene contract, not a late overlay.

### 8.5 A typing app can accidentally become a keylogger

- Symptom: raw keys, passwords, or unrelated desktop input appear in logs or storage.
- Cause: global hooks, broad event listeners, verbose debugging, or failure to stop capture on blur.
- Fix: remove global capture, constrain listeners to focused lesson surfaces, redact logs, delete unsafe evidence, and review incident obligations.
- Prevention: architecture control CTRL-102, runtime process observation, log tests, and a ban on raw input telemetry.

### 8.6 Content can violate the engine without failing TypeScript

- Symptom: a lesson introduces an untaught key, paid prerequisite blocks free completion, or a story branch is unreachable.
- Cause: curriculum is graph data whose correctness is not guaranteed by compilation.
- Fix: schema, graph, property, reading-level, entitlement, and traversal validators.
- Prevention: stable IDs, reviewer ownership, golden completion paths, and content-specific CI.

### 8.7 Fast feedback can teach bad technique

- Symptom: children mash keys, race timers, or improve WPM while accuracy and posture worsen.
- Cause: the game rewards speed or spectacle more strongly than controlled input.
- Fix: lower or remove timers, score accuracy first, expose assistance, and revisit mastery with a learning reviewer.
- Prevention: playtest observation and accuracy-first invariants before full content production.

### 8.8 Local-first still has network privacy surfaces

- Symptom: marketing says "fully offline" while updater, download, checkout, license recovery, fonts, or support call external services.
- Cause: teams describe gameplay only and ignore distribution and adult flows.
- Fix: publish a complete data-flow inventory and qualify the claim precisely.
- Prevention: release-time network capture and policy comparison across every surface.

### 8.9 Offline licensing creates support promises

- Symptom: a parent loses a license, refund does not revoke cleanly, device count is confusing, or key rotation invalidates access.
- Cause: signed offline artifacts trade continuous enforcement for resilience.
- Fix: simple published policy, recovery workflow, old-key verification window, and support tooling.
- Prevention: decide the commercial contract before implementation and test it under service outage.

### 8.10 SQLite migrations and rollback can disagree

- Symptom: the old app is restored but cannot read data written by the new app.
- Cause: a forward-only migration occurred before a bad release was detected.
- Fix: backup before migration, declare compatibility, ship recovery build, or block unsafe downgrade while preserving export.
- Prevention: test every supported version transition and rollback with real fixtures before release.

### 8.11 The plugin template can be overtrusted

- Symptom: a generated companion passes generic template tests but fails its actual launch or summary journey.
- Cause: the template proves scaffolding and generic contracts, not product-specific behavior.
- Fix: replace placeholders, extend model tests, write an app-absent state, use deterministic summary fixtures, and add a product-specific Buzz assertion.
- Prevention: require claim-by-claim marketplace evidence and reject generic preview proof.

### 8.12 Policy prose drifts from behavior

- Symptom: a privacy page names vendors not used, omits an update endpoint, or displays today's date as though policy changed today.
- Cause: copied templates and runtime-generated dates.
- Fix: policy-as-versioned-content, fixed effective dates, candidate data inventory, and qualified review.
- Prevention: make policy changes a governed release surface and compare them with network/dependency evidence.

### 8.13 Kids detect fake game layers immediately

- Symptom: learners skip dialog, call it schoolwork, or refuse a second session despite polished art.
- Cause: typed text does not cause meaningful game state, tone imitates children, or rewards mask drills.
- Fix: simplify effects, connect every prompt to a decision or action, and co-design before scaling.
- Prevention: the anti-cheese test and voluntary-continuation gate.

### 8.14 One-time pricing can underfund maintenance

- Symptom: update, support, and signing costs continue while revenue is concentrated at purchase.
- Cause: the license promise and cost model were not defined.
- Fix: model support per family, define included update window, sell optional future packs or editions without revoking owned access.
- Prevention: parent research and business approval before checkout.

## 9. Security and Access

### Access Control

| Role | Purpose | Required permissions | MFA |
|---|---|---|---|
| Repository contributor | issues and pull requests | read and proposed changes only | GitHub account policy |
| Maintainer | merge and triage | protected branch review, no signing key by default | required |
| Release manager | prepare and publish release | protected environment after approval | required |
| Signing custodian | sign app/update artifacts | isolated key use only | required plus hardware/approved control |
| Commerce operator | checkout, refunds, recovery | parent commerce records only | required |
| Privacy/legal reviewer | policies, incidents, vendor register | minimum evidence access | required where system supports |
| Research lead | consented participant records | restricted study storage only | required |
| Support operator | parent tickets and previewed bundles | no default database or signing access | required |

Child mode and parent mode are application roles, not online accounts in the first release. The local OS user ultimately controls local files. The app must not imply that a local adult gate provides strong authentication. For family devices, parent settings may use a local PIN if approved, but its limitations and recovery behavior must be honest.

### Secrets

Proposed secrets include app/update signing private keys, entitlement signing private key, checkout provider credentials, webhook secrets, support-mail credentials, and any release-environment tokens. None exists for this product today.

Signing keys need separate purpose and rotation. The app embeds only public verification keys. Private keys live in an approved secrets system or hardware-backed signing process, are accessible only through a protected release environment, and never print to logs. Backup and recovery are documented before the first paid entitlement is issued. Losing the only entitlement key without a rotation plan can strand customers; leaking it can permit forged licenses.

GitHub workflows use least permissions and pinned third-party actions. Pull-request workflows from forks cannot access production secrets or sign artifacts. Release jobs require protected environment approval and validate that they operate on the approved tag/SHA. Artifact attestations can add provenance, but they do not replace application signatures, update signatures, reviewer trust, or reproducible verification.

### Threat Summary

| Threat | Primary control | Verification |
|---|---|---|
| renderer invokes broad native action | narrow Tauri commands and capabilities | static command inventory and negative IPC tests |
| path traversal or symlink swap | app-owned directory, allowlists, descriptor-safe lifecycle | filesystem adversarial tests |
| malformed content or license exhaustion | byte/count limits and strict schemas | fuzz and boundary tests |
| forged entitlement | modern signature, algorithm/key allowlist | cryptographic fixture matrix |
| malicious update | signed artifact/metadata and target/version policy | altered, replay, and downgrade tests |
| dependency compromise | locks, review, SBOM, scans, protected build | candidate supply-chain packet |
| child data leak | local-only model, no telemetry, redaction | runtime network and log observation |
| global input collection | focused app listeners only, no global hooks | permission/process/code audit |
| asset rights failure | provenance manifest and human review | release control |
| social harm/manipulative design | no social/ads/pressure loops and child testing | route inventory and study review |

### Honest Security Assessment

There is no implemented security control for the app because there is no app. The Blueprint specifies controls and verification, which improves planning but is not protection. Tauri's security model, Rust memory safety, a local database, and cryptographic libraries can all be misconfigured. A static scanner cannot establish child privacy, and a legal page cannot establish runtime behavior.

The companion template has real static and automated strength. At `19f1e64`, its 28 Node tests passed; measured `Model.js` statement, function, branch, and line coverage were all 100 percent; three race repetitions passed; mutation reported 49 killed and zero survived counted mutants for 100 percent; deep audit reported five passes; gitleaks and link checks passed; and 13 vendored plugin gates passed. OSV and Markdown lint were advisory/unmeasured because tools were missing. No native Buzz render was run here. These facts apply only to the template revision, not the future companion.

COPPA applicability and compliance remain legal questions. FTC materials state that child-directed online services collecting personal information from children under 13 can be covered and that persistent identifiers, IP addresses, photos, voice, and other data can qualify. The 2025 amendments and planned release date require current review. The proposed local-first model minimizes collection, but update and commerce systems still need precise analysis. Public claims wait for qualified approval.

## 10. Cost and Performance

### Monthly Costs

No vendor is selected and no approved budget exists. The table is a planning envelope, not a quote.

| Resource | Early free release | Paid release | Notes |
|---|---:|---:|---|
| Public source repositories and CI | $0 to plan-dependent usage | $0 to plan-dependent usage | private signing environments or heavy native matrices may add cost |
| Static downloads/update metadata | $0 to $50 | $0 to $100+ | depends on artifact size and volume |
| Domain and policy pages | existing portfolio allocation to $25 | same | reuse approved Intent infrastructure where appropriate |
| Checkout/merchant | not applicable | transaction fees and possibly monthly/vendor charges | merchant of record versus direct merchant is U-104 |
| License delivery/recovery | not applicable | $0 to $100+ at small scale | custom static flow may be cheap but adds operations |
| Support email/ticketing | existing allocation | $0 to $100+ | staff time is likely larger than software cost |
| Signing/key custody | $0 to service/hardware cost | service/hardware cost | design and custody matter more than raw monthly fee |
| Child/parent research | study-specific | ongoing study-specific | consent, compensation, facilitation, and review not included |
| Art, audio, writing, learning/legal review | project investment | project investment | likely dominant pre-launch spend, currently unknown |

The primary cost is not cloud infrastructure. It is high-quality curriculum, original content, art/audio rights, learning review, child research, accessibility, Linux hardware testing, support, and maintained releases. An offline app can have low hosting costs and still be expensive to build responsibly.

### Performance Targets

| Metric | Proposed target | Evidence status |
|---|---:|---|
| key to visible feedback p50 | under 25 ms | unmeasured |
| key to visible feedback p95 | under 50 ms | unmeasured |
| active frame p99 | under 33 ms on minimum device | unmeasured |
| warm start interactive | under 2 seconds | unmeasured |
| cold start interactive | under 5 seconds | unmeasured |
| ordinary save transaction | under 50 ms p95 without blocking input | unmeasured |
| hidden idle CPU | below 1 percent on minimum device | unmeasured |
| unexplained gameplay network | zero connections | unmeasured |
| memory | baseline and cap set after slice profiling | unknown |

Measurements record device, CPU/GPU, RAM, kernel, compositor, Omarchy, WebKitGTK, display scale, refresh rate, keyboard, power state, app SHA, content version, run length, and method. A number without environment identity is not release evidence.

### Scaling Limits

The local app does not scale by concurrent users on one server. It scales by profile count, lesson/content size, session history, database size, asset memory, and supported device diversity. Initial product limits should be explicit and tested: at least four paid profiles, a maximum content pack size, bounded prompt and event records, bounded support export, and a history-compaction policy. Exact limits follow slice profiling rather than arbitrary large numbers.

Commerce and update infrastructure scale with active installations, release artifact bandwidth, checkout attempts, license issuance/recovery, and support. Static update metadata and object storage can handle early volume cheaply, but an entitlement recovery service introduces authentication, abuse, mail deliverability, rate limiting, refund state, and on-call needs. Vendor SLAs and quotas are unknown until selected.

The most likely early scale limit is human: creating and reviewing enough high-quality curriculum and responding to family support. The roadmap should gate new platforms and content packs on maintained release capacity, not only demand.

## 11. Current State

### Health Score

| Area | Weight | Score | Evidence |
|---|---:|---:|---|
| Product framing and scope | 15 | 10 | draft brief, PRD, free/paid and app/plugin boundary |
| Architecture and decisions | 15 | 9 | proposed ADRs and target architecture; spike absent |
| Learning and child evidence | 15 | 1 | plan exists; no reviewer or study |
| Implementation | 15 | 0 | no app or companion repository |
| Testing and quality design | 10 | 7 | detailed test plan; no implementation results |
| Privacy, legal, and safety | 10 | 3 | minimization and annex; no qualified approval or product policy |
| Release and supply chain | 10 | 2 | target controls; no pipeline, keys, or artifact |
| Operations and ownership | 10 | 2 | proposed roles/runbook; owners and coverage absent |
| **Total** | **100** | **34 raw planning points, capped to 24 for zero implementation** | pre-build |

The cap prevents extensive planning documents from making an unbuilt product appear operationally healthy.

### What Is Working

- The umbrella repository exists and already uses a flat `000-docs` sequence, an index, and prior Blueprint precedent.
- The current workbook defines objectives, requirements, decisions, architecture, UX, privacy, acceptance, tests, playtests, risk, and operations with stable IDs.
- The public marketplace snapshot confirms adjacent typing and Omarchy-learning tools, including an exact `OmaType` name collision, which prevents accidental duplicate branding.
- The local widget template is clean at `19f1e64` and its portable declared test/gate lane passed during this audit with the limitations stated above.
- HustleStats exposes a Privacy Policy and Terms page. Their topics and deficiencies have been inventoried for product-specific policy work.
- The design has a clear stop rule: do not scale content or commerce until the child loop, learning model, privacy model, and parent value pass their gates.

### What Needs Attention

High findings:

1. **No approved identity**: public name, app ID, repository names, domain, and trademark screen are unresolved. Impact: rework, collision, or rights dispute. Next: TASK-101.
2. **No implementation repository**: no app code, dependency locks, CI, executable, or companion exists. Impact: architecture remains unverified. Next: scaffold spike after owner review.
3. **No learning owner or validated curriculum**: mastery and lesson order are proposals. Impact: product may teach poor technique. Next: TASK-103.
4. **No child or parent evidence**: no co-design, usability, retention, or price evidence. Impact: high risk of a polished product children reject. Next: TASK-102 and TASK-107.
5. **No product-specific legal approval**: COPPA, state law, seller, license, and jurisdiction are unresolved. Impact: unsafe claims or blocked commerce. Next: qualified review of KTA-PRIV-001.
6. **No commerce contract**: merchant, price, refund, recovery, device, taxes, update promise, and entitlement operations are unresolved. Impact: customer harm and support debt. Next: TASK-113 after free pilot.
7. **No signing/update/rollback capability**: no keys, protected environment, prior artifact, or rehearsal exists. Impact: supply-chain and data-loss risk. Next: TASK-111.
8. **No named maintenance coverage**: product, security, privacy, curriculum, accessibility, creative, release, and support roles are unaccepted. Impact: paid product could become unmaintained. Next: ownership gate before full build.

Medium findings:

1. Exact Omarchy/Arch/WebKitGTK/hardware/layout support matrix is unknown.
2. Tauri/Phaser performance and focus behavior is unproven.
3. Character/story/art/audio direction lacks original final assets and rights records.
4. Accessibility scope beyond WCAG-adapted UI targets lacks specialist review.
5. Shortcut academy depends on changing Omarchy bindings and a safe sandbox.
6. Local history retention and compaction defaults remain proposals.
7. Support bundle redaction and diagnostic usefulness are not designed in code.
8. Cross-platform sequencing and economic trigger are undefined.
9. HustleStats legal footer and policy versioning defects should not be copied and deserve a separate fix in that product.

Low findings:

1. Final design tokens and typography are undecided.
2. Companion bar cue and panel information density need a prototype.
3. Marketing screenshots, demo cast, and store description depend on a real candidate.
4. Appaudit filename uses the repository's established `AA-AUDT` convention even though the generic doc-filing table normally categorizes audits under `RA`; this is a documented project-specific convention.

### Implementation Status

| Component | Status | Evidence |
|---|---|---|
| Blueprint workbook | draft implemented | documents 014 through 025 in planning worktree |
| Public product name | blocked on decision | marketplace collision evidence only |
| App repository | not created | none |
| Domain engine | not implemented | requirements and architecture only |
| Curriculum | not authored | model and review requirements only |
| React/Phaser UI | not implemented | UX and ADR only |
| Rust/Tauri host | not implemented | ADR and architecture only |
| SQLite storage | not implemented | data model and tests only |
| Entitlement/checkout | not implemented | proposed contract only |
| Companion plugin | not implemented | template audited as seed |
| App CI/release | not implemented | quality and operations contract only |
| Child/parent study | not conducted | protocol only |
| Legal/privacy approval | not conducted | source inventory and questions only |
| Production | nonexistent | no release or deploy |

### Widget Template Verification Snapshot

| Check | Result | Limit |
|---|---|---|
| `npm test` | 28/28 pass; Model.js 100 percent measured statements, branches, functions, lines | template only |
| `npm run test:race` | three concurrent repetitions passed | portable Node layer only |
| `npm run test:mutation` | 49 killed, 0 survived counted mutants, 100 percent | mutation scope is Model.js |
| `npm run audit` | deep 5 pass; scan 3 pass, 2 advisory | OSV and Markdown lint tools absent |
| `scripts/run-plugin-gates.sh .` | 13 enforced gates pass | static/vendored lane |
| Buzz/real shell | not run | native behavior unverified in this audit |
| Repo-dress | 18 present, 6 alternative/N/A, 3 missing | separate governance audit, not an executable gate |

## 12. Roadmap

### Week 1: Decision and Evidence Foundation

- Approve or revise the app-first boundary and first target age/platform.
- Assign owners for product, engineering, learning, accessibility, privacy/legal, creative, release, and support.
- Open durable Beads work under the correct umbrella epic when the implementation repository is chosen.
- Complete naming candidates, repository/app ID rules, preliminary collision search, and legal screen.
- Fix the Blueprint after human review and mark actual decisions with approvers and dates.
- Write a child-research protocol and recruit only after guardian-consent and evidence-storage review.
- Turn the widget-template repo-dress findings into a separate bounded maintenance change, not a side effect of this documentation branch.

Week 1 exits when the team can name the product internally, name accountable people, explain the first study, and state which decisions remain explicitly blocked.

### Month 1: Discovery and Disposable Proofs

- Run parent interviews and child paper co-design.
- Obtain learning and accessibility review of curriculum v0 and measurement probes.
- Create a new app repository with repo-dress governance, Beads, doc-filing, protected CI, and no generic enterprise clutter beyond what this product needs.
- Pin Tauri, Rust, Node, pnpm, React, Phaser, test tools, and Arch dependencies.
- Build an environment doctor and reproducible preview/native setup.
- Implement input normalization, deterministic session core, a small curriculum graph, SQLite dev store, and synthetic fixtures.
- Build three disposable 3 to 5 minute gameplay greyboxes for one skill family, plus a minimally dressed drill and an attractive neutral alternative.
- Run a separate native input, focus, accessibility, performance, audio, and packaging spike with synthetic data.
- Test candidate ages 9 to 11 and 12 to 14 separately after research-entry controls are approved; do not select an audience from Roblox demographics alone.
- Record the owner decision on whether any durable vertical slice may begin.
- Run static, unit, property, component, browser, native, accessibility, and performance slice gates.
- Conduct Stage B playtests and issue a proceed/change/stop decision.

Month 1 exits only when the gameplay and native proofs meet their separate thresholds, children understand the challenge and voluntarily choose to continue, errors do not encourage mashing, the selected direction works across supported accessibility paths, and qualified reviewers accept the research and learning direction. Passing Month 1 permits an owner decision; it does not automatically authorize a durable slice.

### Quarter 1: Free Product and Operational Proof

- Author and review the complete free world with provenance.
- Implement durable migrations, compaction, backup, recovery, support bundle, and privacy controls.
- Create the separate companion repository from the current widget template, then apply repo-dress fill-gaps behavior and product-specific tests.
- Establish resettable minimum/current Omarchy rigs and real Buzz journeys.
- Implement protected build, SBOM, signing, update metadata, prior-version migration, rollback, and candidate evidence verification.
- Publish product-specific privacy, terms/EULA, child safety, deletion, security, support, and open-source notices only after approval.
- Run the closed free-world pilot and analyze voluntary continuation, learning probes, reliability, accessibility, and support.
- Publish free v1.0 only after its exact-candidate approval and completed rollback rehearsal.
- Observe the free release, then conduct parent pricing and paid-boundary research.
- Decide whether paid Family v1.1, one-time pricing, later content packs, and platform expansion are justified.

Quarter 1 does not automatically end in paid launch. It establishes a real free product and ends in a separate paid-build decision backed by evidence. If the free product is enjoyed but willingness to pay is weak, the team can keep a high-quality open-source/free Omarchy product without prematurely adding commerce operations.

## 13. Quick Reference

### URLs

| Resource | URL |
|---|---|
| Omarchy marketplace catalog | https://plugins.omarchy.org/catalog.json |
| Omarchy publishing guidance | https://plugins.omarchy.org/publish.html |
| Tauri prerequisites | https://v2.tauri.app/start/prerequisites/ |
| Tauri tests | https://v2.tauri.app/develop/tests/ |
| Tauri updater | https://v2.tauri.app/plugin/updater/ |
| Phaser docs | https://docs.phaser.io/ |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ |
| FTC COPPA guidance | https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions |
| FTC 2025 COPPA amendments | https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-312-coppa-final-rule-amendments |
| HustleStats Privacy | https://hustlestats.io/privacy |
| HustleStats Terms | https://hustlestats.io/terms |
| GitHub artifact attestations | https://docs.github.com/en/actions/concepts/security/artifact-attestations |

### First-Week Checklist

- [ ] Read the project brief, decision records, privacy annex, test plan, and this playbook.
- [ ] Confirm working label is not used as public identity.
- [ ] Assign accountable owners and reviewers.
- [ ] Record approved age, platform, privacy, licensing, and research boundaries.
- [ ] Create Beads epic and dependencies only in the chosen implementation authority.
- [ ] Create app repo with repo-dress fill-gaps audit and doc-filing index.
- [ ] Pin toolchain and pass environment doctor on minimum Omarchy rig.
- [ ] Compare three disposable gameplay proofs and complete the separate native-runtime spike before deciding on a durable vertical slice or full content production.
- [ ] Never use real child data in local development or CI.
- [ ] Never describe planned checks as passed evidence.
- [ ] Never publish a release, marketplace submission, policy, or paid change without fresh exact-candidate approval.

---

## Appendices

### A. Glossary

| Term | Meaning here |
|---|---|
| Adult gate | A local UX separation before parent controls; not strong identity proof unless implemented and described as such |
| App | The standalone desktop learning game in its own process |
| Attempt evidence | Minimal local record needed to update mastery for the active learning prompt |
| Companion | Free Omarchy QML plugin that launches the app and reads a bounded summary |
| Content version | Immutable identifier for curriculum, story, and assets used in a session |
| Deterministic replay | Re-running the same engine/content/seed/actions to reproduce the same normative state |
| Entitlement | Signed document declaring paid capabilities without learner data |
| Free world | Permanent, coherent introductory curriculum and story, not a timed trial |
| Mastery | Explainable skill readiness based primarily on accurate independent evidence and spacing |
| Omarchy rig | Resettable native system used for real shell, compositor, plugin, webview, and package tests |
| Parent mode | Local app area for settings, progress, commerce, export, reset, and deletion |
| Provenance | Evidence connecting source revision, build inputs, artifact, signatures, and review |
| Summary contract | Minimal versioned file/schema through which app shares non-sensitive status with companion |
| Vertical slice | Small complete experience proving architecture, learning loop, game feel, storage, and testing before scale |

### B. Reference Links and Authority

The local Blueprint workbook is the product planning authority only after owner review. The future app source and tests become implementation authority. The content registry becomes curriculum execution authority after learning/content approval. Public legal policies become disclosure authority after legal approval, but runtime evidence remains authority for what code actually does. Release receipts become authority for which bytes were published.

HustleStats policies are sources, not authorities for this product. They describe a networked youth soccer service with parent accounts, athlete data, analytics, cookies, hosting, email, and payments. The typing app has a different data model and cannot inherit those facts. The Hustle pages also need their own maintenance because the Privacy footer link is broken and the effective date is generated dynamically.

The widget template is authority for the current companion scaffold only at its exact revision. Its vendored gate manifest proves its local gate bytes match the recorded lane, not that a newer canonical lane does not exist. The advisory freshness check and release review remain important.

### C. Troubleshooting Playbooks

#### C.1 Learner progress is missing after update

1. Stop the app and do not create a new profile with the same identifier.
2. Record app version, content version, database schema, platform, and last known working version.
3. Copy the database and backups using the approved read-only recovery tool.
4. Verify checksums before inspection.
5. Run migration diagnosis against a copy, never the only file.
6. Determine whether the data is present but unreadable, migrated partially, stored under a different app ID/path, or deleted.
7. Restore through the tested recovery build or export/import path.
8. Redact the support bundle and obtain parent approval before sending it.
9. If systemic, stop updater metadata and invoke P1/P0 criteria.

#### C.2 App grades the wrong key

1. Pause the lesson and preserve the session seed/content version.
2. Record OS layout name, physical keyboard, modifiers, composition state, and sanitized target/result classifications.
3. Reproduce in the input-package fixture without storing unrelated key sequences.
4. Compare `key`, `code`, location, repeat, Caps Lock, and composition behavior.
5. Add a failing regression case before changing normalization.
6. Re-run layout, mastery, browser, and native tests.
7. Review whether the affected layout remains supported for the current release.

#### C.3 Native app is blank or slow

1. Record exact package and hardware inventory.
2. Check WebKitGTK and graphics logs without enabling broad production telemetry.
3. Compare browser preview, native debug, and native release builds.
4. Disable one cosmetic layer at a time in a diagnostic build.
5. Measure main-thread, render, and IPC timing before selecting a workaround.
6. Do not weaken correctness or accessibility to hide a performance failure.
7. If minimum hardware fails, reopen ADR-102 before content expansion.

#### C.4 Entitlement stops working offline

1. Confirm free content still works.
2. Inspect only entitlement metadata needed for validation, not learner profiles.
3. Check token size/schema, product, edition, signature algorithm, key ID, validity policy, and app clock behavior.
4. Verify with known-good fixtures and the embedded public-key set.
5. If a release changed verification unexpectedly, stop update rollout and restore the prior candidate.
6. Issue a signed recovery entitlement through the approved parent support path if policy permits.
7. Record whether refund, transfer, or key rotation caused the state.

#### C.5 Companion fails or destabilizes shell

1. Disable the companion while leaving the standalone app installed.
2. Capture bounded relevant shell logs and process state.
3. Validate manifest and QML against the exact revision.
4. Run pure model tests with current and prior summary fixtures.
5. Verify timers/watchers stop when hidden and no arbitrary process command exists.
6. Run the Buzz lifecycle journey on a reset rig.
7. Ship a companion-only fix or fall back to launch-only behavior; no app data migration should be needed.

#### C.6 Unexpected outbound connection appears

1. Stop the candidate and preserve network/process evidence.
2. Identify process, destination, DNS name, dependency, trigger, and data categories.
3. Determine whether it is an approved updater/checkout action or an undeclared request such as remote font, image, analytics, crash tool, or webview behavior.
4. Remove or isolate the dependency and add a regression block.
5. Compare public policy and child-safety claims.
6. Invoke privacy/legal incident review if any learner or persistent identifier may have been transmitted.
7. Re-run the complete network observation before release resumes.

### D. Open Questions

| ID | Question | Decision owner | Needed before |
|---|---|---|---|
| U-101 | What public name, app ID, repositories, domain, and marks are cleared? | product/legal | public scaffold and marketing |
| U-102 | Who owns the curriculum, what sequence is approved, and how is mastery calculated? | learning/product | vertical-slice teaching claims |
| U-103 | What exact age, reading, accessibility, locale, and keyboard-layout range is supported? | product/accessibility | content freeze |
| U-104 | What price, merchant role, taxes, refund, device, update, transfer, and recovery promise applies? | business/legal | commerce implementation |
| U-105 | Which jurisdictions apply and what notices/consent/review are required? | legal/privacy | research and public release |
| U-106 | Who creates and clears story, art, audio, fonts, and lesson text? | creative/legal | asset production |
| U-107 | What minimum/current Omarchy, Arch, WebKitGTK, GPU, display, audio, and keyboard matrix is supported? | engineering/QA | architecture acceptance |
| U-108 | Who owns signing, release, security, privacy incident, and paid support coverage? | executive/operations | signed pilot and paid launch |

### E. Requirement-to-Evidence Spine

| Objective | Requirements | Decisions/components | Acceptance | Tests/evidence | Release gate |
|---|---|---|---|---|---|
| OBJ-101 voluntary return | REQ-120 through REQ-124 | ADR-103, CMP-102, CMP-104 | AC-120 through AC-122 | PLAY-101 through PLAY-106 | GATE-101, GATE-102 |
| OBJ-102 typing improvement | REQ-111 through REQ-119 | ADR-104, CMP-103 through CMP-106 | AC-111 through AC-119 | TEST-111 through TEST-120, PLAY-103 | GATE-103 |
| OBJ-103 local child safety | REQ-106, REQ-109, REQ-127, REQ-131 through REQ-136 | ADR-106, CMP-107 through CMP-110 | AC-106, AC-109, AC-125, AC-129 through AC-134 | TEST-106, TEST-109, TEST-123, TEST-126 through TEST-130 | GATE-104 |
| OBJ-104 complete free level | REQ-116, REQ-126 | curriculum graph | AC-116, AC-124 | TEST-116, TEST-122, Stage C | free-world release gate |
| OBJ-105 paid family level | REQ-107, REQ-128 through REQ-130 | ADR-107, CMP-109 | AC-107, AC-126 through AC-128 | TEST-107, TEST-124, TEST-125, Stage D | GATE-105 and commerce approval |
| OBJ-106 shortcut academy | REQ-117 | ADR-109 | AC-117 | TEST-117 and binding matrix | post-foundation content gate |
| OBJ-107 representation | REQ-108 | ADR-108 | AC-108 | TEST-108, PLAY-107 | creative/accessibility review |

### F. Finding Counts and Final Audit Verdict

Product/system findings: **8 high, 9 medium, 4 low, 0 critical incidents**. Zero critical incidents does not mean zero critical risk; there is no production system. Template governance findings: **0 high, 5 medium, 3 low**. Template executable audit: pass with two explicitly unmeasured advisory tool checks and no native Buzz claim.

Primary tradeoffs accepted in the proposal are two repositories instead of one, a broader Rust/TypeScript toolchain instead of plugin-only QML, WebKitGTK variability instead of Electron's bundled runtime, local-only progress instead of sync, and slower evidence-driven content expansion instead of immediate full production. These costs are justified by shell containment, child privacy, testability, offline resilience, and the ability to stop before large creative spend if the loop does not work.

Final verdict: **approve discovery, three disposable gameplay proofs, and a separate native-runtime spike after owner review; do not approve a durable vertical slice, full curriculum production, paid implementation, public naming, or release yet.**
