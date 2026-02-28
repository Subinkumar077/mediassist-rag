from sentence_transformers import SentenceTransformer
from pathlib import Path
import yaml

try:
    from streamlit import cache_resource as _cache_resource
except ImportError:          # Not running inside Streamlit (e.g. scripts/)
    def _cache_resource(fn):  # noqa: D401 – simple passthrough
        return fn

_CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"
with open(_CONFIG_PATH) as f:
    config = yaml.safe_load(f)


@_cache_resource(show_spinner="Loading medical embedding model...")
def get_model() -> SentenceTransformer:
    """Load (and cache across Streamlit reruns) the BioBERT embedding model."""
    return SentenceTransformer(config["embedding_model"])


def embed_text(text: str) -> list:
    model = get_model()
    return model.encode(text).tolist()


def embed_batch(texts: list) -> list:
    model = get_model()
    return model.encode(texts, batch_size=32, show_progress_bar=True).tolist()