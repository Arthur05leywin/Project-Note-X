import re

filepath = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module07_head_neck.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Diagram 7.1
rep1 = """    <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
      <div class="diag-num">DIAGRAM 7.1</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray188.png" alt="Pterion" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Pterion on lateral skull (Gray's Anatomy)</div>
    </div>"""
content = re.sub(r'<div class="diagram-placeholder"[^>]*>\s*<div class="diag-num">DIAGRAM 7.1</div>.*?</div>\s*</div>', rep1, content, flags=re.DOTALL)

# Replace Diagram 7.2
rep2 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diag-num">DIAGRAM 7.2</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Cavernous_sinus.png" alt="Cavernous Sinus" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Cavernous Sinus coronal section (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diag-num">DIAGRAM 7.2</div>.*?</div>\s*</div>', rep2, content, flags=re.DOTALL)

# Replace Diagram 7.3
rep3 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diag-num">DIAGRAM 7.3</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/External_carotid_artery.png" alt="ECA branches" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">External Carotid Artery (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diag-num">DIAGRAM 7.3</div>.*?</div>\s*</div>', rep3, content, flags=re.DOTALL)

# Replace Diagram 7.4
rep4 = """    <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
      <div class="diag-num">DIAGRAM 7.4</div>
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1024.png" alt="Parotid gland" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
      <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Parotid and Salivary Glands (Gray's Anatomy)</div>
    </div>"""
content = re.sub(r'<div class="diagram-placeholder"[^>]*>\s*<div class="diag-num">DIAGRAM 7.4</div>.*?</div>\s*</div>', rep4, content, flags=re.DOTALL)

# Replace Diagram 7.5
rep5 = """  <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
    <div class="diag-num">DIAGRAM 7.5</div>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1174.png" alt="Thyroid gland posterior view" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;margin-top:10px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:6px;">Thyroid and Parathyroid Glands Posterior View (Gray's Anatomy)</div>
  </div>"""
content = re.sub(r'<div class="diagram-placeholder">\s*<div class="diag-num">DIAGRAM 7.5</div>.*?</div>\s*</div>', rep5, content, flags=re.DOTALL)

# Footer
content = content.replace("Diagram placeholders ready for tablet art", "Includes Gray's Anatomy diagrams")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Module 7 placeholders replaced successfully.")
