import os
import re

html_path = r"c:\Users\sayan\Downloads\biochem Note X\modules\module-02\carb_metabolism_notes.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style\b[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
if style_match:
    css = style_match.group(1)
    print("FIRST 500 CHARACTERS:")
    print(css[:500])
    print("\nLAST 500 CHARACTERS:")
    print(css[-500:])
else:
    print("No style tag found.")
