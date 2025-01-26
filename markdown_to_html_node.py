class HTMLNode:
    def __init__(self, tag, children=None, text=None):
        self.tag = tag
        self.children = children if children is not None else []
        self.text = text

    def __repr__(self):
        return f'HTMLNode("{self.tag}", {self.children}, "{self.text}")'

def markdown_to_html_node(markdown):
    def text_to_children(text):
        nodes = text_to_textnodes(text)
        html_nodes = []
        for node in nodes:
            if node.text_type == TextType.TEXT:
                html_nodes.append(HTMLNode("span", text=node.text))
            elif node.text_type == TextType.BOLD:
                html_nodes.append(HTMLNode("strong", text=node.text))
            elif node.text_type == TextType.ITALIC:
                html_nodes.append(HTMLNode("em", text=node.text))
            elif node.text_type == TextType.CODE:
                html_nodes.append(HTMLNode("code", text=node.text))
            elif node.text_type == TextType.IMAGE:
                img_node = HTMLNode("img", text=node.text)
                img_node.src = node.url
                html_nodes.append(img_node)
            elif node.text_type == TextType.LINK:
                link_node = HTMLNode("a", text=node.text)
                link_node.href = node.url
                html_nodes.append(link_node)
        return html_nodes

    blocks = markdown_to_blocks(markdown)
    parent_node = HTMLNode("div")

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            level = block.count('#')
            tag = f'h{level}'
            text = block[level+1:].strip()
            parent_node.children.append(HTMLNode(tag, text=text))
        elif block_type == "code block":
            code_content = block[3:-3].strip()
            code_node = HTMLNode("code", text=code_content)
            pre_node = HTMLNode("pre", children=[code_node])
            parent_node.children.append(pre_node)
        elif block_type == "quote block":
            quote_node = HTMLNode("blockquote", children=text_to_children(block.replace("> ", "")))
            parent_node.children.append(quote_node)
        elif block_type == "unordered list block":
            ul_node = HTMLNode("ul")
            for line in block.split('\n'):
                item_text = line[2:].strip()
                ul_node.children.append(HTMLNode("li", children=text_to_children(item_text)))
            parent_node.children.append(ul_node)
        elif block_type == "ordered list block":
            ol_node = HTMLNode("ol")
            for line in block.split('\n'):
                item_text = line[3:].strip()
                ol_node.children.append(HTMLNode("li", children=text_to_children(item_text)))
            parent_node.children.append(ol_node)
        else:
            parent_node.children.append(HTMLNode("p", children=text_to_children(block)))

    return parent_node

# Tests
def test_markdown_to_html_node():
    markdown = """
    # Heading

    This is a paragraph with **bold** text and *italic* text.

    ```
    Code block
    ```

    > This is a quote block.

    * List item 1
    * List item 2

    1. Ordered item 1
    2. Ordered item 2
    """
    
    expected_output = HTMLNode("div", [
        HTMLNode("h1", text="Heading"),
        HTMLNode("p", [
            HTMLNode("span", text="This is a paragraph with "),
            HTMLNode("strong", text="bold"),
            HTMLNode("span", text=" text and "),
            HTMLNode("em", text="italic"),
            HTMLNode("span", text=" text.")
        ]),
        HTMLNode("pre", [HTMLNode("code", text="Code block")]),
        HTMLNode("blockquote", [HTMLNode("span", text="This is a quote block.")]),
        HTMLNode("ul", [
            HTMLNode("li", [HTMLNode("span", text="List item 1")]),
            HTMLNode("li", [HTMLNode("span", text="List item 2")])
        ]),
        HTMLNode("ol", [
            HTMLNode("li", [HTMLNode("span", text="Ordered item 1")]),
            HTMLNode("li", [HTMLNode("span", text="Ordered item 2")])
        ])
    ])
    
    result = markdown_to_html_node(markdown)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    print("All tests passed!")

# Run tests
test_markdown_to_html_node()
