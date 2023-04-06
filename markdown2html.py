#!/usr/bin/python3
"""
Script that converts Markdown to HTML
Usage: ./markdown2html.py README.md README.html
"""
import sys
import os.path
import markdown


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Get the input and output file names
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Convert the Markdown file to HTML and write it to the output file
    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        html = markdown.markdown(f_in.read())
        f_out.write(html)
    
    sys.exit(0)
