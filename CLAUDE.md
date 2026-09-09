# CLAUDE.md

Guidance for Claude Code working in this repository.

## What this repo is

The Intent Solutions **public portfolio** for the Omarchy Quattro plugin work. It owns the
README catalog and the static site published at `oma.intentsolutions.io`. **No plugin code
lives here and nothing installs from here.**

The plugin repos it presents all live under `jeremylongshore`:

| Repo | Role |
| --- | --- |
| `omarchy-widget-template` | The template every entry is built from. The highest-leverage asset in the set. |
| `omarchy-bazaar-entry` | Bazaar |
| `omarchy-pit-wall-entry` | Pit Wall |
| `omarchy-wait-state-entry` | Wait State |
| `omarchy-mlb-booth-entry` | MLB Booth |
| `omarchy-x-files-entry` | X Files |
| `omarchy-docket-entry` | Docket |
| `omarchy-crew-chief-entry` | Crew Chief |
| `omarchy-listening-post-entry` | Listening Post |
| `omarchy-desk-transition-entry` | Desk Transition |
| `omarchy-foundry-entry` | Foundry |
| `omarchy-loose-ends-entry` | Loose Ends |
| `omarchy-capture-conveyor-entry` | Capture Conveyor |
| `omarchy-workspace-storyboard-entry` | Workspace Storyboard |
| `omarchy-quiet-queue-entry` | Quiet Queue |
| `omarchy-flow-boundary-entry` | Flow Boundary |
| `omarchy-omatrail-entry` | omaTrail. Listed in the official marketplace. |

All are cloned as siblings under `~/000-projects/`.

## The one rule about the README

**Never hand-edit the block between `<!-- METRICS:START -->` and `<!-- METRICS:END -->`.**
It is generated. `scripts/refresh-metrics.sh` owns it and a scheduled workflow reruns it
daily. Pull requests run `scripts/check-site.sh` to prove the committed README and site
snapshot agree without racing live counters.

```bash
bash scripts/refresh-metrics.sh          # rewrite from the live endpoints
bash scripts/refresh-metrics.sh --check  # compare both surfaces with a live snapshot
```

To add or remove a plugin, edit `plugins.json` and rerun the script. Do not add a row by
hand, edit `site/data/plugins.json`, or put an install command in the README by hand.
Install commands are read out of the marketplace catalog's own `installCommand` field so
neither public surface can print a command the listing disagrees with.

The freshness stamp in the generated block is the **catalog's own `generatedAt`**, not the
local clock. That is what makes two consecutive runs byte-identical. Do not replace it with
`date`.

## House conventions that apply here

- **No em dashes or en dashes anywhere.** Same rule the `c28` gate enforces in every entry
  repo. Use a period, comma, colon or parentheses.
- Docs go in flat `000-docs/` under the `NNN-CC-ABCD-description.md` filing standard.
- Branch from `origin/main`, never commit to main. Commit subject is
  `type(scope): imperative subject`, body carries what, why, and how it was verified.
- Beads live in the umbrella `~/000-projects/.beads/` under the epic
  `bd_000-projects-ypaf`, labelled `omarchy`. Close through `bd-sync close`, never raw
  `bd close`.

## Things that are true and easy to get wrong

- **omaTrail is listed.** The official catalog contains
  `io.github.jeremylongshore.omatrail`. Treat the live catalog as lifecycle authority.
- **The marketplace moves fast.** It passed 1,363 listings on 2026-08-25 and gains dozens a
  day. Any count in a doc here is a snapshot with the jq filter printed next to it. Re-derive
  before citing.
- The gate lane is vendored per entry repo and hash-pinned. It is not in this repo, and this
  repo describes it rather than running it.
