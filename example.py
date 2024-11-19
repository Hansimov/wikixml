import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from wikixml import ZhWikiBz2Parser

if __name__ == "__main__":
    wiki_xml_bz2 = "zhwiki-20241101-pages-meta-current.xml.bz2"
    file_path = Path(__file__).parent / "data" / wiki_xml_bz2
    parser = ZhWikiBz2Parser(file_path)
    parser.preview_lines(100)
    # parser.preview_pages(max_pages=10000)

    # python example.py
