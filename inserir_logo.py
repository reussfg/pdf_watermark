from pdfrw import PdfReader, PdfWriter, PageMerge
from pathlib import Path
import os

# Find all PDF files and convert to PDF object
pdf_files = Path(r"/Users/gabrielreus/Desktop/Python/PDF/old/").glob("*.pdf")

# Iterate over all pdf files and retrieve name
pdf_names = []
path = r"/Users/gabrielreus/Desktop/Python/PDF/old"
for file in os.listdir(path):
    if file.endswith('.pdf') or file.endswith('.PDF'):
        pdf_names.append(file)

print(pdf_names)
for x in range(len(pdf_names)):
    name = pdf_names[x]
    input_file = f"/Users/gabrielreus/Desktop/Python/PDF/old/{pdf_names[x]}"
    output_file = f"/Users/gabrielreus/Desktop/Python/PDF/new/{pdf_names[x]}"
    watermark_file = "/Users/gabrielreus/Desktop/Python/PDF/logo/logo.pdf"

    # define the reader and writer objects
    reader_input = PdfReader(input_file)
    writer_output = PdfWriter()
    watermark_input = PdfReader(watermark_file)
    watermark = watermark_input.pages[0]

    # go through the pages one after the next
    for current_page in range(len(reader_input.pages)):
        merger = PageMerge(reader_input.pages[current_page])
        merger.add(watermark).render()

    # write the modified content to disk
    writer_output.write(output_file, reader_input)
