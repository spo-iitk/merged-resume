from os import path, listdir
from pathlib import Path

"""
Find pdf directories.
"""

# get root path
def root_dir() -> str:
    return Path(path.dirname(__file__)).parent.parent.absolute()


# find all folders having pdf files in tmp directory
def find() -> list[str]:
    pdf_path = path.join(root_dir(), "tmp")
    try:
        return listdir(pdf_path)
    except:
        print("No pdf files found in tmp directory.")
        return []
