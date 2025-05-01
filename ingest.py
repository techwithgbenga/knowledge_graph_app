import os, json
from pdfminer.high_level import extract_text
from ingest import split_into_chunks
from database import SessionLocal
from models import Document, Chunk
from vector_store import embed_text

def ingest_file(path):
    session = SessionLocal()
    text = extract_text(path) if path.lower().endswith(".pdf") else open(path, "r").read()
    title = os.path.basename(path)
    doc = Document(path=path, title=title)
    session.add(doc); session.commit()
    
    chunks = split_into_chunks(text)
    for c in chunks:
        emb = embed_text(c)
        chunk = Chunk(document_id=doc.id, text=c, embedding=json.dumps(emb))
        session.add(chunk)
    session.commit()
    session.close()
