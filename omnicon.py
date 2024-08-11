import argparse
import docx2pdf
from pdf2docx import Converter
import md2pdf


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
    if args.newname:
        nn = path_nn(fn, args.newname, args.type)
    else:
        nn = fn.replace(fn.split(".")[-1], args.type)

    try:
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        match args.type:  # pdf to docx conversion
            case "pdf":
                if fn.endswith(".docx"):
                    docx2pdf.convert(fn, nn)
                elif fn.endswith(".md"):
                    md2pdf.convert_md_to_pdf(fn, nn, wkhtmltopdf_path)

            case "docx":
                if fn.endswith(".pdf"):
                    cv = Converter(fn)
                    cv.convert(nn, start=0, end=None)
                    cv.close()
                elif fn.endswith(".md"):
                   print("You can't directly convert md to docx file")


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
        
if __name__ == "__main__":
    main()
