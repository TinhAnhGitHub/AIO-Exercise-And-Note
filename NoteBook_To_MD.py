import nbformat
from nbconvert import MarkdownExporter
import sys
import os

def convert_ipynb_to_md(input_path, output_path=None):
    try:
        # Read the notebook
        with open(input_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)

        # Create the exporter
        markdown_exporter = MarkdownExporter()

        # Convert the notebook to markdown
        body, _ = markdown_exporter.from_notebook_node(nb)

        # Write the markdown to a file
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + '.md'
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(body)

        print(f"Successfully converted {input_path} to Markdown.")
        print(f"Output file: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input_notebook.ipynb [output_file.md]")
    elif len(sys.argv) == 2:
        convert_ipynb_to_md(sys.argv[1])
    else:
        convert_ipynb_to_md(sys.argv[1], sys.argv[2])