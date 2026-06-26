import re

filepath = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module06_pelvis_perineum.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Diagram 1
rep1 = """    <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
      <div class="dp-num">DIAGRAM 01 — Levator Ani from Below</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Levator_ani.png" alt="Levator Ani from Below" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Levator Ani from below (Gray's Anatomy)</div>
    </div>"""

content = re.sub(r'<div class="diagram-placeholder">\s*<div class="dp-num">DIAGRAM 01 — Levator Ani from Below</div>\s*<div class="dp-desc">.*?</div>\s*</div>', rep1, content, flags=re.DOTALL)

# Diagram 2
rep2 = """    <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
      <div class="dp-num">DIAGRAM 02 — Perineum Diamond Shape</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray406.png" alt="Perineum Diamond Shape" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Perineum Diamond Shape (Gray's Anatomy)</div>
    </div>"""

content = re.sub(r'<div class="diagram-placeholder">\s*<div class="dp-num">DIAGRAM 02 — Perineum Diamond Shape</div>\s*<div class="dp-desc">.*?</div>\s*</div>', rep2, content, flags=re.DOTALL)

# Footer
content = content.replace("Diagram placeholders ready for tablet art", "Includes Gray's Anatomy diagrams")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Placeholders replaced with Gray's Anatomy images in module 06.")
