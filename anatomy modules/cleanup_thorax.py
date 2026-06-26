import re

mod_path = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module04_thorax.html"

with open(mod_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove TOC link
html = re.sub(r'<a href="#s12"><span class="toc-num">12</span> Diagrams</a>\s*', '', html)

# 2. Fix footer text
html = html.replace("Replace diagram placeholders with tablet artwork", "Includes detailed anatomical diagrams")

# 3. Remove CSS
css_pattern = r'/\* DIAGRAM PLACEHOLDER \*/.*?\.diagram-placeholder\{.*?\}.*?\.diag-num\{.*?\}.*?\.diag-icon\{.*?\}.*?\.diag-desc\{.*?\}'
html = re.sub(css_pattern, '', html, flags=re.DOTALL)

with open(mod_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Cleanup completed.")
