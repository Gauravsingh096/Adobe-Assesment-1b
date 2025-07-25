def rank_sections(sections, persona, job):
    # Simple keyword-based ranking: count job/persona keywords in section text
    keywords = set(re.findall(r'\w+', persona + ' ' + job))
    for section in sections:
        text = section.get("text", "").lower()
        score = sum(1 for k in keywords if k.lower() in text)
        section["importance_rank"] = score
    # Sort by score descending
    ranked = sorted(sections, key=lambda x: -x["importance_rank"])
    # Add rank index
    for idx, section in enumerate(ranked, 1):
        section["importance_rank"] = idx
    return ranked
# Relevance ranking model using MiniLM sentence transformer and caching
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# In-memory cache for embeddings
_embedding_cache = {}

def get_embedding(model, text):
    key = hash(text)
    if key in _embedding_cache:
        return _embedding_cache[key]
    emb = model.encode(text, convert_to_numpy=True, normalize_embeddings=True)
    _embedding_cache[key] = emb
    return emb

def rank_sections(sections, persona, job, top_k=10):
    # Use MiniLM for sentence embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query = persona + " " + job
    query_emb = get_embedding(model, query)
    filtered_sections = []
    for section in sections:
        text = section.get("text", "")
        # Filter out empty or very short sections
        if not text or len(text.strip()) < 30:
            continue
        section_emb = get_embedding(model, text)
        sim = cosine_similarity([section_emb], [query_emb])[0][0]
        section["similarity_score"] = float(sim)
        filtered_sections.append(section)
    # Sort by similarity descending
    ranked = sorted(filtered_sections, key=lambda x: -x["similarity_score"])
    # Only keep top_k
    ranked = ranked[:top_k]
    # Add rank index
    for idx, section in enumerate(ranked, 1):
        section["importance_rank"] = idx
    return ranked
