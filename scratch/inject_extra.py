import re
filepath = r'c:\Users\sayan\Downloads\biochem Note X\anatomy modules\module10_histology.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Liver
liver_inject = '''
  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diagram-num">LIVER LOBULE</div>
    <img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1090.png" alt="Liver Lobule" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Section of a liver lobule (Gray's Anatomy)</div>
  </div>'''
content = re.sub(r'(<div class="card-title">Liver Histology .*?</div>\s*<div class="table-wrap">.*?</table>\s*</div>)', r'\1' + liver_inject, content, count=1, flags=re.DOTALL)

# Kidney
kidney_inject = '''
  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diagram-num">KIDNEY CORPUSCLE</div>
    <img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1129.png" alt="Renal Corpuscle" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Malpighian corpuscle (renal corpuscle) (Gray's Anatomy)</div>
  </div>'''
content = re.sub(r'(<div class="card-title">Kidney Histology .*?</div>\s*<div class="table-wrap">.*?</table>\s*</div>)', r'\1' + kidney_inject, content, count=1, flags=re.DOTALL)

# Testis
testis_inject = '''
  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diagram-num">TESTIS SECTION</div>
    <img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1144.png" alt="Testis Section" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Transverse section of a testicular lobule (Gray's Anatomy)</div>
  </div>'''
content = re.sub(r'(<div class="card-title">Testis \&amp; Ovary .*?</div>\s*<div class="table-wrap">.*?</table>\s*</div>)', r'\1' + testis_inject, content, count=1, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added extra organ images.")
