import os
from bs4 import BeautifulSoup

file_path = r'c:\Users\sayan\Downloads\biochem Note X\modules\module-10\module10_immunochemistry_oncogenesis_X.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

hidden_count = 0

for container in soup.find_all(['div'], class_=['card', 'flow-box']):
    # Only keep if it has a mnemonic, key-fact, viva-ans, or details
    if not container.find(['details', 'div'], class_=['viva-ans', 'viva-section', 'mnemonic', 'key-fact']):
        # If it doesn't have any of these, we hide it from print
        if 'd-print-none' not in container.get('class', []):
            classes = container.get('class', [])
            classes.append('d-print-none')
            container['class'] = classes
            hidden_count += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f"Aggressively hid {hidden_count} conceptual cards/flow-boxes from print.")
