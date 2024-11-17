#!/bin/bash

# Check if directory path is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <directory_path>"
  exit 1
fi

# Change to specified directory
cd "$1" || exit 1

# Check if jq is installed
if ! command -v jq &>/dev/null; then
  echo "Error: jq is not installed. Please install it first."
  exit 1
fi

# Output file name
output="merged_notebook.ipynb"

# Initialize the merged notebook with basic structure
echo '{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}' >"$output"

# Process each module directory in numerical order
for module_dir in $(find . -maxdepth 1 -type d -name "module-*" | sort -V); do
  echo "Processing directory: $module_dir"

  # Check if directory contains any .ipynb files
  if ! ls "$module_dir"/*.ipynb >/dev/null 2>&1; then
    echo "No .ipynb files found in $module_dir"
    continue
  fi

  # Process each notebook in the current module directory
  for notebook in "$module_dir"/*.ipynb; do
    echo "Processing $notebook..."

    # Check if file is valid JSON
    if ! jq empty "$notebook" 2>/dev/null; then
      echo "Error: $notebook is not valid JSON. Skipping..."
      continue
    fi

    # Extract cells array and merge
    jq -s '.[0].cells = ([.[].cells] | flatten) | .[0]' "$output" "$notebook" >temp.ipynb
    mv temp.ipynb "$output"
  done
done

# Verify the output has content
if [ "$(jq '.cells | length' "$output")" -eq 0 ]; then
  echo "Warning: No cells were merged. Output is empty."
else
  echo "Successfully merged notebooks into $output"
fi
