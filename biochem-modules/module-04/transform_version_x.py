import re
import sys

html_path = r'modules/module-04/module04_protein_haemoglobin_X.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- Phase 1: Header Injection ---
print('Applying Phase 1: Header Injection...')
pb_tag = '      <div class="progress-bar"></div>'
if pb_tag not in content:
    print('ERROR: progress-bar div not found!')
    sys.exit(1)

priority_map_revision_mode_html = """      <div class="progress-bar"></div>

      <!-- 📊 EXAM PRIORITY MAP -->
      <div class="big-picture">
        <div class="big-picture-label">📊 EXAM PRIORITY MAP</div>
        <p>Prioritize your revision based on high-yield exam patterns. Focus heavily on Tier 1 and Tier 2 sections for last-day prep.</p>
        <div class="priority-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 15px;">
          <div style="background: rgba(232, 51, 74, 0.08); border: 1px solid rgba(232, 51, 74, 0.3); border-radius: 6px; padding: 12px;">
            <strong style="color: var(--accent); display: block; margin-bottom: 6px;">🔴 TIER 1 (Critical High-Yield)</strong>
            <ul style="list-style: none; padding-left: 0; font-size: 12px; line-height: 1.6;">
              <li>• Sec 01: Protein Structure Levels</li>
              <li>• Sec 04: O₂ Dissociation Curve</li>
              <li>• Sec 05: 2,3-BPG & Bohr Effect</li>
              <li>• Sec 06: HbA · HbS · HbF</li>
              <li>• Sec 08: Bilirubin & Jaundice</li>
            </ul>
          </div>
          <div style="background: rgba(244, 196, 100, 0.08); border: 1px solid rgba(244, 196, 100, 0.3); border-radius: 6px; padding: 12px;">
            <strong style="color: var(--gold); display: block; margin-bottom: 6px;">🟡 TIER 2 (Medium-Yield)</strong>
            <ul style="list-style: none; padding-left: 0; font-size: 12px; line-height: 1.6;">
              <li>• Sec 02: α-Helix & β-Sheet</li>
              <li>• Sec 03: Hb vs Myoglobin</li>
              <li>• Sec 10: Electrophoresis (SPEP)</li>
            </ul>
          </div>
          <div style="background: rgba(107, 203, 119, 0.08); border: 1px solid rgba(107, 203, 119, 0.3); border-radius: 6px; padding: 12px;">
            <strong style="color: var(--green); display: block; margin-bottom: 6px;">🟢 TIER 3 (Low-Yield / Collapsed)</strong>
            <ul style="list-style: none; padding-left: 0; font-size: 12px; line-height: 1.6;">
              <li>• Sec 07: Haem Degradation</li>
              <li>• Sec 09: Plasma Proteins</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 00: 🔥 Last Day Revision Mode -->
      <div class="clinical-box">
        <div class="cbox-title">00: 🔥 Last Day Revision Mode</div>
        <p><strong>Speed-read the high-yield essentials!</strong> The module has been optimized for rapid revision:</p>
        <ul class="checklist" style="margin-top: 8px;">
          <li>All sections tagged with <strong>🔴 TIER 1</strong>, <strong>🟡 TIER 2</strong>, or <strong>🟢 TIER 3</strong> priority badges.</li>
          <li>🟢 TIER 3 sections are automatically collapsed into interactive details tags to prevent cognitive overload.</li>
          <li>High-priority <strong>⚠️ EXAM TRAPS</strong> are injected at critical conceptual points to save you from common mistakes.</li>
          <li>Use standard <strong>Ctrl+P</strong> to print this entire module as an optimized high-contrast PDF with all sections automatically expanded.</li>
        </ul>
      </div>"""

content = content.replace(pb_tag, priority_map_revision_mode_html)

# --- Phase 2: Core Tagging & Traps (H2 badge replacement) ---
print('Applying Phase 2: H2 badge tagging...')
h2_replacements = {
    r'<h2>Levels of Protein <em>Structure</em></h2>': r'<h2>Levels of Protein <em>Structure</em> <span class="badge badge-rls">🔴 TIER 1</span></h2>',
    r'<h2><em>α-Helix</em> & β-Pleated Sheet</h2>': r'<h2><em>α-Helix</em> & β-Pleated Sheet <span class="badge badge-fav">🟡 TIER 2</span></h2>',
    r'<h2>Haemoglobin <em>vs</em> Myoglobin</h2>': r'<h2>Haemoglobin <em>vs</em> Myoglobin <span class="badge badge-fav">🟡 TIER 2</span></h2>',
    r'<h2>O₂ Dissociation <em>Curve</em></h2>': r'<h2>O₂ Dissociation <em>Curve</em> <span class="badge badge-rls">🔴 TIER 1</span></h2>',
    r'<h2><em>2,3-BPG</em> & Bohr Effect</h2>': r'<h2><em>2,3-BPG</em> & Bohr Effect <span class="badge badge-rls">🔴 TIER 1</span></h2>',
    r'<h2>HbA · HbS · <em>HbF</em></h2>': r'<h2>HbA · HbS · <em>HbF</em> <span class="badge badge-rls">🔴 TIER 1</span></h2>',
    r'<h2>Haem <em>Degradation</em></h2>': r'<h2>Haem <em>Degradation</em> <span class="badge badge-new">🟢 TIER 3</span></h2>',
    r'<h2>Bilirubin & <em>Jaundice</em></h2>': r'<h2>Bilirubin & <em>Jaundice</em> <span class="badge badge-rls">🔴 TIER 1</span></h2>',
    r'<h2>Plasma <em>Proteins</em></h2>': r'<h2>Plasma <em>Proteins</em> <span class="badge badge-new">🟢 TIER 3</span></h2>',
    r'<h2>Serum Protein <em>Electrophoresis</em></h2>': r'<h2>Serum Protein <em>Electrophoresis</em> <span class="badge badge-fav">🟡 TIER 2</span></h2>',
    r'<h2>Viva & Exam <em>Q&A</em></h2>': r'<h2>Viva & Exam <em>Q&A</em> <span class="badge badge-rls">🔴 TIER 1</span></h2>',
    r'<h2>Essay Question <em>Templates</em></h2>': r'<h2>Essay Question <em>Templates</em> <span class="badge badge-rls">🔴 TIER 1</span></h2>',
}

for original, replacement in h2_replacements.items():
    if original not in content:
        print(f'WARNING: H2 header not found: {original}')
    else:
        content = content.replace(original, replacement)

# --- Phase 2: Exam Traps Injection (strictly in key-fact containers) ---
print('Applying Phase 2: Injecting Exam Traps...')

s1_old = '        <div class="warn-box">\n          <span\n            ><strong>Denaturation</strong> disrupts 2°, 3°, 4° structure but NOT\n            1° (peptide bonds remain intact). Renaturation is possible if 1° is\n            intact.</span\n          >\n        </div>\n      </div>'
s1_trap = """        <div class="warn-box">
          <span
            ><strong>Denaturation</strong> disrupts 2°, 3°, 4° structure but NOT
            1° (peptide bonds remain intact). Renaturation is possible if 1° is
            intact.</span
          >
        </div>

        <div class="key-fact">
          <div class="key-fact-icon">⚠️</div>
          <div class="key-fact-text">
            <strong>EXAM TRAP:</strong> Denaturation disrupts 2°, 3°, and 4° structures by breaking non-covalent bonds (and disulphide bonds), but it <strong>NEVER disrupts the 1° structure</strong> (covalent peptide bonds). Always state this explicitly to secure full marks!
          </div>
        </div>
      </div>"""
if s1_old in content:
    content = content.replace(s1_old, s1_trap)
else:
    print('WARNING: Section 1 end string not found!')

s4_old = '            <div class="keypoint" style="margin-top: 8px">\n              Left shift = <strong>Hb grabs O₂ but won\'t release it</strong>.\n              Dangerous in CO poisoning.\n            </div>\n          </div>\n        </div>\n      </div>'
s4_trap = """            <div class="keypoint" style="margin-top: 8px">
              Left shift = <strong>Hb grabs O₂ but won't release it</strong>.
              Dangerous in CO poisoning.
            </div>
          </div>
        </div>

        <div class="key-fact">
          <div class="key-fact-icon">⚠️</div>
          <div class="key-fact-text">
            <strong>EXAM TRAP:</strong> A <strong>shift to the RIGHT</strong> means <strong>DECREASED oxygen affinity</strong> (easier oxygen unloading, higher P₅₀). A shift to the LEFT means INCREASED affinity (harder unloading, lower P₅₀). Confusing these is the most common reason for losing marks!
          </div>
        </div>
      </div>"""
if s4_old in content:
    content = content.replace(s4_old, s4_trap)
else:
    print('WARNING: Section 4 end string not found!')

s6_old = '              <li>\n                <span>Clinical:</span> After birth, γ→β switch occurs; HbF → HbA\n                by 6 months. Persistence of HbF (HPFH) is actually protective in\n                sickle cell and β-thalassaemia\n              </li>\n            </ol>\n          </div>\n        </div>\n      </div>'
s6_trap = """              <li>
                <span>Clinical:</span> After birth, γ→β switch occurs; HbF → HbA
                by 6 months. Persistence of HbF (HPFH) is actually protective in
                sickle cell and β-thalassaemia
              </li>
            </ol>
          </div>
        </div>

        <div class="key-fact">
          <div class="key-fact-icon">⚠️</div>
          <div class="key-fact-text">
            <strong>EXAM TRAP:</strong> In Sickle Cell Anaemia (HbS), the mutation is strictly a substitution of <strong>Valine (hydrophobic) for Glutamic Acid (polar)</strong> at <strong>position 6 of the β-globin chain</strong> (not the α-chain). Writing α-chain or wrong amino acids results in immediate zero for that section!
          </div>
        </div>
      </div>"""
if s6_old in content:
    content = content.replace(s6_old, s6_trap)
else:
    print('WARNING: Section 6 end string not found!')

s8_old = '          <div class="keypoint" style="margin-top: 8px">\n            <strong>Total bilirubin = Direct + Indirect.</strong> Normal: Total\n            &lt;1 mg/dL, Direct &lt;0.3 mg/dL.\n          </div>\n        </div>\n      </div>'
s8_trap = """          <div class="keypoint" style="margin-top: 8px">
            <strong>Total bilirubin = Direct + Indirect.</strong> Normal: Total
            &lt;1 mg/dL, Direct &lt;0.3 mg/dL.
          </div>
        </div>

        <div class="key-fact">
          <div class="key-fact-icon">⚠️</div>
          <div class="key-fact-text">
            <strong>EXAM TRAP:</strong> Do not mix up the **Van den Bergh reaction** results! <strong>Pre-hepatic (hemolytic) jaundice</strong> gives an **Indirect Positive** (water-insoluble unconjugated bilirubin). <strong>Post-hepatic (obstructive) jaundice</strong> gives a **Direct Positive** (water-soluble conjugated bilirubin). <strong>Hepatic jaundice</strong> gives a **Biphasic** response.
          </div>
        </div>
      </div>"""
if s8_old in content:
    content = content.replace(s8_old, s8_trap)
else:
    print('WARNING: Section 8 end string not found!')

# --- Phase 3: Low-Yield Collapse ---
print('Applying Phase 3: Collapsing low-yield sections...')
s7_pattern = r'(<div id="s7">\s*<div class="section-header">.*?</h2>\s*</div>)(.*?)(</div>\s*<div class="divider">)'
def wrap_s7(match):
    return f'{match.group(1)}\n      <details>\n        <summary>🟢 TIER 3: Low-Yield Content — Click to expand Haem Degradation pathway</summary>\n{match.group(2)}\n      </details>\n{match.group(3)}'
if re.search(s7_pattern, content, re.DOTALL):
    content = re.sub(s7_pattern, wrap_s7, content, flags=re.DOTALL)
else:
    print('WARNING: Section 7 boundary pattern not found!')

s9_pattern = r'(<div id="s9">\s*<div class="section-header">.*?</h2>\s*</div>)(.*?)(</div>\s*<div class="divider">)'
def wrap_s9(match):
    return f'{match.group(1)}\\n      <details>\\n        <summary>🟢 TIER 3: Low-Yield Content — Click to expand Plasma Proteins functions and properties</summary>\\n{match.group(2)}\\n      </details>\\n{match.group(3)}'
if re.search(s9_pattern, content, re.DOTALL):
    content = re.sub(s9_pattern, wrap_s9, content, flags=re.DOTALL)
else:
    print('WARNING: Section 9 boundary pattern not found!')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('SUCCESS: HTML transformations applied to Version X!')
