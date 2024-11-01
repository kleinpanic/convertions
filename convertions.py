#!/usr/bin/env python3
import sys
import subprocess
import os
import logging

# Set up logging to write to /tmp directory
log_path = '/tmp/convertions.log'
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def display_help():
    help_text = """
Usage: convertions <command> [args...]
Available commands:
  csvtoexcel <input_csv_path> <output_excel_path>
  csvtojson <input_csv_path> <output_json_path>
  exceltocsv <input_excel_path> <output_csv_path>  # corrected command
  htmltomd <input_html_path> <output_md_path>
  jsontocsv <input_json_path> <output_csv_path>
  mdtohtml <input_md_path> <output_html_path>
  yamltomd <input_yaml_path> <output_md_path>
  pngtojpg <input_png_path> <output_jpg_path>
  jpgtopng <input_jpg_path> <output_png_path>
  pdftojpg <input_pdf_path> <output_jpg_path>
  imagetomd <input_image_path> <output_md_path>
  jpgstopdf <output_pdf_path> <input_jpg_path1> <input_jpg_path2> ...
  pdftomd <input_pdf_path> <output_md_path>
  csvmerge <output_csv_path> <common_key> <input_csv1> <input_csv2> ...
  mdtabletocsv <input_md_path> <output_csv_path>
  yamlttojson <input_yaml_path> <output_json_path>
  jsontoyaml <input_json_path> <output_yaml_path>
  audiototext <input_audio_path> <output_text_path>
  texttospeech <input_text_path> <output_audio_path>
  videotoaudio <input_video_path> <output_audio_path>
  pdftoexcel <input_pdf_path> <output_excel_path>
  docxtomd <input_pdf_path> <output_excel_path>
  mergepdfs <output_pdf_path> <input_pdf1> <input_pdf2> ...
"""
    print(help_text)

def expand_path(path):
    """ Expand ~ to the user's home directory """
    return os.path.expanduser(path)

def validate_paths(command, args):
    if command in ["jpgstopdf", "csvmerge", "mergepdfs"]:
        output_path = expand_path(args[0])
        input_paths = [expand_path(path) for path in args[1:]]
        if len(input_paths) < 2:
            print(f"Error: Command '{command}' requires at least two input files.")
            sys.exit(1)
        if not all(os.path.isfile(path) for path in input_paths):
            print("Error: One or more input paths do not exist.")
            sys.exit(1)
    else:
        if len(args) < 2:
            print(f"Error: Command '{command}' requires an input and an output path.")
            sys.exit(1)
        input_path, output_path = expand_path(args[0]), expand_path(args[1])
        if not os.path.isfile(input_path):
            print(f"Error: Input file '{input_path}' does not exist.")
            sys.exit(1)
    return output_path


def main():
    if len(sys.argv) < 2:
        display_help()
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "help":
        display_help()
        sys.exit(0)

    script_map = {
        "csvtoexcel": "csvtoexcel.py",
        "csvtojson": "csvtojson.py",
        "docxtomd": "docxtomd.py",
        "exceltocsv": "exceltocsv.py",  # corrected from "excelto_csv"
        "htmltomd": "htmltomd.py",
        "jsontocsv": "jsontocsv.py",
        "mdtohtml": "mdtohtml.py",
        "mdtodocx": "mdtodocx.py",
        "yamltomd": "yamltomd.py",
        "pngtojpg": "pngtojpg.py",
        "jpgtopng": "jpgtopng.py",
        "pdftojpg": "pdftojpg.py",
        "imagetomd": "imagetomd.py",
        "jpgstopdf": "jpgstopdf.py",
        "pdftomd": "pdftomd.py",
        "csvmerge": "csvmerge.py",
        "mdtabletocsv": "mdtabletocsv.py",
        "yamlttojson": "yamlttojson.py",
        "jsontoyaml": "jsontoyaml.py",
        "audiototext": "audiototext.py",
        "texttospeech": "texttospeech.py",
        "videotoaudio": "videotoaudio.py",
        "pdftoexcel": "pdftoexcel.py",
        "mergepdfs": "mergepdfs.py" 
    }

    if command not in script_map:
        print(f"Unknown command: {command}")
        display_help()
        sys.exit(1)

    if len(args) < 2 and command not in ["jpgstopdf", "csvmerge"]:
        print(f"Error: Insufficient arguments for command '{command}'.")
        display_help()
        sys.exit(1)

    output_path = validate_paths(command, args)

    script_path = os.path.join(os.path.dirname(__file__), script_map[command])
    try:
        result = subprocess.run([sys.executable, script_path] + args, check=True)
        logging.info(f"Successfully executed {command} on {args}.")
        print(f"Conversion completed successfully. Output saved to '{output_path}'.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing {command} on {args}: {e}")
        print(f"Error: Conversion failed. Check the log file at /tmp/convertions.log for details.")

if __name__ == "__main__":
    main()

