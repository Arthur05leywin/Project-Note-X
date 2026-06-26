import os
import re

file_paths = [
    r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-07\module07_biological_oxidation.html",
    r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-07\module07_biological_oxidation_X.html"
]

def fix_cyanide(content):
    target = r"""<div class="clinical-box"\s*style="margin-top:\s*8px">\s*<div class="cbox-title">Cyanide Poisoning — Mechanism</div>\s*<p>.*?CN⁻ binds tightly.*?Thiosulphate.*?thiocyanate\).*?</p>\s*</div>"""
    
    replacement = """<div class="clinical-box" style="margin-top: 8px">
<div class="cbox-title">Cyanide Poisoning — Mechanism</div>
<div class="flowchart" style="margin:0; padding:0; background:transparent; border:none;">
<div class="flow-v" style="align-items:flex-start;">
<div class="flow-box accent" style="text-align:left; padding:12px; margin-bottom:12px;">
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;">CN⁻ binds tightly to the Fe³⁺ of cytochrome a₃ (Complex IV)</li>
  <li style="margin-bottom: 6px;">Prevents electron transfer to O₂</li>
  <li style="margin-bottom: 6px;">ETC stops → ATP production stops</li>
  <li>Cell death. <strong>Tissues that die fastest:</strong> brain and heart (highest O₂ demand).</li>
</ul>
</div>
<div style="font-size:13px; line-height:1.6; padding-left:12px;"><strong>Treatment:</strong> Hydroxocobalamin (binds CN⁻) or Nitrites (generate metHb that competes with CN⁻) + Thiosulphate (converts CN⁻ → thiocyanate).</div>
</div>
</div>
</div>"""
    content = re.sub(target, replacement, content, flags=re.DOTALL)
    return content

for fp in file_paths:
    with open(fp, 'r', encoding='utf-8') as f:
        cont = f.read()
    orig = cont
    cont = fix_cyanide(cont)
    if orig != cont:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(cont)
        print(f"Fixed Cyanide Poisoning in {fp}")

file_paths_6 = [
    r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-06\module06_molecular_biology.html",
    r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-06\module06_molecular_biology_X.html"
]

def fix_genetics(content):
    # Sickle Cell
    target_sickle = r"""<div class="clinical-box">\s*<div class="cbox-title">\s*Sickle Cell — Point Mutation \(Missense\)\s*</div>\s*<p>\s*GAG → GTG.*?HbS\s*polymerisation when deoxygenated\.\s*</p>\s*<p style="margin-top:\s*4px">\s*<strong>EQ.*?molecular level.*?1949\)\.\s*</p>\s*</div>"""
    
    replace_sickle = """<div class="clinical-box">
<div class="cbox-title">Sickle Cell — Point Mutation (Missense)</div>
<ul style="margin: 0 0 12px 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;"><strong>Mutation:</strong> GAG → GTG (codon 6, β-globin).</li>
  <li style="margin-bottom: 6px;"><strong>Type:</strong> A→T transversion at 2nd position of codon.</li>
  <li style="margin-bottom: 6px;"><strong>Effect:</strong> Glu (charged) → Val (hydrophobic).</li>
  <li><strong>Result:</strong> HbS polymerisation when deoxygenated.</li>
</ul>
<p style="margin-top: 4px; font-size: 13px; line-height: 1.6;">
<strong>EQ: "Sickle cell anaemia is a molecular disease [2023]"</strong>
— first disease understood at molecular level (Linus Pauling, 1949).
</p>
</div>"""
    content = re.sub(target_sickle, replace_sickle, content, flags=re.DOTALL)

    # Frameshift
    target_frame = r"""<div class="clinical-box">\s*<div class="cbox-title">Frameshift vs Point Mutation Impact</div>\s*<p>\s*Point mutation.*?more severe\s*than point mutation\.\s*</p>\s*</div>"""
    
    replace_frame = """<div class="clinical-box">
<div class="cbox-title">Frameshift vs Point Mutation Impact</div>
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 10px;"><strong>Point mutation:</strong> Changes 1 amino acid (may retain some function — e.g., missense).</li>
  <li><strong>Frameshift:</strong> Disrupts ALL downstream amino acids → completely non-functional truncated protein → usually more severe than point mutation.</li>
</ul>
</div>"""
    content = re.sub(target_frame, replace_frame, content, flags=re.DOTALL)
    
    # Philadelphia Chromosome
    target_philly = r"""<div class="keypoint">\s*<strong>Philadelphia chromosome \[PYQ 2023\]:</strong> t\(9;22\)\s*translocation → BCR-ABL fusion gene → constitutively active tyrosine\s*kinase → CML\. Imatinib \(Gleevec\) specifically inhibits BCR-ABL kinase\.\s*Example of chromosomal translocation → oncogene activation\.\s*</div>"""
    
    replace_philly = """<div class="keypoint" style="display: flex; flex-direction: column; gap: 8px;">
  <div><strong>Philadelphia chromosome <span class="badge badge-pyq">PYQ 2023</span>:</strong></div>
  <ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
    <li style="margin-bottom: 6px;">t(9;22) translocation</li>
    <li style="margin-bottom: 6px;">BCR-ABL fusion gene</li>
    <li style="margin-bottom: 6px;">Constitutively active tyrosine kinase</li>
    <li style="margin-bottom: 6px;"><strong>Result:</strong> CML. Example of chromosomal translocation → oncogene activation.</li>
    <li><strong>Treatment:</strong> Imatinib (Gleevec) specifically inhibits BCR-ABL kinase.</li>
  </ul>
</div>"""
    content = re.sub(target_philly, replace_philly, content, flags=re.DOTALL)
    
    return content

for fp in file_paths_6:
    with open(fp, 'r', encoding='utf-8') as f:
        cont = f.read()
    orig = cont
    cont = fix_genetics(cont)
    if orig != cont:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(cont)
        print(f"Fixed Genetics Flowcharts in {fp}")

print("Done flowcharts.")
