# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The Intent Solutions **public portfolio** for the Omarchy Quattro plugin work. It owns the
README catalog and the static site published at `oma.intentsolutions.io`. **No plugin code
lives here and nothing installs from here.** Planning documents under `000-docs/`
and narrowly scoped repository-governance tooling may live here. Product implementation
belongs in the app and entry repositories.

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

## Commands

There is no package manifest and no compile step. The only build is the generator pipeline
described in the next section. The toolchain is `bash`, `python3` (stdlib
only), and Node 22 for `node --check` and `node --test`.

```bash
bash scripts/check-site.sh                 # the whole PR gate. Offline, deterministic. Run before every push.
python3 -m http.server 4173 --directory site   # preview the site at http://127.0.0.1:4173

# one test
python3 -m unittest tests.test_catalog_pipeline -k <substring>
python3 -m unittest tests.test_fetch_github_metadata -k <substring>
node --test --test-name-pattern='<regex>' tests/site-data.test.mjs

python3 scripts/build-site-pages.py --check    # generated pages vs site/data/plugins.json, no network
python3 tests/site-browser.py                  # Playwright journeys. NOT in CI. See below.
```

`tests/site-browser.py` needs the preview server above already running (override with
`OMA_SITE_BASE_URL`) and a Python with `playwright` installed, which the system Python on
the dev box does not have. It mocks the live stats and Perception APIs and writes the
desktop and mobile screenshots a visible-change PR must attach to `/tmp/oma-site-browser`.

`check-site.sh` is what both `site-ci.yml` and the pull request lane of
`refresh-metrics.yml` run. It syntax-checks the site JS, runs both unit suites, verifies
the generated pages, then lints every `site/**/*.html` for title, meta description,
favicon, Umami script (legal routes exempt), image alt text, and dashes. A new page that
skips any of those fails CI.

## How the catalogue pipeline fits together

One hand-edited inventory, three generated surfaces, and a script that owns each hop:

```
plugins.json  (hand-edited: id, repo, family, lifecycle, pitch)
   |
   |  refresh-metrics.sh fetches marketplace catalog.json + /v1/stats (curl) and
   |  repo, manifest and preview facts (fetch_github_metadata.py, GitHub hosts allowlisted)
   v
catalog_pipeline.py  validates the inventory, merges the snapshots
   |--> README.md            block between the METRICS markers
   '--> site/data/plugins.json
            |
            v
      build-site-pages.py
            |--> site/plugins/<slug>/index.html      one detail page per plugin
            '--> site/index.html                     block between the STATIC_CATALOG markers
```

- `site/assets/app.js` renders the interactive catalogue in the browser from
  `site/data/plugins.json` and overlays live counters from the stats API. The
  `STATIC_CATALOG` block is the no-JavaScript fallback for the same data, which is why
  both are generated from one file.
- `catalog_pipeline.py` rejects bad inventory rather than rendering it: ids must match
  `io.github.jeremylongshore.<slug>`, repos `omarchy-<slug>-entry`, `family` must be in the
  `families` array, `lifecycle` one of `listed`, `under-review`, `developing`, `unreleased`,
  `retired`, `not-listed`.
- `refresh-metrics.sh --check` hits the live endpoints, so it races moving counters. That
  is why CI runs `check-site.sh` (committed surfaces agree with each other) and only the
  daily scheduled job talks to the network. That job commits generated files **straight to
  main**, so rebase before pushing and never resolve a conflict in a generated file by
  hand: rerun the script.
- `deploy-site.yml` publishes `site/` to GitHub Pages on any push to main that touches
  `site/**`. Merge is deploy. There is no staging.

Everything else under `site/` is hand-authored static HTML (product surfaces
`the-beacon-wakes/`, `bluegoldblue/`, `omaquest/`, and the legal routes), with two
exceptions that are build output from other repos and must not be edited here:
`site/perception/` (a hashed build bundle) and `site/the-beacon-wakes/play/`, which
`scripts/publish-beacon-demo.sh <path-to-omarchy-typing-adventure>` rebuilds and which must
ship without source maps. Read `PRODUCT.md` before changing claims on a product surface and
`DESIGN.md` before changing how one looks.

The showcase campaign scripts (`build-showcase-packet.py`, `plane-sync-packets.py`,
`plane-assign-when-accepted.sh`, `campaign-baseline.py`) are dev-box operator tools, not
part of CI. They share one rule with the pipeline: `showcase-packets.json` holds only
authored words, and every link, install command and metric is appended from the live
catalog at build time. A URL in that file fails the builder's lint.

## The one rule about generated files

**Never hand-edit a generated surface.** There are four:

- the block between `<!-- METRICS:START -->` and `<!-- METRICS:END -->` in `README.md`
  (written by `catalog_pipeline.py`)
- all of `site/data/plugins.json` (written by `catalog_pipeline.py`)
- all of `site/plugins/` (written by `build-site-pages.py`)
- the block between the `STATIC_CATALOG` markers in `site/index.html` (written by
  `build-site-pages.py`)

`scripts/refresh-metrics.sh` owns them and a scheduled workflow reruns it daily. Pull requests run `scripts/check-site.sh` to prove the committed README and site
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
- Beads live in the umbrella `~/000-projects/.beads/`, labelled `omarchy`. The original
  stand-up epic `bd_000-projects-ypaf` is closed. The Beacon Wakes (typing adventure) work
  runs under `bd_000-projects-v41u`. Close through `bd-sync close`, never raw `bd close`.

## Things that are true and easy to get wrong

- **omaTrail is listed.** The official catalog contains
  `io.github.jeremylongshore.omatrail`. Treat the live catalog as lifecycle authority.
- **The marketplace moves fast.** It passed 1,363 listings on 2026-08-25 and gains dozens a
  day. Any count in a doc here is a snapshot with the jq filter printed next to it. Re-derive
  before citing.
- The gate lane is vendored per entry repo and hash-pinned. It is not in this repo, and this
  repo describes it rather than running it.
