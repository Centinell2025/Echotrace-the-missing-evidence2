# VM deployment and validation — educational isolated lab

These are reproducible **VM definitions**, not exported VM images or proof of successful boot.

## Prerequisites
- Host with VirtualBox and Vagrant installed; virtualization enabled
- Minimum 8 GB RAM available for the two Ubuntu guests, plus host overhead
- Internet may be needed initially to download Ubuntu box images; do not connect guest services to real targets
- No Windows VM is provisioned. OPS-WS-07 and BKP-CTRL-01 are fictional evidence hosts; native Windows acquisition needs licensed guest images and separately documented setup

## Commands
```bash
cd virtual-machines
vagrant validate
vagrant up
vagrant status
vagrant ssh analyst -c 'cat /opt/echotrace2/NOTICE.txt'
vagrant ssh restore-node -c 'cat /opt/echotrace2/NOTICE.txt'
vagrant halt
```

Private-network addresses are lab deployment addresses, **not** the synthetic documentation addresses (192.0.2.0/24) in case records. No assumption of routing between these networks.

## Security boundaries
No host bridged adapters. Avoid placing sensitive host files in shared folders. This starter uses a standard private network, **not an air gap**: Vagrant guests may retain NAT for box provisioning. For strict isolation, disable NAT and shared folders after provisioning using hypervisor controls and verify with `ip route` and `ip addr`.

## Verification evidence required
Record host hypervisor/version, guest image digest, command outputs, timestamp, snapshot names, VM export hashes, and analyst signature before asserting PASS. No such execution is claimed by this repository.
