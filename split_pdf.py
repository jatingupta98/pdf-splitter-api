from flask import Flask, request, send_file
from PyPDF2 import PdfReader, PdfWriter
import io

app = Flask(__name__)

@app.route('/split_pdf', methods=['POST'])
def split_pdf():
    pdf_file = request.files['file']
    pages = request.form['pages'].split(',')
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfWriter()

    for page in pages:
        pdf_writer.add_page(pdf_reader.pages[int(page) - 1])

    output_pdf = io.BytesIO()
    pdf_writer.write(output_pdf)
    output_pdf.seek(0)

    return send_file(output_pdf, as_attachment=True, download_name='split.pdf')

if __name__ == "__main__":
    app.run()
