# Showcase campaign baseline

**Taken:** marketplace snapshot `2026-08-25T18:12:41.735Z`, across 1366 listed plugins.
**Campaign:** `omarchy-showcase-2026-08`, nine packets to Ezekiel on 2026-08-25.

## Why a baseline instead of UTM tags

The marketplace links in the packets carry no UTM parameters, on purpose. The
analytics for omarchyplugins.com belong to the marketplace, so a `utm_source` we
attach is a parameter nobody on this side can read back. It would be the appearance
of measurement rather than measurement.

Two signals are genuinely readable, and both are captured below.

1. **The marketplace's own counters.** Views, copies and hearts per plugin, from the
   public stats endpoint. Copies is the closest thing the marketplace exposes to an
   install, so copies is the conversion metric.
2. **GitHub traffic on repos we own.** GitHub reports referrer hostnames natively, so
   x.com and linkedin.com arrive already separated with no tagging needed. That is
   also why the GitHub links in the packets are untagged.

GitHub traffic is a rolling 14 day window and cannot be backfilled, which is why this
had to be taken on the day the packets went out.

## Baseline

| Plugin | Views | Copies | Hearts | GitHub views (14d) | GitHub uniques |
| --- | --: | --: | --: | --: | --: |
| **Bazaar** | 199 | 20 | 0 | 8 | 6 |
| **Pit Wall** | 113 | 19 | 3 | 15 | 7 |
| **Wait State** | 100 | 9 | 0 | 2 | 2 |
| **MLB Booth** | 92 | 2 | 1 | 16 | 5 |
| **X Files** | 90 | 1 | 1 | 5 | 2 |
| **Docket** | 89 | 3 | 1 | 1 | 1 |
| **Crew Chief** | 66 | 8 | 1 | 4 | 2 |
| **Listening Post** | not listed | not listed | not listed | 5 | 2 |
| **Widget Template** | n/a | n/a | n/a | 1 | 1 |

## How to read it afterwards

```bash
python3 scripts/campaign-baseline.py --compare 000-docs/003-RP-BASE-showcase-campaign-baseline.md
gh api repos/jeremylongshore/omarchy-bazaar-entry/traffic/popular/referrers
```

The second command is the one that answers which voice moved anything, because it
splits by referrer hostname. Run it inside 14 days of the posts or the window will
have rolled past them.

## The two questions worth answering

1. **Do hearts move at all?** Bazaar and Wait State are at zero on 199 and 100 views.
   Hearts are the social proof the listing page renders, and nothing in the product
   asks for one. If a campaign cannot move that number, the fix is on the listing
   page, not in the posting.
2. **Does X or LinkedIn convert better here?** The audience is Arch and Hyprland
   users, which argues for X, but the LinkedIn copy carries the engineering argument
   and this set's differentiator is engineering. The referrer split settles it, and
   it settles it for every campaign after this one.

## Packets sent

Nine packets to `ezekiel@intentsolutions.io`, CC `jeremy@intentsolutions.io`, on
2026-08-25, in this order. Individual plugins first, the template, then the portfolio
page last, because the portfolio packet reads as a summary and a summary lands better
once a few of the parts have gone out.

| # | Packet | Message id |
| --: | --- | --- |
| 1 | `pit-wall` | `<2d670a08-4e0a-61c7-28a1-c9256746d5e9@intentsolutions.io>` |
| 2 | `bazaar` | `<c1358517-5266-9080-6190-ed24f1ac15fe@intentsolutions.io>` |
| 3 | `crew-chief` | `<d12f7285-95fb-e79e-5896-b41c9ba13caa@intentsolutions.io>` |
| 4 | `wait-state` | `<905aa8c3-ebd6-bd78-f85a-07653f6b12ad@intentsolutions.io>` |
| 5 | `docket` | `<b25bc072-222d-2211-6a9d-fff836755b1a@intentsolutions.io>` |
| 6 | `mlb-booth` | `<8815516e-0785-6132-2eb5-45ba7d6e5502@intentsolutions.io>` |
| 7 | `x-files` | `<1067fe56-2a8b-74f0-a708-9e4fd0ec57f7@intentsolutions.io>` |
| 8 | `widget-template` | `<4149514e-2394-b8a3-8209-113016190693@intentsolutions.io>` |
| 9 | `umbrella` | `<5712883c-2975-bc02-9abb-5f8a8f5d33cc@intentsolutions.io>` |

**Listening Post got no packet.** Its marketplace submission
([#1229](https://github.com/HANCORE-linux/omarchy-plugin-marketplace/issues/1229)) is open
with `needs-fixes` on an unresolved request forgery finding, and there is no listing page
for a packet to link. Pushing it publicly while a marketplace reviewer has a documented,
open security finding against it costs more than one fewer post. The packet builder still
covers the case: given a plugin absent from the catalog it emits a HOLD banner rather than
a link. See `002-LS-BLOK` for what closes it.
