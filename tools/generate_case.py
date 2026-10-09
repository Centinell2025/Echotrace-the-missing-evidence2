#!/usr/bin/env python3
"""Generate deterministic, fictional EchoTrace 2 forensic training evidence."""
from pathlib import Path
import csv, hashlib, json, zipfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build"
ART = OUT / "artifacts"
def write(name, content):
    path = ART / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
def csvwrite(name, rows):
    path = ART / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerows(rows)
def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    ART.mkdir(parents=True, exist_ok=True)
    # Reserved documentation addresses and a fictional example domain.
    csvwrite("identity/signins.csv", [
        ["utc","user","src_host","src_ip","result","event_id","session"],
        ["2026-09-22T01:56:12Z","svc_backup","BKP-CTRL-01","192.0.2.18","SUCCESS","4624","S-8841"],
        ["2026-09-22T02:03:04Z","mara.ellis","OPS-WS-07","192.0.2.47","SUCCESS","4624","S-8852"],
        ["2026-09-22T02:11:55Z","svc_restore","BKP-CTRL-01","192.0.2.18","SUCCESS","4624","S-8860"]
    ])
    csvwrite("windows/security_events.csv", [
        ["utc","host","event_id","account","session","action","object"],
        ["2026-09-22T02:03:04Z","OPS-WS-07","4624","mara.ellis","S-8852","logon","interactive"],
        ["2026-09-22T02:07:19Z","BKP-CTRL-01","4663","mara.ellis","S-8852","WRITE","catalog/current.json"],
        ["2026-09-22T02:11:55Z","BKP-CTRL-01","4624","svc_restore","S-8860","logon","service"]
    ])
    csvwrite("change_control/approvals.csv", [
        ["request","owner","approved_utc","scope","status"],
        ["CHG-2408","mara.ellis","2026-09-21T18:30:00Z","weekly restore verification","APPROVED"],
        ["CHG-2411","simon.reed","","catalog replacement","REJECTED"]
    ])
    csvwrite("recovery/catalog.csv", [
        ["snapshot","dataset","created_utc","state","approval"],
        ["SNAP-0919-A","ledger","2026-09-19T23:00:00Z","VERIFIED","CHG-2408"],
        ["SNAP-0922-X","ledger","2026-09-22T02:06:00Z","VERIFIED","CHG-2408"],
        ["SNAP-0919-B","hr","2026-09-19T23:05:00Z","UNVERIFIED","CHG-2408"]
    ])
    csvwrite("recovery/immutable_inventory.csv", [
        ["snapshot","dataset","object","created_utc","verification"],
        ["SNAP-0919-A","ledger","obj-ledger-a","2026-09-19T23:00:00Z","PASS"],
        ["SNAP-0919-B","hr","obj-hr-b","2026-09-19T23:05:00Z","FAIL"]
    ])
    csvwrite("recovery/restore_dry_run.csv", [
        ["utc","snapshot","dataset","result","detail"],
        ["2026-09-22T02:16:00Z","SNAP-0922-X","ledger","FAIL","object not found"],
        ["2026-09-22T02:21:00Z","SNAP-0919-A","ledger","PASS","isolated checksum validation"],
        ["2026-09-22T02:24:00Z","SNAP-0919-B","hr","FAIL","chunk missing"]
    ])
    write("linux/auth.log", """2026-09-22T02:10:01Z restore-node sshd[2180]: Accepted publickey for svc_restore from 192.0.2.18 port 51214 ssh2
2026-09-22T02:12:10Z restore-node systemd[1]: Started isolated-restore-check.service
2026-09-22T02:13:05Z restore-node audit[2201]: EXECVE exe=/usr/local/bin/verify_restore args=--snapshot SNAP-0922-X
""")
    csvwrite("network/flows.csv", [
        ["utc","src_ip","dst_ip","proto","dst_port","bytes","purpose"],
        ["2026-09-22T02:06:51Z","192.0.2.47","198.51.100.24","HTTPS","443","8142","catalog-upload"],
        ["2026-09-22T02:10:01Z","192.0.2.18","192.0.2.60","SSH","22","1920","restore-session"]
    ])
    csvwrite("network/dns.csv", [
        ["utc","client_ip","query","answer"],
        ["2026-09-22T02:06:40Z","192.0.2.47","catalog-sync.example","198.51.100.24"]
    ])
    write("recovery/object_chunks.json", json.dumps({
        "obj-ledger-a":{"chunk":"ledger-A-001","sha256":sha(b"FICTIONAL_LEDGER_RECOVERABLE_V1")},
        "obj-hr-b":{"chunk":"hr-B-001","sha256":None},
        "SNAP-0922-X":{"object":None,"status":"missing"}
    }, indent=2)+"\n")
    write("case_context.txt", """ECHOTrace 2: The Phantom Restore
ALL DATA IS SYNTHETIC. Timeline is UTC. The approved CHG-2408 covers only weekly verification, not catalog replacement.
Events are simplified CSV training exports, NOT native Windows EVTX or a packet capture.
Do not attribute any activity to AI without independent evidence.
""")
    manifest = {}
    for p in sorted(ART.rglob("*")):
        if p.is_file():
            manifest[p.relative_to(ART).as_posix()] = {"sha256":sha(p.read_bytes()),"bytes":p.stat().st_size}
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"evidence_manifest.json").write_text(json.dumps({"case":"EchoTrace-2","synthetic":True,"files":manifest},indent=2)+"\n",encoding="utf-8")
    with zipfile.ZipFile(OUT/"artifacts.zip","w",compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ART.rglob("*")):
            if p.is_file(): z.write(p,p.relative_to(ART).as_posix())
    print("Generated",len(manifest),"artifacts and artifacts.zip")

if __name__ == "__main__":
    main()
