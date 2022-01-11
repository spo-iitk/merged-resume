from unzip import unzip, cleanup
from merge import merge


def main():
    files = unzip()
    for file in files:
        print("Unzipping file ", file, "...")
    if len(files) == 0:
        print("No zip files in _inout directory. Exiting program.")
        return

    print("Merging unzipped PDF...")
    merge()

    print("Cleaning up unzipped files...")
    cleanup()

    print("Done! Find merged files in _inout directory.")


if __name__ == "__main__":
    main()
