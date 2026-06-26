import os
import sys
from html.parser import HTMLParser

class TagValidator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.tags_stack = []
        self.errors = []
        # Self-closing tags in HTML5
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

def validate_file(file_path):
    filename = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    parser = TagValidator(filename)
    try:
        parser.feed(content)
    except Exception as e:
        print(f"[{filename}] CRITICAL ERROR parsing file: {e}")
        return False, [f"Critical parse error: {e}"], []
        
    unclosed_errors = []
    if parser.tags_stack:
        for tag, pos in reversed(parser.tags_stack):
            unclosed_errors.append(f"Unclosed tag <{tag}> opened at line {pos[0]}, col {pos[1]}")
            
    return len(parser.errors) == 0 and len(unclosed_errors) == 0, parser.errors, unclosed_errors

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
    
    all_success = True
    for filename in files:
        file_path = os.path.join(base_dir, filename)
        if not os.path.exists(file_path):
            print(f"ERROR: {filename} does not exist in {base_dir}")
            all_success = False
            continue
            
        success, mismatches, unclosed = validate_file(file_path)
        if success:
            print(f"SUCCESS: {filename} is valid.")
        else:
            all_success = False
            print(f"FAILURE: {filename} has structural errors.")
            if mismatches:
                print("  Mismatches / Unexpected tags:")
                for m in mismatches[:10]:
                    print(f"    - {m}")
            if unclosed:
                print("  Unclosed tags:")
                for u in unclosed[:10]:
                    print(f"    - {u}")
            print()
            
    if not all_success:
        print("Overall status: FAIL")
        sys.exit(1)
    else:
        print("Overall status: PASS")
        sys.exit(0)

if __name__ == "__main__":
    main()
