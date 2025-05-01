import spacy
import networkx as nx
from database import SessionLocal
from models import Entity, Relation

nlp = spacy.load("en_core_web_sm")

def build_graph():
    session = SessionLocal()
    G = nx.DiGraph()
    for chunk in session.query(Chunk).all():
        doc = nlp(chunk.text)
        ents = {ent.text: ent.label_ for ent in doc.ents}
        for name, label in ents.items():
            entity = session.query(Entity).filter_by(name=name).first()
            if not entity:
                entity = Entity(name=name, type=label)
                session.add(entity); session.commit()
            G.add_node(entity.id, name=name, label=label)
        # simple relation: consecutive entities in text
        names = list(ents.keys())
        for i in range(len(names)-1):
            src = session.query(Entity).filter_by(name=names[i]).one()
            dst = session.query(Entity).filter_by(name=names[i+1]).one()
            rel = Relation(src_id=src.id, dst_id=dst.id, label="co_occurrence")
            session.add(rel)
            G.add_edge(src.id, dst.id, label="co_occurrence")
    session.commit()
    session.close()
    return G
