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
const bluegold = await readFile(new URL("../site/bluegoldblue/index.html", import.meta.url), "utf8");
const bluegoldInterest = await readFile(new URL("../site/assets/bluegold-interest.js", import.meta.url), "utf8");
const legalDocuments = new Map(await Promise.all([
  ["privacy", "Privacy Policy"],
  ["app-privacy", "The Beacon Wakes App Privacy Policy"],
  ["acceptable-use", "Acceptable Use Policy"],
  ["terms", "Terms and Conditions"],
].map(async ([route, heading]) => [
  route,
  { heading, html: await readFile(new URL(`../site/${route}/index.html`, import.meta.url), "utf8") },
])));
const perception = await readFile(new URL("../site/perception/index.html", import.meta.url), "utf8");

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
    assert.deepEqual(generated.project, source.project || null);
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
    assert.match(plugin.github.defaultBranchUpdatedAt, /^\d{4}-\d{2}-\d{2}T/);
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
  assert.match(html, /class="bluegold-feature"/);
  assert.match(html, /href="bluegoldblue\/"/);
  assert.match(html, /id="project-count"/);
  assert.doesNotMatch(html, /id="roadmap-count"/);
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
  assert.equal(data.marketplaceStatsUrl, "https://api.omarchyplugins.com/v1/stats");
});

test("repository-owned legal routes match product and child-safety contracts", () => {
  for (const [route, legal] of legalDocuments) {
    assert.ok(legal.html.includes(`<h1 id="${route === "terms" ? "terms-title" : "policy-title"}">${legal.heading}</h1>`));
    assert.match(legal.html, /Intent Solutions LLC/);
    assert.match(legal.html, /support@intentsolutions\.io/);
    assert.match(legal.html, new RegExp(`https://oma\\.intentsolutions\\.io/${route}/`));
    assert.doesNotMatch(legal.html, /<script\b|<iframe\b|getterms|No You Pick|diagnosticpro\.reports@gmail\.com/i);
    assert.doesNotMatch(legal.html, /not (?:aimed|intended|designed) (?:at|for) children|children under (?:the age of )?13 may not use|must be (?:at least )?18 (?:years old )?to use/i);
  }
  assert.match(legalDocuments.get("privacy").html, /designed for children to play with parent or guardian involvement/i);
  assert.match(legalDocuments.get("privacy").html, /BLUE GOLD BLUE interest form asks for your name, email address/i);
  assert.match(legalDocuments.get("terms").html, /BLUE GOLD BLUE is currently a research and development project/i);
  assert.match(legalDocuments.get("app-privacy").html, /does not ask the child playing for a name/i);
  assert.match(legalDocuments.get("app-privacy").html, /does not send typing performance or gameplay progress/i);
  assert.match(legalDocuments.get("terms").html, /a parent or legal guardian must review and accept these Terms on the child's behalf/i);
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
    if (plugin.project) {
      assert.ok(html.includes(`href="${plugin.project.url}"`));
      assert.ok(detail.includes(`href="${plugin.project.url}"`));
    }
    assert.doesNotMatch(detail, /href=""/);
    assert.match(detail, /href="\.\.\/\.\.\/privacy\/"/);
    assert.match(detail, /href="\.\.\/\.\.\/terms\/"/);
  }
});

test("Perception has a permanent OMA product route", async () => {
  assert.match(perception, /<title>Perception: Let the signal come to you<\/title>/);
  assert.match(perception, /https:\/\/oma\.intentsolutions\.io\/perception\//);
  assert.match(perception, /src="\/perception\/assets\/index-[^"]+\.js"/);
  assert.match(perception, /href="\/perception\/assets\/index-[^"]+\.css"/);
  assert.doesNotMatch(perception, /on the way/i);
  const script = perception.match(/src="\/perception\/(assets\/index-[^"]+\.js)"/)?.[1];
  assert.ok(script);
  const bundle = await readFile(new URL(`../site/perception/${script}`, import.meta.url), "utf8");
  assert.match(bundle, /Stop checking feeds/);
  assert.match(bundle, /Listening Post/);
  assert.match(bundle, /support@intentsolutions\.io/);
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

test("BLUE GOLD BLUE is an honest research page with bounded interest collection", () => {
  assert.match(bluegold, /<h1 id="bluegold-title">Windows to Omarchy\./);
  assert.match(bluegold, /BLUE is your personal cloud/);
  assert.match(bluegold, /a physical storage device you keep/);
  assert.match(bluegold, /GOLD is the key/);
  assert.match(bluegold, /256 GB/);
  assert.match(bluegold, /512 GB/);
  assert.match(bluegold, /1 TB/);
  assert.match(bluegold, /2 TB/);
  assert.match(bluegold, /Keep BLUE as your backup/);
  assert.match(bluegold, /WELCOME local assistant/);
  assert.match(bluegold, /id="faq"/);
  assert.equal((bluegold.match(/<details>/g) || []).length, 43);
  assert.match(bluegold, /id="faq-start"/);
  assert.match(bluegold, /id="faq-computer"/);
  assert.match(bluegold, /id="faq-data"/);
  assert.match(bluegold, /id="faq-safety"/);
  assert.match(bluegold, /id="faq-after"/);
  assert.match(bluegold, /What exactly is BLUE GOLD BLUE\?/);
  assert.match(bluegold, /What would arrive at my door\?/);
  assert.match(bluegold, /Do I send you my computer\?/);
  assert.match(bluegold, /Will GOLD remove Windows from my computer\?/);
  assert.match(bluegold, /can replace Windows and erase the existing system disk/);
  assert.match(bluegold, /What about OneDrive, Dropbox, or files that are only online\?/);
  assert.match(bluegold, /What about Microsoft Office, Adobe apps, QuickBooks, games/);
  assert.match(bluegold, /How will GOLD avoid erasing the wrong drive\?/);
  assert.match(bluegold, /Is BLUE an internet cloud, and are my files uploaded\?/);
  assert.match(bluegold, /Can BLUE put Windows back if I change my mind\?/);
  assert.match(bluegold, /Is Omarchy involved in this project\?/);
  assert.match(bluegold, /Can BLUE rescue a computer that is already failing\?/);
  assert.match(bluegold, /What happens if BLUE says REVIEW or STOP\?/);
  assert.match(bluegold, /Do I need to know Linux, use a terminal, or understand computer drives\?/);
  assert.match(bluegold, /What happens when I register interest\?/);
  assert.match(bluegold, /not an internet cloud service/i);
  assert.match(bluegold, /BLUE BEFORE GOLD\. ALWAYS\./);
  assert.match(bluegold, /Research and development/);
  assert.match(bluegold, /Not for sale yet/);
  assert.match(bluegold, /not an Omarchy endorsement/i);
  assert.match(bluegold, /name="name" type="text"/);
  assert.match(bluegold, /name="email" type="email"/);
  assert.match(bluegold, /name="offer" required/);
  assert.match(bluegold, /name="journey"/);
  assert.match(bluegold, /name="currentOs"/);
  assert.match(bluegold, /name="blueStorage"/);
  assert.match(bluegold, /name="capacity"/);
  assert.match(bluegold, /name="timing"/);
  assert.match(bluegold, /name="consent" type="checkbox" required/);
  assert.match(bluegold, /href="\.\.\/privacy\/"/);
  assert.match(bluegold, /href="\.\.\/acceptable-use\/"/);
  assert.match(bluegold, /href="\.\.\/terms\/"/);
  assert.match(bluegold, /id="bluegold-confirm-button"/);
  assert.match(bluegold, /Optional preferences/);
  assert.match(bluegold, /Need a new link\? Submit the form again\./);
  assert.match(bluegoldInterest, /bluegold-interest-v1/);
  assert.match(bluegoldInterest, /https:\/\/intentsolutions\.io\/api\/forms\/bluegold-interest/);
  assert.match(bluegoldInterest, /https:\/\/intentsolutions\.io\/api\/forms\/bluegold-confirm/);
  assert.match(bluegoldInterest, /window\.location\.hash/);
  assert.match(bluegoldInterest, /\^\[A-Za-z0-9_-\]\{22\}\$/);
  assert.match(bluegoldInterest, /confirmationParams\.has\("c"\)/);
  assert.match(bluegoldInterest, /confirmationParams\.get\("c"\)/);
  assert.match(bluegoldInterest, /\{ code: confirmationCode \}/);
  assert.match(bluegoldInterest, /\{ token: legacyConfirmationToken \}/);
  assert.match(bluegoldInterest, /Try confirmation again/);
  assert.doesNotMatch(bluegold, /buy now|reserve your|guaranteed|official Omarchy|works on every|available now/i);
});
