#!/usr/bin/env python3
import sys
import subprocess
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: convertions <command> [args...]")
        print("Available commands:")
        print("  csvtoexcel <input_csv_path> <output_excel_path>")
        print("  csvtojson <input_csv_path> <output_json_path>")
        print("  excelto_csv <input_excel_path> <output_csv_path>")
        print("  htmltomd <input_html_path> <output_md_path>")
        print("  jsontocsv <input_json_path> <output_csv_path>")
        print("  mdtohtml <input_md_path> <output_html_path>")
        print("  yamltomd <input_yaml_path> <output_md_path>")
        print("  pngtojpg <input_png_path> <output_jpg_path>")
        print("  jpgtopng <input_jpg_path> <output_png_path>")
        print("  pdftojpg <input_pdf_path> <output_jpg_path>")
        print("  imagetomd <input_image_path> <output_md_path>")
        print("  jpgstopdf <output_pdf_path> <input_jpg_path1> <input_jpg_path2> ...")
        print("  pdftomd <input_pdf_path> <output_md_path>")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    script_map = {
        "csvtoexcel": "csvtoexcel.py",
        "csvtojson": "csvtojson.py",
        "excelto_csv": "excelto_csv.py",
        "htmltomd": "htmltomd.py",
        "jsontocsv": "jsontocsv.py",
        "mdtohtml": "mdtohtml.py",
        "yamltomd": "yamltomd.py",
        "pngtojpg": "pngtojpg.py",
        "jpgtopng": "jpgtopng.py",
        "pdftojpg": "pdftojpg.py",
        "imagetomd": "imagetomd.py",
        "jpgstopdf": "jpgstopdf.py",
        "pdftomd": "pdftomd.py",
    }

    if command not in script_map:
        print(f"Unknown command: {command}")
        sys.exit(1)

    script_path = os.path.join(os.path.dirname(__file__), script_map[command])

    # Path to the virtual environment's Python executable
    venv_python = os.path.join(os.path.dirname(__file__), 'convertions-env', 'bin', 'python')

    if not os.path.isfile(venv_python):
        print(f"Virtual environment not found at {venv_python}. Please set up the virtual environment.")
        sys.exit(1)

    # Run the script using the virtual environment's Python interpreter
    subprocess.run([venv_python, script_path] + args)

if __name__ == "__main__":
    main()
