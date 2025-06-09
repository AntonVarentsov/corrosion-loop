"""Excel export utilities."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .database import get_session
from .models import Document, Equipment, LineNumber


def export_to_excel(output: Path) -> None:
    """Export parsed records to an Excel file."""

    with get_session() as session:
        docs = session.query(Document).all()
        lines = session.query(LineNumber).all()
        equip = session.query(Equipment).all()

        df_docs = pd.DataFrame([d.__dict__ for d in docs])
        df_lines = pd.DataFrame([l.__dict__ for l in lines])
        df_equip = pd.DataFrame([e.__dict__ for e in equip])

        with pd.ExcelWriter(output) as writer:
            df_docs.to_excel(writer, sheet_name="documents", index=False)
            df_lines.to_excel(writer, sheet_name="line_numbers", index=False)
            df_equip.to_excel(writer, sheet_name="equipment", index=False)
