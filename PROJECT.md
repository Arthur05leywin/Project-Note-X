# Project: Anatomy Notes PYQ Integration & Validation

## Architecture
- **Source Material**: `anatomy_pyq_text.txt` containing past paper questions from 2010-2025.
- **Anatomy Modules**: 10 completed HTML modules located in `anatomy modules/`:
  1. `module01_general_anatomy.html`
  2. `anatomy_module02_upper_limb.html`
  3. `anatomy_module03_lower_limb.html`
  4. `anatomy_module04_thorax.html`
  5. `anatomy_module05_abdomen.html`
  6. `anatomy_module06_pelvis_perineum.html`
  7. `anatomy_module07_head_neck.html`
  8. `module08_neuroanatomy.html`
  9. `module09_embryology.html`
  10. `module10_histology.html`
- **Infrastructure**: Custom HTML/CSS templates, validation script.

## Milestones
| # | Name | Scope | Dependencies | Status | Conv ID |
|---|------|-------|-------------|--------|---------|
| 1 | Exploration & Analysis | Parse PYQs and identify gaps in modules | None | DONE | 35ce96fa, d667fb68, 335e8228 |
| 2 | Implementation of Gaps | Update HTML files with missing topics & badges | M1 | DONE | d7002760, edccd7b5, d860261b |
| 3 | Validation | Run script to verify HTML structure | M2 | DONE | ba8ba683, 5b8cdd94, aeaa2e9c |
| 4 | Final Report & Audit | Run Forensic Auditor and synthesize final report | M3 | DONE | b96a2fc2 |

## Interface Contracts & Guidelines
- All modifications to HTML modules must conform to the existing CSS class names (`.card`, `.clinical-box`, `.mnemonic-box`, `.keypoint`, `.warn-box`, `.badge-pyq`).
- Unclosed HTML tags are prohibited and must be verified programmatically.
- No dummy or hardcoded verification logic.
