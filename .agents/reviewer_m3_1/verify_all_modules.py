import os
import re
import json
from html.parser import HTMLParser

class TagValidator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.tags_stack = []
        self.errors = []
        self.self_closing = {'img', 'br', 'hr', 'meta', 'link', 'input', 'col', 'embed', 'param', 'source', 'track', 'wbr'}
        
    def handle_starttag(self, tag, attrs):
        if tag not in self.self_closing:
            self.tags_stack.append((tag, self.getpos()))
            
    def handle_endtag(self, tag):
        if tag in self.self_closing:
            return
        if not self.tags_stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
            return
        expected_tag, pos = self.tags_stack.pop()
        if expected_tag != tag:
            self.errors.append(
                f"Mismatched tag: expected </{expected_tag}> (opened at line {pos[0]}, col {pos[1]}), "
                f"but found </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}"
            )
            # Put the expected tag back to attempt recovery
            self.tags_stack.append((expected_tag, pos))

def run_checks():
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
    
    results = {}
    for filename in files:
        file_path = os.path.join(base_dir, filename)
        if not os.path.exists(file_path):
            print(f"Error: {file_path} does not exist.")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. HTML Tag Balance Check
        parser = TagValidator(filename)
        parser.feed(content)
        unclosed = []
        if parser.tags_stack:
            for tag, pos in reversed(parser.tags_stack):
                unclosed.append(f"Unclosed <{tag}> at line {pos[0]}, col {pos[1]}")
                
        # 2. Check CSS styling for .two-col
        two_col_norm = re.sub(r'\s+', '', content)
        two_col_ok = 'grid-template-columns:repeat(auto-fill,minmax(min(280px,100%),1fr))' in two_col_norm or 'grid-template-columns:repeat(auto-fill,minmax(min(280px,100%),1fr));' in two_col_norm
        
        # 3. Check CSS styling for .keypoint and .warn-box
        keypoint_css_match = re.search(r'\.keypoint\s*\{([^}]+)\}', content)
        warnbox_css_match = re.search(r'\.warn-box\s*\{([^}]+)\}', content)
        
        def check_box_css(css_text):
            if not css_text:
                return False, ["Not found"]
            norm = re.sub(r'\s+', '', css_text)
            checks = ['display:block', 'position:relative', 'word-break:break-word', 'overflow-wrap:break-word']
            missing = [c for c in checks if c not in norm]
            return len(missing) == 0, missing

        keypoint_ok, keypoint_missing = check_box_css(keypoint_css_match.group(1) if keypoint_css_match else "")
        warnbox_ok, warnbox_missing = check_box_css(warnbox_css_match.group(1) if warnbox_css_match else "")
        
        # 4. Check Wikimedia images URL format
        img_tags = re.findall(r'<img[^>]+>', content)
        invalid_imgs = []
        for img in img_tags:
            src_match = re.search(r'src=["\']([^"\']+)["\']', img)
            if src_match:
                src = src_match.group(1)
                # Check if it is a wikimedia URL.
                if 'wikimedia.org' in src or 'wikipedia.org' in src:
                    if not src.startswith('https://commons.wikimedia.org/wiki/Special:FilePath/'):
                        invalid_imgs.append(src)
                elif src.startswith('http'):
                    # Any external URL that is not Special:FilePath is logged
                    if not src.startswith('https://commons.wikimedia.org/wiki/Special:FilePath/'):
                        invalid_imgs.append(src)
            
        # 5. Check badges
        pyq_badges = len(re.findall(r'class="badge badge-pyq"', content))
        fav_badges = len(re.findall(r'class="badge badge-fav"', content))
        
        results[filename] = {
            "html_valid": len(parser.errors) == 0 and len(unclosed) == 0,
            "html_errors": parser.errors,
            "html_unclosed": unclosed,
            "two_col_ok": two_col_ok,
            "keypoint_ok": keypoint_ok,
            "keypoint_missing": keypoint_missing,
            "warnbox_ok": warnbox_ok,
            "warnbox_missing": warnbox_missing,
            "invalid_imgs": invalid_imgs,
            "pyq_badges": pyq_badges,
            "fav_badges": fav_badges,
            "total_imgs": len(img_tags)
        }
        
    return results

if __name__ == '__main__':
    res = run_checks()
    print(json.dumps(res, indent=2))
