import subprocess

cmd = ["git", "diff", r"modules/module-02/carb_metabolism_notes.html"]
result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=r"c:\Users\sayan\Downloads\biochem Note X")
diff_lines = result.stdout.splitlines()
in_style = False
filtered_lines = []

for line in diff_lines:
    if line.startswith("@@"):
        in_style = False
    if "<style>" in line:
        in_style = True
        filtered_lines.append(line + " ... [STYLE BLOCK DIFF HIDDEN]")
        continue
    if "</style>" in line:
        in_style = False
        filtered_lines.append(line)
        continue
    
    if in_style:
        continue
    else:
        filtered_lines.append(line)

diff_text = "\n".join(filtered_lines[:150])
print(diff_text.encode('ascii', errors='replace').decode('ascii'))
if len(filtered_lines) > 150:
    print(f"... and {len(filtered_lines) - 150} more lines")
