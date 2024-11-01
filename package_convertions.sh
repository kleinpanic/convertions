#!/bin/bash

# Activate virtual environment
if [ -d "venv" ]; then
  source venv/bin/activate
  echo "Virtual environment activated."
else
  echo "Error: Virtual environment not found. Please create one using 'python3 -m venv venv' and install the required packages."
  exit 1
fi

# Check if pyinstaller is installed
if ! command -v pyinstaller &> /dev/null; then
  echo "PyInstaller not found. Installing PyInstaller in the virtual environment..."
  pip install pyinstaller
fi

# Define the path for your convertions directory
CONVERTIONS_DIR="."

# Collect all .py files
PY_FILES=$(find $CONVERTIONS_DIR -name "*.py" -not -name "venv/*")

# Construct --add-data arguments for each .py file
ADD_DATA_ARGS=""
for file in $PY_FILES; do
  ADD_DATA_ARGS="$ADD_DATA_ARGS --add-data \"$file:./\""
done

# Run pyinstaller with --onefile and --add-data for all .py files
echo "Running PyInstaller to package convertions.py with dependencies..."

eval "pyinstaller --onefile $ADD_DATA_ARGS convertions.py"

# Deactivate virtual environment
deactivate

echo "Packaging complete. The binary can be found in the 'dist' directory."
