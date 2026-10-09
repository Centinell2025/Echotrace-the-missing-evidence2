#!/usr/bin/env python3
"""Build HTB password-protected ZIP containing only the verified student release."""
from pathlib import Path
import hashlib
import subprocess
import sys
root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(root/"tools"/"build_student_release.py")],cwd=root,check=True)
subprocess.run([sys.executable,str(root/"tools"/"verify_student_release.py")],cwd=root,check=True)
try:
    import pyzipper
except ImportError as exc:
    raise SystemExit("Install dependency: python -m pip install pyzipper") from exc
source=root/"build"/"EchoTrace2_STUDENT_RELEASE.zip"
target=root/"build"/"EchoTrace2_HTB_hackthebox.zip"
with pyzipper.AESZipFile(target,"w",compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES) as z:
    z.setpassword(b"hackthebox")
    z.setencryption(pyzipper.WZ_AES,nbits=256)
    z.write(source,arcname=source.name)
with pyzipper.AESZipFile(target) as z:
    z.setpassword(b"hackthebox")
    assert z.namelist()==[source.name], "Unexpected contents"
    assert z.read(source.name)==source.read_bytes(), "Password-protected ZIP mismatch"
print("PASS: HTB encrypted ZIP built and decrypted successfully")
print("File:",target)
print("SHA256:",hashlib.sha256(target.read_bytes()).hexdigest())
print("NOTE: This confirms ZIP encryption and contents, not HTB approval.")
