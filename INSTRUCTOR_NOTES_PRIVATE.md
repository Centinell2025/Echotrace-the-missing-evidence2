# Instructor Notes — Keep Private

This is a preliminary answer map for the **generated** synthetic evidence. Do not submit the 20-question draft unchanged: some proposed questions lack artifacts or uniquely defensible answers.

- First catalog write: 2026-09-22T02:07:19Z, windows/security_events.csv, event 4663.
- Account: mara.ellis; correlated session S-8852 and workstation OPS-WS-07.
- Suspicious advertised snapshot: SNAP-0922-X (catalog.csv), absent from immutable_inventory.csv.
- Known recoverable ledger snapshot: SNAP-0919-A (restore_dry_run.csv PASS).
- HR snapshot: SNAP-0919-B failed dry run; do not claim permanent loss from this evidence alone.
- Approval CHG-2408 only covers weekly verification, not catalog replacement; CHG-2411 is rejected.
- DNS: catalog-sync.example at 02:06:40Z; HTTPS flow at 02:06:51Z from 192.0.2.47.
- Linux verification command: /usr/local/bin/verify_restore, SNAP-0922-X.
- No evidence proving AI involvement.

The current CSV exports are educational simplifications, not genuine EVTX/PCAP. Upgrade the evidence before final submission and validate each question against the resulting files.
