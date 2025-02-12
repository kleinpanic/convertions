import yaml
import json
import sys
import os

def convert_yaml_to_json(input_yaml_path, output_json_path):
    # Check if the input YAML file exists
    if not os.path.isfile(input_yaml_path):
        print(f"Error: The file '{input_yaml_path}' does not exist.")
        sys.exit(1)

    # Check if the output directory is writable
    output_dir = os.path.dirname(output_json_path)
    if output_dir and not os.access(output_dir, os.W_OK):
        print(f"Error: The output directory '{output_dir}' is not writable.")
        sys.exit(1)

    try:
        # Load the YAML content
        with open(input_yaml_path, 'r', encoding='utf-8') as yaml_file:
            yaml_content = yaml.safe_load(yaml_file)

        # Write the JSON content
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(yaml_content, json_file, indent=4)
        
        print(f"Conversion complete. Check the '{output_json_path}' file.")
    except Exception as e:
        print(f"Error during YAML to JSON conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python yamlttojson.py <input_yaml_path> <output_json_path>")
        sys.exit(1)

    input_yaml_path = sys.argv[1]
    output_json_path = sys.argv[2]

    convert_yaml_to_json(input_yaml_path, output_json_path)

