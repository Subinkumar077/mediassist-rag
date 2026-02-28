import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datasets import load_dataset
import chromadb
from pipeline.embedder import embed_batch
from pathlib import Path
from tqdm import tqdm
import yaml
import uuid

_PROJECT_ROOT = Path(__file__).parent.parent
_CONFIG_PATH  = _PROJECT_ROOT / "config.yaml"

with open(_CONFIG_PATH) as f:
    config = yaml.safe_load(f)

# Resolve chroma_path relative to the project root
_chroma_path = str(_PROJECT_ROOT / config['chroma_path'].lstrip("./"))

print("Loading PubMedQA dataset from HuggingFace...")
dataset = load_dataset("qiaojin/PubMedQA", "pqa_labeled", split="train")

client = chromadb.PersistentClient(path=_chroma_path)
collection = client.get_or_create_collection(config['collection_name'])

BATCH = 50
items = list(dataset)

print(f"Indexing {len(items)} documents into ChromaDB...")

for i in tqdm(range(0, len(items), BATCH)):
    batch = items[i:i+BATCH]
    texts = [
        item['question'] + " " + " ".join(item['context']['contexts'])
        for item in batch
    ]
    embeds = embed_batch(texts)
    ids = [str(uuid.uuid4()) for _ in batch]
    metas = [{'source': 'PubMedQA', 'pmid': str(item['pubid'])} for item in batch]
    collection.add(documents=texts, embeddings=embeds, ids=ids, metadatas=metas)

print(f"Done! {collection.count()} documents indexed.")
