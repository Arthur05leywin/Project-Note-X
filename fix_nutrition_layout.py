import os
import re

mod8 = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-08\module08_nutrition_vitamins.html"
mod8_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-08\module08_nutrition_vitamins_X.html"

def fix_nutrition(content):
    # ==========================
    # 1. Collagen Synthesis
    # ==========================
    t_c2 = r"""<div class="flow-box teal">\s*<span class="lbl">Step 2 — Hydroxylation \(ER\) — Requires Vitamin C \+ O₂ \+ Fe²⁺</span>\s*<strong>Prolyl hydroxylase:</strong> Proline → <strong>Hydroxyproline</strong> \(4-Hyp stabilises triple helix via H-bonds\)\s*<strong>Lysyl hydroxylase:</strong> Lysine → <strong>Hydroxylysine</strong> \(attachment point for O-linked glycosylation \+ cross-link formation\)\s*Both use α-ketoglutarate \+ O₂; require Fe²⁺ and <strong>Ascorbate \(Vit C\)</strong> to re-reduce Fe³⁺ → Fe²⁺\s*</div>"""
    r_c2 = """<div class="flow-box teal" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 2 — Hydroxylation (ER) — Requires Vitamin C + O₂ + Fe²⁺</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;"><strong>Prolyl hydroxylase:</strong> Proline → <strong>Hydroxyproline</strong> (4-Hyp stabilises triple helix via H-bonds)</li>
  <li style="margin-bottom:6px;"><strong>Lysyl hydroxylase:</strong> Lysine → <strong>Hydroxylysine</strong> (attachment point for O-linked glycosylation + cross-link formation)</li>
  <li>Both use α-ketoglutarate + O₂; require Fe²⁺ and <strong>Ascorbate (Vit C)</strong> to re-reduce Fe³⁺ → Fe²⁺</li>
</ul>
</div>"""
    content = re.sub(t_c2, r_c2, content, flags=re.DOTALL)

    t_c4 = r"""<div class="flow-box purple">\s*<span class="lbl">Step 4 — N/C Propeptide Cleavage \(extracellular\)</span>\s*Procollagen N-protease \+ C-protease cleave propeptides → <strong>Tropocollagen</strong> \(native collagen monomer\)\s*<span class="sub">Cleavage defect → Dermatosparaxis type Ehlers-Danlos \(EDS\)</span>\s*</div>"""
    r_c4 = """<div class="flow-box purple" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 4 — N/C Propeptide Cleavage (extracellular)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>Procollagen N-protease + C-protease cleave propeptides → <strong>Tropocollagen</strong> (native collagen monomer)</li>
  <li><span class="sub">Cleavage defect → Dermatosparaxis type Ehlers-Danlos (EDS)</span></li>
</ul>
</div>"""
    content = re.sub(t_c4, r_c4, content, flags=re.DOTALL)

    t_c5 = r"""<div class="flow-box rose">\s*<span class="lbl">Step 5 — Cross-linking by Lysyl Oxidase \(extracellular\) — requires Copper</span>\s*Lysyl oxidase oxidises Lys/HydroxyLys → Allysine → forms covalent cross-links between adjacent tropocollagen molecules → <strong>mature collagen fibril</strong> \(very high tensile strength\)\s*<span class="sub">Copper deficiency → defective cross-linking → weak connective tissue \(seen in Menkes disease\)</span>\s*</div>"""
    r_c5 = """<div class="flow-box" style="padding: 16px; text-align: left; background: var(--rose); color: #ffffff; border: 1px solid var(--rose); border-radius: 8px;">
<span class="lbl" style="display:block; margin-bottom: 8px; color: #ffffff; font-weight: 700;">Step 5 — Cross-linking by Lysyl Oxidase (extracellular) — requires Copper</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">Lysyl oxidase oxidises Lys/HydroxyLys → Allysine → forms covalent cross-links between adjacent tropocollagen molecules → <strong>mature collagen fibril</strong> (very high tensile strength)</li>
  <li><span style="font-weight:600;">Copper deficiency</span> → defective cross-linking → weak connective tissue (seen in Menkes disease)</li>
</ul>
</div>"""
    content = re.sub(t_c5, r_c5, content, flags=re.DOTALL)


    # ==========================
    # 2. SAM Cycle
    # ==========================
    t_s1 = r"""<div class="flow-box gold">\s*<span class="lbl">Methionine Activation \(ATP-dependent\)</span>\s*Methionine \+ ATP → <strong>S-Adenosylmethionine \(SAM\)</strong> \+ PPi \+ Pi\s*<span class="sub">Catalysed by Methionine adenosyltransferase\. SAM = universal methyl donor</span>\s*</div>"""
    r_s1 = """<div class="flow-box gold" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Methionine Activation (ATP-dependent)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>Methionine + ATP → <strong>S-Adenosylmethionine (SAM)</strong> + PPi + Pi</li>
  <li><span class="sub">Catalysed by Methionine adenosyltransferase. SAM = universal methyl donor</span></li>
</ul>
</div>"""
    content = re.sub(t_s1, r_s1, content, flags=re.DOTALL)

    t_s2 = r"""<div class="flow-box teal">\s*<span class="lbl">Methylation Reactions by SAM</span>\s*SAM → <strong>S-Adenosylhomocysteine \(SAH\)</strong> after donating methyl group\s*Examples: Norepinephrine → Epinephrine \(COMT\); Guanidinoacetate → Creatine; DNA CpG methylation \(epigenetics\); Phosphatidylethanolamine → Phosphatidylcholine; Histamine → N-methylhistamine\s*</div>"""
    r_s2 = """<div class="flow-box teal" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Methylation Reactions by SAM</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">SAM → <strong>S-Adenosylhomocysteine (SAH)</strong> after donating methyl group</li>
  <li><strong>Examples:</strong> Norepinephrine → Epinephrine (COMT); Guanidinoacetate → Creatine; DNA CpG methylation (epigenetics); Phosphatidylethanolamine → Phosphatidylcholine; Histamine → N-methylhistamine</li>
</ul>
</div>"""
    content = re.sub(t_s2, r_s2, content, flags=re.DOTALL)

    t_s3 = r"""<div class="flow-box rose">\s*<span class="lbl">Homocysteine Fate</span>\s*<strong>Route 1 \(Remethylation\):</strong> Homocysteine \+ Methyl-THF → Methionine \(needs B12 \+ Methionine synthase\) — salvage pathway\s*<strong>Route 2 \(Transsulphuration\):</strong> Homocysteine \+ Serine → Cystathionine → Cysteine \(needs PLP/B6\)\s*<span class="sub">Cysteine → Glutathione \(GSH\)\. Taurine\. Sulphate\.</span>\s*</div>"""
    r_s3 = """<div class="flow-box" style="padding: 16px; text-align: left; background: var(--rose); color: #ffffff; border: 1px solid var(--rose); border-radius: 8px;">
<span class="lbl" style="display:block; margin-bottom: 8px; color: #ffffff; font-weight: 700;">Homocysteine Fate</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;"><strong>Route 1 (Remethylation):</strong> Homocysteine + Methyl-THF → Methionine (needs B12 + Methionine synthase) — salvage pathway</li>
  <li style="margin-bottom:6px;"><strong>Route 2 (Transsulphuration):</strong> Homocysteine + Serine → Cystathionine → Cysteine (needs PLP/B6)</li>
  <li><span style="font-weight:600;">Cysteine</span> → Glutathione (GSH). Taurine. Sulphate.</li>
</ul>
</div>"""
    content = re.sub(t_s3, r_s3, content, flags=re.DOTALL)


    # ==========================
    # 3. Iron Absorption
    # ==========================
    t_i1 = r"""<div class="flow-box amber">\s*<span class="lbl">Dietary Sources &amp; Forms</span>\s*<strong>Haem iron</strong> \(myoglobin, Hb from meat\): absorbed directly as intact haem via HCP1 receptor → ~25% absorption, not affected by dietary factors\s*<strong>Non-haem iron</strong> \(ferric Fe³⁺ from plants, cereals\): must be reduced to Fe²⁺ first → absorbed by DMT-1 \(divalent metal transporter\) → lower bioavailability \(~5%\)\s*<span class="sub">Vitamin C \(ascorbate\) reduces Fe³⁺→Fe²⁺ → ↑ non-haem absorption 3-fold</span>\s*</div>"""
    r_i1 = """<div class="flow-box amber" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Dietary Sources &amp; Forms</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;"><strong>Haem iron</strong> (myoglobin, Hb from meat): absorbed directly as intact haem via HCP1 receptor → ~25% absorption, not affected by dietary factors</li>
  <li style="margin-bottom:6px;"><strong>Non-haem iron</strong> (ferric Fe³⁺ from plants, cereals): must be reduced to Fe²⁺ first → absorbed by DMT-1 (divalent metal transporter) → lower bioavailability (~5%)</li>
  <li><span class="sub">Vitamin C (ascorbate) reduces Fe³⁺→Fe²⁺ → ↑ non-haem absorption 3-fold</span></li>
</ul>
</div>"""
    content = re.sub(t_i1, r_i1, content, flags=re.DOTALL)

    t_i2 = r"""<div class="flow-box gold">\s*<span class="lbl">Export from Enterocyte — Basolateral Side</span>\s*Fe²⁺ exported by <strong>Ferroportin</strong> \(only iron exporter in body\)\s*→ Oxidised to Fe³⁺ by <strong>Hephaestin</strong> \(ferroxidase, copper-dependent\)\s*→ Binds <strong>Apotransferrin</strong> → <strong>Transferrin</strong> \(carries 2 Fe³⁺ atoms, β₁-globulin\)\s*</div>"""
    r_i2 = """<div class="flow-box gold" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Export from Enterocyte — Basolateral Side</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>Fe²⁺ exported by <strong>Ferroportin</strong> (only iron exporter in body)</li>
  <li>Oxidised to Fe³⁺ by <strong>Hephaestin</strong> (ferroxidase, copper-dependent)</li>
  <li>Binds <strong>Apotransferrin</strong> → <strong>Transferrin</strong> (carries 2 Fe³⁺ atoms, β₁-globulin)</li>
</ul>
</div>"""
    content = re.sub(t_i2, r_i2, content, flags=re.DOTALL)

    t_i3 = r"""<div class="flow-box accent">\s*<span class="lbl">Cellular Uptake — Receptor-mediated Endocytosis</span>\s*Transferrin-TfR complex → endosome \(acidified\) → Fe³⁺ released → reduced to Fe²⁺ by Steap3 → exits endosome via DMT-1 → used for haem/Fe-S cluster synthesis or stored as Ferritin\s*</div>"""
    r_i3 = """<div class="flow-box accent" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Cellular Uptake — Receptor-mediated Endocytosis</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">Transferrin-TfR complex → endosome (acidified)</li>
  <li style="margin-bottom:6px;">Fe³⁺ released → reduced to Fe²⁺ by Steap3</li>
  <li>Exits endosome via DMT-1 → used for haem/Fe-S cluster synthesis or stored as Ferritin</li>
</ul>
</div>"""
    content = re.sub(t_i3, r_i3, content, flags=re.DOTALL)

    t_i4 = r"""<div class="flow-box teal">\s*<span class="lbl">Iron Storage — Ferritin &amp; Haemosiderin</span>\s*<strong>Ferritin:</strong> 24 subunits, stores up to 4500 Fe atoms as Fe\(OH\)₃ core\. Serum ferritin = best indicator of iron stores \(1 ng/mL ≈ 8 mg stored iron\)\s*<strong>Haemosiderin:</strong> Degraded ferritin, insoluble, stains with Perl's Prussian blue\. Seen in iron overload\.\s*</div>"""
    r_i4 = """<div class="flow-box teal" style="padding: 16px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Iron Storage — Ferritin &amp; Haemosiderin</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;"><strong>Ferritin:</strong> 24 subunits, stores up to 4500 Fe atoms as Fe(OH)₃ core. Serum ferritin = best indicator of iron stores (1 ng/mL ≈ 8 mg stored iron)</li>
  <li><strong>Haemosiderin:</strong> Degraded ferritin, insoluble, stains with Perl's Prussian blue. Seen in iron overload.</li>
</ul>
</div>"""
    content = re.sub(t_i4, r_i4, content, flags=re.DOTALL)

    # ==========================
    # 4. Mineral Table
    # ==========================
    
    t_m1 = r"""<tr><td>Zinc \(Zn\)</td><td>Cofactor for &gt;300 enzymes \(carbonic anhydrase, carboxypeptidase, alcohol dehydrogenase, DNA polymerase, superoxide dismutase\)\. Zinc finger proteins \(transcription factors\)\. Wound healing\. Insulin storage \(Zn-insulin hexamer\)\.</td><td>Growth retardation, Acrodermatitis enteropathica \(perioral/perianal rash\), hypogonadism, poor wound healing, impaired taste/smell \(hypogeusia/anosmia\), immune dysfunction\. Night blindness \(↓ retinol-binding protein synthesis\)</td><td>Rare — nausea, copper deficiency \(compete for absorption\)</td><td>2022 \(Wilson's\)</td></tr>"""
    r_m1 = """<tr>
  <td><strong>Zinc (Zn)</strong></td>
  <td>
    <ul style="margin:0; padding-left:16px; font-size:13px; line-height:1.6;">
      <li style="margin-bottom:4px;">Cofactor for >300 enzymes (carbonic anhydrase, alcohol dehydrogenase, DNA polymerase)</li>
      <li style="margin-bottom:4px;">Zinc finger proteins (transcription)</li>
      <li style="margin-bottom:4px;">Wound healing</li>
      <li>Insulin storage (Zn-hexamer)</li>
    </ul>
  </td>
  <td>
    <ul style="margin:0; padding-left:16px; font-size:13px; line-height:1.6;">
      <li style="margin-bottom:4px;"><strong>Acrodermatitis enteropathica</strong> (perioral/perianal rash)</li>
      <li style="margin-bottom:4px;">Growth retardation, hypogonadism</li>
      <li style="margin-bottom:4px;">Poor wound healing</li>
      <li style="margin-bottom:4px;">Impaired taste/smell (hypogeusia/anosmia)</li>
      <li>Night blindness (↓ RBP synthesis)</li>
    </ul>
  </td>
  <td style="font-size:13px; line-height:1.6;">Rare — nausea, copper deficiency</td>
  <td></td>
</tr>"""
    content = re.sub(t_m1, r_m1, content)
    
    t_m2 = r"""<tr><td>Copper \(Cu\)</td><td>Ceruloplasmin \(ferroxidase — Fe²⁺→Fe³⁺\), Cytochrome c oxidase \(Complex IV of ETC\), Superoxide dismutase \(Cu-Zn SOD\), Dopamine β-hydroxylase, Lysyl oxidase \(collagen cross-linking\), Tyrosinase \(melanin\)</td><td>Menkes disease \(X-linked\): kinky hair \(pili torti\), neurodegeneration, connective tissue defects, ↓ ceruloplasmin\. Acquired: anaemia, bone disease</td><td><strong>Wilson's disease:</strong> AR, ATP7B gene \(copper transport ATPase\) → copper accumulates in liver \(cirrhosis\), brain \(neuropsychiatric\), eye \(Kayser-Fleischer rings in cornea\), kidney, joints\. ↑ urinary copper, ↓ ceruloplasmin</td><td>2022, 2025</td></tr>"""
    r_m2 = """<tr>
  <td><strong>Copper (Cu)</strong></td>
  <td>
    <ul style="margin:0; padding-left:16px; font-size:13px; line-height:1.6;">
      <li style="margin-bottom:4px;">Ceruloplasmin (ferroxidase — Fe²⁺→Fe³⁺)</li>
      <li style="margin-bottom:4px;">Cytochrome c oxidase (Complex IV)</li>
      <li style="margin-bottom:4px;">Lysyl oxidase (collagen cross-linking)</li>
      <li>Tyrosinase (melanin)</li>
    </ul>
  </td>
  <td>
    <ul style="margin:0; padding-left:16px; font-size:13px; line-height:1.6;">
      <li style="margin-bottom:4px;"><strong>Menkes disease</strong> (X-linked): kinky hair (pili torti), neurodegeneration, connective tissue defects, ↓ ceruloplasmin</li>
      <li>Acquired: anaemia, bone disease</li>
    </ul>
  </td>
  <td>
    <div style="font-size:13px; line-height:1.6;">
      <strong>Wilson's disease:</strong> AR, ATP7B gene (copper transport ATPase) → copper accumulates in liver (cirrhosis), brain (neuropsychiatric), eye (Kayser-Fleischer rings in cornea), joints. ↑ urinary copper, ↓ ceruloplasmin
    </div>
  </td>
  <td>2022, 2025</td>
</tr>"""
    content = re.sub(t_m2, r_m2, content)
    
    t_m3 = r"""<tr><td>Selenium \(Se\)</td><td>Component of <strong>Glutathione peroxidase</strong> \(GPx\) — reduces H₂O₂ and lipid peroxides using GSH\. Selenocysteine = 21st amino acid \(encoded by UGA stop codon with SECIS element\)\. Iodothyronine deiodinase \(T4→T3 conversion\)\. Thioredoxin reductase\.</td><td>Keshan disease \(cardiomyopathy, China\)\. Kashin-Beck disease \(osteoarthropathy\)\. Impaired antioxidant defence\. ↑ cancer risk</td><td>Selenosis: garlic odour, hair/nail loss, nausea, neurological symptoms</td><td>2014 \(antioxidant enzymes\)</td></tr>"""
    r_m3 = """<tr>
  <td><strong>Selenium (Se)</strong></td>
  <td>
    <ul style="margin:0; padding-left:16px; font-size:13px; line-height:1.6;">
      <li style="margin-bottom:4px;">Component of <strong>Glutathione peroxidase</strong> (GPx) — reduces H₂O₂ using GSH</li>
      <li style="margin-bottom:4px;">Selenocysteine = 21st amino acid</li>
      <li>Iodothyronine deiodinase (T4→T3)</li>
    </ul>
  </td>
  <td>
    <ul style="margin:0; padding-left:16px; font-size:13px; line-height:1.6;">
      <li style="margin-bottom:4px;"><strong>Keshan disease</strong> (cardiomyopathy)</li>
      <li style="margin-bottom:4px;"><strong>Kashin-Beck disease</strong> (osteoarthropathy)</li>
      <li>Impaired antioxidant defence</li>
    </ul>
  </td>
  <td style="font-size:13px; line-height:1.6;">Selenosis: garlic odour, hair/nail loss</td>
  <td>2014</td>
</tr>"""
    content = re.sub(t_m3, r_m3, content)

    return content

for fp in [mod8, mod8_x]:
    with open(fp, 'r', encoding='utf-8') as f: cont = f.read()
    new_cont = fix_nutrition(cont)
    if new_cont != cont:
        with open(fp, 'w', encoding='utf-8') as f: f.write(new_cont)
        print("Updated " + fp)
