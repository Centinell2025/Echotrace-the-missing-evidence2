# Balanced virtual-machine resource plan

**EXCLUSIVELY FOR EDUCATIONAL USE.** These are capacity recommendations, not proof of booted VMs.

## Implemented Vagrant starter (Ubuntu)
| Guest | vCPU | RAM | Disk recommendation | Role |
|---|---:|---:|---:|---|
| ANALYST | 2 | 3072 MiB | 35 GiB | Evidence inspection, Python validation, timelines |
| RESTORE-NODE | 2 | 2048 MiB | 25 GiB | Isolated synthetic restore checks |

Total allocated guest RAM: **5120 MiB**. Provisioning requires additional host RAM, storage, and hypervisor overhead. The Vagrantfile currently sets CPU/RAM but does **not** enforce disk size.

## Planned Windows extension (not provisioned)
| Guest | vCPU | RAM | Disk recommendation | Role |
|---|---:|---:|---:|---|
| OPS-WS-07 (Windows 11) | 2 | 4096 MiB | 64 GiB or more | Synthetic workstation, event generation |
| BKP-CTRL-01 (Windows Server) | 2 | 4096 MiB | 60 GiB or more | Synthetic backup controller |

Windows guest RAM above is a *planning baseline*; adjust to supported Microsoft OS requirements and workload. Licensed installation media, guest images, and forensic acquisition procedures are not supplied. Do not claim native EVTX evidence from current CSV exports.

## Deployment profiles
- **Low-resource host (8 GiB physical RAM):** run only one Ubuntu guest at a time; stop it before starting the other. Avoid concurrent Windows VMs.
- **Standard host (16 GiB physical RAM):** run both Ubuntu guests together (5 GiB allocated), with host headroom. Run Windows guests individually when needed.
- **Extended host (32 GiB or more):** run four guests concurrently only after confirming host CPU capacity, storage, and OS requirements.

## Acceptance tests
1. `cd virtual-machines && vagrant validate`
2. `vagrant up analyst && vagrant ssh analyst -c 'free -m; nproc; ip route'`
3. `vagrant up restore-node && vagrant ssh restore-node -c 'free -m; nproc; ip route'`
4. `vagrant status`; verify expected guest resources in VirtualBox.
5. Verify isolated networking and absence of unintended host/third-party exposure.
6. Preserve command output, VM snapshot names and guest image hashes.

**Current status:** resource configuration committed; actual boot, guest commands, Windows images and VM exports are not verified.
