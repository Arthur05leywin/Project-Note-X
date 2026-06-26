from html.parser import HTMLParser

class DivTracer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        
    def handle_starttag(self, tag, attrs):
        if self.getpos()[0] >= 242 and self.getpos()[0] <= 385:
            if tag == 'div':
                cls = next((v for k, v in attrs if k == 'class'), '')
                id_ = next((v for k, v in attrs if k == 'id'), '')
                desc = f"div.{cls}" if cls else "div"
                if id_:
                    desc += f"#{id_}"
                self.stack.append((desc, self.getpos()))
                print(f"[{self.getpos()[0]}] Pushed {desc}")
            
    def handle_endtag(self, tag):
        if self.getpos()[0] >= 242 and self.getpos()[0] <= 385:
            if tag == 'div':
                if not self.stack:
                    print(f"[{self.getpos()[0]}] Extra </div> found!")
                    return
                desc, pos = self.stack.pop()
                print(f"[{self.getpos()[0]}] Popped {desc} (opened line {pos[0]})")

tracer = DivTracer()
with open(r"c:\Users\sayan\Downloads\biochem Note X\anatomy modules\anatomy_module02_upper_limb.html", "r", encoding="utf-8") as f:
    tracer.feed(f.read())
