#!/usr/bin/env python

"""Public tests for PGE 323M Assignment 2."""

from math import isclose
from pathlib import Path
import re
import unittest

from assignment2 import finite_diff, square, well


class TestAgentInstructions(unittest.TestCase):
    def test_required_submission_contract(self):
        path = Path("AGENTS.md")
        self.assertTrue(path.is_file(), "AGENTS.md must remain at the repository root")

        text = " ".join(path.read_text(encoding="utf-8").lower().split())
        required = (
            "submit assignment",
            "git status --short",
            "assignment2.py",
            "python -m unittest -v test.py",
            "git diff --check",
            "git add -- assignment2.py",
            "git commit",
            "git push",
            "stop",
        )
        for fragment in required:
            self.assertIn(fragment, text, f"AGENTS.md is missing: {fragment}")

        self.assertIsNone(
            re.search(r"\bgit\s+add\s+\.(?:\s|$)", text),
            "AGENTS.md must not use broad staging with 'git add .'",
        )


class TestAssignment2Public(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(10), 100)
        self.assertEqual(square(0), 0)

    def test_finite_diff(self):
        self.assertTrue(isclose(finite_diff(4, 0.1), 5.0, abs_tol=1.0e-6))

    def test_well(self):
        self.assertTrue(isclose(well(1.2, 5000, 3000), 427.44, abs_tol=0.1))


if __name__ == "__main__":
    unittest.main()
