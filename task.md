# Task List: Biochemistry Notes Remastering & Restructuring

## 📋 Phase 1: Module 01 Pilot (Completed)
- `[x]` Step 1.1: Standard Notes Remastering (Masterclass Course)
- `[x]` Step 1.2: Version X Notes Remastering (Fast-Paced Revision)
- `[x]` Step 1.3: Stylesheet & Compilation Sync

## 📋 Phase 3: Module 03 Remastering (Lipid Metabolism) [Completed]

- `[x]` **Step 3.1: Standard Notes Remastering (Masterclass Course)**
  - `[x]` Inject "Caffeine & Cadaver" brand bar and logo (`../../Caffeine &amp; Cadaver.jpg`)
  - `[x]` Clean up WBUHS terminology -> MBBS globally and remove KIMS/NMO mentions
  - `[x]` Add comprehensive Lynen's β-oxidation spiral details and formulas (stearate/palmitate ATP yields)
  - `[x]` Add peroxisomal VLCFA oxidation (acyl-CoA oxidase, catalase)
  - `[x]` Add unsaturated fatty acids (isomerase, reductase) and odd-chain fatty acids (Propionyl-CoA, Biotin, Vitamin B12, Methylmalonic Aciduria)
  - `[x]` Add reciprocal regulation of β-oxidation (ACC, Malonyl-CoA CPT-I block)
  - `[x]` Add DKA vs. Fasting Ketosis comparison (insulin brake mechanism) and diagnostics (Gerhardt's test)
  - `[x]` Add Lipoprotein LPL Km kinetics (Cardiac LPL low Km vs Adipose LPL high Km)
  - `[x]` Add Tangier disease (ABCA1 defect, orange tonsils) and Statin LDL receptor upregulation mechanism
  - `[x]` Add Fatty Acid Synthesis pathway (Citrate shuttle, ACC RLS with Biotin/ATP/CO2, FAS homodimer complex, phosphopantetheine, circular schematic, CRDR steps)
  - `[x]` Construct and embed **native Carnitine Shuttle SVG** diagram

- `[x]` **Step 3.2: Version X Notes Remastering (Fast-Paced Revision)**
  - `[x]` Sync cover page and brand bar layout
  - `[x]` Scrub WBUHS -> MBBS and KIMS/NMO mentions
  - `[x]` Prune conceptual paragraphs and mathematical derivations to keep it purely revision cards
  - `[x]` Replace raw bold markers (`**`) with `<strong>` tags
  - `[x]` Embed thecentered flowchains:
    - `[x]` Carnitine Shuttle SVG
    - `[x]` β-Oxidation Spiral centered vertical flowchain
    - `[x]` Ketogenesis & Ketolysis reciprocal flowchain (highlighting "Absent in Liver" thiophorase)
    - `[x]` Cholesterol Synthesis & Statin regulation flowchain
  - `[x]` Optimize Lipoprotein comparison table grid padding to prevent horizontal print bleed

- `[x]` **Step 3.3: Stylesheet, Propagation & PDF Compilation**
  - `[x]` Run `propagate_css.py` to inline master CSS and sync the fallback `<link>` tag
  - `[x]` Run `generate_pdf.py --module 3` to compile A4 print PDFs
  - `[x]` Run `scratch_verify_shipping.py` (after adding Module 3 to the checklist) to run compliance checks
  - `[x]` Verify compiled page count and ensure zero layout-breaking negative margins or visual gaps (> 220px)
