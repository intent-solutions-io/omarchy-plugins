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

  const generatedById = new Map(data.plugins.map((plugin) => [plugin.id, plugin]));
  for (const source of config.plugins) {
    const generated = generatedById.get(source.id);
    assert.ok(generated, `missing generated entry for ${source.id}`);
    assert.equal(generated.name, source.name);
    assert.equal(generated.slug, source.repo.replace(/^omarchy-/, "").replace(/-entry$/, ""));
    assert.equal(generated.repo, source.repo);
    assert.equal(generated.repoUrl, `https://github.com/jeremylongshore/${source.repo}`);
    assert.equal(generated.pitch, source.pitch);
    assert.equal(generated.lifecycle, source.lifecycle);
    if (source.lifecycle === "under-review") {
      assert.equal(generated.category, source.category);
      assert.deepEqual(generated.tags, source.tags);
      assert.equal(generated.submissionUrl, source.submissionUrl);
    }
  }
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

  for (const plugin of data.plugins) {
    const category = plugin.lifecycle === "listed"
      ? `[${plugin.category}](${plugin.marketplaceUrl})`
      : `[under review](${plugin.submissionUrl})`;
    const metrics = plugin.metrics
      ? `${plugin.metrics.views} | ${plugin.metrics.copies} | ${plugin.metrics.hearts}`
      : "n/a | n/a | n/a";
    const row = `| **${plugin.name}** | ${plugin.pitch} | [repo](${plugin.repoUrl}) | ${category} | ${metrics} |`;
    assert.ok(readme.includes(row), `README row drift for ${plugin.name}`);
    if (plugin.installCommand) {
      assert.ok(readme.includes(`# ${plugin.name}\n${plugin.installCommand}`), `README install drift for ${plugin.name}`);
    }
    if (plugin.metrics) {
      for (const value of Object.values(plugin.metrics)) {
        assert.ok(Number.isSafeInteger(value) && value >= 0, `invalid metric for ${plugin.name}`);
      }
    }
  }
});

test("site shell includes discovery, delivery, accessibility, and domain contracts", () => {
  assert.match(html, /id="catalog"/);
  assert.match(html, /id="ledger"/);
  assert.match(html, /class="skip-link"/);
  assert.match(html, /Intent Solutions Omarchy Plugins/);
  assert.doesNotMatch(html, /O\/|OMA PLUGIN WORKS|Omarchy Plugin Works|wordmark-mark/);
  assert.match(css, /prefers-reduced-motion/);
  assert.equal(cname, "oma.intentsolutions.io");
});

test("every plugin has a generated permanent detail page", async () => {
  for (const plugin of data.plugins) {
    const detail = await readFile(new URL(`../site/plugins/${plugin.slug}/index.html`, import.meta.url), "utf8");
    assert.ok(detail.includes(`<h1>${plugin.name}</h1>`), `missing title for ${plugin.name}`);
    assert.ok(detail.includes(plugin.repoUrl), `missing repo link for ${plugin.name}`);
    assert.ok(detail.includes(plugin.marketplaceUrl || plugin.submissionUrl), `missing marketplace authority for ${plugin.name}`);
    assert.ok(detail.includes(plugin.pitch.replaceAll("&", "&amp;")), `missing pitch for ${plugin.name}`);
    assert.ok(detail.includes("Intent Solutions Omarchy Plugins"), `missing site brand for ${plugin.name}`);
    assert.doesNotMatch(detail, /O\/|OMA PLUGIN WORKS|Omarchy Plugin Works|wordmark-mark/);
    if (plugin.installCommand) assert.ok(detail.includes(plugin.installCommand), `missing install command for ${plugin.name}`);
  }
});

test("public product branding keeps the capital T in omaTrail", () => {
  const publicText = `${html}\n${JSON.stringify(data)}`;
  assert.ok(publicText.includes("omaTrail"));
  assert.ok(!publicText.includes("Omatrail"));
  assert.ok(!publicText.includes("OMATRAIL"));
});
