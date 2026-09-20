---
blueprint:
  documentId: KTA-PLAY-001
  documentType: playtest-usability-plan
  schemaVersion: 1.0.0
  templateVersion: 3.0.0
  status: draft
  owner: Jeremy Longshore
  authors: ["Intent Solutions / Codex"]
  reviewers: []
  approvers: []
  generatedAt: 2026-09-10
  updatedAt: 2026-09-10
  classification: restricted-draft
  sourceRefs: [KTA-BRIEF-001, KTA-PRD-001, KTA-UX-001, KTA-PRIV-001, KTA-AC-001]
  assumptions: [A-102]
  unknowns: [U-102, U-103, U-105]
  relatedArtifacts: [KTA-TEST-001, KTA-RISK-001, KTA-OPS-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure playtest and usability plan

> No study has run. Participant targets and pass bands are proposals. Guardian consent, privacy review, and child-safe research procedures are required before recruiting minors.

## Research questions

| ID | Question | Decision informed |
|---|---|---|
| PLAY-101 | Does the child understand the game goal before the typing lesson is explained? | fantasy and onboarding |
| PLAY-102 | Does typing feel like the control system, or like a drill between rewards? | core loop |
| PLAY-103 | Does accuracy-first coaching improve technique without reducing willingness to continue? | mastery and feedback |
| PLAY-104 | Can a child complete the vertical slice with only bounded facilitator help? | slice readiness |
| PLAY-105 | Is a 10 to 20 minute session satisfying, and can the child stop without pressure? | session design |
| PLAY-106 | How do children react emotionally to errors, assistance, replay, and result language? | child safety and tone |
| PLAY-107 | Do character options feel inclusive and meaningful without affecting curriculum expectations? | representation |
| PLAY-108 | Can a parent understand progress, privacy, deletion, and the free/paid boundary? | parent experience |
| PLAY-109 | Does the free world feel complete, and does paid expansion feel fair? | monetization |
| PLAY-110 | Do reduced-motion, sound-off, large-text, and untimed modes preserve play value? | accessibility |
| PLAY-111 | Do ages 9 to 11 and 12 to 14 interpret the presentation as being for players like them without either cohort feeling excluded or patronized? | audience selection |
| PLAY-112 | Do original challenge clarity, escalation, world agency, and visible creation increase voluntary replay without reducing comprehension or calm accuracy? | attention-quality hypothesis |

## Study stages

### Preconditions for any minor participation

- A qualified human records the applicable IRB or research-ethics determination.
- Versioned guardian consent, age-appropriate assent and comprehension, continuing dissent, recruitment, compensation, facilitator conduct, adverse-event, withdrawal, and deletion procedures are approved.
- A separate research data-management plan and protected store are operational. Research-recruitment interest in CRM is not study consent.
- A curriculum evidence review, supported audience definition, and public-claim registry exist.

### Stage A: Co-design and paper prototype

- Participants: six to ten children with at least three in each candidate cohort, ages 9 to 11 and 12 to 14, plus their parents or guardians; exact sampling requires protocol approval
- Build: character sheets, story map, three mechanic cards, an attractive neutral alternative, a minimally dressed drill with matched prompts, and a fake progress screen
- Goal: reject weak fantasy, tone, character, and parent-dashboard assumptions before code
- Capture: facilitator notes and coded task outcomes; no child photo, voice, or public name
- Gate: pre-registered numeric thresholds cover causal-loop comprehension, age-fit and babyishness signals by cohort, unprompted replay choice against the attractive alternative, frustration, abandonment, and mashing. Stage A is formative and never estimates population efficacy.

### Stage B: Instrumented vertical slice

- Participants: eight to twelve children with at least four in each candidate cohort, balanced where practical across current typing comfort and stated character preference; guardians present or following approved protocol
- Build: local-only app with onboarding, teach, practice, mission, set-piece, result, and parent view
- Goal: test comprehension, input behavior, enjoyment, correction, session length, and recovery
- Capture: local study IDs, task events needed for research, observation notes, pre/post probes, and deletion date
- Gate: no safety stop; pre-registered thresholds for onboarding, why an action was chosen, typing-as-control, age fit by cohort, unprompted replay against equally prominent stop and alternate options, frustration, abandonment, correction comprehension, and mashing. Supported accessibility paths are represented. Stage B remains formative.

### Stage C: Closed free-world pilot

- Participants: 20 to 30 family units using supported Omarchy devices where possible
- Duration: two to four weeks
- Goal: repeat use, learning progress, installation, crashes, family-profile needs, and support load
- Capture: prefer parent-submitted weekly survey and local export over automatic telemetry
- Gate: proposed MET-101 repeat-session threshold, no severe data-loss or privacy incident, and acceptable support burden

### Stage D: Paid-boundary pilot

- Participants: parents from the closed pilot, after a price study
- Goal: purchase comprehension, refund expectation, recovery, device rules, and fairness
- No child sees checkout or pricing during testing
- Gate: policies are understood without facilitator interpretation and recovery works during a simulated service outage

## Participant safety

- Obtain guardian consent and child assent in age-appropriate language.
- State that the child is testing the product and cannot fail the study.
- Permit stopping at any moment without losing compensation or progress.
- Do not collect legal names in study artifacts unless a separately protected consent record requires them.
- Do not record screen, voice, face, or hands by default. Any recording needs a specific purpose, access list, retention date, and separate consent.
- Use study IDs in notes and evidence.
- Never ask a child to type personal facts, passwords, addresses, school, team, birthday, email, or phone.
- Stop immediately for distress, pain, repeated frustration, flashing sensitivity, or privacy surprise.
- Keep raw research evidence restricted and publish only reviewed aggregate findings.

## Session protocol

1. Guardian completes consent and data-use review.
2. Facilitator explains that the game is being tested.
3. Child selects a character without facilitator steering.
4. Child attempts first launch and onboarding while facilitator remains silent unless the help threshold is reached.
5. Child plays one teach, practice, mission, and result sequence.
6. Facilitator asks neutral questions: "What do you think happened?", "What would you do next?", and "Was anything annoying or confusing?"
7. Child may choose to stop or play a second mission.
8. Parent attempts the progress, accessibility, export, and deletion explanation tasks.
9. Facilitator records coded outcomes and deletes temporary local test data according to protocol.

The facilitator records guardian prompting or observation influence. Voluntary return means an unpressured child choice with a genuinely attractive stop or alternative activity. Parent-reported use alone is not voluntary-return evidence.

Avoid leading questions such as "Was the animation fun?" or "Would you pay for this?" Use observable choices and parent tradeoff questions.

## Measures

| Measure | Method | Interpretation limit |
|---|---|---|
| Onboarding completion | observed task | does not prove learning |
| Help interventions | coded count and reason | facilitator consistency required |
| Accuracy by introduced skill | local pre/post probes | short-term gain is not durable mastery |
| Delayed retention and transfer | pre-registered follow-up and untaught transfer task | required before any durable-learning claim |
| Physical keyboard looking | observation sample | must not shame or over-interpret |
| Voluntary continuation | explicit choice with easy stop | novelty can inflate first-session interest |
| Error recovery | time and attempts after feedback | accessibility aids must be recorded |
| Parent progress comprehension | explain-back task | small sample is directional |
| Age fit and babyishness | neutral explain-back, self-placement, and observed rejection signals reported by cohort | small samples do not select a population alone |
| Parent price reaction | structured price research after free gameplay proof | stated intent is not purchase behavior and child attention is not parent demand |

Before an efficacy claim, pre-register population, exposure dose, baseline, primary outcome, validated or specialist-reviewed probe, immediate result, delayed retention, transfer, assistance handling, missing-data rule, analysis, and minimum meaningful threshold. Usability evidence never substitutes for learning evidence.

## Segmentation without stereotyping

Analyze results separately for ages 9 to 11 and 12 to 14, then by reading comfort, prior typing exposure, keyboard layout, accessibility settings, and session context. Do not publish a combined result that hides a poor cohort outcome. Character choice may be observed, but presentation settings must not create different curriculum or imply ability. Small samples must not be presented as demographic conclusions.

## Severity and disposition

| Severity | Example | Action |
|---|---|---|
| S0 safety/privacy | unexpected network data, distress, seizure risk, parent gate bypass | stop study and release work |
| S1 blocking | cannot begin, data loss, repeated focus trap, lesson teaches wrong key | fix before next round |
| S2 material | unclear feedback, poor readability, unfair paid boundary | fix or record owner-approved experiment |
| S3 polish | minor visual or wording issue | prioritize with evidence |

Every finding records study ID, build revision, content version, environment, scenario, observation, participant segment without identity, severity, recommendation, owner, decision, and retest evidence.
