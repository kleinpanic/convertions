#!/usr/bin/env python3
from PIL import Image
import sys

def convert_images_to_pdf(image_paths, output_pdf_path):
    images = []
    for image_path in image_paths:
        img = Image.open(image_path)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        images.append(img)
    
    if images:
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
        print(f"PDF created at {output_pdf_path}")
    else:
        print("No images to convert.")

if len(sys.argv) < 3:
    print("Usage: jpgstopdf <output_pdf_path> <input_jpg_path1> <input_jpg_path2> ...")
    sys.exit(1)

output_pdf_path = sys.argv[1]
image_paths = sys.argv[2:]

convert_images_to_pdf(image_paths, output_pdf_path)
