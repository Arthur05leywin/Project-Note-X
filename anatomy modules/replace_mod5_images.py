import re
import os

mod5_path = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module05_abdomen.html"

with open(mod5_path, 'r', encoding='utf-8') as f:
    mod5 = f.read()

# 1. DIAGRAM 01
img1 = """<div class="wiki-img" style="margin: 1.5rem 0; text-align: center; background: var(--surface2); padding: 1rem; border-radius: 8px; border: 1px solid var(--border);">
      <div style="color:var(--accent);font-family:'JetBrains Mono',monospace;font-size:11px;margin-bottom:8px;text-align:left;">DIAGRAM 01 — Rectus Sheath Cross-sections</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray393.png" alt="Rectus Sheath Cross-sections" loading="lazy" style="max-width: 100%; height: auto; border-radius: 8px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:8px;">Transverse section of rectus sheath — Gray's Anatomy</div>
    </div>"""
mod5 = re.sub(r'<div class="diagram-placeholder">\s*<div class="dp-num">DIAGRAM 01 — Rectus Sheath Cross-sections</div>.*?</div>\s*</div>', img1, mod5, flags=re.DOTALL)

# 2. DIAGRAM 02
img2 = """<div class="wiki-img" style="margin: 1.5rem 0; text-align: center; background: var(--surface2); padding: 1rem; border-radius: 8px; border: 1px solid var(--border);">
      <div style="color:var(--accent);font-family:'JetBrains Mono',monospace;font-size:11px;margin-bottom:8px;text-align:left;">DIAGRAM 02 — Inguinal Canal Walls</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1146.png" alt="Inguinal Canal Walls" loading="lazy" style="max-width: 100%; height: auto; border-radius: 8px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:8px;">Inguinal canal and its relations — Gray's Anatomy</div>
    </div>"""
mod5 = re.sub(r'<div class="diagram-placeholder">\s*<div class="dp-num">DIAGRAM 02 — Inguinal Canal Walls</div>.*?</div>\s*</div>', img2, mod5, flags=re.DOTALL)

# 3. DIAGRAM 03
img3 = """<div class="wiki-img" style="margin: 1.5rem 0; text-align: center; background: var(--surface2); padding: 1rem; border-radius: 8px; border: 1px solid var(--border);">
      <div style="color:var(--accent);font-family:'JetBrains Mono',monospace;font-size:11px;margin-bottom:8px;text-align:left;">DIAGRAM 03 — Duodenum and its relations</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1058.png" alt="Duodenum and its relations" loading="lazy" style="max-width: 100%; height: auto; border-radius: 8px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:8px;">The duodenum and pancreas — Gray's Anatomy</div>
    </div>"""
mod5 = re.sub(r'<div class="diagram-placeholder">\s*<div class="dp-num">DIAGRAM 03 — Duodenum and its relations</div>.*?</div>\s*</div>', img3, mod5, flags=re.DOTALL)

# 4. DIAGRAM 04
img4 = """<div class="wiki-img" style="margin: 1.5rem 0; text-align: center; background: var(--surface2); padding: 1rem; border-radius: 8px; border: 1px solid var(--border);">
      <div style="color:var(--accent);font-family:'JetBrains Mono',monospace;font-size:11px;margin-bottom:8px;text-align:left;">DIAGRAM 04 — Couinaud's 8 Segments</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Liver_04_Couinaud_classification.svg" alt="Couinaud's 8 Segments" loading="lazy" style="max-width: 100%; height: auto; border-radius: 8px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:8px;">Couinaud's segments of the liver</div>
    </div>"""
mod5 = re.sub(r'<div class="diagram-placeholder">\s*<div class="dp-num">DIAGRAM 04 — Couinaud\'s 8 Segments</div>.*?</div>\s*</div>', img4, mod5, flags=re.DOTALL)

# 5. DIAGRAM 05
img5 = """<div class="wiki-img" style="margin: 1.5rem 0; text-align: center; background: var(--surface2); padding: 1rem; border-radius: 8px; border: 1px solid var(--border);">
      <div style="color:var(--accent);font-family:'JetBrains Mono',monospace;font-size:11px;margin-bottom:8px;text-align:left;">DIAGRAM 05 — Porto-Systemic Anastomoses</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray591.png" alt="Porto-Systemic Anastomoses" loading="lazy" style="max-width: 100%; height: auto; border-radius: 8px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:8px;">Portal vein and its tributaries — Gray's Anatomy</div>
    </div>"""
mod5 = re.sub(r'<div class="diagram-placeholder">\s*<div class="dp-num">DIAGRAM 05 — Porto-Systemic Anastomoses</div>.*?</div>\s*</div>', img5, mod5, flags=re.DOTALL)

# 6. DIAGRAM 06
img6 = """<div class="wiki-img" style="margin: 1.5rem 0; text-align: center; background: var(--surface2); padding: 1rem; border-radius: 8px; border: 1px solid var(--border);">
      <div style="color:var(--accent);font-family:'JetBrains Mono',monospace;font-size:11px;margin-bottom:8px;text-align:left;">DIAGRAM 06 — Anterior Relations of Both Kidneys</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1120.png" alt="Anterior Relations of Both Kidneys" loading="lazy" style="max-width: 100%; height: auto; border-radius: 8px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:8px;">Anterior relations of kidneys — Gray's Anatomy</div>
    </div>"""
mod5 = re.sub(r'<div class="diagram-placeholder">\s*<div class="dp-num">DIAGRAM 06 — Anterior Relations of Both Kidneys</div>.*?</div>\s*</div>', img6, mod5, flags=re.DOTALL)

with open(mod5_path, 'w', encoding='utf-8') as f:
    f.write(mod5)

print("Module 5 updated with Gray's Anatomy images.")
