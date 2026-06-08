import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\sayan\Downloads\biochem Note X\BIOCHEM_MODULE_4\module04_protein_haemoglobin.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("=== Section 4 End ===")
idx4 = content.find('CO poisoning.')
if idx4 != -1:
    print(repr(content[idx4-50:idx4+200]))

print("\n=== Section 6 End ===")
idx6 = content.find('HPFH) is actually protective')
if idx6 != -1:
    print(repr(content[idx6-150:idx6+200]))

print("\n=== Section 8 End ===")
idx8 = content.find('Direct &lt;0.3 mg/dL.')
if idx8 != -1:
    print(repr(content[idx8-100:idx8+200]))
