# Security

## Reporting

Use this repository's **Security** tab and choose **Report a vulnerability**.
Do not open a public issue first. Expect acknowledgement within a few days.

## Scope

This repository publishes a static GitHub Pages site. It has no login, database,
user-submitted content, or client-side secret. Its automation reads public
Omarchy marketplace endpoints and writes generated portfolio data.

Security-sensitive changes must keep credentials out of the repository and
logs, pin third-party GitHub Actions to reviewed commits, validate remote data
before rendering it, and grant each workflow only the permissions it needs.
