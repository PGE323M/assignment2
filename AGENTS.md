# Agent Instructions

## Submit assignment

When the user says `submit assignment`:

1. Do not edit any files during submission.
2. Run `git status --short`.
3. Verify that `assignment2.py` is the only changed file. If any other tracked or untracked path has changed, stop and report it.
4. Run `python -m unittest -v test.py`. If any test fails, stop and report the failure.
5. Run `git diff --check`. If it reports a problem, stop.
6. Stage only `assignment2.py` with `git add -- assignment2.py`; never use `git add .`.
7. Run `git commit -m "Complete assignment 2"`.
8. Run `git push origin HEAD`.
9. Run `git status --short` and `git log -1 --oneline`, then report the result.

Never bypass a failing test, hide an unexpected change, or modify these instructions during submission.
