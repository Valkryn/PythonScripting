import PyPDF2
import sys


def main():
    merger = PyPDF2.PdfFileMerger()
    for pdf in sys.argv[1:]:
        merger.append(pdf)
    merger.write("merged-pdf.pdf")
    merger.close()


if __name__ == '__main__':
    main()
