import re

mod_path = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module04_thorax.html"

with open(mod_path, 'r', encoding='utf-8') as f:
    html = f.read()

def get_img_html(num, title, filename, desc):
    if num:
        header = f'<div style="color:var(--accent);font-family:\'JetBrains Mono\',monospace;font-size:11px;margin-bottom:8px;">DIAGRAM {num} — {title}</div>'
    else:
        header = f'<div style="color:var(--accent);font-family:\'JetBrains Mono\',monospace;font-size:11px;margin-bottom:8px;">{title}</div>'
        
    return f"""
  <div class="wiki-img" style="text-align: center; margin: 24px 0;">
    {header}
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/{filename}" alt="{title}" loading="lazy" style="max-width: 100%; border-radius: 8px;">
    <div class="wiki-caption" style="font-size:11px;color:var(--text2);text-align:center;margin-top:8px;">{desc}</div>
  </div>
"""

insertions = [
    (r'(<h2>Thoracic <em>Wall</em></h2>\s*</div>)', 
     get_img_html('01', 'Typical Rib', 'Gray122.png', 'A central rib of the left side (inferior aspect) — Gray\'s Anatomy')),
     
    (r'(<h2><em>Pleura</em></h2>\s*</div>)', 
     get_img_html('', 'Pleural Cavities', 'Gray974.png', 'Pleural reflection and recesses — Gray\'s Anatomy')),
     
    (r'(<h2>Lungs <em>&amp; Lobes</em></h2>\s*</div>)', 
     get_img_html('03', 'Right Lung Medial Surface', 'Gray972.png', 'Mediastinal surface of right lung — Gray\'s Anatomy') +
     get_img_html('', 'Left Lung Medial Surface', 'Gray973.png', 'Mediastinal surface of left lung — Gray\'s Anatomy')),
     
    (r'(<h2>Bronchopulmonary <em>Segments</em></h2>\s*</div>)', 
     get_img_html('04 & 05', 'Bronchopulmonary Segments', 'Bronchopulmonary_segments.svg', 'Bronchopulmonary segments of the right and left lungs')),
     
    (r'(<h2>Trachea <em>&amp; Bronchi</em></h2>\s*</div>)', 
     get_img_html('', 'Trachea and Bronchi', 'Gray961.png', 'The trachea and its primary bronchi — Gray\'s Anatomy')),
     
    (r'(<h2>Heart — External <em>&amp; Chambers</em></h2>\s*</div>)', 
     get_img_html('06', 'External Features of Heart', 'Gray492.png', 'Anterior (sternocostal) surface of the heart — Gray\'s Anatomy')),
     
    (r'(<h2>Conducting <em>System</em></h2>\s*</div>)', 
     get_img_html('07', 'Conducting System', 'Conduction_system_of_the_heart_without_the_Heart.png', 'Schematic of the heart conduction system')),
     
    (r'(<h2>Coronary <em>Arteries</em></h2>\s*</div>)', 
     get_img_html('08', 'Coronary Arteries', 'Gray498.png', 'Coronary arteries and their branches — Gray\'s Anatomy')),
     
    (r'(<h2>Cardiac <em>Valves</em></h2>\s*</div>)', 
     get_img_html('', 'Cardiac Valves', 'Gray497.png', 'Base of ventricular portion of heart showing valves — Gray\'s Anatomy')),
     
    (r'(<h2>Pericardium <em>&amp; Mediastinum</em></h2>\s*</div>)', 
     get_img_html('09', 'Pericardial Sinuses', 'Gray490.png', 'Posterior wall of the pericardial sac showing sinuses — Gray\'s Anatomy')),
     
    (r'(<h2><em>Diaphragm</em></h2>\s*</div>)', 
     get_img_html('10', 'Diaphragm', 'Gray391.png', 'The diaphragm, under surface — Gray\'s Anatomy')),
]

for pattern, img_html in insertions:
    # Need to handle potential &amp; vs & in html text
    pattern = pattern.replace('&amp;', '&')
    html, count = re.subn(pattern, r'\1' + img_html, html, flags=re.DOTALL)
    if count == 0:
        print(f"Failed to find pattern: {pattern}")
    else:
        print(f"Inserted image for {pattern}")

# Remove Diagram Placeholders section entirely
html = re.sub(r'<!-- ════════════════════════════════ S11: PLACEHOLDERS ════════════════════════════════ -->.*?<div id="s12">', r'<div id="s12">', html, flags=re.DOTALL)

# Fallback regex if the above didn't catch the exact comment
html = re.sub(r'<div id="s11">.*?<h2>Diagram <em>Placeholders</em></h2>.*?</div>\s*</div>\s*<div class="divider"></div>', '', html, flags=re.DOTALL)

with open(mod_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Module 4 updated successfully.")
