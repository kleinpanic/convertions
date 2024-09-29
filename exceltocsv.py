import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Usage: python excel_to_csv.py <input_excel_path> <output_csv_path>")
    sys.exit(1)

input_excel_path = sys.argv[1]
output_csv_path = sys.argv[2]

try:
    df = pd.read_excel(input_excel_path)
    df.to_csv(output_csv_path, index=False)
    print(f"Conversion complete. Check the {output_csv_path} file.")
except Exception as e:
    print(f"Error during conversion: {e}")
    sys.exit(1)
