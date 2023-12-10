#!/usr/bin/env python3
import sys

def convert_markdown_to_html(markdown_file, output_file):
    # Your markdown to HTML conversion logic here
    pass

if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the Markdown file exists
try:
    with open(markdown_file, 'r'):
        pass
except FileNotFoundError:
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# Perform the conversion
convert_markdown_to_html(markdown_file, output_file)
