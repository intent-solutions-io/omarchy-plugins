import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const config = JSON.parse(await readFile(new URL("../plugins.json", import.meta.url)));
const data = JSON.parse(await readFile(new URL("../site/data/plugins.json", import.meta.url)));
const html = await readFile(new URL("../site/index.html", import.meta.url), "utf8");
const css = await readFile(new URL("../site/assets/styles.css", import.meta.url), "utf8");
const readme = await readFile(new URL("../README.md", import.meta.url), "utf8");
const cname = (await readFile(new URL("../site/CNAME", import.meta.url), "utf8")).trim();

test("generated site inventory matches the canonical config", () => {
  assert.equal(config.plugins.length, 16);
  assert.equal(data.plugins.length, config.plugins.length);
  assert.deepEqual(
    new Set(data.plugins.map((plugin) => plugin.id)),
    new Set(config.plugins.map((plugin) => plugin.id)),
  );
});

test("public lifecycle separates listings from marketplace review", () => {
  const listed = data.plugins.filter((plugin) => plugin.lifecycle === "listed");
  const review = data.plugins.filter((plugin) => plugin.lifecycle === "under-review");
  assert.equal(listed.length, 15);
  assert.equal(review.length, 1);
  assert.equal(review[0].name, "omaTrail");
  assert.equal(review[0].submissionUrl, "https://github.com/omacom/omarchy-plugin-marketplace/issues/5498");
  assert.equal(review[0].marketplaceUrl, null);
});

test("listed entries use official marketplace and public GitHub links", () => {
  for (const plugin of data.plugins) {
    assert.match(plugin.repoUrl, /^https:\/\/github\.com\/jeremylongshore\/omarchy-[a-z0-9-]+-entry$/);
    assert.match(plugin.previewUrl, /^https:\/\/raw\.githubusercontent\.com\/jeremylongshore\//);
    if (plugin.lifecycle === "listed") {
      assert.match(plugin.marketplaceUrl, /^https:\/\/plugins\.omarchy\.org\/plugin\.html\?id=/);
      assert.match(plugin.installCommand, /^omarchy plugin add https:\/\/github\.com\/jeremylongshore\/.+\.git --enable$/);
    }
  }
});

test("generated README metrics agree with the generated site snapshot", () => {
  const listed = data.plugins.filter((plugin) => plugin.lifecycle === "listed");
  const totals = listed.reduce(
    (sum, plugin) => ({
      views: sum.views + plugin.metrics.views,
      copies: sum.copies + plugin.metrics.copies,
      hearts: sum.hearts + plugin.metrics.hearts,
    }),
    { views: 0, copies: 0, hearts: 0 },
  );
  assert.ok(readme.includes(`Marketplace data generated at \`${data.generatedAt}\``));
  assert.ok(readme.includes(`**${listed.length} of ${data.plugins.length} listed** on the marketplace, ${totals.views} views, ${totals.copies} copies, ${totals.hearts} hearts.`));
});

test("site shell includes discovery, delivery, accessibility, and domain contracts", () => {
  assert.match(html, /id="catalog"/);
  assert.match(html, /id="ledger"/);
  assert.match(html, /class="skip-link"/);
  assert.match(css, /prefers-reduced-motion/);
  assert.equal(cname, "oma.intentsolutions.io");
});

test("public product branding keeps the capital T in omaTrail", () => {
  const publicText = `${html}\n${JSON.stringify(data)}`;
  assert.ok(publicText.includes("omaTrail"));
  assert.ok(!publicText.includes("Omatrail"));
  assert.ok(!publicText.includes("OMATRAIL"));
});
