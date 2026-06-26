# Implementation Plan: Anatomy PYQ Integration & Validation

This plan outlines the milestones for cross-referencing Past Year Questions (PYQs) against the 10 anatomy HTML modules, updating the modules with missing topics, and validating the structural integrity of the modified files.

## Milestones

### Milestone 1: Exploration, Extraction & Cross-referencing
- **Objective**: Identify all high-yield PYQ topics from `anatomy_pyq_text.txt` and compare them with the 10 completed HTML modules to locate gaps.
- **Tasks**:
  1. Parse `anatomy_pyq_text.txt` to extract questions for each region.
  2. Inspect each of the 10 anatomy HTML files for coverage of these topics.
  3. Identify missing or insufficiently covered topics.
- **Verification**: An exploration report (`.agents/explorer_1/gaps_report.md`) detailing the exact gaps identified for each module.

### Milestone 2: Implementation of Missing Topics
- **Objective**: Update the HTML files to include the missing topics seamlessly.
- **Tasks**:
  1. Add missing topics using the established styling (`.card`, `.clinical-box`, `.mnemonic-box`, `.keypoint`, `.warn-box`).
  2. Embed appropriate PYQ badges (e.g., `<span class="badge badge-pyq">PYQ 2018</span>`).
  3. Keep changes clean and localized to avoid bloating.
- **Verification**: Modified HTML files containing the new content and badges.

### Milestone 3: HTML Structure Validation
- **Objective**: Verify that the modified files maintain structural compliance and do not have unclosed tags or broken styling.
- **Tasks**:
  1. Create and execute a validation script to parse the modified HTML files and check for tags, structural integrity, and CSS rendering.
- **Verification**: Test logs showing 100% passing validation checks for all updated HTML files.

### Milestone 4: Final Synthesis & Review
- **Objective**: Review the changes, run the Forensic Audit, and compile the final summary report.
- **Tasks**:
  1. Run the Forensic Auditor to verify there are no integrity violations.
  2. Compile a detailed summary report of modified files, added topics, and validation status.
- **Verification**: Complete and clean Forensic Audit verdict and final human-facing report.
