#!/usr/bin/env python3
from PIL import Image
import sys

if len(sys.argv) != 3:
    print("Usage: pngtojpg <input_png_path> <output_jpg_path>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

try:
    img = Image.open(input_path)
    img = img.convert("RGB")
    img.save(output_path, "JPEG")
    print(f"Conversion complete. Check the {output_path} file.")
except Exception as e:
    print(f"Error during conversion: {e}")
    sys.exit(1)
