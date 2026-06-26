import re

file_path = "anatomy.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace links
content = re.sub(r'href="anatomy modules/[^"]+"', 'href="contact.html"', content)

# 2. Add CSS
css_to_add = """
/* ── PACKS ── */
.pack-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 40px;
}

.pack-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 30px;
  display: flex;
  flex-direction: column;
}

.pack-card.featured {
  border-color: rgba(214,60,60,0.5);
  background: linear-gradient(135deg, var(--surface), rgba(214,60,60,0.05));
}

.pack-card.bundle {
  border-color: rgba(212,175,55,0.4);
  background: linear-gradient(135deg, var(--surface), rgba(212,175,55,0.05));
}

.pack-label {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 12px;
}

.pack-title {
  font-family: 'Playfair Display', serif;
  font-size: 22px;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 20px;
}

.pack-features {
  list-style: none;
  margin-bottom: 30px;
  flex: 1;
}

.pack-features li {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 10px;
  padding-left: 20px;
  position: relative;
}

.pack-features li::before {
  content: '•';
  color: var(--accent);
  position: absolute;
  left: 0;
}

.pack-price {
  font-family: 'Playfair Display', serif;
  font-size: 36px;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 24px;
}

.pack-card.bundle .pack-price {
  color: #d4af37;
}
.pack-card.featured .pack-price {
  color: var(--accent);
}

.pack-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

/* ── DIVIDER ── */"""

content = content.replace("/* ── DIVIDER ── */", css_to_add)

# 3. Add HTML section
html_to_add = """
<hr class="section-divider">

<!-- PACKS -->
<div class="section" id="packs">
  <div class="section-label">Get started</div>
  <h2 class="section-title">Choose your <span>entry point</span>.</h2>
  
  <div class="pack-grid">
    <div class="pack-card featured">
      <div class="pack-label">Starter Pack</div>
      <div class="pack-title">Module 01 Launch Bundle</div>
      <ul class="pack-features">
        <li>Module 01 Version X with PYQ priority map</li>
        <li>Normal Module 01 for complete study flow</li>
        <li>Printable PDF included</li>
      </ul>
      <div class="pack-price">₹49</div>
      <div class="pack-actions">
        <a href="contact.html" class="btn-primary">Buy Now</a>
        <a href="sample.html" class="btn-secondary">View Sample</a>
      </div>
    </div>

    <div class="pack-card bundle">
      <div class="pack-label">Complete Bundle</div>
      <div class="pack-title">Full Anatomy Ranker Series</div>
      <ul class="pack-features">
        <li>All 10 Masterclass modules</li>
        <li>All 10 Version X modules</li>
        <li>All 20 printable PDFs included</li>
        <li>Full MBBS 1st Year Anatomy syllabus covered</li>
      </ul>
      <div class="pack-price">₹399</div>
      <div class="pack-actions">
        <a href="contact.html" class="btn-primary" style="background: #d4af37; color: #0a0808;">Buy Bundle</a>
        <a href="#modules" class="btn-secondary">View All Modules</a>
      </div>
    </div>
  </div>
</div>

<!-- WHAT TO EXPECT -->"""

content = content.replace("<!-- WHAT TO EXPECT -->", html_to_add)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated anatomy.html successfully!")
