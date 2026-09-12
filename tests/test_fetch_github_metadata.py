import unittest
from unittest.mock import patch

from scripts.fetch_github_metadata import MetadataError, fetch_repo


class FetchGithubMetadataTests(unittest.TestCase):
    def test_default_branch_commit_date_is_repository_freshness(self):
        metadata = {
            "html_url": "https://github.com/jeremylongshore/omarchy-example-entry",
            "stargazers_count": 4,
            "pushed_at": "2026-09-12T01:00:00Z",
            "default_branch": "main",
            "archived": False,
            "open_issues_count": 2,
        }
        head = {"commit": {"committer": {"date": "2026-09-09T11:00:00Z"}}}
        with patch("scripts.fetch_github_metadata.request_json", side_effect=[metadata, head, []]) as request:
            _, result = fetch_repo(
                "https://api.github.com",
                "jeremylongshore",
                "omarchy-example-entry",
                None,
            )

        self.assertEqual(result["defaultBranchUpdatedAt"], "2026-09-09T11:00:00Z")
        self.assertNotIn("pushedAt", result)
        self.assertIn("/commits/main", request.call_args_list[1].args[0])

    def test_missing_default_branch_commit_date_fails_closed(self):
        metadata = {
            "default_branch": "main",
            "html_url": "https://github.com/jeremylongshore/omarchy-example-entry",
        }
        with patch("scripts.fetch_github_metadata.request_json", side_effect=[metadata, {"commit": {}}]):
            with self.assertRaisesRegex(MetadataError, "committer date"):
                fetch_repo(
                    "https://api.github.com",
                    "jeremylongshore",
                    "omarchy-example-entry",
                    None,
                )


if __name__ == "__main__":
    unittest.main()
