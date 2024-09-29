
# Convertions

The `convertions` project is a collection of Python scripts designed to convert between various file formats and extract content from different types of files. This toolset includes scripts for converting CSV, JSON, Excel, HTML, Markdown, YAML, PNG, JPG, PDF files, and more. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [CSV to Excel](#csv-to-excel)
  - [CSV to JSON](#csv-to-json)
  - [Excel to CSV](#excel-to-csv)
  - [HTML to Markdown](#html-to-markdown)
  - [JSON to CSV](#json-to-csv)
  - [Markdown to HTML](#markdown-to-html)
  - [YAML to Markdown](#yaml-to-markdown)
  - [PNG to JPG](#png-to-jpg)
  - [JPG to PNG](#jpg-to-png)
  - [PDF to JPG](#pdf-to-jpg)
  - [JPGs to PDF](#jpgs-to-pdf)
  - [Image to Markdown](#image-to-markdown)
  - [PDF to Markdown](#pdf-to-markdown)
- [Adding New Scripts](#adding-new-scripts)
- [Virtual Environment](#virtual-environment)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/convertions.git
   cd convertions
   ```

2. **Set Up the Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add the Convertions Directory to PATH**:
   - For Bash:
     ```bash
     echo 'export PATH="$HOME/codeWS/Python3/convertions:$PATH"' >> ~/.bashrc
     source ~/.bashrc
     ```
   - For Zsh:
     ```bash
     echo 'export PATH="$HOME/codeWS/Python3/convertions:$PATH"' >> ~/.zshrc
     source ~/.zshrc
     ```

## Usage

### CSV to Excel
Convert a CSV file to an Excel file.
```bash
convertions csvtoexcel <input_csv_path> <output_excel_path>
```

### CSV to JSON
Convert a CSV file to a JSON file.
```bash
convertions csvtojson <input_csv_path> <output_json_path>
```

### Excel to CSV
Convert an Excel file to a CSV file.
```bash
convertions excelto_csv <input_excel_path> <output_csv_path>
```

### HTML to Markdown
Convert an HTML file to a Markdown file.
```bash
convertions htmltomd <input_html_path> <output_md_path>
```

### JSON to CSV
Convert a JSON file to a CSV file.
```bash
convertions jsontocsv <input_json_path> <output_csv_path>
```

### Markdown to HTML
Convert a Markdown file to an HTML file.
```bash
convertions mdtohtml <input_md_path> <output_html_path>
```

### YAML to Markdown
Convert a YAML file to a Markdown file.
```bash
convertions yamltomd <input_yaml_path> <output_md_path>
```

### PNG to JPG
Convert a PNG image to a JPG image.
```bash
convertions pngtojpg <input_png_path> <output_jpg_path>
```

### JPG to PNG
Convert a JPG image to a PNG image.
```bash
convertions jpgtopng <input_jpg_path> <output_png_path>
```

### PDF to JPG
Convert a PDF file to JPG images (one per page).
```bash
convertions pdftojpg <input_pdf_path> <output_jpg_path>
```

### JPGs to PDF
Combine multiple JPG images into a single PDF file.
```bash
convertions jpgstopdf <output_pdf_path> <input_jpg_path1> <input_jpg_path2> ...
```

### Image to Markdown
Extract text content from an image (JPG/PNG) using OCR and convert it to a Markdown file.
```bash
convertions imagetomd <input_image_path> <output_md_path>
```

### PDF to Markdown
Extract text content from a PDF file and convert it to a Markdown file.
```bash
convertions pdftomd <input_pdf_path> <output_md_path>
```

## Adding New Scripts

To add a new script to the convertions toolset:

1. Place the new script in the \`~/codeWS/Python3/convertions\` directory.
2. Ensure the script is executable:
   ```bash
   chmod +x ~/codeWS/Python3/convertions/new_script.py
   ```
3. Update \`convertions.py\` to include the new command and map it to the script.

## Virtual Environment

The convertions toolset uses a virtual environment to manage dependencies. Ensure the virtual environment is activated before running any scripts:
```bash
source venv/bin/activate
```

To deactivate the virtual environment, use:
```bash
deactivate
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Pillow](https://python-pillow.org/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [pytesseract](https://pypi.org/project/pytesseract/)
