import os
import glob

base_dir = r"c:\Users\sayan\Downloads\biochem Note X"
css_files = glob.glob(os.path.join(base_dir, "**", "wbuhs_master_style.css"), recursive=True)

for file in css_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to change `margin: 8px 0 !important;` to `margin: 8px auto !important;`
    # and maybe add `width: 100% !important;` to ensure they span and center.
    # Let's target the exact blocks:
    #   .flow-arrow, .arrow {
    #     display: inline-block !important;
    #     transform: rotate(90deg) !important;
    #     margin: 8px 0 !important;
    #     text-align: center !important;
    #   }
    # 
    #   .flow-arrow.down, .arrow-down {
    #     transform: none !important;
    #     margin: 8px 0 !important;
    #     max-width: 100% !important;
    #   }

    content = content.replace(
        "margin: 8px 0 !important;\n    text-align: center !important;",
        "margin: 8px auto !important;\n    width: 100% !important;\n    text-align: center !important;"
    )
    content = content.replace(
        "margin: 8px 0 !important;\n    max-width: 100% !important;",
        "margin: 8px auto !important;\n    width: 100% !important;\n    text-align: center !important;\n    max-width: 100% !important;"
    )

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated {len(css_files)} CSS files.")
