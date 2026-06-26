import os
import re

mod7 = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-07\module07_biological_oxidation.html"
mod7_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-07\module07_biological_oxidation_X.html"
mod8 = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-08\module08_nutrition_vitamins.html"
mod8_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-08\module08_nutrition_vitamins_X.html"

def fix_chemiosmotic(content):
    # Fix the keypoint flex issue with an inline style
    target_kp = r"""<div class="keypoint">\s*Proposed by Peter Mitchell.*?<span class="badge badge-fav">⭐ PYQ 2010, 2023</span>\s*</div>"""
    replace_kp = """<div class="keypoint" style="display: block !important;">
          Proposed by Peter Mitchell (1961) — Nobel Prize 1978. Key insight:
          Energy from electron transport is stored as a
          <strong>proton electrochemical gradient</strong> (proton motive
          force), not as a chemical intermediate.
          <span class="badge badge-fav" style="display: inline-block; margin-left: 8px;">⭐ PYQ 2010, 2023</span>
        </div>"""
    content = re.sub(target_kp, replace_kp, content, flags=re.DOTALL)
    
    # Fix Chemiosmotic flowchart congestion
    target_flow = r"""<div class="flow-box accent">\s*<span class="lbl">Step 1 — Electron Transport</span>.*?Matrix is alkaline \+ negative</span>\s*</div>"""
    replace_flow = """<div class="flow-box accent" style="padding: 16px; margin-bottom: 12px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 1 — Electron Transport</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">Complexes I, III, IV pump H⁺ from <strong>matrix → intermembrane space (IMS)</strong></li>
  <li>Builds proton gradient: IMS is acidic (high [H⁺]) + positive; Matrix is alkaline + negative</li>
</ul>
</div>"""
    content = re.sub(target_flow, replace_flow, content, flags=re.DOTALL)
    
    target_flow2 = r"""<div class="flow-box gold">\s*<span class="lbl">Step 2 — Proton Motive Force \(PMF\)</span>.*?Total PMF ≈ <strong>0\.22 V</strong> \(or ~200 mV\) across IMM\s*</div>"""
    replace_flow2 = """<div class="flow-box gold" style="padding: 16px; margin-bottom: 12px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 2 — Proton Motive Force (PMF)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">Two components: <strong>Chemical gradient (ΔpH)</strong> = ~0.75 V + <strong>Electrical gradient (ΔΨ)</strong> = ~0.14 V</li>
  <li>Total PMF ≈ <strong>0.22 V</strong> (or ~200 mV) across IMM</li>
</ul>
</div>"""
    content = re.sub(target_flow2, replace_flow2, content, flags=re.DOTALL)
    
    target_flow3 = r"""<div class="flow-box teal">\s*<span class="lbl">Step 3 — ATP Synthesis.*?<strong>ADP \+ Pi → ATP</strong>\s*</div>"""
    replace_flow3 = """<div class="flow-box teal" style="padding: 16px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 3 — ATP Synthesis (F₀F₁ ATPase / Complex V)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">H⁺ flows down gradient through F₀ (rotor in membrane)</li>
  <li style="margin-bottom:6px;">rotates c-ring → mechanical energy transmitted to F₁ (in matrix)</li>
  <li style="margin-bottom:6px;">conformational changes in β-subunits</li>
  <li><strong>ADP + Pi → ATP</strong></li>
</ul>
</div>"""
    content = re.sub(target_flow3, replace_flow3, content, flags=re.DOTALL)
    return content

for fp in [mod7, mod7_x]:
    with open(fp, 'r', encoding='utf-8') as f:
        cont = f.read()
    new_cont = fix_chemiosmotic(cont)
    if new_cont != cont:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_cont)
        print("Updated mod 7: " + fp)

def fix_vitamins(content):
    # Fix Folate Metabolism colors
    target_folate = r"""<div class="flow-box rose">\s*<span class="lbl">THE FOLATE TRAP \(B12 deficiency\)</span>.*?\(B12-specific, not seen in folate deficiency alone\)</span>\s*</div>"""
    replace_folate = """<div class="flow-box" style="padding: 16px; text-align: left; background: var(--rose); color: #1a1a1a; border: 1px solid var(--rose); margin-bottom: 12px; border-radius: 8px;">
<span class="lbl" style="display:block; margin-bottom: 8px; color: #1a1a1a; font-weight: 700; font-size: 1.1em;">THE FOLATE TRAP (B12 deficiency)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">All cellular folate becomes "trapped" as <strong>methyl-THF</strong> — the monoglutamate form cannot be re-polyglutamated and retained inside cells</li>
  <li style="margin-bottom:6px;">No free THF available → <strong>cannot synthesise thymidylate (dTMP)</strong></li>
  <li style="margin-bottom:6px;">DNA synthesis impaired → megaloblastic anaemia (same as folate deficiency)</li>
  <li><span style="font-weight:600;">But:</span> homocysteine accumulates → demyelination → <strong>NEUROLOGICAL DAMAGE</strong> (B12-specific, not seen in folate deficiency alone)</li>
</ul>
</div>"""
    content = re.sub(target_folate, replace_folate, content, flags=re.DOTALL)

    # Change the other folate boxes to be spaced out and readable
    target_f1 = r"""<div class="flow-box gold">\s*<span class="lbl">Dietary Folate.*?active form\s*</div>"""
    replace_f1 = """<div class="flow-box gold" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Dietary Folate (Folic Acid)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>Dietary polyglutamate → Deconjugated → <strong>Folic acid (PteGlu)</strong></li>
  <li>Reduced to <strong>Dihydrofolate (DHF)</strong> by DHFR</li>
  <li>Further reduced to <strong>Tetrahydrofolate (THF)</strong> — active form</li>
</ul>
</div>"""
    content = re.sub(target_f1, replace_f1, content, flags=re.DOTALL)

    target_f2 = r"""<div class="flow-box teal">\s*<span class="lbl">Key Reaction.*?transfer the methyl group</span>\s*</div>"""
    replace_f2 = """<div class="flow-box teal" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Key Reaction — Methionine Synthase (requires B12)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;"><strong>Methyl-THF</strong> + Homocysteine → <strong>THF</strong> + Methionine</li>
  <li><span class="sub">This reaction REQUIRES Vitamin B12 (as methylcobalamin) to transfer the methyl group</span></li>
</ul>
</div>"""
    content = re.sub(target_f2, replace_f2, content, flags=re.DOTALL)

    target_f3 = r"""<div class="flow-box accent">\s*<span class="lbl">Thymidylate Synthase Reaction.*?inhibitor\)</span>\s*</div>"""
    replace_f3 = """<div class="flow-box accent" style="padding: 16px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Thymidylate Synthase Reaction (DNA synthesis)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li style="margin-bottom:6px;">dUMP + <strong>Methylene-THF</strong> → dTMP + DHF</li>
  <li><span class="sub">DHF → THF (by DHFR). Blocked by: Methotrexate (DHFR inhibitor), 5-FU (thymidylate synthase inhibitor)</span></li>
</ul>
</div>"""
    content = re.sub(target_f3, replace_f3, content, flags=re.DOTALL)

    # Fix Walds visual cycle (Bleaching & Recovery)
    target_v1 = r"""<div class="flow-box purple">\s*<span class="lbl">Bleaching reaction.*?nerve impulse generated\s*</div>"""
    replace_v1 = """<div class="flow-box purple" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Bleaching reaction — isomerisation</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>11-cis Retinal → <strong>all-trans Retinal</strong></li>
  <li>Rhodopsin dissociates → Opsin released</li>
  <li>Conformational change → <strong>nerve impulse generated</strong></li>
</ul>
</div>"""
    content = re.sub(target_v1, replace_v1, content, flags=re.DOTALL)

    target_v2 = r"""<div class="flow-box teal">\s*<span class="lbl">Recovery in darkness.*?dietary replenishment needed\s*</div>"""
    replace_v2 = """<div class="flow-box teal" style="padding: 16px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Recovery in darkness (RPE cells)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>all-trans Retinal → all-trans Retinol → <strong>11-cis Retinal</strong> (by retinal isomerase)</li>
  <li>Combines with opsin → Rhodopsin regenerated</li>
  <li><span class="sub">Vitamin A is NOT consumed — it is recycled. But losses occur → dietary replenishment needed</span></li>
</ul>
</div>"""
    content = re.sub(target_v2, replace_v2, content, flags=re.DOTALL)
    
    target_v0 = r"""<div class="flow-box gold">\s*<span class="lbl">Dark-adapted Rod Cell</span>.*?Scotopsin \+ 11-cis retinal\)\s*</div>"""
    replace_v0 = """<div class="flow-box gold" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Dark-adapted Rod Cell</span>
<div style="font-size:13px; line-height:1.6;">
  <strong>11-cis Retinal</strong> + Opsin → <strong>Rhodopsin</strong> (purple-red pigment, Scotopsin + 11-cis retinal)
</div>
</div>"""
    content = re.sub(target_v0, replace_v0, content, flags=re.DOTALL)


    # Fix Vit D cycle
    target_d1 = r"""<div class="flow-box blue">\s*<span class="lbl">Step 1 — Skin.*?from animals/fish liver oil\s*</div>"""
    replace_d1 = """<div class="flow-box blue" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 1 — Skin (UV-B, 290-315 nm)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li><strong>7-dehydrocholesterol</strong> → UV-B → <strong>Cholecalciferol (Vitamin D3)</strong></li>
  <li><span class="sub">Diet: D2 (ergocalciferol) from plants; D3 (cholecalciferol) from animals/fish liver oil</span></li>
</ul>
</div>"""
    content = re.sub(target_d1, replace_d1, content, flags=re.DOTALL)

    target_d2 = r"""<div class="flow-box gold">\s*<span class="lbl">Step 2 — Liver.*?assess Vit D status\s*</div>"""
    replace_d2 = """<div class="flow-box gold" style="padding: 16px; text-align: left; margin-bottom: 12px;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 2 — Liver (25-hydroxylase)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>Cholecalciferol → <strong>25-hydroxycholecalciferol (Calcidiol / 25-OH-D3)</strong></li>
  <li><span class="sub">Storage form — measured in blood to assess Vit D status</span></li>
</ul>
</div>"""
    content = re.sub(target_d2, replace_d2, content, flags=re.DOTALL)

    target_d3 = r"""<div class="flow-box accent">\s*<span class="lbl">Step 3 — Kidney.*?active form\s*</div>"""
    replace_d3 = """<div class="flow-box accent" style="padding: 16px; text-align: left;">
<span class="lbl" style="display:block; margin-bottom: 8px;">Step 3 — Kidney (1α-hydroxylase)</span>
<ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.6;">
  <li>25-OH-D3 → <strong>1,25-dihydroxycholecalciferol (Calcitriol)</strong></li>
  <li><span class="sub">Biologically active form</span></li>
</ul>
</div>"""
    content = re.sub(target_d3, replace_d3, content, flags=re.DOTALL)

    return content

for fp in [mod8, mod8_x]:
    with open(fp, 'r', encoding='utf-8') as f:
        cont = f.read()
    new_cont = fix_vitamins(cont)
    if new_cont != cont:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_cont)
        print("Updated mod 8: " + fp)

print("Done")
