---
blueprint:
  documentId: OMT-PLAN-001
  documentType: delivery-task-plan
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
  sourceRefs: [OMT-BRIEF-001, OMT-PRD-001, OMT-ARCH-001, OMT-GAME-001, OMT-AC-001, OMT-TEST-001, OMT-PLAY-001, OMT-RISK-001]
  assumptions: [A-001, A-002, A-003, A-004]
  unknowns: [U-001, U-002, U-003, U-004, U-005, U-006]
  relatedArtifacts: [bd_000-projects-hban]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omatrail delivery plan

> This plan decomposes the proposed product. Only the documentation task `bd_000-projects-hban` exists. Future tasks must be created and claimed in Beads after the product owner approves the applicable phase.

## Delivery method

Work is gated by playable evidence. A later phase cannot hide failure in an earlier one by adding content or polish. Estimates are ranges in focused working days for one experienced developer using the current template and automation. They exclude review and marketplace waiting time and have low to medium confidence.

## Phase and task registry

### Gate 0: authorize and establish the repository

| ID | Task | Depends on | Estimate | Owner | State | Closure evidence |
|---|---|---|---:|---|---|---|
| TASK-001 | Review and approve, amend, or reject the Omatrail blueprint. | None | 0.5 to 1 | Product owner | proposed | Recorded document dispositions |
| TASK-002 | Resolve final name, repository, plugin ID, license, minimum Omarchy version, and decision owners. | TASK-001 | 0.5 to 1 | Product owner | proposed | U-002 through U-005 closed or assigned |
| TASK-003 | Create the sibling repository from the current Omarchy plugin foundation and establish CI/security gates. | TASK-002 | 0.5 to 1 | Engineering | proposed | Clean scaffold and gate receipts |

### Gate 1: hunting prototype

| ID | Task | Depends on | Estimate | Owner | State | Closure evidence |
|---|---|---|---:|---|---|---|
| TASK-004 | Implement seeded hunting state, hunter movement, aiming, shots, timer, and pause. | TASK-003 | 1 to 2 | Engineering | proposed | TEST-005 rules pass |
| TASK-005 | Implement plains field generation, deer, bison, obstacles, ammunition, yield, carry, and waste. | TASK-004 | 1 to 2 | Game design | proposed | Seed replay and invariant report |
| TASK-006 | Implement Green Monitor hunting renderer and first control/accessibility settings. | TASK-004 | 1 to 2 | Design | proposed | Runtime captures and TEST-012 subset |
| TASK-007 | Execute hunting playtest Study A and decide advance, iterate, or stop. | TASK-005, TASK-006 | 1 plus recruitment | UX | proposed | PLAY-001/002 results and owner decision |

Gate: the full journey does not begin until Study A meets the approved threshold or the owner records a justified redesign decision.

### Gate 2: complete vertical slice

| ID | Task | Depends on | Estimate | Owner | State | Closure evidence |
|---|---|---|---:|---|---|---|
| TASK-008 | Build deterministic expedition, calendar, inventory, party, pace, ration, health, and event foundations. | TASK-007 | 2 to 3 | Engineering | proposed | TEST-001 through TEST-003 |
| TASK-009 | Build one route leg with store, landmark, trade, illness, repair, and short ending. | TASK-008 | 1 to 2 | Product/content | proposed | Complete fixed-seed run |
| TASK-010 | Build one full river crossing with visible factors and animated outcomes. | TASK-008 | 1 to 2 | Engineering/design | proposed | TEST-008 and PLAY-005 subset |
| TASK-011 | Implement versioned atomic save, recovery, resume, reset, and delete. | TASK-008 | 1 to 2 | Engineering | proposed | TEST-015 and TEST-016 |
| TASK-012 | Wire bar widget, overlay lifecycle, focus, and hidden-work shutdown. | TASK-008 | 1 to 2 | Engineering | proposed | TEST-013, TEST-014, TEST-018 subset |
| TASK-013 | Execute vertical-slice Study B and decide advance, iterate, or stop. | TASK-009 through TASK-012 | 1 plus recruitment | UX | proposed | Study B evidence and owner decision |

### Gate 3: full journey and content

| ID | Task | Depends on | Estimate | Owner | State | Closure evidence |
|---|---|---|---:|---|---|---|
| TASK-014 | Resolve route/year sources and implement all regions, landmarks, crossings, forts, and terminal paths. | TASK-013, U-001 | 2 to 4 | Content/engineering | proposed | TEST-004 route report |
| TASK-015 | Expand hunting regions, animals, behavior, weather, risk, and hunting-light alternatives. | TASK-013, U-001 | 2 to 4 | Game design | proposed | TEST-005, TEST-007, TEST-009 |
| TASK-016 | Author and validate event and party-story content. | TASK-013, U-001 | 3 to 6 | Content | proposed | TEST-009 and CTRL-006 |
| TASK-017 | Implement scoring, endings, difficulty, and replay-seed presentation. | TASK-014 through TASK-016 | 1 to 2 | Product/engineering | proposed | TEST-006 |

### Gate 4: dual display and production art

| ID | Task | Depends on | Estimate | Owner | State | Closure evidence |
|---|---|---|---:|---|---|---|
| TASK-018 | Complete original Green Monitor font, sprites, landmarks, effects, and clean-pixel mode. | TASK-014 through TASK-017 | 2 to 4 | Art/design | proposed | TEST-010, CTRL-005 |
| TASK-019 | Complete Color Deluxe palette and assets using shared geometry and semantics. | TASK-018 | 2 to 4 | Art/design | proposed | TEST-010 and TEST-011 |
| TASK-020 | Complete remapping, mouse alternatives, reduced motion, hunting assists, and non-color cues. | TASK-018 | 1 to 3 | Design/engineering | proposed | TEST-012 |
| TASK-021 | Add original optional audio if ownership and scope are approved. | TASK-018, U-002 | 1 to 2 | Audio | proposed | Provenance ledger and settings test |

### Gate 5: balance, review, and release

| ID | Task | Depends on | Estimate | Owner | State | Closure evidence |
|---|---|---|---:|---|---|---|
| TASK-022 | Run fixed-seed policy simulation, tune within approved bands, and freeze engine/content versions. | TASK-015 through TASK-020 | 1 to 3 | Game design | proposed | TEST-007 report |
| TASK-023 | Execute full-run Study C and disposition findings. | TASK-022 | 2 plus recruitment | UX/product | proposed | PLAY-003 through PLAY-007 report |
| TASK-024 | Complete historical, affected-group, accessibility, security, and legal review. | TASK-016, TASK-018 through TASK-023 | 1 to 3 plus review | Named reviewers | proposed | CTRL-001 through CTRL-007 evidence |
| TASK-025 | Run full acceptance and release candidate lane on an exact revision. | TASK-024 | 1 | Engineering/release | proposed | AC-001 through AC-028 evidence |
| TASK-026 | Prepare README, install/remove instructions, preview, release notes, provenance, and marketplace submission for owner approval. | TASK-025 | 1 to 2 | Release/product | proposed | Approved submission packet |
| TASK-027 | Submit only after ownership assertions and checklist receive explicit approval. | TASK-026 | waiting | Product owner | proposed | Marketplace issue and verification receipt |

## Critical path

```text
TASK-001 -> TASK-002 -> TASK-003 -> TASK-004/005/006 -> TASK-007
-> TASK-008 -> TASK-009/010/011/012 -> TASK-013
-> TASK-014/015/016 -> TASK-017 -> TASK-018 -> TASK-019/020
-> TASK-022 -> TASK-023 -> TASK-024 -> TASK-025 -> TASK-026 -> TASK-027
```

Optional audio, TASK-021, is not on the critical path unless the owner promotes it to a release requirement.

## Estimate and scope controls

- Estimated build: 15 to 25 focused working days.
- External elapsed time: unknown due to recruitment, specialist review, and marketplace review.
- Estimate basis: decomposition above and comparison to existing native QML game structures, not completed Omatrail velocity.
- Re-estimate after TASK-007 and TASK-013 using actual effort.
- Content or art expansion beyond the approved route/event/asset counts requires an owner-approved scope change.

## Definition of done

- Candidate source revision and artifact identity are fixed.
- All non-waivable acceptance criteria pass.
- Test and playtest evidence identify actual environment, seed/build, results, and limitations.
- No critical/high security finding or zero-tolerance risk remains open.
- Historical, affected-group, accessibility, asset-provenance, and legal decisions are recorded.
- Save recovery and removal are demonstrated.
- README and marketplace claims match observed behavior.
- Beads, Git, release, and marketplace receipts reconcile.

## Immediate next action

The project owner reviews `OMT-BRIEF-001`, selects an advance/amend/stop disposition, and assigns the unresolved authorities. No implementation task should be claimed before that decision.
