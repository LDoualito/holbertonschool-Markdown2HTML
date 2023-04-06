#!/usr/bin/python3
"""
markdown2html.py - Convert a markdown file to HTML format

Usage: ./markdown2html.py [MARKDOWN_FILE] [HTML_FILE]
"""

import sys
import os.path
import markdown


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py [MARKDOWN_FILE] [HTML_FILE]\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    with open(markdown_file, "r") as f:
        markdown_text = f.read()

    html_text = markdown.markdown(markdown_text)

    with open(html_file, "w") as f:
        f.write(html_text)

    sys.exit(0)


if __name__ == "__main__":
    main()
