#!/usr/bin/python3
"""
Parse a Markdown file and turns into HTML
"""
import sys


def unlist(lines):
    """Gives ul tags to lines and wraps with <ul>"""
    wrap = ["<ul>\n",]

    for item in lines:
        text = item.replace('-', '')
        text.strip()
        wrap.append(f"<li>{text.strip()}</li>\n")

    wrap.append("</ul>\n")
    return "".join(wrap)


def headings(lines):
    """Gives heading tags to lines"""
    wrap = []

    for item in lines:
        lvl = item.count('#')
        text = item.replace('#', '')
        wrap.append(f"<h{lvl}>{text.strip()}</h{lvl}>\n")

    return "".join(wrap)


def read_file(src, dest):
    """
    Parse Markdown and save as HTML.

    Each line is gonna be wrapped by its own specific tag function
    and returned as a string saved on @render list, then each item
    on render is gonna be written in @dest as a string.

    Args:
        src (str): Source file.
        dest (str): Destination of source file.
    """
    fun_dic = {'#': headings, '-': unlist}

    render = []

    try:
        with open(src, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        sys.stderr.write(f"Missing {src}\n")
        sys.exit(1)

    for mark in fun_dic:
        aux = [line for line in content.split('\n') if mark in line]
        render.append(fun_dic.get(mark)(aux))

    with open(dest, 'w', encoding='utf-8') as to_html:
        for line in render:
            to_html.write("".join(line))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)

    read_file(sys.argv[1], sys.argv[2])
    sys.exit(0)
