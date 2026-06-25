#!/usr/bin/env python3
"""Link delegate abbreviations in proposal pages to their person page.

Turns standalone occurrences of a known abbreviation (e.g. PFC) into a standard
markdown link `[PFC](../people/PFC.md)` so it is clickable in the VSCode
markdown preview (which does NOT support Obsidian `[[wikilinks]]`). Standard
relative links also work in Obsidian, so this is the portable choice.

The set of known abbreviations comes from the filenames in wiki/people/ (run
extract_people.py first).

Behaviour per proposal page:
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
PROPOSALS = ROOT / "wiki" / "proposals"
PEOPLE = ROOT / "wiki" / "people"
REL = "../people"  # from wiki/proposals/ to wiki/people/

# Protect inline code, existing markdown links, and existing wikilinks.
PROTECT = re.compile(r"`[^`]*`|\[[^\]]*\]\([^)]*\)|\[\[[^\]]*\]\]")


def known_abbrs():
    return sorted((p.stem for p in PEOPLE.glob("*.md")), key=len, reverse=True)


def link_line(line, token_re):
    """Link bare abbreviations in a single line, skipping protected spans."""
    out = []
    last = 0
    for m in PROTECT.finditer(line):
        out.append(token_re.sub(repl, line[last:m.start()]))
        out.append(m.group(0))  # keep protected span verbatim
        last = m.end()
    out.append(token_re.sub(repl, line[last:]))
    return "".join(out)


def repl(m):
    a = m.group(1)
    return f"[{a}]({REL}/{a}.md)"


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
    for pf in sorted(PROPOSALS.glob("*.md")):
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
            line = wl_alias.sub(lambda m: f"[{m.group(2)}]({REL}/{m.group(1)}.md)", line)
            line = wl_plain.sub(lambda m: f"[{m.group(1)}]({REL}/{m.group(1)}.md)", line)
            # 2) link bare tokens
            out.append(link_line(line, token_re))
        new = "\n".join(out) + ("\n" if text.endswith("\n") else "")
        if new != text:
            pf.write_text(new, encoding="utf-8")
            changed += 1
            print(f"linked: {pf.relative_to(ROOT)}")

    print(f"abbreviations: {len(abbrs)}  pages changed: {changed}")


if __name__ == "__main__":
    main()
