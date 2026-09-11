import copy
import unittest

from scripts.catalog_pipeline import CatalogError, build_catalog


def fixtures():
    plugin_id = "io.github.jeremylongshore.example"
    repo = "omarchy-example-entry"
    config = {
        "marketplace": {
            "pluginPage": "https://plugins.omarchy.org/plugin.html?id=",
            "authorPage": "https://plugins.omarchy.org/index.html?author=jeremylongshore",
        },
        "github": {"owner": "jeremylongshore"},
        "families": ["Utilities"],
        "plugins": [{
            "id": plugin_id,
            "name": "Example",
            "repo": repo,
            "family": "Utilities",
            "lifecycle": "listed",
            "pitch": "A focused example plugin.",
        }],
        "template": {"name": "Template", "repo": "omarchy-widget-template", "pitch": "A safe starting point."},
    }
    catalog_plugin = {
        "id": plugin_id,
        "name": "Example",
        "version": "1.2.3",
        "category": "Productivity",
        "tags": ["bar"],
        "installCommand": f"omarchy plugin add https://github.com/jeremylongshore/{repo}.git --enable",
        "verificationStatus": "verified",
    }
    catalog = {"generatedAt": "2026-09-10T12:00:00Z", "plugins": [catalog_plugin]}
    stats = {"plugins": {plugin_id: {"views": 10, "copies": 2, "hearts": 1}}}
    github = {"repos": {
        repo: {
            "repoUrl": f"https://github.com/jeremylongshore/{repo}",
            "stars": 4,
            "openIssues": 1,
            "pushedAt": "2026-09-10T11:00:00Z",
            "defaultBranch": "main",
            "archived": False,
            "manifest": {"id": plugin_id, "name": "Example", "version": "1.2.3"},
            "manifestSha": "a" * 40,
            "preview": {
                "available": True,
                "url": f"https://raw.githubusercontent.com/jeremylongshore/{repo}/main/preview.png",
                "path": "preview.png",
                "sha": "b" * 40,
            },
        },
        "omarchy-widget-template": {
            "repoUrl": "https://github.com/jeremylongshore/omarchy-widget-template",
            "stars": 2,
            "openIssues": 0,
            "pushedAt": "2026-09-09T11:00:00Z",
            "defaultBranch": "main",
            "archived": False,
            "manifest": None,
            "manifestSha": None,
            "preview": {"available": False, "url": None, "path": "preview.png", "sha": None},
        },
    }}
    return config, catalog, stats, github


class CatalogPipelineTests(unittest.TestCase):
    def test_official_marketplace_is_lifecycle_authority(self):
        config, catalog, stats, github = fixtures()
        plugin = build_catalog(config, catalog, stats, github)["plugins"][0]
        self.assertEqual(plugin["lifecycle"], "listed")
        self.assertEqual(plugin["manifest"]["status"], "aligned")
        self.assertEqual(plugin["preview"]["status"], "verified")
        self.assertEqual(plugin["github"]["stars"], 4)
        self.assertIsNotNone(plugin["marketplaceUrl"])

    def test_configured_listed_becomes_not_listed_when_absent_upstream(self):
        config, catalog, stats, github = fixtures()
        catalog["plugins"] = []
        plugin = build_catalog(config, catalog, stats, github)["plugins"][0]
        self.assertEqual(plugin["lifecycle"], "not-listed")
        self.assertIsNone(plugin["marketplaceUrl"])
        self.assertIsNone(plugin["installCommand"])
        self.assertIsNone(plugin["metrics"])

    def test_review_and_developing_states_remain_explicit(self):
        for lifecycle in ("under-review", "developing"):
            with self.subTest(lifecycle=lifecycle):
                config, catalog, stats, github = fixtures()
                catalog["plugins"] = []
                config["plugins"][0]["lifecycle"] = lifecycle
                if lifecycle == "under-review":
                    config["plugins"][0]["submissionUrl"] = "https://github.com/basecamp/omarchy-plugins/pull/123"
                plugin = build_catalog(config, catalog, stats, github)["plugins"][0]
                self.assertEqual(plugin["lifecycle"], lifecycle)
                self.assertEqual(plugin["submissionUrl"] is not None, lifecycle == "under-review")

    def test_missing_preview_and_manifest_drift_are_published(self):
        config, catalog, stats, github = fixtures()
        repo = config["plugins"][0]["repo"]
        github["repos"][repo]["preview"] = {"available": False, "url": None, "path": "preview.png", "sha": None}
        github["repos"][repo]["manifest"]["version"] = "9.9.9"
        plugin = build_catalog(config, catalog, stats, github)["plugins"][0]
        self.assertEqual(plugin["preview"]["status"], "missing")
        self.assertIsNone(plugin["previewUrl"])
        self.assertEqual(plugin["manifest"]["status"], "drift")
        self.assertIn("version differs from the official marketplace", plugin["manifest"]["issues"])

    def test_missing_manifest_is_not_treated_as_aligned(self):
        config, catalog, stats, github = fixtures()
        github["repos"][config["plugins"][0]["repo"]]["manifest"] = None
        plugin = build_catalog(config, catalog, stats, github)["plugins"][0]
        self.assertEqual(plugin["manifest"]["status"], "missing")

    def test_malformed_inventory_fails_closed(self):
        mutations = []
        config, catalog, stats, github = fixtures()
        duplicate = copy.deepcopy(config["plugins"][0])
        config["plugins"].append(duplicate)
        mutations.append((config, catalog, stats, github))

        config, catalog, stats, github = fixtures()
        config["plugins"][0]["family"] = "Unknown"
        mutations.append((config, catalog, stats, github))

        config, catalog, stats, github = fixtures()
        config["plugins"][0]["lifecycle"] = "maybe"
        mutations.append((config, catalog, stats, github))

        config, catalog, stats, github = fixtures()
        config["plugins"][0]["pitch"] = "x" * 501
        mutations.append((config, catalog, stats, github))

        config, catalog, stats, github = fixtures()
        github["repos"][config["plugins"][0]["repo"]]["stars"] = -1
        mutations.append((config, catalog, stats, github))

        for case in mutations:
            with self.subTest(case=case[0]["plugins"][0]):
                with self.assertRaises(CatalogError):
                    build_catalog(*case)


if __name__ == "__main__":
    unittest.main()
