import os
import re

mod9_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-09\module09_clinical_biochemistry_X.html"

def fix_jaundice_x(content):
    # 2. Bilirubin Metabolism
    t_bili1 = r"""<div class="flow-box accent d-print-none">\s*<span class="lbl">Step 1 — Haem Catabolism \(Spleen/RES\)</span>\s*Senescent RBCs → Haemoglobin → Haem \+ Globin<br/>\s*Haem → Haem oxygenase → <strong>Biliverdin</strong> \(green\) \+ CO \+ Fe²⁺<br/>\s*Biliverdin → Biliverdin reductase → <strong>Bilirubin</strong> \(yellow, water-insoluble = indirect/unconjugated\)\s*</div>"""
    r_bili1 = """<div class="flow-box accent d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 1 — Haem Catabolism (Spleen/RES)</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">Senescent RBCs → Haemoglobin → Haem + Globin</li>
  <li style="margin-bottom:6px;">Haem → Haem oxygenase → <strong>Biliverdin</strong> (green) + CO + Fe²⁺</li>
  <li>Biliverdin → Biliverdin reductase → <strong>Bilirubin</strong> (yellow, water-insoluble = indirect/unconjugated)</li>
</ul>
</div>"""
    content = re.sub(t_bili1, r_bili1, content, flags=re.DOTALL)

    t_bili2 = r"""<div class="flow-box gold d-print-none">\s*<span class="lbl">Step 2 — Hepatic Uptake</span>\s*Indirect bilirubin \(albumin-bound\) → hepatocyte<br/>\s*Dissociates from albumin → binds ligandin \(Y protein\) \+ Z protein inside hepatocyte\s*</div>"""
    r_bili2 = """<div class="flow-box gold d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 2 — Hepatic Uptake</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">Indirect bilirubin (albumin-bound) → hepatocyte</li>
  <li>Dissociates from albumin → binds ligandin (Y protein) + Z protein inside hepatocyte</li>
</ul>
</div>"""
    content = re.sub(t_bili2, r_bili2, content, flags=re.DOTALL)

    t_bili3 = r"""<div class="flow-box teal d-print-none">\s*<span class="lbl">Step 3 — Conjugation</span>\s*Bilirubin \+ 2× UDP-glucuronic acid → <strong>Bilirubin diglucuronide</strong> \(direct/conjugated bilirubin\)<br/>\s*Enzyme: UDP-glucuronyl transferase \(UGT1A1\) — <strong>absent in Crigler-Najjar; reduced in Gilbert's</strong><br/>\s*Conjugated bilirubin = water-soluble → can be excreted in bile\s*</div>"""
    r_bili3 = """<div class="flow-box teal d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 3 — Conjugation in ER</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">Bilirubin + 2× UDP-glucuronic acid → <strong>Bilirubin diglucuronide</strong> (direct/conjugated bilirubin)</li>
  <li style="margin-bottom:6px;"><strong>Enzyme:</strong> UDP-glucuronyl transferase (UGT1A1) — absent in Crigler-Najjar; reduced in Gilbert's</li>
  <li>Conjugated bilirubin = water-soluble → can be excreted in bile</li>
</ul>
</div>"""
    content = re.sub(t_bili3, r_bili3, content, flags=re.DOTALL)

    t_bili4 = r"""<div class="flow-box purple d-print-none">\s*<span class="lbl">Step 4 — Intestinal Fate</span>\s*Bilirubin diglucuronide → intestinal bacteria → deconjugation → <strong>Urobilinogen</strong><br/>\s*Urobilinogen: \(a\) 10–20% absorbed → portal blood → liver \(enterohepatic circulation\) or kidney → urine \(gives urine yellow colour\)<br/>\s*\(b\) Remainder → further reduced → <strong>Stercobilin</strong> → faeces \(brown colour\)\s*</div>"""
    r_bili4 = """<div class="flow-box d-print-none" style="padding: 16px; text-align: left; background: var(--purple); color: #ffffff; border: 1px solid var(--purple); border-radius: 8px;">
<span class="lbl" style="display:block; margin-bottom: 8px; color: #ffffff; font-weight: 700;">Step 4 — Intestinal Fate</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">Bilirubin diglucuronide → intestinal bacteria → deconjugation → <strong>Urobilinogen</strong></li>
  <li style="margin-bottom:6px;"><strong>Urobilinogen:</strong> (a) 10–20% absorbed → portal blood → liver (enterohepatic circulation) or kidney → urine (gives urine yellow colour)</li>
  <li>(b) Remainder → further reduced → <strong>Stercobilin</strong> → faeces (brown colour)</li>
</ul>
</div>"""
    content = re.sub(t_bili4, r_bili4, content, flags=re.DOTALL)

    # 4. ABG Step 4
    t_abg = r"""<div class="flow-box purple d-print-none">\s*<span class="lbl">Step 4: Hypokalemia \+ Acidic urine — Paradoxical\?</span>\s*<strong>Why hypokalemia\?</strong> Vomiting → volume depletion → Aldosterone ↑ → Na⁺ reabsorption \+ K⁺ and H⁺ excretion → K⁺ loss<br/>\s*<strong>Why acidic urine in alkalosis\?</strong> K⁺ depleted cells exchange K⁺ for H⁺ → H⁺ moves intracellularly \+ K⁺ exits → remaining H⁺ in distal tubule excreted in urine → paradoxically acidic urine despite systemic alkalosis \(called "paradoxical aciduria"\)\s*</div>"""
    r_abg = """<div class="flow-box d-print-none" style="padding: 16px; text-align: left; background: var(--purple); color: #ffffff; border: 1px solid var(--purple); border-radius: 8px;">
<span class="lbl" style="display:block; margin-bottom: 8px; color: #ffffff; font-weight: 700;">Step 4: Hypokalemia + Acidic urine — Paradoxical?</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:8px;"><strong>Why hypokalemia?</strong> Vomiting → volume depletion → Aldosterone ↑ → Na⁺ reabsorption + K⁺ and H⁺ excretion → K⁺ loss</li>
  <li><strong>Why acidic urine in alkalosis?</strong> K⁺ depleted cells exchange K⁺ for H⁺ → H⁺ moves intracellularly + K⁺ exits → remaining H⁺ in distal tubule excreted in urine → paradoxically acidic urine despite systemic alkalosis (called "paradoxical aciduria")</li>
</ul>
</div>"""
    content = re.sub(t_abg, r_abg, content, flags=re.DOTALL)

    return content

with open(mod9_x, 'r', encoding='utf-8') as f:
    cont = f.read()

new_cont = fix_jaundice_x(cont)
if new_cont != cont:
    with open(mod9_x, 'w', encoding='utf-8') as f:
        f.write(new_cont)
    print("Updated " + mod9_x)
else:
    print("No changes made to " + mod9_x)
