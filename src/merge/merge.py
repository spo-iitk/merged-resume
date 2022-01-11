from glob import glob
from PyPDF2 import PdfFileMerger
from os import path
from merge.find import root_dir, find


def merge_pdf(dir_path, output_filename):
    merger = PdfFileMerger(strict=False)
    files = glob(path.join(dir_path, "*.{}".format("pdf")))
    for pdf_file in files:
        bookmark = path.basename(pdf_file[:-4])
        merger.append(pdf_file, bookmark)
    merger.write(output_filename)
    merger.close()


def merge():
    # get the path of the directory
    dir_path = path.join(root_dir(), "tmp")

    # get all directories in the directory
    directories = find()

    # get the output file name
    for dir in directories:
        output_filename = path.join(root_dir(), "_inout", "{}.pdf".format(dir))

        # get all pdf files in the directory
        pdf_files = path.join(dir_path, dir)

        # merge pdf files
        merge_pdf(pdf_files, output_filename)
