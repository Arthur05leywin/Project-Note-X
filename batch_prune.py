import os
import re
from bs4 import BeautifulSoup

base_dir = r'c:\Users\sayan\Downloads\biochem Note X'
files_to_prune = [
    r'modules\module-01\enzyme_inhibition_X.html',
    r'modules\module-02\carb_metabolism_notes X.html',
    r'modules\module-03\lipid_metabolism_notes_X.html',
    r'modules\module-04\module04_protein_haemoglobin_X.html',
    r'modules\module-05\module05_nucleotide_metabolism_X.html',
    r'modules\module-06\module06_molecular_biology_X.html'
]

for relative_path in files_to_prune:
    file_path = os.path.join(base_dir, relative_path)
    print(f"Aggressively pruning: {relative_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    count = 0

    # 1. Hide all `.card` elements that do NOT contain a high-yield/active-recall marker
    for card in soup.find_all('div', class_='card'):
        # Check if it has an active recall class anywhere inside it
        has_viva_ans = card.find('div', class_='viva-ans') is not None
        has_viva_section = card.find('div', class_='viva-section') is not None
        has_mnemonic = card.find('div', class_=re.compile(r'mnemonic(-box)?')) is not None
        has_key_fact = card.find('div', class_='key-fact') is not None
        
        # Check if the card itself is explicitly marked as high yield via badge
        has_high_yield_badge = card.find('span', string=re.compile(r'high-?yield', re.I)) is not None
        
        # If it has none of these, hide it from print
        if not (has_viva_ans or has_viva_section or has_mnemonic or has_key_fact or has_high_yield_badge):
            classes = card.get('class', [])
            if 'd-print-none' not in classes:
                classes.append('d-print-none')
                card['class'] = classes
                count += 1

    # 2. Hide standalone `.flow-box` chains that are conceptual (not inside a viva-ans)
    # Most standalone flowcharts are inside `.flowchart` or `.flowchart-container`
    for flowchart in soup.find_all('div', class_=re.compile(r'flowchart.*')):
        # Don't hide if it's inside an active recall answer
        if flowchart.find_parent('div', class_='viva-ans'):
            continue
            
        classes = flowchart.get('class', [])
        if 'd-print-none' not in classes:
            classes.append('d-print-none')
            flowchart['class'] = classes
            count += 1

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"Aggressively hid {count} conceptual cards/flow-boxes from print for {relative_path}.\n")

