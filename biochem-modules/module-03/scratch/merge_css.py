import re

html_path = r"c:\Users\sayan\Downloads\biochem Note X\BIOCHEM_MODULE_4\module04_protein_haemoglobin.html"
instruction_path = r"c:\Users\sayan\Downloads\biochem Note X\BIOCHEM_MODULE_4\instruction.md"
output_css_path = r"c:\Users\sayan\Downloads\biochem Note X\BIOCHEM_MODULE_4\wbuhs_master_style.css"

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Extract style block content
style_match = re.search(r'<style>(.*?)</style>', html_content, re.DOTALL)
if not style_match:
    raise ValueError("No style block found in HTML!")

style_content = style_match.group(1)

# Remove the old @media print block
# The print block starts with /* ── PRINT ── */ or @media print
print_start = style_content.find('@media print')
if print_start != -1:
    # Find the preceding comment if any
    comment_idx = style_content[:print_start].rfind('/* ── PRINT ── */')
    if comment_idx != -1:
        style_content = style_content[:comment_idx]
    else:
        style_content = style_content[:print_start]

# Strip trailing whitespaces
style_content = style_content.strip()

# 2. Extract print blueprint from instruction.md
with open(instruction_path, 'r', encoding='utf-8') as f:
    instruction_content = f.read()

# Find the print blueprint block (between ```css and ```)
print_code_match = re.search(r'```css\s+(/\* 🖨️ PREMIUM PRINT TO PDF RULES.*?)```', instruction_content, re.DOTALL)
if not print_code_match:
    raise ValueError("No print blueprint found in instruction.md!")

print_blueprint = print_code_match.group(1).strip()

# 3. Custom helper rules (big-picture, key-fact) to keep
big_picture_css = """
/* BIG PICTURE BOX */
.big-picture {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 24px;
  margin-bottom: 28px;
}

.big-picture-label {
  font-family: "IBM Plex Mono", monospace;
  font-size: 10px;
  color: var(--accent2);
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 10px;
}

/* KEY FACT HIGHLIGHT */
.key-fact {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  background: var(--surface);
  border-radius: 6px;
  padding: 14px 18px;
  margin: 10px 0;
}

.key-fact-icon {
  font-size: 16px;
  margin-top: 1px;
  flex-shrink: 0;
}

.key-fact-text {
  font-size: 13px;
  line-height: 1.7;
}

.key-fact-text strong {
  color: var(--accent);
}
"""

# 4. Construct the complete stylesheet
full_css = f"""@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&family=Crimson+Pro:ital,wght@0,400;0,600;1,400&display=swap');

{style_content}

{big_picture_css}

{print_blueprint}
"""

with open(output_css_path, 'w', encoding='utf-8') as f:
    f.write(full_css)

print("SUCCESS: wbuhs_master_style.css has been compiled successfully!")
