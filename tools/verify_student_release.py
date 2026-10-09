#!/usr/bin/env python3
"""Verify the student ZIP, checksums, and absence of instructor-only materials."""
from pathlib import Path
import hashlib, io, json, zipfile

root=Path(__file__).resolve().parents[1]
package=root/"build"/"EchoTrace2_STUDENT_RELEASE.zip"
assert package.is_file(), "Student release not built"
with zipfile.ZipFile(package) as outer:
    names=outer.namelist()
    assert len(names)==len(set(names)), "Duplicate archive members"
    expected={"artifacts.zip","evidence_manifest.json","STUDENT_QUESTIONS.md","EDUCATIONAL_USE_AND_ETHICS.md","SHA256SUMS.txt"}
    assert set(names)==expected,(names,expected)
    assert all(not n.startswith("/") and ".." not in Path(n).parts for n in names)
    sums={}
    for line in outer.read("SHA256SUMS.txt").decode("utf-8").splitlines():
        digest,name=line.split("  ",1)
        assert name not in sums
        sums[name]=digest
    assert set(sums)==expected-{"SHA256SUMS.txt"}
    for name,digest in sums.items():
        assert hashlib.sha256(outer.read(name)).hexdigest()==digest,name
    assert b"EXCLUSIV" in outer.read("EDUCATIONAL_USE_AND_ETHICS.md").upper() or b"EDUCATIONAL" in outer.read("EDUCATIONAL_USE_AND_ETHICS.md").upper()
    questions=outer.read("STUDENT_QUESTIONS.md").decode("utf-8")
    assert questions.count("**Q")==20, "Student question count differs"
    manifest=json.loads(outer.read("evidence_manifest.json"))
    with zipfile.ZipFile(io.BytesIO(outer.read("artifacts.zip"))) as inner:
        evidence=inner.namelist()
        assert len(evidence)==len(set(evidence))
        assert set(evidence)==set(manifest["files"])
        assert "EDUCATIONAL_USE_NOTICE.txt" in evidence
        for name,meta in manifest["files"].items():
            data=inner.read(name)
            assert len(data)==meta["bytes"],name
            assert hashlib.sha256(data).hexdigest()==meta["sha256"],name
        assert not any("answer" in n.lower() or "instructor" in n.lower() or "walkthrough" in n.lower() for n in evidence)
    assert not any(x in questions for x in ("SNAP-0919-A","MFT-3344","RESTORE-INPLACE-01","JOB-014")), "Possible answer disclosure in student questions"
print("PASS: student release structure, 20 questions, checksums, nested evidence integrity and instructor separation")
