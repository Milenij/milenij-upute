import os
import yaml # pip install pyyaml

# 1. Get the folder where THIS script lives (e.g., .../my-project/hooks)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Go up one level to the Project Root (e.g., .../my-project)
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# 3. Find the docs folder from the root
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")

print(f"--- 🚀 Script Started ---")
print(f"📍 Script location: {SCRIPT_DIR}")
print(f"🏠 Project Root detected: {PROJECT_ROOT}")
print(f"🔎 Scanning Docs Directory: {DOCS_DIR}")

if not os.path.exists(DOCS_DIR):
    print(f"❌ ERROR: Still cannot find docs folder at: {DOCS_DIR}")
    exit()

files_found = 0

for root, dirs, files in os.walk(DOCS_DIR):
    if "index.md" in files:
        full_index_path = os.path.join(root, "index.md")
        
        try:
            with open(full_index_path, "r", encoding="utf-8") as f:
                content = f.read()
                parts = content.split("---")
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    title = frontmatter.get("title")
                    
                    if title:
                        pages_path = os.path.join(root, ".pages")
                        if not os.path.exists(pages_path):
                            with open(pages_path, "w", encoding="utf-8") as p:
                                p.write(f"title: {title}\n")
                            print(f"   ✅ Created .pages for: {os.path.basename(root)} -> '{title}'")
                            files_found += 1
                        else:
                            # Optional: Uncomment below to see what is skipped
                            # print(f"   ⚠️  Skipped {root} (.pages exists)")
                            pass
        except Exception as e:
            print(f"   ❌ Error reading {full_index_path}: {e}")

print(f"\n--- 🏁 Finished. Created {files_found} new .pages files. ---")