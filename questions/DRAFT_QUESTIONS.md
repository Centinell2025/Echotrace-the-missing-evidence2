# Instructor Draft — 20 Evidence-Grounded Questions

**Not ready for publication.** Each question below is a design target. Do not create static answers until corresponding evidence is generated and verified.

1. What UTC time was the first unauthorized recovery-catalog modification?
2. Which identity initiated the catalog modification?
3. Which workstation originated that session?
4. What log event proves successful authentication?
5. What approval record was referenced by the restore job?
6. Which independent record contradicts that approval?
7. What backup snapshot ID was advertised as valid?
8. Which snapshot ID is supported by the immutable inventory?
9. Which chunk hash differs between the catalog and object manifest?
10. Which data set has a provably recoverable copy?
11. Which data set has no validated restore point?
12. What is the observed clock offset between two hosts?
13. Which network flow corresponds to catalog upload?
14. Which DNS query precedes that upload?
15. Which Linux process launched the restore validation?
16. What scheduled job is the benign automation baseline?
17. Which action cannot be explained by that baseline?
18. Which file metadata establishes catalog substitution?
19. Which recovery operation would overwrite relevant evidence?
20. What is the earliest defensible incident time in normalized UTC?

Every final question requires: artifact filename, parsing command, expected answer, uniqueness proof, and scoring rubric.
