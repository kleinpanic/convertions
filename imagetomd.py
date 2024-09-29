#!/usr/bin/env python3
from PIL import Image
import pytesseract
import sys
import os

def image_to_markdown(image_path, output_md_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        md_content = "# Image Content\n\n"
        md_content += text
        
        with open(output_md_path, 'w') as file:
            file.write(md_content)
        
        print(f"Markdown file created at {output_md_path}")
    except Exception as e:
        print(f"Error reading image content: {e}")
        sys.exit(1)

if len(sys.argv) != 3:
    print("Usage: imagetomd <input_image_path> <output_md_path>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

image_to_markdown(input_path, output_path)
