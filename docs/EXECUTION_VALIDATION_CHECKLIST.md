# Execution validation and release gate

Execute from the repository root in a trusted Python 3.12 environment:

```bash
python tools/generate_case.py
python tools/verify_case.py
python tools/validate_backup_consistency.py
python tools/validate_questions.py
python tools/verify_answers.py
python tools/build_student_release.py
python tools/check_release.py
```

Expected: first six commands must exit 0. The final release gate is **expected to fail** until the final PDF, native artifact validation, and blind playtest exist. Record stdout, exit codes, Python version and archive SHA-256. Do not write PASS without captured output.

## Independent quality gates
- Evidence manifest verifies all members of the inner ZIP.
- 20 canonical answers are reproduced against evidence.
- No instructor answers or instructor-only paths are in the student package.
- Native EVTX/PCAP claims require real captures and parser results.
- Windows VMs require legitimate guest images; Vagrant Ubuntu starter is not equivalent.
- Blind playtest requires another analyst's independent signed findings.
- Educational notice must be present in each student release.
