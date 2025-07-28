import fitz
import json
import statistics

def is_likely_table_region(page):
    table_regions = []
    blocks = page.get_text("blocks")
    return table_regions

def extract_professional(pdf_path):
    doc = fitz.open(pdf_path)
    output = {"title": "Untitled Document", "outline": []}
    heading_candidates = []

    all_blocks = []
    for page_num, page in enumerate(doc):
        blocks = page.get_text("blocks", sort=True)
        for b in blocks:
            text = b[4].strip().replace('\n', ' ')
            if not text:
                continue
            
            all_blocks.append({
                "text": text,
                "bbox": b[:4],
                "page": page_num + 1
            })

    for block in all_blocks:
        text = block["text"]
        
        if not (0 < len(text.split()) < 12):
            continue

        if text.count('.') > 1 or text.count('(') > 1 or text.count('%') > 0:
            continue
        
        if not text[0].isupper() or text.endswith(('.', ':', ',')):
            continue
            
        if any(len(word) > 20 for word in text.split()):
            continue
        
        heading_candidates.append(block)

    if not heading_candidates:
        return {"title": "No suitable headings found", "outline": []}

    font_size_map = {}
    for page_num, page in enumerate(doc):
        blocks_dict = page.get_text("dict")["blocks"]
        for b in blocks_dict:
            if b.get("lines"):
                for l in b["lines"]:
                    text = "".join(s["text"] for s in l["spans"]).strip().replace('\n', ' ')
                    if text:
                        font_size_map[text] = round(l["spans"][0]["size"])
    
    for h in heading_candidates:
        h["size"] = font_size_map.get(h["text"], 0)

    heading_candidates = [h for h in heading_candidates if h["size"] > 0]
    
    unique_sizes = sorted(list({h["size"] for h in heading_candidates}), reverse=True)
    size_to_level = {size: f"H{i+1}" for i, size in enumerate(unique_sizes[:3])}

    title_found = False
    for heading in heading_candidates:
        size = heading["size"]
        if size in size_to_level:
            level = size_to_level[size]
            if level == "H1" and not title_found:
                output["title"] = heading["text"]
                title_found = True
            else:
                output["outline"].append({
                    "level": level,
                    "text": heading["text"],
                    "page": heading["page"]
                })

    return output

pdf_file = 'input.pdf'
try:
    structure = extract_professional(pdf_file)
    print(json.dumps(structure, indent=4))
except FileNotFoundError:
    print(f"ERROR: The file '{pdf_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")