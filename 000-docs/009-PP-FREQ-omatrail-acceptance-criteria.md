---
blueprint:
  documentId: OMT-AC-001
  documentType: acceptance-criteria
  schemaVersion: 1.0.0
  templateVersion: 3.0.0
  status: draft
  owner: Jeremy Longshore
  authors: ["Intent Solutions / Codex"]
  reviewers: []
  approvers: []
  generatedAt: 2026-09-06
  updatedAt: 2026-09-06
  classification: public-draft
  sourceRefs: [OMT-PRD-001, OMT-GAME-001, OMT-ARCH-001]
  assumptions: [A-003, A-004]
  unknowns: [U-001, U-003, U-004, U-005]
  relatedArtifacts: [OMT-PRD-001, OMT-TEST-001, OMT-PLAY-001, OMT-PLAN-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omatrail acceptance criteria

> These criteria define proposed observable completion. Passing tests does not grant product, historical, legal, or release approval.

## Product and expedition

| ID | Acceptance criterion | Requirements | Evidence |
|---|---|---|---|
| AC-001 | Given no save, when the player starts, then the game permits five party names, occupation, difficulty, departure month, store purchases, and departure. | REQ-004, REQ-005 | TEST-001, TEST-002 |
| AC-002 | Given a valid expedition, when travel advances, then pace, rations, weather, terrain, calendar, supplies, wagon, and party state produce one valid deterministic result. | REQ-006, REQ-014 | TEST-003 |
| AC-003 | Given the same initial state, seed, and action sequence, two runs produce byte-equivalent semantic state. | REQ-006, REQ-022 | TEST-003 |
| AC-004 | Given a complete content set, every required act, region, landmark, crossing, route end, arrival, and loss state is reachable through a valid path. | REQ-007 | TEST-004, TEST-009 |
| AC-005 | Given completion or loss, the ending lists survivors, losses, duration, difficulty, remaining resources, avoidable waste, score, and replay seed. | REQ-027 | TEST-006, PLAY-003 |

## Hunting

| ID | Acceptance criterion | Requirements | Evidence |
|---|---|---|---|
| AC-006 | Given a hunt, the player can move, aim, fire, pause, and return using keyboard only, with mouse alternatives available. | REQ-008, REQ-021 | TEST-005, TEST-012, PLAY-001 |
| AC-007 | Given at least five configured regions, each region selects only eligible terrain and animals and produces a navigable field. | REQ-009 | TEST-005, TEST-009 |
| AC-008 | Given a completed hunt, ammunition, time, energy, yield, carry limit, spoilage state, and risk effects reconcile exactly with the result screen. | REQ-010 | TEST-005 |
| AC-009 | Given harvested meat above capacity, the result distinguishes harvested, carried, and wasted weight and cannot add more than capacity to inventory. | REQ-010 | TEST-005 |
| AC-010 | Given simulated skilled policies, both a hunting-heavy and hunting-light policy can win, and unlimited hunting does not dominate the score or survival distribution. | REQ-011 | TEST-007, PLAY-004 |

## Rivers, events, and story

| ID | Acceptance criterion | Requirements | Evidence |
|---|---|---|---|
| AC-011 | Given a river, the screen states current decision factors, offers only available actions, requires confirmation, and animates the committed outcome. | REQ-012 | TEST-008, PLAY-005 |
| AC-012 | Given identical river state, seed, and choice, the outcome is deterministic and its explanation matches the factors applied. | REQ-006, REQ-012 | TEST-008 |
| AC-013 | Every event record has a unique ID, eligibility predicate, prose, legal choices, effects, source classification, text bound, and terminal or continuing destination. | REQ-013 | TEST-009 |
| AC-014 | Illness and recovery probabilities respond monotonically to documented health factors, within approved bounds. | REQ-014 | TEST-003, TEST-007 |

## Displays and accessibility

| ID | Acceptance criterion | Requirements | Evidence |
|---|---|---|---|
| AC-015 | Every critical scene renders and remains operable in Green Monitor and Color Deluxe from the same semantic state snapshot. | REQ-017 | TEST-010 |
| AC-016 | Switching display mode changes no semantic state, RNG position, controls, hitboxes, inventory, or save identity. | REQ-017, REQ-018 | TEST-011 |
| AC-017 | Green Monitor renders on a black field with the approved phosphor tokens, pixel snapping, integer scaling where possible, and no unapproved multicolor asset. | REQ-019 | TEST-010, PLAY-006 |
| AC-018 | CRT effects can be reduced or disabled, and reduced-motion mode disables flicker and persistence effects without hiding information. | REQ-019, REQ-021 | TEST-012, PLAY-007 |
| AC-019 | Every critical action is possible without a mouse; every status conveyed by color also has text, shape, brightness, or pattern. | REQ-021 | TEST-012, PLAY-007 |

## Runtime, persistence, and release integrity

| ID | Acceptance criterion | Requirements | Evidence |
|---|---|---|---|
| AC-020 | The manifest validates, referenced entry points exist, plugin ID is unique and namespaced, and the plugin can enable, disable, remove, and reinstall cleanly. | REQ-001 | TEST-013 |
| AC-021 | Bar click and shell summon open the overlay; Escape and shell hide close it; focus returns correctly in every tested path. | REQ-002, REQ-003, REQ-024 | TEST-014 |
| AC-022 | A confirmed consequential action survives overlay close and shell restart and resumes the exact expedition. | REQ-015 | TEST-015 |
| AC-023 | Missing, truncated, malformed, oversized, old, and future-version save cases follow the recovery contract without an uncaught shell error or silent data overwrite. | REQ-016 | TEST-016 |
| AC-024 | The player can pause, abandon, restart, and delete expedition data through explicit, confirmed actions. | REQ-028 | TEST-015, TEST-016 |
| AC-025 | Static and runtime inspection find no network request, credential access, telemetry, privilege request, shell interpolation, or write outside the documented state path. | REQ-023 | TEST-017 |
| AC-026 | Every distributed asset has original-work evidence or a redistribution record, and no review identifies a copied protected asset or passage. | REQ-020, REQ-025 | CTRL-005 and human review |
| AC-027 | Every material historical assertion has a source ID and every affected-group representation has recorded human disposition. | REQ-026 | CTRL-006 and human review |
| AC-028 | When hidden, active gameplay timers stop and measured recurring game work is zero; when open, input and frame targets meet NFR-002 through NFR-004. | REQ-024 | TEST-018 |

## Release acceptance boundary

A 1.0 candidate is acceptable only when:

1. AC-001 through AC-028 have evidence or an explicitly approved, time-bounded waiver.
2. No waiver exists for AC-020, AC-023, AC-025, AC-026, or AC-027.
3. All P0 tests pass on the resolved minimum Omarchy version.
4. The hunting prototype and full-run playtest gates pass.
5. Product, engineering, content, and legal authorities are named and have recorded dispositions.
6. Marketplace verification applies to the exact candidate revision.

## Candidate execution snapshot

An implementation now exists in the local `omarchy-omatrail-entry` repository
on branch `main`. It is an uncommitted development candidate,
so it has no exact candidate revision and cannot cross the release acceptance
boundary.

The implementation traceability matrix in `tests/RTM.md` is the authority for
the current criterion counts. The local automated lane records its exact test
and coverage totals in the implementation repository after each final run.
That lane includes 10,000 generated hunting fields, 100,000 full-journey
balance runs over both rules profiles, hostile state-file race cases, a dirty
and unapproved twenty-frame matrix over both rules and visual profiles, and a
targeted live hunting, hidden-timer, focus, restart,
process, TCP, RSS, and open-hide lifecycle receipt. These results do not replace
clean-SHA regeneration, full system lifecycle and device-input scenarios,
complete-run privacy observation, frame and latency measurements, provenance
review, or human historical and affected-group review.

Current acceptance status: **candidate evaluated in part, not accepted**. The
criterion-by-criterion evidence and limitations are maintained in
`tests/RTM.md` in the implementation repository. Human review remains required.
