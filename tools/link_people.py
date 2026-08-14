#!/usr/bin/env python3
"""Link delegate abbreviations in wiki pages to their person page.

Turns standalone occurrences of a known abbreviation (e.g. PFC) into a standard
markdown link `[PFC](../people/PFC.md)` so it is clickable in the VSCode
markdown preview (which does NOT support Obsidian `[[wikilinks]]`). Standard
relative links also work in Obsidian, so this is the portable choice.

Sources: wiki/proposals/, wiki/families/, and wiki/meetings/<YYYY-MM>/ (daily
meeting summaries + their README). The relative link prefix is derived from
each file's depth. Only abbreviations that already have a person page are
linked, so meeting-only attendees stay plain text (no dead links).

The set of known abbreviations comes from the filenames in wiki/people/ (run
extract_people.py first).

Behaviour per page:
  1. Migrate any legacy `[[ABBR]]` / `[[ABBR|name]]` wikilinks to markdown form.
  2. Link bare standalone abbreviations to markdown form.

Protected regions (never touched): YAML frontmatter, fenced code blocks
(```...```), inline code (`...`), existing markdown links ([text](url)), and
remaining wikilinks ([[...]]). The pass is idempotent.

Usage:  python3 tools/link_people.py
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
PROPOSALS = WIKI / "proposals"
FAMILIES = WIKI / "families"
MEETINGS = WIKI / "meetings"
PEOPLE = WIKI / "people"

# Protect inline code, existing markdown links, existing wikilinks, bare URLs.
PROTECT = re.compile(r"`[^`]*`|\[[^\]]*\]\([^)]*\)|\[\[[^\]]*\]\]|https?://\S+")

# Abbreviations too ambiguous to auto-link: the same token usually means
# something else in meeting notes. Link these manually where they really are
# the person; the auto pass skips them. Extend when a new clash appears.
AMBIGUOUS = {
    "JSC",  # almost always the JavaScriptCore engine, rarely J. S. Choi
}


def known_abbrs():
    return sorted(
        (p.stem for p in PEOPLE.glob("*.md") if p.stem not in AMBIGUOUS),
        key=len,
        reverse=True,
    )


def rel_people(pf):
    """Relative path from pf's directory to wiki/people (posix style)."""
    depth = len(pf.parent.relative_to(WIKI).parts)
    return "/".join([".."] * depth) + "/people"


def link_line(line, token_re, rel):
    """Link bare abbreviations in a single line, skipping protected spans."""
    repl = lambda m: f"[{m.group(1)}]({rel}/{m.group(1)}.md)"
    out = []
    last = 0
    for m in PROTECT.finditer(line):
        out.append(token_re.sub(repl, line[last:m.start()]))
        out.append(m.group(0))  # keep protected span verbatim
        last = m.end()
    out.append(token_re.sub(repl, line[last:]))
    return "".join(out)


def main():
    abbrs = known_abbrs()
    if not abbrs:
        print("no person pages found; run extract_people.py first")
        return
    alt = "|".join(map(re.escape, abbrs))
    token_re = re.compile(
        r"(?<![A-Za-z0-9_#@.\[\]])(" + alt + r")(?![A-Za-z0-9_\]])"
    )
    # Legacy wikilink migration: [[ABBR]] and [[ABBR|alias]].
    wl_plain = re.compile(r"\[\[(" + alt + r")\]\]")
    wl_alias = re.compile(r"\[\[(" + alt + r")\|([^\]]*)\]\]")

    changed = 0
    sources = sorted(PROPOSALS.glob("*.md"))
    if FAMILIES.is_dir():
        sources += sorted(FAMILIES.glob("*.md"))
    if MEETINGS.is_dir():
        sources += sorted(MEETINGS.glob("*/*.md"))
    for pf in sources:
        rel = rel_people(pf)
        text = pf.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines(keepends=False)
        out = []
        in_frontmatter = False
        in_fence = False
        for i, line in enumerate(lines):
            stripped = line.strip()
            if i == 0 and stripped == "---":
                in_frontmatter = True
                out.append(line)
                continue
            if in_frontmatter:
                out.append(line)
                if stripped == "---":
                    in_frontmatter = False
                continue
            if stripped.startswith("```"):
                in_fence = not in_fence
                out.append(line)
                continue
            if in_fence:
                out.append(line)
                continue
            # 1) migrate legacy wikilinks to markdown links
            line = wl_alias.sub(lambda m: f"[{m.group(2)}]({rel}/{m.group(1)}.md)", line)
            line = wl_plain.sub(lambda m: f"[{m.group(1)}]({rel}/{m.group(1)}.md)", line)
            # 2) link bare tokens
            out.append(link_line(line, token_re, rel))
        new = "\n".join(out) + ("\n" if text.endswith("\n") else "")
        if new != text:
            pf.write_text(new, encoding="utf-8")
            changed += 1
            print(f"linked: {pf.relative_to(ROOT)}")

    print(f"abbreviations: {len(abbrs)}  pages changed: {changed}")


if __name__ == "__main__":
    main()
