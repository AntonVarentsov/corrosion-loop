# Corrosion Loop MVP

This project parses P&ID diagrams in PDF format and stores line numbers and equipment
tags in a PostgreSQL database. The extracted data can be exported to Excel for further
analysis.

## Architecture Overview

- **pdfplumber** extracts text objects and their coordinates from PDF files.
- **SQLAlchemy** manages PostgreSQL tables defined in `src/corrosion_loop/models.py`.
- **Parser** (`src/corrosion_loop/parser.py`) identifies line numbers and equipment
  tags using regular expressions.
- **Exporter** (`src/corrosion_loop/exporter.py`) writes selected records to Excel.
- **CLI** (`src/corrosion_loop/cli.py`) provides a command-line interface for running
  the entire pipeline.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set the `DATABASE_URL` environment variable pointing to your PostgreSQL instance.
3. Run the pipeline for a directory of PDFs:
   ```bash
   python -m corrosion_loop.cli /path/to/pdfs output.xlsx
   ```

Refer to `AGENTS.md` for repository guidelines.
