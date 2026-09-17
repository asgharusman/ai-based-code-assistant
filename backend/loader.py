import os

folder_path = "test_data"


def chunk_text(text, chunk_size=300):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end
    return chunks


for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "r") as f:
        content = f.read()

    chunks = chunk_text(content)
    print(file_name, "->", len(chunks), "chunk(s)")
    for chunk in chunks:
        print(chunk)