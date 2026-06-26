import os
import re

def fix_module10(content):
    # 1. Immunoglobulin image
    svg_block = r'<div class="ig-diagram">\s*<svg.*?</svg>\s*</div>'
    img_replacement = r'''<div class="ig-diagram" style="text-align:center;">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Antibody.svg/1024px-Antibody.svg.png" style="width: 100%; max-width: 450px; display: block; margin: 0 auto; background: #ffffff; padding: 12px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
<div style="font-size:12px; color:var(--text2); margin-top:8px;">Basic IgG Structure. Source: Wikimedia Commons</div>
</div>'''
    
    # We will just find the <div class="ig-diagram"> ... </div> and replace it
    # Because re.sub with DOTALL can be dangerous if there are multiple ig-diagrams,
    # let's just find the start and end of it.
    start_idx = content.find('<div class="ig-diagram">')
    if start_idx != -1:
        end_idx = content.find('</div>', content.find('</svg>', start_idx)) + 6
        content = content[:start_idx] + img_replacement + content[end_idx:]

    # 2. Type I Hypersensitivity
    # We need to change the flow-boxes to have <ul> and white text.
    content = content.replace('<div class="flow-box accent">', '<div class="flow-box accent" style="color: #ffffff;">')
    content = content.replace('<div class="flow-box rose">', '<div class="flow-box rose" style="color: #ffffff;">')
    content = content.replace('<div class="flow-box teal">', '<div class="flow-box teal" style="color: #ffffff;">')
    # Replace paragraphs with <ul> inside Sensitisation Phase
    text1 = r"""Allergen → APCs → Th2 cells → IL-4, IL-13 → B cells class-switch to IgE production → IgE binds FcεRI on mast cells/basophils \(sensitisation, no symptoms\)"""
    text1_ul = """<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>Allergen → APCs → Th2 cells → IL-4, IL-13</li>
  <li>B cells class-switch to IgE production</li>
  <li>IgE binds high-affinity FcεRI on mast cells/basophils (sensitisation, no symptoms yet)</li>
</ul>"""
    content = re.sub(text1, text1_ul, content)

    text2 = r"""Allergen cross-links IgE on mast cells → FcεRI clustering → <strong>Degranulation</strong> \(within seconds-minutes\):<br/>\s*Preformed mediators: <strong>Histamine</strong> \(vasodilation, pruritus, bronchoconstriction\), <strong>Tryptase</strong> \(mast cell marker\)<br/>\s*Newly synthesised: <strong>Leukotrienes</strong> C4, D4, E4 \(potent bronchoconstrictors — "slow-reacting substances"\), <strong>PGD₂</strong>, <strong>PAF</strong><br/>\s*Cytokines \(late phase\): IL-4, IL-5, TNF-α → eosinophil recruitment \(late-phase reaction, 6–12 hours\)"""
    text2_ul = """<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">Allergen cross-links IgE on mast cells → FcεRI clustering → <strong>Degranulation</strong> (within seconds-minutes)</li>
  <li style="margin-bottom:6px;"><strong>Preformed mediators:</strong> Histamine (vasodilation, pruritus, bronchoconstriction), Tryptase (mast cell marker)</li>
  <li style="margin-bottom:6px;"><strong>Newly synthesised:</strong> Leukotrienes C4, D4, E4 (potent bronchoconstrictors), PGD₂, PAF</li>
  <li><strong>Cytokines (late phase):</strong> IL-4, IL-5, TNF-α → eosinophil recruitment (6–12 hours)</li>
</ul>"""
    content = re.sub(text2, text2_ul, content)
    
    text3 = r"""↓ BP \(vasodilation \+ ↑ permeability → hypovolaemia\) \+ Bronchospasm \+ Urticaria\. Treatment: <strong>Epinephrine</strong> \(adrenaline\) 1:1000 IM — reverses all components"""
    text3_ul = """<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li><strong>Cardiovascular:</strong> ↓ BP (vasodilation + ↑ permeability → hypovolaemia)</li>
  <li><strong>Respiratory:</strong> Bronchospasm, wheezing</li>
  <li><strong>Skin:</strong> Urticaria (hives), angioedema</li>
  <li><strong>Treatment:</strong> <strong>Epinephrine</strong> (adrenaline) 1:1000 IM — rapidly reverses all components</li>
</ul>"""
    content = content.replace("↓ BP (vasodilation + ↑ permeability → hypovolaemia) + Bronchospasm + Urticaria. Treatment: <strong>Epinephrine</strong> (adrenaline) 1:1000 IM — reverses all components", text3_ul)

    # 3. Complement System
    # Make text white
    content = content.replace('<div class="flow-box accent" style="text-align:center;">', '<div class="flow-box accent" style="text-align:center; color:#ffffff;">')
    content = content.replace('<div class="flow-box gold" style="text-align:center;">', '<div class="flow-box gold" style="text-align:center; color:#ffffff;">')
    content = content.replace('<div class="flow-box rose" style="text-align:center;">', '<div class="flow-box rose" style="text-align:center; color:#ffffff;">')
    
    # Wait, the screenshot 1 has "Three Activation Pathways → Common Terminal Pathway"
    # the C3 cleavage box is teal, C5b is blue.
    content = content.replace('<div class="flow-box teal">', '<div class="flow-box teal" style="color: #ffffff;">')
    content = content.replace('<div class="flow-box blue">', '<div class="flow-box blue" style="color: #ffffff;">')

    return content

# Run for module 10
mod10 = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-10\module10_immunochemistry_oncogenesis.html"
mod10_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-10\module10_immunochemistry_oncogenesis_X.html"

for fn in [mod10, mod10_x]:
    with open(fn, 'r', encoding='utf-8') as f:
        cont = f.read()
    new_cont = fix_module10(cont)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(new_cont)
    print("Updated", fn)

def fix_module09_elisa(content):
    # We will replace the <ul class="checklist"> for ELISA types with detailed expanding boxes
    target = r"""<ul class="checklist">\s*<li><strong>Sandwich ELISA:</strong> Quantifies antigen between 2 antibodies \(most common\)</li>\s*<li><strong>Indirect ELISA:</strong> Detects antibodies in patient serum \(HIV screening — ELISA for anti-HIV antibodies\)</li>\s*<li><strong>Competitive ELISA:</strong> Antigen in sample competes with labelled antigen</li>\s*<li><strong>Capture ELISA:</strong> Variant of sandwich, for low-abundance antigens</li>\s*</ul>"""
    
    detailed_elisa = """
<div style="display:flex; flex-direction:column; gap:16px;">

  <div class="flow-box rose" style="color:#ffffff;">
    <span class="lbl">Indirect ELISA (Antibody Detection)</span>
    <ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
      <li><strong>Principle:</strong> Detects specific antibodies in patient serum (e.g. HIV screening).</li>
      <li><strong>Figure:</strong> <code>[Plate] — [Known Antigen] — [Patient Ab] — [Enzyme-linked Anti-human Ig]</code></li>
      <li><strong>Procedure:</strong> Coat plate with known antigen → Add patient serum (primary Ab binds) → Wash → Add enzyme-linked secondary Ab → Wash → Add substrate → Measure color.</li>
    </ul>
  </div>

  <div class="flow-box gold" style="color:#ffffff;">
    <span class="lbl">Sandwich ELISA (Antigen Detection)</span>
    <ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
      <li><strong>Principle:</strong> Detects specific antigen in sample by sandwiching it between two antibodies (most common).</li>
      <li><strong>Figure:</strong> <code>[Plate] — [Capture Ab] — [Sample Antigen] — [Enzyme-linked Detect Ab]</code></li>
      <li><strong>Procedure:</strong> Coat plate with Capture Ab → Add sample (Antigen binds) → Wash → Add enzyme-linked Detection Ab → Wash → Add substrate → Measure color (proportional to Ag).</li>
    </ul>
  </div>

  <div class="flow-box teal" style="color:#ffffff;">
    <span class="lbl">Competitive ELISA (Quantification)</span>
    <ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
      <li><strong>Principle:</strong> Antigen in sample competes with reference labelled antigen for limited antibody binding sites.</li>
      <li><strong>Figure:</strong> <code>[Plate] — [Capture Ab] — [Unlabeled Sample Ag vs Labeled Reference Ag]</code></li>
      <li><strong>Procedure:</strong> Mix sample Ag with a known amount of enzyme-labelled Ag → Add to plate coated with Ab → Both compete to bind → Wash → Add substrate.</li>
      <li><strong>Note:</strong> Signal intensity is <em>inversely</em> proportional to the amount of antigen in the sample!</li>
    </ul>
  </div>

</div>
"""
    return re.sub(target, detailed_elisa, content)

mod9 = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-09\module09_clinical_biochemistry.html"
mod9_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-09\module09_clinical_biochemistry_X.html"

for fn in [mod9, mod9_x]:
    with open(fn, 'r', encoding='utf-8') as f:
        cont = f.read()
    new_cont = fix_module09_elisa(cont)
    if new_cont != cont:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(new_cont)
        print("Updated", fn)

