# Omarchy Plugins

> Fifteen bar plugins for **Omarchy Quattro**, plus the widget template they are all built from. All fifteen are live in the marketplace, every repository ships the same security lane, and every network body parses in a file a unit test can load without a shell.

**Built and maintained by [Jeremy Longshore](https://github.com/jeremylongshore) / [Intent Solutions](https://intentsolutions.io).**

**Live work → [github.com/jeremylongshore](https://github.com/jeremylongshore?tab=repositories&q=omarchy)**
**Marketplace → [omarchyplugins.com](https://omarchyplugins.com)**

[![Marketplace: 15 live](https://img.shields.io/badge/marketplace-15%20live-1a7f37)](https://omarchyplugins.com)
[![Template: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/jeremylongshore/omarchy-widget-template/blob/main/LICENSE)
[![Gates: 12](https://img.shields.io/badge/pre--submit%20gates-12-0969da)](#the-gate-lane)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/U5S225PTME)

---

## What this is

This repository is the **Intent Solutions organization landing page** for the Omarchy plugin work. Nothing installs from here. Each plugin ships and develops in its own repository, and each is listed independently on the marketplace. This page is the single place they read as one body of work.

[Omarchy](https://omarchy.org) is DHH's opinionated Arch and Hyprland desktop. **Quattro** is its plugin system: a bar widget is a [Quickshell](https://quickshell.org) QML component that Omarchy loads into a slot on the bar, with an optional panel that opens under it. A plugin is a git repository with a `manifest.json`, and you install one by pointing Omarchy at the URL.

## The catalog

<!-- METRICS:START -->
Marketplace data generated at `2026-08-31T23:38:05.548Z`, across 2030 listed plugins. Regenerate with `bash scripts/refresh-metrics.sh`; do not edit this table by hand.

| Plugin | What it does | Source | Category | Views | Copies | Hearts |
| --- | --- | --- | --- | --: | --: | --: |
| **Bazaar** | The plugin marketplace itself, in the bar. Search 2,000+ listings, read a plugin's detail, and copy its install command without opening a browser. | [repo](https://github.com/jeremylongshore/omarchy-bazaar-entry) | [Productivity](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.bazaar) | 251 | 26 | 0 |
| **Pit Wall** | The Formula 1 race weekend on the bar. Countdown to the next session, live timing during one, and the pill goes quiet between race weekends. | [repo](https://github.com/jeremylongshore/omarchy-pit-wall-entry) | [Widgets](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.pit-wall) | 141 | 20 | 3 |
| **Wait State** | Linux PSI pressure stall information in the bar. Shows when the machine is stalled on IO, memory or CPU, which load average cannot tell you. | [repo](https://github.com/jeremylongshore/omarchy-wait-state-entry) | [System](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.wait-state) | 135 | 9 | 0 |
| **MLB Booth** | Live baseball on the bar. Score, half inning, base state and count for the game you follow, collapsing to nothing on an off day. | [repo](https://github.com/jeremylongshore/omarchy-mlb-booth-entry) | [Widgets](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.mlb-booth) | 119 | 6 | 1 |
| **X Files** | The replies to your own X posts, read from the desktop. A drainable queue so a conversation does not get lost in the feed. | [repo](https://github.com/jeremylongshore/omarchy-x-files-entry) | [Productivity](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.x-files) | 152 | 2 | 1 |
| **Docket** | The GitHub pull requests actually waiting on you, as a queue. Review requests and your own PRs with a changed state, not a notification firehose. | [repo](https://github.com/jeremylongshore/omarchy-docket-entry) | [Developer Tools](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.docket) | 144 | 3 | 1 |
| **Crew Chief** | Which of your AI coding agent sessions is blocked on you. Reads session state across running agents so a waiting prompt does not sit unseen. | [repo](https://github.com/jeremylongshore/omarchy-crew-chief-entry) | [Productivity](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.crew-chief) | 146 | 13 | 2 |
| **Listening Post** | A curated AI vendor release radar. Model releases, pricing changes and status incidents from 29 sources, in four lanes, quiet when nothing shipped. | [repo](https://github.com/jeremylongshore/omarchy-listening-post-entry) | [Widgets](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.listening-post) | 421 | 16 | 0 |
| **Desk Transition** | Safe local monitor scenes for changing display arrangements and returning focus to the laptop panel without memorizing Hyprland commands. | [repo](https://github.com/jeremylongshore/omarchy-desk-transition-entry) | [Productivity](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.desk-transition) | 147 | 10 | 2 |
| **Foundry** | Turn a product idea into a governed Omarchy plugin workspace with deliberate scaffolding, validation, and an evidence-first path to submission. | [repo](https://github.com/jeremylongshore/omarchy-foundry-entry) | [Developer Tools](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.foundry) | 74 | 2 | 0 |
| **Loose Ends** | A private local queue for small commitments that are easy to lose between work sessions, with fast capture and deliberate clearing. | [repo](https://github.com/jeremylongshore/omarchy-loose-ends-entry) | [Productivity](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.loose-ends) | 59 | 0 | 0 |
| **Capture Conveyor** | A local capture lane that turns a quick thought into a deliberate next destination without opening a project manager or browser. | [repo](https://github.com/jeremylongshore/omarchy-capture-conveyor-entry) | [Widgets](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.capture-conveyor) | 98 | 5 | 0 |
| **Workspace Storyboard** | See the work held by each Hyprland workspace, jump to one, and follow a local re-entry trail when the desktop context gets scattered. | [repo](https://github.com/jeremylongshore/omarchy-workspace-storyboard-entry) | [Widgets](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.workspace-storyboard) | 198 | 6 | 1 |
| **Quiet Queue** | Start a deliberate focus interval that owns Do Not Disturb only while the session is active, then restores the prior notification state. | [repo](https://github.com/jeremylongshore/omarchy-quiet-queue-entry) | [Productivity](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.quiet-queue) | 104 | 2 | 0 |
| **Flow Boundary** | A private local ritual for marking intentional starts and stops, with visible FLOW or PAUSE state and a short transition history. | [repo](https://github.com/jeremylongshore/omarchy-flow-boundary-entry) | [Productivity](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.flow-boundary) | 278 | 3 | 1 |
| **Widget Template** | The skeleton every entry above is built from. BarWidget, Panel, a node-testable Model.js, the 12-gate pre-submit lane and CI, so a new widget starts already passing. | [repo](https://github.com/jeremylongshore/omarchy-widget-template) | not a listing | n/a | n/a | n/a |

**15 of 15 listed** on the marketplace, 2467 views, 123 copies, 12 hearts.

### Install

Every command below is read from the marketplace catalog's own `installCommand` field at refresh time, so it cannot drift from what the listing says.

```bash
# Bazaar
omarchy plugin add https://github.com/jeremylongshore/omarchy-bazaar-entry.git --enable
# Pit Wall
omarchy plugin add https://github.com/jeremylongshore/omarchy-pit-wall-entry.git --enable
# Wait State
omarchy plugin add https://github.com/jeremylongshore/omarchy-wait-state-entry.git --enable
# MLB Booth
omarchy plugin add https://github.com/jeremylongshore/omarchy-mlb-booth-entry.git --enable
# X Files
omarchy plugin add https://github.com/jeremylongshore/omarchy-x-files-entry.git --enable
# Docket
omarchy plugin add https://github.com/jeremylongshore/omarchy-docket-entry.git --enable
# Crew Chief
omarchy plugin add https://github.com/jeremylongshore/omarchy-crew-chief-entry.git --enable
# Listening Post
omarchy plugin add https://github.com/jeremylongshore/omarchy-listening-post-entry.git --enable
# Desk Transition
omarchy plugin add https://github.com/jeremylongshore/omarchy-desk-transition-entry.git --enable
# Foundry
omarchy plugin add https://github.com/jeremylongshore/omarchy-foundry-entry.git --enable
# Loose Ends
omarchy plugin add https://github.com/jeremylongshore/omarchy-loose-ends-entry.git --enable
# Capture Conveyor
omarchy plugin add https://github.com/jeremylongshore/omarchy-capture-conveyor-entry.git --enable
# Workspace Storyboard
omarchy plugin add https://github.com/jeremylongshore/omarchy-workspace-storyboard-entry.git --enable
# Quiet Queue
omarchy plugin add https://github.com/jeremylongshore/omarchy-quiet-queue-entry.git --enable
# Flow Boundary
omarchy plugin add https://github.com/jeremylongshore/omarchy-flow-boundary-entry.git --enable
```
<!-- METRICS:END -->

## One shared architecture

All fifteen entries share one deliberate shell shape while telling different product stories. The shape lives in [`omarchy-widget-template`](https://github.com/jeremylongshore/omarchy-widget-template) and every entry inherits it:

| File | Role |
| --- | --- |
| `BarWidget.qml` | The bar host. Owns the slot and the pill button, and the shape contract the shell uses to summon, hide and toggle the panel. |
| `Panel.qml` | Data lifecycle and popup UI. Fetches through `Process` and `StdioCollector`, never an in-process HTTP client. |
| `Model.js` | The pure data layer. Loads in Quickshell **and** in node, so the entire parse path unit-tests without a running shell. |
| `tests/` | `node --test` against fixtures captured from the real API bodies. |

The reason `Model.js` is a separate file is the reason the whole set holds together: a widget whose parsing only runs inside a compositor is a widget nobody can test, and an untested parser facing a live API is where every one of the defects below came from.

## The security posture every entry inherits

These are not style rules. Each maps to a defect that reached a shipped entry and had to be swept out of it afterwards.

1. **Every network body parses in `Model.js`.** Pure functions. Malformed input returns the empty shape, so the panel keeps last-good state instead of tearing down.
2. **Every API string passes `Model.clean()`** before QML renders it. Strips angle brackets and control characters, caps length.
3. **Every `Text` that renders API data declares `textFormat: Text.PlainText`.** QML's `AutoText` sniffs strings for HTML, and a hostile payload can otherwise trigger an outbound image fetch from a desktop widget.
4. **Every `curl` argv carries `--max-time` and `--max-filesize`.** An unbounded body freezes the shell's UI thread inside `JSON.parse`.
5. **The pill never silently vanishes.** An unreachable API reads as loading, not as a widget that uninstalled itself.
6. **Omakase constants over settings knobs.** A manifest settings schema exists only for choices a user genuinely owns.

## The gate lane

Twelve gates run before anything is submitted, vendored into every entry and hash-pinned so a shrunken lane cannot report clean against itself:

| Gate | What it refuses |
| --- | --- |
| `c28-voice-no-dashes` | Em and en dashes in shipped text |
| `c29-private-names` | Private names and internal paths leaking into a public tree |
| `c30-md-strikethrough` | Markdown artifacts in rendered copy |
| `c31-omarchy-qml-security` | The QML security contract above, mechanically |
| `c34-omarchy-exec-injection` | Untrusted data reaching a process argv |
| `c35-omarchy-runtime-dependency` | A manifest that declares an entry point it does not carry |
| `c36-omarchy-qml-overflow` | Unbounded text and layout overflow in the pill and panel |
| `c38-omarchy-ssrf-host-allowlist` | A user-supplied host reaching a private address |
| `c40-omarchy-panel-design` | Panel window types used where the shell expects another |
| `c41-omarchy-state-file-hygiene` | Mutable local state written without descriptor-safe lifecycle controls |
| `c42-omarchy-local-resource-budget` | Recurring local scans that buffer or sort unbounded input |
| `c43-omarchy-marketplace-presentation` | Thin copy, generic banners, stale render receipts, clipped previews, or missing visual approval |

Above the gates sits [`/omarchy-ship`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills), the submission lane. Its one design rule is that **no layer may report a conclusion whose scope it never established.** A gate that could not run reports `UNPROVEN`, never `PASS` and never "not applicable". That rule exists because every layer of this stack has, at some point, reported success without having checked anything: a runner that counted `SKIP` as `PASS`, a gate that answered about a file it had never opened, and a CI job gated on an unset variable rendering as a grey tick that reads like a completed review.

## Build your own

```bash
gh repo create YOURNAME/omarchy-your-widget-entry \
  --template jeremylongshore/omarchy-widget-template --public --clone
```

Then replace the example fetch in `Panel.qml`, the parse functions in `Model.js`, and the placeholder fields in `manifest.json`. The gates, the CI and the test harness are already wired.

## Keeping this page honest

The table above is generated, never hand-edited:

```bash
bash scripts/refresh-metrics.sh          # rewrite the table from the live endpoints
bash scripts/refresh-metrics.sh --check  # exit 1 if it is stale (this is the CI gate)
```

It reads the ids from [`plugins.json`](plugins.json) rather than from the catalog, so a marketplace rename cannot quietly delete a row, and it reads each install command out of the catalog's own `installCommand` field, so this page cannot print a command the listing disagrees with. [A scheduled workflow](.github/workflows/refresh-metrics.yml) reruns it daily and commits when the numbers move, and the same script runs as `--check` on every pull request so a hand-edited table fails the build.

## Research

- [`000-docs/001-RL-NEXT-next-omarchy-plugin-concepts.md`](000-docs/001-RL-NEXT-next-omarchy-plugin-concepts.md): three specced concepts, chosen against live catalog saturation counts and the HCI literature on peripheral displays, rather than against what looks good in a screenshot.
- [`000-docs/002-LS-BLOK-listening-post-listing-blocked.md`](000-docs/002-LS-BLOK-listening-post-listing-blocked.md): the historical security finding that once blocked Listening Post, retained as a remediation record.

---

Built and maintained by **Jeremy Longshore** · **Intent Solutions**. [intentsolutions.io](https://intentsolutions.io)
