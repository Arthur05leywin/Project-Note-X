import os
import re
from bs4 import BeautifulSoup

ROOT_DIR = r"c:\Users\sayan\Downloads\biochem Note X"

SHIPPING_MODULES = [
    "modules/module-01/enzyme_inhibition_notes.html",
    "modules/module-01/enzyme_inhibition_X.html",
    "modules/module-02/carb_metabolism_notes.html",
    "modules/module-02/carb_metabolism_notes X.html",
    "modules/module-03/lipid_metabolism_notes.html",
    "modules/module-03/lipid_metabolism_notes_X.html",
    "modules/module-04/module04_protein_haemoglobin.html",
    "modules/module-04/module04_protein_haemoglobin_X.html",
    "modules/module-05/module05_nucleotide_metabolism.html",
    "modules/module-05/module05_nucleotide_metabolism_X.html",
    "modules/module-06/module06_molecular_biology.html",
    "modules/module-06/module06_molecular_biology_X.html",
    "modules/module-07/module07_biological_oxidation.html",
    "modules/module-07/module07_biological_oxidation_X.html",
    "modules/module-08/module08_nutrition_vitamins.html",
    "modules/module-08/module08_nutrition_vitamins_X.html",
    "modules/module-09/module09_clinical_biochemistry.html",
    "modules/module-09/module09_clinical_biochemistry_X.html",
    "modules/module-10/module10_immunochemistry_oncogenesis.html",
    "modules/module-10/module10_immunochemistry_oncogenesis_X.html"
]

for relative_path in SHIPPING_MODULES:
    file_path = os.path.join(ROOT_DIR, relative_path)
    print(f"Fixing {relative_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix the stray "Notes" word right after </title>
    html = re.sub(r'</title>\s*Notes', '</title>', html)

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Remove old brand-container
    for container in soup.find_all('div', class_='brand-container'):
        container.decompose()

    # Also remove any rogue brand-logo image if it's floating outside a container
    for img in soup.find_all('img', class_='brand-logo'):
        if not img.find_parent('div', class_='brand-bar'):
            img.decompose()

    # 2. Update Footer
    for footer in soup.find_all('div', class_='footer-warning'):
        if "Compiled for personal academic use" in footer.text:
            footer.string = "Premium Academic Resource • All Rights Reserved"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"  Fixed {relative_path}")

