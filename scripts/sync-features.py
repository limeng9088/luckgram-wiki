#!/usr/bin/env python3
"""Sync the feature catalog and status lines from luckgram-site's data/features.json.

luckgram.cc/features and this Help Center share one feature list (issue specs#103).
The list lives in limeng9088/luckgram-site at data/features.json; this script copies it
to _data/features.json and regenerates, in Chinese and English:

  features/README.md          the catalog between <!-- features:catalog:start/end -->
  every page that has <!-- features:top -->            "back to features" line at the top
  every line ending in <!-- status:<feature id> -->    the status line under that section

Usage (from the repo root):
  python3 scripts/sync-features.py [path/to/luckgram-site/data/features.json]
  python3 scripts/sync-features.py --check     # exit 1 if anything is out of date

Without a path it reads ../luckgram-site/data/features.json, falling back to the copy in
_data/features.json (useful for --check in CI).
"""
import glob
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "_data", "features.json")
SITE = {"zh": "https://luckgram.cc/features/", "en": "https://luckgram.cc/en/features/"}
LANG_ROOT = {"zh": ROOT, "en": os.path.join(ROOT, "en")}
TEXT = {
    "zh": {"feature": "功能", "what": "作用", "status": "状态", "back": "← 返回功能介绍",
           "top": "本页各功能的状态与 [Luckgram 功能介绍]({site}) 一致。",
           "more": "在功能介绍中查看"},
    "en": {"feature": "Feature", "what": "What it does", "status": "Status", "back": "← Back to features",
           "top": "The status of each feature on this page matches [Luckgram features]({site}).",
           "more": "See it on the features page"},
}
STATUS_LINE = re.compile(r"^(?:> .*)?<!-- status:([a-z0-9-]+) -->$")
TOP_START, TOP_END = "<!-- features:top -->", "<!-- features:top:end -->"
CAT_START, CAT_END = "<!-- features:catalog:start -->", "<!-- features:catalog:end -->"


def wiki_link(feature, lang, from_dir):
    """Relative Markdown link from a page in from_dir to the feature's wiki page (.md)."""
    path, _, frag = feature["wiki"].lstrip("/").partition("#")
    target = os.path.join(LANG_ROOT[lang], path.replace(".html", ".md"))
    return os.path.relpath(target, from_dir) + ("#" + frag if frag else "")


def catalog(data, lang, from_dir):
    tx = TEXT[lang]
    out = [CAT_START]
    for g in data["groups"]:
        items = [f for f in data["features"] if f["group"] == g["id"]]
        out += ["", "## %s {#%s}" % (g["name"][lang], g["id"]), "",
                "| %s | %s | %s |" % (tx["feature"], tx["what"], tx["status"]), "|---|---|---|"]
        for f in items:
            out.append("| [%s](%s) | %s | %s |" % (f["name"][lang], wiki_link(f, lang, from_dir), f["title"][lang],
                                                   data["statuses"][f["status"]][lang]))
    out += ["", CAT_END]
    return "\n".join(out)


def status_line(f, data, lang):
    return "> **%s** · [%s](%s#%s) <!-- status:%s -->" % (
        data["statuses"][f["status"]][lang], TEXT[lang]["more"], SITE[lang], f["id"], f["id"])


def top_block(lang):
    tx = TEXT[lang]
    return "%s\n> %s [%s](%s)\n%s" % (TOP_START, tx["top"].format(site=SITE[lang]), tx["back"], SITE[lang], TOP_END)


def render(text, data, lang, path):
    feats = {f["id"]: f for f in data["features"]}
    seen = set()
    lines = []
    for line in text.split("\n"):
        m = STATUS_LINE.match(line)
        if m:
            fid = m.group(1)
            if fid not in feats:
                sys.exit("%s: unknown feature id %r" % (path, fid))
            seen.add(fid)
            line = status_line(feats[fid], data, lang)
        lines.append(line)
    text = "\n".join(lines)
    if TOP_START in text:
        text = re.sub(re.escape(TOP_START) + r".*?" + re.escape(TOP_END), lambda _: top_block(lang), text, flags=re.S)
    if CAT_START in text:
        text = re.sub(re.escape(CAT_START) + r".*?" + re.escape(CAT_END),
                      lambda _: catalog(data, lang, os.path.dirname(path)), text, flags=re.S)
    return text, seen


def main():
    args = [a for a in sys.argv[1:] if a != "--check"]
    check = "--check" in sys.argv[1:]
    src = args[0] if args else os.path.join(ROOT, "..", "luckgram-site", "data", "features.json")
    if not os.path.exists(src):
        src = DATA
    data = json.load(open(src, encoding="utf-8"))
    stale = []
    if os.path.abspath(src) != os.path.abspath(DATA):
        if not os.path.exists(DATA) or open(src, "rb").read() != open(DATA, "rb").read():
            stale.append(DATA)
            if not check:
                os.makedirs(os.path.dirname(DATA), exist_ok=True)
                shutil.copyfile(src, DATA)

    problems = []
    for lang in ("zh", "en"):
        pages = glob.glob(os.path.join(LANG_ROOT[lang], "**", "*.md"), recursive=True)
        if lang == "zh":
            pages = [p for p in pages if not p.startswith(os.path.join(ROOT, "en") + os.sep)
                     and not p.startswith(os.path.join(ROOT, "docs") + os.sep)]
        covered = set()
        for p in pages:
            text = open(p, encoding="utf-8").read()
            new, seen = render(text, data, lang, p)
            covered |= seen
            if new != text:
                stale.append(p)
                if not check:
                    open(p, "w", encoding="utf-8").write(new)
        for f in data["features"]:
            if f["id"] not in covered:
                problems.append("%s: no section with <!-- status:%s --> for %s" % (lang, f["id"], f["wiki"]))
            page = os.path.join(LANG_ROOT[lang], f["wiki"].lstrip("/").partition("#")[0].replace(".html", ".md"))
            anchor = f["wiki"].partition("#")[2]
            if not os.path.exists(page):
                problems.append("%s: %s does not exist" % (lang, page))
            elif anchor and "{#%s}" % anchor not in open(page, encoding="utf-8").read():
                problems.append("%s: %s has no heading {#%s}" % (lang, page, anchor))
    for p in problems:
        print("ERROR", p)
    if check and stale:
        print("out of date (run scripts/sync-features.py):", *[os.path.relpath(s, ROOT) for s in stale], sep="\n  ")
    if problems or (check and stale):
        sys.exit(1)
    print("%d features; %s" % (len(data["features"]), "up to date" if check else "%d files updated" % len(stale)))


if __name__ == "__main__":
    main()
