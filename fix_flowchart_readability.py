import os
import re

file_paths = [
    r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-06\module06_molecular_biology.html",
    r"c:\Users\sayan\Downloads\biochem Note X\biochem-modules\module-06\module06_molecular_biology_X.html"
]

def fix_mrna(content):
    # Eukaryotic mRNA Processing
    orig_mrna_str = """<div class="flow-box accent">
<span class="lbl">Step 1 — 5' Capping (co-transcriptional)</span>
                7-methylguanosine cap added to 5' end via 5'–5' triphosphate
                bridge<br/>
<span class="sub">Protects from exonucleases; aids ribosome binding; required
                  for translation</span>
</div>
<div class="flow-step-label">↓</div>
<div class="flow-box gold">
<span class="lbl">Step 2 — 3' Polyadenylation</span>
                Cleavage ~20 nt after AAUAAA signal → Poly-A polymerase adds
                200–250 A residues<br/>
<span class="sub">Stabilises mRNA; aids nuclear export; facilitates
                  translation</span>
</div>
<div class="flow-step-label">↓</div>
<div class="flow-box teal">
<span class="lbl">Step 3 — RNA Splicing (Intron removal)</span>
                Spliceosome (snRNPs: U1,U2,U4,U5,U6) removes introns via 2-step
                transesterification<br/>
<span class="sub">Lariat intermediate formed. Exons join. Alternative splicing
                  → protein diversity</span>
</div>"""

    # We need to find this using regex because spacing might vary.
    # It's better to replace the exact blocks or use regex.
    
    # Step 1
    content = re.sub(
        r'<div class="flow-box accent">\s*<span class="lbl">Step 1 — 5\' Capping \(co-transcriptional\)</span>.*?<span class="sub">Protects from exonucleases; aids ribosome binding; required\s*for translation</span>\s*</div>',
        """<div class="flow-box accent" style="text-align: left; padding: 16px;">
<span class="lbl" style="margin-bottom: 8px; text-align: center; display: block; font-size: 1.05em;">Step 1 — 5' Capping (co-transcriptional)</span>
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;"><strong>Action:</strong> 7-methylguanosine cap added to 5' end via 5'–5' triphosphate bridge.</li>
  <li><strong>Function:</strong> Protects from exonucleases; aids ribosome binding; required for translation.</li>
</ul>
</div>""",
        content, flags=re.DOTALL
    )

    # Step 2
    content = re.sub(
        r'<div class="flow-box gold">\s*<span class="lbl">Step 2 — 3\' Polyadenylation</span>.*?<span class="sub">Stabilises mRNA; aids nuclear export; facilitates\s*translation</span>\s*</div>',
        """<div class="flow-box gold" style="text-align: left; padding: 16px;">
<span class="lbl" style="margin-bottom: 8px; text-align: center; display: block; font-size: 1.05em;">Step 2 — 3' Polyadenylation</span>
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;"><strong>Action:</strong> Cleavage ~20 nt after AAUAAA signal → Poly-A polymerase adds 200–250 A residues.</li>
  <li><strong>Function:</strong> Stabilises mRNA; aids nuclear export; facilitates translation.</li>
</ul>
</div>""",
        content, flags=re.DOTALL
    )

    # Step 3
    content = re.sub(
        r'<div class="flow-box teal">\s*<span class="lbl">Step 3 — RNA Splicing \(Intron removal\)</span>.*?<span class="sub">Lariat intermediate formed\. Exons join\. Alternative splicing\s*→ protein diversity</span>\s*</div>',
        """<div class="flow-box teal" style="text-align: left; padding: 16px;">
<span class="lbl" style="margin-bottom: 8px; text-align: center; display: block; font-size: 1.05em;">Step 3 — RNA Splicing (Intron removal)</span>
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;"><strong>Action:</strong> Spliceosome (snRNPs: U1, U2, U4, U5, U6) removes introns via 2-step transesterification.</li>
  <li><strong>Result:</strong> Lariat intermediate formed. Exons join. Alternative splicing → protein diversity.</li>
</ul>
</div>""",
        content, flags=re.DOTALL
    )
    
    return content


def fix_translation(content):
    # Prokaryotic translation
    # Initiation
    content = re.sub(
        r'<div class="flow-box accent">\s*<span class="lbl">INITIATION</span>.*?\(unique to\s*initiation\)\s*</div>',
        """<div class="flow-box accent" style="text-align: left; padding: 16px;">
<span class="lbl" style="margin-bottom: 8px; text-align: center; display: block; font-size: 1.05em;">INITIATION</span>
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;">Uses GTP + Initiation Factors (IF1, IF2, IF3).</li>
  <li style="margin-bottom: 6px;">30S + mRNA (Shine-Dalgarno sequence binds 16S rRNA) + fMet-tRNA → <strong>30S initiation complex</strong>.</li>
  <li style="margin-bottom: 6px;">+ 50S subunit → <strong>70S initiation complex</strong>.</li>
  <li>fMet-tRNA enters P site directly (unique to initiation).</li>
</ul>
</div>""",
        content, flags=re.DOTALL
    )

    # Elongation
    content = re.sub(
        r'<div class="flow-box gold">\s*<span class="lbl">ELONGATION</span>\s*— 3 steps per cycle, each costs GTP<br/>\s*<strong>1\. Decoding:</strong> EF-Tu·GTP delivers aminoacyl-tRNA\s*to A site → codon-anticodon check<br/>\s*<strong>2\. Peptide bond formation:</strong> Peptidyl transferase\s*\(23S rRNA — ribozyme!\) transfers growing chain\s*from P-tRNA to A-tRNA<br/>\s*<strong>3\. Translocation:</strong> EF-G·GTP moves ribosome 1\s*codon \(3\'→5\' on mRNA\) → A→P→E shift\s*</div>',
        """<div class="flow-box gold" style="text-align: left; padding: 16px;">
<span class="lbl" style="margin-bottom: 8px; text-align: center; display: block; font-size: 1.05em;">ELONGATION</span>
<div style="text-align: center; margin-bottom: 10px; font-size: 13px; opacity: 0.9;">3 steps per cycle, each costs GTP</div>
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;"><strong>1. Decoding:</strong> EF-Tu·GTP delivers aminoacyl-tRNA to A site → codon-anticodon check.</li>
  <li style="margin-bottom: 6px;"><strong>2. Peptide bond formation:</strong> Peptidyl transferase (23S rRNA — ribozyme!) transfers growing chain from P-tRNA to A-tRNA.</li>
  <li><strong>3. Translocation:</strong> EF-G·GTP moves ribosome 1 codon (3'→5' on mRNA) → A→P→E shift.</li>
</ul>
</div>""",
        content, flags=re.DOTALL
    )
    
    # Termination
    content = re.sub(
        r'<div class="flow-box teal">\s*<span class="lbl">TERMINATION</span>.*?EF-G \+ IF3\s*</div>',
        """<div class="flow-box teal" style="text-align: left; padding: 16px;">
<span class="lbl" style="margin-bottom: 8px; text-align: center; display: block; font-size: 1.05em;">TERMINATION</span>
<ul style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.6; color: inherit; opacity: 0.9;">
  <li style="margin-bottom: 6px;">Release Factors (RF1 recognises UAA/UAG; RF2 recognises UAA/UGA; RF3 is GTPase) bind A site.</li>
  <li style="margin-bottom: 6px;">Peptidyl transferase catalyses hydrolysis → polypeptide released.</li>
  <li>Ribosome dissociates: RRF (ribosome recycling factor) + EF-G + IF3.</li>
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
        content = fix_mrna(content)
        content = fix_translation(content)
        
        if orig != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed flowcharts in {file_path}")
        else:
            print(f"No changes made to {file_path}")
