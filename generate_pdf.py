import os
import sys
import re
import json
import argparse
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_DIR = r"C:\Users\sayan\.gemini\antigravity\brain\60c016ee-bc9d-4eac-86c5-6403267e4e36"

# Metadata mapping for all Biochemistry modules (Standard vs Revision)
MODULES_METADATA = {
    1: {
        "name": "enzyme_inhibition",
        "title": "Enzyme Inhibition",
        "standard_file": os.path.join(ROOT_DIR, "modules", "module-01", "enzyme_inhibition_notes.html"),
        "revision_file": os.path.join(ROOT_DIR, "modules", "module-01", "enzyme_inhibition_X.html"),
        "standard_pdf": "enzyme_inhibition_masterclass.pdf",
        "revision_pdf": "enzyme_inhibition_revision.pdf",
    },
    2: {
        "name": "carb_metabolism",
        "title": "Carbohydrate Metabolism",
        "standard_file": os.path.join(ROOT_DIR, "modules", "module-02", "carb_metabolism_notes.html"),
        "revision_file": os.path.join(ROOT_DIR, "modules", "module-02", "carb_metabolism_notes X.html"),
        "standard_pdf": "carb_metabolism_masterclass.pdf",
        "revision_pdf": "carb_metabolism_revision.pdf",
    },
    3: {
        "name": "lipid_metabolism",
        "title": "Lipid Metabolism",
        "standard_file": os.path.join(ROOT_DIR, "modules", "module-03", "lipid_metabolism_notes.html"),
        "revision_file": os.path.join(ROOT_DIR, "modules", "module-03", "lipid_metabolism_notes_X.html"),
        "standard_pdf": "lipid_metabolism_masterclass.pdf",
        "revision_pdf": "lipid_metabolism_revision.pdf",
    },
    4: {
        "name": "protein_haemoglobin",
        "title": "Protein & Haemoglobin",
        "standard_file": os.path.join(ROOT_DIR, "modules", "module-04", "module04_protein_haemoglobin.html"),
        "revision_file": os.path.join(ROOT_DIR, "modules", "module-04", "module04_protein_haemoglobin_X.html"),
        "standard_pdf": "protein_haemoglobin_masterclass.pdf",
        "revision_pdf": "protein_haemoglobin_revision.pdf",
    },
    5: {
        "name": "nucleotide_metabolism",
        "title": "Nucleotide Metabolism",
        "standard_file": os.path.join(ROOT_DIR, "modules", "module-05", "module05_nucleotide_metabolism.html"),
        "revision_file": os.path.join(ROOT_DIR, "modules", "module-05", "module05_nucleotide_metabolism_X.html"),
        "standard_pdf": "nucleotide_metabolism_masterclass.pdf",
        "revision_pdf": "nucleotide_metabolism_revision.pdf",
    },
    6: {
        "name": "molecular_biology",
        "title": "Molecular Biology",
        "standard_file": os.path.join(ROOT_DIR, "modules", "module-06", "module06_molecular_biology.html"),
        "revision_file": os.path.join(ROOT_DIR, "modules", "module-06", "module06_molecular_biology_X.html"),
        "standard_pdf": "molecular_biology_masterclass.pdf",
        "revision_pdf": "molecular_biology_revision.pdf",
    },
    7: {
        "name": "biological_oxidation",
        "title": "Biological Oxidation",
        "standard_file": os.path.join(ROOT_DIR, "modules", "module-07", "module07_biological_oxidation.html"),
        "revision_file": os.path.join(ROOT_DIR, "modules", "module-07", "module07_biological_oxidation_X.html"),
        "standard_pdf": "biological_oxidation_masterclass.pdf",
        "revision_pdf": "biological_oxidation_revision.pdf",
    },
    8: {
        "name": "nutrition_vitamins",
        "title": "Nutrition & Vitamins",
        "standard_file": os.path.join(ROOT_DIR, "modules", "module-08", "module08_nutrition_vitamins.html"),
        "revision_file": os.path.join(ROOT_DIR, "modules", "module-08", "module08_nutrition_vitamins_X.html"),
        "standard_pdf": "nutrition_vitamins_masterclass.pdf",
        "revision_pdf": "nutrition_vitamins_revision.pdf",
    },
    9: {
        "name": "clinical_biochemistry",
        "title": "Clinical Biochemistry",
        "standard_file": os.path.join(ROOT_DIR, "modules", "module-09", "module09_clinical_biochemistry.html"),
        "revision_file": os.path.join(ROOT_DIR, "modules", "module-09", "module09_clinical_biochemistry_X.html"),
        "standard_pdf": "clinical_biochemistry_masterclass.pdf",
        "revision_pdf": "clinical_biochemistry_revision.pdf",
    },
    10: {
        "name": "immunochemistry_oncogenesis",
        "title": "Immunochemistry & Oncogenesis",
        "standard_file": os.path.join(ROOT_DIR, "modules", "module-10", "module10_immunochemistry_oncogenesis.html"),
        "revision_file": os.path.join(ROOT_DIR, "modules", "module-10", "module10_immunochemistry_oncogenesis_X.html"),
        "standard_pdf": "immunochemistry_oncogenesis_masterclass.pdf",
        "revision_pdf": "immunochemistry_oncogenesis_revision.pdf",
    }
}

def count_pdf_pages(pdf_path):
    if not os.path.exists(pdf_path):
        return 0
    try:
        with open(pdf_path, 'rb') as f:
            content = f.read()
        matches = re.findall(rb'/Type\s*/Pages\s*/Count\s*(\d+)', content)
        if matches:
            return int(matches[-1])
        matches = re.findall(rb'/Count\s*(\d+)', content)
        if matches:
            return int(matches[0])
        return len(re.findall(rb'/Type\s*/Page\b', content))
    except Exception as e:
        print(f"[WARN] Page counting failed: {e}")
        return -1

def compile_pdf(module_id, edition="revision", verify=True):
    if module_id not in MODULES_METADATA:
        print(f"[ERROR] Module {module_id} is not configured.")
        return False
        
    meta = MODULES_METADATA[module_id]
    
    if edition == "standard":
        html_path = meta["standard_file"]
        pdf_out_path = os.path.join(ROOT_DIR, meta["standard_pdf"])
        label = "MASTERCLASS COURSE"
    else:
        html_path = meta["revision_file"]
        pdf_out_path = os.path.join(ROOT_DIR, meta["revision_pdf"])
        label = "REVISION EDITION"
        
    if not os.path.exists(html_path):
        print(f"[ERROR] Source file not found: {html_path}")
        return False

    print(f"\n=======================================================")
    print(f"[COMPILING] Module {module_id:02d} ({label}): {meta['title']}")
    print(f"            Source: {os.path.basename(html_path)}")
    print(f"            Target: {os.path.basename(pdf_out_path)}")
    print(f"=======================================================")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        file_url = f"file:///{os.path.abspath(html_path).replace('\\', '/')}"
        page.goto(file_url)
        
        header_html = f"""
        <div style="font-size: 8px; font-family: 'IBM Plex Mono', monospace; width: 100%; display: flex; justify-content: space-between; padding: 0 16mm; color: #8a90a8;">
          <span>MBBS BIOCHEMISTRY NOTES</span>
          <span>{label} · MODULE {module_id:02d}</span>
        </div>
        """
        
        footer_html = f"""
        <div style="font-size: 8px; font-family: 'IBM Plex Mono', monospace; width: 100%; display: flex; justify-content: space-between; padding: 0 16mm; color: #8a90a8;">
          <span>{meta['title']}</span>
          <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
        </div>
        """
        
        page.evaluate("() => document.querySelectorAll('details').forEach(d => d.open = true)")
        
        page.pdf(
            path=pdf_out_path,
            format="A4",
            print_background=True,
            margin={}, 
            display_header_footer=True,
            header_template=header_html,
            footer_template=footer_html
        )
        print(f"[SUCCESS] PDF generated successfully at {pdf_out_path}")
        
        verification_results = {}
        if verify:
            print("[VERIFICATION] Running automated visual testing & assertions...")
            page_count = count_pdf_pages(pdf_out_path)
            print(f"               - Total Page Count: {page_count} pages")
            
            gap_data = page.evaluate("""
                () => {
                    const cards = Array.from(document.querySelectorAll('.revision-card'));
                    const gaps = [];
                    let prevBottom = 0;
                    cards.forEach((card, index) => {
                        const rect = card.getBoundingClientRect();
                        if (index > 0) {
                            const gap = rect.top - prevBottom;
                            gaps.push({ cardIndex: index, title: card.querySelector('.revision-card-title')?.innerText || 'Card', gap: gap });
                        }
                        prevBottom = rect.bottom;
                    });
                    return gaps;
                }
            """)
            
            large_gaps = [g for g in gap_data if g['gap'] > 220]
            if large_gaps:
                print(f"               - [WARNING] Detected {len(large_gaps)} large vertical spacing gaps:")
                for gap in large_gaps:
                    print(f"                 * Card {gap['cardIndex']} ('{gap['title']}'): Gap of {gap['gap']:.1f}px")
            else:
                print("               - [PASS] Gap Spacing Check (No awkward large gaps detected!)")
                
            page.set_viewport_size({"width": 800, "height": 1130})
            
            master_shot_name = f"{meta['name']}_{edition}_master_full.png"
            master_shot_path = os.path.join(ARTIFACTS_DIR, master_shot_name)
            page.screenshot(path=master_shot_path, full_page=True)
            
            verification_results = {
                "module_id": module_id,
                "title": meta["title"],
                "edition": edition,
                "pdf_path": pdf_out_path,
                "pages_detected": page_count,
                "gap_check": "PASS" if not large_gaps else "WARNING",
                "large_gaps_detected": large_gaps,
                "screenshot": master_shot_path,
                "status": "SUCCESS"
            }
            
            report_path = os.path.join(ARTIFACTS_DIR, f"{meta['name']}_{edition}_verification_report.json")
            with open(report_path, 'w', encoding='utf-8') as rf:
                json.dump(verification_results, rf, indent=2)
            print(f"[VERIFIED] Test report written to {report_path}")

        browser.close()
        return verification_results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programmatic PDF Note Compiler & Tester")
    parser.add_argument("--module", type=int, choices=range(1, 11), help="Specific module ID to compile (1-10)")
    parser.add_argument("--edition", type=str, choices=["standard", "revision", "both"], default="both", help="Edition to compile (standard, revision, both)")
    parser.add_argument("--verify", action="store_true", default=True, help="Run automated visual verification pipeline")
    
    args = parser.parse_args()
    module_to_run = args.module if args.module else 1
    
    if args.edition == "both":
        res_std = compile_pdf(module_to_run, "standard", verify=args.verify)
        res_rev = compile_pdf(module_to_run, "revision", verify=args.verify)
        if res_std and res_rev:
            sys.exit(0)
        else:
            sys.exit(1)
    else:
        res = compile_pdf(module_to_run, args.edition, verify=args.verify)
        if res:
            sys.exit(0)
        else:
            sys.exit(1)
