# Omarchy Plugins

> Eight bar plugins for **Omarchy Quattro**, plus the widget template they are all built from. Every listed entry is marketplace-verified, every one ships the same security lane, and every network body parses in a file a unit test can load without a shell.

**Built and maintained by [Jeremy Longshore](https://github.com/jeremylongshore) / [Intent Solutions](https://intentsolutions.io).**

**Live work → [github.com/jeremylongshore](https://github.com/jeremylongshore?tab=repositories&q=omarchy)**
**Marketplace → [omarchyplugins.com](https://omarchyplugins.com)**

[![Marketplace: verified](https://img.shields.io/badge/marketplace-verified-1a7f37)](https://omarchyplugins.com)
[![Template: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/jeremylongshore/omarchy-widget-template/blob/main/LICENSE)
[![Gates: 9](https://img.shields.io/badge/pre--submit%20gates-9-0969da)](#the-gate-lane)

---

## What this is

This repository is the **Intent Solutions organization landing page** for the Omarchy plugin work. Nothing installs from here. Each plugin ships and develops in its own repository, and each is listed independently on the marketplace. This page is the single place they read as one body of work.

[Omarchy](https://omarchy.org) is DHH's opinionated Arch and Hyprland desktop. **Quattro** is its plugin system: a bar widget is a [Quickshell](https://quickshell.org) QML component that Omarchy loads into a slot on the bar, with an optional panel that opens under it. A plugin is a git repository with a `manifest.json`, and you install one by pointing Omarchy at the URL.

## The catalog

<!-- METRICS:START -->
Marketplace data generated at `2026-08-25T18:07:27.272Z`, across 1363 listed plugins. Regenerate with `bash scripts/refresh-metrics.sh`; do not edit this table by hand.

| Plugin | What it does | Source | Category | Views | Copies | Hearts |
| --- | --- | --- | --- | --: | --: | --: |
| **Bazaar** | The plugin marketplace itself, in the bar. Search 1,300+ listings, read a plugin's detail, copy its install command, without opening a browser. | [repo](https://github.com/jeremylongshore/omarchy-bazaar-entry) | [Productivity](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.bazaar) | 199 | 20 | 0 |
| **Pit Wall** | The Formula 1 race weekend on the bar. Countdown to the next session, live timing during one, and the pill goes quiet between race weekends. | [repo](https://github.com/jeremylongshore/omarchy-pit-wall-entry) | [Widgets](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.pit-wall) | 113 | 19 | 3 |
| **Wait State** | Linux PSI pressure stall information in the bar. Shows when the machine is stalled on IO, memory or CPU, which load average cannot tell you. | [repo](https://github.com/jeremylongshore/omarchy-wait-state-entry) | [System](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.wait-state) | 100 | 9 | 0 |
| **MLB Booth** | Live baseball on the bar. Score, half inning, base state and count for the game you follow, collapsing to nothing on an off day. | [repo](https://github.com/jeremylongshore/omarchy-mlb-booth-entry) | [Widgets](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.mlb-booth) | 91 | 2 | 1 |
| **X Files** | The replies to your own X posts, read from the desktop. A drainable queue so a conversation does not get lost in the feed. | [repo](https://github.com/jeremylongshore/omarchy-x-files-entry) | [Productivity](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.x-files) | 90 | 1 | 1 |
| **Docket** | The GitHub pull requests actually waiting on you, as a queue. Review requests and your own PRs with a changed state, not a notification firehose. | [repo](https://github.com/jeremylongshore/omarchy-docket-entry) | [Developer Tools](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.docket) | 89 | 3 | 1 |
| **Crew Chief** | Which of your AI coding agent sessions is blocked on you. Reads session state across running agents so a waiting prompt does not sit unseen. | [repo](https://github.com/jeremylongshore/omarchy-crew-chief-entry) | [Productivity](https://omarchyplugins.com/plugin.html?id=io.github.jeremylongshore.crew-chief) | 66 | 8 | 1 |
| **Listening Post** | A curated AI vendor release radar. Model releases, pricing changes and status incidents from 29 sources, in four lanes, quiet when nothing shipped. | [repo](https://github.com/jeremylongshore/omarchy-listening-post-entry) | not listed | not listed | not listed | not listed |
| **Widget Template** | The skeleton every entry above is built from. BarWidget, Panel, a node-testable Model.js, the nine-gate pre-submit lane and CI, so a new widget starts already passing. | [repo](https://github.com/jeremylongshore/omarchy-widget-template) | not a listing | n/a | n/a | n/a |

**7 of 8 listed and verified** on the marketplace, 748 views, 62 copies, 7 hearts.

Not currently in the catalog: Listening Post. See [000-docs/002-LS-BLOK-listening-post-listing-blocked.md](000-docs/002-LS-BLOK-listening-post-listing-blocked.md) for why, and what unblocks it.

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
```
<!-- METRICS:END -->

## One shared architecture

All eight entries are the same widget three times over, with a different data source bolted on. That is deliberate. The shape lives in [`omarchy-widget-template`](https://github.com/jeremylongshore/omarchy-widget-template) and every entry inherits it:

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

Nine gates run before anything is submitted, vendored into every entry and hash-pinned so a shrunken lane cannot report clean against itself:

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
- [`000-docs/002-LS-BLOK-listening-post-listing-blocked.md`](000-docs/002-LS-BLOK-listening-post-listing-blocked.md): the open finding keeping the eighth entry out of the catalog, and what closes it.

---

Built and maintained by **Jeremy Longshore** · **Intent Solutions**. [intentsolutions.io](https://intentsolutions.io)
