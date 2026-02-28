from sentence_transformers import SentenceTransformer
from pathlib import Path
import yaml

_CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"
with open(_CONFIG_PATH) as f:
    config = yaml.safe_load(f)

_model = None

def get_model():
    global _model
    if _model is None:
        print("Loading medical embedding model...")
        _model = SentenceTransformer(config['embedding_model'])
    return _model

def embed_text(text: str) -> list:
    model = get_model()
    return model.encode(text).tolist()

def embed_batch(texts: list) -> list:
    model = get_model()
    return model.encode(texts, batch_size=32, show_progress_bar=True).tolist()