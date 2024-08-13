import markdown
import pdfkit

def convert_md_to_pdf(md_file_path, pdf_file_path, wkhtmltopdf_path=None):
    try:
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

        html_content = markdown.markdown(md_content)

        custom_css = """
        <style>
            p {
                font-family: 'Arial', sans-serif;
                font-size: 14px;
                color: #333333;
            }
        </style>
        """
        html_content = custom_css + html_content

        config = None
        if wkhtmltopdf_path:
            config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

        pdfkit.from_string(html_content, pdf_file_path, configuration=config)

        print(f"Conversion successful! PDF saved to {pdf_file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__=='__main__':  
    md_file_path = input("Enter the md file name :")
    pdf_file_path = input("Enter the newname for file :")
    wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

    convert_md_to_pdf(md_file_path, pdf_file_path, wkhtmltopdf_path)
