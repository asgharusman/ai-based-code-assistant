import os


def chunk_text(text, chunk_size=300):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end
    return chunks


def load_chunks(folder_path="test_data"):
    """Returns a list of (file_name, chunk_text) pairs."""
    results = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(file_path):
            continue
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        for chunk in chunk_text(content):
            results.append((file_name, chunk))
    return results


if __name__ == "__main__":
    for file_name, chunk in load_chunks():
        print(file_name, "->", chunk[:50].replace("\n", " "))