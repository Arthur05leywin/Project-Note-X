import re

with open('modules/module-04/scratch/haem_degradation_svg.txt', 'r', encoding='utf-8') as f:
    svg_content = f.read()

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    pattern = r'<div class="flowchart">\s*<div class="flow-title">\s*Haem → Bilirubin → Excretion — Complete Pathway\s*</div>\s*<div class="flow-v">.*?</div>\s*</div>'
    
    text = re.sub(pattern, svg_content, text, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

replace_in_file('modules/module-04/module04_protein_haemoglobin.html')
replace_in_file('modules/module-04/module04_protein_haemoglobin_X.html')
print('SVG injected successfully.')
