---
blueprint:
  documentId: OMT-BRIEF-001
  documentType: project-brief
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
  relatedArtifacts: [OMT-PRD-001, OMT-ARCH-001, OMT-GAME-001, OMT-AC-001, OMT-TEST-001, OMT-PLAY-001, OMT-RISK-001, OMT-PLAN-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omatrail project brief

> Draft for human review. The name and product direction are provided. Delivery estimates and success targets are proposals, not measured results or approvals.

## Requested decision

Approve a greenfield prototype for **Omatrail**, a native Omarchy Quattro survival game launched from the bar and played in a fullscreen overlay. The first funding gate is a playable hunting prototype. The full journey proceeds only if that prototype meets the playtest threshold in `OMT-PLAY-001`.

## Project context

| Field | Current state | Evidence state |
|---|---|---|
| Delivery stage | Concept and documentation | verified in repository |
| Audience | Omarchy desktop users and marketplace reviewers | derived from SR-003 and SR-008 |
| Product owner | Jeremy Longshore | derived from repository ownership; approval not recorded |
| Decision authority | Project owner plus named specialist reviewers | proposed; specialist names unknown |
| Classification | Public draft | derived from the public repository destination |
| Jurisdictions | Unknown | Requires legal and distribution review before release |
| Runtime constraint | Third-party code inside the shared `omarchy-shell` process | verified by SR-004 |
| Delivery constraint | Separate plugin repository, local-only runtime, marketplace validation | partly assumed and partly verified |

## Product thesis

Omatrail should recreate the remembered rhythm of a school-computer overland survival game without copying its code, artwork, writing, audio, or branded presentation. Players name a five-person party, buy supplies, manage a westward expedition, hunt, trade, cross rivers, endure illness and breakdowns, and try to arrive with survivors.

Two render profiles serve the two strongest visual memories:

1. **Green Monitor**, the default: black field, phosphor-green bitmap graphics, numbered menus, optional CRT effects.
2. **Color Deluxe**: original limited-color pixel art using the same layout, controls, mechanics, and save file.

## Evidence-backed opportunity

| Claim | State | Evidence |
|---|---|---|
| Omarchy supports `bar-widget` and fullscreen `overlay` plugin kinds. | verified | SR-003 and SR-004 |
| Native Omarchy games already demonstrate overlays, keyboard play, QML rendering, persistence, and pure JavaScript engines. | verified | SR-008 and linked public examples in OMT-ARCH-001 |
| Hunting was the best-known and heavily used activity in the 1985 design. | verified | Original lead designer account, SR-005 |
| River-crossing choices and outcome animations produced strong suspense in child playtests. | verified | Lead designer interview, SR-006 |
| The live catalog contains 83 game-tagged entries and no name or description match for Omatrail, Oregon Trail, wagon survival, or frontier survival. | verified snapshot | SR-002, generated 2026-09-06T21:34:36.021Z; the catalog changes continuously |
| Players will install and retain Omatrail. | unknown | Requires prototype and marketplace evidence |

## Objectives

| ID | Objective | Priority | Owner | Status | Verification |
|---|---|---:|---|---|---|
| OBJ-001 | Prove that hunting is enjoyable without relying on nostalgia alone. | P0 | Product owner | proposed | PLAY-001 and PLAY-002 |
| OBJ-002 | Deliver a complete, replayable expedition whose outcomes follow understandable decisions plus bounded uncertainty. | P0 | Product owner | proposed | TEST-006, TEST-007, PLAY-003 |
| OBJ-003 | Preserve the green-and-black memory while offering Color Deluxe without separate game rules or saves. | P0 | Design owner | provided | TEST-010 through TEST-012 |
| OBJ-004 | Ship as an offline, inspectable Omarchy plugin that does not destabilize the shared shell. | P0 | Engineering owner | derived | TEST-013 through TEST-018 |
| OBJ-005 | Treat historical people and events with care and avoid stereotyped or dehumanizing representation. | P0 | Content owner | proposed | CTRL-006 and human content review |

## Users

- **Primary:** Omarchy users who remember green-screen or early DOS educational games and want a short native desktop game.
- **Secondary:** Omarchy users without that nostalgia who enjoy deterministic survival, resource management, and replayable runs.
- **Affected groups:** People represented in the historical setting, including Indigenous nations whose portrayal requires sourced, specific, human review.

These are proposed segments, not validated personas. No interviews have been conducted.

## Scope

### Version 1.0

- Five-person named party and occupation choice
- Initial store and supply loading
- A complete route divided into three acts and geographically distinct regions
- Resource, pace, ration, health, morale, weather, calendar, and wagon-condition systems
- A full keyboard-first hunting minigame with regional animals and a carrying limit
- Multiple river-crossing strategies with suspenseful animated outcomes
- Hand-written events, illness, injury, breakdown, trading, landmarks, deaths, arrival, scoring, and replay
- Versioned local save and exact resume
- Green Monitor and Color Deluxe render profiles
- Keyboard and mouse controls, remapping, reduced motion, clean-pixel mode, and non-color status cues
- Pure JavaScript game engine and deterministic automated simulation

### Explicit exclusions

- Multiplayer, cloud saves, accounts, telemetry, advertisements, or paid content
- Generative AI, runtime network access, external APIs, or downloaded content
- A hunting-only product or a direct port of any commercial game
- Copied names, artwork, fonts, prose, audio, maps, sprites, or code
- Graphic violence

## Delivery recommendation

Use a gated vertical-slice strategy:

1. Hunting prototype
2. One complete trail leg with store, travel, event, river, save, and ending
3. Full engine and content
4. Dual render profiles and accessibility
5. Balance simulation, playtesting, security review, and marketplace submission

The current estimate is 15 to 25 focused working days for a polished 1.0, excluding waiting time for external playtests and marketplace review. Confidence is low to medium because the art owner, content volume, minimum Omarchy version, and review availability are unresolved.

## Assumptions and unknowns

| ID | State | Statement | Validation action |
|---|---|---|---|
| A-001 | assumed | The game will live in a new sibling plugin repository, not this umbrella repo. | Confirm before scaffolding |
| A-002 | assumed | Version 1.0 is single-player and offline. | Owner approval |
| A-003 | assumed | Keyboard-first desktop play is the primary input model. | Prototype playtest |
| A-004 | assumed | A successful run should take 20 to 40 minutes and support shorter saved sessions. | Timed playtests |
| U-001 | unknown | Exact year, route, landmarks, and historical content authority. | Commission source register and content review |
| U-002 | unknown | Art, audio, and historical-review owners. | Assign before vertical slice |
| U-003 | unknown | Final repository name, plugin ID, and license. | Decide before public scaffolding |
| U-004 | unknown | Trademark and content clearance for the final name and marketing comparison. | Legal review before listing |
| U-005 | unknown | Minimum supported Omarchy Quattro version. | Verify against current shell schema |
| U-006 | unknown | Whether any privacy-preserving local metrics will exist. | Default decision is no telemetry |

## Source register

| ID | State | Source | Use |
|---|---|---|---|
| SR-001 | provided | User decisions in this conversation, 2026-09-05 to 2026-09-06 | Name, hunting priority, Green Monitor and Color Deluxe |
| SR-002 | verified | [Omarchy live catalog](https://plugins.omarchy.org/catalog.json), generated 2026-09-06T21:34:36.021Z | Current game-plugin and collision snapshot |
| SR-003 | verified | [Develop a Custom Plugin](https://plugins.omarchy.org/develop.html) | Plugin kinds, validation, bar and panel lifecycle |
| SR-004 | verified | [Official omarchy-shell reference](https://docs.docuwriter.ai/omarchy-quattro/636811) | Runtime, manifest, overlay, IPC, and security boundary |
| SR-005 | verified | [R. Philip Bouchard: The Hunting Activity](https://www.philipbouchard.com/oregon-trail/hunting.html) | Primary-source hunting design history |
| SR-006 | verified | [Playing the Past interview](https://backstory.newamericanhistory.org/episodes/playing-the-past/1/) | Primary-source core-loop and river-crossing history |
| SR-007 | verified | [1985 screenshot archive](https://commons.wikimedia.org/wiki/Category:Screenshots_of_The_Oregon_Trail_(1985)) | Visual reference only, not reusable assets |
| SR-008 | verified | [Omarchy plugin umbrella README](../README.md) | Local architecture, testability, and security conventions |
| SR-009 | verified | [US Copyright Office: Games](https://www.copyright.gov/register/tx-games.html) | Idea-expression boundary; not trademark clearance |

## Human review

- Required: yes
- Status: not started
- Decision authority: project owner, unconfirmed
- Approval evidence: none
