import os
from bs4 import BeautifulSoup

file_path = r'c:\Users\sayan\Downloads\biochem Note X\modules\module-07\module07_biological_oxidation_X.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Define classes that protect their contents from being pruned
protected_classes = [
    'viva-ans', 'key-fact', 'mnemonic', 'card', 'flow-box', 
    'clinical-box', 'big-picture', 'summary', 'viva-q', 'viva-year'
]

def is_protected(element):
    # Check if element or any of its parents have a protected class
    current = element
    while current and current.name != 'body':
        if current.has_attr('class'):
            for c in current['class']:
                if c in protected_classes:
                    return True
        current = current.parent
    return False

pruned_count_p = 0
pruned_count_ul = 0

# Prune <p> tags
for p in soup.find_all('p'):
    if not is_protected(p):
        p.decompose()
        pruned_count_p += 1

# Prune <ul> and <ol> tags
for lst in soup.find_all(['ul', 'ol']):
    # Don't prune lists that are part of the TOC or other structural elements if any,
    # though TOC is usually hidden in print anyway. Let's protect TOC just in case.
    if lst.parent and lst.parent.has_attr('class') and 'toc' in lst.parent['class']:
        continue
    if not is_protected(lst):
        lst.decompose()
        pruned_count_ul += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f"Pruned {pruned_count_p} <p> tags and {pruned_count_ul} list tags from Revision guide.")
