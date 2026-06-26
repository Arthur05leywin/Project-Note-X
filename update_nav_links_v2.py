import os
import re

base_dir = r"c:\Users\sayan\Downloads\biochem Note X"
html_files = ["anatomy.html", "anatomy_index.html"]

module_links = {
    "Module 01": "anatomy modules/module01_general_anatomy.html",
    "Module 02": "anatomy modules/anatomy_module02_upper_limb.html",
    "Module 03": "anatomy modules/anatomy_module03_lower_limb.html",
    "Module 04": "anatomy modules/anatomy_module04_thorax.html",
    "Module 05": "anatomy modules/anatomy_module05_abdomen.html",
    "Module 06": "anatomy modules/anatomy_module06_pelvis_perineum.html",
    "Module 07": "anatomy modules/anatomy_module07_head_neck.html",
    "Module 08": "anatomy modules/module08_neuroanatomy.html",
    "Module 09": "anatomy modules/module09_embryology.html",
    "Module 10": "anatomy modules/module10_histology.html"
}

banner_pattern = re.compile(r'<!-- Coming soon banner -->\s*<div class="coming-banner">.*?</p>\s*</div>\s*<a[^>]*>.*?</a>\s*</div>', re.DOTALL)

for file in html_files:
    path = os.path.join(base_dir, file)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove coming soon banner safely
    content = banner_pattern.sub('', content)

    # Change all badge-soon to badge-live
    content = content.replace('<span class="module-status-badge badge-soon">Coming Soon</span>', '<span class="module-status-badge badge-live">Live</span>')
    content = content.replace('<span class="module-status-badge badge-building">Building</span>', '<span class="module-status-badge badge-live">Live</span>')

    # Update href for each module card
    for i in range(1, 11):
        mod_num = f"Module {i:02d}"
        target_href = module_links[mod_num]
        
        # Regex to find the <a> tag corresponding to this module.
        pattern = re.compile(r'<a href="[^"]*" class="module-card"([^>]*)>\s*<div class="module-card-header">\s*<span class="module-num">' + mod_num + r'</span>')
        replacement = f'<a href="{target_href}" class="module-card"\\1>\n      <div class="module-card-header">\n        <span class="module-num">{mod_num}</span>'
        content = pattern.sub(replacement, content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Update index.html
index_path = os.path.join(base_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        idx_content = f.read()
    
    # Let's replace the anatomy card
    pattern_anatomy = re.compile(r'<article class="subject-card muted-subject">.*?<span class="subject-code">AN 1\.1</span>.*?</div>\s*</article>', re.DOTALL)
    
    anatomy_new = '''<article class="subject-card active-subject">
            <div class="subject-card-header">
              <span class="subject-tag live">🔴 LIVE PACK AVAILABLE</span>
              <span class="subject-code">AN 1.1</span>
            </div>
            <h3>Anatomy</h3>
            <p>Gross anatomy high-yield matrices, regional embryology trap boxes, and osteology viva rapid-fire prompts.</p>
            <div class="subject-card-footer">
              <span class="module-count">All 10 Modules Live</span>
              <a class="subject-link" href="anatomy.html">Access Series →</a>
            </div>
          </article>'''
          
    idx_content = pattern_anatomy.sub(anatomy_new, idx_content)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(idx_content)

print("Update v2 complete")
