# Forensic analysis playbook — Instructor / investigator
All timestamps in UTC unless a source explicitly documents an offset.

## 1. Preservation
Record evidence ID, collector, acquisition UTC, source host, acquisition tool/version, source SHA-256 and derived artifact SHA-256. Work from read-only copies. Compare against `build/evidence_manifest.json`.

## 2. Identity and endpoint
Correlate `identity/signins.csv` with `windows/security_events.csv` using session, host, account and UTC. Treat an event 4663 in the training export as a **simulated** file write. For native EVTX later, verify the event provider and audit configuration.

## 3. Recovery integrity
Compare `recovery/catalog.csv` against `recovery/immutable_inventory.csv`. For each snapshot, check object existence and `recovery/restore_dry_run.csv` result. A failed test is not proof of irrecoverable loss.

## 4. Linux
Parse `linux/auth.log`; correlate accepted SSH, systemd unit start and verification process. Confirm command and session before attributing action to a human.

## 5. Network
Correlate `network/dns.csv` and `network/flows.csv` by client, destination and timestamp. These are synthetic flow summaries, **not PCAP**. DNS plus HTTPS metadata does not prove content exfiltration.

## 6. Reporting
Separate Observed / Inferred / Unproven statements. Document confidence and contradictory records. Never assert AI involvement without supporting artifacts.

## 7. Suggested commands
```bash
python3 tools/generate_case.py
python3 tools/verify_case.py
sha256sum build/artifacts.zip
unzip -l build/artifacts.zip
```
For future native files: `tshark -r evidence.pcapng`, `evtx_dump evidence.evtx`, `journalctl --file=journalfile` as appropriate to format and installed tool.
