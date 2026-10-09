#!/usr/bin/env python3
"""Fail-closed release readiness check. Does not certify forensic authenticity."""
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
required=[
    root/"EDUCATIONAL_USE_AND_ETHICS.md",
    root/"build"/"artifacts.zip",
    root/"build"/"evidence_manifest.json",
    root/"questions"/"validated_questions.json",
    root/"instructor"/"WALKTHROUGH_FINAL.pdf",
    root/"docs"/"BLIND_PLAYTEST_REPORT.md",
    root/"docs"/"NATIVE_ARTIFACT_VALIDATION.md",
]
missing=[str(p.relative_to(root)) for p in required if not p.is_file()]
if missing:
    print("NOT READY — missing required release artifacts:")
    for item in missing: print(" -",item)
    sys.exit(1)
print("Files present; manual verification of contents, integrity and HTB requirements still required.")
