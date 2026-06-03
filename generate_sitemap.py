import os
import datetime

domain = "https://www.caffeineandcadaver.dpdns.org"

html_files = [f for f in os.listdir('.') if f.endswith('.html') and 'gemini' not in f.lower()]
# Note: we might want to ignore scratch or gemini files

date_str = datetime.datetime.now().strftime("%Y-%m-%d")

sitemap_urls = []
for f in html_files:
    if f == "index.html":
        loc = f"{domain}/"
        priority = "1.0"
    elif f == "biochemistry.html":
        loc = f"{domain}/{f}"
        priority = "0.9"
    elif f == "packs.html":
        loc = f"{domain}/{f}"
        priority = "0.8"
    else:
        loc = f"{domain}/{f}"
        priority = "0.6"
    
    url_node = f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{date_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>"""
    sitemap_urls.append(url_node)

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>"""

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

robots_content = f"""User-agent: *
Allow: /

Sitemap: {domain}/sitemap.xml"""

with open('robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_content)

print(f"Generated sitemap.xml with {len(html_files)} URLs and robots.txt.")
