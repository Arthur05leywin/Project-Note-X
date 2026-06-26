import os
from html.parser import HTMLParser

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags_stack = []
        self.errors = []
        
    def handle_starttag(self, tag, attrs):
        # Self-closing tags in HTML5 do not need a closing tag
        self_closing = {'img', 'br', 'hr', 'meta', 'link', 'input', 'col', 'embed', 'param', 'source', 'track', 'wbr'}
        if tag not in self_closing:
            self.tags_stack.append((tag, self.getpos()))
            
    def handle_endtag(self, tag):
        self_closing = {'img', 'br', 'hr', 'meta', 'link', 'input', 'col', 'embed', 'param', 'source', 'track', 'wbr'}
        if tag in self_closing:
            return
            
        if not self.tags_stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
            return
            
        expected_tag, pos = self.tags_stack.pop()
        if expected_tag != tag:
            self.errors.append(f"Mismatched tag: expected </{expected_tag}> (opened at line {pos[0]}, col {pos[1]}), but found </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
            # Put expected tag back to attempt recovery
            self.tags_stack.append((expected_tag, pos))

def validate_html(file_path):
    print(f"\nValidating {os.path.basename(file_path)}:")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    parser = TagValidator()
    try:
        parser.feed(content)
        if parser.errors:
            print(f"  Found {len(parser.errors)} errors:")
            for err in parser.errors:
                print(f"    - {err}")
        else:
            print("  No tag mismatch errors found.")
            
        if parser.tags_stack:
            print(f"  Warning: {len(parser.tags_stack)} unclosed tags at end of file:")
            for tag, pos in reversed(parser.tags_stack):
                print(f"    - <{tag}> opened at line {pos[0]}, col {pos[1]}")
    except Exception as e:
        print(f"  Failed to parse HTML: {e}")

if __name__ == "__main__":
    base_dir = r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules"
    files = [
        "anatomy_module05_abdomen.html",
        "anatomy_module06_pelvis_perineum.html",
        "anatomy_module07_head_neck.html"
    ]
    for filename in files:
        validate_html(os.path.join(base_dir, filename))
