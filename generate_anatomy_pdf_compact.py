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
        "pdf": "anatomy_module01_general_anatomy_compact.pdf",
    },
    2: {
        "title": "Upper Limb",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module02_upper_limb.html"),
        "pdf": "anatomy_module02_upper_limb_compact.pdf",
    },
    3: {
        "title": "Lower Limb",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module03_lower_limb.html"),
        "pdf": "anatomy_module03_lower_limb_compact.pdf",
    },
    4: {
        "title": "Thorax",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module04_thorax.html"),
        "pdf": "anatomy_module04_thorax_compact.pdf",
    },
    5: {
        "title": "Abdomen",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module05_abdomen.html"),
        "pdf": "anatomy_module05_abdomen_compact.pdf",
    },
    6: {
        "title": "Pelvis & Perineum",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module06_pelvis_perineum.html"),
        "pdf": "anatomy_module06_pelvis_perineum_compact.pdf",
    },
    7: {
        "title": "Head & Neck",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "anatomy_module07_head_neck.html"),
        "pdf": "anatomy_module07_head_neck_compact.pdf",
    },
    8: {
        "title": "Neuroanatomy",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "module08_neuroanatomy.html"),
        "pdf": "anatomy_module08_neuroanatomy_compact.pdf",
    },
    9: {
        "title": "Embryology",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "module09_embryology.html"),
        "pdf": "anatomy_module09_embryology_compact.pdf",
    },
    10: {
        "title": "Histology",
        "file": os.path.join(ROOT_DIR, "anatomy modules", "module10_histology.html"),
        "pdf": "anatomy_module10_histology_compact.pdf",
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
    label = "COMPACT MASTERCLASS"
        
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
            
        html_content = html_content.replace('<details>', '<details open>')
        
        page_css = f"""
        @media print {{
            body {{
                font-size: 10px !important;
                line-height: 1.25 !important;
            }}
            .card {{
                padding: 10px 14px !important;
                margin-bottom: 10px !important;
                break-inside: avoid;
            }}
            .section-header {{
                padding: 12px 15px !important;
                margin-top: 15px !important;
                margin-bottom: 10px !important;
            }}
            h1 {{ font-size: 20px !important; margin-bottom: 10px !important; }}
            h2 {{ font-size: 16px !important; margin-bottom: 8px !important; }}
            h3 {{ font-size: 14px !important; margin-bottom: 6px !important; }}
            .hero {{
                padding: 20px 20px !important;
                min-height: auto !important;
            }}
            .hero h1 {{
                font-size: 26px !important;
            }}
            .two-col {{
                grid-template-columns: repeat(2, 1fr) !important;
                gap: 12px !important;
            }}
            .keypoint, .clinical-box, .mnemonic-box, .warn-box {{
                padding: 10px 12px 10px 35px !important;
                margin-bottom: 8px !important;
                font-size: 9.5px !important;
                display: block !important;
                position: relative !important;
                page-break-inside: avoid;
                word-break: normal !important;
            }}
            .keypoint::before, .clinical-box::before, .mnemonic-box::before, .warn-box::before {{
                font-size: 14px !important;
                left: 10px !important;
                top: 10px !important;
            }}
            table th, table td {{
                padding: 6px 8px !important;
                font-size: 9.5px !important;
            }}
            ul, ol {{
                padding-left: 20px !important;
                margin-bottom: 6px !important;
            }}
            li {{
                margin-bottom: 3px !important;
            }}
            img.wiki-img {{
                max-width: 80% !important;
                margin: 5px auto !important;
            }}
            .toc {{
                padding: 12px !important;
                columns: 2;
            }}
            .toc-link {{
                padding: 4px 8px !important;
                font-size: 10px !important;
            }}
        }}
        @page {{
            size: A4;
            margin: 12mm 10mm;
            @top-left {{
                content: "MBBS ANATOMY NOTES";
                font-size: 7px;
                font-family: 'IBM Plex Mono', monospace;
                color: #8a90a8;
            }}
            @top-right {{
                content: "{label} · MODULE {module_id:02d}";
                font-size: 7px;
                font-family: 'IBM Plex Mono', monospace;
                color: #8a90a8;
            }}
            @bottom-left {{
                content: "{meta['title']}";
                font-size: 7px;
                font-family: 'IBM Plex Mono', monospace;
                color: #8a90a8;
            }}
            @bottom-right {{
                content: "Page " counter(page) " of " counter(pages);
                font-size: 7px;
                font-family: 'IBM Plex Mono', monospace;
                color: #8a90a8;
            }}
        }}
        """
        
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
    parser = argparse.ArgumentParser(description="Programmatic PDF Note Compiler for Anatomy (Compact)")
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
