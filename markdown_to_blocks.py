def markdown_to_blocks(markdown):
    # Split the markdown text into blocks using two or more newlines as delimiters
    blocks = markdown.strip().split('\n\n')

    # Strip leading and trailing whitespace from each block and remove empty blocks
    cleaned_blocks = [block.strip() for block in blocks if block.strip()]

    return cleaned_blocks

# Tests
def test_markdown_to_blocks():
    markdown = """
    # This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    * This is the first list item in a list block
    * This is a list item
    * This is another list item
    """
    
    expected_output = [
        "# This is a heading",
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    ]
    
    assert markdown_to_blocks(markdown) == expected_output

    markdown = """
    This is a paragraph with a [link](https://example.com).

    ![An image](https://example.com/image.jpg)
    """
    
    expected_output = [
        "This is a paragraph with a [link](https://example.com).",
        "![An image](https://example.com/image.jpg)"
    ]
    
    assert markdown_to_blocks(markdown) == expected_output

    markdown = """
    No excessive

    newlines here
    """
    
    expected_output = [
        "No excessive",
        "newlines here"
    ]
    
    assert markdown_to_blocks(markdown) == expected_output

    print("All tests passed!")

# Run tests
test_markdown_to_blocks()
