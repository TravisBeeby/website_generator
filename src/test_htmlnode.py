import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode  # Replace 'your_module_name' with the actual module name

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node(self):
        text_node = TextNode(TextType.TEXT, "Normal text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Normal text")

    def test_bold_node(self):
        text_node = TextNode(TextType.BOLD, "Bold text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_italic_node(self):
        text_node = TextNode(TextType.ITALIC, "Italic text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_code_node(self):
        text_node = TextNode(TextType.CODE, "Code text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")

    def test_link_node(self):
        text_node = TextNode(TextType.LINK, "Anchor text", url="http://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="http://example.com">Anchor text</a>')

    def test_image_node(self):
        text_node = TextNode(TextType.IMAGE, "", url="http://example.com/image.jpg", alt_text="An image")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="http://example.com/image.jpg" alt="An image" />')

    def test_unsupported_text_type(self):
        text_node = TextNode("unsupported_type", "Unsupported text")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

if __name__ == '__main__':
    unittest.main()
