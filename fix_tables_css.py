import os
import glob
import re

base_dir = r"c:\Users\sayan\Downloads\biochem Note X"
css_files = glob.glob(os.path.join(base_dir, "**", "*.css"), recursive=True)

for file in css_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    append_css = """
/* Auto-injected: Fix squashed tables and text overflows on mobile */
@media (max-width: 768px) {
  .comp-table, .table-wrap {
    display: block !important;
    width: 100% !important;
    overflow-x: auto !important;
  }
  .comp-table, .table-wrap table {
    min-width: 600px !important; /* Force horizontal scroll instead of squash */
  }
  .comp-table th, .comp-table td, .table-wrap th, .table-wrap td {
    white-space: normal !important;
    word-break: break-word !important;
    min-width: 120px !important;
  }
  .comp-table td:first-child, .table-wrap td:first-child {
    white-space: normal !important;
  }
}
"""
    if "/* Auto-injected: Fix squashed tables" not in content:
        content += append_css
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed tables in {file}")

print("Done fixing tables.")
