import chromadb

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="test_collection")

data = collection.get(include=["documents", "metadatas"])

print("Total chunks:", len(data["ids"]))
for i in range(len(data["ids"])):
    print("---")
    print("ID:", data["ids"][i])
    print("Document:", data["documents"][i])
    print("Metadata:", data["metadatas"][i])