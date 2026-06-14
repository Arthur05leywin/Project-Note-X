import os

files = ['biochemistry.html', 'contact.html', 'delivery.html', 'faq.html', 'index.html', 'packs.html', 'refund.html', 'terms.html']
old_str = '<a href="packs.html">Packs</a>'
new_str = '<a href="biochemistry.html">Biochemistry</a>\n          <a href="anatomy.html">Anatomy</a>'

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        if old_str in content:
            new_content = content.replace(old_str, new_str)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Updated {f}')
