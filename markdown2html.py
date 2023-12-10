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
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # The actual conversion code goes here

if __name__ == "__main__":
    convert_markdown_to_html(sys.argv[1], sys.argv[2])
