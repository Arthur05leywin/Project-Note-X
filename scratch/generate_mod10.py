import re

filepath = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\module09_embryology.html"
with open(filepath, 'r', encoding='utf-8') as f:
    mod9 = f.read()

# Extract head and style
head_match = re.search(r'(<!DOCTYPE html>.*?</style>\s*</head>)', mod9, re.DOTALL)
if head_match:
    head_content = head_match.group(1)
else:
    raise Exception("Could not find head/style")

# Build Module 10
mod10_content = head_content + """
<body>

<div class="brand-bar">
    <div class="brand-logo-container">
        <a href="../index.html">
            <img src="../logo-full.png" alt="WBUHS Notes" class="brand-logo" onerror="this.src='../logo-full.png'; this.onerror=null;">
        </a>
    </div>
    <div class="brand-nav">
        <a href="../anatomy_index.html" class="nav-btn"><i class="fas fa-undo"></i> Back</a>
    </div>
</div>

<div class="container">
  <div class="hero">
    <div class="module-tag">Anatomy Module 10</div>
    <h1>Histology (General & Systemic)</h1>
    <div class="hero-pills">
      <span class="pill"><i class="fas fa-microscope"></i> Inderbir Singh Based</span>
      <span class="pill"><i class="fas fa-star"></i> High-Yield PYQs</span>
    </div>
  </div>

  <div class="toc">
    <div class="toc-title">Module Contents</div>
    <div class="toc-grid">
      <a href="#s1" class="toc-link">1. General Histology (Tissues)</a>
      <a href="#s2" class="toc-link">2. Lymphoid System (Lymph Node, Tonsil)</a>
      <a href="#s3" class="toc-link">3. Digestive System (Liver, Pancreas)</a>
      <a href="#s4" class="toc-link">4. Quickfire & Mnemonics</a>
    </div>
  </div>

  <!-- SECTION 1 -->
  <div id="s1">
    <div class="section-header">1. General Histology (Tissues)</div>

    <div class="two-col">
      <div class="card">
        <div class="card-title">Epithelial Tissue</div>
        <div class="card-body">
          <p>Epithelium consists of closely packed cells with very little intercellular substance. It covers body surfaces, lines cavities, and forms glands.</p>
          <div class="keypoint"><strong>Simple Squamous:</strong> Single layer of flat cells. Found in alveoli, Bowman's capsule, endothelium.</div>
          <div class="keypoint"><strong>Simple Cuboidal:</strong> Thyroid follicles, PCT, DCT.</div>
          <div class="keypoint"><strong>Simple Columnar:</strong> Stomach and intestines (with microvilli).</div>
          <div class="keypoint"><strong>Pseudostratified Ciliated:</strong> Respiratory tract (trachea, bronchi).</div>
          <div class="keypoint"><strong>Transitional Epithelium (Urothelium):</strong> Umbrella cells allow stretching. Found in ureter and urinary bladder.</div>
        </div>
      </div>

      <div class="card">
        <div class="card-title">Cartilage & Bone</div>
        <div class="card-body">
          <p>Specialized connective tissues providing support.</p>
          <div class="keypoint"><strong>Hyaline Cartilage:</strong> Most common. Glassy matrix with type II collagen. Chondrocytes in lacunae. Found in articular surfaces, costal cartilage, trachea.</div>
          <div class="keypoint"><strong>Elastic Cartilage:</strong> Matrix contains elastic fibers. Found in Epiglottis, Pinna (ear).</div>
          <div class="keypoint"><strong>Fibrocartilage:</strong> Type I collagen. No perichondrium. Found in intervertebral discs, pubic symphysis.</div>
          <div class="keypoint"><strong>Compact Bone:</strong> Characterized by Haversian systems (osteons) with concentric lamellae.</div>
        </div>
      </div>
    </div>
    
    <div style="text-align:center; margin:1rem 0;">
      <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray292.png" alt="Hyaline Cartilage" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;">
        <div class="wiki-caption" style="font-size:11px;color:var(--text2);margin-top:6px;">Hyaline Cartilage Section (Gray's Anatomy)</div>
      </div>
    </div>
    
    <div class="divider"></div>
  </div>

  <!-- SECTION 2 -->
  <div id="s2">
    <div class="section-header">2. Lymphoid System <span class="badge badge-pyq">PYQ 2016, 2019, 2023</span></div>

    <div class="card">
      <div class="card-title">Histology of Lymph Node <span class="badge badge-pyq">PYQ 2016 supple</span></div>
      <div class="card-body">
        <p>A lymph node is a small, bean-shaped encapsulated lymphoid organ.</p>
        <div class="keypoint"><strong>Capsule & Trabeculae:</strong> Dense connective tissue capsule. Trabeculae extend inward, dividing the node into incomplete compartments. Subcapsular sinus is present just beneath the capsule.</div>
        <div class="keypoint"><strong>Cortex (Outer):</strong> Contains lymphatic nodules (follicles) with pale germinal centers (active B-lymphocytes).</div>
        <div class="keypoint"><strong>Paracortex (Inner Cortex):</strong> Deep to the follicles. Contains T-lymphocytes. Thymus-dependent zone.</div>
        <div class="keypoint"><strong>Medulla:</strong> Inner pale region containing medullary cords (lymphocytes, plasma cells) and medullary sinuses (macrophages).</div>
      </div>
    </div>
    
    <div style="text-align:center; margin:1rem 0;">
      <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1064.png" alt="Lymph Node" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;">
        <div class="wiki-caption" style="font-size:11px;color:var(--text2);margin-top:6px;">Section of a Lymph Node (Gray's Anatomy)</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">Palatine Tonsil <span class="badge badge-fav">⭐ PYQ 2019, 2023</span></div>
      <div class="card-body">
        <p>Almond-shaped masses of lymphoid tissue located in the lateral wall of the oropharynx between palatoglossal and palatopharyngeal arches.</p>
        <div class="keypoint"><strong>Epithelium:</strong> Lined by <strong>non-keratinized stratified squamous epithelium</strong>.</div>
        <div class="keypoint"><strong>Tonsillar Crypts:</strong> The epithelium invaginates deeply to form 10-15 deep crypts. The primary crypts may branch into secondary crypts.</div>
        <div class="keypoint"><strong>Lymphatic Nodules:</strong> Underlying the epithelium, numerous lymphatic follicles with germinal centers are present.</div>
        <div class="warn-box"><strong>Identification Point:</strong> Stratified squamous epithelium with deep crypts and subepithelial lymphoid follicles. Unlike lymph nodes, there is <strong>no subcapsular sinus</strong> and it is not completely encapsulated.</div>
      </div>
    </div>

    <div class="divider"></div>
  </div>

  <!-- SECTION 3 -->
  <div id="s3">
    <div class="section-header">3. Digestive System (Liver & Pancreas) <span class="badge badge-fav">⭐ PYQ 2012, 2017, 2019</span></div>

    <div class="card">
      <div class="card-title">Histology of Liver (Classical Hepatic Lobule) <span class="badge badge-pyq">PYQ 2012</span></div>
      <div class="card-body">
        <p>The liver is covered by Glisson's capsule. The parenchyma is organized into lobules.</p>
        <div class="keypoint"><strong>Classical Hepatic Lobule:</strong> Hexagonal shape. A central vein lies at the center. Portal triads lie at the corners.</div>
        <div class="keypoint"><strong>Portal Triad:</strong> Contains branches of portal vein, hepatic artery, and bile duct.</div>
        <div class="keypoint"><strong>Hepatocytes:</strong> Arranged in radiating cords or plates extending from the central vein to the periphery.</div>
        <div class="keypoint"><strong>Hepatic Sinusoids:</strong> Vascular spaces between hepatocyte plates. Lined by fenestrated endothelium and <strong>Kupffer cells</strong> (hepatic macrophages).</div>
        <div class="warn-box"><strong>Liver Acinus:</strong> The functional unit of the liver, diamond-shaped, defined by oxygen gradient. Zone I (periportal) gets the most oxygen, Zone III (pericentral) gets the least and is most susceptible to ischemia.</div>
      </div>
    </div>
    
    <div style="text-align:center; margin:1rem 0;">
      <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Liver_Lobule_(NIH_BioArt_565).png" alt="Liver Lobule" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;">
        <div class="wiki-caption" style="font-size:11px;color:var(--text2);margin-top:6px;">Classical Hepatic Lobule (NIH BioArt)</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">Histology of Pancreas <span class="badge badge-pyq">PYQ 2017, 2019</span></div>
      <div class="card-body">
        <p>The pancreas is a mixed exocrine and endocrine gland.</p>
        <div class="keypoint"><strong>Exocrine Part (Serous Acini):</strong> Consists of closely packed serous acini. Acinar cells are pyramidal with basophilic basal cytoplasm and apical zymogen granules. <strong>Centroacinar cells</strong> are present in the lumen.</div>
        <div class="keypoint"><strong>Endocrine Part (Islets of Langerhans):</strong> Pale-staining, highly vascular clusters of cells scattered among exocrine acini (more numerous in the tail). Contains Alpha cells (glucagon), Beta cells (insulin), and Delta cells (somatostatin).</div>
        <div class="warn-box"><strong>Identification Point:</strong> Serous acini with centroacinar cells + Islets of Langerhans. No striated ducts (differentiates from parotid gland).</div>
      </div>
    </div>
    
    <div style="text-align:center; margin:1rem 0;">
      <div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Gray1056.png" alt="Pancreas Histology" class="wiki-img" style="max-width:100%;height:auto;border-radius:8px;">
        <div class="wiki-caption" style="font-size:11px;color:var(--text2);margin-top:6px;">Section of human pancreas (Gray's Anatomy)</div>
      </div>
    </div>

    <div class="divider"></div>
  </div>

  <!-- SECTION 4 -->
  <div id="s4">
    <div class="section-header">4. High-Yield Quickfire & Mnemonics</div>
    
    <div class="card">
      <div class="card-title">Master Mnemonics <i class="fas fa-brain" style="color:var(--primary);margin-left:8px;"></i></div>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(min(270px, 100%),1fr));gap:10px;margin-top:8px">
        <div class="mnemonic-box">
          <div class="mnemonic-title">Types of Cartilage (HEF)</div>
          <div class="mnemonic-highlight">H · E · F</div>
          <div class="keypoint" style="margin-top:8px"><strong>H</strong>yaline (Type II)<br><strong>E</strong>lastic (Type II + Elastic)<br><strong>F</strong>ibrocartilage (Type I)</div>
        </div>
        <div class="mnemonic-box">
          <div class="mnemonic-title">Islets of Langerhans Cells (GAB)</div>
          <div class="mnemonic-highlight">G · A · B</div>
          <div class="keypoint" style="margin-top:8px"><strong>G</strong>lucagon from <strong>A</strong>lpha cells<br>Insulin from <strong>B</strong>eta cells</div>
        </div>
      </div>
    </div>
    
    <div class="card">
      <div class="card-title">Quickfire Revision Table</div>
      <div class="table-wrap">
        <table>
          <tr><th>Organ</th><th>Epithelium / Defining Feature</th><th>Key Distinguishing Structure</th></tr>
          <tr><td>Lymph Node</td><td>Reticular stroma</td><td>Subcapsular Sinus, Cortex/Medulla</td></tr>
          <tr><td>Palatine Tonsil</td><td>Stratified squamous non-keratinized</td><td>Tonsillar Crypts</td></tr>
          <tr><td>Liver</td><td>Hepatocytes (cuboidal)</td><td>Central vein, Portal triads, Kupffer cells</td></tr>
          <tr><td>Pancreas</td><td>Serous acini</td><td>Centroacinar cells, Islets of Langerhans</td></tr>
        </table>
      </div>
    </div>

  </div>

  <div class="footer">
    <p>Includes Gray's Anatomy diagrams</p>
  </div>
</div>

</body>
</html>
"""

with open(r'c:\Users\sayan\Downloads\biochem Note X\anatomy modules\module10_histology.html', 'w', encoding='utf-8') as f:
    f.write(mod10_content)

print("Module 10 generated successfully.")
