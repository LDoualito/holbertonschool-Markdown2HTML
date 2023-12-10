#!/usr/bin/python3
"""
Parse a Markdown file and convert it to HTML
"""
import re
import hashlib
import sys
import os

def convert_markdown_to_html(markdown_file, output_file):
    """
    Convert Markdown to HTML and save it in the output file.

    Args:
        markdown_file (str): The name of the Markdown file.
        output_file (str): The name of the output HTML file.
    """
    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    with open(markdown_file, 'r') as markdown_file:
        with open(output_file, 'w') as html_file:
            change_status = False
            unordered_status = False
            ordered_status = False
            paragraph = False

            for line in markdown_file:
                # Parse bold syntax
                line = line.replace('**', '<b>', 1).replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1).replace('__', '</em>', 1)

                # Replace [[...]] with MD5 hash
                md5_matches = re.findall(r'\[\[(.+?)\]\]', line)
                if md5_matches:
                    line = line.replace(md5_matches[0], hashlib.md5(md5_matches[0].encode()).hexdigest())

                # Replace ((...)) with deletion of 'C' or 'c'
                delete_c_matches = re.findall(r'\(\((.+?)\)\)', line)
                if delete_c_matches:
                    remove_c_inside = ''.join(c for c in delete_c_matches[0] if c.lower() != 'c')
                    line = line.replace(delete_c_matches[0], remove_c_inside)

                length = len(line)
                headings = line.lstrip('#')
                heading_count = length - len(headings)
                unordered = line.lstrip('-')
                unordered_count = length - len(unordered)
                ordered = line.lstrip('*')
                ordered_count = length - len(ordered)

                # Convert headings to HTML
                if 1 <= heading_count <= 6:
                    line = f'<h{heading_count}>{headings.strip()}</h{heading_count}>\n'

                # Handle unordered lists
                if unordered_count:
                    if not change_status:
                        html_file.write('<ul>\n')
                        change_status = True
                    line = f'<li>{unordered.strip()}</li>\n'
                if change_status and not unordered_count:
                    html_file.write('</ul>\n')
                    change_status = False

                # Handle ordered lists
                if ordered_count:
                    if not ordered_status:
                        html_file.write('<ol>\n')
                        ordered_status = True
                    line = f'<li>{ordered.strip()}</li>\n'
                if ordered_status and not ordered_count:
                    html_file.write('</ol>\n')
                    ordered_status = False

                # Handle paragraphs
                if not (heading_count or change_status or ordered_status):
                    if not paragraph and length > 1:
                        html_file.write('<p>\n')
                        paragraph = True
                    elif length > 1:
                        html_file.write('<br/>\n')
                    elif paragraph:
                        html_file.write('</p>\n')
                        paragraph = False

                # Write the line to the HTML file
                if length > 1:
                    html_file.write(line)

            # Close remaining HTML tags
            if ordered_status:
                html_file.write('</ol>\n')
            if paragraph:
                html_file.write('</p>\n')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)
    convert_markdown_to_html(sys.argv[1], sys.argv[2])
    sys.exit(0)
