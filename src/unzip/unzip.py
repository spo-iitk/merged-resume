from os import path
from shutil import rmtree
import zipfile
from find import root_dir, find

"""
Unzip the zip file to tmp.
"""

# unzip the zip file
def unzip() -> list[str]:
    # get zip files
    zip_files = find()

    for zip_file in zip_files:
        # get tmp directory
        tmp_dir = path.join(root_dir(), "tmp")

        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(tmp_dir)

    return zip_files


def cleanup():
    tmp_dir = path.join(root_dir(), "tmp")
    rmtree(tmp_dir)
