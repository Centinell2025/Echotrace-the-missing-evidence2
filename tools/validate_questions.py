#!/usr/bin/env python3
"""Fail closed on missing answer-evidence mappings in a future JSON question bank."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/"questions"/"validated_questions.json"
if not p.exists():
    raise SystemExit("NOT READY: questions/validated_questions.json missing; draft is not validated.")
data=json.loads(p.read_text(encoding="utf-8"))
assert isinstance(data,list) and len(data)==20,"Expected exactly 20 questions"
ids=set()
for q in data:
    for key in ("id","prompt","answer","primary_artifact","reproduce","cross_check","uniqueness_rationale"):
        assert isinstance(q.get(key),str) and q[key].strip(),f"Missing {key} in {q.get('id')}"
    assert q["id"] not in ids,"Duplicate question ID"
    ids.add(q["id"])
    assert (root/"build"/"artifacts"/q["primary_artifact"]).is_file(),f"Missing evidence for {q['id']}"
    assert (root/"build"/"artifacts"/q["cross_check"]).is_file(),f"Missing cross-check for {q['id']}"
print("PASS: 20 question mappings have evidence paths and mandatory metadata (manual answer review still required)")
