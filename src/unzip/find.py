from os import path
from glob import glob  
from pathlib import Path

# find all zip files in _inout directory
def find() -> list[str]:
	zip_path = Path(path.dirname(__file__)).parent.parent.absolute()
	zip_path = path.join(zip_path, "_inout")
	return find_ext(zip_path, "zip")

def find_ext(dr, ext) -> list[str]:
	return glob(path.join(dr,"*.{}".format(ext)))
