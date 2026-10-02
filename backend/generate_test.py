import chromadb
from sentence_transformers import SentenceTransformer
import ollama

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="test_collection")

def retrieve(query, n_results=1):
    query_embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results["documents"][0]  # list of matching chunk texts

def build_prompt(query, context_chunks):
    context = "\n".join(context_chunks)
    return f"""Context:
{context}

Question: {query}
Answer:"""

def ask(query):
    chunks = retrieve(query)
    prompt = build_prompt(query, chunks)
    print("----- PROMPT SENT TO MODEL -----")
    print(prompt)
    print("---------------------------------")

    response = ollama.chat(
        model="gemma4:e2b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

if __name__ == "__main__":
    query = "what does sample2.py do?"
    answer = ask(query)
    print("----- MODEL ANSWER -----")
    print(answer)