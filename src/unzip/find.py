from os import path
from glob import glob
from pathlib import Path

"""
Find zip files.
"""

# get root path
def root_dir() -> str:
    return Path(path.dirname(__file__)).parent.parent.absolute()


# find all zip files in _inout directory
def find() -> list[str]:
    zip_path = path.join(root_dir(), "_inout")
    return find_ext(zip_path, "zip")


def find_ext(dr, ext) -> list[str]:
    return glob(path.join(dr, "*.{}".format(ext)))
