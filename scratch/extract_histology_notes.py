import fitz
import re

pdf_path = r'c:\Users\sayan\Downloads\biochem Note X\anatomy modules\inderbir_singhs_textbook_of_human_histology_with_colour_atlas_and.pdf'
doc = fitz.open(pdf_path)

topics = {
    'liver': re.compile(r'\bliver\b', re.IGNORECASE),
    'pancreas': re.compile(r'\bpancreas\b', re.IGNORECASE),
    'lymph_node': re.compile(r'\blymph node\b', re.IGNORECASE),
    'palatine_tonsil': re.compile(r'\bpalatine tonsil\b', re.IGNORECASE),
}

extracted = {k: [] for k in topics}

for i in range(len(doc)):
    text = doc[i].get_text()
    for topic, pattern in topics.items():
        if pattern.search(text):
            extracted[topic].append(f"--- PAGE {i} ---\n{text}")

with open(r'c:\Users\sayan\Downloads\biochem Note X\scratch\raw_histology_notes.txt', 'w', encoding='utf-8') as f:
    for topic, pages in extracted.items():
        f.write(f"=== {topic.upper()} ===\n")
        # limit to the most dense pages or first 5 matches to avoid huge files
        for p in pages[:10]:
            f.write(p + "\n")
