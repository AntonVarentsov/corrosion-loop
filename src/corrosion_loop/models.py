"""SQLAlchemy models for the corrosion loop project."""

from __future__ import annotations

from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Document(Base):
    __tablename__ = "documents"

    document_id = Column(Integer, primary_key=True)
    doc_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())


class Equipment(Base):
    __tablename__ = "equipment"

    equip_id = Column(Integer, primary_key=True)
    equip_tag = Column(String, nullable=False)
    equip_type = Column(String)
    document_id = Column(Integer, ForeignKey("documents.document_id"))
    page_number = Column(Integer)
    x0 = Column(Float)
    y0 = Column(Float)
    x1 = Column(Float)
    y1 = Column(Float)
    description = Column(Text)


class LineNumber(Base):
    __tablename__ = "line_numbers"

    line_id = Column(Integer, primary_key=True)
    line_number = Column(String, nullable=False)
    document_id = Column(Integer, ForeignKey("documents.document_id"))
    page_number = Column(Integer)
    x0 = Column(Float)
    y0 = Column(Float)
    x1 = Column(Float)
    y1 = Column(Float)
