# EchoTrace 2 — Instructor answer key (DO NOT DISTRIBUTE)

The answers below are synthetic case facts, not proof of a real compromise. Account correlation is not physical attribution. A dry-run PASS is not a validated production recovery.

### Q01

**Question:** What UTC timestamp records the catalog write on BKP-CTRL-01?

**Answer:** `2026-09-22T02:07:19Z`

**Primary:** `windows/security_events.csv`; **cross-check:** `storage/file_metadata.csv`.

**Basis:** 4663 WRITE record on backup controller.

### Q02

**Question:** Which account is recorded on the catalog WRITE event?

**Answer:** `mara.ellis`

**Primary:** `windows/security_events.csv`; **cross-check:** `identity/signins.csv`.

**Basis:** Account in the unique catalog WRITE row.

### Q03

**Question:** Which workstation is associated with the recorded interactive sign-in of that account?

**Answer:** `OPS-WS-07`

**Primary:** `identity/signins.csv`; **cross-check:** `windows/security_events.csv`.

**Basis:** Unique interactive sign-in host; does not establish physical operator.

### Q04

**Question:** Which Windows event ID is recorded for the successful interactive sign-in?

**Answer:** `4624`

**Primary:** `windows/security_events.csv`; **cross-check:** `identity/signins.csv`.

**Basis:** Event ID on OPS-WS-07 interactive logon.

### Q05

**Question:** Which change request is cited for snapshot SNAP-0922-X in the recovery catalog?

**Answer:** `CHG-2408`

**Primary:** `recovery/catalog.csv`; **cross-check:** `change_control/approvals.csv`.

**Basis:** Approval field on snapshot row.

### Q06

**Question:** Which change request explicitly rejected catalog replacement?

**Answer:** `CHG-2411`

**Primary:** `change_control/approvals.csv`; **cross-check:** `case_context.txt`.

**Basis:** Rejected change with catalog replacement scope.

### Q07

**Question:** Which snapshot is marked VERIFIED in the catalog but absent from the immutable inventory?

**Answer:** `SNAP-0922-X`

**Primary:** `recovery/catalog.csv`; **cross-check:** `recovery/immutable_inventory.csv`.

**Basis:** Set difference restricted to VERIFIED snapshots.

### Q08

**Question:** Which ledger snapshot has a PASS in both immutable inventory and restore dry run?

**Answer:** `SNAP-0919-A`

**Primary:** `recovery/immutable_inventory.csv`; **cross-check:** `recovery/restore_dry_run.csv`.

**Basis:** Intersection of two PASS records.

### Q09

**Question:** Which snapshot has MISSING_OBJECT in object integrity checks?

**Answer:** `SNAP-0922-X`

**Primary:** `recovery/object_integrity_checks.csv`; **cross-check:** `recovery/object_chunks.json`.

**Basis:** Exact status row.

### Q10

**Question:** Which dataset is associated with the successful isolated restore dry run?

**Answer:** `ledger`

**Primary:** `recovery/restore_dry_run.csv`; **cross-check:** `recovery/catalog.csv`.

**Basis:** Dataset on unique PASS dry run.

### Q11

**Question:** Which dataset has a failed restore dry run due to a missing chunk?

**Answer:** `hr`

**Primary:** `recovery/restore_dry_run.csv`; **cross-check:** `recovery/immutable_inventory.csv`.

**Basis:** Exact detail chunk missing.

### Q12

**Question:** What is the observed clock offset in seconds for OPS-WS-07?

**Answer:** `30`

**Primary:** `time/clock_reference.csv`; **cross-check:** `time/README.txt`.

**Basis:** offset_seconds observed minus trusted.

### Q13

**Question:** What is the flow ID for the HTTPS connection from 192.0.2.47 to 198.51.100.24?

**Answer:** `FLOW-1201`

**Primary:** `network/flows.csv`; **cross-check:** `network/proxy_observations.csv`.

**Basis:** Unique matching flow tuple; does not prove payload.

### Q14

**Question:** Which DNS name resolved to 198.51.100.24 immediately before that HTTPS flow?

**Answer:** `catalog-sync.example`

**Primary:** `network/dns.csv`; **cross-check:** `network/flows.csv`.

**Basis:** DNS row preceding flow timestamp.

### Q15

**Question:** Which Linux executable appears in the restore verification audit EXECVE record?

**Answer:** `/usr/local/bin/verify_restore`

**Primary:** `linux/auth.log`; **cross-check:** `recovery/restore_dry_run.csv`.

**Basis:** Executable in EXECVE line; no proof of process ancestry.

### Q16

**Question:** What is the scheduled job ID for weekly restore verification?

**Answer:** `JOB-014`

**Primary:** `scheduler/job_baseline.csv`; **cross-check:** `change_control/approvals.csv`.

**Basis:** Unique baseline job.

### Q17

**Question:** What scope was authorized under CHG-2408?

**Answer:** `weekly restore verification`

**Primary:** `change_control/approvals.csv`; **cross-check:** `scheduler/job_baseline.csv`.

**Basis:** Exact approved scope; catalog replacement not included.

### Q18

**Question:** What file record identifier is listed for catalog/current.json?

**Answer:** `MFT-3344`

**Primary:** `storage/file_metadata.csv`; **cross-check:** `windows/security_events.csv`.

**Basis:** Metadata record identifier; does not prove substitution alone.

### Q19

**Question:** Which recovery operation is identified as risking in-place overwrite of original catalog evidence?

**Answer:** `RESTORE-INPLACE-01`

**Primary:** `recovery/recovery_safety.csv`; **cross-check:** `storage/file_metadata.csv`.

**Basis:** Operation with requires_preservation YES.

### Q20

**Question:** At what UTC timestamp does the synthetic record show the successful interactive sign-in of mara.ellis?

**Answer:** `2026-09-22T02:03:04Z`

**Primary:** `identity/signins.csv`; **cross-check:** `windows/security_events.csv`.

**Basis:** Exact sign-in timestamp, not inferred incident start.
