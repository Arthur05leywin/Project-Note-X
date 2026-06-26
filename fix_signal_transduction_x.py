import os
import re

def fix_signal_x(content):
    # 3. PIP2 IP3/DAG Pathway for X version
    pip2_block_x = r"""<div class="flow-h">
<div class="flow-box rose d-print-none"(.*?)>
<span class="lbl">IP₃ \(Inositol trisphosphate\)</span>
            Water-soluble → ER receptor → Ca²⁺ release from ER → ↑ cytosolic Ca²⁺<br/>
            Ca²⁺ \+ Calmodulin → CaM-kinase → enzyme activation \(myosin light chain kinase, phosphorylase kinase\)
          </div>
<div class="h-arrow">\+</div>
<div class="flow-box teal d-print-none"(.*?)>
<span class="lbl">DAG \(Diacylglycerol\)</span>
            Lipid-soluble → stays in membrane → activates <strong>Protein Kinase C \(PKC\)</strong> \(also needs Ca²⁺\)<br/>
            PKC → Ser/Thr phosphorylation of target proteins
          </div>
</div>"""

    new_pip2_x = """<div class="flow-v">
<div class="flow-box rose d-print-none" style="text-align:left; color:#ffffff;">
<span class="lbl" style="text-align:center; display:block;">IP₃ (Inositol trisphosphate)</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>Water-soluble → diffuses to ER receptor</li>
  <li>Ca²⁺ release from ER → ↑ cytosolic Ca²⁺</li>
  <li>Ca²⁺ + Calmodulin → CaM-kinase activation</li>
  <li>Activates myosin light chain kinase, phosphorylase kinase</li>
</ul>
</div>
<div class="flow-step-label" style="text-align:center; font-size:24px; font-weight:bold;">+</div>
<div class="flow-box teal d-print-none" style="text-align:left; color:#ffffff;">
<span class="lbl" style="text-align:center; display:block;">DAG (Diacylglycerol)</span>
<ul style="margin:0; padding-left:20px; font-size:14px; line-height:1.6;">
  <li>Lipid-soluble → remains in cell membrane</li>
  <li>Activates <strong>Protein Kinase C (PKC)</strong> (along with Ca²⁺)</li>
  <li>PKC → Ser/Thr phosphorylation of target proteins</li>
</ul>
</div>
</div>"""

    content = re.sub(pip2_block_x, new_pip2_x, content, flags=re.DOTALL)
    
    # 1. cAMP Second Messenger System
    # We should make sure the boxes are white text
    content = content.replace('<div class="flow-box gold d-print-none">', '<div class="flow-box gold d-print-none" style="color:#ffffff;">')
    content = content.replace('<div class="flow-box teal d-print-none">', '<div class="flow-box teal d-print-none" style="color:#ffffff;">')
    content = content.replace('<div class="flow-box rose d-print-none">', '<div class="flow-box rose d-print-none" style="color:#ffffff;">')

    return content

fn = r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-10\module10_immunochemistry_oncogenesis_X.html"
with open(fn, 'r', encoding='utf-8') as f:
    cont = f.read()

new_cont = fix_signal_x(cont)

with open(fn, 'w', encoding='utf-8') as f:
    f.write(new_cont)
print("Updated PIP2 in X")
