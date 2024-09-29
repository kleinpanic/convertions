import csv
import json
import sys

if len(sys.argv) != 3:
    print("Usage: python csv_to_json.py <input_csv_path> <output_json_path>")
    sys.exit(1)

input_csv_path = sys.argv[1]
output_json_path = sys.argv[2]

try:
    with open(input_csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
except Exception as e:
    print(f"Error reading CSV file: {e}")
    sys.exit(1)

try:
    with open(output_json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Conversion complete. Check the {output_json_path} file.")
except Exception as e:
    print(f"Error writing JSON file: {e}")
    sys.exit(1)
