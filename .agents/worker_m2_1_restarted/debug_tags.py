from html.parser import HTMLParser

class DetailValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.history = []
        self.self_closing = {'img', 'br', 'hr', 'meta', 'link', 'input', 'col', 'embed', 'param', 'source', 'track', 'wbr'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.self_closing:
            self.stack.append((tag, self.getpos()))
            self.history.append(("push", tag, self.getpos(), len(self.stack)))

    def handle_endtag(self, tag):
        if tag in self.self_closing:
            return
        if not self.stack:
            print(f"Empty stack on closing tag </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
            return
        expected, pos = self.stack.pop()
        self.history.append(("pop", tag, self.getpos(), len(self.stack), expected, pos))
        if expected != tag:
            print(f"Mismatch: expected </{expected}> (opened line {pos[0]}), got </{tag}> at line {self.getpos()[0]}")
            # put back to continue
            self.stack.append((expected, pos))

validator = DetailValidator()
with open(r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module02_upper_limb.html", "r", encoding="utf-8") as f:
    validator.feed(f.read())

print("Final stack state:", validator.stack)
