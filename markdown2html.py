def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts Markdown to HTML.

    Args:
        markdown_file (str): Name of the Markdown file.
        output_file (str): Name of the output HTML file.
    """
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and process headings
    with open(markdown_file, 'r') as f:
        lines = f.readlines()

    # Process each line
    output_lines = []
    for line in lines:
        line = line.rstrip('\n')

        # Check for heading syntax and convert to HTML
        if line.startswith('# '):
            output_lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith('## '):
            output_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith('### '):
            output_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith('#### '):
            output_lines.append(f"<h4>{line[5:]}</h4>")
        elif line.startswith('##### '):
            output_lines.append(f"<h5>{line[6:]}</h5>")
        elif line.startswith('###### '):
            output_lines.append(f"<h6>{line[7:]}</h6>")
        else:
            output_lines.append(line)

    # Write the HTML output
    with open(output_file, 'w') as output:
        output.write('\n'.join(output_lines))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Extracting the filename without extension from sys.argv[2]
    fn_no_extension = os.path.splitext(sys.argv[2])[0]

    # Using the correct HTML filename when opening for reading
    fn_html = f"{fn_no_extension}.html"

    try:
        with open(fn_html, "r") as f:
            pass
    except FileNotFoundError:
        print("FileNotFoundError: [Errno 2] No such file or directory:", repr(fn_html))
        sys.exit(1)
    sys.exit(0)
