import yaml
import sys
import os

def dict_to_markdown(data, indent=0):
    markdown = ""
    for key, value in data.items():
        if isinstance(value, dict):
            markdown += " " * indent + f"- **{key}**:\n"
            markdown += dict_to_markdown(value, indent + 2)
        else:
            markdown += " " * indent + f"- **{key}**: {value}\n"
    return markdown

if len(sys.argv) != 3:
    print("Usage: python convert_yaml_to_md.py <input_yaml_path> <output_md_path>")
    sys.exit(1)

input_yaml_path = sys.argv[1]
output_md_path = sys.argv[2]

if not os.path.isfile(input_yaml_path):
    print(f"Error: The file {input_yaml_path} does not exist.")
    sys.exit(1)

try:
    with open(input_yaml_path, 'r') as file:
        yaml_content = yaml.safe_load(file)
except Exception as e:
    print(f"Error reading YAML file: {e}")
    sys.exit(1)

markdown_content = dict_to_markdown(yaml_content)

try:
    with open(output_md_path, 'w') as file:
        file.write(markdown_content)
    print(f"Conversion complete. Check the {output_md_path} file.")
except Exception as e:
    print(f"Error writing Markdown file: {e}")
    sys.exit(1)
