# PRIVATE — EchoTrace 2 preliminary answer key
DO NOT PUBLISH. These are only answers grounded in the initial **synthetic CSV generator**, not the final HTB question bank.

| ID | Preliminary answer | Evidence |
|---|---|---|
| Q01 | 2026-09-22T02:07:19Z (first **recorded** catalog write) | windows/security_events.csv, event 4663 |
| Q02 | mara.ellis | windows/security_events.csv |
| Q03 | OPS-WS-07 (session correlation; not direct proof of physical operator) | identity/signins.csv and windows/security_events.csv |
| Q04 | 4624, session S-8852 | identity/signins.csv |
| Q05 | CHG-2408 | recovery/catalog.csv |
| Q06 | CHG-2408 authorizes weekly verification only; CHG-2411 catalog replacement rejected | change_control/approvals.csv |
| Q07 | SNAP-0922-X | recovery/catalog.csv |
| Q08 | SNAP-0919-A is verified in immutable inventory; SNAP-0922-X absent | recovery/immutable_inventory.csv |
| Q10 | ledger via SNAP-0919-A (isolated dry-run PASS only) | recovery/restore_dry_run.csv |
| Q11 | hr via SNAP-0919-B failed dry-run; cannot prove no other copy exists | recovery/restore_dry_run.csv |
| Q13 | 192.0.2.47 -> 198.51.100.24 TCP/443 at 02:06:51Z | network/flows.csv |
| Q14 | catalog-sync.example | network/dns.csv |
| Q15 | /usr/local/bin/verify_restore --snapshot SNAP-0922-X | linux/auth.log |

**Not yet answerable as drafted:** Q09, Q12, Q16, Q17, Q18, Q19, Q20 require additional or stronger evidence. Q01, Q03, Q08, Q11, Q13 need precise wording. Never invent missing answers. Final key must map all 20 validated questions with artifact offsets, commands and independent checks.
