# HTB Sherlock submission — file preparation

**EXCLUSIVAMENTE CON FINES EDUCATIVOS.** All persons, organizations and records in this scenario are fictional.

The HTB submission form requests **a ZIP download with password `hackthebox`** and a **Markdown writeup accessible to reviewers without exposing the answers to participants**.

## Create the encrypted student ZIP

From the repository root:

```bash
python3 -m pip install pyzipper
python3 tools/build_htb_submission.py
```

This runs the generator, validates the synthetic evidence and all 20 answers, checks the isolated student package, creates `build/EchoTrace2_HTB_hackthebox.zip` and verifies decryption using `hackthebox`. It does not include instructor answers. Confirm the printed SHA256 and archive content.

## Prepare the writeup

Use `instructor/WALKTHROUGH_COMPLETE.md` as the instructor procedure. Supplement it with `instructor/ANSWER_KEY_FINAL.md` for the 20 canonical answers **inside a reviewer-only copy**. Do not use README.md as the writeup and do not put instructor material in the student ZIP.

## Links to paste into the form

**Sherlock Download:** a direct HTTPS download URL for the generated `EchoTrace2_HTB_hackthebox.zip` (not the repository home page).

**Writeup Download:** a reviewer-accessible direct URL to a Markdown writeup containing the full solution (not the repository README).

A private GitHub repository's `blob/main` links are not necessarily accessible to HTB reviewers. Share files using a provider that supports restricted, reviewer-accessible download links and verify both links in a logged-out browser session before submitting. Do not make instructor answers public.

**Status:** Build script committed, but successful local execution, upload, link accessibility, blind playtest and HTB acceptance are not yet confirmed.
