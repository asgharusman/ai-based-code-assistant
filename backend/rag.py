import chromadb
from sentence_transformers import SentenceTransformer
import ollama

_model = None
_collection = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def get_collection():
    global _collection
    if _collection is None:
        client = chromadb.PersistentClient(path="chroma_db")
        _collection = client.get_or_create_collection(name="test_collection")
    return _collection

def retrieve(query, n_results=1):
    model = get_model()
    collection = get_collection()
    query_embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results["documents"][0]

def build_prompt(query, context_chunks):
    context = "\n".join(context_chunks)
    return f"""Context:
{context}

Question: {query}
Answer:"""

def ask(query, n_results=1):
    chunks = retrieve(query, n_results=n_results)
    prompt = build_prompt(query, chunks)
    response = ollama.chat(
        model="qwen2.5:0.5b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]