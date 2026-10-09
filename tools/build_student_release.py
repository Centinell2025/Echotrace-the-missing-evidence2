#!/usr/bin/env python3
"""Create isolated synthetic student package after reproducible validation."""
from pathlib import Path
import hashlib, shutil, subprocess, sys, zipfile
root=Path(__file__).resolve().parents[1]
for name in ("generate_case.py","verify_case.py","validate_backup_consistency.py","validate_questions.py","verify_answers.py"):
    subprocess.run([sys.executable,str(root/"tools"/name)],cwd=root,check=True)
out=root/"build"
student=out/"student"
if student.exists(): shutil.rmtree(student)
student.mkdir(parents=True)
shutil.copy2(out/"artifacts.zip",student/"artifacts.zip")
shutil.copy2(out/"evidence_manifest.json",student/"evidence_manifest.json")
shutil.copy2(root/"questions"/"STUDENT_QUESTIONS.md",student/"STUDENT_QUESTIONS.md")
shutil.copy2(root/"EDUCATIONAL_USE_AND_ETHICS.md",student/"EDUCATIONAL_USE_AND_ETHICS.md")
for p in student.iterdir():
    assert p.is_file()
    assert not any(word in p.name.lower() for word in ("answer","instructor","walkthrough","validated_questions"))
lines=[f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in sorted(student.iterdir())]
(student/"SHA256SUMS.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")
release=out/"EchoTrace2_STUDENT_RELEASE.zip"
with zipfile.ZipFile(release,"w") as z:
    for p in sorted(student.iterdir()):
        info=zipfile.ZipInfo(p.name,(2026,9,22,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o644<<16
        z.writestr(info,p.read_bytes())
print(f"PASS: isolated student package created: {release}")
