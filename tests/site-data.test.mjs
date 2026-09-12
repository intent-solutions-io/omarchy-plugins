import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const config = JSON.parse(await readFile(new URL("../plugins.json", import.meta.url)));
const data = JSON.parse(await readFile(new URL("../site/data/plugins.json", import.meta.url)));
const html = await readFile(new URL("../site/index.html", import.meta.url), "utf8");
const css = await readFile(new URL("../site/assets/styles.css", import.meta.url), "utf8");
const readme = await readFile(new URL("../README.md", import.meta.url), "utf8");
const cname = (await readFile(new URL("../site/CNAME", import.meta.url), "utf8")).trim();
const beacon = await readFile(new URL("../site/the-beacon-wakes/index.html", import.meta.url), "utf8");
const beaconSignup = await readFile(new URL("../site/assets/beacon-signup.js", import.meta.url), "utf8");
const beaconDemo = await readFile(new URL("../site/the-beacon-wakes/play/index.html", import.meta.url), "utf8");
const beaconRedirect = await readFile(new URL("../site/omaquest/index.html", import.meta.url), "utf8");
const legalDocuments = new Map(await Promise.all([
  ["privacy", "privacy"],
  ["app-privacy", "app-privacy"],
  ["acceptable-use", "acceptable-use"],
  ["terms", "terms-of-service"],
].map(async ([route, document]) => [
  route,
  { document, html: await readFile(new URL(`../site/${route}/index.html`, import.meta.url), "utf8") },
])));

test("generated site inventory matches the canonical config", () => {
  assert.equal(data.plugins.length, config.plugins.length);
  assert.deepEqual(new Set(data.families), new Set(config.families));
  assert.deepEqual(
    new Set(data.plugins.map((plugin) => plugin.id)),
    new Set(config.plugins.map((plugin) => plugin.id)),
  );

  const generatedById = new Map(data.plugins.map((plugin) => [plugin.id, plugin]));
  for (const source of config.plugins) {
    const generated = generatedById.get(source.id);
    assert.ok(generated, `missing generated entry for ${source.id}`);
    assert.equal(generated.name, source.name);
    assert.equal(generated.slug, source.repo.replace(/^omarchy-/, "").replace(/-entry$/, ""));
    assert.equal(generated.repo, source.repo);
    assert.equal(generated.repoUrl, `https://github.com/${config.github.owner}/${source.repo}`);
    assert.equal(generated.pitch, source.pitch);
    assert.equal(generated.family, source.family);
    assert.ok(config.families.includes(generated.family));
  }
});

test("public lifecycle is reconciled with the official marketplace", () => {
  for (const plugin of data.plugins) {
    assert.match(plugin.repoUrl, /^https:\/\/github\.com\/jeremylongshore\/omarchy-[a-z0-9-]+-entry$/);
    if (plugin.lifecycle === "listed") {
      assert.match(plugin.marketplaceUrl, /^https:\/\/plugins\.omarchy\.org\/plugin\.html\?id=/);
      assert.match(plugin.installCommand, /^omarchy plugin add https:\/\/github\.com\/jeremylongshore\/.+\.git --enable$/);
      assert.equal(plugin.submissionUrl, null);
    } else {
      assert.equal(plugin.marketplaceUrl, null);
      assert.equal(plugin.installCommand, null);
    }
  }
  const omaTrail = data.plugins.find((plugin) => plugin.name === "omaTrail");
  assert.ok(omaTrail);
  assert.equal(omaTrail.marketplaceUrl, "https://plugins.omarchy.org/plugin.html?id=io.github.jeremylongshore.omatrail");
});

test("repository health includes bounded stars, freshness, preview provenance, and manifest checks", () => {
  for (const plugin of data.plugins) {
    assert.ok(Number.isSafeInteger(plugin.github.stars) && plugin.github.stars >= 0);
    assert.ok(Number.isSafeInteger(plugin.github.openIssues) && plugin.github.openIssues >= 0);
    assert.match(plugin.github.pushedAt, /^\d{4}-\d{2}-\d{2}T/);
    assert.match(plugin.github.defaultBranch, /^[A-Za-z0-9._/-]+$/);
    assert.ok(["aligned", "drift", "missing"].includes(plugin.manifest.status));
    assert.ok(Array.isArray(plugin.manifest.issues));
    if (plugin.preview.status === "verified") {
      assert.match(plugin.preview.url, /^https:\/\/raw\.githubusercontent\.com\/jeremylongshore\//);
      assert.match(plugin.preview.sha, /^[a-f0-9]{40}$/);
      assert.equal(plugin.previewUrl, plugin.preview.url);
    } else {
      assert.equal(plugin.preview.status, "missing");
      assert.equal(plugin.previewUrl, null);
    }
  }
});

test("generated README metrics agree with the generated site snapshot", () => {
  const listed = data.plugins.filter((plugin) => plugin.lifecycle === "listed");
  const totals = listed.reduce(
    (sum, plugin) => ({
      views: sum.views + (plugin.metrics?.views || 0),
      copies: sum.copies + (plugin.metrics?.copies || 0),
      hearts: sum.hearts + (plugin.metrics?.hearts || 0),
      stars: sum.stars + plugin.github.stars,
    }),
    { views: 0, copies: 0, hearts: 0, stars: 0 },
  );
  assert.ok(readme.includes(`Marketplace data generated at \`${data.generatedAt}\``));
  assert.ok(readme.includes(`**${listed.length} of ${data.plugins.length} listed** on the marketplace, ${totals.views} views, ${totals.copies} copies, ${totals.hearts} hearts, and ${totals.stars} GitHub stars.`));

  for (const plugin of data.plugins) {
    const authority = plugin.marketplaceUrl
      ? `[${plugin.category}](${plugin.marketplaceUrl})`
      : plugin.submissionUrl
        ? `[under review](${plugin.submissionUrl})`
        : plugin.lifecycle.replaceAll("-", " ");
    const metrics = plugin.metrics
      ? `${plugin.metrics.views} | ${plugin.metrics.copies} | ${plugin.metrics.hearts}`
      : "n/a | n/a | n/a";
    const row = `| **${plugin.name}** | ${plugin.family} | ${plugin.pitch} | [repo](${plugin.repoUrl}) | ${authority} | ${plugin.github.stars} | ${metrics} |`;
    assert.ok(readme.includes(row), `README row drift for ${plugin.name}`);
    if (plugin.installCommand) assert.ok(readme.includes(`# ${plugin.name}\n${plugin.installCommand}`));
  }
});

test("site shell preserves discovery, fallback, accessibility, and domain contracts", () => {
  assert.match(html, /id="catalog"/);
  assert.match(html, /id="ledger"/);
  assert.match(html, /id="family-filters"/);
  assert.match(html, /id="featured-project"/);
  assert.match(html, /href="the-beacon-wakes\/play\/"/);
  assert.match(html, /<h2 id="beacon-feature-title">The Beacon Wakes<\/h2>/);
  assert.match(html, /STATIC_CATALOG:START/);
  assert.match(html, /Complete plugin index/);
  for (const plugin of data.plugins) {
    assert.match(html, new RegExp(`plugins/${plugin.slug}/`));
  }
  assert.match(html, /class="skip-link"/);
  assert.match(html, /Intent Solutions Omarchy Plugins/);
  assert.doesNotMatch(html, /O\/|OMA PLUGIN WORKS|Omarchy Plugin Works|wordmark-mark/);
  assert.match(css, /prefers-reduced-motion/);
  assert.match(css, /caret-color: var\(--orange-deep\)/);
  assert.equal(cname, "oma.intentsolutions.io");
});

test("GetTerms legal routes use the supplied account and document contracts", () => {
  for (const [route, legal] of legalDocuments) {
    assert.match(legal.html, /data-getterms="wH2cn"/);
    assert.ok(legal.html.includes(`data-getterms-document="${legal.document}"`));
    assert.match(legal.html, /data-getterms-lang="en-us"/);
    assert.match(legal.html, /data-getterms-mode="direct"/);
    assert.match(legal.html, /data-getterms-env="https:\/\/gettermscdn\.com"/);
    assert.match(legal.html, /https:\/\/gettermscdn\.com\/dist\/js\/embed\.js/);
    assert.ok(legal.html.includes(`https://gettermscdn.com/view/wH2cn/${legal.document}/en-us`));
    assert.match(legal.html, new RegExp(`https://oma\\.intentsolutions\\.io/${route}/`));
    assert.doesNotMatch(legal.html, /embed-js\/goaal/);
  }
  for (const route of legalDocuments.keys()) {
    assert.match(html, new RegExp(`href="${route}/"`));
  }
  assert.match(beacon, /href="\.\.\/privacy\/"/);
  assert.match(beacon, /href="\.\.\/app-privacy\/"/);
});

test("every plugin has a generated permanent detail page with source receipts", async () => {
  for (const plugin of data.plugins) {
    const detail = await readFile(new URL(`../site/plugins/${plugin.slug}/index.html`, import.meta.url), "utf8");
    assert.ok(detail.includes(`<h1>${plugin.name}</h1>`));
    assert.ok(detail.includes(plugin.repoUrl));
    assert.ok(detail.includes(plugin.pitch.replaceAll("&", "&amp;")));
    assert.ok(detail.includes(`data-manifest-status="${plugin.manifest.status}"`));
    assert.ok(detail.includes(plugin.family));
    if (plugin.marketplaceUrl) assert.ok(detail.includes(plugin.marketplaceUrl));
    if (plugin.submissionUrl) assert.ok(detail.includes(plugin.submissionUrl));
    if (!plugin.marketplaceUrl && !plugin.submissionUrl) assert.ok(detail.includes("No official listing link is published"));
    if (plugin.installCommand) assert.ok(detail.includes(plugin.installCommand));
    if (plugin.preview.status === "verified") assert.ok(detail.includes(plugin.preview.sha.slice(0, 12)));
    else assert.ok(detail.includes("Preview unavailable"));
    assert.doesNotMatch(detail, /href=""/);
    assert.match(detail, /href="\.\.\/\.\.\/privacy\/"/);
    assert.match(detail, /href="\.\.\/\.\.\/terms\/"/);
  }
});

test("public product branding keeps the capital T in omaTrail", async () => {
  const omaTrailDetail = await readFile(new URL("../site/plugins/omatrail/index.html", import.meta.url), "utf8");
  const publicText = `${html}\n${JSON.stringify(data)}\n${omaTrailDetail}`;
  assert.ok(publicText.includes("omaTrail"));
  assert.ok(!publicText.includes("Omatrail"));
  assert.ok(!publicText.includes("OMATRAIL"));
});

test("The Beacon Wakes demo and parent handoff are honest and ungated", () => {
  assert.match(beacon, /<h1 id="beacon-title">The Beacon<br>Wakes<\/h1>/);
  assert.match(beacon, /by Intent Solutions/i);
  assert.match(beacon, /id="parent-guide"/);
  assert.match(beacon, /No email required/);
  assert.match(beacon, /No child account/);
  assert.match(beacon, /No checkout inside play/);
  assert.match(beacon, /browser demo is live/i);
  assert.match(beacon, /href="play\/"/);
  assert.match(beaconDemo, /<title>The Beacon Wakes/);
  assert.match(beaconDemo, /assets\/index-[^"']+\.js/);
  assert.match(beaconDemo, /assets\/index-[^"']+\.css/);
  assert.match(beacon, /id="beacon-signup"/);
  assert.match(beacon, /name="firstName"/);
  assert.match(beacon, /name="lastName"/);
  assert.match(beacon, /name="email" type="email"/);
  assert.match(beacon, /name="consent" type="checkbox"/);
  assert.match(beacon, /Adults only/);
  assert.match(beacon, /Parent or guardian first name/);
  assert.match(beacon, /Parent or guardian last name/);
  assert.match(beacon, /class="beacon-release-link"/);
  assert.match(beaconSignup, /beacon-release-updates-v1/);
  assert.match(beaconSignup, /https:\/\/intentsolutions\.io\/api\/forms\/beacon-signup/);
  assert.match(beaconSignup, /https:\/\/intentsolutions\.io\/api\/forms\/beacon-confirm/);
  assert.match(beaconSignup, /window\.location\.hash/);
  assert.match(beacon, /id="beacon-confirm-button"/);
  assert.doesNotMatch(beacon, /name="(?:child|learner)|href="[^"]*checkout|buy now|download now/i);
  assert.match(beacon, /https:\/\/oma\.intentsolutions\.io\/the-beacon-wakes\//);
  assert.doesNotMatch(beacon, /omaQuest|OmaQuest|OMAQUEST/);
  assert.match(beaconRedirect, /url=\.\.\/the-beacon-wakes\//);
});
