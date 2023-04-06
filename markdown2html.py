#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
"""
import sys
import os
import markdown


def main():
    # Check that 2 arguments were provided
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)

    # Check that the input file exists
    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Read the input file and convert markdown to html
    with open(input_file, "r") as f:
        md = f.read()
        html = markdown.markdown(md)

    # Write the html output to the specified output file
    output_file = sys.argv[2]
    with open(output_file, "w") as f:
        f.write(html)

    # Exit with a status of 0 to indicate success
    sys.exit(0)


if __name__ == "__main__":
    main()