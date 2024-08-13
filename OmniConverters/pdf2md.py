import pdfplumber

def convert_pdf_to_md(input_pdf, output_md):
    try:
        with pdfplumber.open(input_pdf) as pdf:
            with open(output_md, 'w') as md_file:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        md_file.write(text)
                        md_file.write("\n\n")  # Adding spacing between pages
        print(f"File converted successfully and saved as {output_md}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__=='__main__':
    input_pdf_file = input("Enter pdf file name : ")
    output_md_file = input("Enter md file name : ")

    convert_pdf_to_md(input_pdf_file, output_md_file)
