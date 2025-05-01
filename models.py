from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Document(Base):
    __tablename__ = "documents"
    id       = Column(Integer, primary_key=True)
    path     = Column(String, unique=True, nullable=False)
    title    = Column(String)
    chunks   = relationship("Chunk", back_populates="document")

class Chunk(Base):
    __tablename__ = "chunks"
    id         = Column(Integer, primary_key=True)
    document_id= Column(Integer, ForeignKey("documents.id"))
    text       = Column(Text, nullable=False)
    embedding  = Column(Text, nullable=False)  # JSON-serialized list
    document   = relationship("Document", back_populates="chunks")

class Entity(Base):
    __tablename__ = "entities"
    id    = Column(Integer, primary_key=True)
    name  = Column(String, index=True)
    type  = Column(String)
    
class Relation(Base):
    __tablename__ = "relations"
    id      = Column(Integer, primary_key=True)
    src_id  = Column(Integer, ForeignKey("entities.id"))
    dst_id  = Column(Integer, ForeignKey("entities.id"))
    label   = Column(String)
