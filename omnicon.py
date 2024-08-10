import argparse
from pdf2docx import Converter
import docx2pdf
import sys
import os

def path_nn(fn, newname, typ):
    path_split = fn.split("\\")
    only_old = path_split[-1]
    nn = fn.replace(only_old, f"{newname}.{typ}")
    return nn

def main():
    parser = argparse.ArgumentParser(
        description='A utillity that converts every type of file, almost every type of file')
    parser.add_argument("file_name", type=str, help="The input file")
    parser.add_argument(
        "type",
        type=str,
        choices=["pdf", "docx", "ppt", "md"],
        help="The convertion to perform: Convertion to pdf, docx, ppt or md")
    parser.add_argument("-n", "--newname", type=str,
                        help="New name of the file sy: --newname [new_name]")
    args = parser.parse_args()

    fn = args.file_name
    try:
        match args.type:  # pdf to docx conversion
            case "pdf":
                if fn.endswith(".docx"):
                    if args.newname:
                        nn = path_nn(fn, args.newname, args.type)
                        docx2pdf.convert(fn, nn)
                    else:
                        docx2pdf.convert(fn, fn.replace("docx", "pdf"))
            case "docx":
                if fn.endswith(".pdf"):
                    if args.newname:
                        nn = path_nn(fn, args.newname, args.type)
                    else:
                        nn = fn.replace("pdf", "docx")
                    cv = Converter(fn)
                    cv.convert(nn, start=0, end=None)
                    cv.close()

    except NotADirectoryError:
        print("File not found error")
    except IsADirectoryError:
        print("File not found error")
    except FileNotFoundError:
        print("File not found, please check the file path and try again.")
    except PermissionError:
        print("Permission denied, please check the file path and try again.")
    except OSError:
        print("OS error, please check the file path and try again.")
    except KeyboardInterrupt:
        print("Keyboard Interrupt Error")
    except Exception as e:
        print(e)
        
    print(args.file_name)
    print(args.type)
    if args.newname:
        print(args.newname)
    else:
        print("No new name provided")

if __name__ == "__main__":
    main()
