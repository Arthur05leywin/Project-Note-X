import os

files = [
    r'c:\Users\sayan\Downloads\biochem Note X\anatomy modules\module09_embryology.html',
    r'c:\Users\sayan\Downloads\biochem Note X\anatomy modules\module10_histology.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('<img src="https://commons.wikimedia.org/wiki/Special:FilePath/', '<img referrerpolicy="no-referrer" src="https://commons.wikimedia.org/wiki/Special:FilePath/')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {os.path.basename(filepath)}")
    else:
        print(f"No changes needed for {os.path.basename(filepath)}")
