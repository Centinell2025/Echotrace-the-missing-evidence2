#!/usr/bin/env python3
"""Validate consistency of the fictional backup case."""
from pathlib import Path
import csv, hashlib, json
root=Path(__file__).resolve().parents[1]/"build"/"artifacts"
def rows(name):
    with (root/name).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))
objects=json.loads((root/"recovery/object_chunks.json").read_text())
claims={r["snapshot"]:r for r in rows("recovery/catalog_chunk_claims.csv")}
checks={r["snapshot"]:r for r in rows("recovery/object_integrity_checks.csv")}
digest=hashlib.sha256(b"FICTIONAL_LEDGER_RECOVERABLE_V1").hexdigest()
assert objects["obj-ledger-a"]["sha256"]==digest
assert claims["SNAP-0919-A"]["claimed_sha256"]==digest
assert checks["SNAP-0919-A"]["verified_sha256"]==digest
assert checks["SNAP-0922-X"]["result"]=="MISSING_OBJECT"
assert "EDUCATIONAL AND AUTHORIZED" in (root/"EDUCATIONAL_USE_NOTICE.txt").read_text()
print("PASS: synthetic backup hashes and educational notice")
