# Anatomy Module Generation Workflow

When asked to create a new anatomy module, follow these steps strictly to match the established project design:

1. **Information Gathering & Notes Extraction:**
   - Scan the `2010-25 1ST PROFF PYQS NMO-BENGAL (2).pdf` using the `view_file` tool to identify and extract **every single question** related to the requested anatomical region, regardless of frequency.
   - For medical content, prioritize extracting raw notes from an external source or file if provided by the user. If not provided, generate concise, high-yield medical notes using internal knowledge.

2. **File Structure & Styling:**
   - Create a single HTML file (e.g., `module10_region.html`).
   - Include the standard `<!DOCTYPE html>`, `<head>`, and the complete internal `<style>` block from previous modules.
   - **Crucial CSS Rules:** Ensure `.two-col` uses `grid-template-columns: repeat(auto-fill, minmax(min(280px, 100%), 1fr));`. Ensure `.keypoint` and `.warn-box` use `display: block; position: relative;` with absolute positioned pseudo-element icons and `word-break: break-word; overflow-wrap: break-word;`.

3. **Content Layout:**
   - **Hero:** `<div class="hero">` with an overarching title, `.module-tag`, and `.hero-pills`.
   - **TOC:** `<div class="toc">` linking to sections.
   - **Sections:** `<div id="s1">...` with a `<div class="section-header">` and a `<div class="divider"></div>` separating them.
   - **Components:** Use `<div class="card">` for topics, `<div class="clinical-box">` for clinical correlates, `<div class="mnemonic-box">` for memory aids, `<div class="keypoint">` and `<div class="warn-box">` for specific notes.
   - **Tables:** Use `<div class="table-wrap"><table>...</table></div>`.
   - **Quickfire & Mnemonics:** Always conclude the module with a "High-Yield Quickfire Revision" table and a "Master Mnemonics" grid section.

4. **PYQ Integration:**
   - Next to relevant `<div class="card-title">` or headings, append PYQ badges based on the PDF data.
   - Examples: `<span class="badge badge-pyq">PYQ 2014, 2019</span>`, `<span class="badge badge-fav">⭐ PYQ 2018, 2021, 2023</span>`, `<span class="badge badge-fav">⭐ PYQ EVERY YEAR</span>`.

5. **Diagrams (Automated Retrieval):**
   - Automatically search Wikimedia Commons (via python script) for relevant "Gray's Anatomy" images (e.g., `Gray123.png`) that match the extracted topics.
   - Embed them directly during generation using `<div class="diagram-placeholder" style="border:none; padding:0; background:transparent;">` with the actual `<img class="wiki-img">` pointing to the Wikimedia `Special:FilePath` URL.
   - Only leave empty placeholders if absolutely no relevant image can be found.
