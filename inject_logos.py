"""
inject_logos.py
===============
Injects the Caffeine & Cadaver <img> tag into the HTML body
of every module 02-10 (both normal and Version X files).

- Modules 02-03 use  <div class="cover"> — classic layout
- Modules 04-10 use  <div class="hero">  — modern layout

Checks for the actual img src before injecting to prevent duplicates.
"""

import re
from pathlib import Path

ROOT = Path(r"c:\Users\sayan\Downloads\biochem Note X\modules")

IMG_SRC = "Caffeine%20%26%20Cadaver.jpg"

# Logo block for classic .cover layout
CLASSIC_LOGO = (
    '  <div class="brand-container">\n'
    '    <img src="../../Caffeine%20%26%20Cadaver.jpg"'
    ' alt="Caffeine &amp; Cadaver Logo" class="brand-logo">\n'
    '  </div>\n'
)

# Logo block for modern .hero layout
MODERN_LOGO = (
    '      <div class="brand-container" style="margin-bottom:20px;">\n'
    '        <img src="../../Caffeine%20%26%20Cadaver.jpg"'
    ' alt="Caffeine &amp; Cadaver Logo" class="brand-logo">\n'
    '      </div>\n'
)

CLASSIC_MODULES = ["module-02", "module-03"]
MODERN_MODULES  = ["module-04", "module-05", "module-06",
                   "module-07", "module-08", "module-09", "module-10"]

injected = []
skipped  = []
errors   = []


def inject(mod_list, pattern, logo_block):
    for mod in mod_list:
        mod_dir = ROOT / mod
        if not mod_dir.exists():
            errors.append(f"{mod}: directory not found")
            continue
        for f in sorted(mod_dir.glob("*.html")):
            text = f.read_text(encoding="utf-8")

            # Already has the img? Skip.
            if IMG_SRC in text:
                skipped.append(f.name)
                continue

            # Inject logo as first child of the target div
            new_text, n = re.subn(
                pattern,
                lambda m: m.group(0) + "\n" + logo_block,
                text,
                count=1
            )
            if n:
                f.write_text(new_text, encoding="utf-8")
                injected.append(f"{mod}/{f.name}")
            else:
                errors.append(f"{mod}/{f.name}: pattern not matched")


# Classic cover layout
inject(CLASSIC_MODULES, r'<div class="cover">', CLASSIC_LOGO)

# Modern hero layout — handle both indented and non-indented variants
inject(MODERN_MODULES, r'<div class="hero">', MODERN_LOGO)

print("=" * 55)
print("  Logo Injection Report")
print("=" * 55)
print(f"  Injected : {len(injected)}")
for f in injected:
    print(f"    + {f}")
print(f"  Skipped  : {len(skipped)} (already had logo)")
print(f"  Errors   : {len(errors)}")
for e in errors:
    print(f"    ! {e}")
print("=" * 55)
