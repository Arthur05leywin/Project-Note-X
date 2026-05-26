import os
import re

html_path = r"c:\Users\sayan\Downloads\biochem Note X\modules\module-02\carb_metabolism_notes.html"
with open(html_path, 'r', encoding='utf-8') as f:
    head_content = f.read().split("</head>")[0]

# Count <!-- and -->
open_comments = head_content.count("<!--")
close_comments = head_content.count("-->")
print(f"HTML Head Comments: <!-- count: {open_comments}, --> count: {close_comments}")

if open_comments != close_comments:
    print("WARNING: Unmatched HTML comments in head!")
    # Find positions
    for m in re.finditer(r'<!--|-->', head_content):
        print(f"Found '{m.group()}' at character index {m.start()}")
else:
    print("HTML comments in head are balanced.")
