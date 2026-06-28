#!/usr/bin/env python3
"""Generate per-person reference pages for delegates referenced in the wiki.

Scope: only people whose abbreviation actually appears in a curated proposal
page (`wiki/proposals/*.md`). The set grows automatically as more proposal
pages are added -- just re-run this script.

For each referenced abbreviation it collects:
  - full name        (from raw/notes/delegates.txt, fallback: attendee tables)
  - organization(s)  (from attendee tables across all meetings)
  - 担当ドラフト       (proposals whose frontmatter `champions` lists the abbr)
  - 言及された提案     (proposal pages whose body references the abbr)
  - 参加したミーティング (meetings whose attendee table lists the abbr; rendered
                          as a list, linked to wiki/meetings/<YYYY-MM>/ when a
                          summary exists)

Output: wiki/people/<ABBR>.md (filename = abbreviation, so Obsidian `[[ABBR]]`
links resolve). These files are GENERATED -- do not hand-edit; re-run instead.

Usage:  python3 tools/extract_people.py
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
NOTES = ROOT / "raw" / "notes"
MEETINGS = NOTES / "meetings"
DELEGATES = NOTES / "delegates.txt"
PROPOSALS = ROOT / "wiki" / "proposals"
FAMILIES = ROOT / "wiki" / "families"
WIKI_MEETINGS = ROOT / "wiki" / "meetings"
OUT_DIR = ROOT / "wiki" / "people"

ABBR_TOKEN = re.compile(r"[A-Z][A-Z0-9]{1,4}")
# A delegate abbreviation as it appears standalone in prose.
REF_TOKEN = re.compile(r"(?<![A-Za-z0-9_#@.\[\]])([A-Z][A-Z0-9]{1,4})(?![A-Za-z0-9_])")
# Abbreviations already linked by link_people.py. Detection must still see
# these so the pipeline stays stable once pages are linked. Two forms:
# legacy Obsidian wikilink [[PFC]] / [[PFC|name]], and the markdown link
# [PFC](../people/PFC.md) that link_people.py now emits (the path is the
# reliable signal).
WIKILINK = re.compile(r"\[\[([A-Z][A-Z0-9]{1,4})(?:\|[^\]]*)?\]\]")
PEOPLE_LINK = re.compile(r"/people/([A-Z][A-Z0-9]{1,4})\.md")

# Acronyms that collide with delegate abbreviations but are common nouns in
# prose (e.g. "API surface", "JS value"). Never treat these as person refs.
NON_PERSON = {
    "API", "JS", "JSON", "CSS", "HTML", "IDL", "RFC", "GC", "DOM", "URL",
    "UTC", "ISO", "TG", "ES", "IO", "OS", "UI", "ID", "ECMA", "IETF", "CLDR",
    "WHATWG", "CSP", "PR", "TC", "CLI", "AO", "JIT", "TS", "VM",
}


def load_delegates():
    """abbr -> full name, from 'Full Name (ABBR)' lines."""
    out = {}
    if not DELEGATES.exists():
        return out
    for line in DELEGATES.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^(.*?)\s*\(([A-Z][A-Za-z0-9?]{0,5})\)\s*$", line.strip())
        if m:
            out[m.group(2)] = m.group(1).strip()
    return out


def scan_attendance():
    """abbr -> {'orgs': set, 'meetings': set, 'names': set} from attendee tables."""
    data = {}
    meetings = sorted(
        d for d in MEETINGS.iterdir() if d.is_dir() and re.match(r"\d{4}-\d{2}", d.name)
    )
    for mdir in meetings:
        ym = mdir.name
        for f in mdir.glob("*.md"):
            if f.name in ("toc.md", "README.md"):
                continue
            for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
                if not line.startswith("|"):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) < 2:
                    continue
                name, abbr = cells[0], cells[1]
                org = cells[2] if len(cells) >= 3 else ""
                # skip header / separator rows
                if abbr.lower() in ("abbreviation", "abbr", "") or set(abbr) <= set("-: "):
                    continue
                if not ABBR_TOKEN.fullmatch(abbr):
                    continue
                d = data.setdefault(abbr, {"orgs": set(), "meetings": set(), "names": set()})
                d["meetings"].add(ym)
                if org:
                    d["orgs"].add(org)
                if name and not set(name) <= set("-: "):
                    d["names"].add(name)
    return data


def parse_frontmatter(text):
    """Return (frontmatter_dict_subset, body) for a proposal page."""
    fm = {"title": None, "slug": None, "champions": []}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end]
            body = text[end + 4:]
            for line in block.splitlines():
                m = re.match(r"^(\w+):\s*(.*)$", line)
                if not m:
                    continue
                k, v = m.group(1), m.group(2).strip()
                if k == "title":
                    fm["title"] = v
                elif k == "slug":
                    fm["slug"] = v
                elif k == "champions":
                    fm["champions"] = [
                        x.strip() for x in v.strip("[]").split(",") if x.strip()
                    ]
            return fm, body
    return fm, text


def main():
    delegates = load_delegates()
    attendance = scan_attendance()
    roster = set(delegates) | set(attendance)

    # Meetings that have a wiki summary (wiki/meetings/<YYYY-MM>/README.md).
    # Attendance entries for these get linked; the rest stay plain text.
    summarised = set()
    if WIKI_MEETINGS.is_dir():
        summarised = {
            d.name for d in WIKI_MEETINGS.iterdir()
            if d.is_dir() and (d / "README.md").exists()
        }

    # Gather proposal metadata + referenced abbreviations.
    proposals = []  # (slug, title, champions, referenced_set)
    referenced = set()
    for pf in sorted(PROPOSALS.glob("*.md")):
        text = pf.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        slug = fm["slug"] or pf.stem
        title = fm["title"] or slug
        tokens = (set(REF_TOKEN.findall(text)) & roster) - NON_PERSON
        tokens |= (set(WIKILINK.findall(text)) & roster) - NON_PERSON
        tokens |= (set(PEOPLE_LINK.findall(text)) & roster) - NON_PERSON
        tokens |= (set(fm["champions"]) & roster) - NON_PERSON
        proposals.append((slug, title, set(fm["champions"]), tokens))
        referenced |= tokens

    # Family pages also reference delegates (cross-cutting synthesis). Scan them
    # too so their person links resolve (people pages are generated for any abbr
    # appearing in a family page, even if it never appears in a proposal page).
    families = []  # (slug, title, referenced_set)
    if FAMILIES.is_dir():
        for ff in sorted(FAMILIES.glob("*.md")):
            text = ff.read_text(encoding="utf-8", errors="replace")
            fm, body = parse_frontmatter(text)
            slug = fm["slug"] or ff.stem
            title = fm["title"] or slug
            tokens = (set(REF_TOKEN.findall(text)) & roster) - NON_PERSON
            tokens |= (set(WIKILINK.findall(text)) & roster) - NON_PERSON
            tokens |= (set(PEOPLE_LINK.findall(text)) & roster) - NON_PERSON
            families.append((slug, title, tokens))
            referenced |= tokens

    if not referenced:
        print("no referenced delegates found in wiki/proposals/ or wiki/families/")
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Clear stale generated pages (fully regenerated each run).
    for old in OUT_DIR.glob("*.md"):
        old.unlink()
    written = 0
    for abbr in sorted(referenced):
        name = delegates.get(abbr)
        att = attendance.get(abbr, {"orgs": set(), "meetings": set(), "names": set()})
        if not name:
            # fallback to the most complete name seen in attendee tables
            name = max(att["names"], key=len) if att["names"] else "(不明)"
        orgs = sorted(att["orgs"])
        meetings = sorted(att["meetings"])
        champ_of = [(s, t) for (s, t, ch, _ref) in proposals if abbr in ch]
        appears_in = [(s, t) for (s, t, _ch, ref) in proposals if abbr in ref]
        fam_in = [(s, t) for (s, t, ref) in families if abbr in ref]

        lines = []
        lines.append("---")
        lines.append(f"abbr: {abbr}")
        lines.append(f"name: {name}")
        lines.append(f"orgs: [{', '.join(orgs)}]")
        lines.append(f"meetings_attended: {len(meetings)}")
        lines.append("tags: [person]")
        lines.append("---")
        lines.append("")
        lines.append(f"# {abbr} — {name}")
        lines.append("")
        lines.append(f"- **フルネーム**: {name}")
        if orgs:
            lines.append(f"- **所属**: {' / '.join(orgs)}")
        else:
            lines.append("- **所属**: (出席者テーブルから特定できず)")
        if champ_of:
            lines.append(
                "- **担当ドラフト (champion)**: "
                + ", ".join(f"[{t}](../proposals/{s}.md)" for s, t in champ_of)
            )
        else:
            lines.append("- **担当ドラフト (champion)**: (精読済みページ内では該当なし)")
        if appears_in:
            lines.append(
                "- **言及される提案ページ**: "
                + ", ".join(f"[{t}](../proposals/{s}.md)" for s, t in appears_in)
            )
        if fam_in:
            lines.append(
                "- **言及される family ページ**: "
                + ", ".join(f"[{t}](../families/{s}.md)" for s, t in fam_in)
            )
        lines.append(f"- **参加したミーティング**: 全 {len(meetings)} 回")
        lines.append("")
        if meetings:
            lines.append("## 参加したミーティング")
            lines.append("")
            for ym in reversed(meetings):
                if ym in summarised:
                    lines.append(f"- [{ym}](../meetings/{ym}/README.md)")
                else:
                    lines.append(f"- {ym}")
            lines.append("")
        lines.append("> このページは `tools/extract_people.py` による生成物。"
                     "フルネーム/所属/参加会合は `raw/notes`(delegates.txt と各会合の出席者テーブル)由来、"
                     "担当ドラフトは提案ページ frontmatter の `champions` から相互参照。手で編集せず再生成すること。")
        lines.append("")

        (OUT_DIR / f"{abbr}.md").write_text("\n".join(lines), encoding="utf-8")
        written += 1

    print(f"roster size: {len(roster)}  referenced in proposals: {len(referenced)}")
    print(f"wrote {written} person pages to {OUT_DIR.relative_to(ROOT)}/")
    print("referenced:", " ".join(sorted(referenced)))


if __name__ == "__main__":
    main()
