import os
import re
import shutil
import markdown
from custom_markdown_extension import CustomExtension

def delete_public_directory():
    if os.path.exists('public'):
        shutil.rmtree('public')
        print("Deleted everything in the public directory.")
    else:
        print("Public directory does not exist.")

def copy_static_to_public():
    if os.path.exists('static'):
        shutil.copytree('static', 'public/static')
        print("Copied static files to public directory.")
    else:
        print("Static directory does not exist.")

def extract_title(markdown_content):
    match = re.match(r'^# (.+)', markdown_content.strip())
    if match:
        return match.group(1).strip()
    else:
        raise Exception("No h1 header found")

def markdown_to_html_node(markdown_content):
    return markdown.markdown(markdown_content, extensions=[CustomExtension()])

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    with open(template_path, 'r', encoding='utf-8') as file:
        template_content = file.read()

    html_content = markdown_to_html_node(markdown_content)
    title = extract_title(markdown_content)
    html_page = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(html_page)

    print(f"Page generated successfully at {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, relative_path).replace('.md', '.html')
                generate_page(from_path, template_path, dest_path)

def main():
    delete_public_directory()
    copy_static_to_public()
    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == "__main__":
    main()
