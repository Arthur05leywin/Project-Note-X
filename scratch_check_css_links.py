import os

ROOT_DIR = r"c:\Users\sayan\Downloads\biochem Note X"

for root, dirs, files in os.walk(os.path.join(ROOT_DIR, "modules")):
    for file in files:
        if file.lower().endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            has_link = "wbuhs_master_style.css" in content
            print(f"File: {os.path.relpath(path, ROOT_DIR)} - Has stylesheet link: {has_link}")
