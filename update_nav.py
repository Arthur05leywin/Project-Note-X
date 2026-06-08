import glob
import os

for f in glob.glob('*.html'):
    if f in ['anatomy.html', 'anatomy_index.html']:
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    target = '<a href="biochemistry.html">Biochemistry</a>'
    replacement = '<a href="biochemistry.html">Biochemistry</a>\n        <a href="anatomy.html">Anatomy</a>'
    
    if target in content:
        content = content.replace(target, replacement)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
