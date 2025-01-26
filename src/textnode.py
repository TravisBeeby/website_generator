from enum import Enum
from htmlnode import LeafNode  # Add this import statement

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6
    UNDERLINE = 7

class TextNode:
    def __init__(self, type, text, url=None, alt_text=None):
        self.type = type
        self.text = text
        self.url = url
        self.alt_text = alt_text
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.type == other.type and self.text == other.text and 
                self.url == other.url and self.alt_text == other.alt_text)

def text_node_to_html_node(text_node):
    if text_node.type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.type == TextType.LINK:
        if not text_node.url:
            raise ValueError("URL must be provided for LINK type")
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.type == TextType.IMAGE:
        if not text_node.url or not text_node.alt_text:
            raise ValueError("Both URL and alt_text must be provided for IMAGE type")
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.alt_text})
    else:
        raise ValueError("Unsupported TextType")
