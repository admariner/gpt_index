"""Epub parser.

Contains parsers for epub files.
"""

from pathlib import Path
from typing import Dict

from gpt_index.readers.file.base_parser import BaseParser


class EpubParser(BaseParser):
    """Epub Parser."""

    def _init_parser(self) -> Dict:
        """Init parser."""
        return {}

    def parse_file(self, file: Path, errors: str = "ignore") -> str:
        """Parse file."""
        try:
            import ebooklib
            from ebooklib import epub
        except ImportError:
            raise ImportError(
                "`EbookLib` is required to read Epub files: `pip install EbookLib`"
            )
        try:
            import html2text
        except ImportError:
            raise ImportError(
                "`html2text` is required to parse Epub files: `pip install html2text`"
            )

        book = epub.read_epub(file, options={"ignore_ncx": True})

        text_list = [
            html2text.html2text(item.get_content().decode("utf-8"))
            for item in book.get_items()
            if item.get_type() == ebooklib.ITEM_DOCUMENT
        ]
        return "\n".join(text_list)
