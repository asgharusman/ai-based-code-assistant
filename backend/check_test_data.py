import os

print("Running from:", os.getcwd())
for f in os.listdir("test_data"):
    path = os.path.join("test_data", f)
    print(f, "-> is file:", os.path.isfile(path), "size:", os.path.getsize(path) if os.path.isfile(path) else "-")