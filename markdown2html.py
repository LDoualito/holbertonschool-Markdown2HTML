#!/usr/bin/python3
"""
Script that converts Markdown to HTML
"""
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]

    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    html_file = sys.argv[2]

    # Perform Markdown to HTML conversion here

    sys.exit(0)
