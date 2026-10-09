#!/usr/bin/env python3
"""Render instructor-only PDF from reviewed Markdown sources."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from xml.sax.saxutils import escape

root=Path(__file__).resolve().parents[1]
out=root/"build"/"instructor"
out.mkdir(parents=True,exist_ok=True)
target=out/"WALKTHROUGH_FINAL.pdf"
styles=getSampleStyleSheet()
story=[]
for name in ("WALKTHROUGH_COMPLETE.md","ANSWER_KEY_FINAL.md"):
    story.append(Paragraph(escape(name.replace("_"," ")),styles["Heading1"]))
    for line in (root/"instructor"/name).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            story.append(Spacer(1,7))
        elif line.startswith("#"):
            story.append(Paragraph(escape(line.lstrip("# ").strip()),styles["Heading2"]))
        else:
            story.append(Paragraph(escape(line).replace("  "," &nbsp;"),styles["BodyText"]))
doc=SimpleDocTemplate(str(target),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=48,bottomMargin=48)
doc.build(story)
assert target.is_file() and target.stat().st_size>1000
print("PASS: instructor PDF generated at",target)
