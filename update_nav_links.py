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

for file in html_files:
    path = os.path.join(base_dir, file)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove coming soon banner
    banner_pattern = re.compile(r'<!-- Coming soon banner -->.*?</div>\s*</div>', re.DOTALL)
    content = banner_pattern.sub('', content)

    # Change all badge-soon to badge-live
    content = content.replace('<span class="module-status-badge badge-soon">Coming Soon</span>', '<span class="module-status-badge badge-live">Live</span>')

    # Now let's try to update href for each module card
    # Usually it's <a href="..." class="module-card" ...>
    # or something similar. Let's find each module card block and update its href.
    
    for i in range(1, 11):
        mod_num = f"Module {i:02d}"
        target_href = module_links[mod_num]
        
        # Regex to find the <a> tag corresponding to this module.
        # This is tricky without parsing. Let's do a replace based on finding the module number in the inner text.
        # But wait, maybe the structure is exactly:
        # <a href="contact.html" class="module-card" style="--card-accent: var(--m01);">
        #   <div class="module-card-header">
        #     <span class="module-num">Module 01</span>
        
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
    
    # Replace Anatomy coming soon with live
    anatomy_old = '''<article class="subject-card muted-subject">
            <div class="subject-card-header">
              <span class="subject-tag coming-soon" style="background: rgba(214,60,60,0.1); color: #d63c3c; border-color: rgba(214,60,60,0.3);">⏳ SERIES COMING SOON</span>
              <span class="subject-code">AN 1.1</span>
            </div>
            <h3>Anatomy</h3>
            <p>Gross anatomy high-yield matrices, regional embryology trap boxes, and osteology viva rapid-fire prompts.</p>
            <div class="subject-card-footer">
              <span class="module-count">Preview Available</span>
              <a class="subject-link" href="anatomy.html" style="color: #d63c3c;">View Preview →</a>
            </div>
          </article>'''
          
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
          
    if anatomy_old in idx_content:
        idx_content = idx_content.replace(anatomy_old, anatomy_new)
    else:
        # Try a more robust regex if exact match fails
        pattern_anatomy = re.compile(r'<article class="subject-card muted-subject">.*?<span class="subject-code">AN 1\.1</span>.*?</div>\s*</article>', re.DOTALL)
        idx_content = pattern_anatomy.sub(anatomy_new, idx_content)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(idx_content)

print("Update complete")
