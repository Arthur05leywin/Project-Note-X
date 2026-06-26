import os
import re
import shutil

mod_dir = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-09"
files = ["module09_clinical_biochemistry.html", "module09_clinical_biochemistry_X.html"]

# Copy image
src_img = r"C:\Users\sayan\.gemini\antigravity\brain\1691e826-d1b4-41cd-a4df-e33dba306da0\lipid_peroxidation_diagram_1781829882819.png"
dst_img = os.path.join(mod_dir, "lipid_peroxidation.png")
if os.path.exists(src_img):
    shutil.copy(src_img, dst_img)

def fix_content(content):
    # 1. ADA
    content = content.replace("Diagnostic Criteria (WHO/ADA)", "Diagnostic Criteria (ADA)")
    
    # 2. Image
    img_tag = r'<img src="lipid_peroxidation.png" alt="Lipid Peroxidation Diagram" style="width:100%; border-radius:12px; margin-bottom:16px; border:1px solid rgba(255,255,255,0.1);">'
    if 'src="lipid_peroxidation.png"' not in content:
        content = content.replace('<div class="flow-title">Free Radical Chain Reaction — Lipid Peroxidation</div>',
                                  f'<div class="flow-title">Free Radical Chain Reaction — Lipid Peroxidation</div>\n{img_tag}')
                                  
    # 3. Glutathione Table reactions (white-space nowrap)
    # We will just replace all <td> inside the reaction column for these specific enzymes
    # Let's just do a regex replace for the reactions
    content = content.replace('<td>ROOH + 2GSH → ROH + GSSG + H₂O<br/>H₂O₂ + 2GSH → 2H₂O + GSSG</td>',
                              '<td style="white-space:nowrap; font-family: \'JetBrains Mono\', monospace; font-size:13px; line-height:1.6;">ROOH + 2GSH → ROH + GSSG + H₂O<br/>H₂O₂ + 2GSH → 2H₂O + GSSG</td>')
    content = content.replace('<td>GSSG + NADPH → 2GSH</td>',
                              '<td style="white-space:nowrap; font-family: \'JetBrains Mono\', monospace; font-size:13px;">GSSG + NADPH → 2GSH</td>')
    content = content.replace('<td>Trx(ox) + NADPH → Trx(red)</td>',
                              '<td style="white-space:nowrap; font-family: \'JetBrains Mono\', monospace; font-size:13px;">Trx(ox) + NADPH → Trx(red)</td>')

    # 4. Paracetamol
    p_text = r"<p>Therapeutic dose: paracetamol → glucuronide/sulphate conjugates \(Phase II\)\. Overdose → CYP2E1 \(Phase I\) → NAPQI \(toxic reactive metabolite\)\. Normal: NAPQI \+ GSH → non-toxic mercapturic acid\. Overdose: GSH depleted → NAPQI binds hepatocyte proteins → hepatocellular necrosis → fulminant hepatic failure\. <strong>Treatment: N-Acetylcysteine \(NAC\)</strong> — replenishes GSH by providing cysteine → cures paracetamol hepatotoxicity if given early\.</p>"
    p_repl = """<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li style="margin-bottom:6px;"><strong>Therapeutic dose:</strong> Paracetamol → glucuronide/sulphate conjugates (Phase II detox).</li>
  <li style="margin-bottom:6px;"><strong>Overdose:</strong> Saturated Phase II → CYP2E1 (Phase I) takes over → produces <strong>NAPQI</strong> (highly toxic reactive metabolite).</li>
  <li style="margin-bottom:6px;"><strong>Normal Rescue:</strong> NAPQI + Glutathione (GSH) → non-toxic mercapturic acid (excreted).</li>
  <li style="margin-bottom:6px;"><strong>Toxic Crisis:</strong> GSH pool depleted → NAPQI binds covalently to hepatocyte proteins → widespread hepatocellular necrosis → fulminant hepatic failure.</li>
  <li><strong>Treatment — N-Acetylcysteine (NAC):</strong> Replenishes GSH by providing cysteine. Cures paracetamol hepatotoxicity if administered early!</li>
</ul>"""
    content = re.sub(p_text, p_repl, content)

    # 5. Biotransformation White Text
    # For Phase I
    content = content.replace('<div class="flow-box rose">', '<div class="flow-box rose" style="color:#ffffff;">')
    # For Phase I with d-print-none
    content = content.replace('<div class="flow-box rose d-print-none">', '<div class="flow-box rose d-print-none" style="color:#ffffff;">')

    # For Phase III
    content = content.replace('<div class="flow-box gold">', '<div class="flow-box gold" style="color:#ffffff;">')
    content = content.replace('<div class="flow-box gold d-print-none">', '<div class="flow-box gold d-print-none" style="color:#ffffff;">')
    
    # Wait! If the original string had newlines, it might not match. Let's make sure our replacements are solid.
    # The <div class="flow-box rose"> is fairly standard.
    
    # Also fix text colors inside Phase I / III
    # The sub text <span class="sub"> might be gray and unreadable on rose. We can force it white too.
    content = content.replace('<span class="sub">Makes drug more reactive — NOT always detoxification!</span>', 
                              '<span class="sub" style="color:#ffeeee; opacity:0.9;">Makes drug more reactive — NOT always detoxification!</span>')
    content = content.replace('<span class="sub">Usually detoxification. Some conjugates still active',
                              '<span class="sub" style="color:#e0f2f1; opacity:0.9;">Usually detoxification. Some conjugates still active')
    content = content.replace('<span class="sub">Important for multi-drug resistance in cancer</span>',
                              '<span class="sub" style="color:#fff8e1; opacity:0.9;">Important for multi-drug resistance in cancer</span>')

    return content

for fn in files:
    fp = os.path.join(mod_dir, fn)
    with open(fp, 'r', encoding='utf-8') as f:
        cont = f.read()
    
    new_cont = fix_content(cont)
    
    if new_cont != cont:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_cont)
        print(f"Updated {fn}")
    else:
        print(f"No changes to {fn}")
