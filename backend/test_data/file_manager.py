import os


def list_python_files(folder_path):
    """Return a list of all .py files in the given folder."""
    return [f for f in os.listdir(folder_path) if f.endswith(".py")]


def read_file_contents(file_path):
    """Read and return the full contents of a file as a string."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def count_lines(file_path):
    """Count the number of lines in a given file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return len(f.readlines())