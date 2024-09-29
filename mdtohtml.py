import markdown
import sys

if len(sys.argv) != 3:
    print("Usage: python md_to_html.py <input_md_path> <output_html_path>")
    sys.exit(1)

input_md_path = sys.argv[1]
output_html_path = sys.argv[2]

try:
    with open(input_md_path, 'r') as md_file:
        md_content = md_file.read()
except Exception as e:
    print(f"Error reading Markdown file: {e}")
    sys.exit(1)

try:
    html_content = markdown.markdown(md_content)
    with open(output_html_path, 'w') as html_file:
        html_file.write(html_content)
    print(f"Conversion complete. Check the {output_html_path} file.")
except Exception as e:
    print(f"Error writing HTML file: {e}")
    sys.exit(1)
