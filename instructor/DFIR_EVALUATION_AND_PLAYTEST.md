# EchoTrace 2 — DFIR Instructor Evaluation and Blind Playtest

**Scope:** fictional, authorized training only. This document is an evaluation rubric, not a claim of HTB acceptance or an Insane certification.

## Evidence-backed investigation
1. Verify SHA-256 manifest and each evidence file before analysis.
2. Correlate Windows 4663 catalog WRITE with identity sign-in by account and session; distinguish account identity from physical attribution.
3. Normalize workstation timestamps using the observed +30-second offset; explain why an offset measured at one point may not generalize to all logs.
4. Compare CHG-2408 scope against the catalog change and rejected CHG-2411. Distinguish missing authorization evidence from proof of intent.
5. Compute VERIFIED catalog snapshots minus immutable inventory entries, then corroborate with object integrity checks and restore dry runs.
6. Reconcile catalog chunk claims with object verification, and identify the safer isolated restore candidate.
7. Correlate DNS resolution, flow tuple and TLS SNI; explain why encrypted body invisibility prevents an exfiltration conclusion.
8. Identify the Linux verification executable and scheduled-job baseline without inferring process ancestry.
9. Explain evidence-preservation risks of in-place restore.
10. Produce a timeline with provenance and confidence per event, including uncertainty.

## Scoring rubric (100 points)
- Evidence integrity and chain-of-custody explanation: 15
- Identity/session and timestamp correlation: 15
- Approval scope and alternative hypotheses: 15
- Immutable inventory and restore consistency: 20
- Network and Linux artifact correlation: 15
- Safe recovery decision and evidence preservation: 10
- Uncertainty, negative findings and reproducible citations: 10

## Independent blind-playtest protocol
- Give an analyst only the student questions and student evidence, never the answer key.
- Record time-to-solve, wrong-answer count, ambiguous questions and hints used.
- Require an evidence citation for each of the 20 answers.
- Require an independent instructor to confirm every answer from source artifacts.
- Fail the release gate if any question is ambiguous, an answer is disclosed, or any artifact is missing.
- Rate difficulty from observed playtest performance, not from the number of questions or the repository label.

## Known release gaps
- Synthetic CSV/text/JSON exports, not native EVTX, PCAP or disk images.
- No independent blind playtest recorded.
- No verified live VM boot or remote CI success in this document.
- No demonstrated HTB reviewer-accessible student and private writeup links.

**Verdict:** The current package is a reproducible synthetic DFIR exercise. Its Insane rating is a proposal, not an independently established difficulty.
