<div align="center">
  <img src="https://raw.githubusercontent.com/Centinell2025/the-last-evidence-standing/main/branding/BEACON_SEAL.png" alt="Beacon of the Eagle LLC — logotipo corporativo" width="165" />
  <p><strong>BEACON OF THE EAGLE LLC</strong><br/><strong>CENTINELL SUITE DEFENSE</strong></p>
</div>

# EchoTrace 2 — The Phantom Restore

**Status:** Educational fictional DFIR Sherlock candidate. Not submitted, approved or published by Hack The Box.

## Scenario
Investigate a suspicious backup-catalog modification by correlating synthetic Windows security-event exports, Linux authentication records, identity sign-ins, DNS and network flow observations, immutable backup inventory, restore dry runs, clock references and change approvals.

All people, organizations, domains, hosts, IP addresses and incident events are fictional or synthetic. This is not a real-world incident report.

## Repository map
- [Student questions (20)](questions/STUDENT_QUESTIONS.md)
- [Synthetic evidence generator](tools/generate_case.py)
- [Evidence hash verifier](tools/verify_case.py)
- [Answer verifier](tools/verify_answers.py)
- [Instructor index — restricted access](instructor/HTB_REVIEWER_INDEX.md)
- [Virtual machine setup](virtual-machines/Vagrantfile)
- [Educational use and ethics](EDUCATIONAL_USE_AND_ETHICS.md)
- [Submission preparation](docs/HTB_SUBMISSION_FILES.md)

## Local checks
Run from the repository root:

```bash
python3 tools/generate_case.py
python3 tools/verify_case.py
python3 tools/validate_backup_consistency.py
python3 tools/validate_questions.py
python3 tools/verify_answers.py
```

These scripts generate evidence in `build/artifacts/` and verify integrity and 20 canonical answers. Student evidence must not include instructor solutions. GitHub Actions workflow configuration exists, but a passing remote workflow run must be independently verified.

## Release limitations
The current evidence is synthetic CSV, text and JSON, not native EVTX, PCAP or full disk images. VM boot tests, independent blind playtesting, reviewer download accessibility and the claimed Insane difficulty remain unverified. The HTB submission form may require a password-protected ZIP for student distribution; the source repository itself remains uncompressed.

**Do not publish instructor answers or private walkthroughs in a public repository.**


---
**Ethical and educational use / Uso ético y educativo:** This is a fictional or simulated defensive cybersecurity training exercise. Test only systems you own or are explicitly authorized to assess. / Ejercicio de ciberseguridad defensiva ficticio o simulado. Realice pruebas solo en sistemas propios o con autorización expresa. See / Consulte [Educational Purpose Notice](EDUCATIONAL_PURPOSE_NOTICE.md).
