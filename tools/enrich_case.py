"""Additional synthetic artifacts for EchoTrace 2. No native EVTX/PCAP claims."""
import csv, json
from pathlib import Path

def enrich(art: Path):
    def rows(name, data):
        p=art/name
        p.parent.mkdir(parents=True,exist_ok=True)
        with p.open("w",encoding="utf-8",newline="") as f:
            csv.writer(f).writerows(data)
    rows("time/clock_reference.csv",[
        ["host","observed_local_utc","trusted_reference_utc","offset_seconds","source"],
        ["OPS-WS-07","2026-09-22T02:07:49Z","2026-09-22T02:07:19Z","30","isolated-ntp-test"],
        ["BKP-CTRL-01","2026-09-22T02:07:19Z","2026-09-22T02:07:19Z","0","isolated-ntp-test"]])
    rows("scheduler/job_baseline.csv",[
        ["job_id","account","scope","frequency","approved_change","last_normal_utc"],
        ["JOB-014","svc_backup","weekly restore verification","weekly","CHG-2408","2026-09-15T02:00:00Z"]])
    rows("storage/file_metadata.csv",[
        ["file","source","mtime_utc","ctime_utc","size_bytes","record"],
        ["catalog/current.json","BKP-CTRL-01","2026-09-22T02:07:19Z","2026-09-22T02:07:19Z","8142","MFT-3344"],
        ["catalog/previous.json","BKP-CTRL-01","2026-09-15T02:00:00Z","2026-09-15T02:00:00Z","8030","MFT-3320"]])
    rows("recovery/catalog_chunk_claims.csv",[
        ["snapshot","object","chunk_id","claimed_sha256","claim_source"],
        ["SNAP-0922-X","obj-ledger-x","ledger-X-001","8c5b0fa0f983e4b52b114f1e672d5e2bd3bb35f5d7db5ad34b4686d11e49a107","catalog"],
        ["SNAP-0919-A","obj-ledger-a","ledger-A-001","a4f4d4e8c109b8b99a4d180d1b32e45a2b99d94e7bdb8b7832bb018c0a38a0d1","catalog"]])
    rows("recovery/object_integrity_checks.csv",[
        ["snapshot","object","expected_chunk","verified_sha256","result"],
        ["SNAP-0922-X","obj-ledger-x","ledger-X-001","","MISSING_OBJECT"],
        ["SNAP-0919-A","obj-ledger-a","ledger-A-001","","SEE_OBJECT_CHUNKS_JSON"]])
    rows("recovery/recovery_safety.csv",[
        ["operation_id","target","mode","evidence_risk","requires_preservation"],
        ["RESTORE-INPLACE-01","BKP-CTRL-01/catalog/current.json","in-place-overwrite","overwrites_original_catalog_metadata","YES"],
        ["RESTORE-ISOLATED-02","offline-copy","isolated-read-only","preserves_original","NO"]])
    rows("network/proxy_observations.csv",[
        ["utc","flow_id","src_ip","dst_ip","tls_sni","http_method_visible","body_visible"],
        ["2026-09-22T02:06:51Z","FLOW-1201","192.0.2.47","198.51.100.24","catalog-sync.example","NO","NO"]])
    (art/"time"/"README.txt").write_text("Synthetic clock reference. offset_seconds = observed clock minus trusted UTC. Do not assume all hosts share the same offset.\n",encoding="utf-8")
