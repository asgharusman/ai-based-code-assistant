import chromadb
from sentence_transformers import SentenceTransformer

# Step 1: Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 2: Create a ChromaDB client (this will save data to a local folder called "chroma_db")
client = chromadb.PersistentClient(path="chroma_db")

# Step 3: Create (or get) a collection — think of it like a table in a database
collection = client.get_or_create_collection(name="test_collection")

# Step 4: Our test chunks (pretend these came from loader.py)
chunks = [
    "print hello world",
    "print second file"
]

# Step 5: Convert each chunk to an embedding and store it
for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk).tolist()
    collection.add(
        ids=[str(i)],
        embeddings=[embedding],
        documents=[chunk]
    )

print("Stored", len(chunks), "chunks in ChromaDB")