import re
import os

mod2_path = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module02_upper_limb.html"
mod3_path = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module03_lower_limb.html"

with open(mod2_path, 'r', encoding='utf-8') as f:
    mod2 = f.read()

with open(mod3_path, 'r', encoding='utf-8') as f:
    mod3 = f.read()

# Fix Module 2

# 1. Replace DIAGRAM 01 Placeholder
scapula_img = """<div class="wiki-img">
          <div style="color:var(--accent);font-family:'JetBrains Mono',monospace;font-size:11px;margin-bottom:8px;">DIAGRAM 01 — Scapula Posterior Surface</div>
          <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray203.png" alt="Scapula Posterior Surface" loading="lazy" style="border-radius: 8px;">
          <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:8px;">Posterior surface of the scapula — Gray's Anatomy</div>
        </div>"""
mod2 = re.sub(r'<div class="diagram-placeholder">\s*<div class="diagram-num">DIAGRAM 01</div>.*?</div>\s*</div>', scapula_img + '\n      </div>', mod2, flags=re.DOTALL)

# 2. Replace DIAGRAM 02 Placeholder
veins_img = """<div class="wiki-img">
      <div style="color:var(--accent);font-family:'JetBrains Mono',monospace;font-size:11px;margin-bottom:8px;">DIAGRAM 02 — Superficial Veins</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray573.png" alt="Superficial Veins of Upper Limb" loading="lazy" style="border-radius: 8px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:8px;">Superficial veins of the upper limb — Gray's Anatomy</div>
    </div>"""
mod2 = re.sub(r'<div class="diagram-placeholder">\s*<div class="diagram-num">DIAGRAM 02</div>.*?</div>', veins_img, mod2, flags=re.DOTALL)

# 3. Replace DIAGRAM 03 Placeholder
dermatome_img = """<div class="wiki-img">
      <div style="color:var(--accent);font-family:'JetBrains Mono',monospace;font-size:11px;margin-bottom:8px;">DIAGRAM 03 — Dermatomes</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray812and814.svg" alt="Dermatomes of Upper Limb" loading="lazy" style="border-radius: 8px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:8px;">Dermatome map of the upper limb — Gray's Anatomy</div>
    </div>"""
mod2 = re.sub(r'<div class="diagram-placeholder">\s*<div class="diagram-num">DIAGRAM 03</div>.*?</div>', dermatome_img, mod2, flags=re.DOTALL)

# 4. Fix stray images
mod2 = mod2.replace('<img src="https://upload.wikimedia.org/wikipedia/commons/3/3b/Gray326.png" alt="Shoulder Joint Anatomy" style="max-width: 100%; border-radius: 8px;">',
'<img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray326.png" alt="Shoulder Joint Anatomy" style="max-width: 100%; border-radius: 8px;">')

mod2 = mod2.replace('<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Brachial_plexus_color.svg/600px-Brachial_plexus_color.svg.png"',
'<img src="https://commons.wikimedia.org/wiki/Special:FilePath/Brachial_plexus_color.svg" style="max-width: 100%; border-radius: 8px;"')

mod2 = mod2.replace('<img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Gray523.png" alt="Axillary Artery and Space" style="max-width: 100%; border-radius: 8px;">',
'<img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray523.png" alt="Axillary Artery and Space" style="max-width: 100%; border-radius: 8px;">')

mod2 = mod2.replace('<img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Gray574.png" alt="Cubital Fossa Diagram" style="max-width: 100%; border-radius: 8px;">',
'<img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray574.png" alt="Cubital Fossa Diagram" style="max-width: 100%; border-radius: 8px;">')


# Fix Module 3

mod3 = mod3.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Femur_-_anterior_view.png/300px-Femur_-_anterior_view.png',
'https://commons.wikimedia.org/wiki/Special:FilePath/Femur_-_anterior_view.png')

mod3 = mod3.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Hip_joint_anatomy.png/300px-Hip_joint_anatomy.png',
'https://commons.wikimedia.org/wiki/Special:FilePath/Gray343.png')

mod3 = mod3.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Knee_diagram.svg/300px-Knee_diagram.svg.png',
'https://commons.wikimedia.org/wiki/Special:FilePath/Gray348.png')

mod3 = mod3.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Gray544.png/300px-Gray544.png',
'https://commons.wikimedia.org/wiki/Special:FilePath/Gray544.png')

mod3 = mod3.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Gray433.png/300px-Gray433.png',
'https://commons.wikimedia.org/wiki/Special:FilePath/Gray433.png')

mod3 = mod3.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Dermatoms.svg/300px-Dermatoms.svg.png',
'https://commons.wikimedia.org/wiki/Special:FilePath/Dermatoms.svg')

with open(mod2_path, 'w', encoding='utf-8') as f:
    f.write(mod2)

with open(mod3_path, 'w', encoding='utf-8') as f:
    f.write(mod3)

print("Images replaced in both modules.")
