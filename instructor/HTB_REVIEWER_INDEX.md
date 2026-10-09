# EchoTrace 2 — Instructor reviewer index

**EXCLUSIVAMENTE CON FINES EDUCATIVOS.** The case is fictional and uses synthetic forensic evidence. This folder contains solutions; keep access restricted.

## Instructor documents
- [Complete investigation walkthrough](WALKTHROUGH_COMPLETE.md)
- [Answer key — 20 canonical answers](ANSWER_KEY_FINAL.md)
- [DFIR evaluation, scoring rubric and blind playtest](DFIR_EVALUATION_AND_PLAYTEST.md)

## Student-facing material (without solutions)
- [Student questions](../questions/STUDENT_QUESTIONS.md)
- [Synthetic evidence generator](../tools/generate_case.py)
- [Evidence integrity verifier](../tools/verify_case.py)
- [Answer reproducibility verifier](../tools/verify_answers.py)
- [Independent cross-source reasoning verifier](../tools/verify_cross_source_reasoning.py)
- [Student release validator](../tools/verify_student_release.py)
- [Ethics and fictional-case notice](../EDUCATIONAL_USE_AND_ETHICS.md)

## Review and release
1. Run `python3 tools/build_student_release.py` from the repository root.
2. Run `python3 tools/verify_student_release.py`.
3. Confirm all 20 answers using `python3 tools/verify_answers.py`.
4. Share student evidence separately from the instructor solutions.
5. Verify the reviewer can open the provided download links before submitting to HTB.

**Verification boundaries:** Repository file presence is confirmed; this index does not prove a CI PASS, booted virtual machines, independent blind playtest, or HTB acceptance. The generated student package is not stored as an archive in this GitHub repository.
