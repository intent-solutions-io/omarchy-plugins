---
blueprint:
  documentId: KTA-RISK-001
  documentType: risk-register
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
  sourceRefs: [KTA-BRIEF-001, KTA-PRD-001, KTA-ADR-001, KTA-ARCH-001, KTA-UX-001, KTA-PRIV-001, KTA-TEST-001, KTA-PLAY-001]
  assumptions: [A-101, A-102, A-103, A-104, A-105]
  unknowns: [U-101, U-102, U-103, U-104, U-105, U-106, U-107, U-108]
  relatedArtifacts: [KTA-OPS-001, KTA-AUDT-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Omarchy kids typing adventure risk register

Scale: likelihood and impact are 1 to 5. Score is their product before mitigation. All owners are roles until people accept them.

| ID | Risk | L | I | Score | Early signal | Mitigation | Contingency | Owner |
|---|---|---:|---:|---:|---|---|---|---|
| RISK-101 | Tauri/WebKitGTK behaves poorly on supported Omarchy devices | 3 | 5 | 15 | input/frame spike misses NFRs | run a disposable native spike before selecting the stack; test minimum device and software matrix | switch scene renderer or app stack before durable implementation | engineering |
| RISK-102 | App crash or resource use harms the shared desktop | 2 | 5 | 10 | shell lag, leaked processes, focus loss | separate process, lifecycle tests, bounded resources | disable companion integration and ship standalone while fixed | engineering |
| RISK-103 | Companion drifts from app contract or marketplace rules | 3 | 3 | 9 | summary parse errors or validation change | versioned minimal schema, template gates, current marketplace check | show launch-only fallback | plugin maintainer |
| RISK-104 | Child-related learning data leaves the device or appears in logs | 2 | 5 | 10 | packet or support-bundle observation | no telemetry, focused capture, redaction, data-flow tests | stop distribution, revoke endpoint, notify/review as required | privacy/security |
| RISK-105 | Child reaches purchase/external content or feels monetization pressure | 2 | 5 | 10 | route inventory or playtest finding | adult boundary, no child upsell, permanent free world | remove commerce from app and use parent-only website/support | product/privacy |
| RISK-106 | Migration, disk, update, or deletion bug loses or retains progress | 3 | 5 | 15 | fixture mismatch or recovery failure | SQLite transactions, backups, migration matrix, deletion tests | preserve original DB, export recovery tool, rollback release | engineering |
| RISK-107 | Curriculum graph has gaps, dead ends, or incoherent reading load | 3 | 4 | 12 | validator or child confusion | typed schema, graph proof, learning/content review | narrow free-world scope and revise content version | curriculum |
| RISK-108 | Game rewards speed and teaches poor technique | 3 | 5 | 15 | mashing, falling accuracy, posture concern | accuracy-first mastery, untimed practice, specialist review | remove timers and rebalance progression | learning owner |
| RISK-109 | Non-US layout, IME, modifier, or repeat behavior produces false errors | 4 | 4 | 16 | layout fixture discrepancy | explicit `key`/`code` model, declare supported layouts, real hardware tests | limit launch layouts honestly and add later | input/QA |
| RISK-110 | Free level feels like a crippled trial | 3 | 4 | 12 | children stop at paywall; parent distrust | complete world, no timer, no safety paywall | expand free scope before commerce launch | product |
| RISK-111 | Name, story, art, audio, fonts, or comparisons infringe rights | 3 | 5 | 15 | collision, takedown concern, missing license | original work, provenance manifest, trademark and legal review | rename or replace disputed material before release | legal/creative |
| RISK-112 | Offline license is forged, lost, over-restrictive, or hard to recover | 3 | 4 | 12 | support tickets, invalid unlock, refund conflict | signed artifact, documented recovery, fixtures, simple device policy | manual recovery and temporary signed replacement | commerce/engineering |
| RISK-113 | Canvas game excludes keyboard, low-vision, motion-sensitive, or assistive users | 3 | 5 | manual accessibility failures | semantic companion UI, options free, inclusive testing | provide alternate lesson presentation and block unsupported claims | accessibility |
| RISK-114 | Supply-chain or release compromise ships altered binaries | 2 | 5 | signature/provenance mismatch | protected release environment, signing custody, SBOM, attestation, exact SHA gates | revoke release, publish hashes/advisory, rotate key as planned | security/release |
| RISK-115 | Updater breaks app or makes progress unreadable | 3 | 5 | canary recovery failure | staged channel, migration backup, signed metadata, rollback rehearsal | withdraw metadata and restore prior signed artifact | release |
| RISK-116 | Repository looks complete while ownership and maintenance are absent | 4 | 4 | stale dependencies, unanswered issues, no release owner | repo-dress, CODEOWNERS, support scope, maintainer call, release roster | pause paid sales and publish maintenance status | owner |
| RISK-117 | Children find the product cheesy or compulsory | 4 | 5 | low voluntary continuation, eye-rolling, skipped story | co-design, anti-cheese gate, meaningful typing actions | change fantasy/loop before expanding curriculum | design/product |
| RISK-118 | One-time price cannot fund support and updates | 3 | 4 | high support cost or low conversion | parent research, cohort cost model, defined update window | adjust future edition or pack model without removing owned access | business |
| RISK-119 | Public privacy or compliance claims exceed actual behavior | 3 | 5 | policy-runtime mismatch | candidate data inventory, qualified review, fixed policy versions | remove claim, correct policy, stop affected data processing | legal/privacy |
| RISK-120 | Omarchy-specific scope is too small for commercial sustainability | 3 | 4 | low qualified audience despite good retention | Linux-first portable architecture, measure demand before platform work | expand to another desktop platform after architecture gate | business/product |
| RISK-121 | Parent contact collection silently expands into child or learning surveillance | 3 | 5 | CRM fields or forms request child details; identifiers become joinable | separate service/schema, prohibited-field gate, purpose-specific consent, no child join key | stop intake, quarantine records, notify privacy owner, correct/delete under approved process | privacy/product |
| RISK-122 | Consent, unsubscribe, CRM, and email state drift apart | 3 | 4 | duplicate sends, unverifiable opt-in, resubscribed suppression, mismatched purpose | append-only consent events, idempotency, reconciliation job, double opt-in, suppression | halt sends, reconcile from ledger, honor most restrictive state | platform/privacy |
| RISK-123 | Shared VPS has point-in-time headroom but becomes an overloaded failure domain | 3 | 5 | swap growth, disk trend, backup window, latency, queue age, incident coupling | limits, capacity gate, load test, monitoring, backup forecast, separation trigger | disable intake safely or move bounded service to approved isolated host | platform/operations |
| RISK-124 | A client or repository leaks CRM, mail, merchant, deployment, or signing credentials | 2 | 5 | secret scanner, unusual API use, public bundle strings | server-only adapters, least privilege, SOPS/estate custody, access review, artifact scanning | revoke/rotate, stop service, preserve evidence, incident review | security/operations |
| RISK-125 | Public reviewers find architecture claims unsupported by behavior | 4 | 5 | issue reports, unexplained network traffic, irreproducible build, policy mismatch | open source, exact evidence, known-limit disclosure, reproducible gates, independent review | withdraw claim or candidate, fix and regenerate evidence | delivery/product |
| RISK-126 | Reference qualities drift into copied identity, trade dress, or implied endorsement | 3 | 5 | prototype depends on recognizable branding, likeness, slogans, or presentation | translate only abstract mechanics, preserve provenance, conduct similarity and rights review | replace the disputed direction before public testing or release | legal/creative |
| RISK-127 | Roblox demographics are treated as proof of this product's audience | 4 | 4 | age target changes without direct cohort evidence | separate platform facts from product inference and test ages 9 to 11 and 12 to 14 independently | retain broad discovery scope and delay target selection | product/research |
| RISK-128 | Spectacle or return mechanics become coercive or obscure learning | 3 | 5 | accuracy falls, stopping is de-emphasized, or rewards depend on urgency or loss | equal stop/replay choices, accuracy gate, reduced-motion path, no streak or randomized monetization | remove the mechanism and rerun the gameplay proof | design/learning |
| RISK-129 | Online creation, public UGC, chat, or runtime AI expands the child-data and moderation system | 3 | 5 | roadmap assumes accounts, model calls, publishing, or contact without a new decision | keep the first product authored, offline, and deterministic; require a separate council, threat model, cost model, and owner gate | stop the capability and return to local curated creation | product/security/privacy |

## Top decisions by risk reduction

1. Compare three disposable gameplay greyboxes and run a separate native-runtime spike before selecting a durable slice or commissioning the full art and curriculum package.
2. Appoint a learning reviewer before finalizing mastery or lesson order.
3. Keep gameplay and profiles local, with no telemetry in the initial release.
4. Resolve public name and rights before repository and marketing investment.
5. Test child interest and parent willingness separately. Children use the product; parents approve and pay.
6. Define the exact paid license, update, refund, and recovery promise before checkout.
7. Create a maintained clean Omarchy rig and signing/rollback practice before release.
8. Select the primary audience only after separate cohort evidence, not from Roblox demographics alone.

## Risk review cadence

- Weekly during slice development
- At every architecture or vendor change
- Before any child research round
- Before checkout enablement
- At release candidate freeze and after each incident

A score of 15 or more blocks expansion until mitigation evidence or explicit owner risk acceptance with an expiry exists. Privacy, child safety, data loss, signature bypass, and rights disputes may block regardless of numeric score.
