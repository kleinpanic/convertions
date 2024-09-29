import json
import csv
import sys

if len(sys.argv) != 3:
    print("Usage: python json_to_csv.py <input_json_path> <output_csv_path>")
    sys.exit(1)

input_json_path = sys.argv[1]
output_csv_path = sys.argv[2]

try:
    with open(input_json_path, 'r') as json_file:
        data = json.load(json_file)
except Exception as e:
    print(f"Error reading JSON file: {e}")
    sys.exit(1)

try:
    with open(output_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write headers
        writer.writerow(data[0].keys())
        # Write data rows
        for row in data:
            writer.writerow(row.values())
    print(f"Conversion complete. Check the {output_csv_path} file.")
except Exception as e:
    print(f"Error writing CSV file: {e}")
    sys.exit(1)
