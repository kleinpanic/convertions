#!/usr/bin/env python3
from PIL import Image
import sys

if len(sys.argv) != 3:
    print("Usage: jpgtopng <input_jpg_path> <output_png_path>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

try:
    img = Image.open(input_path)
    img.save(output_path, "PNG")
    print(f"Conversion complete. Check the {output_path} file.")
except Exception as e:
    print(f"Error during conversion: {e}")
    sys.exit(1)
