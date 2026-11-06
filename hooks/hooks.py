"""MkDocs hooks:

* adds each page's `keywords` front matter as hidden text so search finds them;
* replaces <!-- LATEST_UPDATES --> on the home page with a table of the
  10 most recently changed articles (dates from git history).
"""
import logging
import os

import git  # GitPython
import yaml

log = logging.getLogger("mkdocs.hooks.hooks")

# Marker in docs/index.md that gets replaced with the "latest changes" table
UPDATES_PLACEHOLDER = '<!-- LATEST_UPDATES -->'
UPDATES_COUNT = 10


def get_page_title(filepath):
    """Title from YAML front matter, else the first '# ' heading, else the file name."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError as e:
        log.warning("Could not read %s: %s", filepath, e)
        content = ''

    # 1. YAML front matter (between ---)
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                data = yaml.safe_load(parts[1]) or {}
                if data.get('title'):
                    return data['title']
            except yaml.YAMLError as e:
                log.warning("Invalid front matter in %s: %s", filepath, e)

    # 2. First Markdown heading
    for line in content.split('\n'):
        if line.strip().startswith('# '):
            return line.strip()[2:].strip()

    # 3. Cleaned-up file name
    filename = os.path.basename(filepath)
    return filename.replace('.md', '').replace('-', ' ').replace('_', ' ').title()


def build_updates_table(config, files):
    docs_dir = config['docs_dir']
    repo = git.Repo(docs_dir, search_parent_directories=True)
    latest_pages = []

    for file in files:
        path = file.src_uri  # always '/'-separated, also on Windows
        if not path.endswith('.md') or path == 'index.md':
            continue
        if path.startswith(('system/', 'assets/')):
            continue

        abs_path = file.abs_src_path
        commit = next(repo.iter_commits(paths=abs_path, max_count=1), None)
        if commit is None:
            continue  # not committed yet

        latest_pages.append({
            'title': get_page_title(abs_path),
            'url': path,  # link to the .md file so MkDocs resolves (and validates) it
            'date': commit.committed_datetime,
        })

    latest_pages.sort(key=lambda x: x['date'], reverse=True)

    table = "\n\n## 🔄 Zadnje promjene\n\n"
    table += "| Članak | Datum |\n"
    table += "| :----- | :---- |\n"
    for item in latest_pages[:UPDATES_COUNT]:
        date_str = item['date'].strftime('%d.%m.%Y.')
        safe_title = str(item['title']).replace('|', '-')
        table += f"| [{safe_title}]({item['url']}) | {date_str} |\n"
    return table


def on_page_markdown(markdown, page, config, files):
    # --- Keywords for search ---
    keywords = page.meta.get('keywords')
    if isinstance(keywords, list) and keywords:
        markdown += f"\n\n<div style='display:none'>{', '.join(map(str, keywords))}</div>"

    # --- Latest updates table (home page only) ---
    if page.file.src_path == 'index.md' and UPDATES_PLACEHOLDER in markdown:
        try:
            table = build_updates_table(config, files)
        except (git.exc.GitError, ValueError) as e:
            log.warning("Could not build the latest-changes table: %s", e)
            table = ''
        # Replace the first marker; drop any accidental extra copies
        markdown = markdown.replace(UPDATES_PLACEHOLDER, table, 1)
        markdown = markdown.replace(UPDATES_PLACEHOLDER, '')

    return markdown
