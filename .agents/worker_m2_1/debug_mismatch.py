import re
from html.parser import HTMLParser

class DetailedValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        
    def handle_starttag(self, tag, attrs):
        self_closing = {'img', 'br', 'hr', 'meta', 'link', 'input', 'col', 'embed', 'param', 'source', 'track', 'wbr'}
        if tag not in self_closing:
            self.stack.append((tag, self.getpos()))
            if self.getpos()[0] >= 1400:
                print(f"[{self.getpos()[0]}] START <{tag}> - stack len: {len(self.stack)}")
            
    def handle_endtag(self, tag):
        self_closing = {'img', 'br', 'hr', 'meta', 'link', 'input', 'col', 'embed', 'param', 'source', 'track', 'wbr'}
        if tag in self_closing:
            return
            
        if not self.stack:
            print(f"[{self.getpos()[0]}] Empty stack! Unexpected </{tag}>")
            return
            
        expected, pos = self.stack.pop()
        if self.getpos()[0] >= 1400:
            print(f"[{self.getpos()[0]}] END </{tag}> (expected </{expected}> opened at {pos[0]}) - stack len: {len(self.stack)}")
        if expected != tag:
            print(f"  Mismatch! Expected </{expected}>, got </{tag}>")
            self.stack.append((expected, pos))

with open(r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module02_upper_limb.html", "r", encoding="utf-8") as f:
    content = f.read()

parser = DetailedValidator()
parser.feed(content)
print("Parsing complete.")
print("Remaining stack:")
for tag, pos in reversed(parser.stack):
    print(f"  - <{tag}> opened at line {pos[0]}, col {pos[1]}")
