import os
import glob

base_dir = r"c:\Users\sayan\Downloads\biochem Note X"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    content = content.replace(
        "transform: rotate(90deg) !important;\n    margin: 8px auto !important;",
        "transform: none !important;\n    margin: 8px auto !important;"
    )
    content = content.replace(
        "transform: rotate(90deg) !important;\n    margin: 8px 0 !important;",
        "transform: none !important;\n    margin: 8px auto !important;\n    width: 100% !important;"
    )
    # Just in case there's another variation with inline styles
    
    if content != original:
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file}")

print(f"Done processing {len(html_files)} HTML files.")
