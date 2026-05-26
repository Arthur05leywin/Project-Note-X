import os
import re

ROOT_DIR = r"c:\Users\sayan\Downloads\biochem Note X"

for root, dirs, files in os.walk(os.path.join(ROOT_DIR, "modules")):
    for file in files:
        if file.lower().endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            style_matches = re.findall(r'<style\b[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
            print(f"File: {os.path.relpath(path, ROOT_DIR)}")
            print(f"  Style tags count: {len(style_matches)}")
            for idx, sm in enumerate(style_matches):
                print(f"    Style tag {idx+1} length: {len(sm)} characters")
                open_comments = sm.count("/*")
                close_comments = sm.count("*/")
                open_braces = sm.count("{")
                close_braces = sm.count("}")
                print(f"    Comments: {open_comments}/{close_comments}, Braces: {open_braces}/{close_braces}")
