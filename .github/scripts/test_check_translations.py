"""Regression checks for translation integrity failures."""

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "check_translations", Path(__file__).with_name("check_translations.py"),
)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class TranslationChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.base = self.root / "docs/i18n"
        self.patch = patch.multiple(checker, ROOT=self.root, BASE=self.base)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.source = (
            "# Arm\n\n| Part | Qty |\n|---|---|\n| STS3215 | 1 |\n\n"
            "1. Connect the servo.\n\n```sh\npython control.py\n```\n\n"
            "[Section](README.md#arm)\n"
        )
        (self.root / "README.md").write_text(self.source, encoding="utf-8")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "add", "README.md"], cwd=self.root, check=True)
        digest = checker.digest(self.root / "README.md")
        record = {"source_sha256": digest, "translations": {}}
        for locale in ("en", "ru"):
            path = self.base / locale / "README.md"
            path.parent.mkdir(parents=True)
            path.write_text(
                "[English](../en/README.md) [Русский](../ru/README.md)\n\n"
                '<!-- translated-content -->\n<a id="arm"></a>\n'
                + self.source + "<!-- /translated-content -->\n",
                encoding="utf-8",
            )
            record["translations"][locale] = {
                "path": path.relative_to(self.root).as_posix(), "source_sha256": digest,
            }
        self.manifest = {"locales": {"en": "English", "ru": "Русский"},
                         "documents": {"README.md": record}}

    def mutate(self, old, new):
        path = self.base / "ru/README.md"
        path.write_text(path.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")

    def assert_failure(self, message):
        self.assertTrue(any(message in error for error in checker.check(self.manifest)))

    def test_complete_documents_pass_and_untracked_notes_are_ignored(self):
        (self.root / "notes.md").write_text("Local notes", encoding="utf-8")
        self.assertEqual([], checker.check(self.manifest))

    def test_source_changes_require_translation_updates(self):
        (self.root / "README.md").write_text(self.source + "Updated.\n", encoding="utf-8")
        self.assert_failure("Outdated translation")

    def test_changed_part_numbers_fail(self):
        self.mutate("STS3215", "STS1234")
        self.assert_failure("Changed part identifiers")

    def test_removed_steps_fail(self):
        self.mutate("1. Connect the servo.\n", "")
        self.assert_failure("Missing or altered sections")

    def test_added_numerical_parameters_fail(self):
        self.mutate("Connect the servo.", "Connect the servo at 24 V.")
        self.assert_failure("Added numerical values")

    def test_changed_commands_fail(self):
        self.mutate("python control.py", "python wrong.py")
        self.assert_failure("Changed fenced code or commands")

    def test_missing_link_targets_fail(self):
        self.mutate("README.md#arm", "missing.md#arm")
        self.assert_failure("Broken local link")

    def test_missing_anchors_fail(self):
        self.mutate('id="arm"', 'id="different"')
        self.assert_failure("Missing explicit anchor")

    def test_body_links_stay_in_the_selected_language(self):
        self.mutate("README.md#arm", "../en/README.md#arm")
        self.assert_failure("Wrong language destination")

    def test_tracked_new_sources_require_translations(self):
        (self.root / "new.md").write_text("# New\n", encoding="utf-8")
        subprocess.run(["git", "add", "new.md"], cwd=self.root, check=True)
        self.assert_failure("Source Markdown documents not translated")


if __name__ == "__main__":
    unittest.main()
