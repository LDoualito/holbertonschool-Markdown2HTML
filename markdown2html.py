#!/usr/bin/python3
"""
markdown2html.py - Convert a markdown file to HTML.

Usage: ./markdown2html.py input_file output_file

Arguments:
    input_file:  The name of the Markdown file to be converted.
    output_file: The name of the output HTML file.

If the number of arguments is less than 2, the script will print the usage message and exit with status code 1.
If the Markdown file does not exist, the script will print an error message and exit with status code 1.
If the conversion is successful, the script will create the HTML file and exit with status code 0.
"""

import sys
import os
import markdown

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py input_file output_file", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    print("Missing file:", input_file, file=sys.stderr)
    sys.exit(1)

with open(input_file, "r") as f:
    html = markdown.markdown(f.read())

with open(output_file, "w") as f:
    f.write(html)

sys.exit(0)
