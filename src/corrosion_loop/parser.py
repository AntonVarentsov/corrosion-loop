"""PDF parsing utilities."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, Tuple

import pdfplumber

from .database import get_session
from .models import Document, Equipment, LineNumber

LINE_PATTERN = re.compile(r"\b\d{2,}-\d{2,}\b")
EQUIP_PATTERN = re.compile(r"[A-Z]-?\d{3}")


class PDFParser:
    """Parse P&ID PDF files and store results in the database."""

    def __init__(self, pdf_path: Path):
        self.pdf_path = Path(pdf_path)

    def parse(self) -> None:
        document = Document(doc_name=self.pdf_path.name, file_path=str(self.pdf_path))
        with get_session() as session:
            session.add(document)
            session.commit()

            with pdfplumber.open(self.pdf_path) as pdf:
                for page_number, page in enumerate(pdf.pages, start=1):
                    for text, bbox in self._iter_text(page):
                        if LINE_PATTERN.fullmatch(text):
                            session.add(
                                LineNumber(
                                    line_number=text,
                                    document_id=document.document_id,
                                    page_number=page_number,
                                    x0=bbox[0],
                                    y0=bbox[1],
                                    x1=bbox[2],
                                    y1=bbox[3],
                                )
                            )
                        elif EQUIP_PATTERN.fullmatch(text):
                            session.add(
                                Equipment(
                                    equip_tag=text,
                                    document_id=document.document_id,
                                    page_number=page_number,
                                    x0=bbox[0],
                                    y0=bbox[1],
                                    x1=bbox[2],
                                    y1=bbox[3],
                                )
                            )
            session.commit()

    @staticmethod
    def _iter_text(page) -> Iterable[Tuple[str, Tuple[float, float, float, float]]]:
        for char in page.extract_words():
            yield char["text"], (char["x0"], char["top"], char["x1"], char["bottom"])
