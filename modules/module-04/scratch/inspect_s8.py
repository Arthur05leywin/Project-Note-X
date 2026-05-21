import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\sayan\Downloads\biochem Note X\BIOCHEM_MODULE_4\module04_protein_haemoglobin.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

s8_start = -1
s9_start = -1

for idx, line in enumerate(lines, 1):
    if 'id="s8"' in line:
        s8_start = idx
    elif 'id="s9"' in line:
        s9_start = idx

print(f"s8 start: {s8_start}, s9 start: {s9_start}")

print("\n=== s8 contents ===")
for j in range(s8_start-1, s8_start+30):
    print(f"{j+1}: {lines[j].strip()}")

print("\n=== s8 end ===")
for j in range(s9_start-15, s9_start):
    print(f"{j+1}: {lines[j].strip()}")
