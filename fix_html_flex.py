import glob
import os

html_files = glob.glob(r'anatomy modules\*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the broken CSS
    new_content = content.replace('display: flex; position: fixed;', 'display: flex;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Successfully fixed {len(html_files)} HTML modules.")
