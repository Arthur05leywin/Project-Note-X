import re

file_path = "anatomy.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacement = '''<div style="display: flex; gap: 10px; align-items: center;">
          <span style="font-family: 'IBM Plex Mono', monospace; font-size: 12px; font-weight: 600; color: var(--white);">₹49</span>
          <span class="module-arrow">→</span>
        </div>'''

content = content.replace('<span class="module-arrow">→</span>', replacement)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added ₹49 price tags to anatomy.html")
