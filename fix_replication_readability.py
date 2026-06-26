import os
import re

file_paths = [
    r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-06\module06_molecular_biology.html",
    r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-06\module06_molecular_biology_X.html"
]

def fix_replication(content):
    # Step 1 - Initiation
    content = re.sub(
        r'<div class="flow-box accent">\s*<span class="lbl">Step 1 — Initiation</span>.*?on both strands\s*</div>',
        """<div class="flow-box accent" style="text-align: left; padding: 16px;">
<span class="lbl" style="margin-bottom: 8px; text-align: center; display: block; font-size: 1.05em;">Step 1 — Initiation</span>
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;"><strong>oriC</strong> recognised by DnaA.</li>
  <li style="margin-bottom: 6px;">Helicase loads (DnaB).</li>
  <li style="margin-bottom: 6px;">Replication bubble forms.</li>
  <li>Primase adds RNA primers on both strands.</li>
</ul>
</div>""",
        content, flags=re.DOTALL
    )

    # Step 2 - Elongation
    content = re.sub(
        r'<div class="flow-box gold">\s*<span class="lbl">Step 2 — Elongation</span>.*?each requires a new\s*primer\s*</div>',
        """<div class="flow-box gold" style="text-align: left; padding: 16px;">
<span class="lbl" style="margin-bottom: 8px; text-align: center; display: block; font-size: 1.05em;">Step 2 — Elongation</span>
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;"><strong>Leading strand:</strong> continuous 5'→3' synthesis (DNA Pol III).</li>
  <li><strong>Lagging strand:</strong> discontinuous — synthesised as <strong>Okazaki fragments</strong> (1000–2000 nt in prokaryotes, 100–200 in eukaryotes), each requires a new primer.</li>
</ul>
</div>""",
        content, flags=re.DOTALL
    )

    # Step 3 - Termination
    content = re.sub(
        r'<div class="flow-box teal">\s*<span class="lbl">Step 3 — Termination</span>.*?interlocked circles\s*</div>',
        """<div class="flow-box teal" style="text-align: left; padding: 16px;">
<span class="lbl" style="margin-bottom: 8px; text-align: center; display: block; font-size: 1.05em;">Step 3 — Termination</span>
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;">Two forks meet at <strong>Ter sequences</strong> (termination sites).</li>
  <li style="margin-bottom: 6px;">Tus protein arrests helicase.</li>
  <li>Topoisomerase II decatenates interlocked circles.</li>
</ul>
</div>""",
        content, flags=re.DOTALL
    )

    return content

for file_path in file_paths:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig = content
        content = fix_replication(content)
        
        if orig != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed replication flowcharts in {file_path}")
        else:
            print(f"No changes made to replication in {file_path}")
