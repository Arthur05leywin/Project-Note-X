import os
import re

files_to_fix = [
    r'modules/module-04/module04_protein_haemoglobin.html',
    r'modules/module-04/module04_protein_haemoglobin_X.html',
    r'modules/module-05/module05_nucleotide_metabolism.html',
    r'modules/module-05/module05_nucleotide_metabolism_X.html',
    r'modules/module-06/module06_molecular_biology.html',
    r'modules/module-06/module06_molecular_biology_X.html',
    r'modules/module-07/module07_biological_oxidation.html',
    r'modules/module-07/module07_biological_oxidation_X.html',
    r'modules/module-08/module08_nutrition_vitamins.html',
    r'modules/module-08/module08_nutrition_vitamins_X.html',
    r'modules/module-09/module09_clinical_biochemistry.html',
    r'modules/module-09/module09_clinical_biochemistry_X.html',
    r'modules/module-10/module10_immunochemistry_oncogenesis.html',
    r'modules/module-10/module10_immunochemistry_oncogenesis_X.html'
]

for file_path in files_to_fix:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix URL-encoded image path
        content = content.replace('src="../../Caffeine%20%26%20Cadaver.jpg"', 'src="../../Caffeine &amp; Cadaver.jpg"')
        
        # Fix **bold** markdown
        # Need to be careful not to match inside comments or tags, but simple replace should work here
        content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content, flags=re.DOTALL)

        # Fix _italics_ markdown, ensuring it doesn't match inside URLs or class names
        content = re.sub(r'(?<!\w)_(.*?)_(?!\w)', r'<em>\1</em>', content, flags=re.DOTALL)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {file_path}')
