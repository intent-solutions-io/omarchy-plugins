---
blueprint:
  documentId: KTA-PROGRAM-001
  documentType: delivery-control-plan
  schemaVersion: 1.0.0
  templateVersion: 3.0.0
  status: draft
  owner: Jeremy Longshore
  authors: ["Intent Solutions / Codex"]
  reviewers: []
  approvers: []
  generatedAt: 2026-09-10
  updatedAt: 2026-09-10
  classification: internal-draft
  sourceRefs: [KTA-BRIEF-001, KTA-PRD-001, KTA-ADR-001, KTA-ARCH-001, KTA-UX-001, KTA-PRIV-001, KTA-AC-001, KTA-TEST-001, KTA-PLAY-001, KTA-RISK-001, KTA-OPS-001, KTA-AUDT-001, KTA-COMMERCE-001, KTA-AUDIENCE-001, SR-111, SR-115, SR-116]
  assumptions: [A-101, A-102, A-103, A-104, A-105]
  unknowns: [U-101, U-102, U-103, U-104, U-105, U-106, U-107, U-108, U-109, U-110]
  relatedArtifacts: [KTA-BRIEF-001, KTA-PRD-001, KTA-ADR-001, KTA-ARCH-001, KTA-UX-001, KTA-PRIV-001, KTA-AC-001, KTA-TEST-001, KTA-PLAY-001, KTA-RISK-001, KTA-OPS-001, KTA-AUDT-001, KTA-COMMERCE-001, KTA-AUDIENCE-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure program controls

> This document defines how the build is controlled. Beads is live task-state authority. The Blueprint is design authority. Git and CI are implementation and evidence authorities. None can silently substitute for another.

## Live program identity

| Item | Value | State |
|---|---|---|
| Master Beads epic | `bd_000-projects-v41u` | open |
| Beads database | `/home/jeremy/000-projects/.beads/dolt` | live umbrella authority until product repositories exist |
| Blueprint branch | `docs/typing-adventure-blueprint` | working branch |
| App repository | unresolved | blocked by identity decision |
| Companion repository | unresolved | blocked by identity decision |
| Public name | unresolved | `OmaType` collides with an existing marketplace entry |
| First public product | complete free v1.0 | conditional product target; not yet owner-approved for implementation or release |
| Paid product | Family v1.1 | conditional on free evidence and commerce decision |

The current umbrella repository is the Omarchy public portfolio and planning surface. It must not accumulate app or plugin implementation. Once the approved repositories exist, each receives a healthy project-level Beads workspace and Dolt remote. The master epic remains the cross-repository program view. Work is routed, not duplicated, and cross-project dependencies name exported capabilities.

## Epic map

| Wave | Epic | Outcome | Hard exit |
|---|---|---|---|
| 0 | `bd_000-projects-v41u.1` | identity, repositories, project Beads, agents, traceability | owner governance decision |
| 1A | `bd_000-projects-v41u.2` | child, parent, learning, privacy, accessibility discovery | vertical-slice go/revise/stop |
| 1B | `bd_000-projects-v41u.3` | parent contact, consent, Twenty, email, production operations | independent privacy and operations audit |
| 2 | `bd_000-projects-v41u.4` | reproducible app foundation and measured runtime spike | architecture go/revise/stop |
| 3A | `bd_000-projects-v41u.5` | deterministic input, session, coaching, mastery, storage, vertical slice | independent engine and playtest review |
| 3B | `bd_000-projects-v41u.7` | local profiles, parent mode, privacy, export, deletion, recovery | data-lifecycle audit |
| 4 | `bd_000-projects-v41u.6` | original complete free world and owned media | learning, child, rights, accessibility freeze |
| 5 | `bd_000-projects-v41u.8` | thin companion plugin and marketplace packet | exact-SHA Omarchy rig evidence |
| 6 | `bd_000-projects-v41u.9` | closed pilot, policies, candidate, approval, free publication | public-state and rollback receipts |
| 7 | `bd_000-projects-v41u.10` | free observation, price research, capacity, commerce decision | signed go/revise/stop ADR |
| 8 | `bd_000-projects-v41u.11` | conditional Family implementation and paid release | separate paid evidence and approval |

The graph contains 11 phase epics plus bounded child beads under the master epic. The exact child count is generated from live Beads during consistency checks because review findings may add work. Each cross-phase prerequisite is an explicit blocking edge. The most important chain is:

```text
identity and controls
        |
research ethics + evidence + three gameplay greyboxes + measured native spike
        |
deterministic vertical slice + Stage B study disposition
        |
free world + companion + closed pilot
        |
free candidate evidence + exact approval + publish
        |
observation + price + capacity + commerce ADR
        |
conditional paid implementation and release
```

## Mandatory bead annotation contract

Every implementation or review bead carries these fields before claim:

| Field | Required content |
|---|---|
| Title | plain-English bounded outcome |
| Parent | exactly one phase epic |
| Labels | `omarchy`, `typing-adventure`, `product`, and wave |
| Blueprint ID | owning KTA document in `spec_id` and metadata |
| Release applicability | free path, shared, or paid only |
| Owner role | accountable specialty, even before a person is assigned |
| Description | outcome, scope, non-goals, and dependency rule |
| Acceptance | externally verifiable completion clauses |
| Design | happy, negative, recovery, rollback, and drift evidence rule |
| Estimate | planning minutes, revised when evidence changes |
| Notes | decisions, assumptions, blockers, seeds, commands, results, artifact pointers, and next action |

Beads must never contain credentials, private keys, child personal data, raw interviews, raw recordings, or raw keystrokes. Research evidence uses participant IDs and approved protected storage. Public GitHub issues receive only safe summaries.

## Claim-to-close process

1. Run `bd prime`, `bd where`, health diagnostics, active work, `bd ready`, and `bd blocked`.
2. Search for duplicates. Show the candidate bead, parent, dependencies, acceptance, and notes.
3. Confirm every blocker is actually closed with the required evidence. A status alone is insufficient.
4. Claim atomically. One actor owns the state transition and integration receipt.
5. Work only the bounded scope. Create a discovered bead for material follow-up instead of hiding it in prose.
6. Append a progress note before handoff or context loss. State implementation complete separately from validation complete.
7. Run change-scoped checks and every named gate. Record exact command, revision, environment, result counts, artifact, limitation, and skipped-check disposition.
8. Have the independent quality agent compare every acceptance clause with evidence. Review agents recommend but do not close.
9. Close only when implementation, verification, recovery, documentation, and evidence are complete. Then re-read the bead.
10. At an epic boundary, inspect all children, dependency tree, cycles, health, Blueprint drift, open risks, and evidence bundle. Closed children do not automatically close the epic.
11. Synchronize Dolt and Git according to repository policy and report both states. External publication requires its own fresh approval.

## WIP and authority limits

- No more than two phase epics actively implementing at once.
- Each specialist owns no more than one implementation bead at a time unless the delivery lead records an exception and reason.
- Research, architecture spike, and parent-contact work may overlap only where their blocker edges permit.
- Production persistence, companion work, and creative scale cannot start before the vertical-slice Stage B gameplay and child-appeal disposition.
- Paid implementation cannot start before `bd_000-projects-v41u.10.5` closes with an explicit go decision.
- Agents may inspect, build, test, document, and prepare evidence within a claimed bead.
- Agents may not invent owner decisions, approve their own work, publish releases, submit marketplace changes, deploy production, or change public legal policy without exact authority.
- A candidate-affecting source, dependency, content, configuration, policy, signing, or artifact change invalidates affected approval and evidence.

## Project agents

| Agent | Model | File | Role | Mutation boundary |
|---|---|---|---|---|
| `typing-delivery-lead` | Haiku | `.claude/agents/typing-delivery-lead.md` | routine ready-work selection, dependency and evidence reconciliation, release packet | read-only repository; Beads state changes require workflow authority |
| `typing-game-engineer` | Sonnet | `.claude/agents/typing-game-engineer.md` | one claimed engineering bead, tests, evidence, handoff | may edit project files, cannot publish or self-approve |
| `typing-learning-designer` | Sonnet | `.claude/agents/typing-learning-designer.md` | curriculum, story-action mapping, coaching, playtests, provenance | content/docs only, no shell or release mutation |
| `typing-quality-auditor` | Sonnet | `.claude/agents/typing-quality-auditor.md` | independent tests, privacy and release scrutiny | read-only, recommends state but never closes |
| `beacon-blueprint-auditor` | inherit | `.claude/agents/beacon-blueprint-auditor.md` | full plan-versus-actual and staged-readiness audit | read-only, recommends reconciliation but never changes state |
| `beacon-plugin-release-auditor` | inherit | `.claude/agents/beacon-plugin-release-auditor.md` | teaser freeze, lifecycle, marketplace, identity, and handoff audit | read-only, never installs, submits, or publishes |
| `beacon-visual-commercial-director` | inherit | `.claude/agents/beacon-visual-commercial-director.md` | game art, accessibility, Intent endorsement, trailer, and lean offer review | read-only, never configures commerce or publishes assets |

The learning designer hands all Beads claim, note, and close requests to the delivery lead because its tool contract cannot mutate Beads. AI agents prepare and audit work; they do not replace accountable human game design, curriculum, research ethics, child safeguarding, accessibility, privacy, data custody, or measurement roles.

Haiku handles the deterministic, high-frequency coordination lane. Sonnet is reserved for implementation, learning judgment, and routine independent technical review. The three Beacon review definitions use `inherit` so their checked-in Claude frontmatter stays portable. The 2026-09-10 council invoked them as bounded `gpt-6-astra` reviews through Codex. No always-on frontier reviewer is defined. Higher-cost adversarial review remains a bounded gate with a named evidence purpose, not an always-on expense.

## Adversarial review order

1. Specialist game, learning and child-research, and Omarchy/Linux architecture reviews inspect the primary artifacts.
2. Relevant thinker-canon lenses challenge architecture, feedback loops, documentation, data invariants, and maintainability. The thinker panel has no canonical game designer, so a separate senior-game-design review is mandatory.
3. A seven-seat executive council receives the unedited findings and commerce analysis, records convergence, dissent, and owner-held decisions.
4. Independent Grok prompt-mode agents review the complete packet when the local Grok CLI is authenticated. Model, version, exact prompt, input hashes, output, errors, and limitations are retained.
5. Reconciliation marks every finding accepted, modified, rejected, deferred, or owner-held and updates documents and Beads without erasing dissent.

Frontmatter follows the current kernel-strict Intent Solutions contract, and agent validation plus body-to-tool consistency is a shipping gate. The app and teaser repositories now exist locally. Any copied agent definition must be narrowed to that repository's actual Electron or QML commands and skills rather than copied blindly from this umbrella.

## Repository test audit and installation sequence

Each executable repository follows the same controlled sequence:

1. Scaffold enough repository structure for deterministic classification.
2. Run `audit-tests` diagnostically. It may write the audit and observational testing records, but it cannot implement tests or weaken engineer-owned policy.
3. Review the classification, applicable and waived L1 through L7 layers, harness state, P0/P1/P2 gaps, requirements traceability matrix, personas, journeys, coverage, mutation, CRAP, architecture, security, and escape-scan results.
4. If P0 or P1 gaps exist, pass the exact structured handoff to `implement-tests`.
5. `implement-tests` installs the in-repository audit harness, frameworks, CI glue, starter tests, traceability records, and hash manifest. It stages changes for engineer review and never commits, publishes, lowers thresholds, or edits engineer-owned walls.
6. Re-run `audit-tests` against the reviewed installation. A repository cannot pass its foundation gate with an unresolved P0 or unaccepted P1 gap.

| Repository scope | Audit bead | Install bead | Re-audit or aggregate gate |
|---|---|---|---|
| Parent contact service | `bd_000-projects-v41u.3.7` | `bd_000-projects-v41u.3.8` | `bd_000-projects-v41u.3.6` |
| Standalone app | `bd_000-projects-v41u.4.8` | `bd_000-projects-v41u.4.9` | `bd_000-projects-v41u.4.10` |
| Omarchy companion | `bd_000-projects-v41u.8.6` | `bd_000-projects-v41u.8.7` | `bd_000-projects-v41u.8.4` |

The app and teaser repositories now exist locally. The app testing audit and installation were executed against the Electron prototype, but the 2026-09-10 Astra review found that the resulting report overstates native Electron coverage and hosted CI enforcement. The teaser has strong local gate evidence, but the legacy companion epic describes a different launch, resume, and summary product. Re-audit must use each actual repository, runtime, candidate revision, and release scope. A workflow file without a configured public remote is not proof of enforced hosted CI.

## Worktree hygiene hook

The planning repository includes a project-local advisory hook at `.claude/settings.json` backed by `scripts/worktree-hygiene.py` and `.worktree-hygiene.json`. It runs a non-destructive audit at session start and after Claude worktree create or remove events. It classifies current, primary, locked, protected-branch, dirty, active, review, and already-missing metadata states and writes an atomic receipt in the shared Git directory. It is an organization aid, not a security boundary or substitute for human Git review.

The hook never removes a worktree or branch. Dirty worktrees are explicitly protected. Missing-path metadata may be previewed with `python3 scripts/worktree-hygiene.py prune-metadata`; applying that metadata-only prune requires the explicit `--apply` flag. Any valid worktree or branch removal remains a separate human-reviewed Git operation after status, unique-commit, and path checks.

Bead `bd_000-projects-v41u.1.14` governs the implementation. Its validation denominator includes unit tests, real-repository smoke behavior, JSON and matcher checks, and the kernel hook schema for every handler.

## Authentication and data ownership

| User or actor | Account/login | Data authority |
|---|---|---|
| Child | none | local SQLite profile only |
| Parent using free app | none; local adult navigation gate | local parent settings and exports |
| Parent joining updates | expiring signed email verification | Twenty contact plus append-only consent event |
| Parent buying Family | approved merchant/recovery identity outside child play | merchant customer and license records; signed entitlement in app |
| Jeremy and operators | unique approved estate/vendor accounts | role-scoped CRM, deployment, support, and signing systems |

The append-only consent and suppression ledger is authoritative for contact permission. Twenty is a rebuildable projection for approved verified-parent relationship fields, never permission authority. The child database never syncs to it and has no join key. The proposed online service keeps only the minimum consent and outbox records. It integrates through a supported API, never by writing to Twenty's database directly.

## Hosting decision and capacity gate

The desktop game is packaged and downloaded. It does not need a permanent game server. This keeps the free experience available offline and materially reduces hosting, privacy, and availability burden.

The optional parent intake and later licensing service are small online workloads, not game hosting. A valid paid installation uses a signed local entitlement and remains usable during a licensing-service outage; an approved offline import and recovery path prevents the vendor or service from becoming a gameplay availability dependency. The recommended production target for those narrow services is the shared `intentsolutions` VPS because it already owns customer-facing ingress, operations, and Twenty. A read-only snapshot on 2026-09-10 showed 8 CPU, 23 GiB RAM with about 16 GiB available, 147 GB free disk at 63 percent used, and 47 running containers. That supports a design recommendation, not a deployment claim.

`team-server` is development only and showed 13 GB free at 97 percent root-disk use. It is rejected for public hosting. Buzz is a dedicated product and validation estate, not spare capacity for this app. Neither may hold the parent database.

Before deployment, `bd_000-projects-v41u.3.5` requires a new dated baseline, staged load and abuse test, CPU and memory limits, queue and retry budgets, TLS and rate limiting, least privilege, health checks, monitoring, backup-size forecast, restore proof, secret custody, deploy receipt, and rollback drill. `bd_000-projects-v41u.10.4` repeats the decision before commerce and defines the threshold for an isolated host or managed service.

## Public scrutiny standard

Assume Omarchy maintainers and users will inspect every permission, dependency, network call, QML lifecycle, key handler, license term, artifact, and claim. Release evidence must make scrutiny cheap:

- reproducible setup and stable top-level commands
- narrowly scoped permissions and no global input capture
- source-visible schemas and deterministic fixtures
- no unexplained outbound request
- published SBOM, checksums, signatures, provenance, asset credits, and known limitations
- exact app-versus-plugin boundary and working install/remove path
- policy claims reconciled against network, storage, logs, CRM, and binaries
- public issue and security-reporting routes with realistic maintainer expectations
- screenshots and casts produced from the exact candidate, never a mock presented as shipped behavior

The quality bar is not "many tests." It is relevant evidence at the correct layer, tied to the correct revision, with failure and rollback behavior visible.

## Current state and next ready work

The master and phase graph, local Electron prototype, local QML teaser, AppImage, test scaffolding, and seven project review or execution agents exist. `The Beacon Wakes` is the owner-selected creative title, endorsed as `by Intent Solutions`; legal clearance and public identifiers remain open. No public app or teaser repository, marketplace listing, working parent destination, configured checkout, production service, signed release, or public release exists.

The next bounded engineering iteration is ready after KTA-ASTRA-001 reconciliation. Keep Electron for this slice. Bead `.4.14` owns focus and input, untimed play, contrast, adult navigation, entitlement schemas and storage, packaged-native evidence, and the first-chapter baseline. Beads `.2.16` and `.3.9` own the ungated Parent Launch Guide, `Light the Beacon Together` co-play opening, and tested parent handoff. Bead `.8.8` owns the exact playable teaser candidate after that handoff exists.

The free parent layer is part of product adoption and child safety, not a lead-capture toll. A parent gets a one-page quick start, a five-minute lesson, invitation language, child choice, accuracy-before-speed guidance, calm mistake modeling, breaks, accessibility adaptations, and an optional seven-day family rhythm without surrendering an email address. Any Friday-letter or product-update signup is a separate adult-only choice, and no child data enters Twenty.

The Omarchy teaser is feature-scope locked but not release-byte locked. Branding, contrast, a working parent handoff, source-to-receipt equivalence, and complete install-to-remove evidence precede its candidate freeze. Payment remains blocked until the free-world definition, commercial model, provider, policies, entitlement behavior, signing, delivery, recovery, and exact paid unit receive owner approval.
