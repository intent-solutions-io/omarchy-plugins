---
blueprint:
  documentId: KTA-ADR-001
  documentType: architecture-decision-record
  schemaVersion: 1.0.0
  templateVersion: 3.0.0
  status: proposed
  owner: Jeremy Longshore
  authors: ["Intent Solutions / Codex"]
  reviewers: []
  approvers: []
  generatedAt: 2026-09-10
  updatedAt: 2026-09-10
  classification: public-draft
  sourceRefs: [KTA-BRIEF-001, KTA-PRD-001, SR-103, SR-104, SR-105, SR-106, SR-111, SR-113]
  assumptions: [A-101, A-105]
  unknowns: [U-101, U-102, U-104, U-107]
  relatedArtifacts: [KTA-ARCH-001, KTA-TEST-001, KTA-RISK-001, KTA-OPS-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure decision records

> These decisions are proposed. `ADR-101` is the recommended product boundary. Framework versions and vendors remain intentionally unpinned until the scaffold spike records compatibility evidence.

## ADR-101: Standalone app plus companion plugin

- Status: proposed
- Chosen: standalone app for the learning game, free Omarchy bar plugin for discovery and launch
- Over: plugin-only game, standalone-only app, browser-only service
- Because: a separate process contains crashes and memory use, supports richer packaging and updates, avoids burdening `omarchy-shell`, and keeps the plugin small enough for marketplace review
- Cost: two release surfaces and a small local integration contract
- Revisit when: Omarchy defines a first-party external-app plugin kind or the companion provides no measurable discovery value

## ADR-102: Tauri 2 native shell

- Status: proposed pending spike
- Chosen: Tauri 2 with a Rust host and a TypeScript frontend
- Over: Electron, pure Qt/QML, Godot, browser-only PWA
- Because: the app needs form-heavy parent screens, testable web UI, a game canvas, local filesystem and SQLite boundaries, signed desktop updates, and a smaller runtime than bundling Chromium
- Cost: Linux WebKitGTK behavior becomes a compatibility surface; Rust and TypeScript increase toolchain breadth; webview behavior differs by platform
- Revisit when: input latency exceeds NFR-101, WebKitGTK rendering fails the minimum device matrix, Tauri packaging is unreliable on Omarchy, or the team chooses game-first tooling over dashboard and testing leverage

### Alternative assessment

| Alternative | Strength | Rejection reason for first slice |
|---|---|---|
| Qt/QML | Native Omarchy fit and existing team patterns | Full app tooling, browser-grade accessibility checks, parent dashboards, and commercial cross-platform path require more custom infrastructure |
| Godot | Excellent game scenes, animation, and editor workflow | Form-heavy parent experience, content tooling, accessibility, and automated UI testing become harder |
| Electron | Mature desktop web ecosystem and uniform Chromium | Runtime size and memory cost are difficult to justify for a child typing app on Linux |
| Browser/PWA | Lowest install friction and easiest web testing | Weaker offline packaging, system integration, commerce entitlement, and Omarchy-native product story |

## ADR-103: React UI plus Phaser scene runtime

- Status: proposed pending slice
- Chosen: React and TypeScript for application UI, Phaser for bounded game scenes
- Over: canvas engine written in-house, DOM-only animation, PixiJS renderer, full Godot client
- Because: React suits parent settings and progress views; Phaser supplies a mature scene, input, audio, WebGL, and Canvas model while allowing the game domain to remain framework-independent
- Cost: coordination between React navigation and Phaser scenes; accessibility mirrors are required for canvas content; Phaser must not own curriculum truth
- Revisit when: three slice scenes are simpler and more accessible using DOM/CSS alone, or Phaser adds more complexity than it removes

## ADR-104: Framework-independent domain core

- Status: proposed
- Chosen: pure TypeScript packages for curriculum, mastery, prompt selection, scoring, session state, and deterministic simulation
- Over: logic inside React components, Phaser scenes, or Rust commands
- Because: the learning rules need fast unit/property tests, deterministic replay, browser preview, and future portability
- Cost: explicit adapters and event schemas are required
- Revisit when: profiling proves a specific domain path must move to Rust, with a differential test retaining behavior

## ADR-105: Local SQLite and bounded append-only session journal

- Status: proposed
- Chosen: SQLite owned by Rust, with one schema and migration authority, transactions, checkpoint-safe backups, and a bounded append-only session journal whose projections update in the same transaction
- Over: JSON files only, browser localStorage, remote database
- Because: multiple profiles, progress queries, migrations, recovery, exports, and transactional integrity outgrow one JSON file; remote storage conflicts with the privacy thesis
- Cost: migration, expected-version, replay, snapshot, compaction, deletion, and native fault-injection discipline
- Revisit when: the free slice proves the data model is small enough for a simpler store or multi-device sync becomes an approved requirement

## ADR-106: Offline-first, no child account

- Status: proposed
- Chosen: learner profiles are local records; the parent purchase exists outside the child profile
- Over: child login, shared cloud profile, social identity
- Because: this minimizes collection, removes account friction, protects play during outages, and narrows COPPA exposure
- Cost: no automatic cross-device sync; device loss can lose progress unless the parent exports it
- Revisit when: parent research shows strong sync demand and a reviewed consent, retention, deletion, security, and recovery design exists

## ADR-107: Signed entitlement, external checkout

- Status: proposed, vendor unresolved
- Chosen: parent buys through an external checkout; the app verifies a signed entitlement document locally
- Over: in-app card collection, child-facing purchase, continuous license-server dependency, honor-only unlock
- Because: it separates payment data from the app, supports offline use, and permits a one-time family license
- Cost: license recovery, key custody, revocation, refunds, and device policy need operations
- Revisit when: merchant-of-record constraints, marketplace rules, or refund economics favor another model

The entitlement payload may include product, edition, issue time, optional expiry or update window, license identifier, and signature. It must not include child profile or typing data. The signing private key must never enter the repository or ordinary developer machines.

## ADR-108: Character customization without curriculum segmentation

- Status: proposed from user direction
- Chosen: equally prominent original heroes, edit, randomize, optional pronouns, and quick-start share all mechanics, themes, worlds, and rewards without requiring a gender category
- Over: separate boys and girls curricula, gendered difficulty, color-locked rewards
- Because: representation supports identification; segmentation creates stereotypes and content drift without learning value
- Cost: more avatar assets and equivalence tests
- Revisit when: research identifies a specific accessibility or representation need, not a marketing stereotype

## ADR-109: Omarchy shortcut training as a later curriculum branch

- Status: proposed
- Chosen: a versioned, opt-in shortcut academy after foundational typing skills
- Over: mixing system shortcuts into the first home-row lessons or globally monitoring child desktop activity
- Because: shortcuts are valuable to Omarchy users but can conflict with typing capture, change between releases, and create privacy concerns
- Cost: compatibility fixtures and ongoing version maintenance
- Revisit when: current Omarchy exposes a stable, queryable training contract or the feature does not improve retention

## ADR-110: Change-scoped quality lanes with a fail-closed release lane

- Status: proposed
- Chosen: path-aware pull-request lanes plus a complete release candidate lane
- Over: running every expensive system test for documentation edits or relying only on a small unit suite
- Because: contributor feedback must be fast while release evidence must be comprehensive and tied to one exact revision
- Cost: path classification itself becomes governed code and must fail closed on ambiguous changes
- Revisit when: the monorepo becomes too large for safe path classification, at which point separate repositories or build graph tooling should replace hand-written rules

### Proposed lanes

| Change class | Required lane |
|---|---|
| Markdown only | markdown lint, links, Blueprint consistency, secret scan |
| Curriculum/content | schema, graph, reading-level report, provenance, unit/property, golden session simulations |
| Web UI/game scene | static, unit/component, browser E2E, accessibility, visual and performance budgets |
| Rust/native/storage | fmt, clippy, unit, integration, migration, security and package build |
| Companion plugin | widget template gates, QML lint, pure model tests, Buzz system lane |
| Release candidate | all applicable lanes, clean Omarchy VM, install/update/rollback, artifact signing, attestation, human approvals |

## ADR-111: Release mutation requires fresh approval

- Status: proposed
- Chosen: automation may prepare commits, artifacts, release notes, submissions, and evidence, but each external release, marketplace submission, paid production change, or public policy publication requires a fresh human approval tied to the exact candidate revision
- Over: blanket standing approval and silent auto-publish
- Because: this adapts Contributing Clanker's authority separation to product release governance
- Cost: more explicit pauses in the release workflow
- Revisit when: a narrowly scoped, auditable delegated authority is formally documented

## ADR-112: Split authentication by trust zone

- Status: proposed
- Chosen: no child login and no free-app login; email-possession verification for parent newsletters and research; parent-controlled merchant or recovery identity for paid Family; signed offline entitlement in the app; unique estate accounts for operators
- Over: one shared account model for parents and children, username/password login inside the game, continuous license-server login, or a local adult gate described as identity authentication
- Because: each surface needs a different level of identity assurance. The split minimizes child data and login friction, preserves offline play, keeps passwords and payment credentials out of the app, and gives operators auditable access.
- Cost: more explicit boundaries, consent states, recovery tests, entitlement operations, and parent explanations
- Revisit when: an approved cross-device sync feature requires a new child-data and guardian-consent architecture

## ADR-113: Twenty for parent relationships, separate local learning data

- Status: proposed pending API and data-model spike
- Chosen: the append-only consent and suppression ledger is authoritative for contact permission; Twenty is a projection and source of truth only for approved verified-parent relationship fields; mail is a delivery projection; local SQLite remains the only learner-progress store
- Over: child accounts in CRM, a marketing database inside the game, browser-to-Twenty credentials, direct writes into Twenty's internal database, or using raw email notifications as the contact record
- Because: Intent Solutions already operates Twenty, Jeremy needs contacts he can actually use, and a narrow adapter avoids duplicating a full CRM while preserving an auditable consent history
- Cost: a small online service, field governance, deduplication, consent reconciliation, backup, monitoring, and API compatibility work
- Revisit when: Twenty cannot represent the approved consent contract reliably or a managed email/CRM vendor materially reduces risk without expanding child data

No send may occur unless the current authoritative consent projection permits it. A transactional event-plus-outbox commit, at-least-once delivery, unique idempotency keys, projector cursors, replay and rebuild, and bounded convergence are required. Unverified addresses remain outside Twenty until email possession is verified.

## ADR-114: Shared production VPS for the small parent service only

- Status: proposed after read-only capacity snapshot; deployment not approved
- Chosen: signed game artifacts and update metadata use static release distribution. The parent signup, consent, and later entitlement surfaces may use the shared `intentsolutions` VPS after a production readiness and capacity gate. Buzz and `team-server` are excluded.
- Over: hosting the app as an always-running web game, exposing the development machine, placing unrelated product workloads on the dedicated Buzz host, or buying another server before measured need
- Because: the desktop game does not need server runtime, the shared VPS already owns customer-facing services and Twenty, and the 2026-09-10 snapshot showed 147 GB disk and about 16 GiB memory available with low observed CPU use
- Cost: another small service shares an existing failure domain and must carry limits, health, backup, restore, alerting, and rollback
- Revisit when: sustained load, backup growth, commerce criticality, security isolation, or incident blast radius crosses the approved separation trigger

## ADR-115: Prove gameplay before production architecture

- Status: proposed from adversarial review
- Chosen: test three disposable 3 to 5 minute typing-as-game mechanics and a separate minimal native runtime spike before durable profiles, production persistence, parent service, companion, commerce, or full-world production
- Over: treating a complete app-shaped vertical slice as the first gameplay experiment
- Because: the most expensive failure is a polished worksheet whose typing only triggers decoration
- Cost: early code may be deliberately discarded and delivery estimates wait for evidence
- Revisit when: the selected greybox passes pre-registered causal-loop, replay, frustration, mashing, accessibility, and learning-safety gates

## ADR-116: One package and update authority per format

- Status: unresolved, blocking production foundation
- Required decision: choose exactly one update authority for each package format, with signed artifacts and metadata, channels, prior-binary retention, executable-by-schema compatibility, downgrade rules, and a usable recovery build
- Constraint: an Arch or pacman-owned package must not also be silently replaced by an app updater; export is recovery, not rollback
- Evidence owner: release engineering and security
- Bead: `bd_000-projects-v41u.4.11`

## ADR-117: Free first, merchant-of-record candidate later

- Status: free boundary decided; paid vendor unresolved
- Chosen for v1.0: no payment provider, checkout, paid service, or production entitlement dependency
- Leading v1.1 candidate: Lemon Squeezy, compared in sandbox with Paddle; Stripe Managed Payments is a fallback
- Because: a merchant of record narrows global tax, fraud, dispute, and transaction-support burden, while Lemon Squeezy currently documents one-time digital products, license keys, downloads, webhooks, and 5 percent plus $0.50 headline pricing
- Constraint: provider approval does not authorize the app. A verified webhook drives an Intent Solutions signed offline entitlement, with no child data and an explicit permanent-offline versus revocation policy
- Evidence: KTA-COMMERCE-001 and `bd_000-projects-v41u.1.8`

## ADR-118: Select The Beacon Wakes subject to clearance

- Status: owner-selected creative title; publication clearance pending
- Grok round leader: `Ninewire`
- Grok round runner-up: `Mapwire`
- Rejected as master brands: `OmaQuest`, `omaType`, and `Rover & Relay`
- Because: `OmaQuest` and `omaType` have direct product collisions. The independent Grok review found that `Rover Relay` is already the name of a NASA and Tynker K-12 coding activity involving robotic rovers, which is too close to this product's audience, mechanic, and first mission. Grok scored `Ninewire` highest for distinctiveness, pronunciation, hardware expansion, and story potential, with `Mapwire` as the more literal but less distinctive fallback.
- Later naming-strategy correction: the master name should primarily invite a child into an ownable world, toy, character, or game identity. It does not need to explain typing, education, or the first machine. `Dabble` expresses the broader product behavior well, but the exact mark is rejected for this project because active Dabble products already occupy robotics and STEM control, children's learning and kits, creative apps, word games, learning experiences, and sports betting. The conceptual lesson is retained without adopting the crowded name.
- Superseded provisional challenger: `Tinkdab` originally advanced because it was coined, playful, and usable across game titles and physical boxes. The owner later clarified that the product is universal typing and computer fluency, while coding, robotics, sports, music, art, and other topics are optional worlds. `Tinkdab` is therefore demoted to retained research input because `Tink` pre-classifies the product as maker or STEM content and remains close to Autodesk `Tinkercad` and the crowded `Tinker` education category.
- Brand architecture: Intent Solutions is the master company brand. The child-facing name is an endorsed product brand, expressed as `NAME by Intent Solutions`, not a replacement umbrella or additional studio. Intent Solutions leads parent trust, commerce, privacy, safety, licensing, and support; the product name leads the child's world, characters, gameplay, and packaging.
- Thinker-canon council challenger: three independent child-experience, international, and commercial brand councils converged on a short, invented, gender-neutral world name that does not imply typing, coding, robotics, STEM-only learning, or one culture. `Rilo` is rejected because an active child-focused communication product uses the name. `Farlo` is rejected because an active subscription mobile application uses the exact software name. `Niveri` is the strongest surviving research challenger from this round, with no obvious current game, children's education, or major software collision in a preliminary web screen. It is not approved and must pass pronunciation, hear-and-spell, meaning, age-band, international-language, legal, domain, handle, app-store, and parent-trust testing.
- Nostalgia boundary: retain the emotional inheritance of classic typing tutors through an original beacon, lost-signal, mentor, or generational-guidance story. Do not use `Mavis`, `Mavis Beacon`, the Mavis persona or likeness, `Return of Mavis`, copied trade dress, or official-successor language without a license. `MAVIS BEACON` remains an active educational-software mark and current products remain commercially available. A beacon may be a subordinate original story object or mission, subject to title and trademark review, rather than the master product brand.
- Owner decision: select `The Beacon Wakes` as the child-facing product title, endorsed as `by Intent Solutions`. Retire `Niveri` from the lead position. The exact phrase becomes the product and story identity rather than a subordinate working subtitle.
- Preliminary exact-title screen, 2026-09-10: no obvious exact game, educational software, book, film, or GitHub repository appeared. Verisign RDAP returned HTTP 404 for `thebeaconwakes.com`, indicating no registry record at the time checked. A separate active autonomous-agent project uses `Beacon Wake`, so confusing-similarity and mark-strength review remain required. These transient checks do not reserve a domain or constitute legal clearance.
- Constraint: the Grok result is a preliminary collision screen, not trademark clearance. Do not rename public repositories, publish listings, buy advertising, print kit packaging, or lock executable and application identifiers until the owner approves a candidate after counsel completes a knockout and comprehensive search.
- Required search: `THE BEACON WAKES`, `BEACON WAKES`, `BEACON WAKE`, confusingly similar marks, relevant common-law uses, domains, and handles, including Classes 9, 28, 41, and 42 where applicable
- Evidence: KTA-BUILD-001 and `bd_000-projects-v41u.1.2`

## ADR-119: Reuse the existing Oma site for a lean sales path

- Status: proposed option, not a vendor or launch approval
- Chosen if a paid pilot is authorized: use `oma.intentsolutions.io/<approved-product-slug>` as the product landing page and send the parent to one provider-hosted checkout
- Over: buying a separate domain before naming clearance, building a second full website, hosting the desktop game as a web service, or building a custom order database for the first sale
- Leading provider: Lemon Squeezy, subject to the existing Paddle comparison and all KTA-COMMERCE-001 gates
- Because: the existing GitHub Pages site can own product explanation and discovery while the merchant of record can host checkout, tax handling, receipts, downloadable files, and license keys. The current 125 MB AppImage fits Lemon Squeezy's documented product-file allowance.
- Trial split: a no-card seven-day local trial cannot auto-charge. An auto-charging seven-day trial requires a subscription checkout with payment details before play and lifecycle integration. The owner must choose which parent experience is intended.
- Integration boundary: direct provider-key activation is simpler but introduces periodic vendor validation for subscription state. Retaining the current Intent Solutions signed offline entitlement requires a verified webhook and signer, or a bounded manual issuance process for an early pilot. Neither path is implemented or approved for production.
- Domain decision: no new domain is technically required. A defensive product domain may be considered only after the public name survives legal and collision review.
- Evidence: KTA-COMMERCE-001, KTA-BUILD-001, and `bd_000-projects-v41u.1.8`

## ADR-120: Stabilize the existing Electron implementation before reconsidering the runtime

- Status: selected for the next bounded engineering iteration; not a permanent framework commitment
- Chosen: continue the existing Electron, Vite, TypeScript, Canvas 2D, and Web Audio implementation through the first-chapter stabilization gate
- Over: restarting immediately in the proposed Tauri, React, Phaser, Rust, and SQLite architecture
- Because: a working local app and packaged AppImage already exist, while no measured reliability, accessibility, size, performance, or distribution result currently justifies paying the rewrite cost before the gameplay and learning unit are proven
- Required fixes before release: safe input and focus handling, a complete untimed path, corrected contrast, explicit adult navigation, strict entitlement schemas, atomic local persistence, packaged-native tests, and one finished first chapter
- Revisit trigger: measured Electron failure against an approved platform requirement, or completion of the first-chapter evidence package with a favorable rewrite comparison
- Evidence: KTA-ASTRA-001 and `bd_000-projects-v41u.1.15`

## ADR-121: Separate the permanent teaser, downloadable trial, and later Family platform

- Status: recommended commercial boundary; owner decision remains open for the purchase model and the meaning of the larger permanent free world
- Chosen for build planning: keep the Omarchy teaser permanently free, offer a no-card seven-day trial of one completed downloadable chapter, and prepare a parent-only path for a one-time permanent chapter unlock
- Deferred: subscription access, recurring content promises, mailed kits, multiple family profiles, and the broader Family platform
- Because: the split can create a small honest paid unit without forcing checkout, accounts, or commerce into child play, while leaving the larger curriculum and physical-kit program to earn their own evidence
- Constraint: REQ-126 and AC-124 still require a coherent permanent free world. The owner must explicitly decide whether that means a larger desktop world, the permanent teaser as a revised free level, or a separately scoped paid pilot before the requirements are changed or payment is enabled
- Marketing boundary: if the chapter supplies practice rather than a complete beginner sequence, call it a typing-practice adventure, not a complete touch-typing course
- Evidence: KTA-ASTRA-001, KTA-COMMERCE-001, and `bd_000-projects-v41u.1.8`

## ADR-122: Make parent onboarding a free ungated product layer

- Status: owner-directed product requirement; implementation and usability evidence pending
- Chosen: publish a free `Parent Launch Guide` and a child-facing `Light the Beacon Together` opening that a parent and child can begin in under ten minutes
- Required content: invitation rather than coercion, child choice, accuracy before speed, calm modeling of mistakes, breaks and positive stopping, resistance guidance, accessibility adaptations, and an optional seven-day family rhythm without streak pressure
- Data boundary: the core guide requires no signup. No child identity, interests, responses, or performance enters Twenty or another online system. A parent may separately choose a clearly labeled adult newsletter signup
- Because: distribution depends partly on helping adults create a safe first experience, especially when they do not know how to teach typing or expect the child to resist another exercise
- Evidence required: qualified learning and child-safety review plus parent usability tests showing the approach can be understood without staff coaching
- Evidence: KTA-ASTRA-001 and `bd_000-projects-v41u.2.16`

## Decision criteria and weights

Consequential alternatives are scored before approval. A numeric score informs judgment but does not override a child-safety, legal, security, rights, or release blocker.

| Criterion | Weight | Question |
|---|---:|---|
| Child safety and data minimization | 25 | Does the choice prevent unnecessary child identity, tracking, pressure, or disclosure? |
| Offline resilience and learner usability | 20 | Does play continue safely through network, service, and account failure? |
| Security and failure blast radius | 15 | What can one compromised client, token, dependency, database, or host affect? |
| Public verifiability and maintainability | 15 | Can skeptical contributors inspect, reproduce, test, and support the claim? |
| Operational reuse and recovery | 15 | Does it fit owned infrastructure, identity, backup, monitoring, and rollback practices? |
| Cost and delivery time | 10 | What build, vendor, support, and ongoing operating cost follows? |

Every ADR also records assumptions, alternatives, failure behavior, evidence required to select it, owner, and revisit trigger. Legal obligations and measured platform failures remain hard constraints regardless of weighted score.
