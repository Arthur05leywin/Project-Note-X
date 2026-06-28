import os
import sys
import re
import argparse
from weasyprint import HTML, CSS

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Metadata mapping for all Anatomy modules
MODULES_METADATA = {
    1: {
        "title": "General Anatomy",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "module01_general_anatomy.html"),
        "pdf": "anatomy_module01_general_anatomy.pdf",
    },
    2: {
        "title": "Upper Limb",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module02_upper_limb.html"),
        "pdf": "anatomy_module02_upper_limb.pdf",
    },
    3: {
        "title": "Lower Limb",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module03_lower_limb.html"),
        "pdf": "anatomy_module03_lower_limb.pdf",
    },
    4: {
        "title": "Thorax",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module04_thorax.html"),
        "pdf": "anatomy_module04_thorax.pdf",
    },
    5: {
        "title": "Abdomen",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module05_abdomen.html"),
        "pdf": "anatomy_module05_abdomen.pdf",
    },
    6: {
        "title": "Pelvis & Perineum",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module06_pelvis_perineum.html"),
        "pdf": "anatomy_module06_pelvis_perineum.pdf",
    },
    7: {
        "title": "Head & Neck",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module07_head_neck.html"),
        "pdf": "anatomy_module07_head_neck.pdf",
    },
    8: {
        "title": "Neuroanatomy",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "module08_neuroanatomy.html"),
        "pdf": "anatomy_module08_neuroanatomy.pdf",
    },
    9: {
        "title": "Embryology",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "module09_embryology.html"),
        "pdf": "anatomy_module09_embryology.pdf",
    },
    10: {
        "title": "Histology",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "module10_histology.html"),
        "pdf": "anatomy_module10_histology.pdf",
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

def compile_pdf(module_id):
    if module_id not in MODULES_METADATA:
        print(f"[ERROR] Module {module_id} is not configured.")
        return False
        
    meta = MODULES_METADATA[module_id]
    
    html_path = meta["file"]
    pdf_out_path = os.path.join(ROOT_DIR, meta["pdf"])
    label = "MASTERCLASS COURSE"
        
    if not os.path.exists(html_path):
        print(f"[ERROR] Source file not found: {html_path}")
        return False

    print(f"\n=======================================================")
    print(f"[COMPILING] Module {module_id:02d} ({label}): {meta['title']}")
    print(f"            Source: {os.path.basename(html_path)}")
    print(f"            Target: {os.path.basename(pdf_out_path)}")
    print(f"=======================================================")

    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # WeasyPrint does not execute JS, so we manually open <details> tags
        html_content = html_content.replace('<details>', '<details open>')
        
        # Inject CSS for page margins, headers and footers
        page_css = f"""
        @page {{
            size: A4;
            margin: 20mm 10mm;
            @top-left {{
                content: "MBBS ANATOMY NOTES";
                font-size: 8px;
                font-family: 'IBM Plex Mono', monospace;
                color: #8a90a8;
            }}
            @top-right {{
                content: "{label} · MODULE {module_id:02d}";
                font-size: 8px;
                font-family: 'IBM Plex Mono', monospace;
                color: #8a90a8;
            }}
            @bottom-left {{
                content: "{meta['title']}";
                font-size: 8px;
                font-family: 'IBM Plex Mono', monospace;
                color: #8a90a8;
            }}
            @bottom-right {{
                content: "Page " counter(page) " of " counter(pages);
                font-size: 8px;
                font-family: 'IBM Plex Mono', monospace;
                color: #8a90a8;
            }}
        }}
        """
        
        # Insert CSS before closing head tag, or fallback to prepending
        if '</head>' in html_content:
            html_content = html_content.replace('</head>', f'<style>\n{page_css}\n</style>\n</head>')
        else:
            html_content = f'<style>\n{page_css}\n</style>\n' + html_content
            
        file_url = f"file:///{os.path.abspath(html_path).replace('\\', '/')}"
        
        HTML(string=html_content, base_url=file_url).write_pdf(pdf_out_path)
        print(f"[SUCCESS] PDF generated successfully at {pdf_out_path}")
        
        page_count = count_pdf_pages(pdf_out_path)
        print(f"               - Total Page Count: {page_count} pages")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to compile PDF: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programmatic PDF Note Compiler for Anatomy")
    parser.add_argument("--module", type=int, choices=range(1, 11), help="Specific module ID to compile (1-10)")
    parser.add_argument("--all", action="store_true", help="Compile all modules")
    
    args = parser.parse_args()
    
    if args.all:
        all_success = True
        for i in range(1, 11):
            if not compile_pdf(i):
                all_success = False
        sys.exit(0 if all_success else 1)
    else:
        module_to_run = args.module if args.module else 1
        res = compile_pdf(module_to_run)
        sys.exit(0 if res else 1)
