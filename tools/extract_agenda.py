#!/usr/bin/env python3
"""Extract a per-meeting agenda index from the tc39/notes corpus.

For every TC39 plenary meeting under raw/notes/meetings, this walks each day's
transcript, pulls out the level-2 agenda items (`## ...`), and for each item
captures:
  - the raw heading text
  - any stage signal found in the heading (e.g. "for Stage 2.7")
  - the `### Conclusion` block text, if present
  - stage signals found in the conclusion (e.g. "advances to stage 4")

The output is wiki/_generated/agenda-index.md: a compact, greppable backbone
spanning all meetings. It is mechanically generated -- do not hand-edit.
Proposal-name normalization and contention analysis are left to the curated
proposal pages under wiki/proposals/.

Usage:  python3 tools/extract_agenda.py
"""

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MEETINGS = ROOT / "raw" / "notes" / "meetings"
OUT_MD = ROOT / "wiki" / "_generated" / "agenda-index.md"
OUT_JSONL = ROOT / "wiki" / "_generated" / "agenda-index.jsonl"

# Headings that are committee boilerplate rather than proposal discussion.
BOILERPLATE = re.compile(
    r"^(opening|welcome|secretary'?s report|chair|ecma\s?\d|test262 status|"
    r"tg\d .*status|.*status update|coc committee|code of conduct|"
    r"approval of|adoption of|closing|housekeeping|introductions?|"
    r"agenda|next meeting|meeting notes|attendees|administrative)",
    re.IGNORECASE,
)

STAGE_RE = re.compile(r"stage\s+(\d(?:\.\d)?)", re.IGNORECASE)
# Stage transition verbs in a conclusion line.
ADVANCE_RE = re.compile(
    r"(advance[sd]?|advancing|promote[sd]?|move[sd]?\s+to|reach(?:e[sd])?|"
    r"approv(?:e[sd]?|al)|withdraw|reject|decline|block|demote[sd]?|stays?\s+at|"
    r"remain[s]?\s+at|did\s+not|no\s+consensus|conditional)",
    re.IGNORECASE,
)


def parse_day(text):
    """Yield (heading, body_lines) for each level-2 section in a day file."""
    lines = text.splitlines()
    sections = []
    cur_head = None
    cur_body = []
    for ln in lines:
        m = re.match(r"^##\s+(?!#)(.*)$", ln)  # level-2 only
        if m:
            if cur_head is not None:
                sections.append((cur_head, cur_body))
            cur_head = m.group(1).strip()
            cur_body = []
        elif cur_head is not None:
            cur_body.append(ln)
    if cur_head is not None:
        sections.append((cur_head, cur_body))
    return sections


def extract_conclusion(body_lines):
    """Return the text under a `### Conclusion` / `### Summary` sub-header."""
    out = []
    capturing = False
    for ln in body_lines:
        if re.match(r"^###\s+", ln):
            if re.search(r"conclusion|summary", ln, re.IGNORECASE) and not re.search(
                r"speaker", ln, re.IGNORECASE
            ):
                capturing = True
                continue
            else:
                capturing = False
                continue
        if capturing:
            out.append(ln)
    text = "\n".join(out).strip()
    # collapse blank-line runs
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def main():
    meetings = sorted(
        d for d in MEETINGS.iterdir() if d.is_dir() and re.match(r"\d{4}-\d{2}", d.name)
    )
    records = []
    md = ["# Agenda Index (generated)\n",
          "> Mechanically extracted from `raw/notes`. Do not hand-edit; regenerate via `tools/extract_agenda.py`.",
          "> One block per meeting. Each agenda item shows its heading, stage signals, and conclusion.",
          "> To trace a proposal: `grep -i -A4 'temporal' wiki/_generated/agenda-index.md`.\n"]

    for mdir in meetings:
        ym = mdir.name
        day_files = sorted(
            f for f in mdir.glob("*.md") if f.name not in ("toc.md", "README.md")
        )
        meeting_items = []
        for f in day_files:
            text = f.read_text(encoding="utf-8", errors="replace")
            for head, body in parse_day(text):
                if BOILERPLATE.match(head):
                    continue
                head_stages = STAGE_RE.findall(head)
                concl = extract_conclusion(body)
                concl_stages = STAGE_RE.findall(concl)
                # signal lines: conclusion lines mentioning a stage transition
                signals = []
                for cl in concl.splitlines():
                    if STAGE_RE.search(cl) and ADVANCE_RE.search(cl):
                        signals.append(cl.strip(" -*").strip())
                rec = {
                    "meeting": ym,
                    "file": str(f.relative_to(ROOT)),
                    "heading": head,
                    "heading_stages": head_stages,
                    "conclusion": concl,
                    "conclusion_stages": concl_stages,
                    "signals": signals,
                }
                records.append(rec)
                meeting_items.append(rec)

        if not meeting_items:
            continue
        md.append(f"\n## {ym}\n")
        for rec in meeting_items:
            stage_tag = ""
            allst = rec["heading_stages"] + rec["conclusion_stages"]
            if allst:
                stage_tag = " — stage: " + "/".join(sorted(set(allst)))
            md.append(f"- **{rec['heading']}**{stage_tag}  `{rec['file']}`")
            if rec["signals"]:
                for s in rec["signals"]:
                    md.append(f"  - → {s}")
            elif rec["conclusion"]:
                first = rec["conclusion"].splitlines()[0].strip(" -*").strip()
                if first:
                    md.append(f"  - {first[:200]}")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    with OUT_JSONL.open("w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"meetings: {len(meetings)}")
    print(f"agenda items extracted: {len(records)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSONL.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
