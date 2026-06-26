import json
import glob
from bs4 import BeautifulSoup
import os

files = glob.glob('anatomy modules/*.html')
data = []
count = 0

for f in files:
    with open(f, encoding='utf-8') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    
    module_name = os.path.basename(f).replace('.html', '').replace('anatomy_module', '').replace('module', '').replace('_', ' ').strip().title()
    
    viva_sections = soup.find_all('div', class_='viva-section')
    
    for section in viva_sections:
        title_bar = section.find('div', class_='viva-title-bar')
        category = title_bar.text.strip() if title_bar else "General"
        
        summaries = section.find_all('summary')
        for q in summaries:
            vq = q.find(class_='viva-q')
            ans = q.find_next_sibling('div', class_='viva-ans')
            
            if vq and ans:
                ans_text = ""
                for child in ans.children:
                    if child.name == 'ul':
                        for li in child.find_all('li'):
                            ans_text += f"- {li.text.strip()}\n"
                    elif child.name == 'p':
                        ans_text += f"{child.text.strip()}\n"
                    elif child.string:
                        ans_text += child.string.strip() + "\n"
                        
                data.append({
                    'module': module_name,
                    'category': category,
                    'question': vq.text.strip(),
                    'raw_answer': ans_text.strip()
                })
                count += 1

print(f"Total questions found: {count}")

out_path = 'viva_raw.json'
with open(out_path, 'w', encoding='utf-8') as out_file:
    json.dump(data, out_file, indent=2)
print(f"Saved to {out_path}")
