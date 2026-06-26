import os
import re

root_dir = r"c:\Users\sayan\Downloads\biochem Note X"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # CSS Classes
    targets = ['.mnemonic-highlight', '.flow-box', '.clinical-box', '.viva-ans', '.keypoint', '.warn-box', '.couinaud-seg']
    
    for target in targets:
        # Match class definition with or without space before brace
        # Use a regex that finds the class and inserts the properties right after the opening brace
        pattern = re.compile(r'(' + re.escape(target) + r'\s*\{)')
        content = pattern.sub(r'\1 word-break: break-word; overflow-wrap: break-word; ', content)
    
    # General body fallback
    content = re.compile(r'(body\s*\{)').sub(r'\1 overflow-wrap: break-word; word-break: break-word; ', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed CSS in: {filepath}")

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html') or file.endswith('.css'):
            process_file(os.path.join(root, file))

print("CSS rendering fix completed across all HTML and CSS files.")
