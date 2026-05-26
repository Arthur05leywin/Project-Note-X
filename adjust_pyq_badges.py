import re
from pathlib import Path

ROOT = Path(r"c:\Users\sayan\Downloads\biochem Note X")

print("=" * 60)
print("  Adjusting PYQ Badges to Clear the Brand Bar")
print("=" * 60)

# Pattern for the main cover-pyq-badge styling block
# Looks for .cover-pyq-badge { ... top: 60px; ... }
MAIN_PATTERN = re.compile(
    r'(\.cover-pyq-badge\s*\{[^}]*?top:\s*)60px(\s*;[^}]*?\})',
    re.DOTALL
)

# Pattern for the print media query override of cover-pyq-badge
# Looks for top: 40px !important; inside .cover-pyq-badge block
PRINT_PATTERN = re.compile(
    r'(\.cover-pyq-badge\s*\{[^}]*?top:\s*)40px\s*!important(\s*;[^}]*?\})',
    re.DOTALL
)

html_modified = 0
css_modified = 0

# Find all HTML and CSS files
all_files = list(ROOT.glob("modules/**/*.html")) + list(ROOT.glob("modules/**/*.css")) + [ROOT / "wbuhs_master_style.css"]

for path in sorted(all_files):
    if not path.is_file():
        continue
        
    content = path.read_text(encoding="utf-8")
    new_content = content
    
    # 1. Replace main standard top value
    new_content, count_main = MAIN_PATTERN.subn(r'\1120px\2', new_content)
    
    # 2. Replace print top value
    new_content, count_print = PRINT_PATTERN.subn(r'\170px !important\2', new_content)
    
    if count_main > 0 or count_print > 0:
        path.write_text(new_content, encoding="utf-8")
        if path.suffix == ".html":
            html_modified += 1
            print(f"[UPDATED HTML] {path.relative_to(ROOT)} (Standard: {count_main}, Print: {count_print})")
        else:
            css_modified += 1
            print(f"[UPDATED CSS ] {path.relative_to(ROOT)} (Standard: {count_main}, Print: {count_print})")

print("\n" + "=" * 60)
print("  ADJUSTMENT SUMMARY")
print("=" * 60)
print(f"  Modified HTML files : {html_modified}")
print(f"  Modified CSS files  : {css_modified}")
print("=" * 60)
