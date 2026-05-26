import pypdf
import sys
import re

pdf_path = r"c:\Users\sayan\Downloads\biochem Note X\BIOCHEM_PYQ_2010-25.pdf"

def extract_pyqs():
    try:
        reader = pypdf.PdfReader(pdf_path)
        print(f"Total Pages: {len(reader.pages)}")
        
        keywords = ["lipid", "fatty", "oxidation", "cholesterol", "ketone", "ketogenesis", "lipoprotein", "hdl", "ldl", "surfactant", "statin", "atherosclerosis", "chylomicron", "phytanic", "refsum", "dka", "ketosis"]
        
        matches = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            for line in text.split("\n"):
                # If any keyword is in the line (case insensitive)
                if any(re.search(rf"\b{kw}\b", line, re.IGNORECASE) for kw in keywords):
                    matches.append((i+1, line.strip()))
                    
        print(f"Found {len(matches)} matching PYQ lines:")
        for page_num, line in matches[:40]:
            print(f"Page {page_num}: {line}")
            
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    extract_pyqs()
