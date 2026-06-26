import os
import re

def fix_signal(content):
    # 1. cAMP Second Messenger System
    # Step 1
    content = content.replace(
        'Hormone (glucagon/adrenaline) binds 7-TM GPCR → conformational change → GDP on Gα replaced by GTP → Gα-GTP dissociates from Gβγ',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li>Hormone (glucagon/adrenaline) binds 7-TM GPCR</li><li>Conformational change occurs</li><li>GDP on Gα replaced by GTP</li><li>Gα-GTP dissociates from Gβγ</li></ul>'
    )
    # Step 2
    content = content.replace(
        'Gαs + Adenylyl Cyclase → ATP → <strong>cAMP</strong> (second messenger) + PPi<br/>\n          Gαi inhibits adenylyl cyclase → ↓ cAMP (e.g., somatostatin, muscarinic M2)',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li><strong>Gαs:</strong> Activates Adenylyl Cyclase → converts ATP to <strong>cAMP</strong> (second messenger)</li><li><strong>Gαi:</strong> Inhibits adenylyl cyclase → ↓ cAMP (e.g., somatostatin, muscarinic M2)</li></ul>'
    )
    # Step 3
    content = content.replace(
        'cAMP binds regulatory subunits of PKA → releases catalytic subunits → active PKA phosphorylates target proteins (Ser/Thr):<br/>\n          Glycogen phosphorylase kinase (↑) → glycogenolysis ↑<br/>\n          Glycogen synthase (↓) → glycogenesis ↓<br/>\n          Lipase (HSL) (↑) → lipolysis ↑<br/>\n          CREB (nuclear) → gene transcription',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li>cAMP binds regulatory subunits of PKA → releases catalytic subunits</li><li>Active PKA phosphorylates target proteins (Ser/Thr):</li><ul><li>Glycogen phosphorylase kinase (↑) → glycogenolysis ↑</li><li>Glycogen synthase (↓) → glycogenesis ↓</li><li>Hormone-sensitive lipase (HSL) (↑) → lipolysis ↑</li><li>CREB (nuclear) → gene transcription</li></ul></ul>'
    )
    # Termination
    content = content.replace(
        'Gα GTPase activity: GTP → GDP → Gα reassociates with Gβγ → GPCR inactive<br/>\n          Phosphodiesterase (PDE): cAMP → 5\'-AMP (theophylline, caffeine = PDE inhibitors → ↑ cAMP)',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li><strong>Gα GTPase activity:</strong> GTP → GDP → Gα reassociates with Gβγ → GPCR inactive</li><li><strong>Phosphodiesterase (PDE):</strong> cAMP → 5\'-AMP</li><li><em>Note:</em> Theophylline, caffeine are PDE inhibitors → ↑ cAMP</li></ul>'
    )

    # 2. Cholera Toxin
    old_cholera = 'Cholera toxin (CT) ADP-ribosylates Gαs at Arg201 → prevents GTP hydrolysis → Gαs permanently active → adenylyl cyclase permanently on → cAMP ↑↑↑ → PKA → CFTR opens → Cl⁻, HCO₃⁻ secretion → massive water secretion → "rice water" diarrhoea. Pertussis toxin ADP-ribosylates Gαi → prevents Gi activation → no inhibition of cAMP → ↑ cAMP in airway → whooping cough.'
    new_cholera = """<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li><strong>Cholera Toxin (CT):</strong> ADP-ribosylates Gαs (Arg201) → prevents GTP hydrolysis.
    <ul>
      <li>Gαs remains permanently active → Adenylyl cyclase permanently ON.</li>
      <li>cAMP ↑↑↑ → PKA activates → CFTR channel opens.</li>
      <li>Massive Cl⁻, HCO₃⁻ and water secretion into gut → "rice water" diarrhoea.</li>
    </ul>
  </li>
  <li style="margin-top:8px;"><strong>Pertussis Toxin:</strong> ADP-ribosylates Gαi → prevents Gi activation.
    <ul>
      <li>No inhibition of adenylyl cyclase → ↑ cAMP in airway → whooping cough.</li>
    </ul>
  </li>
</ul>"""
    content = content.replace(old_cholera, new_cholera)

    # 3. PIP2 IP3/DAG Pathway
    # Find the flow-h block
    pip2_block = r"""<div class="flow-h">
<div class="flow-box rose"(.*?)>
<span class="lbl">IP₃ \(Inositol trisphosphate\)</span>
            Water-soluble → ER receptor → Ca²⁺ release from ER → ↑ cytosolic Ca²⁺<br/>
            Ca²⁺ \+ Calmodulin → CaM-kinase → enzyme activation \(myosin light chain kinase, phosphorylase kinase\)
          </div>
<div class="h-arrow">\+</div>
<div class="flow-box teal"(.*?)>
<span class="lbl">DAG \(Diacylglycerol\)</span>
            Lipid-soluble → stays in membrane → activates <strong>Protein Kinase C \(PKC\)</strong> \(also needs Ca²⁺\)<br/>
            PKC → Ser/Thr phosphorylation of target proteins
          </div>
</div>"""

    new_pip2 = """<div class="flow-v">
<div class="flow-box rose" style="text-align:left; color:#ffffff;">
<span class="lbl" style="text-align:center; display:block;">IP₃ (Inositol trisphosphate)</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>Water-soluble → diffuses to ER receptor</li>
  <li>Ca²⁺ release from ER → ↑ cytosolic Ca²⁺</li>
  <li>Ca²⁺ + Calmodulin → CaM-kinase activation</li>
  <li>Activates myosin light chain kinase, phosphorylase kinase</li>
</ul>
</div>
<div class="flow-step-label" style="text-align:center; font-size:24px; font-weight:bold;">+</div>
<div class="flow-box teal" style="text-align:left; color:#ffffff;">
<span class="lbl" style="text-align:center; display:block;">DAG (Diacylglycerol)</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>Lipid-soluble → remains in cell membrane</li>
  <li>Activates <strong>Protein Kinase C (PKC)</strong> (along with Ca²⁺)</li>
  <li>PKC → Ser/Thr phosphorylation of target proteins</li>
</ul>
</div>
</div>"""
    content = re.sub(pip2_block, new_pip2, content, flags=re.DOTALL)


    # 4. RTK Pathway
    # Step 1
    content = content.replace(
        'Insulin (or EGF, PDGF, IGF-1) binds extracellular domain of RTK → receptor dimerises → <strong>autophosphorylation</strong> of Tyr residues on cytoplasmic domain',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li>Insulin (or EGF, PDGF, IGF-1) binds extracellular domain of RTK</li><li>Receptor dimerises</li><li><strong>Autophosphorylation</strong> of Tyrosine residues on cytoplasmic domain</li></ul>'
    )
    # Step 2
    step2_rtk_old = r"Insulin receptor: IRS-1 docked → PI3K recruited → PIP₂ → <strong>PIP₃</strong> → PDK1 → <strong>AKT \(PKB\)</strong> → glucose uptake \(GLUT4\), glycogen synthesis, protein synthesis, anti-apoptosis<br/>\s*Grb2-SOS → <strong>RAS activated</strong> → RAF → MEK → ERK → cell proliferation"
    step2_rtk_new = """<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li><strong>Metabolic Pathway:</strong> IRS-1 docked → PI3K recruited → PIP₂ converted to <strong>PIP₃</strong> → PDK1 → <strong>AKT (PKB)</strong>.
    <ul><li>Results in: glucose uptake (GLUT4), glycogen/protein synthesis, anti-apoptosis.</li></ul>
  </li>
  <li style="margin-top:8px;"><strong>Mitogenic Pathway:</strong> Grb2-SOS → <strong>RAS activated</strong> → RAF → MEK → ERK.
    <ul><li>Results in: cell proliferation and gene expression.</li></ul>
  </li>
</ul>"""
    content = re.sub(step2_rtk_old, step2_rtk_new, content)
    
    # Termination
    content = content.replace(
        'Protein tyrosine phosphatases (PTP1B) → remove Tyr phosphorylation. PTEN → removes PIP₃ → opposes PI3K',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li><strong>Protein tyrosine phosphatases (PTP1B):</strong> remove Tyr phosphorylation</li><li><strong>PTEN:</strong> dephosphorylates PIP₃ → PIP₂ (opposes PI3K action)</li></ul>'
    )
    
    # Also fix any remaining missing white text colors in these boxes
    content = content.replace('<div class="flow-box teal">', '<div class="flow-box teal" style="color: #ffffff;">')

    return content

mod10 = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-10\module10_immunochemistry_oncogenesis.html"
mod10_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-10\module10_immunochemistry_oncogenesis_X.html"

for fn in [mod10, mod10_x]:
    with open(fn, 'r', encoding='utf-8') as f:
        cont = f.read()
    new_cont = fix_signal(cont)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(new_cont)
    print("Updated", fn)

