import os
from bs4 import BeautifulSoup

file_path = r'c:\Users\sayan\Downloads\biochem Note X\modules\module-07\module07_biological_oxidation_X.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

count = 0
for element in soup.find_all('div', class_=['big-picture', 'clinical-box']):
    # Add d-print-none class
    classes = element.get('class', [])
    if 'd-print-none' not in classes:
        classes.append('d-print-none')
        element['class'] = classes
        count += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f"Added d-print-none to {count} big-picture and clinical-box elements.")
