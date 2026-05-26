import re
from pathlib import Path

ROOT = Path(r"c:\Users\sayan\Downloads\biochem Note X")

print("=" * 60)
print("  Fixing Mangled PYQ Badge Styles & Restoring CSS Validity")
print("=" * 60)

# Pattern to find the mangled standard block
MANGLED_STANDARD_PATTERN = re.compile(
    r'\.cover-pyq-badge\s*\{\s*position:\s*absolute\s*;\s*J0px\s*;\s*right:\s*60px\s*;',
    re.IGNORECASE
)

# Pattern to find the mangled print block
MANGLED_PRINT_PATTERN = re.compile(
    r'xpx\s*!important\s*;\s*right:\s*40px\s*!important\s*;\s*border:\s*1px\s*solid\s*#000000\s*!important\s*;\s*background:\s*#ffffff\s*!important\s*;\s*padding:\s*6px\s*12px\s*!important\s*;\s*font-size:\s*10px\s*!important\s*;\s*\}',
    re.IGNORECASE
)

# Correct replacements
CORRECT_STANDARD = (
    ".cover-pyq-badge {\n"
    "  position: absolute;\n"
    "  top: 120px;\n"
    "  right: 60px;"
)

CORRECT_PRINT = (
    ".cover-pyq-badge {\n"
    "    position: absolute !important;\n"
    "    top: 70px !important;\n"
    "    right: 40px !important;\n"
    "    border: 1px solid #000000 !important;\n"
    "    background: #ffffff !important;\n"
    "    padding: 6px 12px !important;\n"
    "    font-size: 10px !important;\n"
    "  }"
)

html_fixed = 0
css_fixed = 0

all_files = list(ROOT.glob("modules/**/*.html")) + list(ROOT.glob("modules/**/*.css")) + [ROOT / "wbuhs_master_style.css"]

for path in sorted(all_files):
    if not path.is_file():
        continue
        
    content = path.read_text(encoding="utf-8")
    new_content = content
    
    # 1. Fix standard block
    new_content, count_std = MANGLED_STANDARD_PATTERN.subn(CORRECT_STANDARD, new_content)
    
    # 2. Fix print block
    new_content, count_print = MANGLED_PRINT_PATTERN.subn(CORRECT_PRINT, new_content)
    
    if count_std > 0 or count_print > 0:
        path.write_text(new_content, encoding="utf-8")
        if path.suffix == ".html":
            html_fixed += 1
            print(f"[FIXED HTML] {path.relative_to(ROOT)} (Std: {count_std}, Print: {count_print})")
        else:
            css_fixed += 1
            print(f"[FIXED CSS ] {path.relative_to(ROOT)} (Std: {count_std}, Print: {count_print})")
    else:
        # Let's check if there is any partial match or if we need a more flexible regex
        # Just in case whitespace/formatting is slightly different
        flexible_std = re.sub(r'\s+', r'\\s*', r'.cover-pyq-badge { position: absolute; J0px; right: 60px;')
        flexible_print = re.sub(r'\s+', r'\\s*', r'xpx !important; right: 40px !important; border: 1px solid #000000 !important; background: #ffffff !important; padding: 6px 12px !important; font-size: 10px !important; }')
        
        count_std_flex = 0
        count_print_flex = 0
        
        # Try a more general regex replacement
        general_std_pat = re.compile(r'\.cover-pyq-badge\s*\{\s*position:\s*absolute\s*;\s*J0px\s*;', re.IGNORECASE)
        new_content, count_std_flex = general_std_pat.subn(CORRECT_STANDARD, new_content)
        
        general_print_pat = re.compile(r'xpx\s*!important\s*;\s*right:\s*40px\s*!important\s*;', re.IGNORECASE)
        # Note: we need to replace the entire print block to close the brace correctly
        # Let's construct a pattern that matches up to the closing brace
        general_print_block_pat = re.compile(
            r'xpx\s*!important\s*;\s*right:\s*40px\s*!important\s*;\s*border:[^;]+;\s*background:[^;]+;\s*padding:[^;]+;\s*font-size:[^;]+;\s*\}',
            re.IGNORECASE
        )
        new_content, count_print_flex = general_print_block_pat.subn(CORRECT_PRINT, new_content)
        
        if count_std_flex > 0 or count_print_flex > 0:
            path.write_text(new_content, encoding="utf-8")
            if path.suffix == ".html":
                html_fixed += 1
                print(f"[FLEX FIXED HTML] {path.relative_to(ROOT)} (Std: {count_std_flex}, Print: {count_print_flex})")
            else:
                css_fixed += 1
                print(f"[FLEX FIXED CSS ] {path.relative_to(ROOT)} (Std: {count_std_flex}, Print: {count_print_flex})")

print("\n" + "=" * 60)
print("  FIX SUMMARY")
print("=" * 60)
print(f"  Fixed HTML files : {html_fixed}")
print(f"  Fixed CSS files  : {css_fixed}")
print("=" * 60)
