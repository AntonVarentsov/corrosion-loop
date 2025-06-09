"""Command-line interface for the corrosion loop parser."""

from __future__ import annotations

import argparse
from pathlib import Path

from .exporter import export_to_excel
from .parser import PDFParser


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse P&ID PDFs")
    parser.add_argument("pdf_dir", type=Path, help="Directory with PDF files")
    parser.add_argument("output", type=Path, help="Excel output file")
    args = parser.parse_args()

    for pdf_path in args.pdf_dir.glob("*.pdf"):
        PDFParser(pdf_path).parse()

    export_to_excel(args.output)


if __name__ == "__main__":
    main()
