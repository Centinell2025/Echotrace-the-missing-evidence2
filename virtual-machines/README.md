# EchoTrace 2 — Isolated VM laboratory
All guest identities and network assets are fictional. VM images are NOT included; this directory provides build and acquisition specifications. Never publish preconfigured credentials or licensed operating-system images.

## Suggested topology
| VM | OS | vCPU | RAM | Role |
|---|---|---:|---:|---|
| ANALYST-KALI | Kali Linux | 2 | 4 GiB | Autopsy, Volatility 3, tshark, timeline |
| OPS-WS-07 | Windows 11 evaluation/licensed | 2 | 4 GiB | endpoint telemetry |
| BKP-CTRL-01 | Windows Server evaluation/licensed | 2 | 4 GiB | identity and backup |
| RESTORE-NODE | Ubuntu Server 24.04 LTS | 2 | 2 GiB | restore and audit |
| SENSOR-01 | Security Onion (optional, hardware intensive) | per vendor | per vendor | Zeek/Suricata network visibility |

## Isolation
Use an **internal-only virtual switch** with no bridge, NAT, host-shared clipboard or folders during scenario execution. Configure documentation-only addresses (192.0.2.0/24) on the isolated segment; do not route them. Do not download tools inside the isolated network. Acquire approved installers before isolation and verify signatures. Take clean snapshots before importing synthetic data. Never reuse real credentials.

## Workflow
1. Provision OS images under their respective licenses; record versions and hashes.
2. Install logging and forensic tooling from trusted offline media.
3. Capture clean VM snapshots and note snapshot IDs.
4. Generate the synthetic evidence with `python3 tools/generate_case.py`.
5. Import training records only in a disposable lab, never production.
6. Collect native EVTX, journal exports and PCAP after a scripted benign simulation; retain originals and derivation logs.
7. Hash acquisitions, record custody, and reset all VMs after the exercise.

## Scope limitations
The current case generator produces CSV/log training records, **not** bootable VMs, native EVTX, memory dumps or PCAP. Do not rename CSV to EVTX or claim a capture exists before it has been generated and verified.
