import os

html_path = r"c:\Users\sayan\Downloads\biochem Note X\modules\module-02\carb_metabolism_notes.html"
with open(html_path, 'rb') as f:
    content_bytes = f.read()

# Let's find the start of the style tag
style_start = content_bytes.find(b'<style>')
if style_start != -1:
    print(f"<style> found at byte: {style_start}")
    print("Next 100 bytes of style content:")
    print(content_bytes[style_start:style_start+200])
else:
    # Let's search for case-insensitive <style
    style_start = content_bytes.lower().find(b'<style')
    print(f"<style case-insensitive found at byte: {style_start}")
    if style_start != -1:
        print(content_bytes[style_start:style_start+200])
