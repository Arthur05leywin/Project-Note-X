import os
import glob
import re

base_dir = r"c:\Users\sayan\Downloads\biochem Note X"
css_files = glob.glob(os.path.join(base_dir, "**", "*.css"), recursive=True)

# Also HTML files that have inline styles
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

for fp in css_files + html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    # Replace margin-bottom: 4px; with margin-bottom: 14px; padding-bottom: 4px; inside ul.checklist li
    # We will use regex to find ul.checklist li {...} block and update it.
    # Actually, simpler: replace `margin-bottom: 4px;` with `margin-bottom: 12px;` in context of checklist
    # Or just inject a global override in css files
    if fp.endswith('.css'):
        if "/* Checklist spacing fix */" not in content:
            content += "\n/* Checklist spacing fix */\nul.checklist li {\n  margin-bottom: 14px !important;\n  line-height: 1.6 !important;\n}\n"
    elif fp.endswith('.html'):
        # Some html files have <style> tag with ul.checklist li { margin-bottom: 4px; }
        content = re.sub(
            r'ul\.checklist\s*li\s*\{\s*margin-bottom:\s*4px;',
            r'ul.checklist li { margin-bottom: 14px; line-height: 1.6;',
            content
        )
    
    if orig != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed checklist spacing in {fp}")

print("Done checklist spacing.")
