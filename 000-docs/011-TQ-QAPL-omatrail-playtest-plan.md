---
blueprint:
  documentId: OMT-PLAY-001
  documentType: playtest-and-usability-plan
  schemaVersion: 1.0.0
  templateVersion: 3.0.0
  status: planned
  owner: Jeremy Longshore
  authors: ["Intent Solutions / Codex"]
  reviewers: []
  approvers: []
  generatedAt: 2026-09-06
  updatedAt: 2026-09-06
  classification: public-draft
  sourceRefs: [OMT-PRD-001, OMT-GAME-001, OMT-AC-001, SR-005, SR-006]
  assumptions: [A-003, A-004]
  unknowns: [U-002, U-006]
  relatedArtifacts: [OMT-TEST-001, OMT-RISK-001, OMT-PLAN-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omatrail playtest and usability plan

> This document defines future studies. It contains no participant results and makes no claim that Omatrail is fun, usable, accessible, or balanced.

## Research questions

| ID | Question | Method | Confidence sought | Limitation |
|---|---|---|---|---|
| PLAY-001 | Is hunting enjoyable as a standalone activity? | Moderated repeated-hunt session | Directional | Small convenience sample cannot establish market demand. |
| PLAY-002 | Does hunting reward learning across attempts? | Compare first, third, and fifth hunt | Directional | Prior action-game skill is a confounder. |
| PLAY-003 | Do named party members and accumulated consequences create memorable journey stories? | Full-run observation and recall interview | Directional | Nostalgia can inflate reported attachment. |
| PLAY-004 | Are hunting-heavy and hunting-light strategies both understandable and viable? | Assigned-strategy full runs plus simulation | Moderate | Human sample cannot cover the full seed space. |
| PLAY-005 | Do river choices create informed suspense rather than opaque frustration? | Think-aloud crossing scenarios | Directional | Prototype animation quality affects the result. |
| PLAY-006 | Do Green Monitor and Color Deluxe both remain legible and appealing? | Counterbalanced profile comparison | Directional | Preference does not establish accessibility. |
| PLAY-007 | Can players with different input and visual needs complete critical actions? | Accessibility-focused tasks | Directional | Formal conformance assessment is out of scope. |

## Study sequence

### Study A: hunting gate

Run before building the full journey.

Proposed participants:

- 4 to 6 Omarchy users
- At least two with no strong memory of the historical game
- A spread of action-game comfort
- At least one keyboard-only participant where recruitment permits

Protocol:

1. Show controls for no more than 20 seconds.
2. Play one plains hunt without coaching.
3. Report comprehension, control confidence, enjoyment, and perceived fairness.
4. Play four more hunts across at least two seeds.
5. Explain the carrying-limit results screen.
6. Try one accessibility assist and one alternate input scheme.

Prototype advancement gate:

- Median enjoyment at least 4 of 5
- At least 80% can move, aim, fire, and exit without intervention on the first hunt
- At least 70% improve a declared hunting measure by the third attempt
- At least 80% correctly explain harvested versus carried meat
- No unresolved focus trap, input leak, motion-sickness blocker, or inaccessible required action

These thresholds are proposed. Failure means iterate or stop. It does not justify lowering the threshold after observing results.

### Study B: vertical slice

Scope: new journey, naming, store, one trail leg, one event, one hunt, one river, save/resume, and short ending.

Proposed sample: 6 to 8 participants, split between nostalgia-aware and category-new players. Counterbalance display-profile order.

Critical tasks:

- Start without external instructions
- Name a party and choose an occupation
- Purchase a viable loadout
- Read condition and change pace or rations
- Hunt and interpret the result
- Choose a river strategy using visible evidence
- Close the game, restart the shell, and resume
- Switch display profile without losing progress
- Find reduced motion and key remapping

Advancement gate:

- At least 85% complete all critical tasks without moderator intervention
- Median System Usability Scale is not used as a release gate for this small prototype; task evidence and observed failure patterns control the decision
- No critical wording or focus failure repeats for more than one participant without disposition
- At least 70% can explain one preparation decision that changed a later outcome

### Study C: full-run balance beta

Proposed sample: 10 to 15 completed runs across new, nostalgic, keyboard-first, mouse-first, Green Monitor, and Color Deluxe cohorts. Recruit additional accessibility participants deliberately rather than expecting the general sample to cover them.

Collect:

- Completion time and result
- Difficulty, occupation, departure month, and seed
- Hunting count, hit rate, ammunition spent, meat carried, and meat wasted
- Crossing decisions and outcomes
- Rest, pace, ration, trade, repair, illness, and death events
- Points of confusion, frustration, delight, and remembered story
- Whether the player wants another run and why

Release hypotheses:

- Median completed run: 20 to 40 minutes
- New-player reasonable-strategy win rate: 25 to 45%
- Experienced-player win rate: 55 to 75%
- At least 70% voluntarily use hunting, while at least one successful tested strategy uses it rarely
- At least 70% can recount one specific party event after the session
- Display profile does not produce more than a 10 percentage-point gap in critical-task completion

## Moderator prompts

Use neutral prompts:

- What do you believe will happen if you choose that?
- What information are you using?
- What would you try next?
- What does this result screen tell you?
- What, if anything, felt unfair?
- Which party member do you remember and why?

Do not teach strategy, explain an icon, praise a choice, or mention an intended emotional response until the task is complete.

## Consent, privacy, and retention

- Participation is voluntary and withdrawable.
- Explain what is recorded before the session.
- Do not require real names for party members.
- Prefer anonymous participant IDs.
- Screen or audio recording is opt-in, not assumed.
- Never commit raw recordings, real names, contact data, or unredacted save files to the public repository.
- Record a retention period and deletion owner before recruitment. Both are currently unknown.
- Published findings use aggregated results and scrubbed excerpts with consent.

## Analysis

Tag observations by `discovery`, `comprehension`, `control`, `feedback`, `fairness`, `pacing`, `comfort`, `accessibility`, `attachment`, and `replay`. Separate observed behavior from participant interpretation and moderator inference.

Every recommendation records:

- Finding ID
- Participant count and cohort
- Raw evidence location
- Confidence and limitation
- Requirement, risk, or design decision affected
- Proposed change and owner
- Verification study

## Execution and findings

Status: **not started**. Participants, consent method, dates, builds, results, deviations, and findings are unknown. This plan must be revised when an executable prototype exists.
