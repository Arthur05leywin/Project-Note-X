import os
import re

html_path = r"c:\Users\sayan\Downloads\biochem Note X\modules\module-03\lipid_metabolism_notes_X.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find h2 tags with class="section-title" or similar
# Let's extract the surrounding lines or just the text
matches = re.finditer(r'<div class="section-header"[^>]*>.*?<span class="section-number">(\d+)</span>.*?<h2 class="section-title">(.*?)</h2>', content, re.DOTALL | re.IGNORECASE)

print("MODULE 03 STANDARD SECTIONS:")
for m in matches:
    num = m.group(1)
    title_raw = m.group(2)
    # Strip HTML tags
    title = re.sub(r'<[^>]+>', '', title_raw).strip().replace("\n", " ").replace("  ", " ")
    text = f"Section {num}: {title}"
    print(text.encode('ascii', errors='replace').decode('ascii'))
