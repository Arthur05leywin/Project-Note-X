import os
import re

root_dir = r"c:\Users\sayan\Downloads\biochem Note X"

def fix_css(content):
    # Fix .keypoint container
    # 1. Remove display:flex, gap, align-items
    content = re.sub(r'display:\s*flex;', r'display: block; position: relative;', content) if '.keypoint' in content else content
    
    # Actually, a more targeted regex is safer
    
    # For .keypoint
    def fix_keypoint_box(m):
        inner = m.group(1)
        inner = re.sub(r'display:\s*flex;?', 'display: block; position: relative;', inner)
        inner = re.sub(r'gap:\s*8px;?', '', inner)
        inner = re.sub(r'align-items:\s*flex-start;?', '', inner)
        # Add padding-left override
        inner += ' padding-left: 34px;'
        return '.keypoint {' + inner + '}'
        
    content = re.sub(r'\.keypoint\s*\{([^}]*)\}', fix_keypoint_box, content)
    
    def fix_keypoint_before(m):
        inner = m.group(1)
        inner += ' position: absolute; left: 12px; top: 10px;'
        return '.keypoint::before {' + inner + '}'
        
    content = re.sub(r'\.keypoint::before\s*\{([^}]*)\}', fix_keypoint_before, content)

    # For .warn-box
    def fix_warn_box(m):
        inner = m.group(1)
        inner = re.sub(r'display:\s*flex;?', 'display: block; position: relative;', inner)
        inner = re.sub(r'gap:\s*8px;?', '', inner)
        inner = re.sub(r'align-items:\s*flex-start;?', '', inner)
        inner += ' padding-left: 34px;'
        return '.warn-box {' + inner + '}'
        
    content = re.sub(r'\.warn-box\s*\{([^}]*)\}', fix_warn_box, content)
    
    def fix_warn_before(m):
        inner = m.group(1)
        inner += ' position: absolute; left: 10px; top: 10px;'
        return '.warn-box::before {' + inner + '}'
        
    content = re.sub(r'\.warn-box::before\s*\{([^}]*)\}', fix_warn_before, content)

    # For .clinical-box
    def fix_clinical_box(m):
        inner = m.group(1)
        # Wait, does clinical-box have display: flex? Let me check its CSS...
        # .clinical-box is usually just a div with a title inside. 
        return '.clinical-box {' + inner + '}'
    # Not modifying clinical box right now unless it has display: flex

    return content

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html') or file.endswith('.css'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Special check to avoid double-processing
            if 'position: absolute; left: 12px; top: 10px;' not in content:
                new_content = fix_css(content)
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed: {filepath}")

print("Flex layout rendering fix completed.")
