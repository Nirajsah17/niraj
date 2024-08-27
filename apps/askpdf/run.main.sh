#!/bin/bash

PATH=$1
QUERY=$2

# Check if both arguments are provided
if [ -z "$PATH" ] || [ -z "$QUERY" ]; then
  echo "Usage: $0 <path_to_file> <query>"
  exit 1
fi

echo "Path of the file: $PATH"
echo "Query for the file: $QUERY"

# Run the Python script with the provided arguments
python main.py --input_pdf "$PATH" --query "$QUERY"
