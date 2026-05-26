import os
import json
import glob

reports = glob.glob(r"C:\Users\sayan\.gemini\antigravity\brain\60c016ee-bc9d-4eac-86c5-6403267e4e36\*_verification_report.json")

print("| Module | Topic | Edition | Page Count |")
print("| --- | --- | --- | --- |")

data = {}

for r in sorted(reports):
    try:
        with open(r, 'r', encoding='utf-8') as f:
            js = json.load(f)
            module_id = js.get("module_id")
            title = js.get("title")
            edition = js.get("edition")
            pages = js.get("pages_detected")
            
            if module_id not in data:
                data[module_id] = {"title": title}
            
            data[module_id][edition] = pages
    except Exception as e:
        print(f"Error reading {r}: {e}")

for mid in sorted(data.keys()):
    t = data[mid]["title"]
    std = data[mid].get("standard", "—")
    rev = data[mid].get("revision", "—")
    print(f"| {mid:02d} | {t} | Standard: {std} | Revision: {rev} |")
