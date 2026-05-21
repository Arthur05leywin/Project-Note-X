import re

html_path = "module04_protein_haemoglobin.html"
css_path = "wbuhs_master_style.css"

# 1. Update module04_protein_haemoglobin.html
print("Reading HTML...")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace KIMS title
print("Replacing title tag...")
html_content = html_content.replace(
    "<title>\n      Module 04 \u2014 Protein Chemistry & Haemoglobin | KIMS Biochem Notes\n    </title>",
    "<title>\n      Module 04 \u2014 Protein Chemistry & Haemoglobin | WBUHS Biochemistry Notes\n    </title>"
)
# Support potential alternate whitespace variations
html_content = re.sub(
    r'<title>\s*Module 04 — Protein Chemistry & Haemoglobin \| KIMS Biochem Notes\s*</title>',
    '<title>Module 04 — Protein Chemistry & Haemoglobin | WBUHS Biochemistry Notes</title>',
    html_content,
    flags=re.DOTALL
)

# Replace hero-sub
print("Replacing hero subtitle...")
html_content = html_content.replace(
    '<p class="hero-sub">WBUHS BIOCHEMISTRY \xb7 PAPER 1 \xb7 KIMS KRISHNANAGAR</p>',
    '<p class="hero-sub">WBUHS BIOCHEMISTRY \xb7 PAPER 1</p>'
)

# Replace footer markup
print("Replacing footer markup...")
old_footer = """    <!-- FOOTER -->
    <div class="footer">
      <p>MODULE 04 \xb7 PROTEIN CHEMISTRY & HAEMOGLOBIN</p>
      <p style="margin-top: 4px">
        KIMS Krishnanagar Biochem Notes \xb7 WBUHS \xb7 NMO Bengal PYQs 2010\u20132025
      </p>
      <p style="margin-top: 4px; color: var(--accent); font-size: 11px">
        Compiled for personal academic use
      </p>
    </div>"""

new_footer = """    <!-- FOOTER -->
    <div class="footer">
      <div class="footer-title">WBUHS Biochemistry \u2013 Module 04: Protein Chemistry & Haemoglobin</div>
      <div class="footer-sub">Compiled from PYQ 2010\u20132025</div>
      <div class="footer-desc">
        Crafted with precision to illuminate the pathways of biochemistry and inspire your journey in medicine.
      </div>
      <div>
        <div class="footer-badge">Made with <span class="footer-heart">\u2764\ufe0f</span> for you</div>
      </div>
      <div class="footer-version">Version 1.0 \xb7 Clean Print Edition available separately</div>
    </div>"""

if old_footer in html_content:
    html_content = html_content.replace(old_footer, new_footer)
    print("Direct footer string replaced successfully!")
else:
    # Use re.sub to handle any slight whitespace variation
    html_content = re.sub(
        r'<!-- FOOTER -->\s*<div class="footer">.*?</div>',
        new_footer,
        html_content,
        flags=re.DOTALL
    )
    print("Footer replaced via regex.")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)


# 2. Update wbuhs_master_style.css
print("Reading CSS...")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Replace .footer { ... }
print("Replacing CSS footer style...")
old_css_footer = """      .footer {
        background: var(--surface);
        border-top: 1px solid var(--border);
        text-align: center;
        padding: 2rem 1.5rem;
        color: var(--text3);
        font-size: 12px;
        font-family: "JetBrains Mono", monospace;
      }"""

new_css_footer = """      .footer {
        background: #07070b;
        border-top: 1px solid var(--border);
        text-align: center;
        padding: 3rem 1.5rem;
        font-family: "JetBrains Mono", monospace;
        display: flex;
        flex-direction: column;
        gap: 12px;
        align-items: center;
      }
      .footer-title {
        color: var(--text);
        font-weight: 600;
        font-size: 14px;
        letter-spacing: 0.5px;
      }
      .footer-sub {
        color: var(--text3);
        font-size: 12px;
      }
      .footer-desc {
        color: var(--teal);
        font-style: italic;
        font-size: 12.5px;
        max-width: 600px;
        margin: 4px auto;
        line-height: 1.6;
      }
      .footer-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        border: 1px solid rgba(78, 205, 196, 0.4);
        background: rgba(78, 205, 196, 0.05);
        color: var(--teal);
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 12px;
        font-weight: 500;
        margin: 8px 0;
        transition: all 0.3s ease;
        cursor: default;
      }
      .footer-badge:hover {
        border-color: var(--teal);
        background: rgba(78, 205, 196, 0.1);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(78, 205, 196, 0.15);
      }
      .footer-heart {
        display: inline-block;
        font-size: 11px;
        animation: heartbeat 1.5s infinite;
      }
      @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
      }
      .footer-version {
        color: var(--text3);
        font-size: 10px;
        margin-top: 4px;
      }"""

if old_css_footer in css_content:
    css_content = css_content.replace(old_css_footer, new_css_footer)
    print("Direct CSS footer replaced successfully!")
else:
    css_content = re.sub(
        r'\.footer\s*\{[^}]*\}',
        new_css_footer,
        css_content,
        flags=re.DOTALL
    )
    print("CSS footer replaced via regex.")

# Add print overrides for footer at the end of @media print block
print("Appending print overrides for footer...")
end_viva = """        .viva-a-text {
          display: block !important;
          color: #111111 !important;
          border-left: 2px solid #88888d !important;
          padding-left: 12px !important;
          margin-top: 4px !important;
          margin-left: 0 !important;
        }"""

end_viva_with_footer = """        .viva-a-text {
          display: block !important;
          color: #111111 !important;
          border-left: 2px solid #88888d !important;
          padding-left: 12px !important;
          margin-top: 4px !important;
          margin-left: 0 !important;
        }

        .footer {
          background: #ffffff !important;
          border-top: 1.5px solid #000000 !important;
          color: #000000 !important;
          padding: 20px 0 !important;
        }
        .footer-title, .footer-sub, .footer-desc, .footer-version {
          color: #000000 !important;
        }
        .footer-badge {
          border: 1px solid #000000 !important;
          background: #ffffff !important;
          color: #000000 !important;
        }"""

if end_viva in css_content:
    css_content = css_content.replace(end_viva, end_viva_with_footer)
    print("Print overrides appended successfully!")
else:
    # Safe fallback: find the last closing bracket and insert before it
    last_idx = css_content.rstrip().rfind("}")
    if last_idx != -1:
        css_content = css_content[:last_idx] + "\n        /* Print overrides for footer */\n        .footer { background: #ffffff !important; border-top: 1.5px solid #000000 !important; color: #000000 !important; padding: 20px 0 !important; }\n        .footer-title, .footer-sub, .footer-desc, .footer-version { color: #000000 !important; }\n        .footer-badge { border: 1px solid #000000 !important; background: #ffffff !important; color: #000000 !important; }\n" + css_content[last_idx:]
        print("Print overrides appended to last closing bracket fallback.")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)

print("SUCCESS: Finished all replacements for KIMS, NMO, and Premium Footer!")
