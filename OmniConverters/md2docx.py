import subprocess

def md_to_docx(md_file, docx_file):
  try:
    subprocess.run(["pandoc", md_file, "-o", docx_file], check=True)
    print(f"Markdown file converted to Docx: {docx_file}")
  except subprocess.CalledProcessError as e:
    print(f"Error converting Markdown to Docx: {e}")

if __name__ == "__main__":
  md_file = input("md file here:")
  docx_file = "output.docx"
  md_to_docx(md_file, docx_file)
