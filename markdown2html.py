#!/usr/bin/python3
"""
Script that converts a markdown file to an HTML file.

Usage: ./markdown2html.py README.md README.html
"""

import sys
import os
import markdown


def main():
    # Check that the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Check if the input file exists
    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    # Read the markdown file
    with open(sys.argv[1], 'r') as md_file:
        md_text = md_file.read()

    # Convert the markdown to HTML
    html_text = markdown.markdown(md_text)

    # Write the HTML to the output file
    with open(sys.argv[2], 'w') as html_file:
        html_file.write(html_text)


if __name__ == "__main__":
    main()
