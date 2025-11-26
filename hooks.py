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
            # Extract YAML between first two ---
            if content.startswith('---'):
                try:
                    yaml_block = content.split('---')[1]
                    data = yaml.safe_load(yaml_block)
                    return data.get('title', os.path.basename(filepath))
                except:
                    return os.path.basename(filepath)
    except:
        pass
    return os.path.basename(filepath)

def on_page_markdown(markdown, page, config, files):
    # 1. HANDLE KEYWORDS (Your previous feature)
    if 'keywords' in page.meta:
        keywords_list = page.meta['keywords']
        if isinstance(keywords_list, list):
            keywords_string = ", ".join(keywords_list)
            markdown = markdown + f"\n\n<div style='display:none'>{keywords_string}</div>"

    # 2. HANDLE LATEST UPDATES (Only on the Home Page)
    if page.file.src_path == 'index.md': # Only runs on Homepage
        try:
            repo = git.Repo(ROOT_DIR)
            latest_pages = []

            # Loop through all files in the website
            for file in files:
                # Skip the homepage itself and assets
                if file.src_path == 'index.md' or 'assets' in file.src_path:
                    continue
                
                # Get real file path
                file_abs_path = os.path.join(DOCS_DIR, file.src_path)
                
                try:
                    # Get last commit date for this specific file
                    commit = next(repo.iter_commits(paths=os.path.join('docs', file.src_path), max_count=1))
                    last_date = commit.committed_datetime
                    
                    # Get the pretty title
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

            # Generate the Markdown Table
            update_list = "\n## 🔄 Zadnje promjene\n\n"
            update_list += "| Članak | Datum ažuriranja |\n"
            update_list += "| :----- | :--------------- |\n"

            # Show top 10
            for item in latest_pages[:10]:
                # Format date to Croatian (Day.Month.Year)
                date_str = item['date'].strftime('%d.%m.%Y.')
                update_list += f"| [{item['title']}]({item['url']}) | {date_str} |\n"

            # Inject into the page where the placeholder is
            if "" in markdown:
                markdown = markdown.replace("", update_list)
            else:
                markdown = markdown + update_list

        except Exception as e:
            print(f"Error generating updates: {e}")

    return markdown