# Contributing

This repository owns the public Omarchy plugin portfolio and the static site at
[oma.intentsolutions.io](https://oma.intentsolutions.io/). Plugin runtime code
belongs in the linked entry repositories, not here.

## Before opening a pull request

Run the portfolio checks when changing the site, catalog, generated pages, or
automation:

```bash
bash scripts/check-site.sh
```

Include desktop and mobile screenshots for visible changes. Documentation-only
changes do not need a plugin test suite.

Never hand-edit the generated metrics block in `README.md`,
`site/data/plugins.json`, or generated plugin detail pages. Follow the commands
and ownership rules in `CLAUDE.md`.

## Maintainers wanted

We are looking for dependable Omarchy users who want to review issues, verify
plugin listings, test releases, and keep the portfolio accurate. Start with a
small pull request or open a **Maintainer interest** issue. Tell us which
plugins you use and how you want to help.

## Commits

Use Conventional Commits such as `feat(site):`, `fix(site):`, `docs:`, and
`ci:`.
