import docx2txt

def docx_to_md(docx_path, md_path):
  text = docx2txt.process(docx_path)
  with open(md_path, "w") as f:
    f.write(text)

if __name__ == '__main__':
    input_md_file = input("Enter md file name : ")
    output_docx_file = input("Enter docx file name : ")

    docx_to_md(input_md_file, output_docx_file)
