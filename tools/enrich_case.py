"""Additional synthetic artifacts for EchoTrace 2. No native EVTX/PCAP claims."""
import csv, json, hashlib
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
        ["SNAP-0919-A","obj-ledger-a","ledger-A-001",hashlib.sha256(b"FICTIONAL_LEDGER_RECOVERABLE_V1").hexdigest(),"catalog"]])
    rows("recovery/object_integrity_checks.csv",[
        ["snapshot","object","expected_chunk","verified_sha256","result"],
        ["SNAP-0922-X","obj-ledger-x","ledger-X-001","","MISSING_OBJECT"],
        ["SNAP-0919-A","obj-ledger-a","ledger-A-001",hashlib.sha256(b"FICTIONAL_LEDGER_RECOVERABLE_V1").hexdigest(),"PASS"]])
    rows("recovery/recovery_safety.csv",[
        ["operation_id","target","mode","evidence_risk","requires_preservation"],
        ["RESTORE-INPLACE-01","BKP-CTRL-01/catalog/current.json","in-place-overwrite","overwrites_original_catalog_metadata","YES"],
        ["RESTORE-ISOLATED-02","offline-copy","isolated-read-only","preserves_original","NO"]])
    rows("network/proxy_observations.csv",[
        ["utc","flow_id","src_ip","dst_ip","tls_sni","http_method_visible","body_visible"],
        ["2026-09-22T02:06:51Z","FLOW-1201","192.0.2.47","198.51.100.24","catalog-sync.example","NO","NO"]])
    (art/"time"/"README.txt").write_text("Synthetic clock reference. offset_seconds = observed clock minus trusted UTC. Do not assume all hosts share the same offset.\n",encoding="utf-8")

    # High-fidelity structured synthetic exports. These are NOT native EVTX, PCAP or auditd binaries.
    def jsonlines(name, items):
        p=art/name
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text("".join(json.dumps(x,sort_keys=True)+"\\n" for x in items),encoding="utf-8")
    jsonlines("windows/sysmon_operational.jsonl",[
        {"UtcTime":"2026-09-22 02:01:44.000","EventID":1,"Computer":"OPS-WS-07","User":"NT AUTHORITY\\\\SYSTEM","Image":"C:\\\\Windows\\\\System32\\\\svchost.exe","ProcessGuid":"{FAKE-0001}","CommandLine":"svchost.exe -k netsvcs","synthetic":True},
        {"UtcTime":"2026-09-22 02:05:48.000","EventID":1,"Computer":"OPS-WS-07","User":"LAB\\\\mara.ellis","Image":"C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe","ProcessGuid":"{FAKE-0002}","ParentImage":"C:\\\\Windows\\\\explorer.exe","CommandLine":"powershell.exe -NoProfile -File C:\\\\Lab\\\\scripts\\\\check_catalog.ps1","synthetic":True},
        {"UtcTime":"2026-09-22 02:06:51.000","EventID":3,"Computer":"OPS-WS-07","User":"LAB\\\\mara.ellis","Image":"C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe","DestinationIp":"198.51.100.24","DestinationPort":443,"Protocol":"tcp","ProcessGuid":"{FAKE-0002}","synthetic":True},
        {"UtcTime":"2026-09-22 02:09:18.000","EventID":1,"Computer":"OPS-WS-07","User":"LAB\\\\mara.ellis","Image":"C:\\\\Windows\\\\System32\\\\notepad.exe","ProcessGuid":"{FAKE-0003}","CommandLine":"notepad.exe C:\\\\Lab\\\\notes.txt","synthetic":True}
    ])
    jsonlines("windows/security_events_extended.jsonl",[
        {"TimeCreated":"2026-09-22T02:03:04Z","EventID":4624,"Computer":"OPS-WS-07","TargetUserName":"mara.ellis","LogonType":2,"IpAddress":"192.0.2.47","CorrelationSession":"S-8852","synthetic":True},
        {"TimeCreated":"2026-09-22T02:07:19Z","EventID":4663,"Computer":"BKP-CTRL-01","SubjectUserName":"mara.ellis","ObjectName":"catalog/current.json","AccessMask":"0x2","Accesses":["WriteData"],"CorrelationSession":"S-8852","synthetic":True},
        {"TimeCreated":"2026-09-22T02:11:55Z","EventID":4624,"Computer":"BKP-CTRL-01","TargetUserName":"svc_restore","LogonType":5,"CorrelationSession":"S-8860","synthetic":True}
    ])
    jsonlines("linux/auditd_events.jsonl",[
        {"timestamp":"2026-09-22T02:10:01Z","type":"USER_LOGIN","host":"restore-node","acct":"svc_restore","addr":"192.0.2.18","res":"success","synthetic":True},
        {"timestamp":"2026-09-22T02:13:05Z","type":"EXECVE","host":"restore-node","pid":2201,"uid":1002,"exe":"/usr/local/bin/verify_restore","a0":"--snapshot","a1":"SNAP-0922-X","synthetic":True}
    ])
    rows("storage/usn_journal_export.csv",[
        ["utc","host","usn","file_reference","reason","path","synthetic"],
        ["2026-09-22T02:07:19Z","BKP-CTRL-01","744103","MFT-3344","DATA_OVERWRITE|CLOSE","catalog/current.json","YES"],
        ["2026-09-22T02:07:20Z","BKP-CTRL-01","744104","MFT-3344","BASIC_INFO_CHANGE|CLOSE","catalog/current.json","YES"],
        ["2026-09-22T02:09:21Z","BKP-CTRL-01","744105","MFT-3320","CLOSE","catalog/previous.json","YES"]
    ])
    rows("network/zeek_conn_export.csv",[
        ["ts_utc","uid","id.orig_h","id.orig_p","id.resp_h","id.resp_p","proto","service","duration","orig_bytes","resp_bytes","history"],
        ["2026-09-22T02:06:51Z","FLOW-1201","192.0.2.47","52014","198.51.100.24","443","tcp","ssl","0.43","8142","2014","ShADadFf"],
        ["2026-09-22T02:10:01Z","FLOW-1202","192.0.2.18","51214","192.0.2.60","22","tcp","ssh","1.18","1920","4031","ShADadFf"]
    ])
    rows("network/zeek_ssl_export.csv",[
        ["ts_utc","uid","server_name","version","cipher","validation_status","payload_visibility"],
        ["2026-09-22T02:06:51Z","FLOW-1201","catalog-sync.example","TLSv1.3","TLS_AES_128_GCM_SHA256","NOT_CAPTURED","ENCRYPTED"],
    ])
    rows("recovery/storage_access_audit.csv",[
        ["utc","principal","operation","object","status","request_id"],
        ["2026-09-19T23:00:00Z","svc_backup","PUT","obj-ledger-a","SUCCESS","REQ-7701"],
        ["2026-09-22T02:06:00Z","svc_backup","LIST","obj-ledger-x","NOT_FOUND","REQ-7702"],
        ["2026-09-22T02:16:00Z","svc_restore","GET","obj-ledger-x","NOT_FOUND","REQ-7703"]
    ])
    jsonlines("provenance/acquisition_log.jsonl",[
        {"acquired_utc":"2026-09-22T04:00:00Z","collector":"LAB-IR-01","source":"OPS-WS-07","method":"synthetic-export","evidence":"windows/sysmon_operational.jsonl","case":"EchoTrace-2","synthetic":True},
        {"acquired_utc":"2026-09-22T04:03:00Z","collector":"LAB-IR-01","source":"BKP-CTRL-01","method":"synthetic-export","evidence":"storage/usn_journal_export.csv","case":"EchoTrace-2","synthetic":True},
        {"acquired_utc":"2026-09-22T04:06:00Z","collector":"LAB-IR-01","source":"LAB-NET-01","method":"synthetic-export","evidence":"network/zeek_conn_export.csv","case":"EchoTrace-2","synthetic":True}
    ])
    (art/"provenance"/"LIMITATIONS.txt").write_text(
        "All evidence is fabricated for an isolated educational exercise.\\n"
        "Sysmon, Windows Security, auditd, Zeek and USN files are structured synthetic exports, not native EVTX, PCAP, $UsnJrnl or auditd logs.\\n"
        "The synthetic acquisition log is NOT a real chain-of-custody record.\\n"
        "Network byte counts and TLS metadata do not prove exfiltration.\\n",
        encoding="utf-8")
