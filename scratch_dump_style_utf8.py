import os
import re

html_path = r"c:\Users\sayan\Downloads\biochem Note X\modules\module-02\carb_metabolism_notes.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style\b[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
if style_match:
    css = style_match.group(1)
    print("LAST 500 CHARACTERS (SAFELY):")
    # Replace non-cp1252 characters to print safely
    safe_css = css[-500:].encode('ascii', errors='replace').decode('ascii')
    print(safe_css)
else:
    print("No style tag found.")
