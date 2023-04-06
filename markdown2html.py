#!/usr/bin/python3
"""
Converts markdown to html.
Usage: ./markdown2html.py README.md README.html
"""

import sys
import os


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    # TODO: Convert markdown to HTML and write to file

    sys.exit(0)
