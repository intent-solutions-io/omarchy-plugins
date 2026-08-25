#!/usr/bin/env python3
"""plane-sync-packets.py: mirror each showcase packet into a Plane issue in CONTENT.

WHY PLANE AND NOT JUST THE EMAIL
  The packet email delivers the words. It cannot tell anyone whether the work got done.
  "Reply with the URLs" depends on someone replying, and a missing reply is indistinguishable
  from a missing post. A Plane issue has a state, so done is a fact rather than a report.

  So the split is: the email is the delivery, Plane is the record. The issue carries the full
  packet body as well, so the work can be done from Plane alone without going back to email.

IDEMPOTENCE
  Each issue is stamped external_source=omarchy-showcase and external_id=<key>. Re-running
  matches on that pair and updates rather than creating a duplicate, so this is safe to run
  again after the packets change or after Ezekiel accepts his invite and becomes assignable.

Usage:
  plane-sync-packets.py                 # create or update all nine
  plane-sync-packets.py --assign-only   # only (re)apply the assignee, once he has accepted
  plane-sync-packets.py --dry-run
"""
from __future__ import annotations
import argparse, html, json, os, re, subprocess, sys, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = os.environ.get("PLANE_API_HOST_URL", "https://projects.intentsolutions.io")
SLUG = os.environ.get("PLANE_WORKSPACE_SLUG", "internal")
CONTENT_PROJECT = "b421236a-7a50-4e4b-b01f-6dd3a4cdfaf9"
TODO_STATE = "982586a3-370d-4899-b3f4-ce74bb4d25e3"
OPERATOR_EMAIL = "ezekiel@intentsolutions.io"
EXT_SOURCE = "omarchy-showcase"

def api_key() -> str:
    k = os.environ.get("PLANE_API_KEY")
    if k:
        return k
    m = re.search(r'"PLANE_API_KEY"\s*:\s*"([^"]+)"', Path("/home/jeremy/.claude.json").read_text())
    if m:
        return m.group(1)
    sys.exit("no PLANE_API_KEY in env or ~/.claude.json")

KEY = api_key()

def call(method: str, path: str, body=None):
    req = urllib.request.Request(
        f"{HOST}/api/v1/workspaces/{SLUG}{path}",
        method=method,
        headers={"X-API-Key": KEY, "Content-Type": "application/json"},
        data=json.dumps(body).encode() if body is not None else None,
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
            return r.status, (json.loads(raw) if raw else None)
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, {"raw": raw.decode(errors="replace")[:400]}

def find_operator():
    """Return Ezekiel's member uuid, or None while his invite is still pending."""
    _, members = call("GET", "/members/")
    rows = members.get("results", members) if isinstance(members, dict) else members
    for m in rows or []:
        if (m.get("email") or "").lower() == OPERATOR_EMAIL:
            return m.get("id")
    return None

def esc(s: str) -> str:
    return html.escape(s).replace("\n", "<br>")

def body_html(t: dict, links: list[tuple[str, str]], install: str | None,
              metrics: dict | None) -> str:
    p = []
    p.append("<p>Posting packet. The copy below is written for you, one version per "
             "platform. Copy, paste, post. Do not rewrite it and do not mix the versions up. "
             "The same packet is in your email with the same content.</p>")
    if metrics:
        p.append(f"<p><b>Where it stands on the marketplace today:</b> "
                 f"{metrics['views']} views, {metrics['copies']} copies, "
                 f"{metrics['hearts']} hearts.</p>")
    p.append("<h3>Destinations</h3><ul>"
             "<li>X / Twitter: yes, single post, not a thread</li>"
             "<li>LinkedIn personal: yes, links in the FIRST COMMENT</li>"
             "<li>LinkedIn company: yes, links in the FIRST COMMENT</li>"
             "<li>X Article, Substack, Medium: no, not this packet</li></ul>")
    p.append(f"<h3>1. X post</h3><blockquote>{esc(t['x_post'])}</blockquote>")
    p.append(f"<h3>2. LinkedIn, Jeremy's personal profile</h3>"
             f"<blockquote>{esc(t['li_personal'])}</blockquote>")
    p.append(f"<h3>3. LinkedIn, Intent Solutions company page</h3>"
             f"<blockquote>{esc(t['li_company'])}</blockquote>")
    p.append("<h3>Links (first comment on LinkedIn, reply on X)</h3><ul>")
    for name, url in links:
        p.append(f'<li>{html.escape(name)}: <a href="{html.escape(url)}">{html.escape(url)}</a></li>')
    if install:
        p.append(f"<li>Install command: <code>{html.escape(install)}</code></li>")
    p.append("</ul>")
    p.append(f"<h3>Note from Jeremy</h3><p>{esc(t['posting_note'])}</p>")
    p.append("<h3>How to close this</h3><p>Move it to <b>In Progress</b> when you start and "
             "<b>Done</b> when all three are posted, and leave a comment with the three "
             "resulting URLs. The comment is what makes it auditable later. Do not reply by "
             "email, this issue is the record.</p>")
    return "".join(p)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--assign-only", action="store_true")
    a = ap.parse_args()

    packets = json.loads((ROOT / "scripts" / "showcase-packets.json").read_text())
    cfg = json.loads((ROOT / "plugins.json").read_text())

    def fetch(url):
        req = urllib.request.Request(url, headers={
            "User-Agent": "omarchy-plugins-plane-sync", "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())

    stats = fetch(cfg["marketplace"]["stats"])["plugins"]
    cat = fetch(cfg["marketplace"]["catalog"])
    by_id = {p["id"]: p for p in cat["plugins"]}

    operator = find_operator()
    if operator:
        print(f"assignee: {OPERATOR_EMAIL} -> {operator}")
    else:
        print(f"assignee: {OPERATOR_EMAIL} has NOT accepted the workspace invite yet. "
              f"Issues will be created unassigned. Re-run with --assign-only after he accepts.")

    _, existing = call("GET", f"/projects/{CONTENT_PROJECT}/issues/?per_page=100")
    rows = existing.get("results", []) if isinstance(existing, dict) else []
    seen = {r.get("external_id"): r for r in rows
            if r.get("external_source") == EXT_SOURCE and r.get("external_id")}

    for t in packets["targets"]:
        key = t["key"]
        pid = t.get("id")
        if pid and pid not in by_id:
            print(f"SKIP {key}: not in the marketplace catalog, packet is on hold")
            continue

        gh_owner = "intent-solutions-io" if t.get("org_repo") else "jeremylongshore"
        gh_repo = t.get("org_repo") or t["repo"]
        links = [("GitHub", f"https://github.com/{gh_owner}/{gh_repo}")]
        install, metrics = None, None
        if pid:
            links.append(("Marketplace listing", cfg["marketplace"]["pluginPage"] + pid))
            install = by_id[pid].get("installCommand")
            metrics = stats.get(pid, {"views": 0, "copies": 0, "hearts": 0})
        else:
            links.append(("Marketplace", "https://omarchyplugins.com"))

        name = t["subject"].split(": ", 1)[1]
        payload = {
            "name": f"Post the Omarchy showcase packet: {name}",
            "description_html": body_html(t, links, install, metrics),
            "state": TODO_STATE,
            "priority": "medium",
            "external_source": EXT_SOURCE,
            "external_id": key,
        }
        # Plane assigns the API key's owner by default, which would drop nine posting tasks
        # into Jeremy's My Issues. Set the field explicitly in both directions: Ezekiel when
        # he exists, and empty while his invite is still pending.
        payload["assignees"] = [operator] if operator else []

        cur = seen.get(key)
        if a.assign_only:
            if not cur or not operator:
                print(f"skip {key}: nothing to assign")
                continue
            if a.dry_run:
                print(f"DRY assign {key}")
                continue
            st, r = call("PATCH", f"/projects/{CONTENT_PROJECT}/issues/{cur['id']}/",
                         {"assignees": [operator]})
            print(f"{'assigned' if st < 300 else 'FAILED ' + str(st)} {key}")
            continue

        if a.dry_run:
            print(f"DRY {'update' if cur else 'create'} {key}: {payload['name']}")
            continue

        if cur:
            st, r = call("PATCH", f"/projects/{CONTENT_PROJECT}/issues/{cur['id']}/", payload)
            verb = "updated"
        else:
            st, r = call("POST", f"/projects/{CONTENT_PROJECT}/issues/", payload)
            verb = "created"
        if st >= 300:
            print(f"FAILED {key}: HTTP {st} {json.dumps(r)[:200]}")
        else:
            print(f"{verb} CONTENT-{r.get('sequence_id')}  {key}")

if __name__ == "__main__":
    main()
