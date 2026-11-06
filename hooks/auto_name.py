"""MkDocs hook: create a `.pages` file for every folder whose index.md has a title.

The awesome-pages plugin reads `.pages` to name folders in the navigation, so
articles created through the CMS get a proper section title automatically.
Existing `.pages` files are never overwritten.
"""
import logging
import os

import yaml

log = logging.getLogger("mkdocs.hooks.auto_name")


def _read_title(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    frontmatter = yaml.safe_load(parts[1]) or {}
    return frontmatter.get("title")


def on_pre_build(config):
    docs_dir = config["docs_dir"]
    created = 0

    for root, _dirs, files in os.walk(docs_dir):
        if "index.md" not in files:
            continue
        pages_path = os.path.join(root, ".pages")
        if os.path.exists(pages_path):
            continue

        index_path = os.path.join(root, "index.md")
        try:
            title = _read_title(index_path)
        except Exception as e:
            log.warning("Could not read %s: %s", index_path, e)
            continue
        if not title:
            continue

        with open(pages_path, "w", encoding="utf-8") as p:
            p.write(f"title: {title}\n")
        log.info("Created .pages for %s -> '%s'", os.path.relpath(root, docs_dir), title)
        created += 1

    if created:
        log.info("auto_name: created %d new .pages file(s)", created)
