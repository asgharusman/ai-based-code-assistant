from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "print hello world"
embedding = model.encode(text)

print(embedding)
print("Length:", len(embedding))