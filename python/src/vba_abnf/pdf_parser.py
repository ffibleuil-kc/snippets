from pathlib import Path
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextLine, LTTextBox

import humanfriendly


with humanfriendly.Timer(resumable=True) as t:
    pages = list(extract_pages(Path(__file__).parent / "[MS-VBAL].pdf"))

print(f"Time taken: {t}")
print(f"Number of pages: {len(pages)}")

for single_page in pages:
    if single_page.pageid not in {88}:
        continue
    header_printed = False
    unprocessed_types = set()
    for page_element in single_page:
        if isinstance(page_element, LTTextBox):
            text = page_element.get_text().encode()
            if b"=" in text:
                if not header_printed:
                    print
                    header_printed = True
                print(text.decode("utf-8", errors="strict"))
        else:
            unprocessed_types.add(type(page_element))
