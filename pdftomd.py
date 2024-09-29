#!/usr/bin/env python3
import fitz  # PyMuPDF
import sys
import os

def pdf_to_markdown(pdf_path, output_md_path):
    try:
        pdf_document = fitz.open(pdf_path)
        md_content = "# PDF Content\n\n"
        
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            md_content += f"## Page {page_num + 1}\n\n{text}\n\n"
        
        pdf_document.close()
        
        with open(output_md_path, 'w') as file:
            file.write(md_content)
        
        print(f"Markdown file created at {output_md_path}")
    except Exception as e:
        print(f"Error reading PDF content: {e}")
        sys.exit(1)

if len(sys.argv) != 3:
    print("Usage: pdftomd <input_pdf_path> <output_md_path>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

pdf_to_markdown(input_path, output_path)
