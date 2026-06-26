import os
import glob

base_dir = r"c:\Users\sayan\Downloads\biochem Note X"
css_files = glob.glob(os.path.join(base_dir, "**", "wbuhs_master_style.css"), recursive=True)

for file in css_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # The original CSS for mobile flow-arrow:
    #   .flow-arrow, .arrow {
    #     display: inline-block !important;
    #     transform: rotate(90deg) !important;
    #     margin: 8px auto !important;
    #     width: 100% !important;
    #     text-align: center !important;
    #   }
    
    # We want to change `transform: rotate(90deg) !important;` to `transform: none !important;`
    # This prevents the overlapping words issues on mobile, keeping text horizontal and readable.
    
    content = content.replace(
        "transform: rotate(90deg) !important;\n    margin: 8px auto !important;",
        "transform: none !important;\n    margin: 8px auto !important;"
    )
    # Also catch the older margin in case my previous script missed something
    content = content.replace(
        "transform: rotate(90deg) !important;\n    margin: 8px 0 !important;",
        "transform: none !important;\n    margin: 8px auto !important;\n    width: 100% !important;"
    )

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated {len(css_files)} CSS files.")
