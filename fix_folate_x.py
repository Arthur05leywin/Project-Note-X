import os
import re

mod8_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-08\module08_nutrition_vitamins_X.html"

def fix_vitamins_x(content):
    # Folate
    target_folate = r"""<div class="flow-box rose d-print-none">\s*<span class="lbl">THE FOLATE TRAP \(B12 deficiency\)</span>.*?\(B12-specific, not seen in folate deficiency alone\)</span>\s*</div>"""
    replace_folate = """<div class="flow-box d-print-none" style="padding: 16px; text-align: left; background: var(--rose); color: #1a1a1a; border: 1px solid var(--rose); margin-bottom: 12px; border-radius: 8px;">
<span class="lbl" style="display:block; margin-bottom: 8px; color: #1a1a1a; font-weight: 700; font-size: 1.1em;">THE FOLATE TRAP (B12 deficiency)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">All cellular folate becomes "trapped" as <strong>methyl-THF</strong> — the monoglutamate form cannot be re-polyglutamated and retained inside cells</li>
  <li style="margin-bottom:6px;">No free THF available → <strong>cannot synthesise thymidylate (dTMP)</strong></li>
  <li style="margin-bottom:6px;">DNA synthesis impaired → megaloblastic anaemia (same as folate deficiency)</li>
  <li><span style="font-weight:600;">But:</span> homocysteine accumulates → demyelination → <strong>NEUROLOGICAL DAMAGE</strong> (B12-specific, not seen in folate deficiency alone)</li>
</ul>
</div>"""
    content = re.sub(target_folate, replace_folate, content, flags=re.DOTALL)

    target_f1 = r"""<div class="flow-box gold d-print-none">\s*<span class="lbl">Dietary Folate.*?active form\s*</div>"""
    replace_f1 = """<div class="flow-box gold d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Dietary Folate (Folic Acid)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>Dietary polyglutamate → Deconjugated → <strong>Folic acid (PteGlu)</strong></li>
  <li>Reduced to <strong>Dihydrofolate (DHF)</strong> by DHFR</li>
  <li>Further reduced to <strong>Tetrahydrofolate (THF)</strong> — active form</li>
</ul>
</div>"""
    content = re.sub(target_f1, replace_f1, content, flags=re.DOTALL)

    target_f2 = r"""<div class="flow-box teal d-print-none">\s*<span class="lbl">Key Reaction.*?transfer the methyl group</span>\s*</div>"""
    replace_f2 = """<div class="flow-box teal d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Key Reaction — Methionine Synthase (requires B12)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;"><strong>Methyl-THF</strong> + Homocysteine → <strong>THF</strong> + Methionine</li>
  <li><span class="sub">This reaction REQUIRES Vitamin B12 (as methylcobalamin) to transfer the methyl group</span></li>
</ul>
</div>"""
    content = re.sub(target_f2, replace_f2, content, flags=re.DOTALL)

    target_f3 = r"""<div class="flow-box accent d-print-none">\s*<span class="lbl">Thymidylate Synthase Reaction.*?inhibitor\)</span>\s*</div>"""
    replace_f3 = """<div class="flow-box accent d-print-none" style="padding: 16px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Thymidylate Synthase Reaction (DNA synthesis)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">dUMP + <strong>Methylene-THF</strong> → dTMP + DHF</li>
  <li><span class="sub">DHF → THF (by DHFR). Blocked by: Methotrexate (DHFR inhibitor), 5-FU (thymidylate synthase inhibitor)</span></li>
</ul>
</div>"""
    content = re.sub(target_f3, replace_f3, content, flags=re.DOTALL)

    # Vit D
    target_d1 = r"""<div class="flow-box blue d-print-none">\s*<span class="lbl">Step 1 — Skin.*?from animals/fish liver oil\s*</div>"""
    replace_d1 = """<div class="flow-box blue d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 1 — Skin (UV-B, 290-315 nm)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li><strong>7-dehydrocholesterol</strong> → UV-B → <strong>Cholecalciferol (Vitamin D3)</strong></li>
  <li><span class="sub">Diet: D2 (ergocalciferol) from plants; D3 (cholecalciferol) from animals/fish liver oil</span></li>
</ul>
</div>"""
    content = re.sub(target_d1, replace_d1, content, flags=re.DOTALL)

    target_d2 = r"""<div class="flow-box gold d-print-none">\s*<span class="lbl">Step 2 — Liver.*?assess Vit D status\s*</div>"""
    replace_d2 = """<div class="flow-box gold d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 2 — Liver (25-hydroxylase)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>Cholecalciferol → <strong>25-hydroxycholecalciferol (Calcidiol / 25-OH-D3)</strong></li>
  <li><span class="sub">Storage form — measured in blood to assess Vit D status</span></li>
</ul>
</div>"""
    content = re.sub(target_d2, replace_d2, content, flags=re.DOTALL)

    target_d3 = r"""<div class="flow-box accent d-print-none">\s*<span class="lbl">Step 3 — Kidney.*?active form\s*</div>"""
    replace_d3 = """<div class="flow-box accent d-print-none" style="padding: 16px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 3 — Kidney (1α-hydroxylase)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>25-OH-D3 → <strong>1,25-dihydroxycholecalciferol (Calcitriol)</strong></li>
  <li><span class="sub">Biologically active form</span></li>
</ul>
</div>"""
    content = re.sub(target_d3, replace_d3, content, flags=re.DOTALL)

    # Wald
    target_v1 = r"""<div class="flow-box purple d-print-none">\s*<span class="lbl">Bleaching reaction.*?nerve impulse generated\s*</div>"""
    replace_v1 = """<div class="flow-box purple d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Bleaching reaction — isomerisation</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>11-cis Retinal → <strong>all-trans Retinal</strong></li>
  <li>Rhodopsin dissociates → Opsin released</li>
  <li>Conformational change → <strong>nerve impulse generated</strong></li>
</ul>
</div>"""
    content = re.sub(target_v1, replace_v1, content, flags=re.DOTALL)

    target_v2 = r"""<div class="flow-box teal d-print-none">\s*<span class="lbl">Recovery in darkness.*?dietary replenishment needed\s*</div>"""
    replace_v2 = """<div class="flow-box teal d-print-none" style="padding: 16px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Recovery in darkness (RPE cells)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>all-trans Retinal → all-trans Retinol → <strong>11-cis Retinal</strong> (by retinal isomerase)</li>
  <li>Combines with opsin → Rhodopsin regenerated</li>
  <li><span class="sub">Vitamin A is NOT consumed — it is recycled. But losses occur → dietary replenishment needed</span></li>
</ul>
</div>"""
    content = re.sub(target_v2, replace_v2, content, flags=re.DOTALL)
    
    target_v0 = r"""<div class="flow-box gold d-print-none">\s*<span class="lbl">Dark-adapted Rod Cell</span>.*?Scotopsin \+ 11-cis retinal\)\s*</div>"""
    replace_v0 = """<div class="flow-box gold d-print-none" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Dark-adapted Rod Cell</span>
<div style="font-size:13px; line-height:1.6;">
  <strong>11-cis Retinal</strong> + Opsin → <strong>Rhodopsin</strong> (purple-red pigment, Scotopsin + 11-cis retinal)
</div>
</div>"""
    content = re.sub(target_v0, replace_v0, content, flags=re.DOTALL)

    return content

with open(mod8_x, 'r', encoding='utf-8') as f:
    cont = f.read()
new_cont = fix_vitamins_x(cont)
if new_cont != cont:
    with open(mod8_x, 'w', encoding='utf-8') as f:
        f.write(new_cont)
    print("Updated mod 8 X")
