import chromadb
from pipeline.embedder import embed_text
from pathlib import Path
import yaml

_CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"
with open(_CONFIG_PATH) as f:
    config = yaml.safe_load(f)

# Resolve chroma_path relative to the project root (not CWD)
_PROJECT_ROOT = Path(__file__).parent.parent
_chroma_path = str(_PROJECT_ROOT / config['chroma_path'].lstrip("./"))

client = chromadb.PersistentClient(path=_chroma_path)
collection = client.get_or_create_collection(config['collection_name'])

def retrieve(query: str, k: int = None) -> list:
    """Retrieve top-k chunks from ChromaDB, then re-rank to rerank_top_k."""
    vector_k   = k or config['vector_top_k']
    rerank_k   = config.get('rerank_top_k', vector_k)
    query_vec  = embed_text(query)

    results = collection.query(
        query_embeddings=[query_vec],
        n_results=vector_k,
        include=['documents', 'metadatas', 'distances']
    )

    chunks = []
    for doc, meta, dist in zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0]
    ):
        chunks.append({
            'text':   doc,
            'source': meta.get('source', 'Unknown'),
            'score':  round(1 - dist, 3)
        })

    # Re-rank: sort by cosine similarity score (descending), keep top rerank_k
    chunks.sort(key=lambda c: c['score'], reverse=True)
    return chunks[:rerank_k]