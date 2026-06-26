import os
import re

mod9 = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-09\module09_clinical_biochemistry.html"
mod9_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-09\module09_clinical_biochemistry_X.html"

def fix_acid_base(content):
    # Immediate
    t1 = r"""<div class="flow-box blue d-print-none">\s*<span class="lbl">IMMEDIATE \(seconds\) — Chemical Buffers</span>\s*HCO₃⁻/H₂CO₃ · Phosphate \(HPO₄²⁻/H₂PO₄⁻\) · Protein/Haemoglobin · Ammonia buffer in kidney\s*<span class="sub">First line of defence — do NOT eliminate acid, just neutralise it temporarily</span>\s*</div>"""
    r1 = """<div class="flow-box blue d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">IMMEDIATE (seconds) — Chemical Buffers</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li><strong>Types:</strong> HCO₃⁻/H₂CO₃ · Phosphate (HPO₄²⁻/H₂PO₄⁻) · Protein/Haemoglobin · Ammonia (kidney)</li>
  <li><span class="sub">First line of defence — do NOT eliminate acid, just neutralise it temporarily</span></li>
</ul>
</div>"""
    content = re.sub(t1, r1, content, flags=re.DOTALL)

    # Fast
    t2 = r"""<div class="flow-box gold d-print-none">\s*<span class="lbl">FAST \(minutes to hours\) — Respiratory Compensation</span>\s*CO₂ \+ H₂O ⇌ H₂CO₃ ⇌ H⁺ \+ HCO₃⁻ \(catalysed by carbonic anhydrase\)<br/>\s*Acidosis → ↑ RR → blow off CO₂ → pH rises<br/>\s*Alkalosis → ↓ RR → retain CO₂ → pH falls\s*<span class="sub">Lungs eliminate CO₂ \(volatile acid\)\. Fast but not complete correction\.</span>\s*</div>"""
    r2 = """<div class="flow-box gold d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">FAST (minutes to hours) — Respiratory Compensation</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">CO₂ + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻ (by carbonic anhydrase)</li>
  <li style="margin-bottom:6px;"><strong>Acidosis:</strong> ↑ Respiratory Rate → blow off CO₂ → pH rises</li>
  <li style="margin-bottom:6px;"><strong>Alkalosis:</strong> ↓ Respiratory Rate → retain CO₂ → pH falls</li>
  <li><span class="sub">Lungs eliminate CO₂ (volatile acid). Fast but not complete correction.</span></li>
</ul>
</div>"""
    content = re.sub(t2, r2, content, flags=re.DOTALL)

    # Slow
    t3 = r"""<div class="flow-box accent d-print-none">\s*<span class="lbl">SLOW but COMPLETE \(hours to days\) — Renal Compensation</span>\s*<strong>Acidosis:</strong> Kidneys ↑ H⁺ excretion \(as NH₄⁺ and titratable acid\) \+ ↑ HCO₃⁻ reabsorption<br/>\s*<strong>Alkalosis:</strong> Kidneys ↓ H⁺ excretion \+ ↓ HCO₃⁻ reabsorption \+ ↑ HCO₃⁻ excretion\s*<span class="sub">Only system that can completely restore normal pH\. Carbonic anhydrase inhibitors \(acetazolamide\) block renal H⁺ secretion\.</span>\s*</div>"""
    r3 = """<div class="flow-box accent d-print-none" style="padding: 16px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">SLOW but COMPLETE (hours to days) — Renal Compensation</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;"><strong>Acidosis:</strong> Kidneys ↑ H⁺ excretion (as NH₄⁺ and titratable acid) + ↑ HCO₃⁻ reabsorption</li>
  <li style="margin-bottom:6px;"><strong>Alkalosis:</strong> Kidneys ↓ H⁺ excretion + ↓ HCO₃⁻ reabsorption + ↑ HCO₃⁻ excretion</li>
  <li><span class="sub">Only system that can completely restore normal pH. Carbonic anhydrase inhibitors (acetazolamide) block renal H⁺ secretion.</span></li>
</ul>
</div>"""
    content = re.sub(t3, r3, content, flags=re.DOTALL)

    return content

for fp in [mod9, mod9_x]:
    with open(fp, 'r', encoding='utf-8') as f: cont = f.read()
    new_cont = fix_acid_base(cont)
    if new_cont != cont:
        with open(fp, 'w', encoding='utf-8') as f: f.write(new_cont)
        print("Updated " + fp)
