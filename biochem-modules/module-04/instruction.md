# WBUHS Biochemistry Notes — PDF Print Optimization Guide

This instruction manual provides the complete technical details, CSS design systems, and troubleshooting workflows required to convert interactive, dark-themed HTML biochemistry study modules into textbook-quality, high-fidelity printed PDFs (using standard **Ctrl+P** / Print-to-PDF in Chromium-based browsers like Chrome, Edge, Brave, or Firefox).

---

## ── CORE OBJECTIVES ──

1. **A4 Portrait Compliance**: The layout must conform strictly to A4 page parameters with zero cutoffs or horizontal clipping.
2. **Extreme Contrast & Ink Preservation**: Automatically toggle dark backgrounds to high-visibility pure white (`#ffffff`) and colorized text to absolute black (`#000000`) to conserve ink/toner while preserving readable structure.
3. **Flawless Content Flow**: Ensure tables, lists, flowcharts, and mnemonics never split awkwardly across page breaks.
4. **Auto-Expansion of Interactive Elements**: Force all interactive widgets (like collapsible Q&As or Tier lists) to expand fully in print mode so no study material is lost in the PDF.

---

## ── DETAILED PROBLEMS & CSS SOLUTIONS ──

### 1. The "Name Rotation" Mangle (Vertical Text Wrapping)
* **The Problem**: In narrow portrait columns, CSS flexboxes, or flowchart blocks, long scientific, chemical, or enzyme names (e.g., *Phytanoyl-CoA hydroxylase*, *Phosphatidylcholine*, *Acetoacetyl-CoA*) get compressed. The browser attempts to break the words anywhere, resulting in a single letter wrapping onto each line—resembling vertical, rotated text that is impossible to read.
* **The Solution**: Apply absolute word-break protection, disable default browser hyphenation, and force containers to retain single-line integrity.
* **The Code**:
  ```css
  /* Prevent science names from stacking letter-by-letter */
  .flow-box,
  .flow-arrow,
  .flow-down,
  .stat-pill,
  .key-fact-text,
  .mnemonic-expand,
  td {
    word-break: keep-all !important;
    overflow-wrap: normal !important;
    hyphens: none !important;
  }
  
  /* Force flowchart connectors and single-line steps to stay on one line */
  .flow-arrow,
  .flow-down {
    white-space: nowrap !important;
  }
  ```

---

### 2. Collapsible Q&A & Viva Expansion
* **The Problem**: Modern web designs use interactive `<details>` and `<summary>` blocks to hide answers until clicked (reducing cognitive load). However, default browser printing respects the collapsed state; any closed `<details>` tag will print as a single line, and the valuable answer block inside will be completely lost in the PDF.
* **The Solution**: Force the browser to override the collapsed state and render all internal elements as visible blocks exclusively during print. Additionally, hide browser-default summary disclosure markers (arrows) to ensure a clean book layout.
* **The Code**:
  ```css
  /* Force closed details blocks to expand and layout as visible text blocks */
  details.viva-q,
  details {
    display: block !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    margin-bottom: 15px !important;
    padding-bottom: 15px !important;
    border-bottom: 1px solid #e2e2e6 !important;
  }
  
  /* Remove bottom border on the last question of a block */
  details.viva-q:last-child {
    border-bottom: none !important;
  }

  /* Make summary text behave like standard bold headers */
  summary.viva-q-text,
  details > summary {
    display: block !important;
    font-weight: bold !important;
    color: #000000 !important;
    cursor: default !important;
    font-size: 13px !important;
    margin-bottom: 8px !important;
  }

  /* Hide default web triangles/disclosure arrows in print */
  summary::-webkit-details-marker,
  summary::after,
  summary::before {
    display: none !important;
    content: "" !important;
  }

  /* Force all nested children of closed details to show up */
  details:not([open]) > *:not(summary) {
    display: block !important;
  }

  /* Format expanded answers cleanly with a solid structural left border */
  .viva-a-text {
    display: block !important;
    color: #111111 !important;
    border-left: 2px solid #88888d !important;
    padding-left: 12px !important;
    margin-top: 4px !important;
  }
  ```

---

### 3. Comparison Table A4 Scaling & Fitting
* **The Problem**: Wide comparison tables (e.g., 5-column lipoprotein comparisons) overflow standard A4 margins, causing columns to be cut off horizontally on the right margin.
* **The Solution**: Scale fonts down, restrict cell padding, enforce border-collapse, remove shadow overlays, and reset backgrounds to absolute contrast.
* **The Code**:
  ```css
  /* Scale tables to fit A4 width perfectly */
  .table-wrap {
    width: 100% !important;
    overflow: visible !important;
  }

  .comp-table {
    width: 100% !important;
    font-size: 11px !important; /* Ideal size for text readability vs spatial limits */
    line-height: 1.45 !important;
    border-collapse: collapse !important;
  }

  /* High contrast table headers */
  .comp-table th {
    background: #eef0f4 !important;
    color: #000000 !important;
    border-bottom: 2px solid #88888d !important;
    font-size: 10px !important;
    padding: 8px 10px !important;
  }

  /* Clean rows with light separations */
  .comp-table td {
    border-bottom: 1px solid #d3d3d8 !important;
    color: #111111 !important;
    padding: 8px 10px !important;
    background: #ffffff !important;
  }

  /* Prevent browser from rendering hover states in print */
  .comp-table tr:hover td {
    background: #ffffff !important;
  }
  ```

---

### 4. Page Break & Orphan Prevention
* **The Problem**: 
  1. **Orphan Headings**: Section titles (e.g., `<h2>`) printing at the very bottom of a page while the actual content begins on the next page.
  2. **Split Cards**: High-yield boxes (mnemonics, PYQ lists, clinical boxes) getting sliced in half across pages, creating a highly disjointed reading flow.
* **The Solution**: Enforce strict vertical breaking page rules.
* **The Code**:
  ```css
  /* Ensure headers never get orphaned at the bottom of a page */
  h1, h2, h3, .section-header {
    page-break-after: avoid !important;
    break-after: avoid !important;
  }

  /* Ensure component-level block containers stay together on a single page */
  .pyq-box,
  .clinical-box,
  .mnemonic,
  .viva-section,
  .big-picture,
  .info-card,
  .flowchart-container,
  .table-wrap,
  tr {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  ```

---

### 5. Cover Page Layout
* **The Problem**: Interactive covers often rely on fullscreen heights (`min-height: 100vh`) and huge background gradients that render as massive, ugly ink-consuming splotches in gray scale.
* **The Solution**: Standardize the cover to precisely `92vh`, force a page break immediately after it, disable decorative background glows (`::before` / `::after`), and establish highly refined monochrome typography.
* **The Code**:
  ```css
  .cover {
    min-height: 92vh !important;
    height: 92vh !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    page-break-after: always !important;
    break-after: page !important;
    padding: 40px !important;
    background: #ffffff !important;
    color: #000000 !important;
  }

  /* Hide colored gradient background glows */
  .cover::before,
  .cover::after {
    display: none !important;
  }
  ```

---

## ── COPY-PASTE PRINT BLUEPRINT ──

Place this block at the very end of your HTML's interior `<style>` tag. It overrides standard web styles exclusively when the print command is initiated.

```css
      /* 🖨️ PREMIUM PRINT TO PDF RULES (Ctrl+P Optimized) */
      @page {
        size: A4 portrait;
        margin: 15mm 12mm 15mm 12mm;
      }

      @media print {
        /* 1. Body & Cover Page Layout */
        body,
        .cover {
          background: #ffffff !important;
          color: #000000 !important;
        }

        .cover {
          min-height: 92vh !important;
          height: 92vh !important;
          display: flex !important;
          flex-direction: column !important;
          justify-content: center !important;
          page-break-after: always !important;
          break-after: page !important;
          padding: 40px !important;
        }

        .cover::before,
        .cover::after {
          display: none !important;
        }

        .cover-divider {
          background: #000000 !important;
          border-bottom: 2px solid #000000;
        }

        .cover-pyq-badge {
          border: 1px solid #000000 !important;
          background: #f0f0f2 !important;
          color: #000000 !important;
        }

        /* 2. Page Break Controls */
        h1,
        h2,
        h3,
        .section-header {
          page-break-after: avoid !important;
          break-after: avoid !important;
        }

        .pyq-box,
        .clinical-box,
        .mnemonic,
        .viva-section,
        .big-picture,
        .info-card,
        .flowchart-container,
        .table-wrap,
        tr {
          page-break-inside: avoid !important;
          break-inside: avoid !important;
        }

        /* 3. Absolute Contrast & Typography */
        h1,
        h2,
        h3,
        h1 span,
        h2 span,
        .section-title,
        .cover h1,
        .mnemonic-text,
        p,
        li,
        td,
        strong,
        summary,
        .viva-a-text,
        .viva-q-text {
          color: #000000 !important;
        }

        .section-number {
          color: #555555 !important;
        }

        .section-header {
          border-bottom: 1.5px solid #000000 !important;
        }

        .section-divider {
          border-top: 1px solid #d3d3d8 !important;
        }

        /* 4. Ink-Saving Clean Container Boxes */
        .pyq-box,
        .clinical-box,
        .mnemonic,
        .viva-section,
        .big-picture,
        .info-card,
        .flowchart-container {
          background: #fafafb !important;
          border: 1px solid #d3d3d8 !important;
          box-shadow: none !important;
          color: #111111 !important;
          padding: 18px !important;
          margin: 15px 0 !important;
        }

        .pyq-box-label,
        .clinical-label,
        .mnemonic-label,
        .big-picture-label,
        .viva-label {
          color: #000000 !important;
          font-weight: bold !important;
          border-bottom: 1px dashed #a0a0a5 !important;
          padding-bottom: 4px;
          margin-bottom: 10px;
        }

        .clinical-box ul li::before {
          color: #000000 !important;
        }

        /* 5. Preventing Word Wrapping Mangle on Long Enzyme/Chemical Names */
        .flow-box,
        .flow-arrow,
        .flow-down,
        .stat-pill,
        .key-fact-text,
        .mnemonic-expand,
        td {
          word-break: keep-all !important;
          overflow-wrap: normal !important;
          hyphens: none !important;
        }

        .flow-arrow,
        .flow-down {
          white-space: nowrap !important;
          color: #333333 !important;
        }

        .flow-box {
          background: #ffffff !important;
          border: 1.5px solid #88888d !important;
          color: #000000 !important;
          box-shadow: none !important;
        }

        .flow-box strong {
          color: #000000 !important;
        }

        .stat-pill {
          background: #ffffff !important;
          border: 1px solid #a0a0a5 !important;
          color: #000000 !important;
        }

        .step-list li {
          background: #ffffff !important;
          border: 1px solid #d3d3d8 !important;
          border-left: 4px solid #55555a !important;
          color: #000000 !important;
        }

        /* 6. Table Layout & Scaling (A4 Portrait Fit) */
        .table-wrap {
          width: 100% !important;
          overflow: visible !important;
        }

        .comp-table {
          width: 100% !important;
          font-size: 11px !important;
          line-height: 1.45 !important;
          border-collapse: collapse !important;
        }

        .comp-table th {
          background: #eef0f4 !important;
          color: #000000 !important;
          border-bottom: 2px solid #88888d !important;
          font-size: 10px !important;
          padding: 8px 10px !important;
        }

        .comp-table td {
          border-bottom: 1px solid #d3d3d8 !important;
          color: #111111 !important;
          padding: 8px 10px !important;
          background: #ffffff !important;
        }

        .comp-table tr:hover td {
          background: #ffffff !important;
        }

        /* 7. Collapsible Q&A Expansion (Prints all answers automatically) */
        details.viva-q,
        details {
          display: block !important;
          page-break-inside: avoid !important;
          break-inside: avoid !important;
          margin-bottom: 15px !important;
          padding-bottom: 15px !important;
          border-bottom: 1px solid #e2e2e6 !important;
        }

        details.viva-q:last-child {
          border-bottom: none !important;
        }

        summary.viva-q-text,
        details > summary {
          display: block !important;
          font-weight: bold !important;
          color: #000000 !important;
          cursor: default !important;
          font-size: 13px !important;
          margin-bottom: 8px !important;
          padding-left: 0 !important;
        }

        /* Hide standard web details arrow in print */
        summary::-webkit-details-marker,
        summary::after,
        summary::before {
          display: none !important;
          content: "" !important;
        }

        details:not([open]) > *:not(summary) {
          display: block !important;
        }

        .viva-a-text {
          display: block !important;
          color: #111111 !important;
          border-left: 2px solid #88888d !important;
          padding-left: 12px !important;
          margin-top: 4px !important;
          margin-left: 0 !important;
        }
      }
```

---

## ── VERIFICATION WORKFLOW ──

To manually inspect and test print styles without having to trigger the browser's slow physical print system:

### How to use Chrome DevTools Print Emulation:
1. Open the target HTML document in Google Chrome, Microsoft Edge, or Brave.
2. Press **F12** (or `Ctrl+Shift+I`) to open Developer Tools.
3. Open the **Command Menu** by pressing `Ctrl+Shift+P`.
4. Type `Show Rendering` and press **Enter**.
5. Scroll down inside the rendering pane to **Emulate CSS media type**.
6. Switch the dropdown selection from *No emulation* to **print**.
7. The page rendering will instantly convert to its monochrome, print-ready, expanded layout, allowing you to debug page breaking, margin alignment, and text wrapping issues in real-time.
