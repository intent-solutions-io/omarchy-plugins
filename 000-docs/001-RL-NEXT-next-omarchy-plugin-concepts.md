# Three next Omarchy plugins, chosen from evidence

**Date:** 2026-08-25
**Author:** Jeremy Longshore / Intent Solutions
**Method:** live catalog saturation counts, live per-plugin engagement stats, and the HCI
literature on peripheral displays and interruption cost. No concept below was picked
because it would look good in a screenshot.

---

## 1. What the board actually rewards

All counts below are reproducible against `https://omarchyplugins.com/catalog.json`
(snapshot `generatedAt: 2026-08-25T18:07:27.272Z`, 1,363 plugins) and
`https://api.omarchyplugins.com/v1/stats`.

Top of the board by copies:

| Copies | Hearts | Category | Plugin |
| --: | --: | --- | --- |
| 1,491 | 128 | Hardware | hyprmoncfg: Multi-Monitor Manager |
| 957 | 92 | Appearance | Lock Screen Explorer |
| 897 | 54 | System | Notification Center |
| 863 | 75 | Appearance | Omaland |
| 746 | 63 | Appearance | Navbar Cat |
| 729 | 53 | Widgets | AI Usage |
| 560 | 86 | Productivity | Screen Time |
| 533 | 30 | System | Vitals |

```bash
jq -r --slurpfile s stats.json \
  '[.plugins[]|{name,category,c:($s[0].plugins[.id].copies//0)}]|sort_by(-.c)|.[:8][]' catalog.json
```

Every one of those is a **broad daily-driver utility for hardware, system state or
appearance**. Not one is an interest feed. The eight entries in this org are, with two
exceptions, interest feeds in the two most crowded categories: Widgets holds 446 listings
and Productivity 274, together 53 percent of the marketplace.

The two exceptions are the two that point at the answer. **Wait State** reads Linux PSI and
answers "is this machine stalled." **Crew Chief** reads agent session state and answers "is
something waiting on me." Both are *system state made legible at a glance*, which is exactly
the shape the top of the board is made of. The next three should all be that shape.

## 2. Saturation, measured

Counted by matching name plus description plus tags, case-insensitively. Every filter is
printed so any number here can be re-derived rather than trusted.

```bash
# template: substitute PATTERN
jq '[.plugins[]|select((.name+" "+.description+" "+((.tags//[])|join(" ")))
     |ascii_downcase|test("PATTERN"))]|length' catalog.json
```

| Lane | Count | Pattern |
| --- | --: | --- |
| git / repo status | **3** | `git status\|uncommitted\|dirty repo\|worktree\|repository status` |
| presenter / annotate | **4** | `presentation\|presenter\|annotate\|annotation\|screen draw\|whiteboard\|zoom.?it` |
| home assistant / IoT | **6** | `home assistant\|homeassistant\|mqtt\|zigbee\|smart home\|iot\|home-assistant` |
| backup / snapshot | **7** | `backup\|restic\|borg\|btrfs snapshot\|snapper\|timeshift\|rsnapshot` |
| cert / secret expiry | 9 | `certificate\|ssl expiry\|tls expiry\|gpg key\|ssh key\|token expiry\|secret` |
| screenshare / privacy | 9 | `screenshare\|screen share\|screen recording\|privacy\|camera indicator\|mic indicator` |
| updates / pacman | 13 | `pacman\|aur\|package update\|yay\|paru\|system update` |
| docker / container | 16 | `docker\|podman\|container\|kubernetes\|k8s` |
| focus / pomodoro | 17 | `pomodoro\|focus timer\|deep work\|distraction` |
| disk / filesystem | 18 | `disk usage\|disk space\|filesystem\|df \|storage usage\|smart\|nvme health` |
| clipboard | 20 | `clipboard\|clipse\|cliphist` |
| cpu / gpu temp | 32 | `cpu temp\|gpu\|nvidia\|amdgpu\|fan speed\|sensors` |
| battery / power | 40 | `battery\|power profile\|tlp\|thermal` |
| vpn / network | 58 | `vpn\|wireguard\|tailscale\|openvpn\|network` |
| calendar | 59 | `calendar\|agenda\|meeting\|ical` |
| audio / media | 72 | `audio\|volume\|pipewire\|pulseaudio\|spotify\|music\|mpris` |
| multi-monitor / display | **101** | `monitor\|display\|hdmi\|resolution\|refresh rate\|kanshi\|wlr-randr` |
| spotlight / command palette | **107** | `spotlight\|command palette\|launcher\|app launcher\|fuzzy find\|quick launch\|omni.?search` |

### Corrections to the working idea list

- **A spotlight or command palette was the top-ranked idea. It is the worst entry point on
  the board**, at 107 existing listings. Duplicates are the marketplace's stated failure mode.
- **Multi-monitor is not open either**, at 101 listings, and the single highest-copy plugin in
  the entire marketplace already owns that lane outright.
- **Backup was ranked thin on the strength of "Time Machine just proved demand." Time Machine
  is not in the catalog.** `jankeesvw/omarchy-time-machine` exists on GitHub, and that author
  has five other plugins listed, including Notification Center at 465 copies. But no listing
  named Time Machine exists, so it cannot be cited as marketplace-proven demand. The real
  in-catalog evidence for that lane is Snapshots at 28 copies and OmaVault at 34, which is
  genuine but modest. The lane is thin because it is **hard**, not because nobody wants it.
- **The plugin competition closed on 2026-08-24 at 09:00 CEST**, judged by the Omarchy Core
  Team, with prizes of $2,500 / $1,000 / $500 and winners announced no later than
  Friday 2026-08-28. Nothing built now can enter it. What that changes: the amplification
  window is **this week**, driven by the results announcement and the traffic it pulls to the
  marketplace, and it is a listing-and-promotion window rather than a build window.

## 3. What the literature says about this shape of widget

A bar pill is an ambient display in the strict HCI sense, and that literature is specific
about what separates one that works from one that gets uninstalled.

- **Mankoff et al., "Heuristic evaluation of ambient displays" (CHI 2003, 626 citations,
  paperId `4681baf847295e7f9ad4632c2b18a0eea321285c`).** The canonical heuristic set for
  exactly this artifact. Two of its heuristics carry the whole design: *sufficient information
  design* (display just enough, and no more) and *peripherality of display* (the thing must be
  ignorable, and must move to the center of attention only when it should). This is the
  formal statement of the rule the existing eight already follow: the pill goes quiet when
  there is nothing to say.
- **Altmann and Trafton, "Task Interruption: Resumption Lag and the Role of Cues" (2004, 219
  citations, paperId `039661ae007dd232b4a0170ce66d56e49ae2faba`).** Resuming an interrupted
  task costs measurable time, and a **cue present in the environment at resumption reduces
  that lag.** This is the strongest available argument for a *state* widget over a *feed*
  widget: a feed adds interruptions, a state pill is a resumption cue. It is the theory behind
  concept 3 below, and the reason Crew Chief works.
- **Plaue, Miller and Stasko, "Is a picture worth a thousand words? An evaluation of
  information awareness displays" (2004, 84 citations, paperId
  `dbe5ab3fb33280b69a9e683455ef991cdf19c1e2`).** Comparative evaluation of information
  awareness displays, and the direct evidence that denser is not better: comprehension does
  not scale with information shown.
- **Wu and Yang, "A Design Space for Peripheral Interaction: Evidence Mapping and Transferable
  Implications" (AHFE 2026, paperId `3cb19afef1c2335a8c397a26dbd14af22fbe2159`).** Maps 188
  studies on an attention-demand by spatial-placement grid and finds the landscape **heavily
  skewed toward background environmental systems, with sparse regions elsewhere.** It also
  names the recurring tension this design has to resolve: *detectability versus
  disruptiveness*. That tension is the pill design problem stated exactly.
- **Occhialini, van Essen and Eggen, "Design and Evaluation of an Ambient Display to Support
  Time Management during Meetings" (2011, 41 citations, paperId
  `b4c1d462cc449bac3bba7d95abd60572d7033e4b`)** and **Börner, Kalz and Specht, "Lead me
  gently: attention-aware ambient learning displays" (2014, 18 citations, paperId
  `448870d9f18f1203404c59be9b3dda9e7da5686d`)** both find that an ambient display which
  modulates its own salience by context outperforms a constant one. Börner's is a controlled
  study with 52 participants showing the attention-aware variant beat the control on
  comprehension. Practical translation: **escalation tiers beat a static badge.**
- On the IoT lane specifically, **Yigitbas and Karch (2025, paperId
  `902064c0c51c25173d3b362326813030f4253023`)** ran a user study against Home Assistant's own
  interface and found it scored poorly on usability and interactivity for non-expert users,
  and **Kar and Ingkasit (2024, paperId `584a49324699edc35f8419b1ea4be11a7dd3f5b4`)**
  identified the same gap in existing smart-home dashboards. The complaint in both is that the
  interface is a control surface when what users mostly want is an answer.

**One thing the literature did not supply.** There is no good evidence base on personal
backup verification behaviour. Two searches returned nothing usable, so concept 2 below is
argued from operator experience and from the marketplace numbers, and is not dressed up with
a citation it does not have.

---

## Concept 1. Homestead: the house as one pill, not a control panel

**Lane:** home assistant / IoT, **6 listings**. **Category: Hardware** (99 listings, and the
category the number-one plugin sits in), deliberately not Widgets.

**The gap.** All six existing entries are control surfaces. Home Assistant (298 copies, 40
hearts, 1,061 views, a 28 percent copy-to-view rate that is the highest engagement in any
lane examined here) "views and controls devices." OmaHome reads sensors and controls lights.
Homearchy does presence-first rooms. Dyson Air and WiZ Lights are single-vendor remotes. Every
one of them opens a panel of toggles. **Not one of them answers a question without being
asked**, which is the thing a bar is for and the thing Yigitbas and Kar both found users
actually want.

**What it is.** The pill is silent while the house is fine. It speaks only for the small set
of states a person would want interrupting them: a door or window left open when everyone has
left, a leak or smoke sensor triggered, a device battery below threshold, an entity that has
gone unavailable, a climate setpoint that has been overridden for hours. The panel is a
drainable queue of exactly those, most urgent first, with the one control that resolves each
row. Not a room tree. Not every entity.

**Data source.** The Home Assistant REST API on the local network, long-lived access token.
`GET /api/states` polled, and the token is the only setting.

**Security posture.** This is the plugin in the set that most needs the SSRF discipline in
`002-LS-BLOK`, because the user supplies the host and that host is *by design* a private
address. So the allowlist inverts: the base URL must resolve to RFC1918, link-local or
loopback and nothing else, resolved once and pinned to the request, redirects refused
outright. The token never leaves the process and never reaches an argv that another user can
read from `/proc`. Every response body parses in `Model.js`.

**Bar pill.** Silent by default. One quiet dot when a low-severity row is queued, and a
labelled state with a count when a high-severity one is. Mankoff's peripherality heuristic
and Börner's escalation finding, applied literally.

**Why it wins.** Six competitors and the highest conversion rate on the board in that lane,
against a design nobody in it has attempted. The risk is honest: it requires the user to own a
Home Assistant install, which caps the addressable audience below anything in the top eight.

## Concept 2. Provenance: whether this machine can actually be restored

**Lane:** backup / snapshot, **7 listings**. **Category: System** (181 listings, and where
Notification Center and Vitals live).

**The gap.** Snapshots (28 copies) asks whether snapper can roll this machine back. Restic (0
copies) monitors restic jobs. OmaVault (34 copies) backs up Omarchy customizations. All three
report **that the backup ran**. None reports **that the backup restores**, and those are not
the same claim. A completed job with an unreadable repository is the failure mode that
matters, and it is invisible to every plugin in the lane.

**What it is.** One pill answering one question: *how long ago was it proven that this machine
could be brought back.* It reads whichever engines are present, restic, borg, snapper,
timeshift, rsnapshot, and reports two independent facts per engine: last successful **run**,
and last successful **integrity check**. A repository that has run nightly for 90 days and has
never passed a check reads as **unproven**, not green. The panel offers the check as a single
action, with the age of the last one.

**Data source.** Local only. Engine CLIs in check mode, `restic check`, `borg check`, the
snapper and timeshift listings, plus their systemd timer states. No network, no key, no host
to validate.

**Security posture.** The one deliberate risk is running check subcommands on a user
repository, which is expensive and can be long. It is manual, never automatic, never on a
timer this plugin owns, and it is always a fixed argv with no interpolated user string, per
the `c34` exec-injection gate.

**Bar pill.** A single age, "restorable 3d ago". Amber past the user's threshold. Red on
`unproven`, which is the state the whole plugin exists to surface.

**Why it wins.** It is the `/omarchy-ship` thesis applied to a user's data: *a component
reporting a conclusion whose scope it never established.* A backup job's exit code establishes
that a job exited, and every plugin in this lane presents it as though it established
restorability. That framing is the differentiator, it is defensible in public, and it is
argued from twenty years of operations rather than from a paper.

**The honest risk.** Modest lane demand (28 and 34 copies are the ceiling observed), and the
`check` operation is slow enough that some users will never run it, which is precisely the
behaviour the plugin is diagnosing.

## Concept 3. Loose Ends: the work you left uncommitted

**Lane:** git / repo status, **3 listings**. The thinnest lane found anywhere in the catalog,
in the one domain where every user of this distribution qualifies.

**The gap.** Three listings, and Omarchy is a developer's distribution. Docket, already
shipped in this org, answers "what is waiting on me on GitHub." This answers the strictly
larger and entirely local question: **what did I leave unfinished on this machine.**

**What it is.** Walks a configured set of roots once a minute and reports, across every git
repository found: uncommitted changes, commits ahead of the upstream, stashes older than a
threshold, and detached heads and half-finished rebases. The panel is a queue sorted by how
long each has been that way, because a repository dirty for an hour is work in progress and
one dirty for eleven days is a loose end. Clicking a row opens that repository.

**Data source.** The local filesystem and `git`. No network, no API, no key, no host to
validate, and therefore no SSRF surface at all, which after the Listening Post review is not
a small thing.

**Security posture.** The strongest of the three by construction. Roots are user-supplied
paths, so each is canonicalised and confined before use, symlinks are not followed out of a
declared root, `git` is invoked with `--no-optional-locks` so it never mutates a repository it
is only reading, and every path rendered passes `Model.clean()`.

**Bar pill.** Silent at zero. A count when there is anything, escalating on the age of the
oldest item rather than the number of items, so eleven repositories touched today stay quieter
than one abandoned for two weeks.

**Why it wins.** This is Altmann and Trafton's finding built as a widget. Their result is that
an environmental cue present at resumption reduces the cost of resuming an interrupted task,
and unfinished work in a repository you have forgotten about is the most expensive
interruption a developer has, because nothing anywhere reminds them of it. It has the largest
addressable audience of the three, the thinnest competition, zero external dependencies, and
zero attack surface.

---

## Recommendation

**Build Loose Ends first.** Thinnest lane at three listings, widest audience within this
distribution's actual user base, no key, no network, no host validation, and it is the
concept the literature supports most directly rather than most decoratively. It also ships
fastest, which matters because the amplification window is the competition result week and
not a quarter from now.

**Homestead second**, on the strength of the 28 percent copy rate in its lane, gated on
whether the SSRF discipline in `002-LS-BLOK` lands first. It is the same class of problem
inverted, and shipping it before that is resolved would be repeating a mistake with the
review process already on record.

**Provenance third.** The best story of the three and the smallest measured demand. It is the
one to build when the goal is the argument rather than the counter.

**And the thing none of the three fixes:** the top of this board is Hardware, System and
Appearance, and this org's presence in Appearance is zero. Concepts 1 and 2 move into
Hardware and System deliberately. Appearance is 94 listings holding four of the top five
plugins, and nothing in this document addresses it.
