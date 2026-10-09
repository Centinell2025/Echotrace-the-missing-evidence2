# Advanced forensic architecture — Episode 2

## Continuity and threat model
Use the fictional enterprise from EchoTrace Episode 1. This sequel examines a potentially substituted recovery catalog after the outage. An investigator must separate observation, inference and speculation. No real organization is a victim.

## Evidence layers and required proof
1. Endpoint: native EVTX generated in an isolated Windows VM, Sysmon configuration/version recorded, Registry hives, Prefetch if available. Export source hashes and record IDs.
2. Linux: journald export with boot IDs, auditd records and file timestamps. Record timezone and any NTP offsets.
3. Network: PCAP generated in an isolated network using documentation IPs; DNS and TLS metadata only; no live exfiltration.
4. Identity: fictional directory sign-in, group membership, service principals and approvals.
5. Backup: immutable snapshot index, catalog metadata, object manifests, dry-run restore output and checksum validation.
6. Chain of custody: original SHA-256, acquisition method, custodian, UTC time, tool version, derivation hash and evidence IDs.

## Adversarial ambiguity
- Catalog claims SNAP-0922-X is verified but immutable inventory does not list it.
- An approval is genuine yet applies only to routine verification, not replacement.
- Service account activity overlaps with a human interactive session.
- A plausible DNS lookup is not by itself evidence of data exfiltration.
- Missing backup chunks prove that a given dry run failed, not that all data is permanently lost.
- High-frequency operations do not establish AI assistance.

## Hard-mode design constraints
- At least two independent sources for each pivotal inference.
- One calibrated false lead, resolvable without guessing.
- Timeline clock offset must be derived from independent synchronization evidence.
- Student-facing questions must avoid claims stronger than the artifacts support.
- Native formats must be validated with external parsers, not merely renamed CSVs.
- Never ship real secrets, active malware, customer records or public answer keys.

## Milestones
M1 deterministic synthetic dataset and validation; M2 native evidence exports; M3 complete answer-unique question bank; M4 walkthrough and blind playtest; M5 packaging and HTB submission review.
