import os
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MASTER_CSS_PATH = os.path.join(ROOT_DIR, "wbuhs_master_style.css")

def load_master_css():
    if not os.path.exists(MASTER_CSS_PATH):
        raise FileNotFoundError(f"Master CSS not found at {MASTER_CSS_PATH}")
    with open(MASTER_CSS_PATH, 'r', encoding='utf-8') as f:
        return f.read().strip()

def get_theme_for_html(relative_path):
    path_lower = relative_path.lower().replace("\\", "/")
    
    # 1. Module 4 -> theme-crimson
    if "module-04" in path_lower:
        return "theme-crimson"
        
    # 2. Module 5 -> emerald for normal, gold for classic (_x)
    elif "module-05" in path_lower:
        if "_x.html" in path_lower:
            return "theme-gold"
        else:
            return "theme-emerald"
            
    # 3. Module 7 -> theme-amber
    elif "module-07" in path_lower:
        return "theme-amber"
        
    # 4. Modules 6, 8, 9, 10 -> theme-indigo
    elif any(m in path_lower for m in ["module-06", "module-08", "module-09", "module-10"]):
        return "theme-indigo"
        
    # 5. Classic Modules 1, 2, 3 -> theme-gold
    elif any(m in path_lower for m in ["module-01", "module-02", "module-03"]):
        return "theme-gold"
        
    # Default fallback
    return "theme-gold"

def update_body_tag(html_content, theme_class):
    # Match <body ...> case-insensitively
    body_match = re.search(r'(<body\b[^>]*>)', html_content, flags=re.IGNORECASE)
    if not body_match:
        return html_content, False
        
    original_body_tag = body_match.group(1)
    
    # Check if class attribute exists in the body tag
    if 'class=' in original_body_tag.lower():
        # Replace existing class attribute value with theme_class
        new_body_tag = re.sub(r'class=["\'][^"\']*["\']', f'class="{theme_class}"', original_body_tag, flags=re.IGNORECASE)
        # Handle unquoted class attribute if any
        new_body_tag = re.sub(r'class=[^\s>]+', f'class="{theme_class}"', new_body_tag, flags=re.IGNORECASE)
    else:
        # Inject class attribute right after "<body"
        new_body_tag = re.sub(r'<body\b', f'<body class="{theme_class}"', original_body_tag, flags=re.IGNORECASE)
        
    return html_content.replace(original_body_tag, new_body_tag), True

def propagate():
    print("======================================================================")
    print("[START] Starting Unified Biochemistry Note Module Synchronization...")
    print("======================================================================")
    
    try:
        master_css = load_master_css()
    except Exception as e:
        print(f"[ERROR] Error loading master CSS: {e}")
        return

    css_updated_count = 0
    html_updated_count = 0

    # Walk through only the modules directory
    for root, dirs, files in os.walk(os.path.join(ROOT_DIR, "modules")):
        # Ignore scratch/temp/internal/git folders to keep execution neat
        dirs[:] = [d for d in dirs if d.lower() not in ['.git', 'scratch', 'temp', 'node_modules', '.gemini']]
        
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, ROOT_DIR)

            # 1. Update duplicate stylesheets
            if file.lower() == "wbuhs_master_style.css" and file_path != MASTER_CSS_PATH:
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(master_css)
                    print(f"[CSS] Synced stylesheet copy: {relative_path}")
                    css_updated_count += 1
                except Exception as e:
                    print(f"[ERROR] Failed to sync CSS {relative_path}: {e}")

            # 2. Update and clean up HTML inlined stylesheets
            elif file.lower().endswith(".html"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        html_content = f.read()

                    # A. Determine correct theme for this file
                    theme_class = get_theme_for_html(relative_path)

                    # B. Find how many style blocks exist before removing
                    style_blocks = re.findall(r'<style\b[^>]*>.*?</style>', html_content, flags=re.DOTALL | re.IGNORECASE)
                    style_count = len(style_blocks)

                    # C. Remove ALL existing style blocks to prevent duplicates or residues
                    cleaned_html = re.sub(r'<style\b[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

                    # D. Inject single clean stylesheet right before </head>
                    head_match = re.search(r'</\s*head\s*>', cleaned_html, flags=re.IGNORECASE)
                    if head_match:
                        idx = head_match.start()
                        # Add fallback external link if missing
                        if "wbuhs_master_style.css" not in cleaned_html:
                            new_style_block = f"    <link rel=\"stylesheet\" href=\"wbuhs_master_style.css\">\n    <style>\n{master_css}\n    </style>\n"
                        else:
                            new_style_block = f"    <style>\n{master_css}\n    </style>\n"
                        final_html = cleaned_html[:idx] + new_style_block + cleaned_html[idx:]
                        
                        # E. Inject or update the body theme class
                        final_html, body_updated = update_body_tag(final_html, theme_class)
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(final_html)
                        
                        body_status = f"with {theme_class}" if body_updated else "body class injection skipped"
                        print(f"[HTML] Synced: {relative_path}")
                        print(f"       - Cleaned: {style_count} style block(s) -> inlined 1 master block")
                        print(f"       - Theme: {body_status}")
                        html_updated_count += 1
                    else:
                        print(f"[WARNING] No </head> tag found in {relative_path}. Skipped processing.")

                except Exception as e:
                    print(f"[ERROR] Failed to process HTML {relative_path}: {e}")

    print("======================================================================")
    print("[SUCCESS] Multi-Theme CSS Propagation Completed Successfully!")
    print(f"Summary: Synced {css_updated_count} CSS files & optimized {html_updated_count} HTML pages.")
    print("======================================================================")

if __name__ == "__main__":
    propagate()
