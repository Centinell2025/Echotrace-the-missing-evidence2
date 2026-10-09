# EchoTrace Episode 2 — The Phantom Restore

**Internal development specification — not an accepted HTB submission.**

## Canonical continuity
Episode 1: catastrophic outage; identity, application, storage and backup failures; inconsistent restore catalogs; uncertain automation versus AI involvement. Episode 2 follows the **same unnamed fictional enterprise** and must reuse any canonical names only after they are confirmed from Episode 1's evidence. Never present Beacon of the Eagle LLC / Centinell Suite Defense as the victim organization.

## Case premise
During post-outage recovery, an apparently valid restore point is discovered. Independent telemetry suggests a substituted backup catalog, altered timestamps, and a misleading recovery authorization. Investigators must distinguish genuine recovery data from planted metadata and explain what can be safely recovered.

## Learning outcomes
1. Reconstruct a multi-source UTC timeline with clock drift.
2. Correlate Windows events, Linux audit/auth logs, DNS/HTTP and backup catalogs.
3. Verify chain-of-custody and cryptographic hashes.
4. Identify recovery-point inconsistencies using manifest and object metadata.
5. Differentiate legitimate scheduled automation from unauthorized action; avoid unsupported claims of AI attribution.
6. Recommend evidence-preserving recovery actions.

## Evidence plan (all synthetic)
- Windows: sanitized EVTX exports and registry timeline, with independently verifiable event IDs.
- Linux: auth.log, journal export and file metadata.
- Network: compact PCAP with documentation-only addresses.
- Recovery: snapshot inventory, backup manifest, chunk hashes, restore dry-run logs.
- Identity: simulated authentication audit and change approval records.
- Integrity: SHA-256 manifest, provenance and timestamp normalization guide.

## Validation gates
- Every question must cite at least one real artifact and exact field or offset.
- Answer uniqueness tested; no guessing based on story prose.
- PCAP must open in Wireshark/tshark; exports parse with standard tools.
- Reproducible artifact generation and deterministic checksums.
- Zero real PII, real credentials, malware, or active infrastructure.
- Independent blind playtest before HTB submission.

## Scope / valuation
Internal hypothetical production-value target: USD 5,000, not an appraisal or HTB payout. The USD 800 bounty tier is unverified for this specific submission.
