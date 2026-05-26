import os
import re

# File Paths
ROOT_DIR = r"c:\Users\sayan\Downloads\biochem Note X"
MASTER_HTML = os.path.join(ROOT_DIR, "modules", "module-03", "lipid_metabolism_notes.html")
REVISION_HTML = os.path.join(ROOT_DIR, "modules", "module-03", "lipid_metabolism_notes_X.html")

# Carnitine Shuttle SVG Diagram
CARNITINE_SVG = """
      <div class="graph-box">
        <div class="graph-label">FIG 3.1: NATIVE CARNITINE SHUTTLE &amp; RECIPROCAL REGULATION BY MALONYL-CoA</div>
        <div style="text-align: center; margin: 20px 0;">
          <svg viewBox="0 0 800 350" width="100%" height="auto" style="background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); max-width: 100%;">
            <defs>
              <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--accent)" />
              </marker>
              <marker id="arrow-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--accent2)" />
              </marker>
              <marker id="arrow-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--blue)" />
              </marker>
            </defs>
            <style>
              .shuttle-text { font-family: 'IBM Plex Mono', monospace; font-size: 11px; fill: var(--muted); }
              .title-text { font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 600; fill: var(--white); }
              .sub-text { font-size: 10px; fill: var(--muted); }
              .membrane { fill: rgba(255,255,255,0.03); stroke: var(--border2); stroke-dasharray: 4,4; }
              .protein { fill: var(--surface3); stroke: var(--accent); stroke-width: 2; }
            </style>
            <rect x="0" y="0" width="220" height="40" fill="rgba(0,0,0,0.2)" />
            <text x="110" y="25" text-anchor="middle" class="title-text" fill="var(--white)">CYTOSOL</text>
            <rect x="220" y="0" width="180" height="40" fill="rgba(0,0,0,0.3)" />
            <text x="310" y="25" text-anchor="middle" class="title-text" fill="var(--accent2)">INTERMEMBRANE SPACE</text>
            <rect x="400" y="0" width="400" height="40" fill="rgba(0,0,0,0.2)" />
            <text x="600" y="25" text-anchor="middle" class="title-text" fill="var(--accent)">MITOCHONDRIAL MATRIX</text>
            <rect x="210" y="40" width="20" height="310" class="membrane" fill="rgba(255,255,255,0.05)" stroke="var(--border2)" />
            <text x="220" y="325" text-anchor="middle" class="shuttle-text" transform="rotate(-90 220 325)" style="font-size: 10px;">OUTER MEMBRANE (OMM)</text>
            <rect x="390" y="40" width="20" height="310" class="membrane" fill="rgba(255,255,255,0.05)" stroke="var(--border2)" />
            <text x="400" y="325" text-anchor="middle" class="shuttle-text" transform="rotate(-90 400 325)" style="font-size: 10px;">INNER MEMBRANE (IMM)</text>
            <rect x="15" y="80" width="85" height="35" rx="5" fill="var(--surface3)" stroke="var(--border)" />
            <text x="57" y="102" text-anchor="middle" class="title-text" style="font-size: 11px;">Fatty Acid</text>
            <path d="M 100 97.5 L 140 97.5" stroke="var(--accent2)" stroke-width="2" marker-end="url(#arrow-green)" />
            <text x="120" y="80" text-anchor="middle" class="shuttle-text" style="font-size: 8px; fill: var(--accent2);">Thiokinase</text>
            <text x="120" y="90" text-anchor="middle" class="shuttle-text" style="font-size: 7px;">ATP &rarr; AMP + 2Pi</text>
            <rect x="145" y="80" width="60" height="35" rx="5" fill="var(--surface3)" stroke="var(--accent2)" />
            <text x="175" y="102" text-anchor="middle" class="title-text" style="font-size: 11px; fill: var(--accent2);">Acyl-CoA</text>
            <ellipse cx="220" cy="130" rx="20" ry="30" class="protein" stroke="var(--accent)" />
            <text x="220" y="133" text-anchor="middle" class="title-text" style="font-size: 10px; fill: var(--white);">CPT-I</text>
            <path d="M 195 115 C 205 115, 205 125, 210 125" stroke="var(--accent)" stroke-width="1.5" fill="none" marker-end="url(#arrow)" />
            <path d="M 175 195 C 190 195, 200 145, 210 140" stroke="var(--blue)" stroke-width="1.5" fill="none" marker-end="url(#arrow-blue)" />
            <text x="155" y="210" class="title-text" style="font-size: 11px; fill: var(--blue);">Carnitine</text>
            <path d="M 230 130 C 240 130, 245 130, 255 140" stroke="var(--accent2)" stroke-width="1.5" fill="none" marker-end="url(#arrow-green)" />
            <text x="260" y="155" class="title-text" style="font-size: 11px; fill: var(--accent2);">Acyl-Carnitine</text>
            <text x="260" y="167" class="sub-text">Intermembrane Space</text>
            <path d="M 225 115 C 215 115, 195 140, 185 155" stroke="var(--orange)" stroke-width="1.5" fill="none" marker-end="url(#arrow)" />
            <text x="180" y="170" class="shuttle-text" style="fill: var(--orange); font-size: 10px;">CoA-SH</text>
            <rect x="50" y="145" width="85" height="35" rx="5" fill="rgba(232, 74, 122, 0.1)" stroke="var(--accent3)" stroke-width="1.5" />
            <text x="92" y="162" text-anchor="middle" class="title-text" style="font-size: 10px; fill: var(--accent3);">Malonyl-CoA</text>
            <text x="92" y="173" text-anchor="middle" class="sub-text" style="fill: var(--accent3);">[Synthesis Active]</text>
            <path d="M 135 162 L 205 142" stroke="var(--accent3)" stroke-width="2" stroke-dasharray="3,3" fill="none" marker-end="url(#arrow)" />
            <circle cx="170" cy="152" r="7" fill="var(--bg)" stroke="var(--accent3)" stroke-width="1.5" />
            <text x="170" y="156" text-anchor="middle" class="title-text" style="font-size: 10px; fill: var(--accent3); font-weight: bold;">&times;</text>
            <text x="170" y="142" text-anchor="middle" class="shuttle-text" style="fill: var(--accent3); font-size: 8px;">BLOCKS CPT-I</text>
            <ellipse cx="400" cy="180" rx="20" ry="40" class="protein" stroke="var(--accent2)" />
            <text x="400" y="175" text-anchor="middle" class="title-text" style="font-size: 9px; fill: var(--white);">Trans-</text>
            <text x="400" y="187" text-anchor="middle" class="title-text" style="font-size: 9px; fill: var(--white);">locase</text>
            <path d="M 315 170 C 340 170, 370 175, 385 175" stroke="var(--accent2)" stroke-width="2" fill="none" marker-end="url(#arrow-green)" />
            <path d="M 415 175 C 430 175, 460 170, 485 170" stroke="var(--accent2)" stroke-width="2" fill="none" marker-end="url(#arrow-green)" />
            <text x="495" y="165" class="title-text" style="font-size: 11px; fill: var(--accent2);">Acyl-Carnitine (Matrix)</text>
            <path d="M 485 220 C 450 220, 425 200, 415 195" stroke="var(--blue)" stroke-width="1.5" stroke-dasharray="3,1" fill="none" marker-end="url(#arrow-blue)" />
            <path d="M 385 195 C 360 200, 310 220, 275 220" stroke="var(--blue)" stroke-width="1.5" stroke-dasharray="3,1" fill="none" marker-end="url(#arrow-blue)" />
            <text x="495" y="225" class="title-text" style="font-size: 11px; fill: var(--blue);">Carnitine</text>
            <rect x="430" y="240" width="55" height="50" rx="5" fill="var(--surface3)" stroke="var(--accent)" stroke-width="2" />
            <text x="457.5" y="270" text-anchor="middle" class="title-text" style="font-size: 11px; fill: var(--accent);">CPT-II</text>
            <path d="M 520 185 C 500 205, 470 230, 465 240" stroke="var(--accent2)" stroke-width="1.5" fill="none" marker-end="url(#arrow-green)" />
            <path d="M 550 280 L 490 280" stroke="var(--orange)" stroke-width="1.5" fill="none" marker-end="url(#arrow)" />
            <text x="555" y="284" class="title-text" style="font-size: 11px; fill: var(--orange);">CoA-SH</text>
            <path d="M 445 290 C 445 310, 520 310, 550 310" stroke="var(--accent)" stroke-width="2" fill="none" marker-end="url(#arrow)" />
            <rect x="555" y="292" width="105" height="35" rx="5" fill="var(--surface3)" stroke="var(--accent)" stroke-width="1.5" />
            <text x="607.5" y="313" text-anchor="middle" class="title-text" style="font-size: 11px; fill: var(--accent);">Fatty Acyl-CoA</text>
            <text x="607.5" y="323" text-anchor="middle" class="sub-text" style="fill: var(--accent2);">&beta;-Oxidation Proper</text>
            <path d="M 457.5 240 C 457.5 210, 500 215, 510 215" stroke="var(--blue)" stroke-width="1.5" fill="none" marker-end="url(#arrow-blue)" />
          </svg>
        </div>
      </div>
"""

def remaster_master():
    print("[MASTER] Loading masterclass notes...")
    with open(MASTER_HTML, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean up ampersand inside Caffeine image src attribute
    content = content.replace('src="../../Caffeine%20%26%20Cadaver.jpg"', 'src="../../Caffeine &amp; Cadaver.jpg"')
    content = content.replace('src="../../Caffeine & Cadaver.jpg"', 'src="../../Caffeine &amp; Cadaver.jpg"')
    content = content.replace('alt="Caffeine &amp;amp; Cadaver"', 'alt="Caffeine &amp; Cadaver"')

    # 2. Inject native Carnitine Shuttle SVG right under the Carnitine Shuttle flowchart-container
    shuttle_flowchart_end = """        </div>
      </div>"""
    
    # We will search for CPT-I rate limiting step key-fact and place SVG right before or after it
    cpt_key_fact_search = """      <div class="key-fact">
        <span class="key-fact-icon">⭐</span>
        <div class="key-fact-text">
          <strong>CPT-I is the rate-limiting step</strong>"""
    
    if cpt_key_fact_search in content and "FIG 3.1: NATIVE CARNITINE SHUTTLE" not in content:
        print("[MASTER] Injecting Carnitine Shuttle SVG...")
        content = content.replace(cpt_key_fact_search, CARNITINE_SVG + "\n" + cpt_key_fact_search)

    # 3. Add textbook-grade expansions right inside β-Oxidation Proper section
    beta_proper_anchor = """        <div class="stat-row">
          <div class="stat-pill orange">
            <strong>Palmitate (C16):</strong><br />7 rounds of β-oxidation<br />8
            Acetyl-CoA produced
          </div>
          <div class="stat-pill purple">
            <strong>Per round:</strong><br />1 FADH₂ + 1 NADH<br />= 4 ATP
          </div>
          <div class="stat-pill teal">
            <strong>Net ATP (C16):</strong><br />106 ATP total<br />(−2 for
            activation)
          </div>
        </div>
      </div>"""
    
    textbook_expansion_beta = """
      <!-- §2.1 CONCEPTUAL EXPANSION: METABOLIC ENERGETICS & SPECIAL OXIDATIONS -->
      <div class="big-picture">
        <div class="big-picture-label">📘 Lynen's Spiral (4-Step Cycle) &amp; Molecular Energetics</div>
        <p>
          β-Oxidation of fatty acids is also called <strong>Lynen's spiral</strong>. Long-chain fatty acids are sequentially degraded in a repeating 4-step cyclical spiral process to release 2-carbon Acetyl-CoA units. 
        </p>
        <p>
          <strong>Step 1: Dehydrogenation (FAD-dependent)</strong><br />
          Acyl-CoA is oxidized by mitochondrial membrane-bound <strong>Acyl-CoA Dehydrogenase</strong> to form trans-&Delta;&sup2;-Enoyl-CoA. Electrons are transferred to FAD &rarr; FADH₂ which feeds into the electron transport chain (yielding <strong>1.5 ATP</strong>).
        </p>
        <p>
          <strong>Step 2: Hydration</strong><br />
          Hydration of the double bond by <strong>Enoyl-CoA Hydratase</strong> adds water across the trans double bond, yielding L-3-Hydroxyacyl-CoA.
        </p>
        <p>
          <strong>Step 3: Dehydrogenation (NAD-dependent)</strong><br />
          L-3-Hydroxyacyl-CoA is oxidized by <strong>3-Hydroxyacyl-CoA Dehydrogenase</strong> to yield 3-Ketoacyl-CoA, generating NADH + H&sup2; (yielding <strong>2.5 ATP</strong> in ETC).
        </p>
        <p>
          <strong>Step 4: Thiolytic Cleavage (Thiolase)</strong><br />
          Cleavage of 3-Ketoacyl-CoA by <strong>Thiolase (needs CoASH)</strong> releases 1 molecule of <strong>Acetyl-CoA</strong> and a Fatty Acyl-CoA molecule that is <strong>2 carbons shorter</strong>. The shortened Fatty Acyl-CoA re-enters the cycle.
        </p>
        
        <div class="key-fact">
          <span class="key-fact-icon">🔢</span>
          <div class="key-fact-text">
            <strong>Pathway Energetics Calculations:</strong><br />
            &bull; <strong>Acetyl-CoA Yield</strong> = n / 2 (each enters TCA cycle, yielding 10 ATP).<br />
            &bull; <strong>Number of Cycles</strong> = (n / 2) - 1 (each cycle generates 1 FADH₂ + 1 NADH = 4 ATP).<br />
            &bull; <strong>Activation Cost</strong> = 2 ATP equivalents (Thiokinase reaction consumes 1 ATP &rarr; AMP + PPi, followed by immediate pyrophosphatase hydrolysis).<br />
            &bull; <strong>Palmitate (16C)</strong>: 8 Acetyl-CoA (80 ATP) + 7 cycles (28 ATP) = 108 ATP. Net = <strong>106 ATP</strong>.<br />
            &bull; <strong>Stearate (18C)</strong>: 9 Acetyl-CoA (90 ATP) + 8 cycles (32 ATP) = 122 ATP. Net = <strong>120 ATP</strong>.
          </div>
        </div>
      </div>

      <div class="big-picture">
        <div class="big-picture-label">💡 Specialty Fatty Acid Oxidations</div>
        <p>
          <strong>1. Odd-Chain Fatty Acid Oxidation:</strong><br />
          Odd-chain fatty acids undergo normal &beta;-oxidation until the final thiolytic cleavage yields one molecule of 3-carbon <strong>Propionyl-CoA</strong> instead of two Acetyl-CoAs. 
          Propionyl-CoA &rarr; <strong>D-Methylmalonyl-CoA</strong> (via Biotin-dependent <em>Propionyl-CoA Carboxylase</em>, consuming ATP and CO&sup2;) &rarr; L-Methylmalonyl-CoA &rarr; <strong>Succinyl-CoA</strong> (via Vitamin B12-dependent <em>Methylmalonyl-CoA Mutase</em>) &rarr; enters TCA cycle.<br />
          <strong style="color: var(--accent3)">&bull; Clinical Correlate:</strong> Vitamin B12 deficiency or Mutase enzyme deficiency causes accumulation of methylmalonic acid, leading to severe <strong>Methylmalonic Aciduria</strong>.
        </p>
        <p>
          <strong>2. Peroxisomal &beta;-Oxidation (VLCFA Oxidation):</strong><br />
          Fatty acids with carbon chains &ge; C&sup2;&sup2; cannot enter the carnitine shuttle and must be oxidized in peroxisomes. The first dehydrogenation step uses <strong>Acyl-CoA Oxidase</strong>, which transfers electrons directly to O&sup2; &rarr; <strong>Hydrogen Peroxide (H&sup2;O&sup2;)</strong> (does not generate ATP). H&sup2;O&sup2; is broken down by <strong>Catalase</strong> to yield nascent oxygen [O] to kill bacteria or convert to H&sup2;O and O&sup2;.<br />
          <strong style="color: var(--accent3)">&bull; Zellweger Syndrome:</strong> Congenital defect in peroxisomal biogenesis. Causes VLCFA accumulation in tissues, severe hypotonia, hepatomegaly, craniofacial dysmorphism, myelin destruction, and death in infancy. Adrenoleukodystrophy (ALD) is an X-linked defect in peroxisomal membrane VLCFA transporter ABCD1.
        </p>
        <p>
          <strong>3. Unsaturated Fatty Acid Oxidation:</strong><br />
          Naturally occurring double bonds are in the <strong>cis</strong> configuration, whereas &beta;-oxidation enzymes only recognize the <strong>trans</strong> configuration. 
          Oxidation requires two additional enzymes: <strong>Isomerase</strong> (converts cis-&Delta;&sup3;-Enoyl-CoA to trans-&Delta;&sup2;-Enoyl-CoA) and <strong>Reductase</strong> (removes double bonds in polyunsaturated fatty acids).<br />
          <strong style="color: var(--accent3)">&bull; Energetics:</strong> Bypasses the initial FADH₂-generating Acyl-CoA dehydrogenase step, resulting in a **lower energy yield** compared to saturated fatty acids.
        </p>
      </div>
"""
    if beta_proper_anchor in content and "CONCEPTUAL EXPANSION: METABOLIC ENERGETICS" not in content:
        print("[MASTER] Injecting Lynen's spiral and specialty oxidations...")
        content = content.replace(beta_proper_anchor, beta_proper_anchor + "\n" + textbook_expansion_beta)

    # 4. Inject DKA vs Fasting Ketosis comparison in Section 3
    ketosis_box_search = """      <div class="clinical-box">
        <div class="clinical-label">🩺 ...</div>"""
    
    # Let's search for "Starvation ketosis" inside DKA clinical box
    starvation_ketosis_search = """          <li>
            <strong>Starvation ketosis:</strong> Mild — OAA diverted to GNG →
            Acetyl-CoA cannot enter TCA → ketogenesis. Controlled, compensated.
            pH usually normal.
          </li>"""
    
    detailed_dka_ketosis = """          <li>
            <strong>Fasting Ketosis (Physiological / Safe):</strong><br />
            An overnight fast triggers a decrease in glucose &rarr; insulin falls, glucagon rises &rarr; activates Hormone Sensitive Lipase (HSL) to trigger mild adipose lipolysis &rarr; Free Fatty Acids (FFA) are released and transported to the liver &rarr; Liver &beta;-oxidation increases, generating Acetyl-CoA. At the same time, Gluconeogenesis is activated, depleting Oxaloacetate (OAA) &rarr; Acetyl-CoA is diverted from TCA to Ketogenesis.<br />
            <strong style="color: var(--accent2)">&bull; Safety Mechanism:</strong> A **small amount of circulating insulin remains**, which acts as a molecular brake on lipolysis, preventing it from spiraling out of control. Ketones remain low (&lt; 1 mg/dL) and blood pH remains stable and fully compensated.
          </li>
          <li>
            <strong>Diabetic Ketoacidosis (DKA - Pathological / Unsafe):</strong><br />
            Seen in uncontrolled Type 1 Diabetes Mellitus. Insulin is **completely absent (zero insulin)** &rarr; lipolysis is thrown into massive, unchecked overdrive &rarr; FFA flooded into the liver &rarr; Acetyl-CoA production explodes. Because insulin is zero, glucose cannot enter cells, making the liver think the body is starving &rarr; Gluconeogenesis is extremely active, depleting OAA completely. Acetyl-CoA cannot enter TCA at all and is converted entirely to Ketones.<br />
            <strong style="color: var(--accent3)">&bull; Clinical Presentation:</strong> Acidic ketone bodies accumulate massively &rarr; Bicarbonate buffer system is overwhelmed &rarr; blood pH drops, causing severe **High Anion Gap Metabolic Acidosis**. Patients present with **Kussmaul breathing** (deep, rapid breathing to blow off CO&sup2;), fruity acetone breath, profound dehydration, and coma.<br />
            <strong style="color: var(--accent2)">&bull; Diagnostic &amp; Treatment:</strong> **Gerhardt's Test** is positive for primary acetoacetate. Treatment requires immediate administration of (1) **Glucose + Insulin** (insulin reverses lipolysis) and (2) **NaHCO&sup3;&sup2;** with aggressive electrolyte/fluid resuscitation.
          </li>"""
    
    if starvation_ketosis_search in content:
        print("[MASTER] Injecting Fasting Ketosis vs DKA comparison...")
        content = content.replace(starvation_ketosis_search, detailed_dka_ketosis)

    # 5. Inject Fatty Acid Synthesis (De Novo Lipogenesis) details in Section 4
    acc_key_fact_search = """      <div class="key-fact">
        <span class="key-fact-icon">⭐</span>
        <div class="key-fact-text">
          <strong>ACC (Acetyl-CoA Carboxylase)</strong>"""
    
    fas_detailed_expansion = """
      <!-- §4.1 DE NOVO LIPOGENESIS ENZYME MACHINERY: ACC & FAS COMPLEX -->
      <div class="big-picture">
        <div class="big-picture-label">🔬 Cytoplasmic Shuttle &amp; ACC Regulation</div>
        <p>
          De novo fatty acid synthesis occurs in the <strong>cytosol</strong> of the **liver and lactating mammary glands**. Mitochondrial Acetyl-CoA (produced from pyruvate or &beta;-oxidation) cannot cross the inner mitochondrial membrane. 
        </p>
        <p>
          <strong>Citrate Shuttle:</strong><br />
          Acetyl-CoA is condensed with Oxaloacetate to form <strong>Citrate</strong> (via Citrate Synthase), which exits to the cytoplasm via a tricarboxylate carrier. In the cytosol, <strong>ATP Citrate Lyase</strong> cleaves Citrate back into Acetyl-CoA and Oxaloacetate (consuming ATP).
        </p>
        <p>
          <strong>ACC: The Rate-Limiting Step:</strong><br />
          Cytoplasmic Acetyl-CoA is converted to Malonyl-CoA by <strong>Acetyl-CoA Carboxylase (ACC)</strong>, the rate-limiting enzyme. 
          This carboxylation reaction requires three essential components: **ATP, Biotin (Vitamin B7), and CO&sup2;** (as bicarbonate).<br />
          <strong style="color: var(--accent2)">&bull; Allosteric Regulation:</strong> Activated by <strong>Citrate</strong> (triggers polymerization of inactive monomers into active polymeric filaments) and inhibited by <strong>Palmitoyl-CoA</strong> (triggers depolymerization).<br />
          <strong style="color: var(--accent2)">&bull; Hormonal Regulation:</strong> <strong>Insulin</strong> dephosphorylates and activates ACC (+), promoting fat storage. <strong>Glucagon and Epinephrine</strong> phosphorylate and inhibit ACC (-) via AMP-activated protein kinase (AMPK) and PKA, shutting down fat synthesis during starvation/stress.
        </p>
      </div>

      <div class="big-picture">
        <div class="big-picture-label">🧬 Fatty Acid Synthase (FAS) Homodimer Complex</div>
        <p>
          The remaining steps of lipogenesis are catalyzed by **Fatty Acid Synthase (FAS)**, a multi-enzyme, multi-functional polypeptide complex that functions as a head-to-tail **homodimer**.
        </p>
        <p>
          <strong>Structural Components:</strong><br />
          Each monomer contains **7 distinct catalytic domains** and an **Acyl Carrier Protein (ACP)** domain. 
          ACP is loaded with a **Phosphopantetheine** (derived from Vitamin B5) prosthetic group.
        </p>
        <p>
          <strong>Active Sulfhydryl (-SH) Groups:</strong><br />
          FAS contains two essential -SH groups that must work in close circular coordination:<br />
          1. <strong>Cysteine-SH</strong> group on the &beta;-Ketoacyl Synthase (KS) enzyme domain of one monomer.<br />
          2. <strong>Phosphopantetheine-SH</strong> group on the ACP domain of the adjacent monomer.
        </p>
        <p>
          <strong>The 4-Step Cycle (CRDR Mnemonic):</strong><br />
          Malonyl-CoA units are transferred to the ACP, and the growing acyl chain undergoes a repeating 4-step sequence:<br />
          1. <strong>Condensation (C)</strong>: Condensation of malonyl-ACP with the acetyl group on Cysteine-SH, releasing CO&sup2; (catalyzed by Ketoacyl Synthase).<br />
          2. <strong>Reduction (R)</strong>: Reduction of the &beta;-keto group to a &beta;-hydroxy group, using **NADPH** (catalyzed by Ketoacyl Reductase).<br />
          3. <strong>Dehydration (D)</strong>: Dehydration of the &beta;-hydroxy acyl chain to form a double bond, releasing **H&sup2;O** (catalyzed by Dehydratase).<br />
          4. <strong>Reduction (R)</strong>: Reduction of the double bond to a saturated single bond, using **NADPH** (catalyzed by Enoyl Reductase).
        </p>
        <p>
          This 4-step cycle repeats **7 times** (adding 2 carbons per cycle) until the 16-carbon **Palmitate** is synthesized, which is cleaved from the complex by **Thioesterase**.
        </p>
      </div>
"""
    if acc_key_fact_search in content and "DE NOVO LIPOGENESIS ENZYME MACHINERY" not in content:
        print("[MASTER] Injecting ACC and FAS complex detailed machinery...")
        content = content.replace(acc_key_fact_search, fas_detailed_expansion + "\n" + acc_key_fact_search)

    # 6. Inject Statin competitive inhibition LDL receptor upregulation mechanism in Section 5
    statin_search = """      <div class="key-fact">
        <span class="key-fact-icon">💊</span>
        <div class="key-fact-text">
          <strong>HMG-CoA Reductase</strong>
          <span class="rls-badge">RLS</span> — Inhibited by: Statins"""
    
    statin_detailed_mechanism = """      <div class="big-picture">
        <div class="big-picture-label">💊 Detailed Molecular Mechanism: How Statins Lower Blood LDL</div>
        <p>
          <strong>Statins</strong> (e.g., Atorvastatin, Rosuvastatin) are structural analogues of HMG-CoA and act as potent <strong>competitive inhibitors</strong> of the rate-limiting enzyme <strong>HMG-CoA Reductase</strong>.
        </p>
        <p>
          <strong>Step-by-Step Liver-to-Blood Response:</strong>
        </p>
        <ol class="step-list" style="margin: 15px 0;">
          <li class="hl"><span class="step-num">1</span><strong>Active Site Competition:</strong> Statins bind directly to the active site of HMG-CoA Reductase, preventing the conversion of HMG-CoA to Mevalonate.</li>
          <li class="hl"><span class="step-num">2</span><strong>Intracellular Cholesterol Drop:</strong> Synthesis of cholesterol plummets inside hepatocytes.</li>
          <li class="hl"><span class="step-num">3</span><strong>SREBP-2 Pathway Activation:</strong> Low intracellular cholesterol causes the transcription factor **SREBP-2** (Sterol Regulatory Element Binding Protein-2) to migrate to the nucleus.</li>
          <li class="hl"><span class="step-num">4</span><strong>LDL Receptor Upregulation:</strong> SREBP-2 upregulates the transcription and synthesis of **LDL Receptors** on the hepatocyte cell membrane.</li>
          <li class="hl"><span class="step-num">5</span><strong>LDL Blood Clearance:</strong> The increased density of LDL receptors pulls LDL particles (Apo B-100 containing) out of the bloodstream.</li>
          <li class="hl"><span class="step-num">6</span><strong>Serum Drop:</strong> Circulating **blood LDL level drops dramatically**, lowering cardiovascular plaque risk.</li>
        </ol>
      </div>"""
    
    if statin_search in content and "Detailed Molecular Mechanism: How Statins Lower Blood LDL" not in content:
        print("[MASTER] Injecting detailed Statin mechanism...")
        content = content.replace(statin_search, statin_detailed_mechanism + "\n" + statin_search)

    # 7. Inject Tangier disease and LPL Km kinetics in Section 6
    fh_search = """      <div class="key-fact">
        <span class="key-fact-icon">🧬</span>
        <div class="key-fact-text">
          <strong>Familial Hypercholesterolaemia (FH):</strong>"""
    
    tangier_lpl_details = """
      <div class="big-picture">
        <div class="big-picture-label">🧡 Tangier Disease (ABCA1 Transporter Defect)</div>
        <p>
          <strong>Tangier Disease</strong> is an autosomal recessive disorder caused by mutations in the **ABCA1 transporter** protein.
        </p>
        <p>
          <strong>Pathophysiology:</strong><br />
          ABCA1 is responsible for pumping free cholesterol out of cells onto lipid-poor Apo A-I (nascent discoidal HDL). Without functional ABCA1, cells cannot export cholesterol &rarr; HDL cannot mature and is rapidly degraded in kidneys.
        </p>
        <p>
          <strong>Clinical Presentation:</strong><br />
          &bull; <strong>Zero HDL</strong> in blood (or extremely low levels).<br />
          &bull; Cholesterol esters accumulate in the macrophages of the reticuloendothelial system.<br />
          &bull; **Massively enlarged bright orange tonsils** (hallmark sign, packed with cholesterol-laden macrophages).<br />
          &bull; Severe hepatosplenomegaly, peripheral neuropathy, and highly increased risk of premature <strong>Atherosclerosis</strong>.
        </p>
      </div>

      <div class="big-picture">
        <div class="big-picture-label">💓 Lipoprotein Lipase (LPL) Km Rule &amp; Tissue Affinities</div>
        <p>
          <strong>Lipoprotein Lipase (LPL)</strong> is anchored to capillaries to hydrolyze TAGs in Chylomicrons and VLDLs. Different tissues express different LPL isoforms with distinct kinetic properties:
        </p>
        <p>
          <strong>Cardiac Muscle LPL: Low Km (High Affinity)</strong><br />
          The heart relies constantly on fatty acid oxidation for fuel. The low Km of cardiac LPL ensures that the heart can extract TAGs for energy even when circulating blood lipid levels are extremely low.
        </p>
        <p>
          <strong>Adipose Tissue LPL: High Km (Low Affinity)</strong><br />
          Adipose tissue LPL is regulated by insulin and active only in the postprandial (fed) state. Its high Km ensures that fat storage occurs only when there is an abundance of blood lipids.
        </p>
      </div>
"""
    if fh_search in content and "Tangier Disease (ABCA1 Transporter Defect)" not in content:
        print("[MASTER] Injecting Tangier disease and LPL Km kinetics...")
        content = content.replace(fh_search, tangier_lpl_details + "\n" + fh_search)

    # Save master HTML
    with open(MASTER_HTML, 'w', encoding='utf-8') as f:
        f.write(content)
    print("[MASTER] Masterclass Course successfully remastered!\n")


def remaster_revision():
    print("[REVISION] Loading revision notes...")
    with open(REVISION_HTML, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean up ampersand inside Caffeine image src attribute
    content = content.replace('src="../../Caffeine%20%26%20Cadaver.jpg"', 'src="../../Caffeine &amp; Cadaver.jpg"')
    content = content.replace('src="../../Caffeine & Cadaver.jpg"', 'src="../../Caffeine &amp; Cadaver.jpg"')
    content = content.replace('alt="Caffeine &amp;amp; Cadaver"', 'alt="Caffeine &amp; Cadaver"')

    # 2. Inject native Carnitine Shuttle SVG right under the Carnitine Shuttle flowchart-container
    cpt_key_fact_search = """      <div class="key-fact">
        <span class="key-fact-icon">⭐</span>
        <div class="key-fact-text">
          <strong>CPT-I is the rate-limiting step</strong>"""
    
    if cpt_key_fact_search in content and "FIG 3.1: NATIVE CARNITINE SHUTTLE" not in content:
        print("[REVISION] Injecting Carnitine Shuttle SVG...")
        content = content.replace(cpt_key_fact_search, CARNITINE_SVG + "\n" + cpt_key_fact_search)

    # 3. Inject centered flowchain for β-Oxidation Spiral
    # Locate Palmitate flowchart-container and replace it with a centered vertical flowchain
    palmitate_flow_search = """      <div class="flowchart-container">
        <div class="flowchart-title">
          // One Round of β-Oxidation (Palmitate C16 example)
        </div>"""
    
    centered_beta_spiral = """      <div class="flowchart-container" style="text-align: center;">
        <div class="flowchart-title">
          // &beta;-Oxidation Spiral (Lynen's Spiral) Centered Flowchain
        </div>
        <div class="flow-col" style="align-items: center; max-width: 500px; margin: 0 auto;">
          <div class="flow-row" style="justify-content: center;">
            <div class="flow-box orange" style="width: 280px; text-align: center;">
              <strong>Fatty Acyl-CoA (n carbons)</strong>
            </div>
          </div>
          <span class="flow-down" style="display: block; margin: 10px 0; font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--accent2);">
            &darr; Acyl-CoA Dehydrogenase (FAD &rarr; FADH₂ [+1.5 ATP])
          </span>
          <div class="flow-row" style="justify-content: center;">
            <div class="flow-box teal" style="width: 280px; text-align: center;">
              <strong>Trans-&Delta;&sup2;-Enoyl-CoA</strong>
            </div>
          </div>
          <span class="flow-down" style="display: block; margin: 10px 0; font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--accent2);">
            &darr; Enoyl-CoA Hydratase (+ H&sup2;O)
          </span>
          <div class="flow-row" style="justify-content: center;">
            <div class="flow-box teal" style="width: 280px; text-align: center;">
              <strong>L-3-Hydroxyacyl-CoA</strong>
            </div>
          </div>
          <span class="flow-down" style="display: block; margin: 10px 0; font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--accent2);">
            &darr; 3-Hydroxyacyl-CoA Dehydrogenase (NAD⁺ &rarr; NADH [+2.5 ATP])
          </span>
          <div class="flow-row" style="justify-content: center;">
            <div class="flow-box teal" style="width: 280px; text-align: center;">
              <strong>3-Ketoacyl-CoA</strong>
            </div>
          </div>
          <span class="flow-down" style="display: block; margin: 10px 0; font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--accent2);">
            &darr; Thiolase (+ CoASH)
          </span>
          <div class="flow-row" style="justify-content: center; gap: 20px;">
            <div class="flow-box orange" style="width: 160px; text-align: center;">
              <strong>Acetyl-CoA (2C)</strong><br />&rarr; enters TCA cycle
            </div>
            <div class="flow-box orange" style="width: 160px; text-align: center;">
              <strong>Acyl-CoA (n-2 C)</strong><br />&rarr; enters next round
            </div>
          </div>
        </div>"""
    
    if palmitate_flow_search in content:
        print("[REVISION] Replacing text-based beta-oxidation flowchart with centered flowchain...")
        # Replace up to </div> of the flowchart-container
        # We can locate the entire block using regex or exact replace
        block_regex = r'<div class="flowchart-container">\s*<div class="flowchart-title">\s*// One Round of β-Oxidation [^<]+</div>.*?</div>\s*</div>\s*</div>'
        # Let's see: we want to replace the whole flowchart container
        content = re.sub(r'<div class="flowchart-container">\s*<div class="flowchart-title">\s*// One Round of β-Oxidation.*?</div>\s*<div class="flow-col">.*?</div>\s*<div class="stat-row">.*?</div>\s*</div>\s*</div>', centered_beta_spiral + "\n" + """        <div class="stat-row">
          <div class="stat-pill orange">
            <strong>Palmitate (C16):</strong><br />7 rounds of β-oxidation<br />8
            Acetyl-CoA produced
          </div>
          <div class="stat-pill purple">
            <strong>Per round:</strong><br />1 FADH₂ + 1 NADH<br />= 4 ATP
          </div>
          <div class="stat-pill teal">
            <strong>Net ATP (C16):</strong><br />106 ATP total<br />(−2 for
            activation)
          </div>
        </div>
      </div>""", content, flags=re.DOTALL)

    # 4. Inject centered flowchain for Ketogenesis & Ketolysis reciprocal flows
    ketogenesis_flow_search = r'<div class="flowchart-container">\s*<div class="flowchart-title">\s*// Ketogenesis — Synthesis \(in Liver Mitochondria\).*?</div>\s*<div class="flow-col">.*?</div>\s*</div>'
    
    centered_ketogenesis_ketolysis = """      <div class="flowchart-container" style="text-align: center;">
        <div class="flowchart-title">
          // Ketogenesis &amp; Ketolysis Reciprocal Centered Flows
        </div>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 30px; margin-top: 20px;">
          <!-- Ketogenesis Column -->
          <div class="flow-col" style="align-items: center; max-width: 320px;">
            <h4 style="color: var(--accent); margin-bottom: 12px; text-transform: uppercase; font-size: 11px; font-family: 'IBM Plex Mono';">LIVER (Synthesis only)</h4>
            <div class="flow-box orange" style="width: 220px; text-align: center;">2 &times; Acetyl-CoA</div>
            <span class="flow-down" style="margin: 8px 0; font-size: 10px; font-family: 'IBM Plex Mono';">&darr; Thiolase</span>
            <div class="flow-box orange" style="width: 220px; text-align: center;">Acetoacetyl-CoA</div>
            <span class="flow-down" style="margin: 8px 0; font-size: 10px; font-family: 'IBM Plex Mono';">&darr; HMG-CoA Synthase <span class="rls-badge" style="font-size: 8px;">RLS</span></span>
            <div class="flow-box teal" style="width: 220px; text-align: center;">HMG-CoA</div>
            <span class="flow-down" style="margin: 8px 0; font-size: 10px; font-family: 'IBM Plex Mono';">&darr; HMG-CoA Lyase</span>
            <div class="flow-box orange" style="width: 220px; text-align: center;"><strong>Acetoacetate (1&deg; KB)</strong></div>
            <span class="flow-down" style="margin: 8px 0; font-size: 10px; font-family: 'IBM Plex Mono';">&darr; spontaneous / NADH redⁿ</span>
            <div class="flow-box purple" style="width: 220px; text-align: center;">&beta;-Hydroxybutyrate / Acetone</div>
          </div>
          
          <!-- Ketolysis Column -->
          <div class="flow-col" style="align-items: center; max-width: 320px;">
            <h4 style="color: var(--accent2); margin-bottom: 12px; text-transform: uppercase; font-size: 11px; font-family: 'IBM Plex Mono';">EXTRAHEPATIC (Utilization)</h4>
            <div class="flow-box purple" style="width: 220px; text-align: center;">&beta;-Hydroxybutyrate</div>
            <span class="flow-down" style="margin: 8px 0; font-size: 10px; font-family: 'IBM Plex Mono';">&darr; Dehydrogenase</span>
            <div class="flow-box orange" style="width: 220px; text-align: center;">Acetoacetate</div>
            <span class="flow-down" style="margin: 8px 0; font-size: 10px; font-family: 'IBM Plex Mono'; color: var(--accent3); font-weight: bold;">
              &darr; Thiophorase <br />
              <span style="font-size: 8px; color: var(--accent3);">[ABSENT IN LIVER!]</span>
            </span>
            <div class="flow-box orange" style="width: 220px; text-align: center; border: 1.5px solid var(--accent3);">Acetoacetyl-CoA</div>
            <span class="flow-down" style="margin: 8px 0; font-size: 10px; font-family: 'IBM Plex Mono';">&darr; Thiolase</span>
            <div class="flow-box orange" style="width: 220px; text-align: center;"><strong>2 &times; Acetyl-CoA</strong> &rarr; TCA</div>
          </div>
        </div>
      </div>"""
    
    if re.search(ketogenesis_flow_search, content, flags=re.DOTALL):
        print("[REVISION] Replacing Ketogenesis flowchart with centered reciprocal flowchain...")
        content = re.sub(ketogenesis_flow_search, centered_ketogenesis_ketolysis, content, flags=re.DOTALL)

    # 5. Inject centered flowchain for Cholesterol Synthesis & Statin regulation
    cholesterol_flow_search = r'<div class="flowchart-container">\s*<div class="flowchart-title">\s*// Cholesterol Synthesis — Key Steps.*?</div>\s*<div class="flow-col">.*?</div>\s*<div class="stat-row">.*?</div>\s*</div>'
    
    centered_cholesterol = """      <div class="flowchart-container" style="text-align: center;">
        <div class="flowchart-title">
          // Cholesterol Synthesis &amp; Statin Regulation Centered Flow
        </div>
        <div class="flow-col" style="align-items: center; max-width: 480px; margin: 0 auto;">
          <div class="flow-row" style="justify-content: center;">
            <div class="flow-box orange" style="width: 240px; text-align: center;">3 &times; Acetyl-CoA</div>
          </div>
          <span class="flow-down" style="display: block; margin: 8px 0; font-family: 'IBM Plex Mono'; font-size: 10px;">&darr; HMG-CoA Synthase</span>
          <div class="flow-row" style="justify-content: center;">
            <div class="flow-box orange" style="width: 240px; text-align: center;">HMG-CoA</div>
          </div>
          <span class="flow-down" style="display: block; margin: 8px 0; font-family: 'IBM Plex Mono'; font-size: 11px; color: var(--accent3); font-weight: bold;">
            &darr; HMG-CoA Reductase <span class="rls-badge" style="font-size: 8px;">RLS</span> <br />
            <span style="font-size: 9px; color: var(--accent3);">&times; Competitive Inhibition by Statins</span>
          </span>
          <div class="flow-row" style="justify-content: center;">
            <div class="flow-box teal" style="width: 240px; text-align: center; border: 1.5px solid var(--accent3);">Mevalonate (Statin block target)</div>
          </div>
          <span class="flow-down" style="display: block; margin: 8px 0; font-family: 'IBM Plex Mono'; font-size: 10px;">&darr; IPs &rarr; Squalene &rarr; Lanosterol</span>
          <div class="flow-row" style="justify-content: center;">
            <div class="flow-box orange" style="width: 240px; text-align: center;"><strong>Cholesterol (27C)</strong></div>
          </div>
        </div>
        <div class="stat-row">
          <div class="stat-pill orange">
            <strong>Location:</strong><br />Cytoplasm + ER<br />(mainly liver)
          </div>
          <div class="stat-pill purple">
            <strong>ACAT:</strong><br />Esterifies cholesterol<br />for storage
          </div>
          <div class="stat-pill teal">
            <strong>LCAT:</strong><br />Esterifies cholesterol<br />in plasma
            (HDL)
          </div>
        </div>
      </div>"""
    
    if re.search(cholesterol_flow_search, content, flags=re.DOTALL):
        print("[REVISION] Replacing cholesterol flowchart with centered flowchain...")
        content = re.sub(cholesterol_flow_search, centered_cholesterol, content, flags=re.DOTALL)

    # 6. Remove raw bolds (**word**) from revision text to comply with the standard
    # Replace **word** with <strong>word</strong> case-insensitively
    print("[REVISION] Stripping raw markdown bold markers (**)...")
    content = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', content)

    # Save revision HTML
    with open(REVISION_HTML, 'w', encoding='utf-8') as f:
        f.write(content)
    print("[REVISION] Revision Guide successfully remastered!\n")

if __name__ == "__main__":
    remaster_master()
    remaster_revision()
