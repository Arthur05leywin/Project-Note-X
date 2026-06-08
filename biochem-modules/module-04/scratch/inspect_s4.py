import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\sayan\Downloads\biochem Note X\BIOCHEM_MODULE_4\module04_protein_haemoglobin.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# Find s4 start and s5 start
s4_start = -1
s5_start = -1
s6_start = -1
s7_start = -1

for idx, line in enumerate(lines, 1):
    if 'id="s4"' in line:
        s4_start = idx
    elif 'id="s5"' in line:
        s5_start = idx
    elif 'id="s6"' in line:
        s6_start = idx
    elif 'id="s7"' in line:
        s7_start = idx

print(f"s4 start: {s4_start}, s5 start: {s5_start}")
print(f"s6 start: {s6_start}, s7 start: {s7_start}")

print("\n=== s4 contents ===")
for j in range(s4_start-1, s4_start+35):
    print(f"{j+1}: {lines[j].strip()}")

print("\n=== s4 end ===")
for j in range(s5_start-15, s5_start):
    print(f"{j+1}: {lines[j].strip()}")

print("\n=== s6 contents ===")
for j in range(s6_start-1, s6_start+35):
    print(f"{j+1}: {lines[j].strip()}")

print("\n=== s6 end ===")
for j in range(s7_start-15, s7_start):
    print(f"{j+1}: {lines[j].strip()}")
