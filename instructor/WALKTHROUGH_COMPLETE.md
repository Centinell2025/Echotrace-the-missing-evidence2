# Instructor walkthrough — EchoTrace 2: The Phantom Restore

**Instructor-only. Synthetic evidence. Not a real-world incident or attribution report.**

## Preparation

Run in an isolated authorized environment:

```bash
python3 tools/generate_case.py
python3 tools/verify_case.py
python3 tools/validate_backup_consistency.py
python3 tools/validate_questions.py
python3 tools/verify_answers.py
sha256sum build/artifacts.zip
```

The generator creates the synthetic student evidence ZIP. Never add this instructor document, the answer key, or `validated_questions.json` to the student archive.

## Investigation sequence

1. Read `case_context.txt` and `EDUCATIONAL_USE_NOTICE.txt`. Record the synthetic nature of every source.
2. Examine `identity/signins.csv` and `windows/security_events.csv`. Identify the interactive sign-in at 02:03:04Z and catalog WRITE at 02:07:19Z. Do **not** conclude that the named person was physically present.
3. Read `time/clock_reference.csv`. OPS-WS-07 has a measured +30-second offset in the synthetic reference; BKP-CTRL-01 has zero. Normalize timestamps only when the source clock is known. The exercise does not prove that every exported event was raw host time.
4. Inspect `change_control/approvals.csv`: CHG-2408 authorizes weekly restore verification; CHG-2411 rejects catalog replacement.
5. Compare `recovery/catalog.csv` and `recovery/immutable_inventory.csv`. SNAP-0922-X is catalogued VERIFIED but has no immutable inventory entry.
6. Compare `recovery/object_integrity_checks.csv`, `recovery/object_chunks.json`, `recovery/catalog_chunk_claims.csv`, and `recovery/restore_dry_run.csv`. SNAP-0919-A is the only ledger candidate with recorded PASS outcomes; SNAP-0922-X is missing. This is a synthetic dry-run, **not** a completed real restore.
7. Correlate `network/dns.csv`, `network/flows.csv` and `network/proxy_observations.csv`. FLOW-1201 follows a DNS resolution; the TLS body is not visible. Do not assert payload contents or exfiltration.
8. Inspect `linux/auth.log` for the SSH session and `/usr/local/bin/verify_restore` EXECVE. Do not infer process ancestry or authorization solely from this summary log.
9. Check `scheduler/job_baseline.csv` to distinguish the weekly benign baseline from the separate catalog WRITE.
10. Review `storage/file_metadata.csv` and `recovery/recovery_safety.csv`. Preserve the original before any in-place overwrite.

## Scoring and defensible conclusions

Use `instructor/ANSWER_KEY_FINAL.md` for 20 canonical answers. Each answer must be reproduced by `tools/verify_answers.py` before distribution. Require learners to cite the exact source and explain limitations.

**Supported:** discrepancy between catalog and independent inventory; failed synthetic dry run for SNAP-0922-X; successful synthetic dry run for SNAP-0919-A; insufficient authorization scope for catalog replacement.

**Not supported:** identification of the physical actor; proof of malicious intent; confirmed data exfiltration; AI involvement; full production recovery; verified native forensic provenance.

## Release constraints

The case is educational and fictional. Native EVTX, PCAP, VM images and a documented blind playtest are not yet available. This walkthrough is a Markdown instructor procedure, not a finished PDF.
