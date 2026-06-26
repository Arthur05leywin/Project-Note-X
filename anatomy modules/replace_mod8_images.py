import re

filepath = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\module08_neuroanatomy.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Diagram 01
rep1 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diagram-num">DIAGRAM 01</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray734.png" alt="Ventricular System" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Relations of the ventricles to the surface of the brain (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diagram-num">DIAGRAM 01</div>.*?</div>\s*</div>', rep1, content, flags=re.DOTALL)

# Replace Diagram 02
rep2 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diagram-num">DIAGRAM 02</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Spinal_cord_tracts_-_English.svg" alt="Spinal Cord Tracts" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Spinal Cord Tracts (Wikimedia Commons)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diagram-num">DIAGRAM 02</div>.*?</div>\s*</div>', rep2, content, flags=re.DOTALL)

# Replace Diagram 03
rep3 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diagram-num">DIAGRAM 03</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray683.png" alt="Brainstem Anterior" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Brainstem Anterior Surface (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diagram-num">DIAGRAM 03</div>.*?</div>\s*</div>', rep3, content, flags=re.DOTALL)

# Replace Diagram 04
rep4 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diagram-num">DIAGRAM 04</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray726.png" alt="Lateral Surface of Cerebral Hemisphere" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Lateral Surface of Cerebral Hemisphere (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diagram-num">DIAGRAM 04</div>.*?</div>\s*</div>', rep4, content, flags=re.DOTALL)

# Replace Diagram 05
rep5 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diagram-num">DIAGRAM 05</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray516.png" alt="Circle of Willis" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Circle of Willis (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diagram-num">DIAGRAM 05</div>.*?</div>\s*</div>', rep5, content, flags=re.DOTALL)

# Footer
content = content.replace("Diagram placeholders ready for tablet art", "Includes Gray's Anatomy diagrams")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Module 8 placeholders replaced successfully.")
