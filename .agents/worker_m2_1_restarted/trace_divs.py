from html.parser import HTMLParser

class DivTracer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            cls = next((v for k, v in attrs if k == 'class'), '')
            id_ = next((v for k, v in attrs if k == 'id'), '')
            desc = f"div.{cls}" if cls else "div"
            if id_:
                desc += f"#{id_}"
            self.stack.append((desc, self.getpos()))
            
    def handle_endtag(self, tag):
        if tag == 'div':
            if not self.stack:
                print(f"Extra </div> at line {self.getpos()[0]}")
                return
            desc, pos = self.stack.pop()
            if "content" in desc or not self.stack:
                print(f"Closed {desc} (opened line {pos[0]}) at line {self.getpos()[0]}. Stack size: {len(self.stack)}")

tracer = DivTracer()
with open(r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module02_upper_limb.html", "r", encoding="utf-8") as f:
    tracer.feed(f.read())
