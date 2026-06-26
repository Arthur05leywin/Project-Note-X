import os
import re

mod9 = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-09\module09_clinical_biochemistry.html"
mod9_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-09\module09_clinical_biochemistry_X.html"

def fix_jaundice_and_abg(content):
    # 1. Gilbert's & Neonatal Jaundice
    t_gilbert = r"""<div class="clinical-box">\s*<div class="cbox-title">Gilbert's Syndrome</div>\s*<p>Mildly reduced UGT1A1 activity \(~30% of normal\) → mild unconjugated hyperbilirubinaemia, especially after fasting or stress\. <strong>Benign</strong>, no liver disease\. Serum bilirubin 1\.2–3 mg/dL\. Fasting test: ↑ bilirubin after 48-hour fast\.</p>\s*</div>"""
    r_gilbert = """<div class="clinical-box">
<div class="cbox-title">Gilbert's Syndrome</div>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">Mildly reduced UGT1A1 activity (~30% of normal) → mild unconjugated hyperbilirubinaemia, especially after fasting or stress.</li>
  <li style="margin-bottom:6px;"><strong>Benign</strong>, no liver disease. Serum bilirubin 1.2–3 mg/dL.</li>
  <li>Fasting test: ↑ bilirubin after 48-hour fast.</li>
</ul>
</div>"""
    content = re.sub(t_gilbert, r_gilbert, content, flags=re.DOTALL)

    t_neo = r"""<div class="clinical-box">\s*<div class="cbox-title">Neonatal Physiological Jaundice \+ Phototherapy <span class="badge badge-pyq">PYQ 2011, 2017-S</span></div>\s*<p>UGT1A1 immature at birth → unconjugated hyperbilirubinaemia → indirect bili \(lipid-soluble\) crosses BBB → kernicterus\. <strong>Phototherapy:</strong> blue light \(420–480 nm\) converts insoluble bilirubin → lumirubin/photobilirubin \(water-soluble, polar isomers\) → excreted without conjugation in bile and urine\.</p>\s*</div>"""
    r_neo = """<div class="clinical-box">
<div class="cbox-title">Neonatal Physiological Jaundice + Phototherapy <span class="badge badge-pyq">PYQ 2011, 2017-S</span></div>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">UGT1A1 immature at birth → unconjugated hyperbilirubinaemia → indirect bili (lipid-soluble) crosses BBB → kernicterus.</li>
  <li><strong>Phototherapy:</strong> blue light (420–480 nm) converts insoluble bilirubin → lumirubin/photobilirubin (water-soluble, polar isomers) → excreted without conjugation in bile and urine.</li>
</ul>
</div>"""
    content = re.sub(t_neo, r_neo, content, flags=re.DOTALL)

    # 2. Bilirubin Metabolism
    t_bili1 = r"""<div class="flow-box accent">\s*<span class="lbl">Step 1 — Haem Catabolism \(Spleen/RES\)</span>\s*Senescent RBCs → Haemoglobin → Haem \+ Globin<br/>\s*Haem → Haem oxygenase → <strong>Biliverdin</strong> \(green\) \+ CO \+ Fe²⁺<br/>\s*Biliverdin → Biliverdin reductase → <strong>Bilirubin</strong> \(yellow, water-insoluble = indirect/unconjugated\)\s*</div>"""
    r_bili1 = """<div class="flow-box accent" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 1 — Haem Catabolism (Spleen/RES)</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">Senescent RBCs → Haemoglobin → Haem + Globin</li>
  <li style="margin-bottom:6px;">Haem → Haem oxygenase → <strong>Biliverdin</strong> (green) + CO + Fe²⁺</li>
  <li>Biliverdin → Biliverdin reductase → <strong>Bilirubin</strong> (yellow, water-insoluble = indirect/unconjugated)</li>
</ul>
</div>"""
    content = re.sub(t_bili1, r_bili1, content, flags=re.DOTALL)

    t_bili2 = r"""<div class="flow-box gold">\s*<span class="lbl">Step 2 — Hepatic Uptake</span>\s*Indirect bilirubin \(albumin-bound\) → hepatocyte<br/>\s*Dissociates from albumin → binds ligandin \(Y protein\) \+ Z protein inside hepatocyte\s*</div>"""
    r_bili2 = """<div class="flow-box gold" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 2 — Hepatic Uptake</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">Indirect bilirubin (albumin-bound) → hepatocyte</li>
  <li>Dissociates from albumin → binds ligandin (Y protein) + Z protein inside hepatocyte</li>
</ul>
</div>"""
    content = re.sub(t_bili2, r_bili2, content, flags=re.DOTALL)

    t_bili3 = r"""<div class="flow-box teal">\s*<span class="lbl">Step 3 — Conjugation</span>\s*Bilirubin \+ 2× UDP-glucuronic acid → <strong>Bilirubin diglucuronide</strong> \(direct/conjugated bilirubin\)<br/>\s*Enzyme: UDP-glucuronyl transferase \(UGT1A1\) — <strong>absent in Crigler-Najjar; reduced in Gilbert's</strong><br/>\s*Conjugated bilirubin = water-soluble → can be excreted in bile\s*</div>"""
    r_bili3 = """<div class="flow-box teal" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 3 — Conjugation in ER</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">Bilirubin + 2× UDP-glucuronic acid → <strong>Bilirubin diglucuronide</strong> (direct/conjugated bilirubin)</li>
  <li style="margin-bottom:6px;"><strong>Enzyme:</strong> UDP-glucuronyl transferase (UGT1A1) — absent in Crigler-Najjar; reduced in Gilbert's</li>
  <li>Conjugated bilirubin = water-soluble → can be excreted in bile</li>
</ul>
</div>"""
    content = re.sub(t_bili3, r_bili3, content, flags=re.DOTALL)

    t_bili4 = r"""<div class="flow-box purple">\s*<span class="lbl">Step 4 — Intestinal Fate</span>\s*Bilirubin diglucuronide → intestinal bacteria → deconjugation → <strong>Urobilinogen</strong><br/>\s*Urobilinogen: \(a\) 10–20% absorbed → portal blood → liver \(enterohepatic circulation\) or kidney → urine \(gives urine yellow colour\)<br/>\s*\(b\) Remainder → further reduced → <strong>Stercobilin</strong> → faeces \(brown colour\)\s*</div>"""
    r_bili4 = """<div class="flow-box" style="padding: 16px; text-align: left; background: var(--purple); color: #ffffff; border: 1px solid var(--purple); border-radius: 8px;">
<span class="lbl" style="display:block; margin-bottom: 8px; color: #ffffff; font-weight: 700;">Step 4 — Intestinal Fate</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;">Bilirubin diglucuronide → intestinal bacteria → deconjugation → <strong>Urobilinogen</strong></li>
  <li style="margin-bottom:6px;"><strong>Urobilinogen:</strong> (a) 10–20% absorbed → portal blood → liver (enterohepatic circulation) or kidney → urine (gives urine yellow colour)</li>
  <li>(b) Remainder → further reduced → <strong>Stercobilin</strong> → faeces (brown colour)</li>
</ul>
</div>"""
    content = re.sub(t_bili4, r_bili4, content, flags=re.DOTALL)


    # 3. LFT Result Row Squish Fix
    t_lft = r"""<div class="result-row"><span class="result-param">Total Bilirubin</span><span class="result-val result-high">6\.2 mg/dL ↑↑</span><span class="result-interp">Obstructive pattern: predominantly conjugated \(direct\)</span></div>\s*<div class="result-row"><span class="result-param">Direct Bili</span><span class="result-val result-high">5\.8 mg/dL ↑↑</span><span class="result-interp">Direct:Total ratio = 94% → obstructive/hepatocellular \(not haemolytic\)</span></div>\s*<div class="result-row"><span class="result-param">ALT / AST</span><span class="result-val result-normal">Normal \(32/26\)</span><span class="result-interp">No hepatocellular damage → not viral hepatitis; not alcoholic</span></div>\s*<div class="result-row"><span class="result-param">ALP</span><span class="result-val result-high">387 U/L ↑↑↑</span><span class="result-interp">Markedly elevated → hallmark of cholestasis/biliary obstruction</span></div>\s*<div class="result-row"><span class="result-param">Albumin</span><span class="result-val result-normal">3\.8 g/dL \(normal\)</span><span class="result-interp">Synthetic function preserved → likely acute, not chronic</span></div>\s*<div class="result-row"><span class="result-param">Clinical signs</span><span class="result-val">Dark urine \+ pale stool</span><span class="result-interp">Classic obstructive jaundice: conjugated bili → urine \(dark\) \+ no bile to gut \(pale stool\)</span></div>"""
    r_lft = """<ul style="margin:0 0 16px 0; padding-left:20px; font-size:14px; line-height:1.8;">
  <li><strong>Total Bilirubin:</strong> <span style="color:var(--rose)">6.2 mg/dL ↑↑</span> — Obstructive pattern: predominantly conjugated (direct)</li>
  <li><strong>Direct Bili:</strong> <span style="color:var(--rose)">5.8 mg/dL ↑↑</span> — Direct:Total ratio = 94% → obstructive/hepatocellular (not haemolytic)</li>
  <li><strong>ALT / AST:</strong> <span style="color:var(--teal)">Normal (32/26)</span> — No hepatocellular damage → not viral hepatitis; not alcoholic</li>
  <li><strong>ALP:</strong> <span style="color:var(--rose)">387 U/L ↑↑↑</span> — Markedly elevated → hallmark of cholestasis/biliary obstruction</li>
  <li><strong>Albumin:</strong> <span style="color:var(--teal)">3.8 g/dL (normal)</span> — Synthetic function preserved → likely acute, not chronic</li>
  <li><strong>Clinical signs:</strong> Dark urine + pale stool — Classic obstructive jaundice: conjugated bili → urine (dark) + no bile to gut (pale stool)</li>
</ul>"""
    content = re.sub(t_lft, r_lft, content, flags=re.DOTALL)


    # 4. ABG Step 4
    t_abg = r"""<div class="flow-box purple">\s*<span class="lbl">Step 4: Hypokalemia \+ Acidic urine — Paradoxical\?</span>\s*<strong>Why hypokalemia\?</strong> Vomiting → volume depletion → Aldosterone ↑ → Na⁺ reabsorption \+ K⁺ and H⁺ excretion → K⁺ loss<br/>\s*<strong>Why acidic urine in alkalosis\?</strong> K⁺ depleted cells exchange K⁺ for H⁺ → H⁺ moves intracellularly \+ K⁺ exits → remaining H⁺ in distal tubule excreted in urine → paradoxically acidic urine despite systemic alkalosis \(called "paradoxical aciduria"\)\s*</div>"""
    r_abg = """<div class="flow-box" style="padding: 16px; text-align: left; background: var(--purple); color: #ffffff; border: 1px solid var(--purple); border-radius: 8px;">
<span class="lbl" style="display:block; margin-bottom: 8px; color: #ffffff; font-weight: 700;">Step 4: Hypokalemia + Acidic urine — Paradoxical?</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:8px;"><strong>Why hypokalemia?</strong> Vomiting → volume depletion → Aldosterone ↑ → Na⁺ reabsorption + K⁺ and H⁺ excretion → K⁺ loss</li>
  <li><strong>Why acidic urine in alkalosis?</strong> K⁺ depleted cells exchange K⁺ for H⁺ → H⁺ moves intracellularly + K⁺ exits → remaining H⁺ in distal tubule excreted in urine → paradoxically acidic urine despite systemic alkalosis (called "paradoxical aciduria")</li>
</ul>
</div>"""
    content = re.sub(t_abg, r_abg, content, flags=re.DOTALL)

    return content

for fp in [mod9, mod9_x]:
    with open(fp, 'r', encoding='utf-8') as f:
        cont = f.read()
    new_cont = fix_jaundice_and_abg(cont)
    if new_cont != cont:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_cont)
        print("Updated " + fp)
    else:
        print("No changes made to " + fp)
