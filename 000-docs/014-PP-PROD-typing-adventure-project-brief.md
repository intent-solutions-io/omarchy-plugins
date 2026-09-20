---
blueprint:
  documentId: KTA-BRIEF-001
  documentType: project-brief
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
  sourceRefs: [SR-101, SR-102, SR-103, SR-104, SR-105, SR-106, SR-107, SR-108, SR-109, SR-110, SR-111, SR-112, SR-113, SR-114, SR-115, SR-116, SR-117, SR-118, SR-119, SR-120, SR-121, SR-122, SR-123, SR-124]
  assumptions: [A-101, A-102, A-103, A-104, A-105]
  unknowns: [U-101, U-102, U-103, U-104, U-105, U-106, U-107, U-108, U-109, U-110]
  relatedArtifacts: [KTA-PRD-001, KTA-ADR-001, KTA-ARCH-001, KTA-UX-001, KTA-PRIV-001, KTA-AC-001, KTA-TEST-001, KTA-PLAY-001, KTA-RISK-001, KTA-OPS-001, KTA-AUDT-001, KTA-PROGRAM-001, KTA-AUDIENCE-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure project brief

> This is a decision proposal, not implementation evidence. The owner selected `The Beacon Wakes` as the child-facing product title on 2026-09-10, endorsed as `by Intent Solutions`. Publication, repository renaming, domains, application identifiers, and packaging remain gated on legal and commercial clearance. The existing marketplace name `OmaType` is already used by another author and must not be adopted without permission and collision review.

## Requested decision

Approve discovery, three disposable gameplay greyboxes, and a separate native-runtime spike for an app-first, privacy-first typing adventure for children. Do not approve the durable vertical slice, companion, parent service, or commercial build until the named gameplay, learning, child-research, accessibility, privacy, architecture, and ownership gates pass.

## One-line strategy

Build the part children spend time in as a standalone desktop app, keep the Omarchy integration as a thin open-source plugin, and sell expanded curriculum to parents without placing accounts, advertisements, payments, or pressure loops in the child's play path.

## Why an app, not only a plugin

The Omarchy plugin template is designed for a small QML surface inside the shared `omarchy-shell` process. It is excellent for a bar widget, progress glance, daily goal, launch action, and marketplace discovery. It is the wrong failure domain for a large game with many scenes, audio, child profiles, curriculum data, local persistence, commerce entitlement, updates, and long play sessions.

The proposed product therefore has two deliverables:

1. A standalone Linux desktop app that owns the lesson engine, game scenes, profiles, progress, accessibility, local storage, entitlement, packaging, updates, and crash boundary.
2. A free Omarchy companion plugin derived from the Intent Solutions widget template that can launch or resume the app, show a bounded local progress summary, and explain how to install the app when it is absent.

The complete free learning experience must be playable without the plugin. The plugin must never download or silently install the app, collect child data, or contain purchase UI.

## Product thesis

Children do not want a worksheet with particle effects. The product must feel like an adventure in which accurate typing is the control system. Lessons introduce a small skill, short missions use it under low pressure, and game challenges recombine mastered skills. Failure should result in coaching and another route, not shame, lost streaks, or blocked access.

The remembered value of classic typing software was structured instruction, visible hands, progressive reaches, immediate correction, and progress that parents could understand. The new value is a coherent game world, inclusive original characters, modern accessibility, local-first privacy, and optional Omarchy shortcut missions after touch-typing foundations are secure.

A future sports technology track should meet athlete-oriented children where their interest already lives. It can show that sports also needs analysts, software builders, broadcast operators, sensor technicians, data stewards, equipment designers, and team operations specialists. Parent messaging must present this as an additional way to participate and lead in sports, not as a threat that an athletic dream will fail or a lesser backup career.

## North-star experience

The owner wants the energy of large creator-led challenge entertainment, the inhabitable and eventually creative appeal of online sandbox worlds, a bounded AI twist, and unmistakable Omarchy identity. These are design patterns, not permission to use a creator's name, likeness, voice, slogans, branding, sets, thumbnails, characters, or trade dress, and not permission to copy Roblox assets or product presentation.

For the first proof, translate that direction into rapid challenge clarity, escalating but non-coercive stakes, surprising world restoration, meaningful player choices, and bold audiovisual payoffs. Keep the proof offline, single-player, and free of chat, public profiles, open user-generated content, virtual currency, behavioral advertising, and runtime generative AI.

Only after the free product proves fun, learning value, safety, accessibility, operations, and parent trust may a new decision consider curated creation tools, parent-approved sharing, online play, or AI features. Each requires a separate threat model, moderation and abuse plan, identity and consent model, data-flow inventory, cost model, legal review, acceptance criteria, and owner approval. Human-reviewed AI-assisted authoring is the preferred first AI use; an open child chatbot is not on the roadmap.

## Audience and roles

| Role | Need | Product relationship |
|---|---|---|
| Child learner, candidate cohorts ages 9 to 11 and 12 to 14 | Agency, short sessions, clear feedback, real game stakes, no embarrassment or babyish treatment | Plays lessons and missions |
| Parent or guardian | Safe purchase, local profiles, intelligible progress, easy deletion, no manipulative monetization | Owns settings and paid entitlement |
| Older beginner | A non-childish path through the same curriculum | Optional secondary mode, not MVP promise |
| Omarchy user | Theme-aware launch, daily status, keyboard-first integration | Uses free companion plugin |
| Educator or learning reviewer | Sound sequence, readable metrics, practice quality | Reviews curriculum and evidence |
| Maintainer | Reproducible builds, scoped tests, content provenance, safe releases | Operates repositories and releases |

Age range, secondary audiences, and educator use are hypotheses until research is completed.

## Objectives

| ID | Objective | Priority | Proposed measure | Decision state |
|---|---|---:|---|---|
| OBJ-101 | Make children voluntarily start a second session. | P0 | At least 70 percent of supervised pilot participants choose another mission within one week. | proposed target |
| OBJ-102 | Produce measurable touch-typing improvement without rewarding sloppy speed. | P0 | Accuracy-first mastery and pre/post skill probes reviewed by a learning specialist. | method proposed, target unresolved |
| OBJ-103 | Keep child play offline and free of accounts, advertising, chat, tracking, and purchases. | P0 | Network observation, data inventory, and parent-flow acceptance evidence. | provided direction |
| OBJ-104 | Provide a meaningful free level rather than a timed demo. | P0 | One complete world, 10 to 15 lessons, one local profile, and permanent access. | proposed |
| OBJ-105 | Offer a one-time family upgrade with expanded curriculum and profiles. | P1 | Parent-only purchase and offline-verifiable entitlement. | hypothesis, pricing unresolved |
| OBJ-106 | Teach selected Omarchy shortcuts only after typing basics and without reading private activity. | P1 | Versioned shortcut curriculum and explicit practice sandbox. | proposed |
| OBJ-107 | Make representation customizable without gendered difficulty, rewards, colors, or curriculum. | P0 | Character options and automated content-equivalence checks. | provided direction |
| OBJ-108 | Let interested parents stay in touch without creating child accounts or mixing marketing with learning data. | P0 | Purpose-specific double opt-in, unsubscribe, CRM and consent-ledger reconciliation, and zero child fields. | proposed |
| OBJ-109 | Test whether a sports technology mission track increases voluntary engagement and parent-perceived relevance for athlete-oriented families without weakening the core typing and privacy model. | P1 | Three original concepts plus segmented parent and child evidence under `bd_000-projects-v41u.2.14`. | owner-directed hypothesis |

## Scope boundaries

### Free level

- One complete original story world with 10 to 15 lessons
- A coherent beginner curriculum through lowercase and uppercase letters, space, Enter, Shift, numerals, and essential sentence punctuation, plus essential correction and local adaptation
- One local learner profile with a nickname or generated callsign
- All accessibility controls, including reduced motion, sound controls, remapping where compatible, readable text, and color-independent feedback
- Basic local progress, session history, and parent-readable skill map
- No account, advertisement, telemetry, time limit, streak loss, or purchase prompt in child mode

### Paid family level

- Advanced punctuation and symbols, sustained fluency, code-like patterns, and Omarchy-specific curriculum
- Multiple original story worlds and challenge modes
- Multiple local profiles
- Deeper local adaptation, challenge modes, and extended mastery paths
- Expanded family overview across local profiles without sibling ranking
- Original cosmetic unlocks available without gender restrictions
- Omarchy shortcut academy and future owned curriculum packs

The paid boundary may change after parent interviews and pricing research. Accessibility, privacy, safety, deletion, core error coaching, and the complete free world may not be moved behind the paywall.

### Explicit exclusions for initial release

- Cloud accounts or cloud saves
- Child email, real name, date of birth, voice, photo, location, contacts, or biometric data
- Advertisements, third-party analytics, social sharing, leaderboards, chat, direct messaging, or user-generated public content
- Subscription billing in the initial proposal
- School rostering, teacher surveillance, or classroom administration
- Mobile, browser-hosted, macOS, and Windows production support
- Runtime generative AI or downloaded lesson generation
- A direct copy of Mavis Beacon, its characters, lessons, artwork, audio, name, or trade dress
- A full game inside `omarchy-shell`

## Delivery gates

| Gate | Question | Evidence needed | Stop condition |
|---|---|---|---|
| GATE-101 | Does typing create meaningful game decisions? | Three disposable mechanics, an attractive neutral alternative, a minimally dressed drill, and approved formative sessions | A child cannot explain why an action was chosen, removing typing leaves the game intact, or replay and frustration gates fail |
| GATE-102 | Is the selected typing loop enjoyable, accessible, and accurate? | Approved vertical slice and Stage B protocol with 8 to 12 child sessions | Accuracy degrades, children mash keys, coaching is ignored, or no accessible equivalent path exists |
| GATE-103 | Is the learning sequence defensible? | Independent typing or education specialist review | No qualified reviewer accepts the mastery model |
| GATE-104 | Is the privacy model truthful? | Data-flow inventory, network observation, counsel or qualified privacy review | Child data leaves the device unexpectedly |
| GATE-105 | Is there parent willingness to pay? | At least 15 parent interviews and price test | No credible willingness at the proposed one-time price |
| GATE-106 | Is the release operable on Omarchy? | Clean install, upgrade, rollback, plugin, and hardware matrix evidence | Shell instability, focus traps, data loss, or unsigned artifacts |

## Delivery recommendation

Proceed in five evidence-gated increments:

1. Discovery: naming screen, owner appointments, evidence review, approved research protocol, parent interviews, child co-design, privacy classification, and paper prototypes.
2. Gameplay proof: three disposable 3 to 5 minute greyboxes for one skill family, compared with a neutral alternative and a minimally dressed drill. In parallel, run a separate native input, focus, accessibility, and performance spike.
3. Vertical slice only after both proofs pass: one small narrative chapter, three skill families, reversible minimal persistence, deterministic input, and the approved Stage B study.
4. Free product only after the Stage B disposition: full beginner alphabet, complete free world, production storage and recovery, packaging, companion, accessibility, signed candidate, and closed pilot.
5. Paid expansion only after learning, safety, accessibility, free-world fairness, retention, support, rights, privacy, parent-demand, and commerce evidence: multiple profiles, advanced curriculum, additional worlds, entitlement, refund, recovery, and update operations.

Calendar estimates are planning ranges, not commitments. Team size, art pipeline, reviewer availability, and final scope are unresolved.

## Version sequence

| Version | Audience | Product boundary | Commerce state |
|---|---|---|---|
| v0.1 alpha | internal and supervised testers | three-skill vertical slice and synthetic profiles | entitlement interface uses test fixtures only |
| v0.5 pilot | approved family cohort | complete free world candidate, recovery, accessibility, signed prerelease | no live checkout |
| v1.0 free | public Omarchy users | permanent free world, one profile, companion, signed updates, support and policies | no paid dependency |
| v1.1 Family | parents who choose to upgrade | advanced curriculum, multiple profiles, deeper local adaptation, additional worlds, and expanded family overview | parent-only checkout and signed offline entitlement |
| later packs | existing families | additional original worlds or approved curriculum | optional purchases that never revoke already owned access |

The free v1.0 is a real release, not a beta whose value expires. Its privacy, accessibility, durability, signing, update, support, and rollback obligations remain production-grade. The entitlement seam may exist behind test fixtures so paid work does not require an architectural rewrite, but no live commerce service is required for the free launch.

## What is missing before build approval

| ID | Missing decision or evidence | Why it matters | Owner needed |
|---|---|---|---|
| U-101 | Public name, repository names, application ID, domain, and trademark screen | `OmaType` already collides and Mavis Beacon is a third-party mark | Product and legal |
| U-102 | Learning-science owner and curriculum map | A fun typing game can still teach poor technique | Product and learning reviewer |
| U-103 | Supported ages, reading level, keyboard layouts, and accessibility audience | These choices change content, input, and testing | Product and accessibility |
| U-104 | Price, merchant of record, refund rules, taxes, and license recovery | A one-time tier is a hypothesis, not an operating model | Business and legal |
| U-105 | Jurisdictions and child-privacy applicability | US launch still needs current COPPA review; wider launch adds obligations | Legal/privacy |
| U-106 | Art, audio, writing, font, and content provenance owners | Commercial release requires a complete rights chain | Creative and legal |
| U-107 | Supported Omarchy and Arch baselines plus GPU, scaling, and keyboard matrix | Linux graphics and input behavior vary materially | Engineering and QA |
| U-108 | Support, vulnerability intake, incident owner, and update signing custody | Paid family software needs a maintained release path | Operations/security |
| U-109 | Parent-contact endpoint, consent-ledger implementation, newsletter sender, retention, and deletion workflow | Jeremy needs usable contact information without creating an ungoverned child-data system | Product, privacy, and platform |
| U-110 | Shared production VPS reservation and separation trigger | Point-in-time headroom is adequate, but production placement requires limits, backup, monitoring, and a dated capacity decision | Platform/operations |

## Source register

| ID | State | Source | Use and limitation |
|---|---|---|---|
| SR-101 | provided | User direction in this conversation through 2026-09-10 | Kids typing product, character options, free then paid, strategic planning, full test environment |
| SR-102 | verified snapshot | [Omarchy marketplace catalog](https://plugins.omarchy.org/catalog.json), observed 2026-09-10 | Confirms `OmaType`, Omarchy Typing Test, Omi Companion, and adjacent products; catalog changes continuously |
| SR-103 | verified local | `omarchy-widget-template` at commit `19f1e64` | Companion plugin structure and gates, not the app architecture |
| SR-104 | verified | [Tauri prerequisites](https://v2.tauri.app/start/prerequisites/) | Confirms current Arch dependencies; version pin remains an implementation decision |
| SR-105 | verified | [Phaser documentation](https://docs.phaser.io/) | Confirms open-source HTML5 engine with TypeScript and WebGL/Canvas support |
| SR-106 | verified | [Tauri testing overview](https://v2.tauri.app/develop/tests/) | Mock runtime and WebDriver support; real webview/system tests are still required |
| SR-107 | verified, legal source | [FTC COPPA business guidance](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions) and [2025 amendments](https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-312-coppa-final-rule-amendments) | Compliance reference only, not legal advice or a product-specific determination |
| SR-108 | verified local and public | [HustleStats Privacy Policy](https://hustlestats.io/privacy), source `hustle/src/app/privacy/page.tsx` | Reusable topic inventory; product-specific facts and current legal sufficiency are unverified |
| SR-109 | verified local and public | [HustleStats Terms](https://hustlestats.io/terms), source `hustle/src/app/terms/page.tsx` | Includes acceptable-use section; not a license or terms template for this product |
| SR-110 | verified | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Accessibility baseline adapted to a desktop app and game context |
| SR-111 | verified local | `contributing-clanker` README, CI, and contribution skills | Evidence packets, deterministic gates, exact revision, and human approval boundary |
| SR-112 | verified local | omaTrail Blueprint workbook in this repository | Document structure and traceability precedent |
| SR-113 | verified | [MDN KeyboardEvent guidance](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent) | Character versus physical-key semantics and layout risk |
| SR-114 | verified | [GitHub artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations) | Build-provenance option; repository eligibility and plan limits require confirmation |
| SR-115 | verified local authority | `intent-os/000-docs/033-AT-ARCH-current-estate-architecture.md`, `intent-os/ops/README.md`, and `intent-os/mission-control/self-hosted-services.md` | Establish the dev-only machine, shared production VPS, dedicated Buzz boundary, existing forms service, and Twenty CRM; follow current supersession notices |
| SR-116 | verified live snapshot | Read-only `hostname`, `nproc`, `free -h`, `df -h /`, `docker ps`, and `docker stats --no-stream` on 2026-09-10 | Shared VPS showed 8 CPU, 23 GiB RAM with 16 GiB available, 147 GB disk available at 63 percent used, and 47 running containers. This is a capacity input, not a load test or deployment approval |
| SR-117 | verified primary source | [Roblox Q2 2026 shareholder letter filed with the SEC](https://www.sec.gov/Archives/edgar/data/1315098/000162828026051059/ex991-robloxq22026earnin.htm) | Current age-checked distribution and older-cohort growth and monetization; company-reported and selected by age-check participation |
| SR-118 | verified primary source | [Roblox 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm) | DAU and age-measurement limitations; warns that current and historical series are not comparable |
| SR-119 | verified primary source | [Roblox 2026 proxy statement](https://www.sec.gov/Archives/edgar/data/1315098/000110465926044362/rblx-20260528xdef14a.htm) | Describes younger users as a strategic asset and over-18 as an expansion opportunity; company strategy rather than independent market evidence |
| SR-120 | verified primary source | [Roblox 2023 all-ages statement](https://about.roblox.com/newsroom/2023/05/our-vision-for-all-ages) | Historical older-cohort evidence under a self-reported method that is not directly comparable with current age checks |
| SR-121 | verified primary source | [Roblox Q4 2025 shareholder letter filed with the SEC](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000009/ex991-q42025shareholder.htm) | First age-checked cohort snapshot and current-series baseline; company-reported |
| SR-122 | verified primary source | [Roblox Q1 2026 shareholder letter filed with the SEC](https://www.sec.gov/Archives/edgar/data/1315098/000162828026028882/ex991-q12026earningsshar.htm) | Second age-checked cohort snapshot; company-reported and incomplete coverage |
| SR-123 | verified primary source | [Roblox Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1315098/000162828026051082/rblx-20260630.htm) | Current age-metric and payer-denominator limitations |
| SR-124 | verified primary source | [Roblox Kids and Select worldwide launch](https://ir.roblox.com/news/news-details/2026/Roblox-Kids-and-Roblox-Select-Accounts-Now-Available-Worldwide/default.aspx) | Confirms continued investment in younger cohorts; product announcement rather than independent demographic evidence |

## Assumptions

| ID | State | Assumption | Validation |
|---|---|---|---|
| A-101 | assumed | Linux on current Omarchy is the only initial production target. | Owner approval and market check |
| A-102 | assumed | One of the candidate cohorts ages 9 to 11 or 12 to 14 can sustain an age-respectful typing adventure without excluding the other. | Cohort-separated parent and child discovery under the approved protocol |
| A-103 | assumed | A one-time family license is preferable to a subscription. | Pricing interviews and cost model |
| A-104 | assumed | Local-only progress can support the first paid release. | Parent interviews and support analysis |
| A-105 | assumed | A web-rendered game inside a Tauri shell can meet input and frame targets on the supported matrix. | Vertical-slice benchmark |

## Human review

- Required: yes
- Status: not started
- Approval evidence: none
- Minimum reviewers before build approval: product owner, engineering owner, learning reviewer, privacy/legal reviewer, accessibility reviewer
