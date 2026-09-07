---
blueprint:
  documentId: OMT-RISK-001
  documentType: risk-register
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
  sourceRefs: [OMT-PRD-001, OMT-ARCH-001, OMT-GAME-001, OMT-TEST-001, OMT-PLAY-001, SR-003, SR-004, SR-009]
  assumptions: [A-001, A-002, A-003, A-004]
  unknowns: [U-001, U-002, U-003, U-004, U-005, U-006]
  relatedArtifacts: [OMT-AC-001, OMT-PLAN-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omatrail risk register

> Initial exposure ratings are derived planning judgments, not measured incident data. Residual ratings assume proposed controls are implemented and verified.

## Method and appetite

Likelihood and impact use 1 to 5 ordinal scales. Exposure is `likelihood x impact`: low 1 to 4, moderate 5 to 9, high 10 to 16, critical 17 to 25.

- Zero tolerance: undisclosed network/credential behavior, destructive save handling, copied protected assets, unreviewed materially harmful historical representation, or known shell-crash paths.
- Low tolerance: inaccessible critical actions, focus leakage, or unexplained data writes.
- Moderate tolerance during prototype only: incomplete art, tuning, content, and minor presentation defects.
- Risk acceptance authority: project owner plus the named specialist for legal, historical/content, security, or accessibility risks. Names remain unresolved.

## Risk registry

| ID | Cause and event | Consequence | Inherent L/I | Controls | Residual L/I | Owner | Status and trigger | Review |
|---|---|---|---|---|---|---|---|---|
| RISK-001 | The name, marketing, prose, or assets are too close to a commercial property. | Takedown, rejection, reputational or legal cost. | 3/5 high | CTRL-005; original expression; functional-observation boundary; public design and provenance record; legal review before listing. | 1/5 moderate | Legal owner TBD | Partly mitigated by independent implementation and provenance record; legal disposition remains open. | Before public preview and listing |
| RISK-002 | QML or JavaScript failure occurs inside the shared long-running shell. | Desktop-shell instability or loss of trust. | 3/5 high | Pure engine, bounded inputs, lifecycle tests, no second shell. | 1/5 moderate | Engineering owner TBD | Open; zero uncaught errors required. | Each phase gate |
| RISK-003 | Overlay focus or keys leak to the underlying desktop. | Unintended commands or user input. | 3/5 high | Explicit focus state machine, pause on focus loss, system matrix. | 1/5 moderate | Engineering owner TBD | Open; any leak suspends release testing. | Each runtime candidate |
| RISK-004 | Save write or migration corrupts an expedition. | Progress loss or silent overwrite. | 3/4 high | CTRL-002; atomic replace, last-good backup, version gates, recovery tests. | 1/4 low | Engineering owner TBD | Open; any silent overwrite is release-blocking. | Each save-schema change |
| RISK-005 | Hunting is boring, awkward, or too shallow. | Core product promise fails. | 3/5 high | Hunting-first prototype and PLAY-001 gate. | 2/4 moderate | Game-design owner TBD | Open; prototype misses enjoyment or control threshold. | Hunting gate |
| RISK-006 | Hunting is too difficult or excludes some motor/visual users. | Frustration and inaccessible progression. | 3/4 high | Remapping, assists, mouse alternative, extended time, hunting-light viability. | 2/3 moderate | Accessibility owner TBD | Open; critical task failure or comfort report. | Hunting and beta gates |
| RISK-007 | Hunting is always optimal and trivializes store, trade, and ration choices. | Strategy collapses and replayability falls. | 4/4 high | Time/ammo/risk/carry/spoilage costs, policy simulation, balance beta. | 2/3 moderate | Game-design owner TBD | Mitigated in candidate simulation; reopen if exploit survival or median score exceeds either skilled policy. | Every balance change |
| RISK-008 | Random events feel arbitrary or erase good decisions. | Players attribute loss to unfairness. | 3/4 high | Seeded RNG, bounded effects, visible modifiers, post-outcome explanation. | 2/3 moderate | Product owner | Open; repeated opaque-frustration finding. | Vertical slice and beta |
| RISK-009 | Historical simplification or stereotyped depiction harms represented peoples. | Harm, misinformation, rejection, reputational loss. | 3/5 high | CTRL-006; sourced claims, specific nations, human review, no generic encounter category. | 2/4 moderate | Content owner TBD | Open; disputed claim or reviewer objection. | Each content freeze |
| RISK-010 | Green Monitor effects reduce readability or cause discomfort. | Eye strain, motion discomfort, inaccessible text. | 3/4 high | Clean pixels, reduced motion, adjustable/off CRT, profile playtest. | 1/3 low | Design owner TBD | Open; any comfort blocker. | Each visual milestone |
| RISK-011 | Color Deluxe doubles art and QA scope. | Schedule slips and inconsistent mechanics. | 4/3 high | Shared semantic layout/hitboxes, palette-driven sprites, differential tests. | 2/3 moderate | Design owner TBD | Open; profile-specific logic or over 20% estimate growth. | Vertical slice and art freeze |
| RISK-012 | Content volume expands before the core loop is proven. | Long schedule with an unfun product. | 4/4 high | Hunting gate and vertical-slice gate before full writing. | 2/3 moderate | Product owner | Open; full-content work starts before gate evidence. | Weekly until content freeze |
| RISK-013 | Timers or animation run while hidden or miss frame targets. | Battery, CPU, or shell responsiveness cost. | 3/4 high | Stop hidden work, performance budget, cosmetic degradation. | 1/3 low | Engineering owner TBD | Open; TEST-018 fails. | Each runtime candidate |
| RISK-014 | A mutable upstream update differs from the marketplace-reviewed revision. | User installs behavior that was not reviewed. | 3/4 high | Candidate SHA receipts, release tags, transparent install warning, post-install review guidance. | 2/3 moderate | Release owner TBD | Open; installed SHA differs from reviewed SHA. | Each release and update |
| RISK-015 | Party names enter logs, fixtures, or public evidence. | Personal data disclosure. | 2/4 moderate | No telemetry, scrub logs, synthetic fixtures, opt-in research recording. | 1/3 low | Security owner TBD | Open; any real name appears in public artifact. | Each evidence publication |
| RISK-016 | Current Quattro manifest or overlay behavior changes. | Plugin no longer loads after Omarchy update. | 3/3 moderate | Resolve U-005, CI/current-version checks, documented compatibility. | 2/2 low | Engineering owner TBD | Open; schema or lifecycle change detected. | Each Omarchy release |

## Control registry

| ID | Objective | Implementation state | Required test evidence |
|---|---|---|---|
| CTRL-001 | Prohibit network, credentials, privilege, telemetry, and undeclared processes. | proposed | TEST-017 static plus complete-run observation |
| CTRL-002 | Bound and recover local state safely. | proposed | TEST-015 and TEST-016, including interrupted write |
| CTRL-003 | Bind verification to an exact candidate revision and declared capabilities. | proposed | TEST-013 and marketplace receipt |
| CTRL-004 | Treat content as bounded data and reject invalid references. | proposed | TEST-009 schema and graph report |
| CTRL-005 | Prove asset and content provenance and obtain name/marketing review. | proposed | Provenance ledger and legal disposition |
| CTRL-006 | Source historical claims and obtain affected-group content review. | proposed | Claim register and human review record |
| CTRL-007 | Keep display profiles semantically equivalent and accessible. | implemented with candidate source, differential, reduced-motion, and dual-render evidence; human playtest pending | TEST-010 through TEST-012 and PLAY-006/007 |

## Review and acceptance

Review at each phase gate, on any trigger above, and before marketplace submission. A risk cannot be accepted solely by the implementer when specialist review is required. Acceptance records must include owner, reason, evidence, expiry or review date, and compensating control. No risk has been accepted.
