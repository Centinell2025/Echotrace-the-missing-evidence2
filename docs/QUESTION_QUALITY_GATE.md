# Question quality gate

For each final Sherlock question, record:
- Question ID, objective, difficulty and points.
- Exact artifact name and location (row, record ID, packet number or byte offset).
- Reproduction command and parser/tool version.
- Canonical answer and normalization rules.
- Independent cross-check artifact.
- Uniqueness proof: why alternative answers are incorrect.
- Whether an answer can be found by filename/grep alone (if so, improve reasoning).
- Blind tester result, time-to-solve, hints required and ambiguity notes.

**Release blockers:** nonexistent artifacts, fake native file formats, unverified hashes, questions requiring unstated assumptions, answer leaks, inconsistent timestamps, untested parsers, real personal data, or a public walkthrough.

## Proposed scoring (subject to HTB format verification)
Foundation 5 questions; cross-source correlation 7; recovery engineering 5; executive evidence judgment 3. Final points and proof format must follow the current platform schema.
