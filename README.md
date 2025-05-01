# Personal Knowledge Graph & Semantic Search Engine
An application that lets you ingest documents (PDFs, Markdown, text), build a semantic knowledge graph (entities + relations), and expose a Streamlit-based semantic search UI backed by a vector store (FAISS) and OpenAI embeddings. Perfect for researchers, students, or teams to organize and query their private knowledge.

## Key Features
- Document Ingestion
-- Support for PDF, Markdown, and plain-text files
-- Chunking & metadata extraction (author, date, headings)

- Knowledge Graph Construction
-- Entity & relation extraction with spaCy or OpenAI’s NER
-- Store as a NetworkX graph (nodes = entities, edges = relations)

- Vector Store & Semantic Search
-- Generate embeddings for each text chunk with OpenAI or Hugging Face
-- Index embeddings in FAISS for fast similarity search
-- Query interface returns top-k relevant chunks

- Streamlit UI
-- Upload new documents
-- Browse extracted graph (interactive network visualization)
-- Search bar with autocomplete and “Did you mean?” suggestions
-- Display retrieved context + graph highlights

- Persistence
-- SQLite (via SQLAlchemy) to store metadata, embeddings, and graph nodes/edges
-- Optionally export/import graph in GraphML

## Getting Started
- Clone & Install
```bash
git clone https://github.com/yourusername/knowledge_graph_app.git
cd knowledge_graph_app
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
- Run
```bash
streamlit run app.py
```
- Use
-- Upload docs in the sidebar
-- Build graph & index
-- Search semantically
-- Visualize your personal knowledge graph

This Personal Knowledge Graph & Semantic Search Engine is a “powerful” project combining NLP, graph theory, embeddings, and an interactive UI—ideal for publishing on GitHub as a flagship open-source tool.





