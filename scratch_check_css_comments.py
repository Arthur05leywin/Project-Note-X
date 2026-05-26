import os

css_path = r"c:\Users\sayan\Downloads\biochem Note X\wbuhs_master_style.css"
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Let's check comments
pos = 0
open_comments = []
close_comments = []

while True:
    idx_open = css.find("/*", pos)
    idx_close = css.find("*/", pos)
    
    if idx_open == -1 and idx_close == -1:
        break
        
    if idx_open != -1 and (idx_close == -1 or idx_open < idx_close):
        open_comments.append(idx_open)
        pos = idx_open + 2
    else:
        close_comments.append(idx_close)
        pos = idx_close + 2

print(f"Open comments count: {len(open_comments)}")
print(f"Close comments count: {len(close_comments)}")

if len(open_comments) != len(close_comments):
    print("WARNING: Comments are not balanced!")
else:
    # Check nesting
    pos = 0
    in_comment = False
    comment_start_pos = 0
    errors = 0
    for i in range(len(css) - 1):
        char = css[i:i+2]
        if char == "/*":
            if in_comment:
                print(f"Nested comment open at position {i} inside comment started at {comment_start_pos}")
                errors += 1
            in_comment = True
            comment_start_pos = i
        elif char == "*/":
            if not in_comment:
                print(f"Comment close without open at position {i}")
                errors += 1
            in_comment = False
            
    if errors == 0:
        print("CSS comment structure is perfectly clean.")
