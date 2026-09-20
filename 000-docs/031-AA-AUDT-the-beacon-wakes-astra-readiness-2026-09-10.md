---
blueprint:
  documentId: KTA-ASTRA-001
  documentType: adversarial-readiness-audit
  schemaVersion: 1.0.0
  templateVersion: 3.0.0
  status: completed
  owner: Jeremy Longshore
  authors: ["Intent Solutions / Codex"]
  reviewers: ["gpt-6-astra blueprint auditor", "gpt-6-astra plugin auditor", "gpt-6-astra visual and commercial director"]
  approvers: []
  generatedAt: 2026-09-10
  updatedAt: 2026-09-10
  classification: internal-review
  sourceRefs: [KTA-BRIEF-001, KTA-PRD-001, KTA-ADR-001, KTA-ARCH-001, KTA-UX-001, KTA-AC-001, KTA-TEST-001, KTA-OPS-001, KTA-PROGRAM-001, KTA-BUILD-001]
  assumptions: []
  unknowns: [U-ASTRA-101, U-ASTRA-102, U-ASTRA-103]
  relatedArtifacts: [KTA-RECON-001, KTA-COMMERCE-001]
  reviewDate: 2026-09-10
  supersedes: []
  humanReview:
    required: true
    status: in-progress
---

# The Beacon Wakes Astra readiness council

## Executive verdict

`The Beacon Wakes`, by Intent Solutions, has a real local Electron prototype and a real local Omarchy teaser. The product is ready for a bounded engineering iteration. It is not release-ready, paid-ready, or production-ready. The teaser's feature scope should freeze now, but its release bytes cannot freeze until branding, contrast, parent handoff, and complete install-to-remove evidence are corrected.

The highest-value next action is stabilization, not expansion. Retain Electron for the next slice, make one Beacon mission genuinely accessible and causally satisfying, build one finished first chapter, and treat the Omarchy plugin as a permanently free playable teaser. Do not begin a framework rewrite, subscription platform, full curriculum, hardware subscription, or additional teaser missions.

## Review constitution and receipts

Three independent read-only agents ran with model `gpt-6-astra` and high reasoning effort:

| Review | Scope | Mutation boundary |
|---|---|---|
| `astra_blueprint_readiness` | complete Blueprint 014 through 030, Beads, app, teaser, plan-versus-actual reconciliation | no file, Beads, Git, release, or external mutation |
| `astra_plugin_lock` | teaser source, tests, gates, evidence, marketplace state, identity, lifecycle, and product handoff | no edits, installation, submission, or publication |
| `astra_visual_commerce` | app and teaser visuals, accessibility, Intent relationship, screenshots, trailer, and lean commercial offer | no edits, payment configuration, or external mutation |

Durable project definitions were created as `.claude/agents/beacon-blueprint-auditor.md`, `.claude/agents/beacon-plugin-release-auditor.md`, and `.claude/agents/beacon-visual-commercial-director.md`. Their portable model field is `inherit`; `gpt-6-astra` is a Codex runtime identifier and is not written as invalid Claude frontmatter.

## Candidate identities inspected

| Surface | Identity | Observed state |
|---|---|---|
| Blueprint | `docs/typing-adventure-blueprint`, base `e87598458d89aeb6ff45b33eaf3d714ebe348971` plus current working changes | extensive draft authority, not a committed freeze |
| Standalone app | `/home/jeremy/000-projects/omarchy-typing-adventure`, `feat/two-minute-demo`, `2d4c8fab59fa264691571c16e8d579520dbf82b1` | clean local Electron prototype, no configured Git remote |
| Omarchy teaser | `/home/jeremy/000-projects/omarchy-omaquest-entry`, `feat/omaquest-teaser`, `97cdb6b60a90d9b656a6149c57a7fb63bc2fc2b5` | clean local QML teaser, no configured Git remote |
| AppImage | 125,236,660 bytes | SHA-256 `5e2b8deee88852961fc6c24ce32f997dfd0f881d32bd9384bc80b10a3c69320c` matches the retained receipt |

The closed expedited Beads `bd_000-projects-v41u.12` and `.13` remain valid historical receipts for a local app prototype and local teaser. They did not authorize publication and do not prove the larger free-world, marketplace, paid, or production program.

## Readiness matrix

| Stage | Verdict | Reason |
|---|---|---|
| Local app prototype | complete for its bounded historical scope | executable Electron loop, AppImage, narrow automated tests, and retained smoke receipt exist |
| Local teaser | complete for its bounded historical scope | three-transmission QML game and strong local test evidence exist |
| Next MVP engineering iteration | ready | current code provides a usable baseline; blockers are explicit and bounded |
| Visual prototype | conditional | coherent direction exists, but contrast and input defects must be corrected before child evaluation |
| Teaser release candidate | not locked | visible branding, contrast, live parent destination, and full lifecycle evidence remain incomplete |
| Paid first chapter | not ready | content value, adult boundary, entitlement schema, delivery, policies, recovery, and normal-runtime evidence remain incomplete |
| Marketplace submission | not ready | public repository and listing do not exist; the linked parent page returns HTTP 404 |
| Production | not ready | signing, updates, rollback, support, accessibility, rights, privacy, and release evidence remain incomplete |

## P0 findings

### P0-1: Blueprint authority is stale

The Blueprint still describes future repositories and a Tauri, React, Phaser, Rust, and SQLite target. The actual app is Electron, Vite, TypeScript, Canvas 2D, Web Audio, local access files, and largely in-memory gameplay. The actual teaser is a playable QML game, not the planned launch, resume, and summary companion.

The correction is to document actual baseline plus proposed target deltas. Electron remains the approved next-iteration runtime because an expedited owner-authorized implementation exists and no measured evidence justifies a rewrite. Tauri remains a possible future alternative, not a compulsory prerequisite.

### P0-2: Free and paid product boundaries conflict

REQ-126 and AC-124 specify a permanent coherent free world. The app implements an expiring seven-day trial and paid unlock interface. The teaser provides permanent free play, but it is not the complete beginner curriculum described by the requirement.

The recommended resolution is two explicit tracks:

1. a permanent free Omarchy teaser with one complete Beacon Nine mission;
2. a downloadable first chapter with a no-card seven-day trial and, after commerce readiness, a one-time chapter purchase.

The larger permanent free learning world and later Family product remain separate roadmap decisions. This structure may generate modest early revenue without representing the current two-minute prototype as a finished paid product.

### P0-3: Gameplay captures keyboard navigation

The app prevents default behavior for every unmodified gameplay key, including Tab and Escape. It has no complete blur, composition, repeat, or trusted-event policy. Time-based act changes can replace partially typed prompts.

The next slice requires a pure session and input state machine, pause on focus loss, keyboard-reachable pause and exit, untimed completion, explicit repeat and composition behavior, and packaged Electron tests.

### P0-4: Parent-facing labels are not an adult transition

Expired-trial purchase and license import controls appear automatically. Completion exposes an external project link. The teaser opens its continuation URL after a single completion key. A label containing the word `Parent` is not a navigation safeguard.

The next slice requires one documented adult transition pattern, no checkout or countdown during active child play, failure-safe external navigation, and end-to-end tests for every child-reachable route. It must not be described as identity or age verification.

### P0-5: Release evidence overstates native coverage

The app's Electron test imports an access module; it does not exercise the Electron application. Browser E2E runs the Vite preview. Current capture tooling accelerates the game and shortens success to one prompt. No configured Git remote exists, so workflow definitions do not prove hosted CI enforcement.

Native packaged input, access, lifecycle, performance, install, rollback, and failure evidence must be added before release claims. Prototype screenshots remain valid only when labeled as accelerated development evidence.

### P0-6: The teaser's public continuation is broken

`https://oma.intentsolutions.io/omaquest` returned HTTP 404 during the review. No public GitHub repository or live marketplace entry was found for OmaQuest. The local teaser is demonstrable, but not a working acquisition funnel.

The parent page must be created and verified, or the continuation action must be removed from the release candidate. The public page cannot promise download, checkout, kits, platforms, or support that do not exist.

## P1 findings

- Trial and entitlement files use non-atomic writes and broad silent recovery. The verifier accepts signed but semantically invalid dates and unknown editions. Add bounded schemas, atomic writes, explicit recovery, and main-preload-import integration tests.
- The three app trails primarily change words, route color, and geometry. They are presentation variants, not three proven game mechanics or worlds.
- The first frame is visually coherent but resembles an expedition dashboard more than an inhabitable world. Invest next in one original environment, companion, two consequential routes, and three visible restoration states.
- Teaser rig receipts bind source `aa1fdce`, while current HEAD is `97cdb6b`. Later differences are evidence and documentation files, but candidate equivalence must be explicit or the rig rerun.
- The plugin's legacy Wave 5 companion epic requires no game and launch, resume, and summary behavior. The completed playable teaser is a different product. Preserve both histories and do not close one with the other's evidence.

## Plugin freeze contract

Feature scope freezes now:

- visible title `The Beacon Wakes`, mission subtitle `Beacon Nine`, endorsement `by Intent Solutions`;
- one original mission and three fixed transmissions;
- correct-character progression, visible accuracy effect, completion, replay, and close;
- pure QML and JavaScript with no app dependency, account, save file, child data, analytics, payment, updater, or gameplay network;
- one completion-only parent destination carrying no identity or gameplay payload;
- no additional missions, profiles, curriculum, audio, timers, kits, daily summary, or deep linking before the release candidate.

Release bytes freeze only after contrast, identity, destination, keyboard journey, focus restoration, install, reopen, remove, reinstall, browser-failure, screenshot, cast, hash, and candidate receipts pass on a named supported Omarchy environment.

The current internal repository slug and module identifier may remain stable during stabilization. No public listing identity exists to migrate. Public display copy must not retain OmaQuest as a competing brand. Do not shorten the title to bare `Beacon`, which is already used by an unrelated Omarchy listing.

## Visual direction

The selected direction is a natural living landscape awakened by signals. Natural color belongs to The Beacon Wakes product, not as a claimed universal Intent Solutions mandate. Intent continuity comes from the company endorsement, precise typography, disciplined composition, and ember energy.

| Role | Candidate token | Purpose |
|---|---|---|
| Forest ink | `#18221B` | primary text, prompt surface, outlines |
| Warm paper | `#F4EEDC` | reading panels and inverse prompt text |
| Moss | `#315B46` | terrain and secondary structures |
| Intent ember | `#F97316` | beacon energy and action fill with forest text |
| Signal teal | `#086976` | small information and action text on paper |
| Beacon gold | `#F4C542` | current character and completion energy on dark surfaces |
| Correction | `#A43D2B` | error or repair state on paper, always paired with shape and instruction |

Token calculations produce paper on forest 14.11:1, forest on ember 5.84:1, dark teal on paper 5.50:1, and gold on forest 10.06:1. These are starting calculations, not screen certification. The existing app and teaser contain several 1.40:1 to 4.34:1 functional combinations that fail the normal-text or focus target.

Retain Atkinson Hyperlegible for narrative and accessible prompt options. Remove negative letter spacing from the typing line. Limit condensed display type to short titles. During missions, the world should occupy most of the screen and the opaque typing strip should remain stable. Immediate typed input changes a meaningful state; a short signal and 0.6 to 1.2 second restoration beat follows completed action. Reduced motion uses a state transition without travel, shake, flash, or perpetual decoration.

## Lean commercial boundary

The first monetizable unit should be one finished chapter, not the full future Family platform:

- permanent free Omarchy teaser;
- no-card seven-day trial of the actual downloadable chapter;
- approximately six short authored missions across a few reviewed skill groups;
- one environment, one companion, alternate routing, and a final restoration;
- pause, untimed play, readable correction, local checkpoint and deletion;
- one-time purchase permanently unlocks that chapter;
- parent-only hosted checkout and signed offline entitlement import after operational approval.

Six missions is a build hypothesis, not proof of sufficient curriculum or value. If the chapter provides practice but not full beginner instruction, market it as a typing-practice adventure rather than a complete touch-typing course. Do not promise subscription cadence, physical kits, Windows or macOS, global keyboard layouts, AI companions, learning outcomes, or future chapters before they exist.

## Free parent education layer

The free product is also responsible for helping a parent introduce typing without turning it into punishment, surveillance, or another homework conflict. The working package is a freely accessible `Parent Launch Guide` plus a child-facing `Light the Beacon Together` first-session option.

The minimum free package contains:

- a one-page quick start and a five-minute parent lesson;
- language for inviting rather than ordering a child to play;
- child choice of interest world, pace, and whether to continue;
- accuracy, strategy, and persistence before speed;
- modeling mistakes calmly and avoiding comparison with siblings or classmates;
- clear frustration, break, and stopping guidance;
- adaptations for reading, motor, attention, sensory, and keyboard-layout needs without diagnosis claims;
- a short first mission a parent and child can begin together, followed by child control;
- an optional seven-day family rhythm with no streak punishment;
- separate, optional adult newsletter consent.

The core guide must not require an email address. No child data, responses, interests, performance, or identity enters Twenty or another online system. A parent may separately opt into product updates or the Friday letter through the governed parent-only consent flow. The guide's learning and motivation claims require qualified review and parent usability evidence. Tracking: `bd_000-projects-v41u.2.16`.

## Ordered build gate

1. Reconcile Blueprint and Beads against the existing Electron app and playable teaser.
2. Stabilize the app's input, untimed path, contrast, parent boundary, access schema, and native evidence.
3. Define and build one finished first chapter with honest practice-versus-instruction positioning.
4. Create the working parent page and support, privacy, platform, trial, purchase, and limitation copy.
5. Apply The Beacon Wakes identity and contrast corrections to the teaser.
6. Run complete teaser lifecycle evidence and freeze one candidate.
7. Configure commerce only after seller, provider, terms, refund, entitlement, recovery, signing, and delivery operations are approved.
8. Publish only after a separate exact-candidate decision.

## Beads disposition

| Bead | Disposition |
|---|---|
| `bd_000-projects-v41u.12` | retain closed as bounded local Electron MVP receipt |
| `bd_000-projects-v41u.13` | retain closed as bounded local teaser receipt, with non-public limitations |
| `.1.2` | keep open for clearance and public identifiers; creative title is settled |
| `.1.12` | reconcile all stale future-repository, Tauri-only, no-implementation, free-only, and companion-only statements |
| `.2.5`, `.2.11`, `.5.2` | own layout, focus, Tab, Escape, blur, composition, repeat, untimed, contrast, and assistive paths |
| `.2.10` | treat the existing trails as a baseline, not proof of three meaningful mechanics |
| `.2.12` | govern claims about worlds, typing instruction, accessibility, kits, trial, and screenshots |
| `.2.16` | design and validate the ungated Parent Launch Guide and first-session co-play |
| `.4.4`, `.6.1`, `.6.2` | own the natural-plus-signal design, first environment, companion, tokens, contrast, art, fonts, and provenance |
| `.4.8` through `.4.10` | re-audit and implement actual Electron and packaged-native test gaps |
| `.4.14` | execute the bounded Electron stabilization and first-chapter baseline after this council closes |
| `.8` | retain as deferred launch, resume, and summary companion unless explicitly re-scoped |
| `.8.4`, `.8.5` | use only after their dependency and scope reconciliation; do not inherit teaser evidence silently |
| `.8.8` | freeze the exact playable teaser candidate after the working parent handoff exists |
| `.1.8`, `.10.5`, `.11.1` through `.11.4` | reconcile the early one-time chapter option against the free-first Family roadmap before commerce work |
| `.3.9` | replace the broken parent destination with a tested, truthful handoff and free-guide entry point |

## Unknowns requiring owner or specialist disposition

- `U-ASTRA-101`: approve one-time first-chapter purchase after a no-card trial, or retain subscription as the first paid model.
- `U-ASTRA-102`: decide whether the larger permanent free world remains a later product commitment or whether the permanent Omarchy teaser becomes the defined free level.
- `U-ASTRA-103`: decide whether the legacy launcher and summary companion remains a later separate plugin feature or is retired in favor of the playable teaser.

## Council conclusion

Proceed with a bounded stabilization and first-chapter build. Do not rewrite frameworks. Do not add worlds before one world feels alive. Do not enable payment before the paid unit and parent operations exist. The natural palette is directionally right, with darker semantic text and brighter controlled beacon energy. The plugin is scope-locked but not release-locked.
