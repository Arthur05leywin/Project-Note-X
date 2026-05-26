import os
from playwright.sync_api import sync_playwright

m1_path = r"c:\Users\sayan\Downloads\biochem Note X\modules\module-01\enzyme_inhibition_notes.html"
m2_path = r"c:\Users\sayan\Downloads\biochem Note X\modules\module-02\carb_metabolism_notes.html"

def get_style_info(html_path):
    file_url = f"file:///{os.path.abspath(html_path).replace('\\', '/')}"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(file_url)
        
        # Check what styles are computed on body
        bg = page.evaluate("() => window.getComputedStyle(document.body).backgroundColor")
        color = page.evaluate("() => window.getComputedStyle(document.body).color")
        font = page.evaluate("() => window.getComputedStyle(document.body).fontFamily")
        
        # Check if the brand-bar is visible or has style
        brand_bar = page.query_selector(".brand-bar")
        brand_bar_display = page.evaluate("(el) => el ? window.getComputedStyle(el).display : 'NOT_FOUND'", brand_bar)
        brand_bar_bg = page.evaluate("(el) => el ? window.getComputedStyle(el).backgroundColor : 'NOT_FOUND'", brand_bar)
        
        browser.close()
        return {
            "bg": bg,
            "color": color,
            "font": font,
            "brand_bar_display": brand_bar_display,
            "brand_bar_bg": brand_bar_bg
        }

print("Module 1:")
print(get_style_info(m1_path))
print("\nModule 2:")
print(get_style_info(m2_path))
