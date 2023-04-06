#!/usr/bin/python3

"""
This script converts a Markdown file to HTML.

Usage: ./markdown2html.py <inputfile> <outputfile>

Arguments:
    inputfile: The name of the Markdown file to convert to HTML.
    outputfile: The name of the output HTML file.

If the input file does not exist, the script will print an error message to
stderr and exit with status code 1. If the conversion is successful, the output
HTML file will be created with the converted content and the script will exit
with status code 0.
"""

import sys
import os
import markdown

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <inputfile> <outputfile>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

with open(input_file, 'r') as f:
    text = f.read()

html = markdown.markdown(text)

with open(output_file, 'w') as f:
    f.write(html)

sys.exit(0)
