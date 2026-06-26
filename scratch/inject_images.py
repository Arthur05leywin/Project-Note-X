import re

filepath = r'c:\Users\sayan\Downloads\biochem Note X\anatomy modules\module10_histology.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Cartilage Placeholder (Gray72.png)
cartilage_img = '''<img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray72.png" alt="Cartilage Histology" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
<div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Section of hyaline cartilage (Gray's Anatomy)</div>'''
content = re.sub(r'(<div class="diagram-num">DIAGRAM 4\.1.*?</div>)\s*<div class="diagram-instruction">.*?</div>', r'\1\n' + cartilage_img, content, flags=re.DOTALL)

# 2. Replace Bone Placeholder (Gray73.png)
bone_img = '''<img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray73.png" alt="Haversian System" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
<div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Transverse section of compact tissue of bone (Gray's Anatomy)</div>'''
content = re.sub(r'(<div class="diagram-num">DIAGRAM 5\.1.*?</div>)\s*<div class="diagram-instruction">.*?</div>', r'\1\n' + bone_img, content, flags=re.DOTALL)

# 3. Replace Muscle Placeholder (Gray406.png)
muscle_img = '''<img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray406.png" alt="Sarcomere Structure" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
<div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Striated muscle fibres (Gray's Anatomy)</div>'''
content = re.sub(r'(<div class="diagram-num">DIAGRAM 6\.1.*?</div>)\s*<div class="diagram-instruction">.*?</div>', r'\1\n' + muscle_img, content, flags=re.DOTALL)

# 4. Replace Skin Placeholder (Gray940.png)
skin_img = '''<img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray940.png" alt="Skin Cross-Section" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
<div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Section of skin (Gray's Anatomy)</div>'''
content = re.sub(r'(<div class="diagram-num">DIAGRAM 9\.1.*?</div>)\s*<div class="diagram-instruction">.*?</div>', r'\1\n' + skin_img, content, flags=re.DOTALL)

# Now inject extra images at the end of specific .card blocks if they don't exist yet
# Liver
if 'Gray1090.png' not in content:
    liver_inject = '''    </ul>
    <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
      <div class="diagram-num">LIVER HISTOLOGY</div>
      <img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1090.png" alt="Liver Lobule" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Section of a liver lobule (Gray's Anatomy)</div>
    </div>
  </div>'''
    content = re.sub(r'(<div class="card-title">Liver — Classic Hepatic Lobule.*?</ul>)\s*</div>', r'\1\n' + liver_inject.replace('    </ul>\n', ''), content, count=1, flags=re.DOTALL)

# Kidney
if 'Gray1129.png' not in content:
    kidney_inject = '''    </ul>
    <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
      <div class="diagram-num">KIDNEY CORPUSCLE</div>
      <img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1129.png" alt="Renal Corpuscle" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Malpighian corpuscle (renal corpuscle) (Gray's Anatomy)</div>
    </div>
  </div>'''
    content = re.sub(r'(<div class="card-title">Kidney — Nephron & Renal Corpuscle.*?</ul>)\s*</div>', r'\1\n' + kidney_inject.replace('    </ul>\n', ''), content, count=1, flags=re.DOTALL)

# Testis
if 'Gray1144.png' not in content:
    testis_inject = '''    </ul>
    <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
      <div class="diagram-num">TESTIS HISTOLOGY</div>
      <img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1144.png" alt="Testis Section" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Transverse section of a testicular lobule (Gray's Anatomy)</div>
    </div>
  </div>'''
    content = re.sub(r'(<div class="card-title">Testis — Seminiferous Tubules.*?</ul>)\s*</div>', r'\1\n' + testis_inject.replace('    </ul>\n', ''), content, count=1, flags=re.DOTALL)

# Ovary
if 'Gray1165.png' not in content:
    ovary_inject = '''    </ul>
    <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
      <div class="diagram-num">OVARY HISTOLOGY</div>
      <img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1165.png" alt="Ovary Section" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Section of the ovary (Gray's Anatomy)</div>
    </div>
  </div>'''
    content = re.sub(r'(<div class="card-title">Ovary — Follicular Development.*?</ul>)\s*</div>', r'\1\n' + ovary_inject.replace('    </ul>\n', ''), content, count=1, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Images injected successfully.")
