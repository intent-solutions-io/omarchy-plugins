# Omarchy estate readiness audit

**Audit date:** 2026-08-29 UTC  
**Scope:** `intent-solutions-io/omarchy-plugins`, its 16 declared repositories,
the Omarchy marketplace listings, open submission issues, GitHub CI, and the
Buzz production Omarchy rig.

## Decision

The estate has a sound engineering baseline but is **not yet eligible for a
"best in class" or "fully production certified" public claim**. Do not imply
that every current source revision is marketplace-verified or E2E-tested.

The immediate source-injection finding in Crew Chief was fixed and proven on
the real rig in commit `0ef344e`. Its validator and QML-lint receipts are both
zero-error and its full local suite passes 25/25.

## What is healthy

- 16/16 Git worktrees were clean and synchronized with their remotes at audit.
- `git fsck --no-dangling` was clean for every repository; the targeted secret
  scan found no high-confidence secret pattern; manifest IDs and README names
  agree.
- All local Node test suites pass: **444/444 tests** across 16 repositories.
- All current GitHub `gates` and `test` workflow runs were green at audit.
- Every live marketplace listing has a preview asset.

## Findings that block the claim

### P0 — marketplace review is not an approval we can self-grant

Desk Transition's refreshed preview is at source commit `2e06d94`; its correct
marketplace verification request is
[HANCORE-linux/omarchy-plugin-marketplace#3235](https://github.com/HANCORE-linux/omarchy-plugin-marketplace/issues/3235).
Automation validated it, but the issue is still open with
`security-review-required`. A marketplace maintainer must make the independent
approval decision. The catalog remains on old snapshot `9383567` until then.

Five submitted plugins are also security-blocked after their basic validation:

| Plugin | Submission | Blocking class |
| --- | --- | --- |
| Loose Ends | #2899 | spool file replacement / TOCTOU |
| Capture Conveyor | #2900 | config and record tempfile TOCTOU |
| Workspace Storyboard | #2901 | history lifecycle TOCTOU |
| Quiet Queue | #2902 | session read/write TOCTOU |
| Flow Boundary | #2903 | ledger read/publication TOCTOU |

Each needs a descriptor-bound/no-follow lifecycle implementation and adversarial
replacement tests before an exact-SHA resubmission. These are genuine security
findings, not labeling or copy problems.

### P1 — the live catalog does not certify current heads

Nine plugins are live. Listening Post's validated commit matches its current
head. The other eight live listings reference older validated source snapshots:
Pit Wall, MLB Booth, Bazaar, Wait State, Crew Chief, Docket, X Files, and Desk
Transition. Every public repo must receive a verified update only after its
current source is proven in the rig and review accepts that exact commit.

Foundry has a local preview and current source but no marketplace listing or
submission. It must clear the normal submission lane before it can be counted.

### P1 — CI proves static and unit tests, not a running Omarchy shell

All 16 repositories provide rig scripts, but none of their GitHub workflows
executes `rig-verify.sh`, `rig-render.sh`, or Foundry's `rig-e2e.sh`. Therefore
a green hosted workflow does not prove a plugin loads in Omarchy.

Current proof is at current source only for Desk Transition, Foundry, and now
Crew Chief. Widget Template has no proof receipt. The other twelve receipts
are ancestors of their current heads. The permanent fix is a trusted Buzz
self-hosted runner (or equivalent securely-attested execution lane) that
records source SHA, source-tree fingerprint, preview SHA-256, rig image digest,
and exit receipts. A hosted runner cannot honestly claim access to the private
Buzz rig without that runner and credential setup.

### P1 — repo protections and action provenance are incomplete

- None of the 16 `main` branches currently has GitHub branch protection.
- 15/16 use mutable action tags such as `actions/checkout@v4`; Foundry is the
  reference implementation with pinned action SHAs and least-privilege
  `contents: read`.
- Eight repositories have stale contributing-clanker lanes whose freshness
  check is `continue-on-error`; the workflow can be green while its shared
  gates are stale.
- Six repos declare coverage thresholds but invoke raw `node --test` in CI,
  bypassing the threshold command. Ten declare no coverage floor.

### P2 — public portfolio drift

`README.md` in the umbrella repository fails
`bash scripts/refresh-metrics.sh --check`. Its generated marketplace table and
verification language are stale, and `plugins.json` omits Desk Transition.
The portfolio must be updated to distinguish: live + exact-head verified,
live but snapshot-verified, submitted / security remediation, and local-only.

Eight newer entry repos lack the common governance pack (SECURITY,
CONTRIBUTING, Code of Conduct, and Dependabot). Docket alone lacks the shared
`assets/banner.svg` convention.

## Ordered release program

1. Preserve independent marketplace approval: do not apply maintainer-only
   labels ourselves. Follow #3235 and the five security issues to closure.
2. Repair the five TOCTOU classes with descriptor-bound helpers and hostile
   replacement/FIFO/parent-swap tests; rerun gates and the real rig; submit
   exact commits.
3. Establish one Buzz self-hosted E2E runner lane and make its signed receipt
   a required check. Add preview and source provenance fields to receipts.
4. Enable `main` branch protection with required checks, pin actions to commit
   SHAs, and synchronize the eight stale gate lanes to the Foundry standard.
5. Enforce coverage through the package test command and add coverage floors
   for all widgets, followed by a per-plugin real render refresh.
6. Correct the umbrella inventory and marketplace status language, then only
   announce the status backed by the exact SHA receipts.

## Evidence commands

```sh
# local unit suite
npm test

# repository submission gates
scripts/run-plugin-gates.sh .

# real Buzz rig: static compatibility and actual shell render
scripts/rig-verify.sh .
scripts/rig-render.sh . /tmp/plugin-render.png

# umbrella public-metadata drift check
cd /home/jeremy/000-projects/omarchy
bash scripts/refresh-metrics.sh --check
```

## Honest public status

Use this until the ordered program closes: **"16 maintained Omarchy plugin
repositories; 9 live marketplace listings; all local suites currently green;
marketplace verification and production-render certification are tracked per
exact commit."**

