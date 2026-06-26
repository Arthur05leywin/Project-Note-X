import os
import glob
import re
import base64
import urllib.request

base_dir = r"c:\Users\sayan\Downloads\biochem Note X"

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# ==========================================
# 1. Base64 Encode Logo and Inject into HTML
# ==========================================
logo_path = os.path.join(base_dir, "Caffeine & Cadaver.jpg")
if os.path.exists(logo_path):
    with open(logo_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    base64_src = f"data:image/jpeg;base64,{encoded_string}"
    
    html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)
    logo_patterns = [
        r'src=".*?Caffeine\s*&amp;\s*Cadaver\.jpg"',
        r'src=".*?Caffeine\s*&\s*Cadaver\.jpg"'
    ]
    for file in html_files:
        content = read_file(file)
        orig_content = content
        for pat in logo_patterns:
            content = re.sub(pat, f'src="{base64_src}"', content, flags=re.IGNORECASE)
        if content != orig_content:
            write_file(file, content)
            print(f"Injected base64 logo into {file}")
else:
    print("Logo not found.")

# ==========================================
# 2. Pyrimidine Soft Pastels
# ==========================================
module5_files = glob.glob(os.path.join(base_dir, "biochem-modules", "module-05", "*.html"))
for file in module5_files:
    content = read_file(file)
    # The user wants "soft pastels" instead of strong colors.
    # We will replace 'flow-box blue', 'flow-box accent', etc. with 'flow-box muted'
    if "Pyrimidine De Novo" in content:
        # Find the Pyrimidine pathway section
        start_idx = content.find('<!-- Pyrimidine pathway -->')
        if start_idx != -1:
            end_idx = content.find('</div>\n</div>\n<div class="clinical-box">', start_idx)
            if end_idx != -1:
                sub_content = content[start_idx:end_idx]
                # Replace classes
                sub_content = sub_content.replace('flow-box blue', 'flow-box muted')
                sub_content = sub_content.replace('flow-box accent', 'flow-box muted')
                sub_content = sub_content.replace('flow-box gold', 'flow-box muted')
                sub_content = sub_content.replace('flow-box green', 'flow-box muted')
                sub_content = sub_content.replace('flow-box rose', 'flow-box muted')
                
                content = content[:start_idx] + sub_content + content[end_idx:]
                write_file(file, content)
                print(f"Applied pastels to {file}")

# ==========================================
# 3. Clean up O2 Curve Congestion
# ==========================================
module4_files = glob.glob(os.path.join(base_dir, "biochem-modules", "module-04", "*.html"))
for file in module4_files:
    content = read_file(file)
    if 'Oxygen Dissociation Curves — Hb vs Mb vs HbF' in content:
        # Extract the legend rect and text from SVG and remove them
        # Let's just remove the rect and legend text completely from the SVG,
        # and instead prepend a clean HTML div with the info!
        
        legend_html = """
<div class="clinical-box" style="margin-bottom: 16px;">
  <strong>Right shift (↓ O₂ affinity):</strong> ↑ pCO₂, ↑ H⁺ (Bohr), ↑ temp, ↑ 2,3-BPG → T state<br>
  <strong>Left shift (↑ O₂ affinity):</strong> HbF, CO poisoning → R state
</div>
"""     
        # Remove the `<rect ...>` up to the end of the legend texts.
        # The legend block in SVG is exactly:
        # <!-- Legend box -->
        # ... up to </text> just before </svg>
        
        # We can use regex to remove the legend block
        pattern_legend = re.compile(r'<!-- Legend box -->.*?((?=</svg>)|(?=<!--))', re.DOTALL)
        if pattern_legend.search(content):
            new_content = pattern_legend.sub('', content)
            # Insert the HTML legend right BEFORE the SVG
            new_content = new_content.replace('<svg viewBox="0 0 500 340"', legend_html + '\n<svg viewBox="0 0 500 340"')
            write_file(file, new_content)
            print(f"Cleaned O2 Curve in {file}")

print("Script execution completed.")
