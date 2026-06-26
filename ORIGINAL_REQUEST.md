# Original User Request

## Initial Request — 2026-06-24T00:52:17Z

# Teamwork Project Prompt — Final Draft

Cross-reference all extracted PYQs (Past Year Questions) against the 10 completed anatomy HTML modules. Identify any high-yield topics that are missing from the modules, and update the respective HTML files to include them seamlessly.

Working directory: `c:\Users\sayan\Downloads\biochem Note X`
Integrity mode: development

## Requirements

### R1. Cross-Reference PYQs
Scan `anatomy_pyq_text.txt` and compare the required topics against the contents of `anatomy modules/module01_...` through `anatomy modules/module10_histology.html`.

### R2. Update Modules with Missing Topics
If a significant PYQ topic has been omitted or insufficiently covered in the existing modules, add the missing content into the appropriate HTML module. Ensure strict adherence to the established CSS and HTML structure (e.g., using `.card`, `.keypoint`, `.warn-box`, and `.badge-pyq`). Do not modify files if they already cover the topic adequately.

## Acceptance Criteria

### Verification & Quality
- [ ] The agent team must write and run a quick Python script to validate the HTML structure of any modified files (e.g., checking for unclosed tags) before considering the task complete.
- [ ] A summary report is generated detailing which PYQ topics were missing and exactly which HTML files were modified to include them.
- [ ] All newly added topics feature the correct `<span class="badge badge-pyq">` elements.
