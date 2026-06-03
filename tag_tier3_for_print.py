import os
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

def process_file(filepath):
    print(f"Processing: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <summary> tags
    summaries = soup.find_all('summary')
    tagged_count = 0

    for summary in summaries:
        text = summary.get_text().upper()
        if "TIER 3" in text or "LOW-YIELD" in text or "ESSAY QUESTION TEMPLATES" in text:
            # We found a target, let's find the parent <details> tag
            details = summary.find_parent('details')
            if details:
                # Add the 'd-print-none' class
                classes = details.get('class', [])
                if 'd-print-none' not in classes:
                    classes.append('d-print-none')
                    details['class'] = classes
                    tagged_count += 1
                    print(f"  Tagged details: {text.strip()}")

    if tagged_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"  Successfully tagged {tagged_count} elements.")
    else:
        print("  No target elements found to tag.")

if __name__ == "__main__":
    files_to_process = [
        r"c:\Users\sayan\Downloads\biochem Note X\modules\module-07\module07_biological_oxidation_X.html"
    ]

    for filepath in files_to_process:
        if os.path.exists(filepath):
            process_file(filepath)
        else:
            print(f"File not found: {filepath}")
