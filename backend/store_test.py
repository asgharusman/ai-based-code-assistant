import chromadb
from sentence_transformers import SentenceTransformer
from loader import load_chunks

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")

# wipe the old collection so the 2 hand-typed chunks (ids "0", "1") are removed
try:
    client.delete_collection("test_collection")
except Exception:
    pass
collection = client.create_collection(name="test_collection")

chunks = load_chunks("test_data")
texts = [text for _, text in chunks]

collection.add(
    ids=[f"{name}::{i}" for i, (name, _) in enumerate(chunks)],
    embeddings=model.encode(texts).tolist(),
    documents=texts,
    metadatas=[{"file": name} for name, _ in chunks],
)

print("Stored", len(chunks), "chunks in ChromaDB")