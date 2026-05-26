"""
brand_bar_inject.py
===================
Replaces the plain logo img injection with a premium top-bar brand strip
on every module cover page (both classic .cover and modern .hero layouts).

Design: A full-width bar pinned to the absolute top of the cover/hero,
with the Caffeine & Cadaver logo on the left and series text on the right.
Works for print too — collapses gracefully in @media print.
"""

import re
from pathlib import Path

ROOT = Path(r"c:\Users\sayan\Downloads\biochem Note X\modules")
IMG_SRC = "Caffeine%20%26%20Cadaver.jpg"

# ─── Brand Bar HTML ────────────────────────────────────────────────────────────
# This replaces whatever brand-container was previously injected.
# It uses position:absolute so it doesn't push any cover content down.

BRAND_BAR = '''\
  <!-- ═══ BRAND BAR ═══ -->
  <div class="brand-bar">
    <img src="../../Caffeine%20%26%20Cadaver.jpg" alt="Caffeine &amp; Cadaver" class="brand-bar-logo">
    <div class="brand-bar-text">
      <span class="brand-bar-name">Caffeine &amp; Cadaver</span>
      <span class="brand-bar-series">MBBS Biochemistry Notes Series</span>
    </div>
  </div>
'''

BRAND_BAR_MODERN = '''\
      <!-- ═══ BRAND BAR ═══ -->
      <div class="brand-bar">
        <img src="../../Caffeine%20%26%20Cadaver.jpg" alt="Caffeine &amp; Cadaver" class="brand-bar-logo">
        <div class="brand-bar-text">
          <span class="brand-bar-name">Caffeine &amp; Cadaver</span>
          <span class="brand-bar-series">MBBS Biochemistry Notes Series</span>
        </div>
      </div>
'''

# ─── CSS to inject into <style> if not already present ─────────────────────────
BRAND_BAR_CSS = """
/* ─── Premium Brand Bar ─────────────────────────────── */
.brand-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 60px;
  background: rgba(0, 0, 0, 0.35);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
  z-index: 10;
}

.brand-bar-logo {
  height: 36px;
  width: auto;
  border-radius: 4px;
  object-fit: contain;
  flex-shrink: 0;
}

.brand-bar-text {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.brand-bar-name {
  font-family: "IBM Plex Mono", "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 600;
  color: var(--accent, #e8c84a);
  letter-spacing: 2px;
  text-transform: uppercase;
}

.brand-bar-series {
  font-family: "IBM Plex Mono", "JetBrains Mono", monospace;
  font-size: 9px;
  color: rgba(255, 255, 255, 0.4);
  letter-spacing: 1.5px;
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
    padding: 8px 40px !important;
    backdrop-filter: none !important;
  }
  .brand-bar-logo {
    height: 24px !important;
    filter: grayscale(100%) !important;
  }
  .brand-bar-name {
    color: #000000 !important;
    font-size: 9px !important;
  }
  .brand-bar-series {
    color: #495057 !important;
    font-size: 8px !important;
  }
}
/* ──────────────────────────────────────────────────── */
"""

CLASSIC_MODULES = ["module-01", "module-02", "module-03"]
MODERN_MODULES  = ["module-04", "module-05", "module-06",
                   "module-07", "module-08", "module-09", "module-10"]

stats = {"injected": [], "css_added": [], "errors": []}


def upgrade_css(content: str, filename: str) -> tuple[str, bool]:
    """Inject brand bar CSS into the first </style> tag if not already present."""
    if ".brand-bar {" in content:
        return content, False
    close = content.find("</style>")
    if close == -1:
        return content, False
    content = content[:close] + BRAND_BAR_CSS + content[close:]
    return content, True


def remove_old_brand_container(content: str) -> str:
    """Remove the previously injected plain brand-container div."""
    # Matches the simple brand-container block with img inside
    content = re.sub(
        r'\s*<div class="brand-container"[^>]*>\s*<img[^>]*Caffeine[^>]*>\s*</div>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )
    # Also handle the comment + brand-container pattern
    content = re.sub(
        r'\s*<!--\s*Brand Identity\s*-->\s*<div class="brand-container"[^>]*>\s*<img[^>]*>\s*</div>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )
    # Also handle the ═══ BRAND BAR ═══ comment if already injected (idempotent)
    content = re.sub(
        r'\s*<!--\s*═══ BRAND BAR ═══\s*-->\s*<div class="brand-bar">.*?</div>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )
    return content


def inject_classic(content: str, fname: str) -> tuple[str, bool]:
    """Inject brand bar as absolute-positioned first child of .cover div."""
    content = remove_old_brand_container(content)
    # Match <div class="cover"> allowing optional leading whitespace
    pattern = r'(<div class="cover">)'
    new, n = re.subn(pattern, r'\1\n' + BRAND_BAR, content, count=1)
    if n:
        return new, True
    # Try indented variant
    pattern2 = r'([ \t]*<div class="cover">)'
    def repl(m):
        return m.group(0) + '\n' + BRAND_BAR
    new, n = re.subn(pattern2, repl, content, count=1)
    if n:
        return new, True
    stats["errors"].append(f"{fname}: cover div not found")
    return content, False


def inject_modern(content: str, fname: str) -> tuple[str, bool]:
    """Inject brand bar as absolute-positioned first child of .hero div."""
    content = remove_old_brand_container(content)
    pattern = r'(<div class="hero">)'
    new, n = re.subn(pattern, r'\1\n' + BRAND_BAR_MODERN, content, count=1)
    if n:
        return new, True
    pattern2 = r'([ \t]*<div class="hero">)'
    def repl(m):
        return m.group(0) + '\n' + BRAND_BAR_MODERN
    new, n = re.subn(pattern2, repl, content, count=1)
    if n:
        return new, True
    stats["errors"].append(f"{fname}: hero div not found")
    return content, False


def process(mod_list, layout):
    for mod in mod_list:
        mod_dir = ROOT / mod
        if not mod_dir.exists():
            stats["errors"].append(f"{mod}: directory not found")
            continue
        for f in sorted(mod_dir.glob("*.html")):
            try:
                content = f.read_text(encoding="utf-8")
                original = content

                # Step 1: inject / upgrade CSS
                content, css_added = upgrade_css(content, f.name)
                if css_added:
                    stats["css_added"].append(f.name)

                # Step 2: inject brand bar into cover/hero
                if layout == "classic":
                    content, ok = inject_classic(content, f.name)
                else:
                    content, ok = inject_modern(content, f.name)

                if ok:
                    stats["injected"].append(f"{mod}/{f.name}")

                if content != original:
                    f.write_text(content, encoding="utf-8")

            except Exception as e:
                stats["errors"].append(f"{mod}/{f.name}: {e}")


process(CLASSIC_MODULES, "classic")
process(MODERN_MODULES,  "modern")

print("=" * 60)
print("  Brand Bar Injection — Report")
print("=" * 60)
print(f"  Injected in : {len(stats['injected'])} files")
for f in stats["injected"]:
    print(f"    + {f}")
print(f"  CSS added   : {len(stats['css_added'])} files")
if stats["errors"]:
    print(f"  Errors      : {len(stats['errors'])}")
    for e in stats["errors"]:
        print(f"    ! {e}")
else:
    print(f"  Errors      : 0")
print("=" * 60)
