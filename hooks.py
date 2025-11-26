import os
import git
import yaml
from datetime import datetime

# Settings
ROOT_DIR = os.getcwd()
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')

def get_page_title(filepath):
    """Reads the 'title' from the YAML frontmatter of a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                try:
                    # Split only on the first two --- markers
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        yaml_block = parts[1]
                        data = yaml.safe_load(yaml_block)
                        return data.get('title', os.path.basename(filepath))
                except:
                    pass
    except:
        pass
    # Fallback: Clean up filename (e.g., "my-file.md" -> "My File")
    filename = os.path.basename(filepath).replace('.md', '').replace('-', ' ').title()
    return filename

def on_page_markdown(markdown, page, config, files):
    # 1. HANDLE KEYWORDS (Keep your existing keyword logic)
    if 'keywords' in page.meta:
        keywords_list = page.meta['keywords']
        if isinstance(keywords_list, list):
            keywords_string = ", ".join(keywords_list)
            markdown = markdown + f"\n\n<div style='display:none'>{keywords_string}</div>"

    # 2. HANDLE LATEST UPDATES (Strict Filter)
    # Only run this if the placeholder exists in the text
    if "" in markdown:
        try:
            repo = git.Repo(ROOT_DIR)
            latest_pages = []

            for file in files:
                path = file.src_path
                
                # --- FILTERS: WHAT TO IGNORE ---
                if not path.endswith('.md'): continue      # Ignore images/css/js
                if path == 'index.md': continue            # Ignore the homepage itself
                if 'tags.md' in path: continue             # Ignore the tags index
                if '.pages' in path: continue              # Ignore config files
                if 'assets' in path: continue              # Ignore assets folder
                if 'stylesheets' in path: continue         # Ignore styles
                # -------------------------------

                file_abs_path = os.path.join(DOCS_DIR, path)
                
                try:
                    # Get last commit date
                    commit = next(repo.iter_commits(paths=os.path.join('docs', path), max_count=1))
                    last_date = commit.committed_datetime
                    
                    # Get Title
                    title = get_page_title(file_abs_path)
                    
                    latest_pages.append({
                        'title': title,
                        'url': file.url,
                        'date': last_date
                    })
                except:
                    continue

            # Sort by date (Newest first)
            latest_pages.sort(key=lambda x: x['date'], reverse=True)

            # Generate Table
            update_list = "\n## 🔄 Zadnje promjene\n\n"
            update_list += "| Članak | Datum |\n"
            update_list += "| :----- | :---- |\n"

            # Show Top 10
            for item in latest_pages[:10]:
                date_str = item['date'].strftime('%d.%m.%Y.')
                update_list += f"| [{item['title']}]({item['url']}) | {date_str} |\n"

            # Replace the placeholder
            markdown = markdown.replace("", update_list)

        except Exception as e:
            print(f"Error generating updates: {e}")

    return markdown