#!/usr/bin/env python3
"""Check all 20 answer values against actual synthetic evidence, not only file paths."""
import csv
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
art=root/"build"/"artifacts"
bank=json.loads((root/"questions"/"validated_questions.json").read_text(encoding="utf-8"))
assert len(bank)==20
def table(path):
    with (art/path).open(encoding="utf-8",newline="") as stream:
        return list(csv.DictReader(stream))
def match(path,**criteria):
    result=[r for r in table(path) if all(r.get(k)==v for k,v in criteria.items())]
    assert len(result)==1,(path,criteria,len(result))
    return result[0]
def answer(q):
    if q==1: return match("windows/security_events.csv",event_id="4663",action="WRITE")["utc"]
    if q==2: return match("windows/security_events.csv",event_id="4663",action="WRITE")["account"]
    if q==3: return match("identity/signins.csv",user="mara.ellis",result="SUCCESS")["src_host"]
    if q==4: return match("windows/security_events.csv",host="OPS-WS-07",action="logon")["event_id"]
    if q==5: return match("recovery/catalog.csv",snapshot="SNAP-0922-X")["approval"]
    if q==6: return match("change_control/approvals.csv",scope="catalog replacement",status="REJECTED")["request"]
    if q==7:
        inv={r["snapshot"] for r in table("recovery/immutable_inventory.csv")}
        candidates=[r["snapshot"] for r in table("recovery/catalog.csv") if r["state"]=="VERIFIED" and r["snapshot"] not in inv]
        assert len(candidates)==1
        return candidates[0]
    if q==8:
        passed={r["snapshot"] for r in table("recovery/restore_dry_run.csv") if r["result"]=="PASS"}
        both=[r["snapshot"] for r in table("recovery/immutable_inventory.csv") if r["verification"]=="PASS" and r["snapshot"] in passed and r["dataset"]=="ledger"]
        assert len(both)==1
        return both[0]
    if q==9: return match("recovery/object_integrity_checks.csv",result="MISSING_OBJECT")["snapshot"]
    if q==10: return match("recovery/restore_dry_run.csv",result="PASS")["dataset"]
    if q==11: return match("recovery/restore_dry_run.csv",detail="chunk missing")["dataset"]
    if q==12: return match("time/clock_reference.csv",host="OPS-WS-07")["offset_seconds"]
    if q==13: return match("network/flows.csv",src_ip="192.0.2.47",dst_ip="198.51.100.24",dst_port="443")["flow_id"]
    if q==14: return match("network/dns.csv",answer="198.51.100.24")["query"]
    if q==15:
        lines=(art/"linux/auth.log").read_text(encoding="utf-8").splitlines()
        matches=[line.split("exe=",1)[1].split(" ",1)[0] for line in lines if "EXECVE exe=" in line]
        assert len(matches)==1
        return matches[0]
    if q==16: return match("scheduler/job_baseline.csv",scope="weekly restore verification")["job_id"]
    if q==17: return match("change_control/approvals.csv",request="CHG-2408")["scope"]
    if q==18: return match("storage/file_metadata.csv",file="catalog/current.json")["record"]
    if q==19: return match("recovery/recovery_safety.csv",mode="in-place-overwrite",requires_preservation="YES")["operation_id"]
    if q==20: return match("identity/signins.csv",user="mara.ellis",result="SUCCESS")["utc"]
    raise ValueError(q)
for index,item in enumerate(bank,1):
    assert item["id"]==f"Q{index:02}",item["id"]
    for field in ("primary_artifact","cross_check"):
        assert (art/item[field]).is_file(),(item["id"],field)
    actual=answer(index)
    assert actual==item["answer"],f"{item['id']}: expected {item['answer']}, actual {actual}"
print("PASS: all 20 canonical answers reproduced from synthetic evidence")
