import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Usage: python csv_to_excel.py <input_csv_path> <output_excel_path>")
    sys.exit(1)

input_csv_path = sys.argv[1]
output_excel_path = sys.argv[2]

try:
    df = pd.read_csv(input_csv_path)
    df.to_excel(output_excel_path, index=False)
    print(f"Conversion complete. Check the {output_excel_path} file.")
except Exception as e:
    print(f"Error during conversion: {e}")
    sys.exit(1)
