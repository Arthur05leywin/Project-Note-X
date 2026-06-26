import os
import re

def fix_module10_p53_and_hybridoma(content):
    # 1. HYBRIDOMA TECHNOLOGY
    # Step 1
    content = content.replace(
        'Inject mouse with antigen of interest → B cell response → spleen contains antigen-specific B cells',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li>Inject mouse with antigen of interest</li><li>B cell response generated</li><li>Spleen contains antigen-specific B cells</li></ul>'
    )
    # Step 2
    content = content.replace(
        '<div class="flow-box gold">',
        '<div class="flow-box gold" style="color:#ffffff;">'
    )
    step2_old = r"""Spleen B cells \+ Myeloma cells \(HAT-sensitive, immortal\) → <strong>Hybridoma cells</strong><br/>\s*Selection in HAT medium \(hypoxanthine, aminopterin, thymidine\) — only hybridomas survive \(myeloma dies, B cells die\)"""
    step2_new = """<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>Spleen B cells + Myeloma cells (HAT-sensitive, immortal) → <strong>Hybridoma cells</strong></li>
  <li>Selection in HAT medium (hypoxanthine, aminopterin, thymidine)</li>
  <li>Only hybridomas survive (myeloma dies, unfused B cells die naturally)</li>
</ul>"""
    content = re.sub(step2_old, step2_new, content)
    
    # Step 3
    content = content.replace(
        'Positive hybridoma cloned → each clone produces identical antibody → <strong>Monoclonal antibody</strong>',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li>Positive hybridoma cloned</li><li>Each clone produces identical antibody → <strong>Monoclonal antibody</strong></li></ul>'
    )
    
    # Step 4
    content = content.replace(
        'Mouse mAbs → chimeric (mouse Fv + human Fc) → humanised (only CDRs murine) → fully human (phage display). Suffix: -omab (murine), -ximab (chimeric), -zumab (humanised), -umab (fully human)',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li>Mouse mAbs (-omab)</li><li>Chimeric (mouse Fv + human Fc) (-ximab)</li><li>Humanised (only CDRs murine) (-zumab)</li><li>Fully human (phage display) (-umab)</li></ul>'
    )


    # 2. P53 AS GUARDIAN OF THE GENOME
    # Normal state
    content = content.replace(
        'p53 kept low by <strong>MDM2</strong> (E3 ubiquitin ligase) → ubiquitinates p53 → proteasomal degradation. MDM2 is itself induced by p53 (negative feedback)',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li>p53 kept low by <strong>MDM2</strong> (E3 ubiquitin ligase)</li><li>MDM2 ubiquitinates p53 → proteasomal degradation</li><li>MDM2 is itself induced by p53 (negative feedback loop)</li></ul>'
    )
    # Activation
    content = content.replace(
        'ATM/ATR kinases phosphorylate p53 at Ser15, Ser20 → MDM2 cannot bind → p53 stabilised + acetylated + tetramerises → TRANSCRIPTION FACTOR active',
        '<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;"><li>ATM/ATR kinases phosphorylate p53 at Ser15, Ser20</li><li>MDM2 cannot bind anymore</li><li>p53 is stabilised, acetylated, and tetramerises</li><li>Becomes an active <strong>TRANSCRIPTION FACTOR</strong></li></ul>'
    )
    
    # The p53 outcomes block. It is currently in a flow-h.
    # We will find the specific block starting from <div class="flow-h"> down to </div></div></div></div>
    
    target_block = r"""<div class="flow-h">
<div class="flow-box teal" style="text-align:center;">
<span class="lbl">Reversible damage → ARREST</span>
          p21 \(CDKN1A\) → inhibits CDK2 → Rb stays unphosphorylated → E2F sequestered → no S phase → G1/S arrest → time for DNA repair
        </div>
<div class="h-arrow">OR</div>
<div class="flow-box rose" style="text-align:center; color:#ffffff;">
<span class="lbl">Irreparable damage → APOPTOSIS</span>
          BAX, PUMA, NOXA → mitochondrial pathway → cytochrome c release → caspase 9 → effector caspases → cell death
        </div>
<div class="h-arrow">OR</div>
<div class="flow-box gold" style="text-align:center; color:#ffffff;">
<span class="lbl">Chronic/replicative stress → SENESCENCE</span>
          Permanent cell cycle arrest\. Prevents tumourigenesis in pre-malignant lesions
        </div>
</div>"""

    new_block = """<div class="flow-v">
<div class="flow-box teal" style="text-align:left; color:#ffffff;">
<span class="lbl" style="text-align:center; display:block;">Reversible damage → ARREST</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>p21 (CDKN1A) → inhibits CDK2</li>
  <li>Rb stays unphosphorylated → E2F sequestered</li>
  <li>No S phase → G1/S arrest</li>
  <li>Provides time for DNA repair</li>
</ul>
</div>
<div class="flow-step-label">OR</div>
<div class="flow-box rose" style="text-align:left; color:#ffffff;">
<span class="lbl" style="text-align:center; display:block;">Irreparable damage → APOPTOSIS</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>Activation of BAX, PUMA, NOXA</li>
  <li>Mitochondrial pathway → Cytochrome C release</li>
  <li>Activates caspase 9 → effector caspases</li>
  <li>Programmed cell death</li>
</ul>
</div>
<div class="flow-step-label">OR</div>
<div class="flow-box gold" style="text-align:left; color:#ffffff;">
<span class="lbl" style="text-align:center; display:block;">Chronic/replicative stress → SENESCENCE</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>Permanent cell cycle arrest</li>
  <li>Prevents tumourigenesis in pre-malignant lesions</li>
</ul>
</div>
</div>"""

    if target_block in content:
        content = content.replace(target_block, new_block)
    else:
        # try regex because of spacing
        content = re.sub(r'<div class="flow-h">\s*<div class="flow-box teal" style="text-align:center;">\s*<span class="lbl">Reversible damage → ARREST</span>\s*p21 \(CDKN1A\) → inhibits CDK2 → Rb stays unphosphorylated → E2F sequestered → no S phase → G1/S arrest → time for DNA repair\s*</div>\s*<div class="h-arrow">OR</div>\s*<div class="flow-box rose" style="text-align:center; color:#ffffff;">\s*<span class="lbl">Irreparable damage → APOPTOSIS</span>\s*BAX, PUMA, NOXA → mitochondrial pathway → cytochrome c release → caspase 9 → effector caspases → cell death\s*</div>\s*<div class="h-arrow">OR</div>\s*<div class="flow-box gold" style="text-align:center; color:#ffffff;">\s*<span class="lbl">Chronic/replicative stress → SENESCENCE</span>\s*Permanent cell cycle arrest\. Prevents tumourigenesis in pre-malignant lesions\s*</div>\s*</div>', new_block, content, flags=re.DOTALL)

    return content

mod10 = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-10\module10_immunochemistry_oncogenesis.html"
mod10_x = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-10\module10_immunochemistry_oncogenesis_X.html"

for fn in [mod10, mod10_x]:
    with open(fn, 'r', encoding='utf-8') as f:
        cont = f.read()
    new_cont = fix_module10_p53_and_hybridoma(cont)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(new_cont)
    print("Updated", fn)
