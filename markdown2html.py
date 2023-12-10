#!/usr/bin/env python3
import sys
import os

def convert_markdown_to_html(markdown_file, output_file):
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Extract arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Implement the Markdown to HTML conversion logic here
    # For simplicity, let's just print a success message
    print(f"Converting {markdown_file} to {output_file}")

if __name__ == "__main__":
    convert_markdown_to_html(sys.argv[1], sys.argv[2])
    sys.exit(0)
