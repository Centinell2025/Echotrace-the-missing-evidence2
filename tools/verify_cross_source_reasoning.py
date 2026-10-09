#!/usr/bin/env python3
"""Independent cross-source forensic reasoning gates for fictional EchoTrace 2."""
from pathlib import Path
import csv, json, hashlib
from datetime import datetime, timezone
root=Path(__file__).resolve().parents[1]/"build"/"artifacts"
def rows(name):
    with (root/name).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))
def stamp(s):
    return datetime.fromisoformat(s.replace("Z","+00:00"))
events=rows("windows/security_events.csv")
signins=rows("identity/signins.csv")
changes=rows("change_control/approvals.csv")
catalog=rows("recovery/catalog.csv")
inventory=rows("recovery/immutable_inventory.csv")
checks=rows("recovery/object_integrity_checks.csv")
runs=rows("recovery/restore_dry_run.csv")
dns=rows("network/dns.csv")
flows=rows("network/flows.csv")
proxy=rows("network/proxy_observations.csv")
clocks=rows("time/clock_reference.csv")
writes=[e for e in events if e["action"]=="WRITE" and e["object"]=="catalog/current.json"]
assert len(writes)==1
write=writes[0]
assert write["event_id"]=="4663"
auth=[a for a in signins if a["user"]==write["account"] and a["session"]==write["session"]]
assert len(auth)==1 and stamp(auth[0]["utc"])<stamp(write["utc"])
assert any(c["request"]=="CHG-2408" and c["status"]=="APPROVED" and c["scope"]=="weekly restore verification" for c in changes)
assert any(c["request"]=="CHG-2411" and c["status"]=="REJECTED" and c["scope"]=="catalog replacement" for c in changes)
verified={r["snapshot"] for r in catalog if r["state"]=="VERIFIED"}
immutable={r["snapshot"] for r in inventory}
phantoms=verified-immutable
assert phantoms=={"SNAP-0922-X"}
assert any(c["snapshot"]=="SNAP-0922-X" and c["result"]=="MISSING_OBJECT" for c in checks)
assert any(r["snapshot"]=="SNAP-0922-X" and r["result"]=="FAIL" for r in runs)
assert any(r["snapshot"]=="SNAP-0919-A" and r["result"]=="PASS" for r in runs)
assert any(r["host"]=="OPS-WS-07" and r["offset_seconds"]=="30" for r in clocks)
linked=[(d,f,p) for d in dns for f in flows for p in proxy if d["client_ip"]==f["src_ip"] and d["answer"]==f["dst_ip"] and f["flow_id"]==p["flow_id"] and d["query"]==p["tls_sni"] and stamp(d["utc"])<=stamp(f["utc"])]
assert len(linked)==1 and linked[0][2]["body_visible"]=="NO"
assert (root/"EDUCATIONAL_USE_NOTICE.txt").is_file()
print("PASS: cross-source identity/session correlation, authorization mismatch, phantom snapshot, recovery, clock and network evidence")
print("LIMITATIONS: synthetic exports; TLS payload invisible; no exfiltration, actor attribution or production restore proven")
