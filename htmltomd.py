import html2text
import sys

if len(sys.argv) != 3:
    print("Usage: python html_to_md.py <input_html_path> <output_md_path>")
    sys.exit(1)

input_html_path = sys.argv[1]
output_md_path = sys.argv[2]

try:
    with open(input_html_path, 'r') as html_file:
        html_content = html_file.read()
except Exception as e:
    print(f"Error reading HTML file: {e}")
    sys.exit(1)

try:
    md_content = html2text.html2text(html_content)
    with open(output_md_path, 'w') as md_file:
        md_file.write(md_content)
    print(f"Conversion complete. Check the {output_md_path} file.")
except Exception as e:
    print(f"Error writing Markdown file: {e}")
    sys.exit(1)
