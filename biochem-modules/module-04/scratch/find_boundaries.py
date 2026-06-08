import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\sayan\Downloads\biochem Note X\BIOCHEM_MODULE_4\module04_protein_haemoglobin.html"

with open(html_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the start of Section 7, Section 8, Section 9, and Section 10
s7_line = -1
s8_line = -1
s9_line = -1
s10_line = -1

for idx, line in enumerate(lines, 1):
    if 'id="s7"' in line:
        s7_line = idx
    elif 'id="s8"' in line:
        s8_line = idx
    elif 'id="s9"' in line:
        s9_line = idx
    elif 'id="s10"' in line:
        s10_line = idx

print(f"Section 7 starts at line: {s7_line}")
print(f"Section 8 starts at line: {s8_line}")
print(f"Section 9 starts at line: {s9_line}")
print(f"Section 10 starts at line: {s10_line}")

# Print around Section 7 start and end (before Section 8 start)
print("\n=== SECTION 7 BOUNDARY STUFF ===")
for j in range(max(0, s7_line-5), s7_line+15):
    print(f"{j+1}: {lines[j].strip()}")

print("\n=== SECTION 7 END STUFF ===")
for j in range(s8_line-10, s8_line+5):
    print(f"{j+1}: {lines[j].strip()}")

# Print around Section 9 start and end (before Section 10 start)
print("\n=== SECTION 9 BOUNDARY STUFF ===")
for j in range(max(0, s9_line-5), s9_line+15):
    print(f"{j+1}: {lines[j].strip()}")

print("\n=== SECTION 9 END STUFF ===")
for j in range(s10_line-10, s10_line+5):
    print(f"{j+1}: {lines[j].strip()}")
