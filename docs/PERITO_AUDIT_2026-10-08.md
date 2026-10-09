# Independent-style desk audit — 2026-10-08
Status: DOCUMENT REVIEW ONLY. Not an independent certification, external pentest or forensic validation.

## Reviewed
README.md, SIMULATION_NOTICE.md, DESIGN_SPEC.md, tools/generate_case.py, tools/verify_case.py, questions/DRAFT_QUESTIONS.md, .github/workflows/forensic-integrity.yml.

## Findings and remediation
**CRITICAL — Answerability:** Draft Q09/Q12/Q16/Q17/Q18/Q19/Q20 lack complete supporting evidence; Q01/Q03/Q08/Q11/Q13 overstate or under-specify proof. BLOCK submission until each is uniquely answerable and independently checked.
**HIGH — Native authenticity:** CSV security event summaries are not EVTX; network flow summaries are not PCAP. Obtain native isolated-lab acquisitions and test parser compatibility.
**HIGH — Evidence leakage:** network/flows.csv includes a 'purpose' field containing 'catalog-upload', making inference trivial. Replace with observed network attributes; retain interpretation in private key only.
**HIGH — Timeline:** proposed clock-offset question has no NTP or clock-reference artifact. Provide measurable offset evidence and normalization.
**HIGH — Integrity:** generator creates hashes, but no documented immutable original acquisition, custodian signature, or independently verified restore operation.
**MEDIUM — Continuity:** canonical fictional names and infrastructure from Episode 1 remain unverified.
**MEDIUM — Reproducibility:** GitHub Actions workflow is configured, but this desk review did not inspect a successful run; deterministic zip check needs an observed passing run.
**MEDIUM — Student separation:** answers exist in private repository; construct explicit student-only distribution without instructor files.
**MEDIUM — Scope:** virtual machines are specifications only, not provisioned appliances or images.

## Required release gates
1. Build and verify all artifacts; archive integrity and SHA-256 confirmed.
2. Produce native EVTX/PCAP/journal captures where promised, with tool versions.
3. Verify exact answers to 20 questions with independent sources and commands.
4. Separate student and instructor deliverables and inspect archive for answer leaks.
5. Confirm scenario continuity and educational disclaimer.
6. Run independent blind playtest and fix ambiguities.
7. Check current HTB Sherlock submission schema and restrictions before submission.

No readiness score or valuation is claimed from this document.
