import os
import glob
import re

base_dir = r"c:\Users\sayan\Downloads\biochem Note X"

# 1. Clean up residual rotate(90deg) on .flow-arrow and .arrow
css_files = glob.glob(os.path.join(base_dir, "**", "*.css"), recursive=True)
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

pattern_css_inline = re.compile(r'(?:\.flow-arrow|\.arrow)[^\{]*\{[^\}]*?transform:\s*rotate\(90deg\)[^;]*;?[^\}]*\}', re.IGNORECASE)

modified_count = 0

for file in css_files + html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Removing the specific rotate(90deg) property from the rules, or just replacing it with transform: none
    # Since regexing CSS rules is tricky, let's just find "transform: rotate(90deg)" and if it's near .flow-arrow, we kill it.
    # Actually, a simpler way is to replace "transform: rotate(90deg);" with "/* transform removed */" 
    # BUT only inside .flow-arrow or .arrow blocks.
    
    # Let's replace ANY "transform: rotate(90deg);" or "transform: rotate(90deg) !important;" 
    # that happens right after .arrow or .flow-arrow
    # Since these are often in media queries:
    # @media (max-width: 768px) { .flow-arrow, .arrow { transform: rotate(90deg); ... } }
    
    # We can just use re.sub on the property if it's in the file, but we don't want to break other rotations (like details summary).
    # "details[open]>summary::before{transform:rotate(90deg);}" -> we want to keep this!
    
    content = re.sub(r'(\.flow-arrow[\s,]*\.arrow|\.arrow[\s,]*\.flow-arrow|\.flow-arrow|\.arrow)\s*\{([^}]*?)transform\s*:\s*rotate\(90deg\)[^;}]*;?', r'\1 {\2', content)
    content = re.sub(r'(\.flow-arrow[\s,]*\.arrow|\.arrow[\s,]*\.flow-arrow|\.flow-arrow|\.arrow)\s*\{([^}]*?)transform\s*:\s*rotate\(90deg\)[^;}]*;?', r'\1 {\2', content)

    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        modified_count += 1
        print(f"Removed rotate(90deg) from {file}")

print(f"Cleaned {modified_count} files for rotate(90deg).")
