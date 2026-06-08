import sys

filepath = r'c:\Users\sayan\Downloads\biochem Note X\modules\module-04\module04_protein_haemoglobin_X.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<!-- SECTION 11:')
if idx == -1:
    print('Section 11 not found')
    sys.exit(1)

text_to_keep = text[:idx]
footer = """    </div>
    <!-- /content -->

    <!-- FOOTER -->
    <div class="footer">
      <p>MODULE 04 · PROTEIN CHEMISTRY & HAEMOGLOBIN</p>
      <p style="margin-top: 4px">
        Caffeine &amp; Cadaver · MBBS Biochemistry Notes · 2010–2025
      </p>
      <p style="margin-top: 4px; color: var(--accent); font-size: 11px">
        Compiled for personal academic use
      </p>
    </div>

    <button
      class="top-btn"
      onclick="window.scrollTo({ top: 0, behavior: 'smooth' })"
    >
      ↑
    </button>

    <script>
      // Smooth open/close animation for details
      document.querySelectorAll("details").forEach((d) => {
        d.addEventListener("toggle", () => {
          if (d.open) {
            const content = d.querySelector(".viva-ans");
            if (content) {
              content.style.animation = "fadeIn 0.2s ease";
            }
          }
        });
      });
    </script>
  </body>
</html>"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text_to_keep + footer)
print('Pruned successfully.')
