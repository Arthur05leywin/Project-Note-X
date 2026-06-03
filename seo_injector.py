import os
import re

domain = "https://www.caffeineandcadaver.dpdns.org"
image_url = f"{domain}/Caffeine%20&%20Cadaver.jpg"

schema_script = f"""
    <!-- JSON-LD SEO Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "EducationalOrganization",
          "name": "Caffeine & Cadaver",
          "url": "{domain}",
          "logo": "{domain}/logo-full.png"
        }},
        {{
          "@type": "Product",
          "name": "MBBS Biochemistry Masterclass & Revision Notes",
          "description": "Complete high-yield biochemistry notes and PYQs for MBBS students.",
          "image": "{image_url}",
          "brand": {{
            "@type": "Brand",
            "name": "Caffeine & Cadaver"
          }},
          "offers": {{
            "@type": "Offer",
            "price": "49",
            "priceCurrency": "INR",
            "availability": "https://schema.org/InStock"
          }}
        }}
      ]
    }}
    </script>
"""

# Get all HTML files in root directory
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update og:url
    page_url = f"{domain}/{filename}" if filename != 'index.html' else f"{domain}/"
    content = re.sub(
        r'<meta\s+property="og:url"\s+content="[^"]*">',
        f'<meta property="og:url" content="{page_url}">',
        content
    )

    # Prepare tags to inject
    inject_tags = f"""
    <link rel="canonical" href="{page_url}">
    <meta property="og:image" content="{image_url}">
    <meta property="twitter:image" content="{image_url}">"""

    if filename == 'index.html':
        inject_tags += schema_script

    # Inject tags right before </head> if not already there
    if '<link rel="canonical"' not in content:
        content = content.replace('</head>', f'{inject_tags}\n  </head>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated SEO tags in {len(html_files)} HTML files.")
