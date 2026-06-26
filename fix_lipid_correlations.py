import os
import re

file_path = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-03\lipid_metabolism_notes.html"
file_path_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-03\lipid_metabolism_notes_X.html"

def convert_clinical(content):
    # We are looking for paragraphs or list items with "Statin therapy:", "MCAD deficiency:", etc.
    # We can just manually replace them with flowcharts.
    # This is a bit specific, so let's do targeted replacements.
    
    replacements = {
        r"<strong>Statin therapy:</strong>.*?(\r?\n)*.*?Inhibit HMG-CoA reductase → ↓ cholesterol synthesis → upregulate hepatic LDL receptors → ↑ LDL clearance\. Side effect: myopathy \(↑ CK-MM\)\. Monitor liver enzymes\.": 
"""<strong>Statin therapy:</strong>
  <div class="flowchart-container" style="margin-top: 10px; margin-bottom: 14px;">
    <div class="flow-box muted" style="text-align: left; width: 100%; box-sizing: border-box; padding: 12px; margin: 0 auto; display: block;">
      Inhibit HMG-CoA reductase
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      ↓ cholesterol synthesis
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      upregulate hepatic LDL receptors
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      ↑ LDL clearance
    </div>
    <div style="font-size: 0.85em; color: var(--muted); margin-top: 6px; text-align: center;">Side effect: myopathy (↑ CK-MM). Monitor liver enzymes.</div>
  </div>""",

        r"<strong>MCAD deficiency:</strong>.*?(\r?\n)*.*?Medium Chain Acyl-CoA Dehydrogenase deficiency → β-oxidation block → hypoketotic hypoglycaemia in fasting infants → <strong>SIDS-like presentation</strong>\. Increased C8-C10 acylcarnitines on newborn screen\.":
"""<strong>MCAD deficiency:</strong>
  <div class="flowchart-container" style="margin-top: 10px; margin-bottom: 14px;">
    <div class="flow-box muted" style="text-align: left; width: 100%; box-sizing: border-box; padding: 12px; margin: 0 auto; display: block;">
      Medium Chain Acyl-CoA Dehydrogenase deficiency
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      β-oxidation block
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      hypoketotic hypoglycaemia in fasting infants
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      <strong>SIDS-like presentation</strong>
    </div>
    <div style="font-size: 0.85em; color: var(--muted); margin-top: 6px; text-align: center;">Increased C8-C10 acylcarnitines on newborn screen.</div>
  </div>""",

        r"<strong>Alcohol → Fatty liver:</strong>.*?(\r?\n)*.*?Ethanol → Acetaldehyde → NADH ↑ ↑ → NADH/NAD⁺ ratio ↑ → OAA → Malate \(depletes TCA\) → FA synthesis ↑ \+ FA oxidation ↓ → TAG accumulates\. Also: Acetaldehyde inhibits VLDL secretion\.":
"""<strong>Alcohol → Fatty liver:</strong>
  <div class="flowchart-container" style="margin-top: 10px; margin-bottom: 14px;">
    <div class="flow-box muted" style="text-align: left; width: 100%; box-sizing: border-box; padding: 12px; margin: 0 auto; display: block;">
      Ethanol → Acetaldehyde → NADH ↑ ↑
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      NADH/NAD⁺ ratio ↑
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      OAA → Malate (depletes TCA)
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      FA synthesis ↑ + FA oxidation ↓
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      TAG accumulates
    </div>
    <div style="font-size: 0.85em; color: var(--muted); margin-top: 6px; text-align: center;">Also: Acetaldehyde inhibits VLDL secretion.</div>
  </div>""",

        r"<strong>Refsum\'s disease:</strong>.*?(\r?\n)*.*?Phytanoyl-CoA hydroxylase deficiency → phytanic acid accumulates → peripheral neuropathy, retinitis pigmentosa, cerebellar ataxia\. Avoid chlorophyll-rich foods\.":
"""<strong>Refsum's disease:</strong>
  <div class="flowchart-container" style="margin-top: 10px; margin-bottom: 14px;">
    <div class="flow-box muted" style="text-align: left; width: 100%; box-sizing: border-box; padding: 12px; margin: 0 auto; display: block;">
      Phytanoyl-CoA hydroxylase deficiency
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      phytanic acid accumulates
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      peripheral neuropathy, retinitis pigmentosa, cerebellar ataxia
    </div>
    <div style="font-size: 0.85em; color: var(--muted); margin-top: 6px; text-align: center;">Avoid chlorophyll-rich foods.</div>
  </div>""",

        r"<strong>Tangier disease:</strong>.*?(\r?\n)*.*?ApoA-I deficiency → HDL deficiency → cholesterol accumulates in macrophages \(foam cells\) → orange tonsils, hepatosplenomegaly, ↑ atherosclerosis risk\.":
"""<strong>Tangier disease:</strong>
  <div class="flowchart-container" style="margin-top: 10px; margin-bottom: 14px;">
    <div class="flow-box muted" style="text-align: left; width: 100%; box-sizing: border-box; padding: 12px; margin: 0 auto; display: block;">
      ApoA-I deficiency
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      HDL deficiency
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      cholesterol accumulates in macrophages (foam cells)
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      orange tonsils, hepatosplenomegaly, ↑ atherosclerosis risk
    </div>
  </div>""",

        r"<strong>Abetalipoproteinaemia:</strong>.*?(\r?\n)*.*?ApoB deficiency → cannot form chylomicrons \+ VLDL → fat malabsorption, acanthocytes, ataxia, retinitis pigmentosa\. No dietary fat or fat-soluble vitamins absorbed\.":
"""<strong>Abetalipoproteinaemia:</strong>
  <div class="flowchart-container" style="margin-top: 10px; margin-bottom: 14px;">
    <div class="flow-box muted" style="text-align: left; width: 100%; box-sizing: border-box; padding: 12px; margin: 0 auto; display: block;">
      ApoB deficiency
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      cannot form chylomicrons + VLDL
      <div class="flow-arrow"><span class="dir-arrow">↓</span></div>
      fat malabsorption, acanthocytes, ataxia, retinitis pigmentosa
    </div>
    <div style="font-size: 0.85em; color: var(--muted); margin-top: 6px; text-align: center;">No dietary fat or fat-soluble vitamins absorbed.</div>
  </div>"""
    }

    for pat, rep in replacements.items():
        content = re.sub(pat, rep, content)
    
    return content

for fp in [file_path, file_path_x]:
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            orig = f.read()
        new_content = convert_clinical(orig)
        if new_content != orig:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated flowcharts in {fp}")
