# Listening Post is not in the marketplace catalog, and why

**Status:** blocked on an open security finding, not on a lost submission.
**Date:** 2026-08-25
**Owner:** Jeremy Longshore
**Evidence:** [HANCORE-linux/omarchy-plugin-marketplace#1229](https://github.com/HANCORE-linux/omarchy-plugin-marketplace/issues/1229)

## The observation that started this

Seven of the eight entries appear in `https://omarchyplugins.com/catalog.json` with
`verificationStatus: verified`. Listening Post appears nowhere in it, and therefore has no
row in the stats endpoint either. That is not a metrics rounding error. It is the whole
listing.

The reflex reading is "the submission never landed." It landed. Reproduce the check:

```bash
gh search issues --author jeremylongshore "listening post" --json repository,number,state
```

## What actually happened

Submission issue **#1229**, opened 2026-08-21, is **still open** and carries the labels
`submission`, `validated`, `needs-fixes`.

Automated validation passed on the first pass: public and reachable, one valid manifest,
README and license present, Quattro compatibility green at `3759cfe`, automated security
baseline passed. So the listing pipeline is not the obstacle.

The obstacle is a human review thread on the custom-feed feature, in three rounds:

| Round | Reviewer | Finding | Response |
| --- | --- | --- | --- |
| 1 | `ryanrhughes` | URL userinfo was read as part of the hostname, so `https://user@127.0.0.1/feed` passed the private-host check and curl dialled loopback | Fixed in `e8d00af`. The check moved out of `Service.qml` into `Model.js` so the offline suite covers it, with the reported payload pinned as a regression |
| 2 | `HANCORE-linux` | Alternate IPv4 spellings still resolved to loopback: `https://127.1/feed`, `https://0177.0.0.1/feed` | Fixed. `inet_aton` accepts one to four parts in decimal, octal and hex, and the check now rejects every form it parses as an address |
| 3 | `HANCORE-linux` (2026-08-24, still open) | **The class, not the spelling.** The policy still validates only the hostname *string*. An ordinary attacker-controlled hostname can resolve to `127.0.0.1`, RFC1918 or link-local, and DNS rebinding can change the address after any separate lookup | **Unresolved** |

Round three is correct, and it is not fixable by another regex. Local HEAD is
`d26746cbbfdcd4282ef1a3faa9b303f14b3f3a3e`, exactly the commit that comment names, and the
83-test offline suite is green against it. **A green suite here means the spellings it
knows about are rejected. It says nothing about the resolution step, because the resolution
step is curl's, and the test suite never runs curl.** That is the same defect class the
`/omarchy-ship` lane exists to refuse: a component reporting a conclusion whose scope it
never established.

## What closes it

The reviewer named the acceptable outcomes. Either:

1. **Resolve and pin.** Resolve the host first, reject every non-public result, and bind the
   validated address to the request so the name is never resolved twice. In curl terms that
   is an explicit `--resolve host:port:addr` pin, `--proto =https`, and `--max-redirs 0`,
   with each redirect hop re-validated in `Model.js` rather than followed by curl. This is
   the only option that keeps arbitrary custom feeds.
2. **Remove arbitrary custom-feed hosts.** Ship the 29 curated sources and drop user-supplied
   feed URLs entirely. The SSRF surface disappears with the feature, and 29 curated sources
   is the plugin's actual pitch anyway.

Option 2 is the smaller, more defensible change, and the custom-feed field is not what
anyone installs this for. Option 1 is the right answer only if custom feeds turn out to be
the thing users ask for after the plugin is listed, which is not knowable before it is
listed.

## Consequences for everything else in this repo

- The README metrics table renders Listening Post as `not listed` rather than dropping it.
  A row that vanishes is a row nobody investigates.
- **No public showcase packet ships for Listening Post** until #1229 closes. Promoting an
  entry while the marketplace maintainer has a publicly documented, unresolved SSRF finding
  against it is a worse outcome than one fewer post, and the packet would have no
  marketplace page to link to in any case.
- The gate `c38-omarchy-ssrf-host-allowlist` catches the spelling class across every entry.
  It does not catch the resolution class, in any entry. Whichever fix lands here should be
  reflected back into the template and the gate, because every plugin that ever accepts a
  user-supplied URL inherits this exact hole.
