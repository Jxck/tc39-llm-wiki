#!/usr/bin/env python3
"""Link proposal names in meeting summaries to their proposal page.

Two idempotent passes over wiki/meetings/<YYYY-MM>/*.md:

1. Daily files only: for each `## <topic>` whose heading names a deep-read
   proposal (title or alias, backticks ignored), ensure the section's FIRST
    bullet is `- wiki: [Title](../../proposals/<slug>.md)` — before Slides. An
    existing wiki bullet is moved to the front (its content is kept); topics
    without a matching page get no bullet.
2. All files: turn inline occurrences of a deep-read proposal's title (e.g.
   "Await Dictionary") into a markdown link. Only proposals that already have
   a page in wiki/proposals/ are linked, so unread proposals stay plain text
   (no dead links). Matching is case-insensitive and the original casing is
   kept as the link text. Within one `## <topic>` section (or the preamble
   before the first one) only the FIRST mention of each proposal stays a
   link; later links to the same page are reduced to plain text. The meta
   bullets at the top of a topic do not count as a mention.

Titles come from each page's frontmatter `title:`; ALIASES adds textual
variants that appear in summaries (renames, abbreviations, old names).

Protected regions (never touched): YAML frontmatter, fenced code blocks,
inline code (`...`), existing markdown links, wikilinks, bare URLs, and
headings (`#...` topic titles stay verbatim). The pass is idempotent.

Usage:  python3 tools/link_proposals.py
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
PROPOSALS = WIKI / "proposals"
MEETINGS = WIKI / "meetings"

# Protect inline code, existing markdown links, wikilinks, and bare URLs.
PROTECT = re.compile(r"`[^`]*`|\[[^\]]*\]\([^)]*\)|\[\[[^\]]*\]\]|https?://\S+")

# Textual variants seen in summaries -> proposal page filename. Extend when a
# summary uses a spelling that differs from the page's frontmatter title.
ALIASES = {
    "Records and Tuples": "records-and-tuples.md",
    "Intl Era/Month Code": "intl-era-month-code.md",
    "Intl Era and Month Code": "intl-era-month-code.md",
    "Intl Era Monthcode": "intl-era-month-code.md",
    "Map take": "map-get-and-delete.md",
    "Intl.DateTimeFormat Alignment": "intl-datetimeformat-alignment.md",
    "Curtailing the power of \"Thenables\"": "thenable-curtailment.md",
    "How to make thenables safer": "thenable-curtailment.md",
    "Keep trailing zeros": "intl-keep-trailing-zeros.md",
    "isTemplateObject": "is-template-object.md",
    "Import Buffer": "import-bytes.md",
    "Immutable ArrayBuffer": "immutable-arraybuffer.md",
    "Module Import Hook and new Global": "module-global.md",
    "proposal-module-global": "module-global.md",
    "Uint8Array base64": "uint8array-base64.md",
    "TypedArray concat": "typedarray-concat.md",
    "TypedArray find within": "typedarray-find-within.md",
    "TypedArray findWithin": "typedarray-find-within.md",
    "Error.prototype.stack accessor": "error-stack-accessor.md",
    "Sync Imports": "import-sync.md",
    "Measure": "amount.md",
}

# Titles that are also ordinary English words ("the amount of work", "clearer
# signals"). These only match with their exact capitalization, so lowercase
# prose is never mistaken for the proposal.
CASE_SENSITIVE = {
    "Amount",
    "Comparisons",
    "Decimal",
    "Enums",
    "Extractors",
    "Measure",
    "Signals",
    "Stabilize",
}


def page_titles():
    """title -> filename for existing deep-read pages, plus aliases."""
    m = {}
    for pf in sorted(PROPOSALS.glob("*.md")):
        if pf.name == "index.md":
            continue
        fm = re.search(r"^---\n(.*?)\n---", pf.read_text(encoding="utf-8"), re.DOTALL)
        if not fm:
            continue
        t = re.search(r"^title:\s*(.+)$", fm.group(1), re.MULTILINE)
        if t:
            m[t.group(1).strip()] = pf.name
    for alias, fname in ALIASES.items():
        if (PROPOSALS / fname).exists():
            m[alias] = fname
    return m


def rel_proposals(pf):
    """Relative path from pf's directory to wiki/proposals (posix style)."""
    depth = len(pf.parent.relative_to(WIKI).parts)
    return "/".join([".."] * depth) + "/proposals"


def link_line(line, token_re, titles_ci, rel):
    def repl(m):
        fname = titles_ci[m.group(1).lower()]
        return f"[{m.group(1)}]({rel}/{fname})"

    out = []
    last = 0
    for m in PROTECT.finditer(line):
        out.append(token_re.sub(repl, line[last:m.start()]))
        out.append(m.group(0))  # keep protected span verbatim
        last = m.end()
    out.append(token_re.sub(repl, line[last:]))
    return "".join(out)


def page_title_of(fname):
    """Frontmatter title of a proposal page (link text for topic bullets)."""
    fm = re.search(
        r"^---\n(.*?)\n---", (PROPOSALS / fname).read_text(encoding="utf-8"), re.DOTALL
    )
    t = re.search(r"^title:\s*(.+)$", fm.group(1), re.MULTILINE) if fm else None
    return t.group(1).strip() if t else fname


DAILY = re.compile(r"^\d{4}-\d{2}-\d{2}")
META_BULLET = re.compile(r"^- (?:wiki|proposal|[Ss]lides?):")


def dedupe_links(line, rel, seen):
    """Keep only the first link per proposal page in a section: later links
    to a page already in `seen` become their plain link text."""
    pat = re.compile(r"\[([^\]]*)\]\(" + re.escape(rel) + r"/([a-z0-9-]+\.md)\)")

    def repl(m):
        if m.group(2) in seen:
            return m.group(1)
        seen.add(m.group(2))
        return m.group(0)

    return pat.sub(repl, line)
# The legacy label is still accepted so older files can be migrated to "wiki".
WIKI_BULLET = re.compile(r"^- (?:wiki|\u63d0\u6848\u30da\u30fc\u30b8):")
PROPOSAL_BULLET = re.compile(r"^- proposal:")
# Lowercase singular "slide:" is the convention; match the legacy forms
# (Slides/slides) too so reordering still works until files are converted.
SLIDES_BULLET = re.compile(r"^- [Ss]lides?:")


def take_first(core, pat):
    """Remove and return the first line matching pat (or None)."""
    for j, l in enumerate(core):
        if pat.match(l):
            return core.pop(j)
    return None


def ensure_topic_bullets(lines, token_re, titles_ci, rel):
    """Daily files: order each topic's meta bullets as wiki > proposal >
    Slides, with the wiki bullet added from the heading when missing.

    The section is rebuilt in oxfmt's canonical shape (one blank line after
    the heading, one blank line between a list and a following paragraph) so
    the pass reaches a fixpoint with the formatter.
    """
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        i += 1
        if not line.startswith("## "):
            continue
        # Pages named in the heading (ignore backticks so `Intl.X` matches).
        heading = line[3:].replace("`", "")
        fnames = []
        for m in token_re.finditer(heading):
            fname = titles_ci[m.group(1).lower()]
            if fname not in fnames:
                fnames.append(fname)
        # Collect this topic's lines up to the next heading.
        section = []
        while i < len(lines) and not lines[i].startswith("## "):
            section.append(lines[i])
            i += 1
        had_trailing_blank = bool(section) and section[-1] == ""
        core = list(section)
        while core and core[0] == "":
            core.pop(0)
        while core and core[-1] == "":
            core.pop()
        wikis = []
        while (w := take_first(core, WIKI_BULLET)) is not None:
            wikis.append(WIKI_BULLET.sub("", w).strip())  # migrate legacy label
        wiki = None
        if wikis:
            # Several wiki bullets (e.g. one added by hand after Slides) are
            # merged into a single bullet, keeping each link once.
            links = []
            for w in wikis:
                for part in re.findall(r"\[[^\]]*\]\([^)]*\)", w) or [w]:
                    if part not in links:
                        links.append(part)
            wiki = "- wiki: " + ", ".join(links)
        elif fnames:
            wiki = "- wiki: " + ", ".join(
                f"[{page_title_of(f)}]({rel}/{f})" for f in fnames
            )
        proposal = take_first(core, PROPOSAL_BULLET)
        slides = take_first(core, SLIDES_BULLET)
        header = [b for b in (wiki, proposal, slides) if b]
        if not header:
            out.extend(section)  # nothing to order; keep the topic verbatim
            continue
        while core and core[0] == "":
            core.pop(0)
        rebuilt = list(header)
        if core and not core[0].startswith("- "):
            rebuilt.append("")  # blank line between the list and prose
        rebuilt.extend(core)
        out.append("")
        out.extend(rebuilt)
        if had_trailing_blank:
            out.append("")
    return out


def main():
    titles = page_titles()
    if not titles:
        print("no proposal pages found")
        return
    # Longest-first so "Intl.DateTimeFormat Alignment With Other Standards"
    # wins over its shorter alias. Case-insensitive; original text is kept.
    ordered = sorted(titles, key=len, reverse=True)
    titles_ci = {t.lower(): fname for t, fname in titles.items()}
    # Case-sensitive titles are matched by a scoped (?-i:...) group so the
    # longest-first alternation still works as one regex.
    alt = "|".join(
        f"(?-i:{re.escape(t)})" if t in CASE_SENSITIVE else re.escape(t)
        for t in ordered
    )
    token_re = re.compile(
        r"(?<![A-Za-z0-9])(" + alt + r")(?![A-Za-z0-9])", re.IGNORECASE
    )

    changed = 0
    for pf in sorted(MEETINGS.glob("*/*.md")):
        rel = rel_proposals(pf)
        orig = pf.read_text(encoding="utf-8", errors="replace")
        text = orig
        if DAILY.match(pf.name):
            lines = ensure_topic_bullets(
                text.splitlines(keepends=False), token_re, titles_ci, rel
            )
            text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
        lines = text.splitlines(keepends=False)
        out = []
        in_frontmatter = False
        in_fence = False
        seen = set()  # proposal pages already linked in the current section
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
            if stripped.startswith("## "):
                seen = set()
            if in_fence or stripped.startswith("#"):
                out.append(line)  # headings keep the original topic title
                continue
            if META_BULLET.match(line):
                out.append(line)  # topic meta bullets are not body mentions
                continue
            out.append(dedupe_links(link_line(line, token_re, titles_ci, rel), rel, seen))
        new = "\n".join(out) + ("\n" if text.endswith("\n") else "")
        if new != orig:
            pf.write_text(new, encoding="utf-8")
            changed += 1
            print(f"linked: {pf.relative_to(ROOT)}")

    print(f"titles: {len(titles)}  pages changed: {changed}")


if __name__ == "__main__":
    main()
