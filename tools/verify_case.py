#!/usr/bin/env python3
"""Verify deterministic synthetic artifact package integrity and case logic."""
from pathlib import Path
import csv, hashlib, json, zipfile
root=Path(__file__).resolve().parents[1]
out=root/"build"
manifest=json.loads((out/"evidence_manifest.json").read_text())
with zipfile.ZipFile(out/"artifacts.zip") as z:
    assert set(z.namelist())==set(manifest["files"])
    for name,meta in manifest["files"].items():
        data=z.read(name)
        assert len(data)==meta["bytes"],name
        assert hashlib.sha256(data).hexdigest()==meta["sha256"],name
    def rows(name):
        return list(csv.DictReader(z.read(name).decode().splitlines()))
    cat=rows("recovery/catalog.csv")
    inv=rows("recovery/immutable_inventory.csv")
    assert "SNAP-0922-X" in {x["snapshot"] for x in cat}
    assert "SNAP-0922-X" not in {x["snapshot"] for x in inv}
    assert any(x["snapshot"]=="SNAP-0919-A" and x["result"]=="PASS" for x in rows("recovery/restore_dry_run.csv"))
    assert any(x["request"]=="CHG-2411" and x["status"]=="REJECTED" for x in rows("change_control/approvals.csv"))
print("PASS: hashes, archive, catalog discrepancy, restore result, rejected approval")
