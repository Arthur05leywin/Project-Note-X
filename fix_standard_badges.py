import re
from pathlib import Path

ROOT = Path(r"c:\Users\sayan\Downloads\biochem Note X")

print("=" * 60)
print("  Fixing Standard Badge Selector & Restoring CSS Validity")
print("=" * 60)

# Pattern to find the mangled standard block
# It starts with J0px; and is followed by right: 60px; and background: var(--accent);
MANGLED_STANDARD_PATTERN = re.compile(
    r'J0px\s*;\s*right:\s*60px\s*;\s*background:\s*var\(--accent\)\s*;',
    re.IGNORECASE
)

# Correct replacement
CORRECT_STANDARD = (
    ".cover-pyq-badge {\n"
    "  position: absolute;\n"
    "  top: 120px;\n"
    "  right: 60px;\n"
    "  background: var(--accent);"
)

html_fixed = 0
css_fixed = 0

all_files = list(ROOT.glob("modules/**/*.html")) + list(ROOT.glob("modules/**/*.css")) + [ROOT / "wbuhs_master_style.css"]

for path in sorted(all_files):
    if not path.is_file():
        continue
        
    content = path.read_text(encoding="utf-8")
    new_content = content
    
    new_content, count = MANGLED_STANDARD_PATTERN.subn(CORRECT_STANDARD, new_content)
    
    if count > 0:
        path.write_text(new_content, encoding="utf-8")
        if path.suffix == ".html":
            html_fixed += 1
            print(f"[FIXED HTML] {path.relative_to(ROOT)} ({count} replacements)")
        else:
            css_fixed += 1
            print(f"[FIXED CSS ] {path.relative_to(ROOT)} ({count} replacements)")

print("\n" + "=" * 60)
print("  FIX SUMMARY")
print("=" * 60)
print(f"  Fixed HTML files : {html_fixed}")
print(f"  Fixed CSS files  : {css_fixed}")
print("=" * 60)
