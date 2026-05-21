import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\sayan\Downloads\biochem Note X\BIOCHEM_MODULE_4\module04_protein_haemoglobin.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all div tags with their class names
divs = re.findall(r'<div\s+class="([^"]+)"', content)
unique_div_classes = sorted(list(set(divs)))
print("=== UNIQUE DIV CLASSES ===")
for c in unique_div_classes:
    print(c)
