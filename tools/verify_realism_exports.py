#!/usr/bin/env python3
"""Validate synthetic cross-format forensic evidence and its limits."""
from pathlib import Path
import csv, json
root=Path(__file__).resolve().parents[1]/"build"/"artifacts"
def table(name):
    with (root/name).open(encoding="utf-8",newline="") as f: return list(csv.DictReader(f))
def jsonl(name):
    with (root/name).open(encoding="utf-8") as f: return [json.loads(line) for line in f if line.strip()]
sysmon=jsonl("windows/sysmon_operational.jsonl")
security=jsonl("windows/security_events_extended.jsonl")
audit=jsonl("linux/auditd_events.jsonl")
prov=jsonl("provenance/acquisition_log.jsonl")
usn=table("storage/usn_journal_export.csv")
conn=table("network/zeek_conn_export.csv")
ssl=table("network/zeek_ssl_export.csv")
storage=table("recovery/storage_access_audit.csv")
assert len(sysmon)>=4 and all(x["synthetic"] is True for x in sysmon)
assert any(x["EventID"]==3 and x["DestinationIp"]=="198.51.100.24" for x in sysmon)
assert any(x["EventID"]==4663 and x["CorrelationSession"]=="S-8852" for x in security)
assert any(x["type"]=="EXECVE" and x["exe"]=="/usr/local/bin/verify_restore" for x in audit)
assert any(x["file_reference"]=="MFT-3344" and "DATA_OVERWRITE" in x["reason"] for x in usn)
assert any(x["uid"]=="FLOW-1201" for x in conn)
assert any(x["uid"]=="FLOW-1201" and x["payload_visibility"]=="ENCRYPTED" for x in ssl)
assert any(x["object"]=="obj-ledger-x" and x["status"]=="NOT_FOUND" for x in storage)
assert len(prov)>=3 and all(x["synthetic"] is True for x in prov)
assert "not native EVTX" in (root/"provenance/LIMITATIONS.txt").read_text()
print("PASS: structured synthetic Sysmon, Security, auditd, USN, Zeek, storage audit and provenance")
