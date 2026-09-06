---
blueprint:
  documentId: OMT-GAME-001
  documentType: frontend-and-gameplay-specification
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
  sourceRefs: [SR-001, SR-005, SR-006, SR-007, SR-009]
  assumptions: [A-003, A-004]
  unknowns: [U-001, U-002, U-004]
  relatedArtifacts: [OMT-BRIEF-001, OMT-PRD-001, OMT-ARCH-001, OMT-AC-001, OMT-TEST-001, OMT-PLAY-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omatrail game and experience specification

> The gameplay, visual, and story treatments below are design proposals. Original game screenshots are references for historical analysis only and are not asset sources.

## Experience promise

**Name your party. Pack your wagon. Hunt, trade, cross rivers, and try to get everyone west alive.**

Omatrail should feel immediately legible to someone who remembers a green-screen school computer while remaining a fair, coherent survival game for someone without that memory.

## Design pillars

1. **Hunting is a game, not a button.** It receives the first prototype and the largest single gameplay investment.
2. **Named people make consequences matter.** Health, disagreement, competence, injury, and death attach to party members rather than anonymous lives.
3. **Preparation echoes forward.** Store and route decisions create later advantages and failures that the player can understand.
4. **Uncertainty creates stories, not arbitrary punishment.** Randomness is seeded, bounded, and modified by visible conditions.
5. **The journey has place.** Terrain, animals, weather, landmarks, and available decisions change across regions.
6. **The old monitor is a mode, not a usability excuse.** Green Monitor stays stark while focus, remapping, reduced motion, and readable alternatives remain available.

## Core loop

```text
Prepare -> Choose pace/rations/action -> Travel -> Encounter or landmark
    ^                                               |
    |                                               v
Review supplies <- Camp/trade/repair/rest/hunt <- Resolve consequence
```

One normal travel turn represents several days. A turn should take 15 to 45 seconds unless the player enters hunting, a river crossing, trading, or a major story scene.

## Journey structure

### Prologue: departure

- Name five party members.
- Choose an occupation and difficulty.
- Select departure month.
- Buy supplies under a fixed budget.
- Receive advice that can be ignored.

### Act I: open country

- Teaches pace, rations, rest, trade, hunting, and shallow crossings.
- Consequences are recoverable but visible.
- Party relationships begin through short linked events.

### Act II: distance and scarcity

- Prices rise, routes split, terrain changes, and repairs matter.
- Illness and injury interact with prior fatigue.
- Hunting becomes region-specific and less predictable.
- Decisions about helping, trading, waiting, or leaving reshape later events.

### Act III: cold and commitment

- Weather closes options and punishes a late calendar.
- Mountain travel stresses oxen, wagon, health, and supplies.
- Major crossings and the final route demand explicit risk choices.
- Arrival reflects who survived, what was sacrificed, time, waste, and difficulty.

Exact historical route, nations, dates, and landmark copy remain U-001 until sourced and reviewed.

## Party and story model

The player names the party. Each member has health, fatigue, morale, one occupation-linked competence, current conditions, and a compact relationship state. Story content uses modular chains rather than one fixed novel.

Proposed chain types:

- A worsening symptom that can be disclosed, hidden, treated, or ignored
- Disagreement about pace or rationing
- A member becoming the party's best hunter, medic, repairer, trader, or navigator
- A promise to help another traveler later on the route
- Grief, fear, and morale changes following loss
- A companion considering remaining at a settlement

Events shall not invent melodrama that overrides the simulation. Every branch must expose the decision, immediate consequence, and any persistent flag used later.

## Hunting specification

### Session

- Duration: proposed 60 to 90 seconds, tuned by playtest
- View: top-down, full game canvas
- Movement: eight directions
- Aim: eight directions, independently controllable
- Fire: deliberate single shot with a visible cooldown appropriate to the chosen weapon
- Exit: time expires, ammunition is depleted, the player returns, or the player abandons

Default keyboard mapping:

| Action | Default |
|---|---|
| Move | `W A S D` |
| Aim | Arrow keys |
| Fire | `Space` |
| Move quietly | `Shift` |
| Return | `R` with confirmation |
| Pause/close | `Esc` |

Mouse aiming and firing are supported. Remapping is required before release.

### Regions and field generation

| Region | Terrain vocabulary | Proposed animals | Play effect |
|---|---|---|---|
| Eastern woodland | deciduous trees, brush, creek | rabbit, turkey, deer | Short sightlines |
| Plains | tall grass, shallow gullies, rock | rabbit, pronghorn, bison | Long sightlines, fast prey |
| Rocky Mountains | conifers, boulders, slopes | deer, elk, bear | Occlusion and elevation |
| High desert | scrub, rock, dry channels | rabbit, pronghorn | Sparse cover and heat |
| Western forest | dense conifers, fallen timber | deer, elk, bear | Close encounters |

Animal list and range are provisional until U-001 closes. Field generation uses a seed and a validated obstacle budget so the hunter and animals always have navigable space.

### Hunting economy

- A hunt consumes part of a day and party energy.
- Every shot consumes ammunition.
- Meat yield reflects animal type and shot outcome.
- The player may carry only a bounded amount back.
- The results screen reports harvested, carried, and wasted amounts.
- Meat spoils over time unless a later approved preservation mechanic exists.
- Repeated indiscriminate waste affects score and may affect morale.
- Hunting risk includes becoming lost, minor injury, weather exposure, or a defensive animal encounter. Risk must be telegraphed and capped.

Hunting cannot be the only winning strategy. Store-heavy, trade-heavy, and careful-ration strategies remain viable.

## River crossings

The player sees river width, depth, current, recent weather, wagon condition, party condition, price, and available help before choosing. Not every option appears at every crossing.

Proposed actions:

- Ford
- Caulk and float
- Pay for ferry
- Hire a knowledgeable guide
- Wait for conditions to change
- Seek another route

After commitment, controls disappear and a slow animation shows the wagon crossing. The animation is not cosmetic filler: its duration holds the uncertainty. Outcome factors are logged in the post-scene explanation without revealing raw random numbers.

## Visual system

### Shared canvas

- Semantic game canvas: `320 x 200`
- Integer scaling when display geometry permits
- Letterbox rather than stretch
- Shared layout and hitboxes across both display profiles
- Pixel snapping for sprites, text, and rules

### Green Monitor, default

| Token | Value | Use |
|---|---|---|
| `phosphor.black` | `#020603` | Canvas |
| `phosphor.dim` | `#1F7A35` | Terrain and secondary rules |
| `phosphor.main` | `#63FF73` | Text and ordinary sprites |
| `phosphor.hot` | `#B6FFB9` | Focus, muzzle flash, urgent cue |

- Original bitmap font with a redistribution record
- No modern cards, gradients, faux parchment, or multicolor decoration
- Optional subtle scanlines, bloom, persistence trail, and rare flicker
- CRT effects default to subtle and disable under reduced motion
- `Clean pixels` disables scanlines, flicker, bloom, and persistence

### Color Deluxe

- Original 16-color maximum scene palette, refined after art exploration
- Same canvas, typography metrics, object silhouettes, menus, and focus order
- Color may distinguish regions and status but never carries meaning alone
- No traced or recreated commercial sprites, borders, maps, or title treatments

### Screens

| Screen | Primary job | Signature element |
|---|---|---|
| Title | Start, continue, settings, credits | Wagon silhouette crossing the phosphor horizon |
| Party | Name people and choose occupation | Five compact name rows |
| Store | Build a loadout under budget | Text ledger and remaining cash |
| Trail | Read conditions and choose next action | Small moving wagon scene above status lines |
| Landmark | Establish place and offer context | One strong pixel illustration |
| Hunting | Skill-based food acquisition | Full canvas field with minimal HUD |
| River | Understand conditions and commit | Wide water animation with no outcome preview |
| Event | Read and decide | Stark prose plus numbered actions |
| Supplies | Inspect and reorganize inventory | Plain ledger, sortable only if needed |
| Ending | Explain the journey | Survivor list, route facts, score, waste, and seed |

## Audio

Audio is original, optional, and muted by a single control. Proposed sounds are restrained: keyboard chirp, menu confirm, wagon creak, river, wind, shot, animal movement, illness cue, and arrival motif. No continuous music is required for the prototype. Audio ownership is U-002.

## Accessibility and comfort

- Full keyboard operation and visible focus
- Mouse alternatives for all gameplay
- Remappable movement, aim, fire, pause, and menu controls
- Reduced-motion mode
- Clean-pixel mode
- Adjustable CRT strength
- Non-color status icons and labels
- Text-speed control and instant text option
- Paused hunting when focus is lost
- No required rapid repeated input
- Hunting difficulty assists: larger target silhouettes, slower animals, extended time, aim hold, and optional single-stick movement/aim mode

## Content and representation controls

- Historical claims require a source ID.
- Fictional people are labeled as composites in credits.
- Indigenous nations are named specifically when supported, not treated as a generic encounter category.
- Trade, guidance, sovereignty, conflict, disease, displacement, and migration require content review appropriate to the claim.
- Hunting avoids graphic depiction and does not reward unnecessary kills.
- No shipped copy uses the famous commercial game's exact event text, interface text, jokes, or epitaphs.

## Open design decisions

| ID | Unknown | Decision gate |
|---|---|---|
| U-001 | Route, year, landmark list, animal range, historical source authority | Before full content writing |
| U-002 | Art, audio, and content-review owners | Before vertical slice |
| U-004 | Name and comparison-marketing clearance | Before public listing |
| UX-001 | Whether Green Monitor uses simulated phosphor persistence by default | Prototype comfort test |
| UX-002 | Whether hunting uses independent movement and aim or a simpler direction lock by default | Hunting playtest |
| UX-003 | Whether death allows an epitaph | Content and IP review |
