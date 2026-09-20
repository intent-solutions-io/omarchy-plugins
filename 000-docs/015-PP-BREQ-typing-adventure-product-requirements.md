---
blueprint:
  documentId: KTA-PRD-001
  documentType: product-requirements
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
  sourceRefs: [KTA-BRIEF-001, SR-102, SR-107, SR-110, SR-113]
  assumptions: [A-101, A-102, A-103, A-104, A-105]
  unknowns: [U-101, U-102, U-103, U-104, U-105]
  relatedArtifacts: [KTA-ADR-001, KTA-ARCH-001, KTA-UX-001, KTA-PRIV-001, KTA-AC-001, KTA-TEST-001, KTA-PLAY-001, KTA-RISK-001, KTA-OPS-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure product requirements

> Requirements are proposed until human approval. Numeric thresholds are design targets, not measured results.

## Product promise

The product is designed to help a child practice touch typing by controlling an original adventure. No public learning-outcome claim is permitted until the specified evidence, retention, transfer, and qualified-review gates pass. A parent can understand progress and later buy expanded curriculum without creating a child account.

The current Electron prototype and playable Omarchy teaser are implementation baselines, not evidence that the full requirement set is complete. The expedited build lane keeps the teaser permanently free, stabilizes one downloadable first chapter for a no-card seven-day trial, and prepares a parent-only one-time unlock path. This lane does not silently supersede REQ-116 or REQ-126. Before payment is enabled, the owner must decide whether the permanent free world remains a larger desktop commitment or whether the permanent teaser becomes a formally revised free level, then update the linked acceptance and test contracts together.

Parent education is part of the free trust layer. The core `Parent Launch Guide` and `Light the Beacon Together` first-session flow shall be useful without signup, collect no child data, and keep any adult newsletter opt-in separate. Detailed acceptance remains tracked by `bd_000-projects-v41u.2.16` and ADR-122.

## Requirement registry

### Product and platform

| ID | Requirement | Priority | Verification |
|---|---|---:|---|
| REQ-101 | The complete learning game shall run as a standalone desktop process. | P0 | AC-101, TEST-101 |
| REQ-102 | The first production target shall be x86_64 Arch Linux on a named Omarchy baseline. | P0 | AC-102, TEST-102 |
| REQ-103 | A separate free companion plugin shall launch/resume the app and show only bounded local summary data. | P1 | AC-103, TEST-103 |
| REQ-104 | The app shall remain fully usable without the plugin. | P0 | AC-104, TEST-104 |
| REQ-105 | The plugin shall not silently install, update, purchase, or execute arbitrary app content. | P0 | AC-105, TEST-105 |

### Learners and profiles

| ID | Requirement | Priority | Verification |
|---|---|---:|---|
| REQ-106 | The free level shall support one local learner profile without requiring real name, birth date, email, photo, or voice. | P0 | AC-106, TEST-106 |
| REQ-107 | Paid family mode shall support at least four local profiles. | P1 | AC-107, TEST-107 |
| REQ-108 | A learner may choose among equally prominent original heroes, edit or randomize interchangeable appearance features, use optional pronouns, or quick-start without selecting a gender category. Presentation never changes curriculum, rewards, difficulty, or available colors. | P0 | AC-108, TEST-108 |
| REQ-109 | Parent-controlled actions shall be separated from child play by a documented adult gate that does not claim to prove identity unless it actually does. | P0 | AC-109, TEST-109 |
| REQ-110 | Parent mode shall expose export, reset, and complete local deletion for every learner profile. | P0 | AC-110, TEST-110 |

### Curriculum and mastery

| ID | Requirement | Priority | Verification |
|---|---|---:|---|
| REQ-111 | Curriculum content shall be versioned data, reviewed separately from engine code, with unique skill, lesson, prompt, and mission IDs. | P0 | AC-111, TEST-111 |
| REQ-112 | Each lesson shall declare prerequisites, target keys, allowed keys, reading level, prompt source, mastery rule, accessibility notes, and free/paid entitlement. | P0 | AC-112, TEST-112 |
| REQ-113 | Mastery shall prioritize accuracy and technique before speed. | P0 | AC-113, TEST-113, PLAY-103 |
| REQ-114 | The engine shall distinguish character meaning from physical key position and shall record the active keyboard-layout assumption. | P0 | AC-114, TEST-114 |
| REQ-115 | Repeated key, modifier, composition, dead-key, focus-loss, paste, synthetic-event, and input-method cases shall have explicit policies. | P0 | AC-115, TEST-115 |
| REQ-116 | The permanent free world shall provide a coherent beginner sequence through lowercase and uppercase letters, space, Enter, Shift, numerals, and essential sentence punctuation across the number of lessons approved by curriculum and playtesting. | P0 | AC-116, TEST-116 |
| REQ-117 | The paid curriculum may add advanced punctuation and symbols, sustained fluency, code-like patterns, and Omarchy shortcuts only when prerequisites are satisfied. | P1 | AC-117, TEST-117 |
| REQ-118 | Essential correction and basic adaptive practice shall be included free, derived locally from error patterns, and explainable to a parent and learner. Paid mode may deepen adaptation but may not withhold needed remediation. | P0 | AC-118, TEST-118 |
| REQ-119 | Lesson selection shall avoid trapping a learner in an impossible or monotonous loop. | P0 | AC-119, TEST-119 |

### Game experience

| ID | Requirement | Priority | Verification |
|---|---|---:|---|
| REQ-120 | Typing shall directly control meaningful mission actions, and original challenge clarity, escalating world change, and creator-like agency shall remain understandable without reference-brand explanation. | P0 | PLAY-101, PLAY-102, PLAY-112 |
| REQ-121 | The first playable slice shall contain an onboarding scene, a teach scene, a practice scene, a mission, a boss or set-piece, and a calm results scene. | P0 | AC-120, PLAY-104 |
| REQ-122 | A normal session shall support a satisfying stopping point within 10 to 20 minutes, with stop, replay, and alternate choices presented without streak loss, urgency, randomized rewards, or facilitator pressure. | P0 | PLAY-105, PLAY-112 |
| REQ-123 | Incorrect input shall produce specific, brief coaching and never ridicule, public ranking, loss of purchased access, or permanent punishment. | P0 | AC-121, PLAY-106 |
| REQ-124 | Difficulty shall adjust through prompt length, pace, assistance, and mastery spacing, not hidden accuracy inflation or impossible timers. | P0 | AC-122, TEST-120 |
| REQ-125 | Story, character, art, audio, lesson text, challenge framing, and product presentation shall be original or supported by documented redistribution rights, with no copied identity, likeness, trade dress, or implied endorsement. | P0 | AC-123, TEST-121 |

### Free and paid boundary

| ID | Requirement | Priority | Verification |
|---|---|---:|---|
| REQ-126 | Free access shall be permanent and contain one coherent world rather than a timed trial. | P0 | AC-124, TEST-122 |
| REQ-127 | The child play surface shall contain no price, checkout, advertising, upsell countdown, or purchase requirement. | P0 | AC-125, TEST-123 |
| REQ-128 | Paid entitlement shall be acquired through a parent-only external flow and verified locally using a signed, non-secret entitlement artifact. | P1 | AC-126, TEST-124 |
| REQ-129 | Loss of network or licensing service shall not remove already unlocked local access during the documented entitlement validity period. | P1 | AC-127, TEST-125 |
| REQ-130 | Refund, transfer, device limit, recovery, and support rules shall be published before accepting payment. | P0 for commerce | AC-128, CTRL-109 |

### Privacy, safety, and accessibility

| ID | Requirement | Priority | Verification |
|---|---|---:|---|
| REQ-131 | Gameplay, learner progress, and error history shall remain local by default and shall not be transmitted. | P0 | AC-129, TEST-126 |
| REQ-132 | Initial release shall contain no third-party analytics, crash-report upload, advertisements, chat, social graph, public profile, or push-notification engagement system. | P0 | AC-130, TEST-127 |
| REQ-133 | The app shall publish an accurate data inventory and child-appropriate privacy explanation plus a parent-facing policy. | P0 | AC-131, CTRL-101 through CTRL-110 |
| REQ-134 | All menus and non-timing learning functions shall be keyboard operable without a keyboard trap. | P0 | AC-132, TEST-128 |
| REQ-135 | Reduced motion, pause, adjustable audio, readable type, color-independent feedback, and a complete untimed playable path shall be available across the free world. | P0 | AC-133, TEST-129 |
| REQ-136 | The product shall avoid rapid flashing and shall document animation, sound, and timing safety limits. | P0 | AC-134, TEST-130 |

### Persistence, updates, and operations

| ID | Requirement | Priority | Verification |
|---|---|---:|---|
| REQ-137 | Local state shall use versioned schemas, atomic writes, a last-good backup, migrations, and a documented storage location. | P0 | AC-135, TEST-131 |
| REQ-138 | Corrupt, future-version, read-only, full-disk, and interrupted-write cases shall fail without silent data loss. | P0 | AC-136, TEST-132 |
| REQ-139 | Release artifacts and updater metadata shall be signed and tied to an exact source revision and dependency lock. | P0 | AC-137, TEST-133 |
| REQ-140 | Update checks shall occur only from a documented parent-facing or neutral app flow and shall never disclose learner data. | P0 | AC-138, TEST-134 |
| REQ-141 | Every release shall have a rollback path that preserves compatible learner data or explicitly blocks unsafe downgrade. | P0 | AC-139, TEST-135 |
| REQ-142 | The repositories shall publish support, security-reporting, contribution, conduct, license, asset provenance, and maintenance expectations. | P0 | AC-140, TEST-136 |

### Parent relationship, authentication, and hosting

| ID | Requirement | Priority | Verification |
|---|---|---:|---|
| REQ-143 | A parent-only stay-in-touch flow shall collect no more than parent email, optional parent display name, explicit purpose choices, consent policy version, source, and disclosed campaign context. | P0 | AC-141, TEST-137 |
| REQ-144 | Newsletter, research-recruitment interest, product support, and paid-license purposes shall be separate contact permissions and shall never be inferred from child play. Research-recruitment interest is not guardian consent, child assent, or study enrollment. | P0 | AC-142, TEST-138 |
| REQ-145 | Newsletter enrollment shall require email-possession verification, record a consent event, provide one-action unsubscribe, and retain suppression state so an address is not silently re-added. | P0 | AC-143, TEST-139 |
| REQ-146 | The append-only consent and suppression ledger shall be authoritative for contact permission. Twenty CRM shall be a rebuildable projection for approved verified-parent relationship fields, reached only from a server-side adapter; child profiles, age, lessons, prompts, keystrokes, mastery, and session history shall be prohibited fields. | P0 | AC-144, TEST-140 |
| REQ-147 | The free app and child mode shall require no authentication. A local adult gate is a navigation safeguard, not proof of identity. | P0 | AC-145, TEST-141 |
| REQ-148 | If paid Family is approved, checkout and recovery shall use a parent-controlled identity flow outside child play, while the installed app consumes only a signed offline entitlement with no password or payment credential. A licensing-service outage shall not interrupt an already valid local entitlement, and an operator-approved offline import and recovery path shall exist. | P0 for commerce | AC-146, TEST-142 |
| REQ-149 | Operator access to CRM, consent, deployment, signing, and support systems shall use unique authorized accounts and approved estate secret handling; no browser or desktop bundle shall contain an administrative credential. | P0 | AC-147, TEST-143 |
| REQ-150 | The public parent service shall run only on an approved production surface with measured capacity, resource limits, health checks, backup and restore inclusion, monitoring, and rollback. Buzz and `team-server` shall not host it. | P0 | AC-148, TEST-144 |
| REQ-151 | Signed desktop artifacts, content, checksums, and updater metadata shall use static release distribution rather than an always-running game server. | P0 | AC-149, TEST-145 |

## Non-functional requirements

| ID | Target | Measurement note |
|---|---|---|
| NFR-101 | Key-to-visible-feedback p95 below 50 ms on the minimum supported device during a lesson. | Measure end-to-end with hardware and software details. |
| NFR-102 | Sustained scene rendering at 60 fps or display refresh, with p99 frame time below 33 ms on the minimum device. | Allow a documented 30 fps reduced profile if user selected. |
| NFR-103 | Warm start to interactive below 2 seconds and cold start below 5 seconds on the minimum device. | Proposed, not measured. |
| NFR-104 | Idle CPU below 1 percent and no learner-progress writes while the app is hidden and unchanged. | Proposed, hardware-normalized. |
| NFR-105 | No critical or high known vulnerabilities in a release candidate without written risk acceptance and expiry. | Scanner findings still require human triage. |
| NFR-106 | Zero unexplained outbound connections during complete free and paid-mode test sessions. | Local license fixtures used in tests. |
| NFR-107 | All shipped learner-facing text meets the approved reading-level band or carries a deliberate exception. | Band remains U-103. |
| NFR-108 | WCAG 2.2 AA is the default UI target where applicable, with documented game-specific exceptions and manual testing. | Automated scans alone are insufficient. |
| NFR-109 | Parent-service requests shall be rate limited, size bounded, idempotent, and safe under CRM and email-provider timeout or retry. | Thresholds are set from a staged abuse and load test before production. |
| NFR-110 | The shared VPS deployment shall declare CPU and memory limits and a separation trigger based on sustained resource use, backup growth, incident blast radius, or commerce criticality. | Re-measure at deployment and before paid launch; the 2026-09-10 snapshot is not a permanent reservation. |

## Success measures

No business or learning metric is currently measured. The following are proposed experiments:

| ID | Measure | Initial gate | Evidence class |
|---|---|---:|---|
| MET-101 | Child voluntarily begins another session within seven days | 70 percent in pilot | observed playtest |
| MET-102 | Child completes onboarding without adult action after launch | 80 percent | observed playtest |
| MET-103 | Accuracy on taught keys after the free world | improvement from individual baseline; final threshold by reviewer | pre/post probe |
| MET-104 | Parent can explain progress and next skill | 80 percent | interview and task test |
| MET-105 | Parent expresses credible willingness to pay | threshold after price research | interview plus purchase-intent method |
| MET-106 | Crash-free local sessions | threshold deferred until a lawful denominator and collection method exist; report bounded lab or pilot counts meanwhile | privacy-reviewed operational evidence |

## Traceability rule

Every shipped feature must trace from an objective to a requirement, decision or component, user flow, acceptance criterion, task or change set, test result, candidate revision, release artifact, and metric or risk. A feature with no evidence link is unproven, not complete.
