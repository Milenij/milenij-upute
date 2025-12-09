import os
import git # type: ignore
import yaml
from datetime import datetime

# Settings
ROOT_DIR = os.getcwd()
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')

def get_page_title(filepath):
    """Robustly extracts the title from a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # 1. Try to read YAML Frontmatter (Between ---)
            if content.startswith('---'):
                try:
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        yaml_block = parts[1]
                        data = yaml.safe_load(yaml_block)
                        return data.get('title', os.path.basename(filepath))
                except:
                    pass
            
            # 2. Fallback: Check for first Markdown Header (# Title)
            lines = content.split('\n')
            for line in lines:
                if line.strip().startswith('# '):
                    return line.strip().replace('# ', '').strip()

    except:
        pass
        
    # 3. Last Resort: Clean Filename
    filename = os.path.basename(filepath)
    clean_name = filename.replace('.md', '').replace('-', ' ').replace('_', ' ').title()
    return clean_name

def on_page_markdown(markdown, page, config, files):
    # --- LOGIC FOR KEYWORDS (Search) ---
    if 'keywords' in page.meta:
        keywords_list = page.meta['keywords']
        if isinstance(keywords_list, list):
            keywords_string = ", ".join(keywords_list)
            markdown = markdown + f"\n\n<div style='display:none'>{keywords_string}</div>"

    # --- LOGIC FOR LATEST UPDATES (Home Page Only) ---
    # Only run if we are on index.md AND the placeholder exists
    if page.file.src_path == 'index.md' and "" in markdown:
        try:
            repo = git.Repo(ROOT_DIR)
            latest_pages = []

            for file in files:
                path = file.src_path
                
                # --- FILTERS ---
                if not path.endswith('.md'): continue
                if path == 'index.md': continue
                if 'tags' in path: continue
                if '.pages' in path: continue
                if 'assets' in path: continue
                
                file_abs_path = os.path.join(DOCS_DIR, path)
                
                try:
                    # Get Date
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

            # Sort by Date
            latest_pages.sort(key=lambda x: x['date'], reverse=True)

            # Build Table String
            update_list = "\n\n## 🔄 Zadnje promjene\n\n"
            update_list += "| Članak | Datum |\n"
            update_list += "| :----- | :---- |\n"

            for item in latest_pages[:10]:
                date_str = item['date'].strftime('%d.%m.%Y.')
                # Ensure title doesn't contain weird characters
                safe_title = str(item['title']).replace('|', '-') 
                update_list += f"| [{safe_title}]({item['url']}) | {date_str} |\n"

            # SAFETY REPLACE:
            # 1. Replace the FIRST placeholder with the table
            markdown = markdown.replace("", update_list, 1)
            
            # 2. Remove any EXTRA placeholders (if you pasted it twice by mistake)
            markdown = markdown.replace("", "")

        except Exception as e:
            print(f"Error generating updates: {e}")

    return markdown