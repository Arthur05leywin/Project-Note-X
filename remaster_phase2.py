"""
remaster_phase2.py
==================
Phase 2 Automation Script — Biochemistry Notes Remastering
Handles ALL files except Module 01 (already done).

Tasks:
  1. Global branding scrub: WBUHS → MBBS, remove KIMS/NMO references
  2. Logo injection into cover pages (.cover layout and .hero layout)
  3. Title tag cleanup
  4. Footer cleanup
  5. Storefront pages cleanup

Run from project root:
  python remaster_phase2.py
"""

import re
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# 🎨 Configuration ────────────────────────────────────────────────────────────

ROOT = Path(__file__).parent
MODULES_DIR = ROOT / "modules"

# Logo HTML snippet for CLASSIC layout (modules 2-3 which use .cover)
CLASSIC_LOGO_HTML = '''  <div class="brand-container">
    <img src="../../Caffeine%20%26%20Cadaver.jpg" alt="Caffeine &amp; Cadaver Logo" class="brand-logo">
  </div>
'''

# Logo HTML snippet for MODERN layout (modules 4-10 which use .hero)
MODERN_LOGO_HTML = '''      <div class="brand-container" style="margin-bottom:20px;">
        <img src="../../Caffeine%20%26%20Cadaver.jpg" alt="Caffeine &amp; Cadaver Logo" class="brand-logo">
      </div>
'''

# Storefront logo HTML (for index.html, etc. — one level up from modules)
STOREFRONT_LOGO_HTML = '''    <div class="brand-container" style="margin-bottom:24px;">
      <img src="Caffeine%20%26%20Cadaver.jpg" alt="Caffeine &amp; Cadaver Logo" class="brand-logo" style="max-width:160px;">
    </div>
'''

# Modules using classic .cover layout
CLASSIC_MODULES = ["module-02", "module-03"]

# Modules using modern .hero layout
MODERN_MODULES = ["module-04", "module-05", "module-06", "module-07", "module-08", "module-09", "module-10"]

# Storefront files to clean
STOREFRONT_FILES = [
    ROOT / "index.html",
    ROOT / "sample.html",
    ROOT / "packs.html",
    ROOT / "faq.html",
    ROOT / "contact.html",
    ROOT / "delivery.html",
    ROOT / "refund.html",
    ROOT / "terms.html",
]

# CSS brand classes to inject if missing (for files that have inline <style>)
BRAND_CSS = """
/* Premium Brand Identity */
.brand-container {
  display: block;
  margin-bottom: 28px;
  animation: fadeIn 0.8s ease-out;
}
.brand-logo {
  max-width: 200px;
  height: auto;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.5);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.brand-logo:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(232, 200, 74, 0.15);
}
"""

# ─── Counter ──────────────────────────────────────────────────────────────────

stats = {
    "files_processed": 0,
    "wbuhs_replaced": 0,
    "kims_removed": 0,
    "nmo_removed": 0,
    "logos_injected": 0,
    "titles_fixed": 0,
    "css_injected": 0,
    "errors": [],
}


# ─── Core Substitution Engine ─────────────────────────────────────────────────

def apply_global_scrub(content: str, filename: str) -> tuple[str, dict]:
    """Apply all branding scrubs and return updated content + change counts."""
    changes = {"wbuhs": 0, "kims": 0, "nmo": 0}

    # 1. WBUHS → MBBS (various cases and contexts)
    # Keep "WBUHS BIOCHEMISTRY · PAPER" → "MBBS BIOCHEMISTRY · PAPER"
    replacements_wbuhs = [
        # Titles and meta descriptions
        ("WBUHS Biochemistry revision system", "MBBS Biochemistry revision system"),
        ("WBUHS Biochemistry", "MBBS Biochemistry"),
        ("WBUHS biochemistry", "MBBS Biochemistry"),
        ("WBUHS BIOCHEMISTRY", "MBBS BIOCHEMISTRY"),
        # Cover tag
        ("WBUHS Biochemistry · Module", "MBBS Biochemistry · Module"),
        # PYQ box label
        ("Appeared in WBUHS", "MBBS PYQ Appearances"),
        # Hero sub text
        ("WBUHS BIOCHEMISTRY · PAPER", "MBBS BIOCHEMISTRY · PAPER"),
        # Intelligence matrix
        ("WBUHS 1st Year MBBS Intelligence Matrix", "MBBS 1st Year Biochemistry Intelligence Matrix"),
        # Common paragraph mentions
        ("Built from WBUHS PYQs", "Built from MBBS PYQs"),
        ("Built from real WBUHS exam patterns", "Built from real MBBS exam patterns"),
        ("for WBUHS students", "for MBBS students"),
        ("for WBUHS Biochemistry", "for MBBS Biochemistry"),
        ("WBUHS Biochemistry system", "MBBS Biochemistry system"),
        ("WBUHS papers mapped", "MBBS papers mapped"),
        ("WBUHS Revision System", "MBBS Revision System"),
        ("Project X - WBUHS Revision System", "Project X - MBBS Revision System"),
        ("WBUHS syllabus", "MBBS syllabus"),
        ("WBUHS exams", "MBBS exams"),
        ("WBUHS exam patterns", "MBBS exam patterns"),
        ("WBUHS exam grind", "MBBS exam grind"),
        ("WBUHS Ranker", "MBBS Ranker"),
        ("WBUHS appearance history", "MBBS appearance history"),
        ("WBUHS may still", "MBBS board exams may still"),
        ("still accepted in WBUHS", "still accepted in MBBS boards"),
        ("WBUHS often accepts", "MBBS boards often accept"),
        # Iron lab test label
        ("Iron Lab Tests - WBUHS Exam Must-Know", "Iron Lab Tests - MBBS Exam Must-Know"),
        # Catch-all remaining WBUHS
        ("WBUHS", "MBBS"),
        ("wbuhs", "mbbs"),
    ]

    for old, new in replacements_wbuhs:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            changes["wbuhs"] += count

    # 2. Remove / replace KIMS Krishnanagar references
    kims_patterns = [
        # Full footer branding lines
        (r"KIMS Krishnanagar Biochem Notes\s*[·•]\s*WBUHS\s*[·•]\s*NMO Bengal PYQs 2010[–-]2025",
         "Caffeine &amp; Cadaver · MBBS Biochemistry Notes · 2010–2025"),
        (r"KIMS Krishnanagar Biochem Notes\s*[·•]\s*MBBS\s*[·•]\s*NMO Bengal PYQs 2010[–-]2025",
         "Caffeine &amp; Cadaver · MBBS Biochemistry Notes · 2010–2025"),
        (r"KIMS Krishnanagar Biochem Notes\s*[·•]\s*WBUHS\s*[·•]\s*NMO Bengal PYQs",
         "Caffeine &amp; Cadaver · MBBS Biochemistry Notes"),
        # Hero sub with KIMS
        (r"WBUHS BIOCHEMISTRY\s*[·•]\s*PAPER\s*\d+\s*[·•]\s*KIMS KRISHNANAGAR",
         "MBBS BIOCHEMISTRY · PAPER 1"),
        (r"MBBS BIOCHEMISTRY\s*[·•]\s*PAPER\s*\d+\s*[·•]\s*KIMS KRISHNANAGAR",
         "MBBS BIOCHEMISTRY · PAPER 1"),
        (r"WBUHS BIOCHEMISTRY\s*[·•]\s*PAPER\s*2\s*[·•]\s*KIMS KRISHNANAGAR",
         "MBBS BIOCHEMISTRY · PAPER 2"),
        (r"MBBS BIOCHEMISTRY\s*[·•]\s*PAPER\s*2\s*[·•]\s*KIMS KRISHNANAGAR",
         "MBBS BIOCHEMISTRY · PAPER 2"),
        # Title tag: "| KIMS Biochem" suffix
        (r"\|\s*KIMS Biochem(?:em)?(?:\<\/title\>)?", " | MBBS Biochemistry Notes</title>"),
        # "KIMS Krishnanagar WBUHS Biochemistry Note Series"
        (r"KIMS Krishnanagar WBUHS Biochemistry Note Series",
         "Caffeine &amp; Cadaver MBBS Biochemistry Note Series"),
        (r"KIMS Krishnanagar MBBS Biochemistry Note Series",
         "Caffeine &amp; Cadaver MBBS Biochemistry Note Series"),
        # "KIMS Krishnanagar" standalone
        (r"KIMS\s*Krishnanagar", "Caffeine &amp; Cadaver"),
        # .kims-tag CSS class (rename the class reference to .brand-tag)
        (r"\.kims-tag\s*\{", ".brand-tag {"),
        (r'class="kims-tag"', 'class="brand-tag"'),
        # Just "KIMS" remaining
        (r"\bKIMS\b", "C&amp;C"),
    ]

    for pattern, replacement in kims_patterns:
        new_content, n = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
        if n > 0:
            content = new_content
            changes["kims"] += n

    # 3. Remove NMO Bengal references
    nmo_patterns = [
        (r"NMO Bengal PDF\s*[·•]\s*Mobile-optimised", "MBBS Biochemistry Notes · Mobile-optimised"),
        (r"NMO Bengal PYQs?\s*2010[–-]2025", "MBBS PYQs 2010–2025"),
        (r"NMO Bengal", "MBBS"),
    ]

    for pattern, replacement in nmo_patterns:
        new_content, n = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
        if n > 0:
            content = new_content
            changes["nmo"] += n

    return content, changes


def fix_title_tag(content: str) -> tuple[str, bool]:
    """Fix title tags to use MBBS Biochemistry Notes branding."""
    changed = False

    # Pattern: <title>Module XX - Topic Name | KIMS Biochem</title>
    # → <title>Module XX - Topic Name | MBBS Biochemistry Notes</title>
    new_content = re.sub(
        r'<title>(Module\s+\d+[^<]*?)\s*\|\s*(?:KIMS\s*Biochem[^<]*?|WBUHS[^<]*?)</title>',
        r'<title>\1 | MBBS Biochemistry Notes</title>',
        content,
        flags=re.IGNORECASE
    )
    if new_content != content:
        changed = True
        content = new_content

    # Fix storefront titles
    new_content = re.sub(
        r'<title>Project X\s*\|\s*WBUHS Biochemistry</title>',
        '<title>Project X | MBBS Biochemistry</title>',
        content, flags=re.IGNORECASE
    )
    if new_content != content:
        changed = True
        content = new_content

    # Fix meta description
    new_content = re.sub(
        r'content="Project X - WBUHS Biochemistry revision system',
        'content="Project X - MBBS Biochemistry revision system',
        content, flags=re.IGNORECASE
    )
    if new_content != content:
        changed = True
        content = new_content

    return content, changed


def inject_brand_css_if_missing(content: str) -> tuple[str, bool]:
    """Inject brand CSS classes into the <style> block if not already present."""
    if ".brand-container" in content:
        return content, False  # Already has it

    # Find the end of the first <style> block and inject before </style>
    # We look for the first occurrence of the CSS comment or @import
    style_close = content.find("</style>")
    if style_close == -1:
        return content, False

    # Find the last </style> in the head area (first big style block)
    # Only inject in the first </style> found
    content = content[:style_close] + BRAND_CSS + content[style_close:]
    return content, True


def inject_logo_classic(content: str, filename: str) -> tuple[str, bool]:
    """
    Inject logo into classic .cover layout.
    Logo goes as first child inside <div class="cover">.
    Skips if already present.
    """
    if 'brand-container' in content or 'Caffeine' in content:
        return content, False

    # Match the opening cover div and insert logo right after it
    pattern = r'(<div class="cover">)\s*'
    replacement = r'\1\n' + CLASSIC_LOGO_HTML
    new_content, n = re.subn(pattern, replacement, content, count=1)
    if n > 0:
        return new_content, True
    return content, False


def inject_logo_modern(content: str, filename: str) -> tuple[str, bool]:
    """
    Inject logo into modern .hero layout.
    Logo goes as first child inside <div class="hero">.
    Skips if already present.
    """
    if 'brand-container' in content or 'Caffeine' in content:
        return content, False

    # Match the hero div (handles indented variants)
    pattern = r'(<div class="hero">)\s*'
    replacement = r'\1\n' + MODERN_LOGO_HTML
    new_content, n = re.subn(pattern, replacement, content, count=1)
    if n > 0:
        return new_content, True

    # Also try with leading whitespace (indented)
    pattern2 = r'([ \t]*<div class="hero">)'
    def hero_replacer(m):
        indent = '    '
        logo_indented = MODERN_LOGO_HTML
        return m.group(1) + '\n' + logo_indented

    new_content, n = re.subn(pattern2, hero_replacer, content, count=1)
    if n > 0:
        return new_content, True

    return content, False


def process_module_file(filepath: Path, layout: str) -> bool:
    """Process a single module HTML file. Returns True on success."""
    try:
        content = filepath.read_text(encoding="utf-8")
        original = content

        # Step 1: Global branding scrub
        content, changes = apply_global_scrub(content, filepath.name)
        stats["wbuhs_replaced"] += changes["wbuhs"]
        stats["kims_removed"] += changes["kims"]
        stats["nmo_removed"] += changes["nmo"]

        # Step 2: Fix title tag
        content, title_fixed = fix_title_tag(content)
        if title_fixed:
            stats["titles_fixed"] += 1

        # Step 3: Inject brand CSS if missing
        content, css_added = inject_brand_css_if_missing(content)
        if css_added:
            stats["css_injected"] += 1

        # Step 4: Inject logo
        if layout == "classic":
            content, logo_added = inject_logo_classic(content, filepath.name)
        else:  # modern
            content, logo_added = inject_logo_modern(content, filepath.name)

        if logo_added:
            stats["logos_injected"] += 1

        # Step 5: Write back only if changed
        if content != original:
            filepath.write_text(content, encoding="utf-8")
            stats["files_processed"] += 1
            print(f"  ✅ {filepath.name}: WBUHS×{changes['wbuhs']} KIMS×{changes['kims']} NMO×{changes['nmo']}"
                  f"{' [logo]' if logo_added else ''}{' [css]' if css_added else ''}{' [title]' if title_fixed else ''}")
        else:
            print(f"  ⚪ {filepath.name}: No changes needed")

        return True

    except Exception as e:
        msg = f"ERROR processing {filepath}: {e}"
        print(f"  ❌ {msg}")
        stats["errors"].append(msg)
        return False


def process_storefront_file(filepath: Path) -> bool:
    """Process a storefront HTML file (root level, no logo injection needed in most)."""
    if not filepath.exists():
        print(f"  ⚠️  {filepath.name}: File not found, skipping")
        return True

    try:
        content = filepath.read_text(encoding="utf-8")
        original = content

        # Global branding scrub
        content, changes = apply_global_scrub(content, filepath.name)
        stats["wbuhs_replaced"] += changes["wbuhs"]
        stats["kims_removed"] += changes["kims"]
        stats["nmo_removed"] += changes["nmo"]

        # Fix title/meta
        content, title_fixed = fix_title_tag(content)
        if title_fixed:
            stats["titles_fixed"] += 1

        # Write back only if changed
        if content != original:
            filepath.write_text(content, encoding="utf-8")
            stats["files_processed"] += 1
            print(f"  ✅ {filepath.name}: WBUHS×{changes['wbuhs']} KIMS×{changes['kims']} NMO×{changes['nmo']}"
                  f"{' [title]' if title_fixed else ''}")
        else:
            print(f"  ⚪ {filepath.name}: No changes needed")

        return True

    except Exception as e:
        msg = f"ERROR processing {filepath}: {e}"
        print(f"  ❌ {msg}")
        stats["errors"].append(msg)
        return False


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("  PHASE 2: Biochemistry Notes Remaster Automation Script")
    print("  Caffeine & Cadaver — MBBS Biochemistry Series")
    print("=" * 65)
    print()

    # ── Modules 02 & 03: Classic .cover layout ──
    print("📘 Processing Classic Layout Modules (02-03)...")
    for mod_name in CLASSIC_MODULES:
        mod_dir = MODULES_DIR / mod_name
        if not mod_dir.exists():
            print(f"  ⚠️  {mod_name}: Directory not found")
            continue
        html_files = list(mod_dir.glob("*.html"))
        print(f"\n  [{mod_name}] — {len(html_files)} files:")
        for f in sorted(html_files):
            process_module_file(f, layout="classic")

    print()

    # ── Modules 04-10: Modern .hero layout ──
    print("📗 Processing Modern Layout Modules (04-10)...")
    for mod_name in MODERN_MODULES:
        mod_dir = MODULES_DIR / mod_name
        if not mod_dir.exists():
            print(f"  ⚠️  {mod_name}: Directory not found")
            continue
        html_files = list(mod_dir.glob("*.html"))
        print(f"\n  [{mod_name}] — {len(html_files)} files:")
        for f in sorted(html_files):
            process_module_file(f, layout="modern")

    print()

    # ── Storefront files ──
    print("🏪 Processing Storefront Files...")
    for f in STOREFRONT_FILES:
        process_storefront_file(f)

    print()
    print("=" * 65)
    print("  PHASE 2 COMPLETE — Summary Report")
    print("=" * 65)
    print(f"  📄 Files modified      : {stats['files_processed']}")
    print(f"  🔄 WBUHS → MBBS       : {stats['wbuhs_replaced']} replacements")
    print(f"  🗑️  KIMS refs removed  : {stats['kims_removed']} occurrences")
    print(f"  🗑️  NMO refs removed   : {stats['nmo_removed']} occurrences")
    print(f"  🖼️  Logos injected     : {stats['logos_injected']} files")
    print(f"  🎨 CSS injected        : {stats['css_injected']} files")
    print(f"  📝 Title tags fixed    : {stats['titles_fixed']} files")
    if stats["errors"]:
        print(f"\n  ❌ ERRORS ({len(stats['errors'])}):")
        for e in stats["errors"]:
            print(f"     {e}")
    else:
        print(f"\n  ✅ Zero errors. All files clean.")
    print("=" * 65)


if __name__ == "__main__":
    main()
