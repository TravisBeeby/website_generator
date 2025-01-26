class TextType:
    TEXT = "text"
    CODE = "code"
    BOLD = "bold"
    ITALIC = "italic"

class TextNode:
    def __init__(self, text, text_type):
        self.text = text
        self.text_type = text_type

    def __repr__(self):
        return f'TextNode("{self.text}", TextType.{self.text_type.upper()})'

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception(f"Unmatched delimiter '{delimiter}' found in node: {node.text}")

        for i, part in enumerate(parts):
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

# Tests
def test_split_nodes_delimiter():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    assert new_nodes == [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
    ]

    node = TextNode("Text with **bold** and *italic* and `code`", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    assert new_nodes == [
        TextNode("Text with ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" and ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode("", TextType.TEXT),
    ]

    node = TextNode("Unmatched **bold", TextType.TEXT)
    try:
        split_nodes_delimiter([node], "**", TextType.BOLD)
        assert False, "Exception expected"
    except Exception as e:
        assert str(e) == "Unmatched delimiter '**' found in node: Unmatched **bold"

    print("All tests passed!")

# Run tests
test_split_nodes_delimiter()
