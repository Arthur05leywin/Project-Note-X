import os
import re

file_paths = [
    r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-06\module06_molecular_biology.html",
    r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-06\module06_molecular_biology_X.html"
]

def fix_lac_operon(content):
    content = content.replace(
        '<span class="lbl">CAP site</span>Positive control',
        '<span class="lbl">CAP site</span><br/>Positive control'
    )
    content = content.replace(
        '<span class="lbl">Promoter (P)</span>RNA Pol binds',
        '<span class="lbl">Promoter (P)</span><br/>RNA Pol binds'
    )
    content = content.replace(
        '<span class="lbl">Operator (O)</span>Repressor binds',
        '<span class="lbl">Operator (O)</span><br/>Repressor binds'
    )
    content = content.replace(
        '<span class="lbl">lacZ</span>β-galactosidase',
        '<span class="lbl">lacZ</span><br/>β-galactosidase'
    )
    content = content.replace(
        '<span class="lbl">lacY</span>Permease',
        '<span class="lbl">lacY</span><br/>Permease'
    )
    content = content.replace(
        '<span class="lbl">lacA</span>Transacetylase',
        '<span class="lbl">lacA</span><br/>Transacetylase'
    )
    return content

for fp in file_paths:
    with open(fp, 'r', encoding='utf-8') as f:
        cont = f.read()
    orig = cont
    cont = fix_lac_operon(cont)
    if orig != cont:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(cont)
        print(f"Fixed Lac Operon in {fp}")
