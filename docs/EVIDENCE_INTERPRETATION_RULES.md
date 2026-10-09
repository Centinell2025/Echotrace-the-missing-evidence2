# Expert evidence interpretation rules
1. **Clock offset:** Use trusted clock reference and record the sign of the offset; normalization is not arbitrary.
2. **Attribution:** Account/session correlation does not identify the physical human operating a host.
3. **Network:** A TLS flow and DNS query do not prove payload content or exfiltration. Do not infer it from labels.
4. **Backups:** Missing object or failed dry-run does not prove permanent data destruction.
5. **AI:** Coordinated timing is not proof of AI involvement.
6. **Metadata:** A changed mtime alone cannot prove malicious substitution; corroborate with security events and immutable inventory.
7. **SHA-256:** A file hash proves byte-level equality with a previously recorded digest, not that the contents are truthful.
8. **Educational limitation:** Synthetic CSV event summaries are not native forensic acquisitions.
