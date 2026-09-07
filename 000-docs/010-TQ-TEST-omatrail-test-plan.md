---
blueprint:
  documentId: OMT-TEST-001
  documentType: test-plan
  schemaVersion: 1.0.0
  templateVersion: 3.0.0
  status: draft
  owner: Jeremy Longshore
  authors: ["Intent Solutions / Codex"]
  reviewers: []
  approvers: []
  generatedAt: 2026-09-06
  updatedAt: 2026-09-07
  classification: public-draft
  sourceRefs: [OMT-PRD-001, OMT-ARCH-001, OMT-GAME-001, OMT-AC-001, SR-003, SR-004, SR-008]
  assumptions: [A-001, A-003]
  unknowns: [U-003, U-005]
  relatedArtifacts: [OMT-AC-001, OMT-PLAY-001, OMT-RISK-001, OMT-PLAN-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omatrail test plan

> This is a plan, not a test report. Actual results, environments, revisions, timestamps, and evidence paths must be added during execution.

## Test objectives

- Prove deterministic rules independently of QML.
- Prove hunting is mechanically correct and balanced before expanding content.
- Prove both display profiles operate on identical semantic state.
- Prove saves are durable, bounded, migratable, and recoverable.
- Prove lifecycle, input, and performance do not destabilize `omarchy-shell`.
- Prove shipped content and assets satisfy provenance and review controls.

## Allocation rationale

The largest automated investment belongs in the pure engine because most defects can be reproduced there cheaply. QML integration testing concentrates on lifecycle, focus, rendering, and host compatibility. Human playtesting evaluates enjoyment, comprehension, comfort, and balance claims that automated tests cannot establish.

## Proposed environments

| ID | Environment | Purpose | Status |
|---|---|---|---|
| ENV-001 | Node version supported by the plugin CI | Pure rules, content, simulations | unresolved |
| ENV-002 | Minimum supported Omarchy Quattro on Hyprland | Compatibility floor | U-005 |
| ENV-003 | Current stable Omarchy Quattro | Primary runtime | unresolved at execution |
| ENV-004 | 1920x1080, 2560x1440, 3840x2160, ultrawide; scale 1 and applicable fractional scale | Rendering matrix | proposed |
| ENV-005 | Single and multiple monitors; keyboard-only and mouse | Focus and input matrix | proposed |

## Test registry

| ID | Level | Test | Traceability | Expected evidence | Priority |
|---|---|---|---|---|---:|
| TEST-001 | unit | Party creation, occupation, naming bounds, and initial state | REQ-004, REQ-022; AC-001 | Node test output and fixtures | P0 |
| TEST-002 | unit/property | Store budget, quantities, weight, and inventory invariants | REQ-005, REQ-022; AC-001 | Node tests plus generated cases | P0 |
| TEST-003 | unit/property | Travel, health, illness, rest, pace, ration, calendar, and RNG determinism | REQ-006, REQ-014, REQ-022; AC-002, AC-003, AC-014; RISK-008 | Node tests and reproducible seeds | P0 |
| TEST-004 | graph | Route connectivity, required acts, landmarks, crossings, and terminal states | REQ-007; AC-004 | Route validator output | P0 |
| TEST-005 | unit/integration | Hunting movement, collision, aim, shot, animal behavior, yield, time, risk, carry, waste, and pause | REQ-008 through REQ-010, REQ-022; AC-006, AC-007, AC-008, AC-009; RISK-005, RISK-006 | Node tests, QML smoke, seed replays | P0 |
| TEST-006 | unit/simulation | Ending and score calculations | REQ-027; AC-005 | Golden cases and seed replays | P1 |
| TEST-007 | simulation | Strategy viability and balance across at least 100,000 fixed seeds | REQ-011, REQ-014, REQ-022; AC-010, AC-014; RISK-007, RISK-008 | Versioned distribution report | P0 |
| TEST-008 | unit/integration | River availability, outcomes, factor explanation, and animation completion | REQ-012, REQ-022; AC-011, AC-012 | Node cases and runtime capture | P0 |
| TEST-009 | schema/graph | Content IDs, bounds, eligibility, destinations, sources, animal-region mapping, and dead branches | REQ-009, REQ-013, REQ-026; AC-004, AC-007, AC-013, AC-027; CTRL-004, CTRL-006 | Content validator report | P0 |
| TEST-010 | visual | Critical-scene snapshots for Green Monitor and Color Deluxe | REQ-017, REQ-019, REQ-020; AC-015, AC-017, AC-026; RISK-010, RISK-011 | Approved image set by resolution/profile | P0 |
| TEST-011 | differential | Switch profiles at every scene and assert identical semantic state and hitboxes | REQ-017, REQ-018; AC-016; CTRL-007 | Automated state diff | P0 |
| TEST-012 | accessibility | Keyboard traversal, remapping, focus, non-color cues, reduced motion, clean pixels, readable scaling, hunting assists | REQ-021; AC-006, AC-018, AC-019; RISK-006, RISK-010; CTRL-007 | Checklist, captures, and playtest evidence | P0 |
| TEST-013 | compatibility | `omarchy plugin validate`, `qmllint`, manifest/files, install, enable, disable, remove, reinstall | REQ-001; AC-020; RISK-014, RISK-016; CTRL-003 | Exact command log and candidate SHA | P0 |
| TEST-014 | system | Bar click, summon, hide, Escape, overlay switch, focus loss, multi-monitor, shell restart | REQ-002, REQ-003, REQ-024; AC-021, AC-028; RISK-002, RISK-003 | Scenario log and screen capture | P0 |
| TEST-015 | persistence | Save after each consequential action; resume after close, crash, and restart | REQ-015, REQ-028; AC-022, AC-024; RISK-004; CTRL-002 | State hashes before and after | P0 |
| TEST-016 | failure/recovery | Missing, malformed, truncated, oversized, old, future, and read-only saves | REQ-016, REQ-028; AC-023, AC-024; RISK-004; CTRL-002 | Failure-path log and preserved artifacts | P0 |
| TEST-017 | security/provenance | Network, process, path, permission, dependency, asset-license, and repository security lane | REQ-023, REQ-025, REQ-026; AC-025 through AC-027; RISK-001, RISK-014, RISK-015; CTRL-001, CTRL-003, CTRL-005, CTRL-006 | Static report, runtime observation, provenance register | P0 |
| TEST-018 | performance | Input latency, frame pacing, memory, open/close cycles, hidden idle work, timer shutdown | REQ-024, NFR-001 through NFR-004; AC-028; RISK-002, RISK-003, RISK-013 | Profile report with hardware and revision | P0 |

## Invariants and generated testing

At minimum, generated tests assert:

- No quantity, health value, date, score input, or condition counter becomes non-finite.
- Inventory cannot exceed declared bounds or create matter through a transaction.
- The RNG advances only through declared engine effects.
- A terminal state cannot accept travel or hunting actions.
- A dead party member cannot act, recover, consume individual medicine, or die again.
- A hunt field always places the hunter in a navigable region.
- Carried meat never exceeds capacity or harvested meat.
- Display mode never changes semantic state.
- Save encode/decode round trips preserve all normative fields.
- Every event has at least one legal exit and content traversal terminates.

## Balance simulation

The simulation harness runs the same engine as the UI with versioned policy bots:

| Policy | Intent | Proposed success band |
|---|---|---|
| Reckless | Grueling pace, poor ration discipline, high-risk crossings | 5 to 20% |
| Naive | Locally reasonable choices without route knowledge | 25 to 45% |
| Skilled hunting-heavy | Uses hunting well and preserves ammunition | 55 to 75% |
| Skilled hunting-light | Buys, trades, rests, and rations carefully | 50 to 70% |
| Exploit seeker | Hunts or rests whenever mechanically profitable | Must not dominate skilled policies |

Bands are hypotheses. Playtests and simulation review may change them. Any balance change records engine version, content version, seed set, policy version, before/after distributions, and rationale.

## Security and privacy checks

- Search QML and JavaScript for network clients, URLs, shell construction, unbounded `Process`, credential paths, and filesystem writes.
- Observe runtime network and child-process activity during a complete seeded run.
- Verify state paths are plugin-specific and state files are not executable.
- Verify local party names never enter logs, screenshots, telemetry, crash reports, or submission fixtures without explicit sanitization.
- Verify repository dependencies and assets against the candidate lockfile and provenance register.
- Run the current Omarchy submission/security lane against the exact candidate revision.

## Entry criteria

- Requirements and architecture have owner review.
- Testable build identifies source revision and content schema version.
- ENV-002 and ENV-003 are resolved.
- Test fixtures contain no personal data or uncleared commercial assets.
- Known deviations are recorded, not silently skipped.

## Suspension criteria

Suspend release testing if:

- The shell crashes or focus remains captured after close.
- A save is silently overwritten after a failed migration.
- Any network, credential, privilege, or undeclared write behavior appears.
- Asset or content provenance is disputed.
- The tested revision changes.

## Exit criteria

- All P0 tests pass on the exact candidate revision.
- P1 failures have named disposition and do not invalidate an acceptance criterion.
- AC-001 through AC-028 have linked actual evidence.
- Coverage reports identify limitations rather than converting missing tests into passes.
- Product, engineering, content, and legal review decisions are recorded.

## Execution record schema

Each run records test ID, requirement/risk/control IDs, source revision, environment, resolved inputs, test data or seed set, expected result, actual result, status, limitation, timestamp, operator, and evidence path. `Skipped` and `unproven` are never reported as `passed`.

## Execution snapshot

Execution continues against the uncommitted local branch `main` in
`omarchy-omatrail-entry`. The candidate covers pure
journey and hunting rules, 10,000 deterministic hunting fields, QML source
contracts, bounded save parsing, a descriptor-bound state helper, and same-UID
file and parent-directory swap races. Exact automated counts and coverage are
recorded in the plugin repository after each final lane rather than projected
in this Blueprint.

TEST-007 ran 100,000 fixed seeds through the public journey dispatcher and
genuine hunting results across all 480 rules-profile, policy, difficulty,
occupation, and departure-month cells. Every run reached victory or loss.
Completion was 4.58 percent reckless, 56.28 percent naive, 82.56 percent
skilled hunting-heavy, 77.22 percent skilled hunting-light, and 51.82 percent
exploit-seeking. The exploit policy remained below both skilled policies in
each rules profile and earned a substantially lower median score. The
aggregate report SHA-256 is
`776ddabcd55a089c6292a799f5fd60f8dacd8b753168ac237ae394e41fbbde7a`.
Serial and multi-worker sentinel reports are asserted to remain byte-identical.

The dirty development tree has passed the real Buzz Omarchy validator with zero
`qmllint` errors and loaded through live shell IPC without plugin QML warnings.
A twenty-frame matrix is specified to cover river, ending, hunting, event, and
trail fixtures across both rules profiles and Green Monitor and Color Deluxe
over one source fingerprint. Every
1280 by 720 PNG reconciles with a hash-bound receipt and retained raw shell log.
Visual inspection caught and corrected a save/profile override, a
scaled-viewport trail overflow, and a clipped hunting instruction before the
matrix run. A targeted live lifecycle run now proves hunting advance, hidden
timer shutdown, reopen and resume, exact persisted-state restoration across a
shell restart, and no added persistent child process or Quickshell TCP
connection. It also records whole-shell RSS and open-hide timing. Exact
clean-revision regeneration, install, enable, disable, remove, reinstall,
owner-approved preview, real device input, complete-run privacy observation,
frame pacing, latency, and long-soak performance remain outstanding.

Current execution status: **in progress, candidate evidence only**. No release
or acceptance verdict is granted by this snapshot.
