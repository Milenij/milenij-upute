"""MkDocs hooks:

* adds each page's `keywords` front matter as hidden text so search finds them;
* replaces <!-- LATEST_UPDATES --> on the home page with a list of the
  10 most recently changed articles: section, new/updated, and the date
  the change went live (all from git history);
* makes search work without č/ć/š/ž/đ ("racun" finds "račun");
* gives each lightbox image link its address (see "Image lightbox" below).
"""
import json
import logging
import os
import re
import unicodedata
from html import escape

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


def section_path(file, title):
    """'Fiskalizacija 2.0 › Računi › Izrada računa' — the menu sections above the article.

    Several articles share a name (Veleprodaja, Wellness, KPD šifre...), so the list
    needs this to tell them apart. Uses the menu titles (from the .pages files).
    """
    page = getattr(file, 'page', None)
    if page is None:
        return ''
    # Outermost section first; skip the article's own folder-section (same title)
    names = [s.title for s in reversed(page.ancestors) if s.title and s.title != title]
    return ' › '.join(names)


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

        # Only main's own history (--first-parent): a CMS edit is many small commits on
        # a cms/... branch, but readers see it once, when its pull request is merged.
        # So the date is when the change went live, and an article counts as new
        # if that change is the one that added it.
        commits = list(repo.iter_commits(paths=file.abs_src_path, first_parent=True))
        if not commits:
            continue  # not committed yet

        title = str(get_page_title(file.abs_src_path))
        latest_pages.append({
            'title': title,
            'section': section_path(file, title),
            'url': file.url,  # relative to the home page, which is at the site root
            'date': commits[0].committed_datetime,
            'new': len(commits) == 1,
        })

    latest_pages.sort(key=lambda x: x['date'], reverse=True)
    if not latest_pages:
        return ''

    # Plain HTML (not a Markdown table) so each row can be one big clickable link
    # that also reads well on a phone; styled in stylesheets/extra.css (.changes).
    rows = []
    for item in latest_pages[:UPDATES_COUNT]:
        kind, label = ('new', 'Novo') if item['new'] else ('updated', 'Ažurirano')
        rows.append(
            f'<a class="changes__row" href="{escape(item["url"])}">'
            f'<span class="changes__text">'
            f'<span class="changes__title">{escape(item["title"])}</span>'
            f'<span class="changes__section">{escape(item["section"])}</span>'
            f'</span>'
            f'<span class="changes__kind changes__kind--{kind}">{label}</span>'
            f'<time class="changes__date" datetime="{item["date"]:%Y-%m-%d}">'
            f'{item["date"]:%d.%m.%Y.}</time>'
            f'</a>'
        )
    return (
        "\n\n## Zadnje promjene\n\n"
        '<div class="changes">\n' + '\n'.join(rows) + '\n</div>\n'
    )


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


# --- Image lightbox ------------------------------------------------------------
# With the privacy plugin on (GitHub builds), mkdocs-glightbox 0.5.3 leaves the href
# out of its <a class="glightbox"> links and fills it in with a script that only runs
# on the first full page load. Pages reached through the menu (instant navigation)
# never get it, so the lightbox opens and spins forever. Write the href in here.

_GLIGHTBOX_LINK = re.compile(
    r'<a class="glightbox"(?![^>]*\shref=)([^>]*)>(\s*<img\b[^>]*?\s(?:data-src|src)="([^"]+)")')


def on_post_page(output, page, config):
    return _GLIGHTBOX_LINK.sub(r'<a class="glightbox" href="\3"\1>\2', output)


# --- Search without Croatian letters -------------------------------------------
# People often type "racun", "sifre", "cijena dostave" without č/ć/š/ž/đ, and the
# search only matches exact letters. After the build, every search entry gets the
# letter-less spelling of its words added as hidden text, so "racun" finds the
# same section as "račun". Nothing changes on the pages themselves.

_HTML_TAG = re.compile(r'<[^>]+>')
_WORD = re.compile(r'\w+')
# Mermaid diagram source would show up in search results as raw code; drop it
_MERMAID = re.compile(
    r'<pre><code>\s*(?:flowchart|graph|sequenceDiagram|stateDiagram|classDiagram|'
    r'erDiagram|gantt|pie|journey|mindmap|timeline)\b.*?</code></pre>', re.S)


def fold(word):
    """'Račun' -> 'Racun', 'Đakovo' -> 'Dakovo' (đ has no accent to strip, so map it)."""
    word = word.replace('đ', 'd').replace('Đ', 'D')
    return ''.join(c for c in unicodedata.normalize('NFD', word)
                   if not unicodedata.combining(c))


def on_post_build(config):
    path = os.path.join(config['site_dir'], 'search', 'search_index.json')
    try:
        with open(path, encoding='utf-8') as f:
            index = json.load(f)
    except (OSError, ValueError) as e:
        log.warning("Search index not found, skipping letter-less search: %s", e)
        return

    for doc in index.get('docs', []):
        doc['text'] = _MERMAID.sub('', doc.get('text', ''))
        plain = _HTML_TAG.sub(' ', f"{doc.get('title', '')} {doc['text']}")
        extra = {fold(w).lower() for w in _WORD.findall(plain) if fold(w) != w}
        if extra:
            doc['text'] = f"{doc['text']} <span hidden>{' '.join(sorted(extra))}</span>"

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, separators=(',', ':'))
