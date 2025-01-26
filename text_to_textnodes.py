def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.TEXT)
    nodes = [initial_node]

    # Split nodes by images
    nodes = split_nodes_image(nodes)
    # Split nodes by links
    nodes = split_nodes_link(nodes)
    # Split nodes by bold text
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    # Split nodes by italic text
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    # Split nodes by code blocks
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes

# Tests
def test_text_to_textnodes():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    expected_output = [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
    ]
    assert text_to_textnodes(text) == expected_output

    text = "Plain text without any special formatting."
    expected_output = [TextNode("Plain text without any special formatting.", TextType.TEXT)]
    assert text_to_textnodes(text) == expected_output

    text = "This is **bold** and *italic* and `code`"
    expected_output = [
        TextNode("This is ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" and ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode("", TextType.TEXT)
    ]
    assert text_to_textnodes(text) == expected_output

    print("All tests passed!")

# Run tests
test_text_to_textnodes()
