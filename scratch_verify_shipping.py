import os
import re
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

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

files_to_check = [os.path.join(ROOT_DIR, *path.split('/')) for path in SHIPPING_MODULES]

print("======================================================================")
print("[START] Programmatic Shipping Verification Pipeline (Modules 01 - 06)")
print("======================================================================\n")

all_passed = True

for path in files_to_check:
    if not os.path.exists(path):
        print(f"[FAIL] Missing file: {os.path.relpath(path, ROOT_DIR)}")
        all_passed = False
        continue
        
    print(f"Checking: {os.path.relpath(path, ROOT_DIR)}")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Strip the CSS style block to avoid false positives inside stylesheet rules
    body_content = content.split("</style>")[-1] if "</style>" in content else content
    
    issues = []
    
    # 1. Check for WBUHS (should be MBBS)
    wbuhs_matches = re.findall(r'\bWBUHS\b', body_content, re.IGNORECASE)
    if wbuhs_matches:
        issues.append(f"Contains legacy 'WBUHS' references ({len(wbuhs_matches)} count)")
        
    # 2. Check for KIMS or NMO Bengal references
    kims_matches = re.findall(r'\bKIMS\b|\bNMO\b|\bBengal\b', body_content, re.IGNORECASE)
    # Ignore the support phone number or address if they match, but check text content
    if kims_matches:
        issues.append(f"Contains regional KIMS/NMO/Bengal references ({len(kims_matches)} count)")
        
    # 3. Check for raw markdown leftover bold/italics
    # Match words wrapped in double asterisks e.g. **text** (except in HTML comments)
    md_bolds = re.findall(r'\*\*[^*]+\*\*|_[^_]+_', body_content)
    if md_bolds:
        issues.append(f"Contains raw markdown formatting (bolds/italics): {md_bolds[:3]}...")
        
    # 4. Check for raw LaTeX delimiters or commands
    latex_chars = re.findall(r'\$[^\$]+\$|\\alpha|\\beta|\\rightarrow|\\gamma|\\Delta', body_content)
    if latex_chars:
        issues.append(f"Contains raw LaTeX markup/symbols: {latex_chars[:3]}...")
        
    # 5. Check for local file URL encoding problems in image sources
    # Look for src="../../Caffeine%20%26%20Cadaver.jpg" or similar
    bad_img_paths = re.findall(r'src=["\'][^"\']*%20[^"\']*["\']|src=["\'][^"\']*%26[^"\']*["\']', body_content)
    # Note: ampersands inside HTML attributes are fine if written as &amp;
    percent_encodings = re.findall(r'src=["\'][^"\']*%20%26%20[^"\']*["\']', body_content)
    if percent_encodings:
        issues.append("Contains raw URL-encoded image paths (%20%26%20) instead of space/HTML entity format")
        
    # 6. Check for legacy flowchart negative margins
    neg_margins = re.findall(r'margin-left\s*:\s*-\d+px', body_content)
    if neg_margins:
        issues.append(f"Contains layout-breaking negative margins: {neg_margins}")
        
    # 7. Check if cover page has duplicate tag wrappers
    if "cover-tag" in body_content:
        cover_tag_count = body_content.count("cover-tag")
        if cover_tag_count > 1:
            issues.append(f"Duplicate cover page tags detected ({cover_tag_count} count)")
            
    if issues:
        print("  [FAIL] Issues detected:")
        for iss in issues:
            print(f"    - {iss}")
        all_passed = False
    else:
        print("  [PASS] Shipping Ready! Structure is pristine.")
    print("-" * 70)

if all_passed:
    print("\n[SUCCESS] All files are 100% compliant with standard MBBS & Caffeine & Cadaver shipping criteria!")
else:
    print("\n[WARNING] Some files have remaining legacy/formatting compliance issues. Action required.")
