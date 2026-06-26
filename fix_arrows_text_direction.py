import os
import glob
import re

base_dir = r"c:\Users\sayan\Downloads\biochem Note X"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

arrow_chars = r'[→←↙↓↑]+'
pattern1 = re.compile(r'(<div\s+class="[^"]*?\bflow-arrow\b[^"]*">)(\s*)(' + arrow_chars + r')')
pattern2 = re.compile(r'(<div\s+class="[^"]*?\barrow\b[^"]*">)(\s*)(' + arrow_chars + r')')

# Pattern for the hl and step-num inversion
# Match: <li class="hl">\s*<span class="step-num">
# Replace: <li>\s*<span class="step-num hl">
pattern_hl = re.compile(r'<li\s+class="hl">(\s*)<span\s+class="step-num">')

modified_count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Apply arrow wrapping
    content = pattern1.sub(r'\1\2<span class="dir-arrow">\3</span>', content)
    content = pattern2.sub(r'\1\2<span class="dir-arrow">\3</span>', content)
    
    # Apply color inversion
    content = pattern_hl.sub(r'<li>\g<1><span class="step-num hl">', content)
    
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Modified: {file}")
        modified_count += 1

print(f"Total files modified: {modified_count}")

# Append the CSS for .dir-arrow to the global CSS files
css_files = glob.glob(os.path.join(base_dir, "**", "wbuhs_master_style.css"), recursive=True)
css_addition = """
/* Fix for mobile arrows: only rotate the arrow character, not the text */
@media (max-width: 768px) {
  .flow-arrow .dir-arrow, .arrow .dir-arrow {
    display: inline-block;
    transform: rotate(90deg);
  }
}
"""

for css_file in css_files:
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    if "dir-arrow" not in css_content:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write(css_addition)
        print(f"Updated CSS: {css_file}")

print("Done!")
