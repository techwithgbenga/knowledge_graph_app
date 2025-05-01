import streamlit as st
from ingest import ingest_file
from graph_builder import build_graph
from vector_store import build_faiss, search
import networkx as nx
from pyvis.network import Network

st.title("📚 Personal Knowledge Graph & Semantic Search")

# Sidebar: ingest
uploaded = st.sidebar.file_uploader("Upload Document", type=["pdf","md","txt"])
if uploaded:
    with open(uploaded.name, "wb") as f: f.write(uploaded.getbuffer())
    ingest_file(uploaded.name)
    st.sidebar.success("Ingested!")

if st.sidebar.button("Build Graph & Index"):
    G = build_graph()
    build_faiss()
    st.sidebar.success("Graph & Index built!")

query = st.text_input("Search the knowledge base")
if st.button("🔍 Search"):
    results = search(query)
    for txt, _ in results:
        st.write("—", txt)

# Visualize graph
if st.button("Show Graph"):
    G = build_graph()
    net = Network(height="600px", width="100%")
    net.from_nx(G)
    net.show("graph.html")
    st.components.v1.html(open("graph.html", "r").read(), height=600)
