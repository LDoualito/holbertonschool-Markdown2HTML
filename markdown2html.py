#!/usr/bin/python3

"""
Converts Markdown to HTML.

Usage: ./markdown2html.py README.md README.html
"""

import sys
import os

def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts Markdown to HTML.

    Args:
        markdown_file (str): Name of the Markdown file.
        output_file (str): Name of the output HTML file.
    """
    # Check the number of arguments
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and process headings
    with open(markdown_file, 'r') as f:
        lines = f.readlines()

    # Process each line
    output_lines = []
    for line in lines:
        line = line.rstrip('\n')

        # Check for heading syntax and convert to HTML
        if line.startswith('# '):
            output_lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith('## '):
            output_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith('### '):
            output_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith('#### '):
            output_lines.append(f"<h4>{line[5:]}</h4>")
        elif line.startswith('##### '):
            output_lines.append(f"<h5>{line[6:]}</h5>")
        elif line.startswith('###### '):
            output_lines.append(f"<h6>{line[7:]}</h6>")
        else:
            output_lines.append(line)

    # Write the HTML output
    with open(output_file, 'w') as output:
        output.write('\n'.join(output_lines))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    convert_markdown_to_html(sys.argv[1], sys.argv[2])
