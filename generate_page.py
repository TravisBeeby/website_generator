import os
import re
import shutil
import markdown

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
    return markdown.markdown(markdown_content)

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

def main():
    delete_public_directory()
    copy_static_to_public()
    generate_page('content/index.md', 'template.html', 'public/index.html')

if __name__ == "__main__":
    main()
