import os
import re

def fix_x(content):
    
    # Normal state - color #ffffff
    content = content.replace('<div class="flow-box blue d-print-none">', '<div class="flow-box blue d-print-none" style="color: #ffffff;">')
    content = content.replace('<div class="flow-box blue" style="color: #ffffff;">', '<div class="flow-box blue" style="color: #ffffff;">') # just in case
    
    # Activation
    content = content.replace('<div class="flow-box accent d-print-none">', '<div class="flow-box accent d-print-none" style="color: #ffffff;">')
    
    # The flow-h block
    new_block_x = """<div class="flow-v">
<div class="flow-box teal d-print-none" style="text-align:left; color:#ffffff;">
<span class="lbl" style="text-align:center; display:block;">Reversible damage → ARREST</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>p21 (CDKN1A) → inhibits CDK2</li>
  <li>Rb stays unphosphorylated → E2F sequestered</li>
  <li>No S phase → G1/S arrest</li>
  <li>Provides time for DNA repair</li>
</ul>
</div>
<div class="flow-step-label">OR</div>
<div class="flow-box rose d-print-none" style="text-align:left; color:#ffffff;">
<span class="lbl" style="text-align:center; display:block;">Irreparable damage → APOPTOSIS</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>Activation of BAX, PUMA, NOXA</li>
  <li>Mitochondrial pathway → Cytochrome C release</li>
  <li>Activates caspase 9 → effector caspases</li>
  <li>Programmed cell death</li>
</ul>
</div>
<div class="flow-step-label">OR</div>
<div class="flow-box gold d-print-none" style="text-align:left; color:#ffffff;">
<span class="lbl" style="text-align:center; display:block;">Chronic/replicative stress → SENESCENCE</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>Permanent cell cycle arrest</li>
  <li>Prevents tumourigenesis in pre-malignant lesions</li>
</ul>
</div>
</div>"""

    content = re.sub(r'<div class="flow-h">\s*<div class="flow-box teal d-print-none" style="text-align:center;">\s*<span class="lbl">Reversible damage → ARREST</span>.*?</div>\s*<div class="h-arrow">OR</div>\s*<div class="flow-box rose d-print-none" style="text-align:center;">\s*<span class="lbl">Irreparable damage → APOPTOSIS</span>.*?</div>\s*<div class="h-arrow">OR</div>\s*<div class="flow-box gold d-print-none" style="text-align:center;">\s*<span class="lbl">Chronic/replicative stress → SENESCENCE</span>.*?</div>\s*</div>', new_block_x, content, flags=re.DOTALL)
    
    # Hybridoma step 2
    content = content.replace('<div class="flow-box gold d-print-none">', '<div class="flow-box gold d-print-none" style="color:#ffffff;">')
    return content

fn = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-10\module10_immunochemistry_oncogenesis_X.html"
with open(fn, 'r', encoding='utf-8') as f:
    cont = f.read()

new_cont = fix_x(cont)

with open(fn, 'w', encoding='utf-8') as f:
    f.write(new_cont)
print("Updated X")
