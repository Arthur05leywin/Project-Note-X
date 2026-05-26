"""
resize_brand_bar.py
===================
Updates the .brand-bar CSS across all 20 module HTML files
to make the bar visually larger and more prominent.
"""

import re
from pathlib import Path

ROOT = Path(r"c:\Users\sayan\Downloads\biochem Note X\modules")

OLD_CSS_PATTERN = re.compile(
    r'/\* ─── Premium Brand Bar ─────────────────────────────── \*/.*?/\* ──────────────────────────────────────────────────── \*/',
    re.DOTALL
)

NEW_CSS = """\
/* ─── Premium Brand Bar ─────────────────────────────── */
.brand-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 18px 60px;
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  z-index: 10;
}

.brand-bar-logo {
  height: 56px;
  width: auto;
  border-radius: 6px;
  object-fit: contain;
  flex-shrink: 0;
  box-shadow: 0 2px 12px rgba(0,0,0,0.4);
}

.brand-bar-text {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.brand-bar-name {
  font-family: "IBM Plex Mono", "JetBrains Mono", monospace;
  font-size: 15px;
  font-weight: 700;
  color: var(--accent, #e8c84a);
  letter-spacing: 3px;
  text-transform: uppercase;
}

.brand-bar-series {
  font-family: "IBM Plex Mono", "JetBrains Mono", monospace;
  font-size: 11px;
  color: rgba(255, 255, 255, 0.5);
  letter-spacing: 2px;
  text-transform: uppercase;
}

@media print {
  .brand-bar {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    background: #f8f9fa !important;
    border-bottom: 1px solid #dee2e6 !important;
    padding: 10px 40px !important;
    backdrop-filter: none !important;
  }
  .brand-bar-logo {
    height: 32px !important;
    filter: grayscale(100%) !important;
  }
  .brand-bar-name {
    color: #000000 !important;
    font-size: 11px !important;
    letter-spacing: 2px !important;
  }
  .brand-bar-series {
    color: #495057 !important;
    font-size: 9px !important;
  }
}
/* ──────────────────────────────────────────────────── */"""

updated = []
not_found = []

for html_file in sorted(ROOT.glob("*/*.html")):
    content = html_file.read_text(encoding="utf-8")
    new_content = OLD_CSS_PATTERN.sub(NEW_CSS, content)
    if new_content != content:
        html_file.write_text(new_content, encoding="utf-8")
        updated.append(html_file.name)
    else:
        not_found.append(html_file.name)

print("=" * 50)
print("  Brand Bar Resize — Report")
print("=" * 50)
print(f"  Updated : {len(updated)} files")
for f in updated:
    print(f"    + {f}")
if not_found:
    print(f"  Skipped : {len(not_found)} (pattern not found)")
    for f in not_found:
        print(f"    - {f}")
print("=" * 50)
