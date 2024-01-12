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
        print(str(page_element))
    #     if isinstance(page_element, LTTextBox):
    #         text = page_element.get_text()
    #         if "=" in text:
    #             if not header_printed:
    #                 print(f"===== Page #{single_page.pageid} =====")
    #                 header_printed = True
    #             print(f"Processed type: {type(page_element)}")
    #             print(text)
    #             print(str(page_element))
    #     else:
    #         unprocessed_types.add(type(page_element))
    # if unprocessed_types and header_printed:
    #     print(f"Unprocessed types for page {single_page.pageid}: {unprocessed_types}")
