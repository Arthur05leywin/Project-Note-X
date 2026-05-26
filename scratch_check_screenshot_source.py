import os

ROOT_DIR = r"c:\Users\sayan\Downloads\biochem Note X"
query = "Subject Biochemistry"

for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        if file.lower().endswith(".html"):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if query in content:
                    print(f"MATCH: {os.path.relpath(path, ROOT_DIR)}")
            except Exception as e:
                pass
