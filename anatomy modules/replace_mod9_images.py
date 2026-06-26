import re

filepath = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\module09_embryology.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Diagram 09.1
rep1 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diag-num">DIAGRAM 09.1</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray38.png" alt="Development Timeline" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Fetus in utero (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diag-num">DIAGRAM 09\.1</div>.*?</div>\s*</div>', rep1, content, flags=re.DOTALL)

# Replace Diagram 09.2
rep2 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diag-num">DIAGRAM 09.2</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray11.png" alt="Blastocyst Structure" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Section through embryonic disk (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diag-num">DIAGRAM 09\.2</div>.*?</div>\s*</div>', rep2, content, flags=re.DOTALL)

# Replace Diagram 09.3
rep3 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diag-num">DIAGRAM 09.3</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray39.png" alt="Placenta Circulation" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Scheme of placental circulation (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diag-num">DIAGRAM 09\.3</div>.*?</div>\s*</div>', rep3, content, flags=re.DOTALL)

# Replace Diagram 09.4
rep4 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diag-num">DIAGRAM 09.4</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray502.png" alt="Fetal Circulation Diagram" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Circulation of a fetus (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diag-num">DIAGRAM 09\.4</div>.*?</div>\s*</div>', rep4, content, flags=re.DOTALL)

# Replace Diagram 09.5
rep5 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diag-num">DIAGRAM 09.5</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray41.png" alt="Pharyngeal Arches" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Head end of human embryo, showing pharyngeal arches (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diag-num">DIAGRAM 09\.5</div>.*?</div>\s*</div>', rep5, content, flags=re.DOTALL)

# Insert Extra Images
content = content.replace(
    '<div class="card-title">Spermatogenesis vs Oogenesis — Comparison</div>',
    '<div class="card-title">Spermatogenesis vs Oogenesis — Comparison</div>\n    <div style="text-align:center; margin:1rem 0;">\n      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray2.png" alt="Human Spermatozoon" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;">\n      <div class="wiki-caption" style="font-size:11px;color:var(--text2);margin-top:6px;">Human spermatozoon (Gray\'s Anatomy)</div>\n    </div>'
)

content = content.replace(
    '<div class="card-title">Neurulation — Neural Tube Formation <span class="badge badge-fav">⭐ PYQ 2012, 2019, 2024</span></div>',
    '<div class="card-title">Neurulation — Neural Tube Formation <span class="badge badge-fav">⭐ PYQ 2012, 2019, 2024</span></div>\n    <div style="text-align:center; margin:1rem 0;">\n      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray15.png" alt="Human Embryo" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;">\n      <div class="wiki-caption" style="font-size:11px;color:var(--text2);margin-top:6px;">Human embryo 2mm long (Gray\'s Anatomy)</div>\n    </div>'
)


# Fix CSS
content = content.replace(
    '.two-col{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;margin:1rem 0;}',
    '.two-col{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(280px, 100%),1fr));gap:1rem;margin:1rem 0;}'
)
content = content.replace(
    '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:10px;margin-top:8px">',
    '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(min(270px, 100%),1fr));gap:10px;margin-top:8px">'
)

content = content.replace(
    ".keypoint{background:rgba(232,96,154,.07);border:1px solid rgba(232,96,154,.22);border-radius:6px;padding:10px 14px;margin:8px 0;font-size:13px;display:flex;gap:8px;align-items:flex-start;}\n.keypoint::before{content:'⚡';flex-shrink:0;}",
    ".keypoint{word-break: break-word; overflow-wrap: break-word; background:rgba(232,96,154,.07);border:1px solid rgba(232,96,154,.22);border-radius:6px;padding:10px 14px 10px 34px;margin:8px 0;font-size:13px;display:block;position:relative;}\n.keypoint::before{content:'⚡';position:absolute;left:12px;top:10px;}"
)

content = content.replace(
    ".warn-box{background:rgba(251,146,60,.07);border:1px solid rgba(251,146,60,.25);border-left:4px solid var(--orange);border-radius:6px;padding:10px 14px;margin:8px 0;font-size:13px;display:flex;gap:8px;}\n.warn-box::before{content:'⚠️';flex-shrink:0;}",
    ".warn-box{word-break: break-word; overflow-wrap: break-word; background:rgba(251,146,60,.07);border:1px solid rgba(251,146,60,.25);border-left:4px solid var(--orange);border-radius:6px;padding:10px 14px 10px 34px;margin:8px 0;font-size:13px;display:block;position:relative;}\n.warn-box::before{content:'⚠️';position:absolute;left:10px;top:10px;}"
)

# Update Footer
content = content.replace("Diagram placeholders ready for tablet art", "Includes Gray's Anatomy diagrams")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Module 9 processed successfully.")
