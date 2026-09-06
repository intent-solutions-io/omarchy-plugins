---
blueprint:
  documentId: OMT-ARCH-001
  documentType: architecture-description
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
  sourceRefs: [SR-003, SR-004, SR-008]
  assumptions: [A-001, A-002, A-003]
  unknowns: [U-003, U-005]
  relatedArtifacts: [OMT-BRIEF-001, OMT-PRD-001, OMT-GAME-001, OMT-AC-001, OMT-TEST-001, OMT-RISK-001, OMT-PLAN-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omatrail system architecture

> Proposed architecture aligned with the current Omarchy Quattro plugin contract. It is not implementation evidence.

## System of interest and concerns

Omatrail is one third-party plugin loaded inside the long-running `omarchy-shell` process. Its primary architectural concern is therefore containment by simplicity: deterministic pure rules, bounded local state, no network, no background service, and no recurring work while hidden.

| Stakeholder | Concern | View |
|---|---|---|
| Player | Fast open, reliable save, responsive input, legible display | Runtime and UX |
| Product owner | Hunting quality, complete journey, replayability | Gameplay |
| Shell maintainer | Plugin lifecycle, focus, memory, failure containment | Runtime |
| Marketplace reviewer | Manifest, permissions, provenance, removal | Deployment and trust |
| Developer/tester | Determinism, headless tests, debuggable state | Code and verification |
| Historical/content reviewer | Source quality and representation | Content governance |

## Architecture decisions

| ID | Decision | Status | Rationale | Revisit trigger |
|---|---|---|---|---|
| ADR-001 | Implement as native QML plus plain JavaScript. | proposed | Matches the host and preserves headless rule tests. | QML cannot meet measured hunting input or frame targets. |
| ADR-002 | Declare `bar-widget` plus `overlay`; the bar summons the overlay over shell IPC. | proposed | Keeps discovery in the bar and gameplay on a focused surface. | Current multi-kind manifest validation rejects the combination. |
| ADR-003 | Use a reducer-like deterministic engine: `(state, action, rng) -> state + effects`. | proposed | Replay, simulation, save debugging, and property tests use the same rules. | Profiling shows unacceptable copy cost. |
| ADR-004 | Seed randomness per expedition and persist the seed plus stream position. | proposed | Exact reproduction of failures and fair balance analysis. | Cryptographic unpredictability becomes a requirement, which is not expected. |
| ADR-005 | Separate semantic scene state from Green Monitor and Color Deluxe render profiles. | provided direction | Both displays must play the identical game and share saves. | Human review changes the two-mode requirement. |
| ADR-006 | Store one versioned JSON save plus a last-good backup under a plugin-specific local-state directory. | proposed | Inspectable, bounded, recoverable, and consistent with local-only scope. | The shell exposes a safer first-party persistence API. |
| ADR-007 | Bundle only original or redistribution-cleared assets and content. | proposed | Supports offline play and the IP boundary. | None; this is a release control. |

## Logical components

```text
BarWidget.qml
    | summon / hide
    v
GameOverlay.qml ----> InputRouter.qml
    |                       |
    | semantic view model   | actions
    v                       v
GameController.js ----> GameEngine.js ----> SeededRandom.js
    |                       |  |  |  |
    |                       |  |  |  +--> ScoreRules.js
    |                       |  |  +-----> RiverRules.js
    |                       |  +--------> HuntingRules.js
    |                       +-----------> TravelRules.js
    |
    +--> ContentRegistry.js ----> content/*.json
    +--> SaveStore.qml ---------> local versioned JSON + backup
    +--> RenderProfile.qml -----> GreenMonitor.qml / ColorDeluxe.qml
```

### Component registry

| ID | Component | Responsibility | Prohibited responsibility |
|---|---|---|---|
| CMP-001 | `BarWidget.qml` | Display inactive icon or bounded expedition cue; request overlay lifecycle. | Game rules, persistence, background polling |
| CMP-002 | `GameOverlay.qml` | Own the fullscreen surface, focus lifecycle, scene switching, and close behavior. | Random outcome calculation |
| CMP-003 | `InputRouter.qml` | Map keyboard and mouse events to semantic actions; honor remapping. | Mutate state directly |
| CMP-004 | `GameController.js` | Coordinate engine, content, persistence, and view model. | Render QML items |
| CMP-005 | `GameEngine.js` | Validate actions and produce deterministic state transitions. | Filesystem, clock, shell, or QML access |
| CMP-006 | Rules modules | Travel, hunting, river, health, inventory, event, and score logic. | Direct UI or file access |
| CMP-007 | `SeededRandom.js` | Reproducible random stream. | Hidden use of system randomness after run creation |
| CMP-008 | `ContentRegistry.js` | Load and validate immutable event, landmark, animal, and item records. | Execute content as code |
| CMP-009 | `SaveStore.qml` | Atomic write, last-good backup, schema migration, deletion, and bounded read. | Network or writes outside its state directory |
| CMP-010 | Render profiles | Map semantic colors, sprites, type, and effects to the same scene geometry. | Change game outcomes or hitboxes |

## Runtime flows

### Open and resume

1. `CMP-001` asks the shell to summon Omatrail.
2. `CMP-002` acquires focus and requests a load from `CMP-009`.
3. `CMP-009` parses within a byte cap, validates schema, and returns valid state, migrated state, no state, or recoverable failure.
4. `CMP-004` initializes `CMP-005` and builds a semantic view model.
5. `CMP-010` renders the selected profile.

### Player action

1. `CMP-003` emits a semantic action such as `HUNT_FIRE`, `SET_PACE`, or `RIVER_CHOOSE`.
2. `CMP-005` rejects an action illegal for the current state or returns next state plus explicit effects.
3. `CMP-004` publishes the view model and asks `CMP-009` to persist after consequential actions.
4. Presentation-only animation never feeds back into outcome logic.

### Close

1. `CMP-002` blocks duplicate input and commits the last confirmed state.
2. All active timers and animations stop.
3. Focus returns through the shell lifecycle.
4. `CMP-001` displays a bounded cue derived from saved state.

## Deployment view

```text
public Git repository
  -> omarchy plugin add
  -> ~/.config/omarchy/plugins/<plugin-id>/
  -> manifest validation
  -> disabled review state
  -> user enables plugin
  -> omarchy-shell loads QML and JavaScript with user permissions
```

There is no server, API, account, daemon, database, or privileged helper.

## Trust boundaries and controls

| Boundary | Exposure | Control | Evidence |
|---|---|---|---|
| Plugin repository to user machine | Mutable upstream code runs as the user. | Reviewed commit, manifest capability review, documented install/remove, no installer script required. | CTRL-003, TEST-013, TEST-017 |
| Content to engine | Malformed records could break gameplay. | Data-only JSON schema, size caps, unique IDs, no executable expressions. | CTRL-004, TEST-009 |
| Save file to shell process | Corrupt or hostile local file could allocate memory or crash parsing. | Descriptor-safe open where available, byte cap, strict schema, migration allowlist, last-good backup. | CTRL-002, TEST-016 |
| Overlay to desktop input | Keys could leak or focus could remain captured. | Explicit focus state machine, close-path matrix, no global key listener. | TEST-014, TEST-018 |
| Renderer to game rules | A profile could change visibility or mechanics. | Shared geometry and semantic state, snapshot comparison, non-color cues. | TEST-010 through TEST-012 |

## Failure modes

| Failure | Required behavior |
|---|---|
| Missing save | Offer a new journey without an error state. |
| Corrupt save | Preserve the file, offer last-good recovery or confirmed restart, never crash the shell. |
| Unknown future save version | Refuse destructive downgrade and explain the compatible recovery path. |
| Missing optional asset | Use a bounded fallback glyph and record a visible development error. |
| Content reference missing | Fail validation before release; at runtime skip the record without corrupting state. |
| Overlay loses focus | Pause hunting and await explicit resume. |
| Shell closes during write | Recover the prior atomic file or last-good backup. |
| Rendering frame overrun | Reduce cosmetic effects; never alter simulation timing. |

## Diagram inventory and conclusions

- Nodes: bar widget, overlay, input router, controller, deterministic engine, rules, RNG, content registry, save store, render profiles.
- Relationships: lifecycle calls flow from bar to overlay; actions flow from input to engine; semantic state flows to renderers; confirmed state flows to the save store.
- Trust boundaries: repository installation, local save input, static content input, desktop focus, renderer isolation.
- Conclusion: native QML is feasible only if the shell-facing layer stays thin and all consequential rules remain headlessly testable.

## Known inconsistencies and unknowns

- The current umbrella template describes nested panels, while Omatrail proposes a separate overlay. The implementation must start from a current overlay example rather than mechanically copying the widget template.
- The final minimum Omarchy version and exact multi-kind manifest behavior remain U-005.
- The final plugin ID and repository remain U-003.
- No implementation or runtime evidence exists yet.
