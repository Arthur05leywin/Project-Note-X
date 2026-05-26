import re
import os

FILES_TO_CLEAN = [
    r"c:\Users\sayan\Downloads\biochem Note X\modules\module-02\carb_metabolism_notes.html",
    r"c:\Users\sayan\Downloads\biochem Note X\modules\module-02\carb_metabolism_notes X.html"
]

def clean_content(content):
    # 1. Convert markdown bold (**text**) to HTML strong
    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
    
    # 2. Convert markdown italics (*text*) to HTML em
    content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', content)
    
    # 3. Resolve LaTeX and Math symbols into proper HTML entities / Unicode
    replacements = [
        (r'$\alpha$-1,4', 'α-1,4'),
        (r'$\alpha$-1,6', 'α-1,6'),
        (r'$\alpha$-1,6-glucosidase', 'α-1,6-glucosidase'),
        (r'$\alpha$-1,6-glucosidic bond', 'α-1,6-glucosidic bond'),
        (r'$\alpha$-Ketoglutarate', 'α-Ketoglutarate'),
        (r'$\alpha$', 'α'),
        (r'$\beta$-islet', 'β-islet'),
        (r'$\beta$-chains', 'β-chains'),
        (r'$\beta$', 'β'),
        (r'$\delta$-ALA', 'δ-ALA'),
        (r'$\delta$', 'δ'),
        (r'$\rightarrow$', '→'),
        (r'$\rightarrow$', '→'),
        (r'$\times 2$', '×2'),
        (r'$\times 2$', '×2'),
        (r'$\approx 0.05 \text{ mM}$', '≈ 0.05 mM'),
        (r'$\approx 10 \text{ mM}$', '≈ 10 mM'),
        (r'$\approx$', '≈'),
        (r'$V_{max}$', 'V<sub>max</sub>'),
        (r'$V_{max}$', 'V<sub>max</sub>'),
        (r'$V_max$', 'V<sub>max</sub>'),
        (r'$K_m$', 'K<sub>m</sub>'),
        (r'$K_m$', 'K<sub>m</sub>'),
        (r'$Km$', 'K<sub>m</sub>'),
        (r'$P_i$', 'P<sub>i</sub>'),
        (r'$P_i$,', 'P<sub>i</sub>,'),
        (r'$Mg^{2+}$', 'Mg<sup>2+</sup>'),
        (r'$2 \text{ NADH} \times 2.5$', '2 NADH × 2.5'),
        (r'$\text{ NADH} \times 2.5$', 'NADH × 2.5'),
        (r'$2 \text{ NADH}$', '2 NADH'),
        (r'$\approx 0.05 \text{ mM}$', '≈ 0.05 mM'),
        (r'$\text{ mM}$', ' mM'),
        (r'$CO_2$', 'CO<sub>2</sub>'),
        (r'$CO_2', 'CO<sub>2</sub>'),
        (r'$CoA-SH$', 'CoA-SH'),
        (r'$FADH_2$', 'FADH<sub>2</sub>'),
        (r'$NAD^+$', 'NAD<sup>+</sup>'),
        (r'$NAD^+', 'NAD<sup>+</sup>'),
        (r'$NADH + H^+$', 'NADH + H<sup>+</sup>'),
        (r'$Ca^{2+$', 'Ca<sup>2+</sup>'),
        (r'$Ca^{2+}', 'Ca<sup>2+</sup>'),
        (r'$Ca^{2+}$', 'Ca<sup>2+</sup>'),
        (r'$H_2O_2$', 'H<sub>2</sub>O<sub>2</sub>'),
        (r'$O_2^{\bullet-}$', 'O<sub>2</sub><sup>•-</sup>'),
        (r'\text{', ''),  # Clean up any leftover LaTeX \text
        (r'}', '')        # Clean up any leftover braces from \text{...}
    ]
    
    # Apply specific LaTeX replacements
    for pattern, replacement in replacements:
        content = content.replace(pattern, replacement)
        
    return content

for file_path in FILES_TO_CLEAN:
    if not os.path.exists(file_path):
        print(f"[WARN] File not found: {file_path}")
        continue
        
    print(f"[CLEANING] File: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        original = f.read()
        
    cleaned = clean_content(original)
    
    if cleaned != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"[SUCCESS] Cleaned successfully.")
    else:
        print(f"[SKIP] No replacements needed.")
