import re

class TextType:
    TEXT = "text"
    CODE = "code"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __repr__(self):
        return f'TextNode("{self.text}", TextType.{self.text_type.upper()}{", " + repr(self.url) if self.url else ""})'

def extract_markdown_images(text):
    pattern = r'!

\[([^\]

]+)\]

\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r'

\[([^\]

]+)\]

\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(node)
            continue

        for alt_text, url in images:
            parts = text.split(f"![{alt_text}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            text = parts[1] if len(parts) > 1 else ""

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue

        for anchor_text, url in links:
            parts = text.split(f"[{anchor_text}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            text = parts[1] if len(parts) > 1 else ""

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

# Tests
def test_split_nodes_image():
    node = TextNode("This is text with an ![image](https://example.com/image.png) and more text", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    assert new_nodes == [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
        TextNode(" and more text", TextType.TEXT)
    ]
    
    node = TextNode("No images here!", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    assert new_nodes == [node]
    
    node = TextNode("![alt text](https://example.com/image.png)", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    assert new_nodes == [
        TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")
    ]
    
    print("All image tests passed!")

def test_split_nodes_link():
    node = TextNode("This is text with a [link](https://example.com) and more text", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    assert new_nodes == [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://example.com"),
        TextNode(" and more text", TextType.TEXT)
    ]
    
    node = TextNode("No links here!", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    assert new_nodes == [node]
    
    node = TextNode("[link](https://example.com)", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    assert new_nodes == [
        TextNode("link", TextType.LINK, "https://example.com")
    ]
    
    print("All link tests passed!")

# Run tests
test_split_nodes_image()
test_split_nodes_link()
