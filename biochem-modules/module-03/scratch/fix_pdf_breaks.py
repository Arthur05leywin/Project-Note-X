import re

css_path = "wbuhs_master_style.css"

print("Reading CSS...")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# 1. Replace the details print rule that avoids page breaks globally
old_details_rule = """  details.viva-q,
  details {
    display: block !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    margin-bottom: 15px !important;
    padding-bottom: 15px !important;
    border-bottom: 1px solid #e2e2e6 !important;
  }"""

new_details_rule = """  details {
    display: block !important;
  }

  .viva-section details {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    margin-bottom: 15px !important;
    padding-bottom: 15px !important;
    border-bottom: 1px solid #e2e2e6 !important;
  }"""

if old_details_rule in css_content:
    css_content = css_content.replace(old_details_rule, new_details_rule)
    print("Generic details page-break rule updated successfully!")
else:
    # Use regex replacement if spacing differed
    css_content = re.sub(
        r'details\.viva-q,\s*details\s*\{\s*display:\s*block\s*!important;\s*page-break-inside:\s*avoid\s*!important;\s*break-inside:\s*avoid\s*!important;\s*margin-bottom:\s*15px\s*!important;\s*padding-bottom:\s*15px\s*!important;\s*border-bottom:\s*1px\s*solid\s*#e2e2e6\s*!important;\s*\}',
        new_details_rule,
        css_content,
        flags=re.DOTALL
    )
    print("Generic details page-break rule updated via regex.")

# 2. Update details.viva-q:last-child to .viva-section details:last-child
css_content = css_content.replace("details.viva-q:last-child", ".viva-section details:last-child")

# 3. Add print overrides inside the @media print block
# Locate the last closing bracket of @media print (which is the last character in the file)
last_bracket_idx = css_content.rstrip().rfind("}")
if last_bracket_idx != -1:
    extra_print_overrides = """
  /* Extra Page Break & Clean Print Optimizations */
  .hero::before,
  .hero::after {
    display: none !important;
  }
  .hero {
    background: #ffffff !important;
    border-bottom: 2px solid #000000 !important;
    padding: 2rem 0 !important;
  }
  .module-tag {
    background: #ffffff !important;
    border: 1px solid #ff0000 !important;
    color: #ff0000 !important;
  }
  .module-tag .dot {
    display: none !important;
  }
  .pill {
    background: #ffffff !important;
    border: 1px solid #000000 !important;
    color: #000000 !important;
  }
  .top-btn,
  .progress-bar,
  .toc {
    display: none !important;
  }
"""
    css_content = css_content[:last_bracket_idx] + extra_print_overrides + "\n}"
    print("Extra print overrides appended successfully inside the media query!")
else:
    print("ERROR: Could not find matching closing bracket for print media query.")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)

print("SUCCESS: Finished PDF print spacing modifications!")
