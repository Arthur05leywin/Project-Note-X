import os
from playwright.sync_api import sync_playwright

html_path = r"c:\Users\sayan\Downloads\biochem Note X\modules\module-02\carb_metabolism_notes X.html"
file_url = f"file:///{os.path.abspath(html_path).replace('\\', '/')}"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Listen to console messages
    page.on("console", lambda msg: print(f"CONSOLE: {msg.type}: {msg.text}"))
    page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
    
    print(f"Loading {file_url}...")
    page.goto(file_url)
    
    # Check what styles are computed on body
    body_bg = page.evaluate("() => window.getComputedStyle(document.body).backgroundColor")
    body_color = page.evaluate("() => window.getComputedStyle(document.body).color")
    body_font = page.evaluate("() => window.getComputedStyle(document.body).fontFamily")
    
    print("\nComputed styles on body:")
    print(f"  Background color: {body_bg}")
    print(f"  Text color: {body_color}")
    print(f"  Font family: {body_font}")
    
    browser.close()
