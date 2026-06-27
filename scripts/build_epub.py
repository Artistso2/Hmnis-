#!/usr/bin/env python3
"""
Dependency-free EPUB 3 builder for HELLO, MY NAME IS STEVEN.

This is intentionally simple. It converts a constrained subset of Markdown to XHTML
and packages an EPUB that can be opened in most readers.
"""
from __future__ import annotations

import html
import re
import shutil
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
OUT = ROOT / "output"
TMP = ROOT / "epub_build" / "hello_my_name_is_steven"
EPUB = OUT / "hello_my_name_is_steven.epub"


def read_metadata() -> dict:
    meta = {}
    path = BOOK / "metadata.yaml"
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.strip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    if not meta.get("identifier"):
        meta["identifier"] = f"urn:uuid:{uuid.uuid4()}"
    return meta


def slugify(path: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", Path(path).stem).strip("_") + ".xhtml"


def md_to_xhtml(md: str, title: str) -> str:
    lines = md.splitlines()
    out = []
    in_list = False
    in_quote = False

    def close_blocks():
        nonlocal in_list, in_quote
        if in_list:
            out.append("</ul>")
            in_list = False
        if in_quote:
            out.append("</blockquote>")
            in_quote = False

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            close_blocks()
            continue
        if line.startswith("# "):
            close_blocks()
            out.append(f"<h1>{html.escape(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            close_blocks()
            out.append(f"<h2>{html.escape(line[3:].strip())}</h2>")
        elif line.startswith("### "):
            close_blocks()
            out.append(f"<h3>{html.escape(line[4:].strip())}</h3>")
        elif line.startswith("> "):
            if in_list:
                out.append("</ul>")
                in_list = False
            if not in_quote:
                out.append("<blockquote>")
                in_quote = True
            out.append(f"<p>{inline_md(line[2:].strip())}</p>")
        elif line.startswith("- "):
            if in_quote:
                out.append("</blockquote>")
                in_quote = False
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline_md(line[2:].strip())}</li>")
        else:
            close_blocks()
            out.append(f"<p>{inline_md(line.strip())}</p>")
    close_blocks()
    body = "\n".join(out)
    return f'''<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
{body}
</body>
</html>
'''


def inline_md(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*(.+?)\*", r"<em>\1</em>", escaped)
    return escaped


def main() -> None:
    meta = read_metadata()
    OUT.mkdir(exist_ok=True)
    if TMP.exists():
        shutil.rmtree(TMP)
    (TMP / "META-INF").mkdir(parents=True)
    (TMP / "EPUB").mkdir(parents=True)

    (TMP / "mimetype").write_text("application/epub+zip", encoding="utf-8")
    (TMP / "META-INF" / "container.xml").write_text('''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
''', encoding="utf-8")

    css = '''body { font-family: serif; line-height: 1.5; margin: 5%; }
h1, h2, h3 { font-family: sans-serif; }
blockquote { border-left: 0.25em solid #777; margin-left: 0; padding-left: 1em; }
'''
    (TMP / "EPUB" / "style.css").write_text(css, encoding="utf-8")

    order = [line.strip() for line in (BOOK / "manuscript_order.txt").read_text(encoding="utf-8").splitlines() if line.strip()]
    items = []
    spine = []
    nav_items = []

    for idx, rel in enumerate(order, start=1):
        md_path = BOOK / rel
        md = md_path.read_text(encoding="utf-8")
        first_heading = next((l[2:].strip() for l in md.splitlines() if l.startswith("# ")), Path(rel).stem)
        xhtml_name = slugify(rel)
        xhtml = md_to_xhtml(md, first_heading)
        (TMP / "EPUB" / xhtml_name).write_text(xhtml, encoding="utf-8")
        item_id = f"chap{idx}"
        items.append(f'<item id="{item_id}" href="{xhtml_name}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="{item_id}"/>')
        nav_items.append(f'<li><a href="{xhtml_name}">{html.escape(first_heading)}</a></li>')

    nav = f'''<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head><title>Navigation</title></head>
<body>
<nav epub:type="toc" id="toc">
<h1>Contents</h1>
<ol>
{''.join(nav_items)}
</ol>
</nav>
</body>
</html>
'''
    (TMP / "EPUB" / "nav.xhtml").write_text(nav, encoding="utf-8")

    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    package = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">{html.escape(meta.get('identifier', 'urn:uuid:draft'))}</dc:identifier>
    <dc:title>{html.escape(meta.get('title', 'Untitled'))}</dc:title>
    <dc:creator>{html.escape(meta.get('creator', 'Unknown'))}</dc:creator>
    <dc:language>{html.escape(meta.get('language', 'en-US'))}</dc:language>
    <dc:publisher>{html.escape(meta.get('publisher', ''))}</dc:publisher>
    <dc:rights>{html.escape(meta.get('rights', ''))}</dc:rights>
    <meta property="dcterms:modified">{modified}</meta>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="style" href="style.css" media-type="text/css"/>
    {' '.join(items)}
  </manifest>
  <spine>
    {' '.join(spine)}
  </spine>
</package>
'''
    (TMP / "EPUB" / "package.opf").write_text(package, encoding="utf-8")

    if EPUB.exists():
        EPUB.unlink()
    with zipfile.ZipFile(EPUB, "w") as zf:
        zf.write(TMP / "mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
        for path in sorted(TMP.rglob("*")):
            if path.is_file() and path.name != "mimetype":
                zf.write(path, path.relative_to(TMP), compress_type=zipfile.ZIP_DEFLATED)
    print(f"Built {EPUB}")


if __name__ == "__main__":
    main()
