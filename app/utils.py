"""
Utility helpers shared across the app layer.
"""

import re

# ─── Emoji Stripper ─────────────────────────────────────────────────────────
_EMOJI_RE = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001f926-\U0001f937"
    "\U00010000-\U0010ffff"
    "\u200d\u2640-\u2642\u2600-\u2B55\u23cf\u23e9-\u23f3\u23f8-\u23fa"
    "\u2934\u2935\u25aa-\u25fe\u2b05-\u2b07\u2b1b\u2b1c\u2b50\u3030\u303d\u3297\u3299"
    "]+",
    flags=re.UNICODE,
)


def strip_emojis(text: str) -> str:
    """Remove emoji characters from a string."""
    if not isinstance(text, str):
        return text
    return _EMOJI_RE.sub("", text).strip()


# ─── JSON Extraction ────────────────────────────────────────────────────────
_CODE_FENCE_RE = re.compile(
    r"```(?:json)?\s*\n?(.*?)\n?\s*```",
    flags=re.DOTALL,
)


def extract_json(text: str) -> str:
    """
    Extract clean JSON from an LLM response that may be wrapped in
    markdown code fences (```json ... ```) or contain leading/trailing
    whitespace and commentary.
    """
    # 1. Try to pull content out of code fences
    m = _CODE_FENCE_RE.search(text)
    if m:
        return m.group(1).strip()

    # 2. Fall back: grab the first { ... last }
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return text[start : end + 1]

    # 3. Nothing found — return as-is and let json.loads raise
    return text.strip()


def sanitize_result(result: dict) -> dict:
    """Strip emojis from every string value (including nested lists/dicts)."""
    for key in result:
        if isinstance(result[key], str):
            result[key] = strip_emojis(result[key])
        elif isinstance(result[key], list):
            result[key] = [
                (
                    {
                        k: strip_emojis(v) if isinstance(v, str) else v
                        for k, v in item.items()
                    }
                    if isinstance(item, dict)
                    else strip_emojis(item) if isinstance(item, str) else item
                )
                for item in result[key]
            ]
    return result


# ─── Retrieval Confidence Score ──────────────────────────────────────────────────────────

def compute_retrieval_score(chunks: list) -> float:
    """
    Aggregate similarity scores from retrieved chunks into a single
    retrieval confidence value (0-1 scale).

    Uses a weighted mean: the top-ranked chunk contributes more to
    the score than lower-ranked ones.  This reflects real-world
    retrieval behaviour where the top hit matters most.
    """
    if not chunks:
        return 0.0

    scores = [c.get("score", 0.0) for c in chunks]
    n = len(scores)

    # Linearly decreasing weights: [n, n-1, ..., 1]
    weights = list(range(n, 0, -1))
    weighted_sum = sum(s * w for s, w in zip(scores, weights))
    total_weight = sum(weights)

    return round(weighted_sum / total_weight, 3) if total_weight else 0.0
