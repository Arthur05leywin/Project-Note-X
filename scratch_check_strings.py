import os
import re

html_path = r"c:\Users\sayan\Downloads\biochem Note X\modules\module-02\carb_metabolism_notes.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style\b[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
if style_match:
    css = style_match.group(1)
    
    # Strip comments to avoid counting quotes inside comments
    # CSS comment regex: /\*.*?\*/
    css_no_comments = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    
    single_quotes = css_no_comments.count("'")
    double_quotes = css_no_comments.count('"')
    
    print(f"Quotes count (excluding comments):")
    print(f"  Single quotes: {single_quotes} (even? {single_quotes % 2 == 0})")
    print(f"  Double quotes: {double_quotes} (even? {double_quotes % 2 == 0})")
    
    # Let's check where the quotes are used
    if single_quotes % 2 != 0 or double_quotes % 2 != 0:
        print("\nPossible unclosed string! Printing lines with quotes:")
        lines = css_no_comments.splitlines()
        for idx, line in enumerate(lines):
            if "'" in line or '"' in line:
                print(f"{idx+1}: {line}")
else:
    print("No style tag found.")
