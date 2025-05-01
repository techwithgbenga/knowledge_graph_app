import faiss, numpy as np
import os, json
from openai import OpenAI
from database import SessionLocal
from models import Chunk

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
INDEX_PATH = "faiss.index"

def embed_text(text):
    resp = openai.embeddings.create(model="text-embedding-ada-002", input=text)
    return resp["data"][0]["embedding"]

def build_faiss():
    session = SessionLocal()
    embs = []
    ids  = []
    for chunk in session.query(Chunk).all():
        vec = np.array(json.loads(chunk.embedding), dtype='float32')
        embs.append(vec)
        ids.append(chunk.id)
    mat = np.stack(embs)
    index = faiss.IndexFlatL2(mat.shape[1])
    index.add(mat)
    faiss.write_index(index, INDEX_PATH)
    session.close()

def search(query, k=5):
    q_emb = np.array(embed_text(query), dtype='float32').reshape(1, -1)
    index = faiss.read_index(INDEX_PATH)
    D, I = index.search(q_emb, k)
    session = SessionLocal()
    results = []
    for idx in I[0]:
        chunk = session.query(Chunk).get(idx)
        results.append((chunk.text, json.loads(chunk.embedding)))
    session.close()
    return results
