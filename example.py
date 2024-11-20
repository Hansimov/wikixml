import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from wikixml import WikiXmlParser

if __name__ == "__main__":
    wiki_xml_bz2 = "zhwiki-20241101-pages-meta-current.xml.bz2"
    file_path = Path(__file__).parent / "data" / wiki_xml_bz2
    parser = WikiXmlParser(file_path)
    # parser.preview_lines(5000)
    parser.preview_pages(max_pages=100)

    # python example.py
