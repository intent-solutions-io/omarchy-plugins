---
blueprint:
  documentId: KTA-UX-001
  documentType: frontend-and-game-specification
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
  sourceRefs: [KTA-BRIEF-001, KTA-PRD-001, KTA-AUDIENCE-001, SR-102, SR-110, SR-113, SR-117, SR-118]
  assumptions: [A-102]
  unknowns: [U-101, U-102, U-103, U-106]
  relatedArtifacts: [KTA-ARCH-001, KTA-AC-001, KTA-TEST-001, KTA-PLAY-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure learning and game experience

> This defines the experience shape, not final story, art, lesson sequence, or learning claims. Those require child research, original creative work, and specialist review.

## Experience principles

1. Game first in the child's language, learning first in the system's rules.
2. Accuracy earns control. Speed emerges after stable technique.
3. Every prompt belongs to the world and causes something visible.
4. Correction is private, specific, and brief.
5. Progress is mastery, not an addictive streak.
6. Sessions end cleanly and never punish a child for leaving.
7. Characters are expressive and customizable, never curriculum stereotypes.
8. Omarchy is a special home, not a prerequisite for understanding the game.

## Spectacle, creation, AI, and Omarchy translation

The experience may borrow four abstract patterns while remaining original:

- Challenge spectacle: explain the goal in seconds, escalate through visible world changes, and end with a memorable payoff. Stakes must come from the mission, never loss aversion, public humiliation, spending pressure, or compulsive retention.
- Inhabitable sandbox energy: make the restored world worth revisiting and let mastery unlock more ways to solve or decorate it. Initial play is authored and offline. Open chat, public UGC, public profiles, virtual currency, and unsupervised multiplayer are excluded.
- Bounded AI: start with human-reviewed authoring support and deterministic local adaptation. No open-ended child conversation, downloaded prompt execution, undisclosed model call, training on child input, or learner-data upload is permitted.
- Omarchy identity: keyboard-first navigation, theme-aware but kid-tested presentation, Linux-native responsiveness, and a later in-world shortcut workshop after foundational typing.

Two kid-facing art directions must be tested without brand explanations. Omarchy supplies craft and interaction discipline; it must not force every game scene into a restrained adult terminal aesthetic.

Roblox's current age-checked population supports a non-childish treatment, not an adult-only target. Test ages 9 to 11 and 12 to 14 as separate candidate cohorts and report results separately. The same learning model may vary reading load, humor, character presentation, challenge framing, and visual intensity without gendered or age-stereotyped rewards. See KTA-AUDIENCE-001.

## Prototype fantasy, not selected mechanic

Test an original "restore the signal" adventure as one fantasy direction. A playful world has lost its routes, lights, machines, and stories. Typed signals may repair paths, steer vehicles, build devices, and outsmart nonviolent hazards. Each region can represent a skill family, but the metaphor must not expose a school worksheet underneath.

This is neither approved story canon nor a defined mechanic. Before production code, a senior game designer must specify and greybox three candidates. Each candidate names the player goal, meaningful choices, state or resources, typing-to-action mapping, opposition, failure and recovery, untimed and accessible form, and replay hook. A child must be able to explain why an action was chosen. If removing typing leaves the same game with a different input device, or if typing only triggers decorative feedback, the candidate fails.

## Core session loop

```text
choose mission
    -> see one clear skill goal
    -> learn with hand/key guidance
    -> practice without time pressure
    -> use the skill in an active mission
    -> face a short set-piece
    -> receive specific result and next choice
    -> stop cleanly or continue
```

### Ten-minute example

1. A character asks the learner to route three signals using `f`, `j`, space, and previously mastered keys.
2. A 45-second teach scene shows resting position and lets the child mirror it without score.
3. A two-minute greybox treats the earliest keys honestly as signals or controls, not fake words. Accurate sequences choose routes, allocate limited power, or time a safe action. A recoverable error changes the state without shaming the learner.
4. A three-minute vehicle scene uses the same keys in phrases, with pace based on recent stable accuracy.
5. A one-minute set-piece asks for three calm, accurate lines. There is no death screen.
6. A results scene says what improved, one key to watch, and whether the next mission is ready.

## Curriculum shape

The final ordering is U-102. The product model should support:

| Stage | Learning purpose | Game expression |
|---|---|---|
| Orientation | posture, resting fingers, space, return, focus | wake a console and choose a character |
| Home anchors | reliable `f` and `j` plus home-row groups | stabilize a base and connect local routes |
| Reaches | introduce small groups with controlled vocabulary | repair tools and explore new zones |
| Shift and capitals | coordinated opposite-hand shift | decode names, signs, and signal headers |
| Punctuation | rhythm and sentence construction | transmit messages and program machines |
| Numbers and symbols | accuracy with top row and modifiers | navigate coordinates and build devices |
| Fluency | phrases, prose, code-like patterns by mode | longer missions with strategic choices |
| Omarchy academy | approved current shortcuts in a sandbox | operate an in-world desktop or workshop |

No stage should infer mastery from one fast run. A proposed mastery state uses recent accuracy, independent correct attempts, spaced recall, hesitation, and error concentration. Exact weights require learning review and simulation.

## Candidate sports technology track

Sports is a credible world theme because the keyboard can control real information work instead of merely typing sports vocabulary. The track should be researched and greyboxed under `bd_000-projects-v41u.2.14`; it is not part of the first Signal Rescue slice yet.

Candidate mission families include:

| Mission family | Meaningful typed action | Visible consequence | Real-world doorway |
|---|---|---|---|
| Live game data | enter and correct fictional play events, formations, substitutions, or split times | a tactical display and scoreboard update from accurate records | data operations and sports analytics |
| Broadcast desk | log highlights, cue graphics, caption a short call, and route a replay | the fictional show assembles correctly and viewers receive the right context | broadcast operations and accessibility |
| Scouting lab | tag fictional clips, compare patterns, and write a concise evidence-based note | a game plan changes based on the selected evidence | scouting technology and data literacy |
| Sensor garage | calibrate a fictional sensor, label readings, and detect an impossible value | a training machine or equipment prototype responds safely | embedded systems, wearables, and hardware testing |
| Team operations | resolve a fictional travel, equipment, or scheduling conflict | the team reaches the event with the right resources | logistics, software, and operations |

The design must use fictional teams, leagues, athletes, uniforms, marks, statistics, and broadcasts unless rights are documented. It must not collect real health, location, school, team, injury, biometric, or athletic-performance data from a child. It must not promise a career outcome or imply that technology is only a fallback for an athlete. Girls and boys receive the same sports, roles, equipment, challenge, colors, and learning paths.

The research should compare at least three framings: competitive strategy, behind-the-scenes production, and build-the-equipment engineering. The winning theme must still pass the core causal test: removing accurate typing should materially break the decision loop, not simply remove a text field from an otherwise unchanged sports game.

## Input feedback hierarchy

| Event | Immediate feedback | Persistent effect |
|---|---|---|
| Correct key | motion, light, or construction response within NFR-101 | bounded progress evidence |
| Incorrect key | strict correction during instruction; recoverable in-world consequence during missions; coaching between action beats | error pattern count, not public penalty |
| Repeat key | ignore or treat once according to lesson policy | diagnostic counter only |
| Focus loss | pause scene and timing | safe checkpoint |
| Paste or automation | exclude from mastery credit without punishing the learner; distinguish accessibility and input-method behavior | bounded diagnostic reason only |
| Composition/dead key | follow declared locale policy | no false error until composition resolves |
| Escape | pause or leave with confirmation appropriate to state | safe checkpoint |

## Character settings

Character creation presents several equally prominent original heroes, plus edit, randomize, and quick-start. Appearance features are interchangeable and pronouns are optional. A child never has to choose a gender category to customize a character. The learner can change presentation without resetting progress. The profile defaults to a generated callsign and warns not to enter a real name.

The UI must never ask a child for legal name, age, school, location, photo, voice, or contact information. If an age band is needed for curriculum, the parent chooses a coarse band in parent mode and the reason is explained.

## Parent experience

Parent mode should answer five questions:

1. What has my child practiced?
2. Is accuracy stable enough to move on?
3. Which keys need calm practice?
4. How do I change accessibility, export, reset, or delete data?
5. What does paid unlock, and how do refunds and recovery work?

The dashboard should avoid ranking siblings, predicting intelligence, diagnosing conditions, or converting every activity into surveillance. It shows skill evidence, recent session length, accuracy bands, assistance used, and suggested next practice. Raw keystroke histories and typed story content are not shown or retained.

## Visual direction

Use Omarchy's restrained dark surface, precise spacing, terminal-informed typography, and active theme colors without turning the product into a developer joke. The game world can be vivid, but navigation, settings, and progress should feel like a polished Intent Solutions product.

Recommended rules:

- One strong accent per scene, derived from the current Omarchy palette when available
- Original illustration and animation, not copied retro software screens
- A legible text face for prompts and a distinctive display face only for short headings
- Visible keyboard and finger guidance that can be hidden after mastery
- No fake scanlines by default, excessive bloom, confetti loops, or neon overload
- Motion communicates cause and direction, not decoration
- Success effects stay below a short duration and respect reduced motion
- Error colors always pair with shape, icon, text, or position

## Audio direction

- Short responsive sounds for correct action, distinct but gentle correction, scene completion, and navigation
- Separate master, music, voice, and effect controls if voice is later approved
- No required voice input or child recording
- No harsh buzzer, mocking character line, or escalating failure music
- Captions or textual equivalents for instructional audio
- Original recordings or licensed assets with source, license, author, modification, and distribution evidence

## Accessibility contract

- All non-game navigation is semantic DOM with visible focus.
- Canvas scenes expose the current prompt, state, and controls through an accessible companion structure.
- No essential action is timed. Untimed mode preserves the complete free-world decision loop, not merely instruction and practice.
- Gameplay pauses when focus leaves the app.
- Reduced motion replaces camera movement and particles with bounded state changes.
- Font size and line spacing can increase without hiding the target or controls.
- Color contrast meets the adopted WCAG target for UI text and controls.
- Supported one-handed and motor-assistance paths are defined and tested before claiming support.
- Screen-reader, captions and visual audio equivalents, remapping, reflow and zoom, one-handed use, contrast, reduced motion, flash thresholds, and a non-canvas equivalent path have complete free-world criteria. Automated scans are not treated as proof.

Every supported accessibility audience must be able to finish the entire free world through an equivalent enjoyable path. An unsupported path requires a specific reviewed public limitation, not a vague accessibility claim.

## Anti-cheese test

A feature fails the tone gate if it does any of the following:

- Calls an ordinary drill an "epic quest" while the typed text has no game consequence
- Uses slang written by adults to imitate children
- Gives coins for meaningless clicking or key mashing
- Adds a mascot who constantly praises trivial input
- Hides a conventional worksheet behind excessive animation
- Uses gendered color, difficulty, or reward assumptions
- Treats WPM as the only achievement
- Punishes breaks with a lost streak

## Content governance

Every lesson and story asset must have a stable ID, owner, version, reading-level result, age-band rationale, skill mapping, provenance record, sensitivity note, accessibility note, and review status. Generated text or imagery may not enter a release without the same human editorial and rights review as commissioned content.

## Prototype questions

- Do children understand what they are trying to accomplish before typing begins?
- Does the mission remain fun when effects are reduced?
- Do children look at the on-screen keyboard too much or at the physical keyboard less over time?
- Does specific correction help, annoy, or interrupt flow?
- Do avatar options feel expressive without becoming the whole product?
- Can a parent explain the skill map in under two minutes?
- Does the free world feel complete enough to earn trust?
- Does the paid boundary feel like more product rather than withheld safety or remediation?
