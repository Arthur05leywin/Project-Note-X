import os
import sys
import re

# Ensure console output is in UTF-8
if sys.platform.startswith('win'):
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

def clean_css(css_str):
    # Remove whitespace and comments to make matching easier
    css_str = re.sub(r'/\*.*?\*/', '', css_str, flags=re.DOTALL)
    css_str = re.sub(r'\s+', '', css_str)
    return css_str

def check_file(file_path):
    filename = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = {
        'filename': filename,
        'two_col_ok': False,
        'two_col_details': '',
        'keypoint_ok': False,
        'keypoint_details': '',
        'keypoint_before_ok': False,
        'keypoint_before_details': '',
        'warn_box_ok': False,
        'warn_box_details': '',
        'warn_box_before_ok': False,
        'warn_box_before_details': '',
        'images_ok': True,
        'images_details': '',
        'badges_count': 0
    }
    
    # 1. Extract style block
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not style_match:
        results['two_col_details'] = 'No style block found'
        return results
    
    style_content = style_match.group(1)
    cleaned_style = clean_css(style_content)
    
    # 2. Check .two-col
    two_col_patterns = [
        r'\.two-col\{[^}]*grid-template-columns:repeat\(auto-fill,minmax\(min\(280px,100%\),1fr\)\)',
        r'\.two-col\{[^}]*grid-template-columns:repeat\(auto-fill,minmax\(min\(280px,100%\),1fr\)\);'
    ]
    for p in two_col_patterns:
        if re.search(p, cleaned_style):
            results['two_col_ok'] = True
            break
    if not results['two_col_ok']:
        # Let's find what .two-col matches
        match = re.search(r'\.two-col\{([^}]+)\}', cleaned_style)
        results['two_col_details'] = f"Found: .two-col{{{match.group(1)}}}" if match else "Not found"
        
    # 3. Check .keypoint
    keypoint_match = re.search(r'\.keypoint\{([^}]+)\}', cleaned_style)
    if keypoint_match:
        rules = keypoint_match.group(1)
        has_display_block = 'display:block' in rules
        has_pos_rel = 'position:relative' in rules
        has_word_break = 'word-break:break-word' in rules
        has_overflow_wrap = 'overflow-wrap:break-word' in rules
        if has_display_block and has_pos_rel and has_word_break and has_overflow_wrap:
            results['keypoint_ok'] = True
        else:
            missing = []
            if not has_display_block: missing.append('display:block')
            if not has_pos_rel: missing.append('position:relative')
            if not has_word_break: missing.append('word-break:break-word')
            if not has_overflow_wrap: missing.append('overflow-wrap:break-word')
            results['keypoint_details'] = f"Missing: {', '.join(missing)}. Content: .keypoint{{{rules}}}"
    else:
        results['keypoint_details'] = ".keypoint not found"
        
    # Check .keypoint::before
    keypoint_before_match = re.search(r'\.keypoint::before\{([^}]+)\}', cleaned_style)
    if keypoint_before_match:
        rules = keypoint_before_match.group(1)
        if 'position:absolute' in rules:
            results['keypoint_before_ok'] = True
        else:
            results['keypoint_before_details'] = f"Missing position:absolute. Content: {rules}"
    else:
        results['keypoint_before_details'] = ".keypoint::before not found"
        
    # 4. Check .warn-box
    warn_box_match = re.search(r'\.warn-box\{([^}]+)\}', cleaned_style)
    if warn_box_match:
        rules = warn_box_match.group(1)
        has_display_block = 'display:block' in rules
        has_pos_rel = 'position:relative' in rules
        has_word_break = 'word-break:break-word' in rules
        has_overflow_wrap = 'overflow-wrap:break-word' in rules
        if has_display_block and has_pos_rel and has_word_break and has_overflow_wrap:
            results['warn_box_ok'] = True
        else:
            missing = []
            if not has_display_block: missing.append('display:block')
            if not has_pos_rel: missing.append('position:relative')
            if not has_word_break: missing.append('word-break:break-word')
            if not has_overflow_wrap: missing.append('overflow-wrap:break-word')
            results['warn_box_details'] = f"Missing: {', '.join(missing)}. Content: .warn-box{{{rules}}}"
    else:
        results['warn_box_details'] = ".warn-box not found"
        
    # Check .warn-box::before
    warn_box_before_match = re.search(r'\.warn-box::before\{([^}]+)\}', cleaned_style)
    if warn_box_before_match:
        rules = warn_box_before_match.group(1)
        if 'position:absolute' in rules:
            results['warn_box_before_ok'] = True
        else:
            results['warn_box_before_details'] = f"Missing position:absolute. Content: {rules}"
    else:
        results['warn_box_before_details'] = ".warn-box::before not found"
        
    # 5. Check images
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    invalid_images = []
    for src in img_srcs:
        if 'commons.wikimedia.org' in src:
            if not src.startswith('https://commons.wikimedia.org/wiki/Special:FilePath/'):
                invalid_images.append(src)
    if invalid_images:
        results['images_ok'] = False
        results['images_details'] = f"Invalid Wikimedia URLs: {invalid_images}"
        
    # 6. Count badges
    badges = re.findall(r'class=["\']badge\s+badge-(?:pyq|fav)["\']', content)
    results['badges_count'] = len(badges)
    
    return results

def main():
    base_dir = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules"
    files = [
        "module01_general_anatomy.html",
        "anatomy_module02_upper_limb.html",
        "anatomy_module03_lower_limb.html",
        "anatomy_module04_thorax.html",
        "anatomy_module05_abdomen.html",
        "anatomy_module06_pelvis_perineum.html",
        "anatomy_module07_head_neck.html",
        "module08_neuroanatomy.html",
        "module09_embryology.html",
        "module10_histology.html"
    ]
    
    print("STYLE COMPLIANCE REPORT\n" + "="*80)
    all_ok = True
    for filename in files:
        file_path = os.path.join(base_dir, filename)
        if not os.path.exists(file_path):
            print(f"{filename}: File not found")
            all_ok = False
            continue
            
        res = check_file(file_path)
        print(f"File: {res['filename']}")
        
        # Output checks
        def print_status(name, ok, details):
            status = "PASS" if ok else "FAIL"
            print(f"  - {name}: {status} {details}")
            
        print_status(".two-col", res['two_col_ok'], res['two_col_details'])
        print_status(".keypoint", res['keypoint_ok'], res['keypoint_details'])
        print_status(".keypoint::before", res['keypoint_before_ok'], res['keypoint_before_details'])
        print_status(".warn-box", res['warn_box_ok'], res['warn_box_details'])
        print_status(".warn-box::before", res['warn_box_before_ok'], res['warn_box_before_details'])
        print_status("Wikimedia URLs", res['images_ok'], res['images_details'])
        print(f"  - Badge count: {res['badges_count']}")
        print("-"*80)
        
        file_ok = (res['two_col_ok'] and res['keypoint_ok'] and res['keypoint_before_ok'] and 
                   res['warn_box_ok'] and res['warn_box_before_ok'] and res['images_ok'])
        if not file_ok:
            all_ok = False
            
    if all_ok:
        print("Overall Style Compliance Status: PASS")
    else:
        print("Overall Style Compliance Status: FAIL")

if __name__ == "__main__":
    main()
