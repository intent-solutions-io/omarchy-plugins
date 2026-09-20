---
blueprint:
  documentId: KTA-AC-001
  documentType: acceptance-criteria
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
  sourceRefs: [KTA-PRD-001, KTA-ADR-001, KTA-ARCH-001, KTA-UX-001, KTA-PRIV-001]
  assumptions: [A-101, A-102, A-105]
  unknowns: [U-101, U-102, U-103, U-104, U-105, U-107]
  relatedArtifacts: [KTA-TEST-001, KTA-PLAY-001, KTA-RISK-001, KTA-OPS-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure acceptance criteria

> Passing these criteria will require actual evidence tied to an exact revision. This document does not assert that any criterion currently passes.

## Product boundary

### AC-101: Standalone failure domain

Given the app is installed, when it starts, plays a lesson, closes, or crashes, then `omarchy-shell` remains responsive and the app runs under a distinct process boundary.

### AC-102: Named platform floor

Given the release candidate, when the support matrix is inspected, then it identifies exact Omarchy, Arch package, WebKitGTK, architecture, display, and keyboard baselines, and the candidate passes install and play on the minimum row.

### AC-103: Companion contract

Given app and companion are installed, when the bar control is used, then it launches or focuses the app and renders only the approved summary schema without learner nickname or per-key history.

### AC-104: App independence

Given the companion is not installed, when the user starts the desktop app, then every free and entitled app function works unchanged.

### AC-105: No silent installation

Given the app is absent, when the companion is selected, then it shows a bounded help state and does not download, install, elevate, or execute a variable command.

## Profiles and representation

### AC-106: Minimal free profile

Given a first launch, when a learner creates a free profile, then only a local callsign or nickname, character settings, and accessibility choices are requested, with no account or online identifier.

### AC-107: Family profiles

Given a valid paid-family entitlement, when a parent creates four profiles, then their mastery, settings, exports, resets, and deletion remain isolated.

### AC-108: Character equivalence

Given original hero, edit, randomize, optional-pronoun, and quick-start paths, when the same content version and seed are used, then curriculum, difficulty, worlds, rewards, colors, and completion paths are identical except for selected presentation fields, and no gender category is required.

### AC-109: Parent boundary

Given child mode, when a learner navigates every reachable route, then purchase, license import, export, deletion, external links, and legal settings are unavailable until the documented adult gate is completed.

### AC-110: Local control

Given a profile with progress, when a parent exports and then deletes it, then the export is readable and bounded, all normative profile records are removed, and unrelated profiles and entitlement remain intact.

## Curriculum and input

### AC-111: Versioned content

Given a release content tree, when the validator runs, then every skill, lesson, prompt, mission, asset, and prerequisite reference is unique, resolvable, versioned, and provenance-linked.

### AC-112: Complete lesson contract

Given any lesson record, when validated, then it declares target skills, prerequisites, allowed input, reading-level result, mastery rule, entitlement, accessibility notes, and review state.

### AC-113: Accuracy-first mastery

Given one learner completes a fast inaccurate attempt and another completes a slower accurate attempt, when mastery updates, then the inaccurate attempt cannot receive a higher accuracy mastery decision solely due to speed.

### AC-114: Layout semantics

Given QWERTY and at least one non-QWERTY fixture, when physical and character inputs differ, then the engine uses the declared `key` or `code` semantic correctly and presents the character the learner is expected to produce.

### AC-115: Input edge cases

Given repeat, Shift, Caps Lock, composition, dead key, paste, synthetic event, focus loss, and Escape fixtures, when processed, then each follows the published policy without false mastery credit or leaked timing.

### AC-116: Complete free path

Given a new free profile, when eligible lessons are completed, then the approved lesson count forms one coherent beginner path through lowercase and uppercase letters, space, Enter, Shift, numerals, and essential sentence punctuation, essential correction, and basic local adaptation, and no paid prerequisite blocks remediation or the ending.

### AC-117: Prerequisite enforcement

Given paid content is unlocked, when an advanced or shortcut mission lacks mastered prerequisites, then it remains unavailable with an understandable next-step explanation.

### AC-118: Explainable adaptation

Given a learner has a stable error pattern, when the next practice is selected, then a parent-facing explanation names the relevant skill evidence without exposing raw keystrokes or a hidden model score.

### AC-119: No practice trap

Given generated learner histories including repeated difficulty, when the selector runs, then it always offers an achievable practice, assistance change, prerequisite return, or break, and terminates within a bounded number of decisions.

## Game and tone

### AC-120: Vertical-slice completeness

Given the slice build, when a new learner plays it, then onboarding, teaching, untimed practice, active mission, set-piece, results, save, resume, and clean exit are all present.

### AC-121: Respectful correction

Given an incorrect key, when feedback appears, then it identifies the expected key or finger through approved cues, uses no ridicule or loss threat, and clears without blocking accessibility settings.

### AC-122: Honest difficulty

Given two difficulty settings, when the same skill is played, then differences are limited to declared pace, prompt, assistance, and spacing parameters, and scoring never labels assisted access as cheating.

### AC-123: Rights chain

Given every shipped story, lesson, font, image, sound, and dependency, when provenance validation runs, then a compatible license or creator agreement, source, author, modification record, and distribution permission exist.

## Free, paid, and privacy

### AC-124: Permanent free world

Given no entitlement and no network, when the app is reopened after any elapsed time, then the complete free world and accessibility features remain playable.

### AC-125: Child-safe commerce boundary

Given child mode, when all screens and error paths are traversed, then no price, checkout, ad, urgency, external purchase link, or paid-loss message appears.

### AC-126: Signed unlock

Given valid, altered, oversized, expired where applicable, wrong-product, wrong-algorithm, and unknown-key entitlement fixtures, when imported, then only the valid fixture unlocks the declared edition.

### AC-127: Offline paid access

Given a previously imported valid entitlement and an unavailable license service, when the app starts and plays, then purchased local content remains accessible under the published license terms.

### AC-128: Published commercial rules

Given checkout is enabled, when the parent reaches it, then price, seller, taxes or tax handling, license scope, device rules, updates, refund, recovery, support, and privacy documents are linked and versioned.

### AC-129: Local learning data

Given a complete play session under network observation, when the app runs, then no nickname, mastery, attempt, prompt, raw key, or session data leaves the device.

### AC-130: Excluded services

Given the candidate dependency tree, permissions, runtime processes, and routes, when audited, then no third-party analytics, ad, social, chat, public profile, push engagement, global keyboard hook, or automatic crash upload is present.

### AC-131: Truthful policy

Given candidate behavior and vendor register, when compared with the public data inventory and policies, then every collection, purpose, recipient, retention, deletion, and contact statement matches observed behavior.

## Accessibility and safety

### AC-132: Keyboard navigation

Given keyboard-only operation, when the user traverses all menus and parent screens, then focus is visible, ordered, escapable, and no function requires pointer input unless documented as a game-specific exception with an alternative.

### AC-133: Free accessibility

Given each supported accessibility audience and a free profile, when reduced motion, a complete untimed mode, sound-off equivalents, larger type, reflow, color-independent feedback, remapping, screen reader, one-handed input, or the non-canvas path applies, then the learner can finish the entire free world or the product publishes a specific reviewed limitation. No accessibility control requires purchase.

### AC-134: Motion and flash safety

Given every effect and transition, when automated timing checks and manual review run, then no prohibited flash pattern exists, reduced motion is honored, and pausable movement follows the adopted standard.

## Persistence, release, and governance

### AC-135: Durable storage

Given a committed session, when the app restarts, then the exact normative state loads; writes are atomic; schema and content versions are recorded; and a last-good recovery artifact exists where specified.

### AC-136: Recovery matrix

Given malformed, truncated, oversized, read-only, future-version, full-disk, interrupted-write, and concurrent-open fixtures, when loaded or saved, then the app preserves recoverable data, explains the state, and never silently replaces it with blank progress.

### AC-137: Candidate identity

Given a release artifact, when verified, then its checksum, signature, source revision, lockfiles, SBOM, test evidence, builder identity, and release notes resolve to the same candidate.

### AC-138: Private update check

Given an update request, when server and client evidence are inspected, then only target, architecture, version, ordinary transport metadata, and explicitly documented fields are sent, with no learner or entitlement detail beyond what is necessary.

### AC-139: Rollback

Given a bad candidate, when rollback is exercised, then the previous signed app starts and can read the preserved data, or the tool blocks downgrade with a tested export/recovery path.

Blocking an unsafe downgrade is a recovery safeguard, not successful rollback. If the previous signed app cannot start with preserved compatible data, AC-139 remains failed until a signed recovery build restores a working supported state. Export is additional protection and never substitutes for a working rollback or recovery result.

### AC-140: Repository readiness

Given each repository, when the release gate runs, then README, license, contributing guide, conduct, security reporting, support scope, ownership, provenance, changelog, CI, and release documentation exist and match actual commands.

## Parent relationship, authentication, and hosting

### AC-141: Minimal parent intake

Given every parent signup request and stored record, when schemas and runtime evidence are inspected, then only approved parent fields and disclosed campaign context exist, and no child or learning field can be submitted or persisted.

### AC-142: Purpose separation

Given newsletter, early-access research, support, and paid-license purposes, when any one is accepted or withdrawn, then no other purpose changes unless the parent explicitly changes it.

### AC-143: Verification and unsubscribe

Given new, replayed, expired, altered, duplicate, bounced, complained, and unsubscribed email cases, when processed, then only a valid unexpired verification activates the selected purpose, unsubscribe takes effect once, and suppression prevents silent re-enrollment.

### AC-144: CRM boundary

Given successful, duplicate, timeout, retry, and Twenty-unavailable requests, when reconciled, then one parent relationship and a complete consent history exist without direct database writes, client credentials, or learner data.

### AC-145: No child or free-app login

Given a fresh offline installation, when a child creates a local profile and completes the free world, then no login, email, network identity, or entitlement is required, and parent mode does not claim verified identity.

### AC-146: Parent-only paid identity

Given paid Family is enabled, when purchase and recovery run, then authentication remains outside child play, no password or payment credential enters the desktop app, and only a valid signed entitlement changes local capabilities.

### AC-147: Operator credential isolation

Given source, browser bundles, desktop artifacts, logs, CI output, and public evidence, when scanned, then no CRM, mail, deployment, merchant, or signing credential appears, and the access inventory identifies unique authorized operator roles.

### AC-148: Production placement

Given a parent-service candidate, when deployment is reviewed, then dated capacity, resource limits, TLS, rate limiting, health, monitoring, secrets, backup, restore, rollback, and separation triggers pass on the approved shared VPS, with no public deployment on Buzz or `team-server`.

### AC-149: Static game distribution

Given the free desktop release, when all infrastructure is unavailable after artifact download, then the signed app and complete free world install and play without an always-running game backend; only optional update and parent workflows are unavailable.

## Acceptance evidence record

Each criterion result records criterion ID, linked requirement and risk, exact source revision, artifact checksum, environment, expected result, actual result, status, limitation, timestamp, operator, reviewer, and evidence path. `Skipped`, `not applicable`, `blocked`, and `unproven` are distinct from `passed`.

## Release applicability

| Release | Required acceptance groups |
|---|---|
| v0.1 slice | AC-101, AC-102, AC-104, AC-108, AC-111 through AC-115, AC-120 through AC-123, AC-129, AC-131 through AC-133, and the approved Stage B entry criteria; complete-world, production recovery, public release, companion, parent-service, and paid criteria do not apply |
| v0.5 free pilot | all free-app criteria plus AC-103, AC-105, AC-110, AC-124, AC-125, AC-137 through AC-140 |
| v1.0 free public | all free and companion criteria, completed pilot disposition, signed update and rollback evidence, and AC-141 through AC-145 plus AC-147 through AC-149 if the parent-contact service is live; AC-107 and AC-126 through AC-128 plus AC-146 are not applicable |
| v1.1 Family paid | every criterion, including AC-107 and AC-126 through AC-128, plus paid-policy and commerce approval |

Paid-only criteria do not block the free public release. Shared safety, privacy, accessibility, storage, release integrity, and support criteria do.
