import os
import yaml
import logging

log = logging.getLogger("mkdocs")

def on_pre_build(config):
    """
    This function runs automatically before MkDocs builds the site.
    """
    docs_dir = config['docs_dir']
    
    for root, dirs, files in os.walk(docs_dir):
        if "index.md" in files:
            full_index_path = os.path.join(root, "index.md")
            pages_path = os.path.join(root, ".pages")
            
            # Only create .pages if it doesn't exist
            if not os.path.exists(pages_path):
                try:
                    with open(full_index_path, "r", encoding="utf-8") as f:
                        # Simple extraction to avoid crashing if yaml is bad
                        content = f.read()
                        parts = content.split("---")
                        if len(parts) >= 3:
                            frontmatter = yaml.safe_load(parts[1])
                            title = frontmatter.get("title")
                            
                            if title:
                                with open(pages_path, "w", encoding="utf-8") as p:
                                    p.write(f"title: {title}\n")
                                log.info(f"Auto-created .pages for: {root}")
                except Exception as e:
                    log.warning(f"Could not process {full_index_path}: {e}")