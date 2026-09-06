---
blueprint:
  documentId: OMT-PRD-001
  documentType: product-requirements
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
  sourceRefs: [SR-001, SR-002, SR-003, SR-004, SR-005, SR-006, SR-007, SR-008, SR-009]
  assumptions: [A-001, A-002, A-003, A-004]
  unknowns: [U-001, U-002, U-003, U-004, U-005, U-006]
  relatedArtifacts: [OMT-BRIEF-001, OMT-ARCH-001, OMT-GAME-001, OMT-AC-001, OMT-TEST-001, OMT-PLAY-001, OMT-RISK-001, OMT-PLAN-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omatrail product requirements

> Normative requirements are proposals until human approval. Evidence IDs resolve through the source register in `OMT-BRIEF-001`.

## Product outcome

Omatrail gives an Omarchy user a complete, locally saved survival journey in which hunting is a skill-based centerpiece and preparation, river decisions, pace, rations, weather, illness, breakdowns, and relationships determine whether a named party reaches its destination.

## Requirements registry

| ID | Requirement | Owner | Source or rationale | Priority | Status | Verification |
|---|---|---|---|---:|---|---|
| REQ-001 | The plugin shall install and validate as a third-party Omarchy Quattro plugin with a namespaced ID. | Engineering | SR-003, SR-004 | P0 | proposed | TEST-013 |
| REQ-002 | A bar widget shall open and close the game surface through the shell lifecycle and remain quiet when no expedition is active. | Engineering | SR-003, local convention SR-008 | P0 | proposed | TEST-014 |
| REQ-003 | The game shall run in a fullscreen overlay suitable for keyboard-focused play. | Engineering | User direction and SR-004 | P0 | proposed | TEST-014, PLAY-001 |
| REQ-004 | A player shall name five party members and choose an occupation before departure. | Product | Genre identity; SR-006 | P0 | proposed | TEST-001, PLAY-003 |
| REQ-005 | The initial store shall support meaningful tradeoffs among oxen, food, ammunition, clothing, medicine, and spare wagon parts. | Product | SR-006 | P0 | proposed | TEST-002, TEST-007 |
| REQ-006 | Each travel turn shall resolve pace, rations, terrain, weather, calendar, party state, supplies, and wagon condition deterministically from state plus a seeded random stream. | Engineering | Testability and replay rationale | P0 | proposed | TEST-003, TEST-006 |
| REQ-007 | The route shall contain three acts, multiple regions, landmarks, route choices, forts, rivers, and a final arrival or loss state. | Narrative | Product direction | P0 | proposed | TEST-004, TEST-008 |
| REQ-008 | Hunting shall be a playable 60 to 90 second keyboard-first arcade activity, not a text-only probability check. | Game design | User direction; SR-005 | P0 | provided | TEST-005, PLAY-001, PLAY-002 |
| REQ-009 | Hunting shall vary animals, behavior, terrain objects, visibility, and yield by geographic region and season. | Game design | SR-005 | P0 | proposed | TEST-005, TEST-009 |
| REQ-010 | Hunting shall consume time and ammunition, expose the hunter to bounded risk, enforce a carrying limit, and report harvested, carried, and wasted meat. | Game design | SR-005 | P0 | proposed | TEST-005, TEST-007 |
| REQ-011 | A hunting-heavy and hunting-light strategy shall both be viable; hunting shall not be a mandatory or infinite-food exploit. | Game design | SR-006 | P0 | proposed | TEST-007, PLAY-004 |
| REQ-012 | River crossings shall offer context-sensitive options such as ford, float, ferry, wait, or hire guidance and show an animated outcome. | Game design | SR-006 | P0 | proposed | TEST-008, PLAY-005 |
| REQ-013 | Hand-written events shall cover illness, injury, weather, breakdown, trade, conflict, aid, landmarks, and loss without runtime-generated prose. | Narrative | Offline scope and story requirement | P0 | proposed | TEST-009, CTRL-006 |
| REQ-014 | Party health shall respond to pace, rations, rest, weather, illness, treatment, and prior condition so consequences remain explainable. | Game design | SR-006 | P0 | proposed | TEST-003, TEST-007 |
| REQ-015 | The game shall save a versioned, bounded local state after consequential actions and resume the exact expedition after close or shell restart. | Engineering | User direction and local precedents | P0 | proposed | TEST-015, TEST-016 |
| REQ-016 | A malformed or incompatible save shall never crash the shell and shall offer backup, recovery, or a clearly confirmed new journey. | Engineering | Shell resilience | P0 | proposed | TEST-016, CTRL-002 |
| REQ-017 | Green Monitor and Color Deluxe shall render the same game state, layout, controls, and content through interchangeable visual profiles. | Design | User direction | P0 | provided | TEST-010, TEST-011 |
| REQ-018 | The player shall be able to switch display profiles during an expedition without changing or restarting the save. | Design | User direction | P0 | proposed | TEST-011 |
| REQ-019 | Green Monitor shall use a black field, monochrome phosphor-green pixel art, numbered menus, sharp integer scaling, and optional CRT effects. | Design | User direction and SR-007 | P0 | provided | TEST-010, PLAY-006 |
| REQ-020 | Color Deluxe shall use original limited-color pixel art and shall not copy protected visual assets. | Design | Product and legal boundary | P0 | proposed | CTRL-005, human asset review |
| REQ-021 | The game shall support complete keyboard operation, mouse alternatives, remappable gameplay keys, visible focus, reduced motion, clean pixels, readable text, and non-color status cues. | Design | Accessibility applicability | P0 | proposed | TEST-012, PLAY-007 |
| REQ-022 | The simulation and content selection shall reside in pure JavaScript modules loadable by both QML and Node tests. | Engineering | SR-008 | P0 | proposed | TEST-001 through TEST-009 |
| REQ-023 | The runtime shall make no network requests, require no credentials, execute no privileged commands, and collect no telemetry by default. | Security | A-002 and least capability | P0 | proposed | TEST-017, CTRL-001 |
| REQ-024 | Timers, animation, and input capture shall stop when the overlay closes; no game key shall reach the previously focused application while open. | Engineering | Shared shell and input safety | P0 | proposed | TEST-014, TEST-018 |
| REQ-025 | All shipped story, code, graphics, fonts, music, and sound shall be original or carry documented redistribution rights. | Product | SR-009 and marketplace submission integrity | P0 | proposed | CTRL-005 |
| REQ-026 | Historical assertions and representations of affected peoples shall cite a source and receive human content review before release. | Narrative | Harm prevention | P0 | proposed | CTRL-006 |
| REQ-027 | A completed run shall produce a local score and ending summary based on survival, time, difficulty, resources, and avoidable waste. | Product | Replayability rationale | P1 | proposed | TEST-006, PLAY-003 |
| REQ-028 | The player shall be able to pause, abandon, restart, and delete local expedition data deliberately. | Product | User control | P1 | proposed | TEST-015, TEST-016 |

## Quality attributes

| ID | Attribute | Proposed target | Evidence method |
|---|---|---|---|
| NFR-001 | Shell safety | Zero uncaught runtime errors in the release scenario matrix | TEST-014 through TEST-018 |
| NFR-002 | Responsiveness | Input-to-visible-response p95 at or below 50 ms on the minimum supported machine | TEST-018; minimum machine is U-005 |
| NFR-003 | Frame pacing | Stable 60 fps target during active animation, with an acceptable 30 fps accessibility fallback | TEST-018 |
| NFR-004 | Idle cost | No hunting loop, travel loop, or recurring animation timer while the overlay is hidden | TEST-018 |
| NFR-005 | Save durability | Consequential actions survive forced shell restart with at most the current unconfirmed action lost | TEST-015 |
| NFR-006 | Testability | All deterministic rules and content eligibility run headlessly under `node --test` | TEST-001 through TEST-009 |
| NFR-007 | Accessibility | Project-specific alignment review against applicable WCAG 2.2 AA principles, without claiming formal conformance | TEST-012 |
| NFR-008 | Repository quality | Manifest, QML, tests, docs, license, preview, and the current Omarchy submission lane pass | TEST-013, TEST-017 |

## Success metrics

These are proposed gates, not observed baselines.

| ID | Question | Formula or measure | Target | Owner |
|---|---|---|---|---|
| MET-001 | Is hunting enjoyable? | Post-hunt enjoyment, 1 to 5 | Median at least 4 | UX owner |
| MET-002 | Is hunting learnable? | Third-hunt success minus first-hunt success | Positive improvement for at least 70% of testers | Game-design owner |
| MET-003 | Do decisions matter more than luck? | Simulated win-rate spread between careless and skilled policies | At least 35 percentage points | Engineering owner |
| MET-004 | Is the whole run paced correctly? | Median completed-run duration | 20 to 40 minutes | Product owner |
| MET-005 | Can new players act without instruction? | Critical-task completion | At least 85% in moderated beta | UX owner |
| MET-006 | Are both displays usable? | Critical-task completion by profile | No profile more than 10 points below the other | Design owner |

## Safety applicability

| Area | Applicability | Rationale | Required evidence |
|---|---|---|---|
| Security | applicable | Third-party code runs unsandboxed inside the shared shell. | CTRL-001 through CTRL-004; TEST-017 and TEST-018 |
| Privacy | limited but applicable | Local party names may be personal data; default telemetry is prohibited. | Local-only data inventory and deletion test |
| Accessibility | applicable | The game is visual and action-based but must support alternate presentation and input. | TEST-012 and PLAY-007 |
| Historical representation | applicable | The setting depicts real places, migration, illness, animals, and affected peoples. | CTRL-006 and named human reviewer |
| AI safety | not applicable | No generative or predictive AI is in scope. | Owner confirmation at release review |

## Traceability summary

| Objective | Requirements | Acceptance | Tests |
|---|---|---|---|
| OBJ-001 | REQ-008 through REQ-011 | AC-006 through AC-010 | TEST-005, TEST-007, PLAY-001, PLAY-002, PLAY-004 |
| OBJ-002 | REQ-004 through REQ-016, REQ-027 | AC-001 through AC-014, AC-024 | TEST-001 through TEST-009, PLAY-003, PLAY-005 |
| OBJ-003 | REQ-017 through REQ-021 | AC-015 through AC-019 | TEST-010 through TEST-012, PLAY-006, PLAY-007 |
| OBJ-004 | REQ-001 through REQ-003, REQ-015, REQ-016, REQ-022 through REQ-025 | AC-020 through AC-023, AC-025 | TEST-013 through TEST-018 |
| OBJ-005 | REQ-025 and REQ-026 | AC-026 and AC-027 | CTRL-005, CTRL-006 |

## Approval boundary

- Requirements status: proposed except decisions explicitly marked provided
- Product owner approval: not recorded
- Engineering feasibility approval: not recorded
- Historical/content approval: not recorded
- Legal approval: not recorded
